import './user_model.dart';

class Message {
  final User sender;
  final String
      time; // Would usually be type DateTime or Firebase Timestamp in production apps
  final String text;
  final bool isLiked;
  final bool unread;

  Message({
    this.sender,
    this.time,
    this.text,
    this.isLiked,
    this.unread,
  });
}

// YOU - current user
final User currentUser = User(
  id: 0,
  name: 'Current User',
  imageUrl: 'assets/images/zucc2.jpg',
);

// USERS
final User zucc = User(
  id: 1,
  name: 'The Zucc',
  imageUrl: 'assets/images/zucc2.jpeg',
);
final User james = User(
  id: 2,
  name: 'James',
  imageUrl: 'assets/images/a.jpeg',
);
final User john = User(
  id: 3,
  name: 'John',
  imageUrl: 'assets/images/c.jpeg',
);
final User olivia = User(
  id: 4,
  name: 'Olivia',
  imageUrl: 'assets/images/b.jpeg',
);
final User sam = User(
  id: 5,
  name: 'Sam',
  imageUrl: 'assets/images/e.jpeg',
);
final User sophia = User(
  id: 6,
  name: 'Sophia',
  imageUrl: 'assets/images/g.jpeg',
);
final User steven = User(
  id: 7,
  name: 'Steven',
  imageUrl: 'assets/images/f.jpeg',
);

// FAVORITE CONTACTS
List<User> favorites = [sam, steven, olivia, john, zucc];

// EXAMPLE CHATS ON HOME SCREEN
List<Message> chats = [
  Message(
    sender: zucc,
    time: '11:30 AM',
    text: 'Hey baby, you heard of facebook?',
    isLiked: false,
    unread: false,
  ),
  Message(
    sender: james,
    time: '5:30 PM',
    text: 'Hey, how\'s it going? What did you do today?',
    isLiked: false,
    unread: true,
  ),
  Message(
    sender: olivia,
    time: '4:30 PM',
    text: 'Hey, You wanna have some fun tonight?',
    isLiked: false,
    unread: true,
  ),
  Message(
    sender: john,
    time: '3:30 PM',
    text: 'I\'ve never tried that ;)',
    isLiked: false,
    unread: false,
  ),
  Message(
    sender: sophia,
    time: '2:30 PM',
    text: 'I do computer science!',
    isLiked: false,
    unread: true,
  ),
  Message(
    sender: steven,
    time: '1:30 PM',
    text: 'FUCK, you\'re so fucking hot WTF',
    isLiked: false,
    unread: false,
  ),
  Message(
    sender: sam,
    time: '12:30 PM',
    text: 'You look so good aaaaaaa',
    isLiked: false,
    unread: false,
  ),
];

// EXAMPLE MESSAGES IN CHAT SCREEN
List<Message> messages = [
  Message(
    sender: james,
    time: '5:30 PM',
    text: 'What do you say? ;)',
    isLiked: false,
    unread: true,
  ),
  Message(
    sender: currentUser,
    time: '4:30 PM',
    text: 'Excuse me??',
    isLiked: true,
    unread: true,
  ),
  Message(
    sender: james,
    time: '3:45 PM',
    text: 'Let me put it in your \"USB\" slot baby ;)',
    isLiked: false,
    unread: true,
  ),
  Message(
    sender: james,
    time: '3:15 PM',
    text: 'Hmmmm, how about a favour?',
    isLiked: false,
    unread: true,
  ),
  Message(
    sender: currentUser,
    time: '2:30 PM',
    text: 'I don\'t know, you\'re The Zucc. You tell me.',
    isLiked: false,
    unread: true,
  ),
  Message(
    sender: james,
    time: '2:00 PM',
    text: 'So, how did I end up matching with someone like you?',
    isLiked: true,
    unread: true,
  ),
];
