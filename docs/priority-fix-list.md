## Prioritization: อะไรต้องแก้ก่อน

| Issue / Problem | Impact | Effort | Priority | เหตุผล |
| --- | --- | --- | --- | --- |
| ข้อมูลอุณหภูมิอัปเดตช้า | High  | Medium  | P0  | กระทบการตรวจสอบข้อมูลแบบ Real-time |
| สถานะการทำงานของระบบยังไม่ชัด | Medium  | Low | P1  | ผู้ใช้ต้องใช้เวลาทำความเข้าใจ |
| เพิ่มระบบแจ้งเตือนอุณหภูมิ | Low | Medium  | P2  | เพิ่มความสะดวก แต่ยังไม่กระทบ Core Flow |

## Decision Table: Fix / Keep / Cut / Later

| สิ่งที่พบ | Decision | เหตุผล | Owner |
| --- | --- | --- | --- |
| อุณหภูมิอัปเดตช้าบางช่วง | Fix  | กระทบการดูข้อมูลแบบ Real-time | Backend / Cloud Developer |
| สถานะการทำงานของระบบยังไม่ชัด | Fix | ผู้ใช้ต้องใช้เวลาในการทำความเข้าใจ | Frontend / UX Product |
| การแสดงผลพัดลม ON/OFF ใช้งานได้ | Keep | ผู้ใช้เข้าใจและทำ task ได้สำเร็จ | Frontend / UX Product |
