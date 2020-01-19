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
  Future<List<Profile>> profiles;

  @override
  void initState() {
    super.initState();
    profiles = load();
  }

  Future<List<Profile>> load() async {
    final response = await http.get("http://127.0.0.1:8080/soulmate/Bob");
    final matches = json.decode(response.body);
    final profiles = <Profile>[];

    for (dynamic match in matches) {
      print(match[0]["pictures"]);
      final photos = <String>[];

      for (dynamic pic in match[0]["pictures"]) {
        print(pic["hash"]);
        photos.add("http://127.0.0.1:8080/static/" + pic["hash"]);
      }
      if (photos.length > 0) {
        profiles
            .add(Profile(name: match[0]["username"], bio: "", photos: photos));
      }
    }
    // List<String> rt = json.decode(response.body)["photos"][0].map<String>((e) {
    // return "http://127.0.0.1:8080" + e;
    // }).toList();
    print(profiles);
    // return rt;
    return profiles;
  }

  @override
  Widget build(BuildContext context) {
    return FutureBuilder(
        future: profiles,
        builder: (ctx, future) {
          if (future.hasData) {
            List<Profile> profiles = future.data;

            profiles.addAll(demoProfiles);

            return TinderSwapCard(
              demoProfiles: profiles,
              myCallback: (decision) {
                print(decision);
              },
            );
          } else {
            return Center(child: CircularProgressIndicator());
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
