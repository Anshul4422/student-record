
import json
class students_record:
   
   def __init__(self):
    self.students=[]
    self.logged_in = False
    self.load_data()

   def load_data(self):
       try:
        with open("record.txt", "r") as f:
            self.students = json.load(f)
       except (FileNotFoundError, json.JSONDecodeError):
        self.students = []    

   def admin_login(self):

    correct_username = "Anshul"
    correct_password = "Anshul@123"

    enter_username = input("enter user name:  ")
    enter_password = input ("enter password :  ")
    

    if enter_username == correct_username and enter_password == correct_password:
        print("admin login successfully ")
        self.logged_in = True
    else:
        print("invalid id password")

  


   def add_student(self):
    name = input("enter the student name:  ")
    roll_no = input("enter the roll no:  ")
    self.students.append({"name": name, "roll_no": roll_no})
    print(f"{name} and {roll_no}")


   def attendence(self):
    found = False
    roll_no= input("enter the roll no:  ")
    for student in self.students:
        if student ["roll_no"] == roll_no:
            found = True
            print ("present")
            break
    if not found :
            print("invalid roll no:  .")

   def view_students(self):
   
    if not self.students:
        print("it is empty")
    else:
        print("students")
        for i, name in enumerate(self.students, start=1):
           print(f"{i}. {name['name']} (Roll No: {name['roll_no']})")


   def remove_student(self):
    found = False
    roll_no = input("enter the roll no:  ").strip()
    for student in self.students:
        if student ["roll_no"] == roll_no:
            self.students.remove(student)
            found = True   
            print("student removed") 
            break
    if not found:
            print("student not found") 

   def save_student(self):
    so = json.dumps(self.students) 
    with open("record.txt","w") as f:
      f.write(so)


   def run(self):
    while True:
     print("1. add student: ")
     print("2. attendence: ")
     print("3. view students: ")
     print("4. want to remove student:  ")
     print("5. want to save student detils:  ")
     print("6. exit program")

     select = input("select an option (1-6):  ")

     if select == "1":
       self.add_student()
     elif select == "2":
        self.attendence()
     elif select == "3":
        self.view_students()
     elif select == "4":
       self.remove_student()
     elif select == "5":
        self.save_student()
     elif select == "6":
        print("exiting.....")
        break

     else:
        print("! invalid choice")

obj =  students_record()
obj.admin_login()
if obj.logged_in:
  obj.run()
else:
   print("accessed denied !")