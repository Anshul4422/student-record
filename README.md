# 🧑‍🎓 Student Management CLI App

A simple command-line interface application written in Python to manage students, take attendance, and save records. Designed for basic usage by teachers or admins.

---

## 📌 Features

✅ Admin login system  
✅ Add student (name, roll number)  
✅ View all students  
✅ Take attendance by roll number  
✅ Remove a student  
✅ Auto-load from and save to a local file (`record.txt`)  

---

## 🚀 How to Run

### 1. Clone or Download the Project
```bash
git clone <your_repo_link>
cd student-management-cli
```

### 2. Run the Script
```bash
python your_script_name.py
```

---

## 🔑 Admin Credentials (Hardcoded)

- **Username**: `Anshul`  
- **Password**: `Anshul@123`

You will be prompted to enter these when the program starts.

---

## 🎮 Menu Options

| Option # | Action                         |
|----------|--------------------------------|
| 1        | Add a new student              |
| 2        | Take attendance by roll number |
| 3        | View all students              |
| 4        | Remove a student               |
| 5        | Save student data              |
| 6        | Exit the program               |

---

## 📁 File Used

- `record.txt` — stores all student data in JSON format.

Example content:
```json
[
  {
    "name": "Amit",
    "roll_no": "101"
  },
  {
    "name": "Sita",
    "roll_no": "102"
  }
]
```

---

## 🔧 Customization Ideas (Next Steps)

- Add `attendance` tracking with date and status (`present/absent`)
- Add search by name or roll number
- Show attendance reports
- Store login credentials securely
- GUI version using Tkinter or web version with Flask/Django

---

## 🧑‍💻 Author

Made ❤️ by Anshul
