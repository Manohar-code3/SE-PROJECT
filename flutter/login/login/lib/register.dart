// ignore_for_file: unused_import

import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:loginuicolors/login.dart';

class MyRegister extends StatefulWidget {
  const MyRegister({Key? key}) : super(key: key);

  @override
  _MyRegisterState createState() => _MyRegisterState();
}

class _MyRegisterState extends State<MyRegister> {
  final nameController = TextEditingController(text: '');
  final emailController = TextEditingController(text: '');
  final passwordController = TextEditingController(text: '');

  Future<void> _registerUser(BuildContext context) async {
    final name = nameController.text;
    final email = emailController.text;
    final password = passwordController.text;

    if (name.isEmpty || email.isEmpty || password.isEmpty) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('Please fill in all fields')),
      );
      return;
    }

    try {
      // Create user with Firebase Authentication
      final authResult =
          await FirebaseAuth.instance.createUserWithEmailAndPassword(
        email: email,
        password: password,
      );

      final user = authResult.user;
      if (user != null) {
        await _saveUserData(user.uid, name, email);

        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text('User registered successfully!')),
        );

        Navigator.push(
          context,
          MaterialPageRoute(builder: (context) => const LoginScreen()),
        );
      }
    } catch (e) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('Error registering user: $e')),
      );
    }
  }

  Future<void> _saveUserData(String uid, String name, String email) async {
    try {
      final db = FirebaseFirestore.instance;
      final usersRef = db.collection('users');

      // Save user data in Firestore with uid as the document ID
      await usersRef.doc(uid).set({
        'name': name,
        'email': email,
      });

      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('User data saved!')),
      );
    } catch (e) {
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('Error saving user data: $e')),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: const BoxDecoration(
        image: DecorationImage(
          image: AssetImage('assets/register.png'),
          fit: BoxFit.cover,
        ),
      ),
      child: Scaffold(
        backgroundColor: Colors.transparent,
        appBar: AppBar(
          backgroundColor: Colors.transparent,
          elevation: 0,
        ),
        body: Stack(
          children: [
            _buildHeader(),
            _buildForm(context),
          ],
        ),
      ),
    );
  }

  Widget _buildHeader() {
    return Container(
      padding: const EdgeInsets.only(left: 35, top: 30),
      child: const Text(
        'Create\nAccount',
        style: TextStyle(color: Colors.white, fontSize: 33),
      ),
    );
  }

  Widget _buildForm(BuildContext context) {
    return SingleChildScrollView(
      child: Container(
        padding: EdgeInsets.only(
          top: MediaQuery.of(context).size.height * 0.28,
        ),
        child: _buildFormContent(context),
      ),
    );
  }

  Widget _buildFormContent(BuildContext context) {
    return Container(
      margin: const EdgeInsets.symmetric(horizontal: 35),
      child: Column(
        children: [
          _buildTextField(
            controller: nameController,
            hintText: "Name",
          ),
          const SizedBox(height: 30),
          _buildTextField(
            controller: emailController,
            hintText: "Email",
          ),
          const SizedBox(height: 30),
          _buildPasswordTextField(),
          const SizedBox(height: 40),
          _buildSignUpButton(context),
          const SizedBox(height: 40),
          _buildFooter(context),
        ],
      ),
    );
  }

  Widget _buildTextField({
    required TextEditingController controller,
    required String hintText,
  }) {
    return TextField(
      controller: controller,
      style: const TextStyle(color: Colors.white),
      decoration: InputDecoration(
        enabledBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(10),
          borderSide: BorderSide(color: Colors.white),
        ),
        focusedBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(10),
          borderSide: BorderSide(color: Colors.black),
        ),
        hintText: hintText,
        hintStyle: const TextStyle(color: Colors.white),
      ),
    );
  }

  Widget _buildPasswordTextField() {
    return TextField(
      controller: passwordController,
      obscureText: true,
      style: const TextStyle(color: Colors.white),
      decoration: InputDecoration(
        enabledBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(10),
          borderSide: BorderSide(color: Colors.white),
        ),
        focusedBorder: OutlineInputBorder(
          borderRadius: BorderRadius.circular(10),
          borderSide: BorderSide(color: Colors.black),
        ),
        hintText: "Password",
        hintStyle: const TextStyle(color: Colors.white),
      ),
    );
  }

  Widget _buildSignUpButton(BuildContext context) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.spaceBetween,
      children: [
        const Text(
          'Sign Up',
          style: TextStyle(
            color: Colors.white,
            fontSize: 27,
            fontWeight: FontWeight.w700,
          ),
        ),
        CircleAvatar(
          radius: 30,
          backgroundColor: const Color(0xff4c505b),
          child: IconButton(
            color: Colors.white,
            onPressed: () async {
              await _registerUser(context);
            },
            icon: const Icon(Icons.arrow_forward),
          ),
        ),
      ],
    );
  }

  Widget _buildFooter(BuildContext context) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.spaceBetween,
      children: [
        TextButton(
          onPressed: () {
            Navigator.pushNamed(context, 'login');
          },
          child: const Text(
            'Sign In',
            style: TextStyle(
              decoration: TextDecoration.underline,
              color: Colors.white,
              fontSize: 18,
            ),
          ),
        ),
      ],
    );
  }
}
