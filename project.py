
import json
import datetime
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

    for attempt in range (3):
       enter_username = input("enter user name:  ")
       enter_password = input ("enter password :  ")

       if enter_username == correct_username and enter_password == correct_password:
                  print("admin login successfully ")
                  self.logged_in = True
                  break 
       else:
      
         print("invalid id password enter again ")
    if self.logged_in == False:
      print("--")
  


   def add_student(self):
    name = input("enter the student name:  ")
    roll_no = input("enter the roll no:  ")
     
    for student in self.students:
       if student["roll_no"] == roll_no:
          print("roll no. is already exists")
          return
       
    self.students.append({
          "name": name,
           "roll_no": roll_no,
           "attendance":[]
       })
    print(f"{name} (Roll No: {roll_no}) added successfully.")
    print(f"the total no. of students is: {len(self.students)}")
    self.save_student()

 
   def attendance(self):
    found = False
    roll_no= input("enter the roll no:  ")
    for student in self.students:
        if student ["roll_no"] == roll_no:
            found = True
            print ("present")
            today = str(datetime.date.today())
            print(today)
            student["attendance"].append(today)  
            break
    if not found :
            print("invalid roll no:  .")
    self.save_student()
   


   def view_students(self):
    if not self.students:
        print("it is empty")
    else:
        print("students")
        for i, name in enumerate(self.students, start=1):
           print(f"{i}. {name['name']} (Roll No: {name['roll_no']})")
    
   def search(self):
      
      roll_no = input("enter the roll no:  ").strip()
      for student in self.students:
         if student ["roll_no"] == roll_no:
            print("student data :")
            for key, value in student.items():
               print (f"{key} : {value}")
            return
      print ("roll no. is not valid: ")
            


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
    self.save_student()



   def update_name(self, student):
      print(f"Current name: {student['name']}")
      new_name = input("ENTER NEW NAME:  ").strip()

      if not new_name:
         print("name cannot be empty")
         return
        
      student["name"] = new_name
      print(f"Name updated successfully to {new_name}.")
      self.save_student()

   def update_roll(self , student):
      print(f"Current roll_no: {student['roll_no']}")
      new_roll = input("ENTER NEW ROLL NO.:  ").strip()

      if not new_roll:
         print("roll no. cannot be empty")
         return
        
      student["roll_no"] = new_roll
      print(f"roll_no.  updated successfully to {new_roll}.")
      self.save_student()

      
   def update_record(self):
    found = False
    roll_no = input("enter the roll no:  ").strip()  
    for student in self.students:
       if student ["roll_no"] == roll_no:
          found = True
          print("choose option to update")
          while True:
             print("------update menu------")
             print("1. Update Name:  ")
             print("---------")
             print("2.update roll_no: ")
             print("---------")
             print("3. exit")
             print("-------------------")

             select= input("select an option (1-3) ")
             if select== '1':
                self.update_name(student)

             elif select== '2':
                self.update_roll(student)

             elif select == "3":
                print("exit.....")
                return
             else :
                print("invalid choise")
    if not found:
     print("roll no. not found")

   def save_student(self):
    so = json.dumps(self.students) 
    with open("record.txt","w") as f:
      f.write(so)


   def run(self):
    while True:
     print("1. add student: ")
     print("---------")
     print("2. attendance: ")
     print("---------")
     print("3. view students: ")
     print("---------")
     print("4. want to remove student:  ")
     print("---------")
     print("5. want to update an record:  ")
     print("---------")
     print("6. search student by roll no.:" )
     print("---------")
     print("7. exit program")

     select = input("select an option (1-7):  ")

     if select == "1":
       self.add_student()
     elif select == "2":
        self.attendance()
     elif select == "3":
        self.view_students()
     elif select == "4":
       self.remove_student()
     elif select == "5":
        self.update_record ()
     elif select == "6":
        self.search()
     elif select == "7":
        print("exit.......")
        break

     else:
        print("! invalid choice")

obj =  students_record()
obj.admin_login()
if obj.logged_in:
  obj.run()
else:
   print("access denied !")