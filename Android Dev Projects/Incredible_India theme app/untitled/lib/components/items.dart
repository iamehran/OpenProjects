import 'package:flutter/material.dart';
import 'package:untitled/components/food.dart';
import 'package:untitled/components/nature.dart';
import 'package:untitled/components/selectedIndex.dart';
import 'itemCard.dart';
import 'destinations.dart';
class items extends StatefulWidget {
  items();

  @override
  State<items> createState() => _itemsState();
}

class _itemsState extends State<items> {
  int selectedIndex=0;
  Destination destination = Destination();
  Food food=Food();
  Nature nature=Nature();


  @override
  Widget build(BuildContext context) {
    return GridView.builder(
      primary: false,
      padding: const EdgeInsets.symmetric(horizontal: 20, vertical: 20),
      gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(
        crossAxisSpacing: 10,
        mainAxisSpacing: 10,
        crossAxisCount: 2,
        childAspectRatio: 0.90,
      ),
      itemCount: destination.NoOfPlaces(),
      itemBuilder: (context,int index){
        switch(Index.getIndexi())
        {
          case 0:return ICard((index));
          case 1: return ICard((index));
          case 2: return ICard((index));
          default:return ICard((index));
        }
      },
    );
  }
}
