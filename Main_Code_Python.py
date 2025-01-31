import mysql.connector as yash
from random import *
from prettytable import PrettyTable
import datetime
date_t=datetime.datetime.now()
print('''------------------------------------------TGVF1 AIRLINE RESERVATIONS------------------------------------------

                                                            " where flying becomes easy ! "                    ''')
l1=PrettyTable(['Airport','Code'])
l1.add_row(['New Delhi' ,'IGI'])
l1.add_row(['New York'  ,'JFK'])
l1.add_row(['London'      ,'LCY'])
l1.add_row(['Tokyo'         ,'HND'])
l1.add_row(['Berlin'         ,'SXF'])
l1.add_row(['Singapore' ,'SIN'])
l1.add_row(['Paris'           ,'CDG'])
l1.add_row(['Dubai'         ,'DXB'])
l1.add_row(['Mumbai'    ,'BOM'])
l1.add_row(['Los Angeles','LAX'])
def password():
    password=input("Enter New Strong Password : ")
    p="@@".join(password)
    if len(password) >= 8:
        try:
            sql="UPDATE passenger_info set pass=%s WHERE flight_id=%s" 
            values=(p,flight_id)
            cursor.execute(sql,values)
            conn.commit()
            print("Password Updated")
            login()
        except:
            print("Error Occured")
            main()
    else:                    
        print("password less than 8 characters is not allowed.")
        main()
                                                                 
def update_phone():
    updated_phone=int(input("Enter 10 Digit New Phone Number: "))
    if len(str(updated_phone)) == 10:
        try:
            sql="UPDATE passenger_info set phone=%s WHERE flight_id=%s"
            values=(updated_phone,flight_id)
            cursor.execute(sql,values)
            conn.commit()
            print("Phone Number Updated. Please Login Again.")
            login()
        except mysql.connector.Error as e:
            print(e)     
            main()
def book():
    print("\n",l1)
    departure_point=input("Select the Departure Location with Code: ")
    destination_point=input("Select the Destination Location with Code :")
    number=int(input("Number of Tickets you want to Book : "))
    date=input("Date of Departure (DD-MM-YYYY): ")
    month=input("Month of Departure: ")
    journey_date=date + "-" +month
    for i in range(1,number+1):
        today_date=datetime.datetime.now()
        name=input("Passenger Full Name  : ")
        age=int(input("Passenger Age : "))
        try:
            sql="INSERT INTO book_flight(name,age,departure_point,destination_point,phone,flight_id,book_date,journey_date) VALUES ('{}',{},'{}','{}',{},{},'{}','{}')".format(name,age,departure_point,destination_point,phone,flight_id,date_t,journey_date)
            cursor.execute(sql)
            conn.commit()
            print(i," Flight Booked\nHave a Safe Journey !\n--------------")
        except exception as e:
            print(e)
            main()
def cancel():
    print("Go to View Ticket Section to know your Ticket Id.\n--------------------")
    try:
        sql="SELECT * FROM book_flight WHERE phone={} AND flight_id={}".format(phone,flight_id)
        cursor.execute(sql)
        a=cursor.fetchall()
        for result in a:
            print("Flights Booked through this Account\n----------------")
            print(result)
        if cursor.rowcount >=1:
           try:
                idd=int(input("How Many Tickets you want to Cancel : "))
                for i in range(1,idd+1):
                    ticket_id=int(input("Enter the Ticket Id : "))
                    s="DELETE FROM book_flight WHERE flight_id={}".format(flight_id)
                    cursor.execute(s)
                    conn.commit()
                    print("Ticket Canceled")
                main()
           except:
                print(" Sorry! Some Error occurred while Cancelling the Ticket")
                main()
        else:
            print("No Tickets are Regestered by this Ticket Id \n")
    except:
        print("Failed")
        main()
def update():
    user_ch_3 = int(input("Enter 1 to change Phone Number\nEnter 2 to change Password\nEnter Any Another key to Exit\n----------: "))

    if user_ch_3 == 1:
        update_phone()
    elif user_ch_3 == 2:
        password()
    else:
        print("Sorry ! Wrong Input.")
        main()
def enquiry():
    print("----------------\nCurrent Status : Flight On Time\n------------------")
    main()
def services():
    print("1.Flight Type\n2.Meals\n3.VIP Lounge Pass")
    sub_menu=int(input("Enter Menu Option :"))
    if sub_menu==1:
                 flight_id=int(input("Enter Your Flight Id:"))
                 print("Select Flight Type:\n ----------\nBusiness\nPremium\nEconomy\n-----------")
                 fl_type=input("Enter Flight Type :")
                 cursor.execute("UPDATE book_flight SET fl_type='%s' WHERE flight_id='%s' "%(fl_type,flight_id))
                 conn.commit()
                 main()
    elif sub_menu==2:
                 flight_id=int(input("Enter Your Flight Id:"))
                 fl_meal=input("In-Flight Meals are served according to the timings of the flights in accordance.\nTo Book them in advance type (Yes/No):")
                 cursor.execute("UPDATE book_flight SET fl_meal='%s' WHERE flight_id='%s' "%(fl_meal,flight_id))
                 conn.commit()
                 main()
    elif sub_menu==3:
                 flight_id=int(input("Enter Your Flight Id:"))
                 fl_lpass=input("To get a VIP-Lounge Pass type(Yes/No):")
                 cursor.execute("UPDATE book_flight SET fl_lpass='%s' WHERE flight_id='%s' "%(fl_lpass,flight_id))
                 conn.commit()
                 main()
    else:
                 print("Wrong Input !")
                 main()
def view():
    try:
        sql="SELECT * FROM book_flight WHERE phone={} AND flight_id={}".format(phone,flight_id)
        cursor.execute(sql)
        row=cursor.rowcount
        while True:
            a=cursor.fetchone()
            print("------------------------------\nTicket ID : ",a[5],"\nName : ",a[0],"\nAge : ",a[1],"\nDeparture from Airport : ",a[2],"\nArrival at Airport : ",a[3],"\nBooking Date : ",a[6],"\nJourney Date : ",a[7],"\nFlight Type : ",a[8],"\nMeals on Flight : ",a[9],"\nLounge Pass :",a[10],"\n-------------------------")
        print("IGNORE THE EMPTY MESSAGE")
    except:
        print("")
        main()
def delete():
    try:
        cursor=conn.cursor()
        sql="DELETE FROM passenger_info WHERE flight_id={}".format(flight_id)
        cursor.execute(sql)
        conn.commit()
        print("Account Deleted")
        log_sign()
    except:
        print("Failed to delete your account.")
        main()
def generate():
    print("You can Generate Only one Ticket at a Time.  Please visit this Section with your Ticket Id.\n-------------")
    no_of_tkt=input("Enter The Number of Ticket's you want to Generate : ")
    for i in range(1,int(no_of_tkt)+1):
        tkt_id=int(input("Enter the Ticket Id : "))
        sql="SELECT * FROM book_flight WHERE flight_id={}".format(tkt_id)
        cursor.execute(sql)
        a=cursor.fetchone()
        iid=a[5]
        name=a[0]
        age=a[1]
        departure_p=a[2]
        destination_p=a[3]
        x=str(iid)
        journey_d=a[7]
        booking_d=a[6]
        fl_type=a[8]
        fl_meal=a[9]
        fl_lpass=a[10]
        try:
            file=open("Flight_Ticket0_"+x+".txt","w")
            file.write("<----------------------------------------------->\nNOTE:-------->Don't Try to Fake your Ticket. Flight Attendents will get to know if the Ticket is Fake or Real.\nTicket id : "+x+"\nName : "+name+"\nAge : "+str(age)+"\nFrom : "+departure_p+"\nTo :"+destination_p+"\nJourney Date :"+journey_d+"\nBooking Date :"+booking_d+"\nFlight Type :"+fl_type+"\nMeals on Flight : "+fl_meal+"\nVIP Lounge Pass : "+fl_lpass+"\n<----------------------------------------------->")
            file.close()
            print(i," Ticket Generated as Flight_Ticket_"+x+".txt\n")
    
        except:
            print("Ticket Not Found !")
            main()
    main()
        
def issue():
    problem=input("Enter Your Issue : ")
    try:
        cursor=conn.cursor()
        sql="INSERT INTO report (phone,report) VALUES ({},'{}')".format(str(phone),problem)
        cursor.execute(sql)
        conn.commit()  
        print("Report Submitted Successfully\nThank you for your Feedback! :)\n---------------------")
        main()
    except:
        print("Failed to Submit. Please try Again.\n")
        issue()
def out():
    user_id=""
    print("You are Logged Out Successfully.\n")
    log_sign()
def main():
    print("--------------------\nTGVF1 AIRLINE RESERVATIONS\n***************\nMENU\n(Choose an Option)\n--------------------\n1. Book a Flight\n2. Cancel your Reservation\n3. Check your Flight Status\n4. In-Flight Services\n5. View your Tickets\n6. Generate your Tickets\n7. Update your Account\n8.  Report an Issue\n9. Delete Account\n10. Log Out\n---------------")
    print("")
    user_ch_2=input("Enter your Option Number from the above Menu : ")
    if user_ch_2=='1':
        book()
    elif user_ch_2=='2':
        cancel()
    elif user_ch_2=='3':
        enquiry()
    elif user_ch_2=='4':
        services()
    elif user_ch_2=='5':
        view()
    elif user_ch_2=='6':
        generate()
    elif user_ch_2=='7':
        update()
    elif user_ch_2=='8':
        issue()
    elif user_ch_2=='9':
        delete()
    elif user_ch_2=='10':
        out()
    else:
        print("Invalid Input")             
        main()
        
def Help():
    print('''              Sign up and Create an Id to Proceed Further.
                   If you have an Id then Login to proceed to the Main Menu.\n-------------------------''')
    print()
    log_sign()
def login():
    global phone
    global flight_id
    phone=int(input("Enter your Phone Number of 10 Digits : "))
    password=input("Enter your Password : ")
    p="@@".join(password)
    if len(str(phone))==10 or len(str(password))>=8:
      try:
        sql="SELECT * FROM passenger_info WHERE phone={} and pass='{}'".format(phone,p)
        cursor.execute(sql)
        a=cursor.fetchone()
        flight_id=a[0]
        data=cursor.rowcount
        if data==1:
            main()
        else:
            print("\nIncorrect Details.\n--------------")
            login()
      except:
        print("\nError Occured. Your Details might be Incorrect.\n--------------")
        log_sign()
    else:
        print("Invalid Pnone Number. Please Login Again\n------------")
        login()

def signup():
    passengername=input("Create your Username : ")
    password=input("Enter your Password : ")
    c_pass=input("Enter your Password Again : ")
    bank_id=input("Enter your Card Details for Transactions:")
    if password==c_pass or len(str(password))>=8:
        p="@@".join(password)
        phone=int(input("Enter your Phone Number : "))
        
        r1=randrange(100,200)
        r2=randrange(100,200)
        print("Prove You are Not a Robot ",r1,"+",r2)
        user_ans=int(input("Enter your Ans : "))
        if user_ans==r1+r2:
            if len(str(phone))==10:                                                                                                                        
              try:
                cursor=conn.cursor()
                sql="INSERT INTO passenger_info (passengername,pass,phone) VALUES ('{}','{}','{}')".format(passengername,p,phone)
                cursor.execute(sql)
                conn.commit()
                print("Account Created Succesfully---------------------------------\n---------------")
                log_sign()
              except:
                print("Failed. The Account May Exist.-------------\n-----------")
            print("Invalid Phone Number Signup Again.--------------\n--------------")
            signup()
        else:
                print("Wrong Answer Signup Again.-----------\n--------------------")
                signup()
                       
    else:
        print("Password Does't Match.Try Again.------------\n------------- ")
        log_sign()
def log_sign():
    print("1. Sign Up\n2. Login\n3. Help\n--------------------- ")
    
    user_ch_1=int(input("Enter your Choice of Option: "))
    if user_ch_1==1:
        signup()
    elif user_ch_1==2:
        login()
    elif user_ch_1==3:
        Help()
    else:
        print("Wrong Input. Try Again !")
        log_sign()
try:
    
    global conn
    flight_id=""
    conn=yash.connect(port='3307',host='localhost',password='yashmalhotra95',user='root',database="airways")
    cursor=conn.cursor()
    if conn.is_connected():
        print("************************************************************************")
        if flight_id=="":
            log_sign()
        if user_id!="":
           main()
       
except:
    print("The server is probably not running....")
