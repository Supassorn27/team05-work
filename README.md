# team05-work-sprint3

## Project Name: Pet Care
## Members

| Name | Role | Location in Repo |
| :--- | :--- | :--- |
| บงกชกร จันเกตุ | Embedded / IoT Developer | firmware/ |
| พัชราภา รุ่งเรือง | Project Manager / Scrum Lead | README.md |
| ภูรี เอกา | Backend / Cloud Developer | backend/ |
| สุภัสสร บุญครอง | Frontend / UX Developer | ux-product/ |

## Core Flow
ผู้ใช้เปิดระบบ → Sensor ตรวจวัดอุณหภูมิ → ESP32 ประมวลผล → Relay สั่งเปิดพัดลมอัตโนมัติ → Dashboard แสดงสถานะ → ผู้ใช้ตรวจสอบข้อมูลได้แบบ real-time

## Prototype
- ผู้ใช้สามารถดูค่าอุณหภูมิและสถานะพัดลมผ่านหน้า Dashboard บนมือถือได้
- ระบบแสดง Flow การทำงานของการตรวจวัดอุณหภูมิผ่าน Figma Prototype
- เมื่ออุณหภูมิสูงเกินค่าที่กำหนด ระบบจะแสดงสถานะพัดลมเป็น “ON” เพื่อจำลองการทำงานอัตโนมัติ
- ESP32, DHT11 และ Relay ได้รับการศึกษาและทดสอบการเชื่อมต่อเบื้องต้น
- มี GitHub Repository สำหรับรวบรวม Evidence, README และเอกสารของทีม

## สิ่งที่ยังทำไม่ได้ใน Prototype
- ยังไม่สามารถแสดงค่าอุณหภูมิจาก DHT11 บน Dashboard แบบ real-time ได้
- การแจ้งเตือนอุณหภูมิยังเป็นการจำลองผ่าน Figma Prototype
- ยังไม่สามารถเชื่อมต่อ ESP32 กับ Firebase หรือฐานข้อมูล Cloud ได้

## Sprint Goal
พัฒนา Prototype v1 สำหรับระบบตรวจวัดอุณหภูมิสัตว์เลี้ยง
โดยให้เซ็นเซอร์ตรวจวัดอุณหภูมิ ส่งข้อมูลไปยัง Dashboard
และสามารถสั่งเปิดพัดลมอัตโนมัติเมื่ออุณหภูมิสูงเกินค่าที่กำหนด

## Documents
- Core Flow: docs/core-flow.md
- Sprint Board: docs/sprint-board-link.md
- Evidence Log: docs/evidence-log.md
- Blocker Log: docs/blocker-log.md
- Demo Script: docs/demo-script.md
