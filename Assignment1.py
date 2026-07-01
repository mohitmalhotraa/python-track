#Question 1
"""def emp_bonus(att,perf):
    if (att>=75 and perf>=6):
        print("Eligible")
    else:
        print("Not Eligible")
emp_bonus(68,5)

#Question 2
Username=input("Enter Username: ")
Password=input("Enter Password: ")
def credential(Username,Password):
    if(Username == "Superman" and Password =="Batman"):
        print("Valid")
    else:
        print("Invalid Username or Password")

credential(Username,Password)

#Question 3
# A traffic monitoring system needs to determine whether a vehicle exceeded the speed limit
def vehicle_speed():
    vehicle = input("Enter Vehicle Type: ")
    speed = int(input("Enter Vehicle speed: "))
    return vehicle,speed

def speed_test(speed,vehicle):
    
    if (vehicle == "Car" or vehicle == "Truck") and speed >=60:
        
        print("Your" ,vehicle, "speed is exceeding at ",speed,"KMPH")
        

    elif (vehicle == "bike" or vehicle=="scooty") and speed >=50:
        print("Your" ,vehicle, "speed is exceeding at ",speed,"KMPH")

    else:
        print("Your" ,vehicle, "is at safe speed of ",speed,"KMPH")
         
    
vehicle, speed = vehicle_speed()       
speed_test(speed, vehicle)

#Question 4 A Bank wants to calculate simple interest for customers based on principal, rate, and time entered by the user
def inp_data():
    P = int(input("Enter Principal Amount: "))
    R = int(input("Enter Rate: "))
    T = int(input("Enter Time: "))
    return P,R,T

def simple_int(P,R,T):
    print ((P*R*T)/100)

P,R,T = inp_data()
simple_int(P,R,T)

#Question 5 
def ager():
    age=int(input("Enter Age: "))

    return age 
def tkt_price(age):
    if(age < 18):
        TicketPrice = "Rs 100"
    elif(18 <= age < 60):
        TicketPrice = "Rs 200"
    else:
        TicketPrice = "Rs 150"
    return TicketPrice
age = ager()
print(tkt_price(age))

#Question6 WAP to find the largest among three entered sales figures
def larger_num(num1,num2,num3):
    if (num1>num2>num3 or num1>num3>num2):
        print(num1,"is largest among all")
    elif (num2>num1>num3 or num2>num3>num1):
        print(num2,"is largest among all")
    else:
        print(num3,"is largest among all")
larger_num(10,12,50)"""



# #Question 7 A school wants to calculate grades for students based on marks obtained in five subjects
# def ip_marks():
#     for i in range(0,5):
#         a = a.extend[0](int(input("Marks of subject")))
        
#     return Marks
# def grade_marks(Marks):
#     avg= sum(Marks)/5
#     if(avg>90):
#         print("A grade")
#     elif(avg>80):
#         print("B grade")
#     elif(avg>70):
#         print("C grade")
#     elif(avg>60):
#         print("D grade")
#     elif(avg>50):
#         print("E grade")
#     else:
#         print("F grade")

# Marks = ip_marks()
# grade_marks(Marks)

#Question8 3 Maximum login attempt
# def get_pass():
    
#     return password

def login(attempt = 0):
    
    while attempt< 3:
        password = input("Enter Password: ")
        
        if (password=="admin"):
            print("Login Successfully")
            break
        
        else:
            attempt += 1
        print("Login Unsuccessful")


login()




    

        

















