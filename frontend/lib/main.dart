import 'package:flutter/material.dart';
import 'package:tinder_card/tinder_card.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        // This is the theme of your application.
        //
        // Try running your application with "flutter run". You'll see the
        // application has a blue toolbar. Then, without quitting the app, try
        // changing the primarySwatch below to Colors.green and then invoke
        // "hot reload" (press "r" in the console where you ran "flutter run",
        // or simply save your changes to "hot reload" in a Flutter IDE).
        // Notice that the counter didn't reset back to zero; the application
        // is not restarted.
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key key, this.title}) : super(key: key);

  // This widget is the home page of your application. It is stateful, meaning
  // that it has a State object (defined below) that contains fields that affect
  // how it looks.

  // This class is the configuration for the state. It holds the values (in this
  // case the title) provided by the parent (in this case the App widget) and
  // used by the build method of the State. Fields in a Widget subclass are
  // always marked "final".

  final String title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  //index for bottom navigation index 
  int _currentIndex = 1;
  final List<Widget> _children = [
    PlaceholderWidget(Colors.white),
    Homescreen(),
    PlaceholderWidget(Colors.green)
  ];
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Fuck me')
      ),
      body: _children[_currentIndex],
        bottomNavigationBar: BottomNavigationBar(
        items: const <BottomNavigationBarItem>[
          BottomNavigationBarItem(
            icon: Icon(Icons.person),
            title: Text('Profile'),
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.whatshot),
            title: Text('Ember'),
          ),
          BottomNavigationBarItem(
            icon: Icon(Icons.chat),
            title: Text('Chats'),
          ),
        ],
        currentIndex: _currentIndex,
        onTap: onTabTapped,
      // : () {
      //   Navigator.push(context, MaterialPageRoute(builder: (context){
      //     return Chatpage();
      //   }));
      // }
    ), // This trailing comma makes auto-formatting nicer for build methods.
    );
  }
  void onTabTapped(int index) {
   setState(() {
     _currentIndex = index;
   });
 }
}

class PlaceholderWidget extends StatelessWidget {
 final Color color;

 PlaceholderWidget(this.color);

 @override
 Widget build(BuildContext context) {
   return Container(
     color: color,
   );
 }
}
class Homescreen extends StatelessWidget {
 @override
 Widget build(BuildContext context) {
   return Scaffold(
      body: TinderSwapCard(
        demoProfiles: demoProfiles,
        myCallback: (decision) {
          print(decision);
          },
        ),
   );
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
      "https://www.petmd.com/sites/default/files/adult-homeless-cat-asking-for-food-picture-id847415388.jpg",
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



