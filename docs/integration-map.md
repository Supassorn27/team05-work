## Integration Map

| ส่วน | คำตอบของทีม |
|---|---|
| Input คืออะไร |  ค่าอุณหภูมิจาก Temperature Sensor (DHT11/DHT22) |
| Component 1 | ESP32 รับค่าอุณหภูมิและประมวลผล |
| Component 2 | Relay Module สั่งเปิด/ปิดพัดลมอัตโนมัติ |
| Component 3 | MQTT / Backend / Dashboard แสดงผลข้อมูล |
| Output คืออะไร | พัดลมเปิดอัตโนมัติ + ผู้ใช้ดูข้อมูลอุณหภูมิผ่านมือถือได้ |

DHT11 → ESP32 → Relay/Fan → MQTT → Dashboard → User
