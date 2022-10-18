import 'package:flutter/material.dart';
import 'package:untitled/constants.dart';
import '../components/desc.dart';
import 'package:flutter_custom_clippers/flutter_custom_clippers.dart';
class Description extends StatefulWidget {
  Description(@required this.name,@required this.image);
  String name,image;
  @override
  State<Description> createState() => _DescriptionState();
}

class _DescriptionState extends State<Description> {
  Desc data=Desc();
  @override
  Widget build(BuildContext context) {
    Size size=MediaQuery.of(context).size;
    return Scaffold(
      appBar: AppBar(
        elevation: 0,
        backgroundColor: Colors.indigo,
        foregroundColor: Colors.white,
        centerTitle: true,
        title: Text("${widget.name}"),
      ),
      body: SingleChildScrollView(
        child: Column(
          //mainAxisAlignment: MainAxisAlignment.start,
          children: [
            ClipPath(
              clipper: OvalBottomBorderClipper(),
              child: Container(
                height: size.height*0.30,
                decoration: BoxDecoration(
                  image: DecorationImage(image: AssetImage("${widget.image}"),fit: BoxFit.fitWidth),
                ),
              ),
            ),
            SizedBox(
              height: size.height*0.05,
            ),
            Padding(
              padding: const EdgeInsets.all(20.0),
              child: Text(data.getData("${widget.name}"),style: kTextDescription),
            ),
          ],
        ),
      ),
    );
  }
}

