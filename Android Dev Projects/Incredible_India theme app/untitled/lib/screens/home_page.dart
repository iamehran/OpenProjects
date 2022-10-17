import 'package:flutter/material.dart';
import '../components/items.dart';
import 'package:untitled/constants.dart';

import '../components/selectedIndex.dart';
class home extends StatefulWidget {
  const home({Key? key}) : super(key: key);
  @override
  State<home> createState() => _homeState();
}

class _homeState extends State<home> {
  int selectedIndex=0;
  List<String> categories=["Destinations","Food","Nature"];
  @override
  Widget build(BuildContext context) {
    return  SafeArea(
      child: Scaffold(
        appBar: AppBar(
          title: Text('INCREDIBLE INDIA!'),
          centerTitle: true,
          foregroundColor: Colors.white,
          backgroundColor: Colors.indigo,
        ),
        body: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Padding(padding: const EdgeInsets.symmetric(vertical: 20),
              child: SizedBox(
                height: 25,
                child: ListView.builder(
                    itemCount: categories.length,
                    scrollDirection: Axis.horizontal,
                    itemBuilder: (context,index){return
                      GestureDetector(
                        onTap: (){
                          setState(() {
                            selectedIndex=index;
                            Index.updateIndex(selectedIndex);
                          });
                        },
                        child: Padding(
                          padding: const EdgeInsets.symmetric(horizontal: 40),
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.center,
                            children: [
                              Text(categories[index],style:TextStyle(
                                fontWeight: FontWeight.bold,
                                color:selectedIndex==index ? kTextColor : kTextLightColor,
                              ),),
                              Container(
                                margin:EdgeInsets.only(top: 5),
                                height: 2,
                                width: 30,
                                color: selectedIndex==index?Colors.green:Colors.transparent,
                              )
                            ],
                          ),
                        ),
                      );}),
              ),),
            Expanded(
              flex: 1,
              child: items(),
            ),
          ],
        ),
      ),
    );
  }
}
