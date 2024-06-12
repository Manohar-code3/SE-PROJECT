// ignore_for_file: unused_import

import 'package:flutter/material.dart';
import 'package:loginuicolors/login.dart';
import 'package:loginuicolors/register.dart';
import 'package:loginuicolors/mic.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:cloud_firestore/cloud_firestore.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp(
    options: const FirebaseOptions(
      apiKey: "AIzaSyAK2FLI05KG4NHCZxlhauxIux7vvK-AxpQ",
      appId: "1:936071446332:android:d2df743ecd974b5783a839",
      messagingSenderId: "936071446332",
      projectId: "voice-auto-5830f",
    ),
  );
  runApp(MaterialApp(
    debugShowCheckedModeBanner: false,
    home: const LoginScreen(),
    routes: {
      'register': (context) => const MyRegister(),
      'login': (context) => const LoginScreen(),
      'mic': (context) => MicScreen(),
    },
  ));
}
