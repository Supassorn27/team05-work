# โครงสร้างฐานข้อมูล

## ตาราง users

| ชื่อฟิลด์ | ชนิดข้อมูล |
|-----------|------------|
| id | INT |
| username | VARCHAR(50) |
| password | VARCHAR(255) |

## ตาราง sensor_data

| ชื่อฟิลด์ | ชนิดข้อมูล |
|-----------|------------|
| id | INT |
| temperature | FLOAT |
| fan_status | VARCHAR(10) |
| created_at | DATETIME |
