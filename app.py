print("*"*70)
print("STUDENT RECORD MANAGEMENT SYSTEM")
print("*"*70)

def student_info(student_id, student_name):
    attendance_info={
        111:{"name": "Christian Effiong", "parent_phonenumber":"075900747", "email" : "chriseffi@gmail.com"},
        222:{"name": "Sallieu Mansaray", "parent_phonenumber":"099856734", "email" : "sallieu@gmail.com"},
        333:{"name": "Angela Yankuba", "parent_phonenumber":"07360897", "email" : "angiebaby@gmail.com"},
        444:{"name": "Alfred Vandy", "parent_phonenumber":"088905634", "email" : "vandy@gmail.com"},
        555:{"name": "Caper Chino", "parent_phonenumber":"09999887", "email" : "chino@gmail.com"},
        666:{"name": "George Ngolo", "parent_phonenumber":"07923435", "email" : "ngolo@gmail.com"},
        777:{"name": "Haja Sombie", "parent_phonenumber":"075778098", "email" : "sombie@gmail.com"},
        888:{"name": "French Genius", "parent_phonenumber":"099900747", "email" : "chriseffi@gmail.com"},
        999:{"name": "Mamta John ", "parent_phonenumber":"0675900747", "email" : "mamta@gmail.com"},
        110:{"name": "Christian Kamara", "parent_phonenumber":"07597875", "email" : "kamara@gmail.com"},
        211:{"name": "Tan Seri", "parent_phonenumber":"08884909", "email" : "serTan@gmail.com"},
    }
    if student_id in attendance_info:
        name=attendance_info[student_id]["name"]
        phonenumber=attendance_info[student_id]["parent_phonenumber"]
        email=attendance_info[student_id]["email"]
        for pid, student in attendance_info.items():
            if name == student_name:
                return f"student: {name} \nparent phonenumber: {phonenumber} \nemail: {email}"
            else:
                return f"No information found for student name: {student_name}\nstudent_id: {student_id}"

            

def  lecturer_access(lecturer_id, lecturer_name):
    lecturer_info={
        121:{"name": "Effiong John", "phone_number":"075900747"},
        122:{"name": "Effiong Fatu", "phone_number":"099708086"},
        123:{"name": "Kamara Conteh", "phone_number":"075780098"},
        124:{"name": "Amadu Kamara", "phone_number":"09995612"},
        125:{"name": "Elijah Fullah", "phone_number":"099960747"}
    }
    if lecturer_id in lecturer_info:
        lect_name=lecturer_info[lecturer_id]["name"]
        lect_phone=lecturer_info[lecturer_id]["phone_number"]
        for id, name in lecturer_info.items():
            if lect_name==lecturer_name:
                return f"lecturer name: {lecturer_name} \nlecturer id: {lecturer_id}\n lecturer phonenumber: {lect_phone}"
                
            else:
                return f"No data found for lecturer name: {lecturer_name} and lecturer id: {lecturer_id}"
        
        
        
student_name={}
student_id=0
while True:
    try:
        student_id=int(input("Enter your student ID: "))
        break
        
    except ValueError:
        print("Id Should be integer ")
        continue


while True:
    student_name=input("Enter your name: ").title()
    if student_name:
        try:
           student_name=int(student_name)
           if isinstance(student_name, int):
            print("name should be string")
            continue
           else:
              break
           
        except ValueError:
            now=student_info(student_id, student_name)
            print(now)
            break

print("#"*100)
print("LECTURER LOGIN PANEL")
print("*"* 100)

while True:
    ask=input("Please answer with yes or no\nAre you a lecturer yes or no: ").lower()
    if ask:
      try:
        ask=int(ask)
        if isinstance(ask, int):
            print("please no number is allowed only use yes or no")
            continue
        else:
            break
      
      except ValueError:
          if ask=="yes":
              break
          elif ask== "no":
              break
          
          else:
              print("not stop messing around ")
              continue

if ask =="yes":
    while True:
        try:
            lecturer_id=int(input("Enter your Lecturer ID: "))
            break

        except ValueError:
            print("String data type not allowed")
            continue

    while True:
        lecturer_name=input("Enter your Name: ").title()
        if lecturer_name:
            try:
               if isinstance(lecturer_name, int):
                print("Please no number allowed")
                continue
               else:
                break

            except ValueError:
                break
        
call=lecturer_access(lecturer_id, lecturer_name)
print(call)

        