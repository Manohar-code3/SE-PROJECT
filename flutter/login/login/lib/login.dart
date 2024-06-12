// ignore_for_file: unused_import

import 'package:flutter/material.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:loginuicolors/mic.dart';

class LoginScreen extends StatefulWidget {
  const LoginScreen({Key? key}) : super(key: key);

  @override
  _LoginScreenState createState() => _LoginScreenState();
}

class _LoginScreenState extends State<LoginScreen> {
  final TextEditingController emailController = TextEditingController();
  final TextEditingController passwordController = TextEditingController();
  final GlobalKey<FormState> _formKey = GlobalKey<FormState>();

  Future<void> _signIn(BuildContext context) async {
    if (_formKey.currentState?.validate() ?? false) {
      final email = emailController.text.trim();
      final password = passwordController.text.trim();

      try {
        await FirebaseAuth.instance
            .signInWithEmailAndPassword(email: email, password: password);
        final currentUser = FirebaseAuth.instance.currentUser;
        if (currentUser != null) {
          Navigator.pushNamed(context, 'mic');
        }
      } on FirebaseAuthException catch (e) {
        _showAuthError(context, e);
      } catch (e) {
        _showUnexpectedError(context, e);
      }
    }
  }

  void _showAuthError(BuildContext context, FirebaseAuthException e) {
    String message;
    if (e.code == 'user-not-found') {
      message = "No User Found for that Email";
    } else if (e.code == 'wrong-password') {
      message = "Wrong Password Provided by User";
    } else {
      message = "Authentication error: ${e.message}";
    }

    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        backgroundColor: Colors.orangeAccent,
        content: Text(message, style: const TextStyle(fontSize: 18)),
      ),
    );
  }

  void _showUnexpectedError(BuildContext context, dynamic error) {
    ScaffoldMessenger.of(context).showSnackBar(
      SnackBar(
        backgroundColor: Colors.redAccent,
        content: Text("An unexpected error occurred: $error",
            style: const TextStyle(fontSize: 18)),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Container(
      decoration: BoxDecoration(
        image: DecorationImage(
            image: AssetImage('assets/login.png'), fit: BoxFit.cover),
      ),
      child: Scaffold(
        backgroundColor: Colors.transparent,
        body: Stack(
          children: [
            _buildWelcomeHeader(),
            _buildLoginForm(context),
          ],
        ),
      ),
    );
  }

  Widget _buildWelcomeHeader() {
    return Container(
      padding: const EdgeInsets.only(left: 35, top: 130),
      child: const Text(
        'Welcome\nBack',
        style: TextStyle(color: Colors.white, fontSize: 33),
      ),
    );
  }

  Widget _buildLoginForm(BuildContext context) {
    return SingleChildScrollView(
      child: Container(
        padding: EdgeInsets.only(top: MediaQuery.of(context).size.height * 0.5),
        child: Form(
          key: _formKey,
          child: Column(
            children: [
              _buildEmailField(),
              const SizedBox(height: 30),
              _buildPasswordField(),
              const SizedBox(height: 40),
              _buildSignInButton(context),
              const SizedBox(height: 40),
              _buildFooter(context),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildEmailField() {
    return TextFormField(
      controller: emailController,
      decoration: InputDecoration(
        fillColor: Colors.grey.shade100,
        filled: true,
        hintText: "Email",
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(10),
        ),
      ),
      validator: (value) {
        if (value == null || value.isEmpty) {
          return 'Please enter your email';
        }
        return null;
      },
    );
  }

  Widget _buildPasswordField() {
    return TextFormField(
      controller: passwordController,
      obscureText: true,
      decoration: InputDecoration(
        fillColor: Colors.grey.shade100,
        filled: true,
        hintText: "Password",
        border: OutlineInputBorder(
          borderRadius: BorderRadius.circular(10),
        ),
      ),
      validator: (value) {
        if (value == null || value.isEmpty) {
          return 'Please enter your password';
        }
        return null;
      },
    );
  }

  Widget _buildSignInButton(BuildContext context) {
    return Row(
      mainAxisAlignment: MainAxisAlignment.spaceBetween,
      children: [
        const Text(
          'Sign in',
          style: TextStyle(fontSize: 27, fontWeight: FontWeight.w700),
        ),
        CircleAvatar(
          radius: 30,
          backgroundColor: const Color(0xff4c505b),
          child: IconButton(
            color: Colors.white,
            onPressed: () async {
              await _signIn(context);
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
          onPressed: () => Navigator.pushNamed(context, 'register'),
          child: const Text(
            'Sign Up',
            style: TextStyle(
              decoration: TextDecoration.underline,
              color: Color(0xff4c505b),
              fontSize: 18,
            ),
          ),
        ),
        /*
        TextButton(
          onPressed: () => Navigator.push(
            context,
            MaterialPageRoute(builder: (context) => MicScreen()),
          ),
          child: const Text(
            'Forgot Password',
            style: TextStyle(
              decoration: TextDecoration.underline,
              color: Color(0xff4c505b),
              fontSize: 18,
            ),
          ),
        ),*/
      ],
    );
  }
}
