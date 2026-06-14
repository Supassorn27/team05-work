# Database Schema

## โครงสร้างฐานข้อมูล Firebase Realtime Database

```json
{
  "temperature": 28,
  "humidity": 65,
  "fanStatus": "OFF"
}
```

## คำอธิบายข้อมูล

| ชื่อข้อมูล  | ประเภทข้อมูล | รายละเอียด                              |
| ----------- | ------------ | --------------------------------------- |
| temperature | float        | ค่าอุณหภูมิที่อ่านได้จากเซ็นเซอร์ DHT11 |
| humidity    | float        | ค่าความชื้นที่อ่านได้จากเซ็นเซอร์ DHT11 |
| fanStatus   | string       | สถานะการทำงานของพัดลม (ON/OFF)          |

## หลักการทำงานของระบบ

1. ESP32 เชื่อมต่อกับเครือข่าย WiFi
2. ESP32 อ่านค่าอุณหภูมิและความชื้นจากเซ็นเซอร์ DHT11
3. ข้อมูลจะถูกส่งไปยัง Firebase Realtime Database
4. เมื่ออุณหภูมิมากกว่าหรือเท่ากับ 30 องศาเซลเซียส พัดลมจะทำงาน
5. เมื่ออุณหภูมิต่ำกว่า 30 องศาเซลเซียส พัดลมจะหยุดทำงาน
6. สถานะพัดลมจะถูกบันทึกลงใน Firebase เป็น ON หรือ OFF
7. ระบบอัปเดตข้อมูลทุก 2 วินาที

## Firebase Realtime Database Example

ตัวอย่างข้อมูลที่ถูกจัดเก็บใน Firebase Realtime Database

```json
{
  "temperature": 28,
  "humidity": 14,
  "fanStatus": "OFF"
}
https://github.com/Supassorn27/team05-work/blob/main/backend/firebase_database.jpg
