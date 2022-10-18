import 'package:flutter/material.dart';
import 'package:untitled/main.dart';
import 'requirements.dart';

class Destination{
  int count=0;
  List<Requirement> _places=[
    Requirement(1,"MUNNAR KERALA","images/i1.jpg"),
    Requirement(2,"BELUR TEMPLE","images/i2.jpg"),
    Requirement(3,"TAJ MAHAL","images/i3.jpg"),
    Requirement(4,"RANN OF KUTCH","images/i4.jpg"),
    Requirement(5,"VARANASI","images/i5.jpg"),
    Requirement(6,"ANDAMAN ISLANDS","images/i6.jpg"),
    Requirement(7,"SIBSAGAR","images/i7.jpg"),
    Requirement(8,"UDAIPUR","images/i8.jpg"),
    Requirement(9,"KANYA KUMARI","images/i9.jpg"),
    Requirement(10,"LAKSHADWEEP","images/i10.jpg"),
  ];
  int NoOfPlaces()
  {
    return _places.length;
  }
  String getPlaceImage(int count){
    return _places[count].image;
  }
  String getPlaceName(int count)
  {
    return _places[count].name;
  }
  void next()
  {
    count++;
  }

}