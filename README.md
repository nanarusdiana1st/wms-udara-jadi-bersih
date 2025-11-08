# wms-udara-jadi-bersih
Application WMS PT. Udara Jadi Bersih
# Warehouse Management System - PT. Udara Jadi Bersih

A full-stack application built with **Flutter (Frontend)**, **FastAPI (Backend)**, and **PostgreSQL (Database)**.

## Features
- Dashboard with interactive charts
- QR Code generation & scanning
- Dead stock & slow moving calculation
- MRP (Material Requirements Planning)
- Stock opname per category
- Monthly reports (Excel/PDF)
- User roles: admin, supervisor, user
- Import/export data
- Material status: active, inactive_temp, inactive_perm

## Setup Instructions

### 1. Backend Setup
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload --host 0.0.0.0 --port 8000
