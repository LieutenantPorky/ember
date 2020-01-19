import 'package:flutter/material.dart';
import 'package:flutter/semantics.dart';
import 'package:tinder_card/tinder_card.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

class Homescreen extends StatefulWidget {
  Homescreen({Key key}) : super(key: key);

  @override
  HomescreenState createState() => HomescreenState();
}

class HomescreenState extends State<Homescreen> {
  Future<List<String>> photos;

  @override
  void initState() {
    super.initState();
    photos = load();
  }

  Future<List<String>> load() async {
    final response = await http.get("http://127.0.0.1:8080/photos/1");
    List<String> rt = json.decode(response.body)["photos"][0].map<String>((e) {
      return "http://127.0.0.1:8080" + e;
    }).toList();
    print(rt);
    return rt;
  }

  @override
  Widget build(BuildContext context) {
    return FutureBuilder(
        future: photos,
        builder: (ctx, future) {
          if (future.hasData) {
            demoProfiles.insert(0, Profile(bio: "added", name: "Tigi", photos: future.data));
            return TinderSwapCard(
              demoProfiles: demoProfiles,
              myCallback: (decision) {
                print(decision);
              },
            );
          } else {
            return CircularProgressIndicator();
          }
        });
  }
}

class Profile {
  final List<String> photos;
  final String name;
  final String bio;

  Profile({this.photos, this.name, this.bio});
}

final List<Profile> demoProfiles = [
  new Profile(
    photos: [
      // URL's for the profiles
      "http://127.0.0.1:8080/static/11b027e19ed473fd28f1eabb0431726501b7125c",
      "https://www.petmd.com/sites/default/files/adult-homeless-cat-asking-for-food-picture-id847415388.jpg",
      "https://www.petmd.com/sites/default/files/adult-homeless-cat-asking-for-food-picture-id847415388.jpg",
      "https://www.petmd.com/sites/default/files/adult-homeless-cat-asking-for-food-picture-id847415388.jpg",
    ],
    name: "Master",
    bio: "Want some good quality pussy?",
  ),
  new Profile(
    photos: [
      "https://www.petmd.com/sites/default/files/adult-homeless-cat-asking-for-food-picture-id847415388.jpg",
      "https://www.petmd.com/sites/default/files/adult-homeless-cat-asking-for-food-picture-id847415388.jpg",
      "https://www.petmd.com/sites/default/files/adult-homeless-cat-asking-for-food-picture-id847415388.jpg",
      "https://www.petmd.com/sites/default/files/adult-homeless-cat-asking-for-food-picture-id847415388.jpg",
    ],
    name: "Master",
    bio: "Want some good quality pussy?",
  )
];
