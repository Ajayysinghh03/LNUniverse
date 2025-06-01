# Project Name: LNUniverse

## 🔍 Purpose
This project is a **centralized university management system** for LNCT University, titled **LNUniverse**. The goal is to build a full-stack website that can **manage all academic, administrative, and operational data** of various colleges under the university in a unified, role-based platform.

## 👥 User Roles and Panels

### 1. Super Admin (University Founders)
- Add, update, or remove colleges under the university
- Full access to all student and faculty data across colleges
- Generate global reports (college-wise student count, performance stats, etc.)
- Create or remove admin users for each college

### 2. College Admin (Individual College Heads)
- Manage teacher and student data within their college
- Assign faculty roles such as HOD, Mentor, or Class In-charge
- Create class schedules, assign courses
- View and export reports for their college

### 3. Teacher Panel
- View assigned classes and subjects
- Take and update student attendance
- Upload student internal marks and notes
- View student list with basic profiles
- Message students or send circulars

### 4. Student Panel
- View personal details (name, enrollment, course, etc.)
- Access attendance records
- View internal marks and uploaded study materials
- Receive announcements and documents from teachers or admins

---

## 🛠 Tech Stack

| Layer       | Tech Used                         |
|-------------|----------------------------------|
| Frontend    | HTML, CSS, JavaScript, TailwindCSS |
| Backend     | Django (Python)                   |
| Database    | PostgreSQL (preferred over Firebase for Django ORM) |
| Hosting     | Render / Railway / Vercel (optional) |
| Authentication | Django AllAuth or Firebase Auth (if you want OTP/email auth) |

---

## 🧠 Key Features (Functionality)

- 🔐 **Role-Based Access Control (RBAC)** using Django permissions
- 📊 **Dashboard** for each panel with graphs (student performance, attendance)
- 🗃️ **Model Structure**:
    - `University`, `College`, `User`, `StudentProfile`, `TeacherProfile`, `Course`, `Subject`, `Attendance`, `Marks`
- 📅 **Timetable Scheduling**
- 🔔 **Notifications & Circular System**
- 🧾 **Downloadable Reports** (PDFs for marksheets, attendance sheets)
- 🔍 **Searchable Student Database** for admins
- 📬 **Messaging Module** between teacher ↔ student, admin ↔ teacher

---

## 🧱 Folder Structure (Planned)
LNUniverse/
├── manage.py
├── lnuniverse/ # Django settings and URLs
├── users/ # Custom user model and auth logic
├── colleges/ # College models and views
├── students/
│ └── models.py # StudentProfile, Attendance, Marks
├── teachers/
│ └── models.py # TeacherProfile, Courses
├── templates/
├── static/
└── README.md


