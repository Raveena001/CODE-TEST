import sqlite3
import sys
import os
os.system("")
from time import sleep

def connectDB():
    return sqlite3.connect("movies.db")

db=connectDB()
cursor=connectDB().cursor()


def createTable(db):
    tabl=cursor.execute("""SELECT * FROM sqlite_master WHERE type='table' and name="database" ; """).fetchall()
    if tabl==[]:
        cursor.execute("""CREATE TABLE IF NOT EXISTS database(movie VARCHAR(100),actor VARCHAR(100), actress VARCHAR(100), director VARCHAR(100),year INT);""")
        print('Table Created !')
        db.commit()
    else:
        print('Table Already Exists')


def checkConnection():
    if connectDB() is not None:
        print("Database Connected Successfully")
        createTable(connectDB())
    else:
        print("ERROR, No DB not connected : ")



def insertData(db):
    movie_name=input("Enter Movie Name : ")
    actor=input("Enter Actor name : ")
    actress=input("Enter Actress name : ")
    director=input("Enter Director name: ")
    year=input("Enter year of release: ")
    cmd=("""INSERT INTO database (movie,actor,actress,director,year) VALUES (?,?,?,?,?);""")
    params=(movie_name,actor,actress,director,year)
    cursor.execute(cmd,params)
    db.commit()
    print("\nData entered saved successfully. ")



def removeData(db):
    cursor.execute("""DELETE FROM database;""").fetchall()
    db.commit()
    print("Data Deleted Successfully!")



def actor():
    act=str(input("Enter Actor Name : "))
    curs=cursor.execute("""SELECT movie FROM database WHERE actor=(?);""",(act,)).fetchall()
    db.commit()
    for i in curs:
        print(i,end='')
    if curs == []:
        print("No Actor Found.")



def actress():
    act=str(input("Enter Actress Name : "))
    curs=cursor.execute("""SELECT movie FROM database WHERE actress=(?);""",(act,)).fetchall()
    db.commit()
    for i in curs:
        print(i,end='')
    if curs==[]:
         print("No Actress Found ")




def director():
    director=str(input("Enter the director name : "))
    curs=cursor.execute("""SELECT movie FROM database WHERE director=(?);""",(director,)).fetchall()
    db.commit()
    for i in curs:
        print(i,end='')
    if curs==[]:
         print("No Dicrectors Found : (")


def year():
    year=str(input("Enter the release year : "))
    curs=cursor.execute("""SELECT movie FROM database WHERE year=(?);""",(year,)).fetchall()
    db.commit()
    for i in curs:
        print(i,end='')
    if curs==[]:
         print("No Movies Found : (")




def displayDB():
    Movie =  []
    Actor = []
    Actress  = []
    Director = []
    Year = []
    data = cursor.execute("""SELECT * FROM database; """).fetchall()
    for row in data:
        Movie.append(row[0])
        Actor.append(row[1])
        Actress.append(row[2])
        Director.append(row[3])
        Year.append(row[4])
    print("Movie = ", Movie)
    print("Actor = ", Actor)
    print("Actress  = ",Actress)
    print("Director  = ", Director)
    print("Year  = ", Year)



def main():
    while(1):
        print("*                    MENU                           *")
        print(" 1. Check database connection.                       ")
        print(" 2. Insert Movie data                                ")
        print(" 3. Delete Movie                                     ")
        print(" 4. Show Movie data                                  ")
        print(" 5. Movies by Actor                                  ")
        print(" 6. Movies by Actress                                ")
        print(" 7. Movies by Director                               ")
        print(" 8. Movies of year                                   ")
        print(" 9. Exit                                             ")
        choice=input("\nEnter your choice ")
        if choice=='1':
            checkConnection()
            sleep(2)
        elif choice=='2':
            insertData(connectDB())
            sleep(2)
        elif choice=='3':
            removeData(connectDB())
            sleep(2)
        elif choice=='4':
            displayDB()
            sleep(10)
        elif choice=='5':
            actor()
            sleep(2)
        elif choice=='6':
            actress()
            sleep(2)
        elif choice=='7':
            director()
            sleep(2)
        elif choice=='8':
            year()
            sleep(2)
        elif choice=='9':
            print("Thank you...")
            sleep(2)
            exit()
            break
        else:
            print("Invalid Choice !")
            sleep(2)
main()