import 'loading_page.dart';
import 'package:flutter/material.dart';
class Splash extends StatefulWidget {
  const Splash({Key? key}) : super(key: key);

  @override
  State<Splash> createState() => _SplashState();
}
class _SplashState extends State<Splash> {
  // @override
  // // void initState(){
  // //   super.initState();
  // //   _navigatetohome();
  // // }

  _navigatetohome() async{
    await Future.delayed(Duration(milliseconds: 3500),(){});
    Navigator.pushReplacement(context, MaterialPageRoute(builder:(context)=>Loader() ));
  }
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: FutureBuilder(
            builder: (context,snapshot){
          return Container(
            decoration: BoxDecoration(
              image: DecorationImage(image: AssetImage("images/splash.jpg"),fit: BoxFit.cover),
            ),
          );
        },
        future: Future.delayed(const Duration(seconds: 1),(){
          return _navigatetohome();
    },)
      ),
    ));
  }
}

