import 'package:flutter/material.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:firebase_database/firebase_database.dart';
import 'package:flutter_local_notifications/flutter_local_notifications.dart';

final FlutterLocalNotificationsPlugin localNotifications =
    FlutterLocalNotificationsPlugin();

void main() async {
  WidgetsFlutterBinding.ensureInitialized();

  await Firebase.initializeApp();

  const androidSettings =
      AndroidInitializationSettings('@mipmap/ic_launcher');

  await localNotifications.initialize(
    settings: const InitializationSettings(
      android: androidSettings,
    ),
  );

  await localNotifications
      .resolvePlatformSpecificImplementation<
          AndroidFlutterLocalNotificationsPlugin>()
      ?.requestNotificationsPermission();

  runApp(const MyApp());
}

Future<void> showNotification(
  String title,
  String body,
) async {
  const androidDetails = AndroidNotificationDetails(
    'fan_channel',
    'Fan Notifications',
    channelDescription: 'Fan status notification',
    importance: Importance.max,
    priority: Priority.high,
  );

  const details = NotificationDetails(
    android: androidDetails,
  );

  await localNotifications.show(
    id: DateTime.now().millisecond,
    title: title,
    body: body,
    notificationDetails: details,
  );
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'Pet Care',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const PetCarePage(),
    );
  }
}

class PetCarePage extends StatefulWidget {
  const PetCarePage({super.key});

  @override
  State<PetCarePage> createState() => _PetCarePageState();
}

class _PetCarePageState extends State<PetCarePage> {
  final DatabaseReference dbRef =
      FirebaseDatabase.instance.ref();

  double temperature = 0;
  double humidity = 0;
  String fanStatus = "OFF";

  String previousFanStatus = "OFF";

  @override
  void initState() {
    super.initState();

    dbRef.onValue.listen((event) {
      if (event.snapshot.value != null) {
        final data = Map<dynamic, dynamic>.from(
          event.snapshot.value as Map,
        );

        final newTemperature =
            double.tryParse(
                  data["temperature"].toString(),
                ) ??
                0;

        final newHumidity =
            double.tryParse(
                  data["humidity"].toString(),
                ) ??
                0;

        final newFanStatus =
            data["fanStatus"]?.toString() ?? "OFF";

        if (newFanStatus != previousFanStatus) {
          previousFanStatus = newFanStatus;

          if (newFanStatus == "ON") {
            showNotification(
              "🌀 Fan Turned ON",
              "Temperature: ${newTemperature.toStringAsFixed(1)}°C\nHumidity: ${newHumidity.toStringAsFixed(1)}%",
            );
          } else {
            showNotification(
              "🛑 Fan Turned OFF",
              "Temperature: ${newTemperature.toStringAsFixed(1)}°C\nHumidity: ${newHumidity.toStringAsFixed(1)}%",
            );
          }
        }

        setState(() {
          temperature = newTemperature;
          humidity = newHumidity;
          fanStatus = newFanStatus;
        });
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    bool isHot = temperature >= 30;

    return Scaffold(
      backgroundColor: Colors.grey.shade200,
      appBar: AppBar(
        centerTitle: true,
        title: const Text("🐶 Pet Care"),
      ),
      body: Center(
        child: SingleChildScrollView(
          child: Container(
            width: 350,
            padding: const EdgeInsets.all(20),
            child: Column(
              children: [
                // Temperature Card
                Container(
                  width: double.infinity,
                  padding: const EdgeInsets.all(25),
                  decoration: BoxDecoration(
                    color: Colors.white,
                    borderRadius:
                        BorderRadius.circular(20),
                    boxShadow: const [
                      BoxShadow(
                        blurRadius: 8,
                        color: Colors.black12,
                      ),
                    ],
                  ),
                  child: Column(
                    children: [
                      const Icon(
                        Icons.thermostat,
                        color: Colors.red,
                        size: 60,
                      ),
                      const SizedBox(height: 10),
                      const Text(
                        "Temperature",
                        style: TextStyle(
                          fontSize: 22,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                      const SizedBox(height: 10),
                      Text(
                        "${temperature.toStringAsFixed(1)}°C",
                        style: TextStyle(
                          fontSize: 50,
                          fontWeight: FontWeight.bold,
                          color: isHot
                              ? Colors.red
                              : Colors.green,
                        ),
                      ),
                      const SizedBox(height: 10),
                      Text(
                        isHot
                            ? "🔴 High Temperature"
                            : "🟢 Normal Temperature",
                        style: const TextStyle(
                          fontSize: 18,
                        ),
                      ),
                    ],
                  ),
                ),

                const SizedBox(height: 20),

                // Humidity Card
                Container(
                  width: double.infinity,
                  padding: const EdgeInsets.all(25),
                  decoration: BoxDecoration(
                    color: Colors.white,
                    borderRadius:
                        BorderRadius.circular(20),
                    boxShadow: const [
                      BoxShadow(
                        blurRadius: 8,
                        color: Colors.black12,
                      ),
                    ],
                  ),
                  child: Column(
                    children: [
                      const Icon(
                        Icons.water_drop,
                        color: Colors.blue,
                        size: 60,
                      ),
                      const SizedBox(height: 10),
                      const Text(
                        "Humidity",
                        style: TextStyle(
                          fontSize: 22,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                      const SizedBox(height: 10),
                      Text(
                        "${humidity.toStringAsFixed(1)}%",
                        style: const TextStyle(
                          fontSize: 50,
                          fontWeight: FontWeight.bold,
                          color: Colors.blue,
                        ),
                      ),
                      const SizedBox(height: 10),
                      Text(
                        humidity >= 70
                            ? "💧 High Humidity"
                            : humidity >= 40
                                ? "✅ Normal Humidity"
                                : "☀️ Low Humidity",
                        style: const TextStyle(
                          fontSize: 18,
                        ),
                      ),
                    ],
                  ),
                ),

                const SizedBox(height: 20),

                // Fan Status Card
                Container(
                  width: double.infinity,
                  padding: const EdgeInsets.all(25),
                  decoration: BoxDecoration(
                    color: Colors.white,
                    borderRadius:
                        BorderRadius.circular(20),
                    boxShadow: const [
                      BoxShadow(
                        blurRadius: 8,
                        color: Colors.black12,
                      ),
                    ],
                  ),
                  child: Column(
                    children: [
                      const Text(
                        "Fan Status",
                        style: TextStyle(
                          fontSize: 22,
                          fontWeight: FontWeight.bold,
                        ),
                      ),
                      const SizedBox(height: 10),
                      Text(
                        fanStatus,
                        style: TextStyle(
                          fontSize: 35,
                          fontWeight: FontWeight.bold,
                          color: fanStatus == "ON"
                              ? Colors.green
                              : Colors.red,
                        ),
                      ),
                      const SizedBox(height: 15),
                      Icon(
                        fanStatus == "ON"
                            ? Icons.air
                            : Icons.air_outlined,
                        size: 80,
                        color: Colors.blue,
                      ),
                    ],
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
