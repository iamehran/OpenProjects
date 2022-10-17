import 'package:flutter/material.dart';
import 'package:untitled/main.dart';
import 'requirements.dart';

class Nature{
  int count=0;
  List<Requirement> _nature=[
    Requirement(1,"KUMARAKOM","images/n1.jpg"),
    Requirement(2,"LEH","images/n2.jpg"),
    Requirement(3,"PACHMARHI","images/n3.jpg"),
    Requirement(4,"SIMLIPAL","images/n4.jpg"),
    Requirement(5,"KOTAGIRI","images/n5.jpg"),
    Requirement(6,"NALBARI","images/n6.jpg"),
    Requirement(7,"COORG","images/n7.jpeg"),
    Requirement(8,"VALLEY OF FLOWERS","images/n8.jpg"),
    Requirement(9,"MAJULI","images/n9.jpg"),
    Requirement(10,"KORAPUT","images/n10.jpg"),
  ];
  int NoOfNature()
  {
    return _nature.length;
  }
  String getNatureImage(int count){
    return _nature[count].image;
  }
  String getNatureName(int count)
  {
    return _nature[count].name;
  }
  void next()
  {
    count++;
  }

}