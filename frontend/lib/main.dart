import 'package:flutter/material.dart';
import 'package:wms_udara_jadi_bersih_frontend/screens/login_screen.dart';

void main() {
  WidgetsFlutterBinding.ensureInitialized();
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'PT. Udara Jadi Bersih WMS',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: LoginScreen(),
      routes: {
        '/dashboard': (context) => DashboardScreen(),
        '/materials': (context) => MaterialScreen(),
        '/qr': (context) => QRScreen(),
        '/opname': (context) => StockOpnameScreen(),
        '/mrp': (context) => MRPScreen(),
        '/reports': (context) => ReportsScreen(),
        '/admin': (context) => AdminScreen(),
      },
    );
  }
}