import 'package:flutter/material.dart';
import 'package:flutter_spinkit/flutter_spinkit.dart';
import 'package:untitled/screens/home_page.dart';
class Loader extends StatefulWidget {
  const Loader({Key? key}) : super(key: key);

  @override
  State<Loader> createState() => _LoaderState();
}

class _LoaderState extends State<Loader> {
  _tohome() async {
    await Future.delayed(Duration(milliseconds: 3500), () {});
    Navigator.pushReplacement(
        context, MaterialPageRoute(builder: (context) => home()));
  }

  @override
  Widget build(BuildContext context) {
    return FutureBuilder(builder: (context, snapshot) {
      return
        Scaffold(
            body: SpinKitRipple(
              color: Colors.orange, duration: Duration(milliseconds: 2000),
              size: 200,
            )
        );
    },
      future: Future.delayed(const Duration(seconds: 1), () {
        return _tohome();
      }),);
  }
}
