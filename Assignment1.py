#Question 1
def emp_bonus(att,perf):
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




