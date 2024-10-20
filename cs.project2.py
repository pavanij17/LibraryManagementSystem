
#* Module Used To connect MySQL Database To Python 
import mysql.connector as db
con = db.connect(host = "localhost",user = "root",password = "@Ganeshji05", database = "project2")

#? A SCHOOL LIBRARY MANAGEMENT SYSTEM
#* Add A a Book To The Databases
def add_book():
    bn = input(" Enter The Book Name ")
    ba = input(" Enter The Author Name ")
    bc = int(input(" Enter The Book Code "))
    t = int(input(" Enter The Total Number Of books "))
    s = input(" Enter The Subject ")
    data = (bn,ba,bc,t,s)
    query = "insert into books values(%s,%s,%s,%s,%s);"
    #! All The Values Are Inserted In The MySQL Database
    c = con.cursor()
    c.execute(query,data)
    con.commit()
    print("\n\n\n\nBook Added Successfully.........\n\n\n\n")
    wait = input("\n\n\nPress enter to continue....\n\n\n\n\n\n")

    main()
#* Issue A Book To The User
def issue_book():
    n = input(" Enter Name ")
    r = int(input(" Enter Registration Number "))
    co = int(input(" Enter Book Code "))
    d = input(" Enter Date ")
    data = (n,r,co,d)
    query = "insert into issue value(%s,%s,%s,%s); "
    #! All The Values Are Inserted In The MySQL Database
    print("\n\n\n\nBook Issued Successful to:",n)
    c = con.cursor()
    c.execute(query,data)
    con.commit()
    wait = input("\n\n\nPress enter to continue....\n\n\n\n\n\n")

    main()
#* Return A Book To The Return  
def return_book():
    n = input(" Enter Name")
    r = int(input(" Enter Registration Number "))
    co = int(input(" Enter Book Code "))
    d = input(" Enter Date ")
    query = "insert into returns value(%s,%s,%s,%s); "
    #! All The Values Are Inserted In The MySQL Database
    data = (n,r,co,d)
    print("\n\n\n\nBook Returned successfully by:",n)
    c = con.cursor()
    c.execute(query,data)
    con.commit()
    wait = input("\n\n\nPress enter to continue....\n\n\n\n\n\n")
    
    main()
#* Delete A Book From The Database  
def delete_book():
    bc = int(input(" Enter the book code "))
    query = "delete from books where bcode= %s;"
    data = (bc,)
    c = con.cursor()
    c.execute(query,data)
    con.commit()
    print("\n\n\n\n\nBook of Book Code",bc," is deleted ")
    wait = input("\n\n\nPress enter to continue....\n\n\n\n\n\n")
    main() 
#* Display All The Books Of The Database  
def display_book():
    query = "select * from books;"
    c = con.cursor()
    c.execute(query)
    display = c.fetchall()
    #! This Will Fetch All The Data From The MySQL Database
    for i in display:
        print("Book Name :", i[0])
        print("Author Name :", i[1])
        print("Book Code :", i[2])
        print("Total Books :", i[3])
        print("subject :", i[4])
        print("\n\n")
    wait = input("\n\n\nPress enter to continue....\n\n\n\n\n\n")
    main() 
def search_book():
    bn = input(" Enter The Book Name ")
    query = "select * from books where bname = %s;"
    print('\n\n')
    data = (bn,)
    c = con.cursor()
    c.execute(query,data)
    display = c.fetchall()
    for i in display:
        print("Book Name :", i[0])
        print("Author Name :", i[1])
        print("Book Code :", i[2])
        print("Total Books :", i[3])
        print("subject :", i[4])
        print("\n\n")
    wait = input("\n\n\nPress enter to continue....\n\n\n\n\n\n")
    main() 
    
    
#* This Is The Main page     
def main():
    print("""
    SCHOOL LIBRARY MANAGEMENT APPLICATION
    1. ADD BOOK
    2. ISSUE OF BOOK
    3. RETURN OF BOOK
    4. DELETE BOOK
    5. DISPLAY BOOKS
    6. SEARCH A BOOK
    7. TO LOG OUT
        """)
    #* All The Functions The Admin Can Use In This Program
    ch = input(" Enter your choice....")

    while True:     

        print("\n\n\n\n\n\n\n")
        if ch == '1':
            add_book()
        elif ch == '2':
            issue_book()
        elif ch == '3':
            return_book()
        elif ch == '4':
            delete_book()
        elif ch == '5':
            display_book()
        elif ch == '6':
            search_book()
        else:
            print(" you are now logged out ")
            break
x = input(" Enter password to log in ")
if x == "1234":
    main()
else:
    print(" Incorrect Password")
