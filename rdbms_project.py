import sys
import sqlite3
db = sqlite3.connect("rdbms_examination_result_project.db")
conn = db.cursor()

'''conn.execute("""CREATE TABLE STUDENT(
                ROLL_NO INT PRIMARY KEY NOT NULL,
                NAME TEXT NOT NULL,
                FATHER_NAME TEXT NOT NULL,
                MOBILE_NO INT NOT NULL,
                AGE INT NOT NULL,
                DEPARTMENT TEXT NOT NULL)""") 

conn.execute("""CREATE TABLE RESULT(
                ROLL_NO INT PRIMARY KEY NOT NULL,
                EXAMINATION TEXT NOT NULL,
                PYTHON INT  NOT NULL,
                RDBMS TEXT NOT NULL,
                CN INT NOT NULL,
                OS INT NOT NULL,
                DS INT NOT NULL,
                FOREIGN KEY (ROLL_NO) REFERENCES STUDENT(ROLL_NO))""")'''


def insert_data():
    ch="y"
    while(ch=="y" or ch=="Y"):
           i=0
           stu_roll_no=int(input("\n\nENTER THE ROLL NUMBER :"))

           q0 = "SELECT * FROM STUDENT where ROLL_NO=?"
           conn.execute(q0, (stu_roll_no,))
           a=conn.fetchall()
           for row in a:
               if(stu_roll_no == row[0]):
                   print("\nTHIS ROLL NUMBER ALREADY EXISTS")
                   print("\n1.UPDATE THE EXISTING RECORD\n2.INSERT NEW RECORD\nPRESS ANY KEY TO GO BACK")
                   sel=input("\nENTER CHOICE : ")
                   if sel=='1':
                       update_data()
                       i=1
                       ch="n"
                   elif sel=='2':
                       ch="y"
                       i=1
                   else:
                       admin()
                       ch="n"
                       i=1
                           
               else:
                   break
           if i!=1:
               stu_name=input("ENTER STUDENT NAME :")
               father_name=input("ENTER  FATHER NAME :")
               mobile=input("ENTER THE MOBILE NO :")
               while(len(mobile)!=10):
                   mobile=input("\nPLEASE ENTER 10-DIGIT MOBILE NUMBER :")
               stu_mobile_no=int(mobile)

               stu_age=int(input("ENTER STUDENT AGE :"))
               while(stu_age<=0 or stu_age>=30):
                   stu_age=int(input("\nENTER CORRECT STUDENT AGE"))
               
               stu_dept=input("ENTER THE DEPARTMENT NAME :")
               stu_dept.upper()
               exam=input("ENTER EXAMINATION NAME :")
               python=int(input("ENTER MARKS IN PYTHON :"))
               rdbms=int(input("ENTER MARKS IN RDBMS :"))
               cn=int(input("ENTER MARKS IN CN :"))
               os=int(input("ENTER MARKS IN OS :"))
               ds=int(input("ENTER MARKS IN DS :"))

               conn.execute("insert into student (ROLL_NO,NAME,FATHER_NAME,MOBILE_NO,AGE,DEPARTMENT) values (?,?,?,?,?,?)",(stu_roll_no,stu_name,father_name,stu_mobile_no,stu_age,stu_dept))
               conn.execute("insert into result (ROLL_NO,EXAMINATION,PYTHON,RDBMS,CN,OS,DS) values (?,?,?,?,?,?,?)",(stu_roll_no,exam,python,rdbms,cn,os,ds))

               print("\n\nRECORD ENTERED SUCCESSFULLY")
               db.commit()

               ch=input("\n\nWANT TO INSERT ANOTHER RECORD ? (Y/N) : ")

def  update_data():
    ch="y"
    u=0
    rn=int(input("\nENTER STUDENT ROLL NUMBER TO UPDATE RECORD :"))
    q0 = "SELECT * FROM STUDENT where ROLL_NO=?"
    conn.execute(q0, (rn,))
    a=conn.fetchall()
    for row in a:
        if(rn == row[0]):
            while(ch=="y" or ch=="Y"):
                u=1
                print("\n1.UPDATE STUDENT NAME ")
                print("2.UPDATE FATHER NAME ")
                print("3.UPDATE MOBILE NUMBER ")
                print("4.UPDATE STUDENT AGE ")
                print("5.UPDATE DEPARTMENT ")
                print("6.UPDATE MARKS IN PYTHON ")
                print("7.UPDATE MARKS IN RDBMS ")
                print("8.UPDATE MARKS IN CN ")
                print("9.UPDATE MARKS IN OS ")
                print("10.UPDATE MARKS IN DS ")
                print("11.UPDATE EXAMINATION NAME ")
                choice = int(input("\nENTER YOUR CHOICE : "))

                if (choice == 1):
                    up_name = input("\nENTER STUDENT NAME :")
                    q5 = "UPDATE STUDENT SET NAME=? where ROLL_NO=?"
                    conn.execute(q5, (up_name, rn,))
                    print("\nNAME SUCCESSFULLY UPDATED")

                elif(choice==2):
                    up_f_name = input("\nENTER FATHER NAME :")
                    q6 = "UPDATE STUDENT SET FATHER_NAME=? where ROLL_NO=?"
                    conn.execute(q6, (up_f_name, rn,))
                    print("\nFATHER NAME UPDATED SUCCESSFULLY")

                elif(choice == 3):
                    mn = input("\nENTER MOBILE NUMBER :")
                    while(len(mn)!=10):
                        mn=input("\nPLEASE ENTER 10-DIGIT MOBILE NUMBER :")
                    up_mn=int(mobile)
                    q7 = "UPDATE STUDENT SET MOBILE_NO=? where ROLL_NO=?"
                    conn.execute(q7, (up_mn, rn,))
                    print("\nMOBILE NUMBER UPDATED SUCCESSFULLY")

                elif(choice == 4):
                    up_age = int(input("\nENTER STUDENT AGE :"))
                    while(up_age<=0 or up_age>30):
                             up_age=int(input("\nENTER CORRECT STUDENT AGE"))                    
                    q15 = "UPDATE STUDENT SET AGE=? where ROLL_NO=?"
                    conn.execute(q15, (up_age, rn,))
                    print("\nAGE UPDATED SUCCESSFULLY")
                    
                elif(choice == 5):
                    up_dept = input("ENTER DEPARTMENT NAME :")
                    q8 = "UPDATE STUDENT SET DEPARTMENT=? where ROLL_NO=?"
                    conn.execute(q8, (up_dept, rn,))
                    print("\nDEPARTMENT UPDATED SUCCESSFULLY")

                elif(choice == 6):
                    up_python = int(input("ENTER MARKS IN PYTHON :"))
                    q9 = "UPDATE RESULT SET PYTHON=? where ROLL_NO=?"
                    conn.execute(q9, (up_python, rn,))
                    print("\nMARKS IN PYTHON UPDATED SUCCESSFULLY")

                elif(choice == 7):
                    up_rdbms = int(input("ENTER MARKS IN RDBMS :"))
                    q10 = "UPDATE RESULT SET RDBMS=? where ROLL_NO=?"
                    conn.execute(q10, (up_rdbms, rn,))
                    print("\nMARKS IN RDBMS UPDATED SUCCESSFULLY")

                elif(choice == 8):
                    up_cn = int(input("ENTER MARKS IN CN :"))
                    q11 = "UPDATE RESULT SET CN=? where ROLL_NO=?"
                    conn.execute(q11, (up_cn, rn,))
                    print("\nMARKS IN CN UPDATED SUCCESSFULLY")

                elif(choice == 9):
                    up_os = int(input("ENTER MARKS IN OS :"))
                    q12 = "UPDATE RESULT SET OS=? where ROLL_NO=?"
                    conn.execute(q12, (up_os, rn,))
                    print("\nMARKS IN OS UPDATED SUCCESSFULLY")

                elif(choice == 10):
                    up_ds = int(input("ENTER MARKS IN DS :"))
                    q13 = "UPDATE RESULT SET DS=?  where ROLL_NO=?"
                    conn.execute(q13, (up_ds, rn,))
                    print("\nMARKS IN DS UPDATED SUCCESSFULLY")

                elif(choice == 11):
                    up_exam =input("ENTER EXAMINATION NAME :")
                    q14 = "UPDATE RESULT SET EXAMINATION=? where ROLL_NO=?"
                    conn.execute(q14, (up_exam, rn,))
                    print("\nEXAMINATION NAME UPDATED SUCCESSFULLY")
                else:
                    print("\nINVALID CHOICE\nCHOOSE AGAIN\n")
                    ch="y"
                    u+=1
                db.commit()
                if u==1:
                    ch=input("\nWANT TO UPDATE MORE RECORDS ? (Y/N): ")
    if u==0:
        print("\nTHIS ROLL NUMBER DOES NOT EXISTS IN RECORD")
        print("\n1. INSERT THIS INTO DATABASE\n2. BACK TO ADMIN MODE")
        sel=int(input("\nENTER CHOICE : "))
        if sel==1:
            insert_data()
        else:
            admin()

def delete_data():
    ch="y"
    while(ch=="y" or ch=="Y"):
        d=0
        rn = int(input("\nENTER THE STUDENT ROLL NUMBER TO DELETE RECORD:"))
        q0 = "SELECT * FROM STUDENT where ROLL_NO=?"
        conn.execute(q0, (rn,))
        a=conn.fetchall()
        for row in a:
            if(rn == row[0]):
                q3 = "delete from STUDENT where ROLL_NO=?"
                conn.execute(q3, (rn,))
                q4 = "delete from RESULT where ROLL_NO=?"
                conn.execute(q4, (rn,))
                print("\nRECORD DELETED SUCCESSFULLY")
                db.commit()
                d=1

                ch=input("\nWANT TO DELETE MORE RECORDS ? (Y/N) : ")
        if d==0:
            print("\nNO SUCH RECORD EXISTS IN THE DATABASE")
            admin()

def user():
    ch="y"
    while ch=="y" or ch=="Y":
        v=0
        rn=int(input("\nENTER THE ROLL NO :"))
        q1 = "SELECT * FROM STUDENT where ROLL_NO=?"
        conn.execute(q1, (rn,))
        a=conn.fetchall()
        for row in a:
            if(rn == row[0]):
                print("\nROLL NUMBER  :", row[0])
                print("STUDENT NAME :", row[1])
                print("FATHER NAME:", row[2])
                print("PHONE NUMBER :", row[3])
                print("STUDENT AGE :", row[4])
                print("DEPARTMENT :", row[5])
                v=1
            else:
                break    
        q2 = "SELECT * FROM RESULT where ROLL_NO=?"
        conn.execute(q2, (rn,))
        b=conn.fetchall()
        for row1 in b:
            if(rn==row1[0]):
                print("\nEXAMINATION NAME :", row1[1])
                print("MARKS IN PYTHON :", row1[2])
                print("MARKS IN RDBMS :", row1[3])
                print("MARKS IN CN :", row1[4])
                print("MARKS IN OS :", row1[5])
                print("MARKS IN DS :", row1[6])
                v=2
            else:
                break
        if v!=2:
            print("\nTHERE IS NO SUCH RECORD")
            sel=int(input("\n1.VIEW ANOTHER\n2.RETURN\nENTER CHOICE : "))
            if sel==1:
                ch="y"
            else:
                return
        else:
            ch=input("\nWANT TO VIEW ANOTHER RECORD ? (Y/N): ")

def login():
    username=input("\nENTER THE USERNAME :")
    if(username=="ARMAN" or username=="arman"):
        password=input("ENTER THE PASSWORD :")
        if(password=="password"):
            print("\nLOGIN SUCCESSFUL")
            admin()
        else:
            print("\nINVALID CREDENTIALS")
            login()
    else:
        print("\nINVALID CREDENTIALS")
        login()

def view():
    q1 = "SELECT * FROM STUDENT"
    conn.execute(q1)
    a=conn.fetchall()
    print("\n........STUDENT TABLE........")
    for row in a:
            print("\n\nROLL NUMBER  :", row[0])
            print("STUDENT NAME :", row[1])
            print("FATHER NAME:", row[2])
            print("PHONE NUMBER :", row[3])
            print("STUDENT AGE :", row[4])
            print("DEPARTMENT :", row[5])    
    q2 = "SELECT * FROM RESULT"
    conn.execute(q2)
    b=conn.fetchall()
    print("\n........RESULT TABLE........")
    for row1 in b:
            print("\n\nROLL NUMBER  :", row1[0])
            print("EXAMINATION NAME :", row1[1])
            print("MARKS IN PYTHON :", row1[2])
            print("MARKS IN RDBMS :", row1[3])
            print("MARKS IN CN :", row1[4])
            print("MARKS IN OS :", row1[5])
            print("MARKS IN DS :", row1[6])    

def admin():
    ch="y"
    while(ch=="y" or ch=="Y"):

        print("\n1. INSERT NEW RECORD IN DATABASE")
        print("2. UPDATE RECORD IN DATABASE")
        print("3. DELETE RECORD FROM DATABASE")
        print("4. SHOW DATABASE")
        print("5. EXIT")
        choice = int(input("\nENTER YOUR CHOICE :"))
        if (choice==1):
            insert_data()
        elif (choice== 2):
            update_data()
        elif (choice==3):
            delete_data()
        elif(choice==4):
            view()   
        elif(choice==5):
            sys.exit()
        else:
            print("\nPLEASE ENTER THE VALID CHOICE")
            admin()
        ch=input("\nWANT TO CONTINUE TO ADMIN MODE ?(Y/N) : ")

#main program
ch="y"
while(ch=="y" or ch=="Y"):
    print("\n\n..........EXAMINATION RESULT MANAGEMENT SYSYTEM............")
    print("\n\n\n1. ADMINISTRATION MODE")
    print("2. USER MODE")
    print("3. EXIT")
    choice=int(input("\nENTER YOUR CHOICE :"))
    if(choice == 1):
            login()
            ch="n"
    elif(choice == 2):
            user()
            ch="n"
    elif(choice == 3):
            sys.exit()
    else:
        print("\nINVALID CHOICE")
sys.exit()
