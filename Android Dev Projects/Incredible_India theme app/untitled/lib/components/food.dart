import 'package:flutter/material.dart';
import 'package:untitled/main.dart';
import 'requirements.dart';

class Food{
  int count=0;
  List<Requirement> _food=[
    Requirement(1,"SAMOSA","images/f1.jpg"),
    Requirement(2,"MASALA CHAI","images/f2.jpg"),
    Requirement(3,"DHOKLA","images/f3.jpg"),
    Requirement(4,"VADA PAV","images/f4.jpg"),
    Requirement(5,"CHANA MASALA","images/f5.jpg"),
    Requirement(6,"THALI","images/f6.jpg"),
    Requirement(7,"BIRYANI","images/f7.jpg"),
    Requirement(8,"MASALA DOSA","images/f8.jpg"),
    Requirement(9,"INDIAN CHAATS","images/f9.jpg"),
    Requirement(10,"GULAB JAMUN","images/f10.jpg"),
  ];
  int NoOfFood()
  {
    return _food.length;
  }
  String getFoodImage(int count){
    return _food[count].image;
  }
  String getFoodName(int count)
  {
    return _food[count].name;
  }
  void next()
  {
    count++;
  }

}