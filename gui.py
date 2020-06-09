from tkinter import *
import sqlite3 as db
import tkinter.messagebox

def register_user():
    username_info = username.get()
    password_info= password.get()

    conn= db.connect('user.db')
    cur= conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS DATA
    (
        Username TEXT NOT NULL,
        Password TEXT NOT NULL,
        Name TEXT,
        Branch TEXT,
        Regd_No TEXT,
        Phy TEXT,
        Chem TEXT,
        Maths TEXT,
        CGPA FLOAT,
        Grade TEXT
    )''')
    cur.execute('''insert into DATA Values("%s","%s",
    null,null,null,null,null,null,null,null)'''%(username_info,password_info))
    cur.close()
    conn.commit()
    conn.close()
    screen1.destroy()

def failed():
    tkinter.messagebox.showinfo("Error", 'Invalid Username or Password')

def save():
    conn = db.connect('user.db')
    cur = conn.cursor()
    cur.execute('''UPDATE DATA SET CGPA=="%f",Grade=="%s"
           WHERE Username == "%s" AND Password =="%s"''' % (c, g, username1, password1))
    cur.close()
    conn.commit()
    conn.close()


def new():
    save()
    screen.destroy()
    main_screen()

def close():
    save()
    screen4.destroy()
    screen.destroy()

def grade():
    global g
    if 9.0<c<=10.0:
        g="O"
    elif 8.0<c<=9.0:
        g="E"
    elif 7.0<c<=8.0:
        g="A"
    elif 6.0<c<=7.0:
        g="B"
    elif 5.0<c<=6.0:
        g="C"
    elif 4.0<c<=5.0:
        g="D"
    elif c<=4.0:
        g="F"

    Label(screen4, text=("Grade:", g)).pack()
    Label(screen4, text="").pack()

def cgpa():
    Label(screen4, text=("CGPA:",c)).pack()
    Label(screen4, text="").pack()

def mark():
    global c
    global screen4
    screen3.destroy()
    screen4= Toplevel()
    screen4.title("GUI-3")
    screen4.geometry("400x400")
    Label(screen4, text="").pack()
    x=physics1.get()
    y=chem1.get()
    z=math1.get()
    sum= (x/10)+(y/10)+(z/10)
    a = sum/3
    c= round(a,2)
    Button(screen4, text="CGPA", height="1", width="10",command=cgpa).pack()
    Label(screen4, text="").pack()
    Button(screen4, text="Grade", height="1", width="10", command=grade).pack()
    Label(screen4, text="").pack()
    Button(screen4, text="New Input", height="1", width="10", command=new).pack()
    Label(screen4, text="").pack()
    Button(screen4, text="Close", height="1", width="10", command=close).pack()
    Label(screen4, text="").pack()


def put():
    phy1 = physics1.get()
    chem3 = chem1.get()
    math3 = math1.get()
    conn = db.connect('user.db')
    cur = conn.cursor()
    cur.execute('''UPDATE DATA SET Phy=="%s",Chem=="%s",Maths=="%s"
       WHERE Username == "%s" AND Password =="%s"''' %(phy1, chem3, math3, username1, password1))
    cur.close()
    conn.commit()
    conn.close()
    mark()


def math():
    global math1
    math1 = IntVar()
    Label(screen3, text="").pack()
    Label(screen3, text="Maths").pack()
    math2 = Entry(screen3, textvariable=math1)
    math2.pack()
    Label(screen3, text="").pack()
    Button(screen3, text="Submit", height="1", width="10", command=put).pack()


def chem():
    global chem1
    chem1 = IntVar()
    Label(screen3, text="").pack()
    Label(screen3, text="Chemistry").pack()
    chem2 = Entry(screen3, textvariable=chem1)
    chem2.pack()

def physics():
    global physics1
    physics1 = IntVar()
    Label(screen3, text="").pack()
    Label(screen3, text="Physics").pack()
    physics2 = Entry(screen3, textvariable=physics1)
    physics2.pack()


def subject():
    global screen3
    screen2.destroy()
    screen3 = Toplevel()
    screen3.title("GUI-2")
    screen3.geometry("500x500")
    Label(screen3, text="").pack()
    Label(screen3, text="Fill Up The Marks Obtained", width="100", height="2").pack()
    Label(screen3,text="").pack()
    Button(screen3,text="Physics", height="1", width="10", command=physics).pack()
    Label(screen3, text="").pack()
    Button(screen3, text="Chemistry", height="1", width="10", command=chem).pack()
    Label(screen3, text="").pack()
    Button(screen3, text="Maths", height="1", width="10", command=math).pack()
    Label(screen3, text="").pack()
    Label(screen3, text="Clear The 0 In The Entry And Then Type Your Marks").pack()


def data():
    name1=name.get()
    branch1=branch.get()
    regd1=regd.get()
    conn = db.connect('user.db')
    cur = conn.cursor()
    cur.execute('''UPDATE DATA SET Name=="%s",Branch=="%s",Regd_No=="%s"
    WHERE Username == "%s" AND Password =="%s"'''%(name1,branch1,regd1,username1,password1))
    cur.close()
    conn.commit()
    conn.close()
    subject()

def login_sucess():
    global screen2
    global name
    global branch
    global regd
    screen2 = Toplevel()
    screen2.title("GUI-1")
    screen2.geometry("500x450")
    name= StringVar()
    branch = StringVar()
    regd= StringVar()
    Label(screen2,text="Register", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Name").pack()
    Label(screen2, text="").pack()
    name_entry = Entry(screen2, textvariable=name)
    name_entry.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Branch").pack()
    Label(screen2, text="").pack()
    branch_entry = Entry(screen2, textvariable=branch)
    branch_entry.pack()
    Label(screen2, text="").pack()
    Label(screen2, text="Registration No.").pack()
    Label(screen2, text="").pack()
    regd_entry = Entry(screen2, textvariable=regd)
    regd_entry.pack()
    Label(screen2, text="").pack()
    Button(screen2, text="Submit", height="1", width="10",command=data).pack()
    Label(screen2, text="").pack()


def login_verify():
    global username1
    global password1
    username1= username_verify.get()
    password1= password_verify.get()
    conn = db.connect('user.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM DATA WHERE Username == '%s' AND Password =='%s'"%(username1,password1))
    list0 = cur.fetchone()
    if list0 is not None:
        login_sucess()
    else:
        failed()
    cur.close()
    conn.close()


def register():
    global screen1
    screen1=Toplevel()
    screen1.title("Sign-in")
    screen1.geometry("400x350")
    global username
    global password
    global username_entry
    global password_entry
    username= StringVar()
    password= StringVar()
    Label(screen1,text="Sign In", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
    Label(screen1, text="").pack()
    Label(screen1,text="Username").pack()
    username_entry= Entry(screen1,textvariable=username)
    username_entry.pack()
    Label(screen1, text="").pack()
    Label(screen1,text="Password").pack()
    password_entry= Entry(screen1,textvariable=password,show="*")
    password_entry.pack()
    Label(screen1,text="").pack()
    Button(screen1,text="Sign In", height="1", width="10",command=register_user).pack()

def login():
    screen.title("Login")
    screen.geometry("500x500")
    global username_verify
    global password_verify
    global username_entry1
    global password_entry1
    username_verify = StringVar()
    password_verify = StringVar()
    Label(text="").pack()
    Label(text="Login", bg="grey", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Label(screen,text="Username").pack()
    username_entry1=Entry(screen,textvariable=username_verify)
    username_entry1.pack()
    Label(screen, text="").pack()
    Label(screen,text="Password").pack()
    password_entry1=Entry(screen,textvariable=password_verify,show="*")
    password_entry1.pack()
    Label(screen,text="").pack()
    Button(screen,text="Login", height="1", width="10",command=login_verify).pack()


def main_screen():
    global screen
    screen= Tk()
    screen.geometry("500x500")
    screen.title("LOGIN")
    Label(text="").pack()
    Button(text="Login",height="2",width="30",command=login).pack()
    Label(text="").pack()
    Button(text="Sign In",height="2",width="30",command=register).pack()
    screen.mainloop()

main_screen()