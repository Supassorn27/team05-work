# team05-work-sprint3

## Project Name: Pet Care
## Members

| Name | Role | Location in Repo |
| :--- | :--- | :--- |
| บงกชกร จันเกตุ | Embedded / IoT Developer | firmware/ |
| พัชราภา รุ่งเรือง | Project Manager / Scrum Lead | README.md |
| ภูรี เอกา | Backend / Cloud Developer | backend/ |
| สุภัสสร บุญครอง | Frontend / UX Product | ux-product/ |

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

## Prototype v1 Readiness Check

| รายการ	 | สถานะ | หลักฐาน / Link |
|---|---|---|
| Prototype เปิดดูหรือทดลองได้ |	Partly Ready |	ux-product/figma.md |
| Core Flow หลักยังอยู่ครบ |	Ready	| docs/core-flow.md |
| มี demo link / file / device / Figma / notebook |	Partly Ready | ux-product/figma.md |
| มี known issues ที่ทีมรู้อยู่แล้ว |	มี	 | docs/known-issues.md ||
| มี workaround ถ้าระบบพัง |	มี |	ใช้ Figma Prototype จำลองการทำงาน |
| ผู้ใช้สามารถลอง task ได้โดยไม่ต้องอธิบายยาว |	Parly Ready | ผู้ใช้สามารถทำ Task หลักได้ แต่ยังต้องมีการอธิบายบางส่วนเนื่องจากระบบยังเป็น Prototype |

## Prototype v2 ที่จะใช้ทดสอบ

| รายการ | คำตอบ |
| --- | --- |
| Prototype ที่ใช้ทดสอบคืออะไร | Figma Prototype ระบบตรวจวัดอุณหภูมิและควบคุมพัดลมอัตโนมัติ |
| Link / File / Device / Location | https://github.com/Supassorn27/team05-work/blob/7ba150716b658e61ffe5c2346d625531af02f7fd/ux-product/figma.md |
| Core Flow ที่จะทดสอบ | ผู้ใช้เปิด Dashboard → ดูค่าอุณหภูมิ → ระบบเปลี่ยนสถานะพัดลม ON/OFF ตามอุณหภูมิ → ผู้ใช้ดูการแจ้งเตือน |
| สิ่งที่ prototype ทำได้แล้ว | แสดงอุณหภูมิ, สถานะพัดลม |
| ข้อจำกัดที่ต้องบอกผู้ใช้ก่อน test | เป็นการจำลองผ่าน figma ยังไม่ได้เชื่อมต่อข้อมูลจาก ESP32 แบบ real-time |
