import 'package:flutter/material.dart';
import 'package:untitled/components/selectedIndex.dart';
import 'package:untitled/screens/description_page.dart';
import '../constants.dart';
import 'destinations.dart';
import 'food.dart';
import 'nature.dart';
class ICard extends StatelessWidget {
ICard(@required this.c);
  Destination destination=Destination();
Food food=Food();
Nature nature=Nature();
  final c;
  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisAlignment: MainAxisAlignment.center,
      crossAxisAlignment: CrossAxisAlignment.center,
      children: [
        GestureDetector(
          onTap: () {
            switch(Index.getIndexi())
            {
              case 0: Navigator.push(context,MaterialPageRoute(builder:(context)=> Description(buildPlaceName(),destination.getPlaceImage(c))) );
              break;
              case 1: Navigator.push(context,MaterialPageRoute(builder:(context)=> Description(food.getFoodName(c),food.getFoodImage(c))) );
              break;
              case 2: Navigator.push(context,MaterialPageRoute(builder:(context)=> Description(nature.getNatureName(c),nature.getNatureImage(c))) );
              break;
            }
          },
          child: Container(
            height: 150,
            width: 150,
            decoration: BoxDecoration(borderRadius: BorderRadius.circular(5),
              image: DecorationImage(
                  image: buildAssetImage(),fit: BoxFit.cover),
            ),
          ),
        ),
        SizedBox(
          height: 5,
        ),
        Text(buildPlaceName(),style: kTextStyle,),
      ],
    );
  }

  String buildPlaceName() {
    switch(Index.getIndexi())
    {
      case 0: return destination.getPlaceName(c);
      case 1: return food.getFoodName(c);
      case 2: return nature.getNatureName(c);
    }
    return destination.getPlaceName(c);
  }

  AssetImage buildAssetImage() {
    switch(Index.getIndexi())
    {
      case 0: return AssetImage(destination.getPlaceImage(c));
      case 1: return AssetImage(food.getFoodImage(c));
      case 2: return AssetImage(nature.getNatureImage(c));
    }
    return AssetImage(destination.getPlaceImage(c));
  }
}

