from tkinter import *
from tkinter import ttk


root = Tk()
root.geometry('900x400')


def raise_frame(frame):
    frame.tkraise()
    k=str(a.get())
    x=str(b.get())
    y=str(c.get())
    z=str(d.get())
    Label(f3, text='name:   '+k,font=('Arial',20)).grid(row=1, column=0)
    Label(f3, text='Rollno:   '+x,font=('Arial',20)).grid(row=2, column=0)
    Label(f3, text='                                                            Class:  '+y,font=('Arial',20)).grid(row=1, column=1)
    Label(f3, text='                                                            Section:  '+z,font=('Arial',20)).grid(row=2, column=1)
    Label(f3, text='===============================================================',font=('Arial',20)).place(x=0,y=70)
    ttk.Button(f3, text='show results',command=lambda:[r(),r1(),r2(),r3(),r4(),r5()]).place(x=0,y=110)


f1 = Frame(root)
f2 = Frame(root)
f3 = Frame(root)

for frame in (f1, f2, f3):
    frame.grid(row=0, column=0, sticky=(N, W, E, S))


def r():
        Label(f3, text='Grade in Maths:',font=('Arial',15)).place(x=0, y=150)
        n=int(e.get())
        if n<50 :
                Label(f3, text='F',font=('Arial',15)).place(x=300, y=150)
        elif 90<=n<100:
                Label(f3, text='A',font=('Arial',15)).place(x=300, y=150)
        elif 80<=n<90:
                Label(f3, text='B',font=('Arial',15)).place(x=300, y=150)
        elif 70<=n<80:
                Label(f3, text='C',font=('Arial',15)).place(x=300, y=150)
        elif 60<=n<70:
                Label(f3, text='D',font=('Arial',15)).place(x=300, y=150)
        elif 50<=n<60:
                Label(f3, text='E',font=('Arial',15)).place(x=300, y=150)

def r1():
        Label(f3, text='Grade in Social:',font=('Arial',15)).place(x=0, y=190)
        n1=int(f.get())
        if n1<50 :
                Label(f3, text='F',font=('Arial',15)).place(x=300, y=190)
        elif 90<=n1<100:
                Label(f3, text='A',font=('Arial',15)).place(x=300, y=190)
        elif 80<=n1<90:
                Label(f3, text='B',font=('Arial',15)).place(x=300, y=190)
        elif 70<=n1<80:
                Label(f3, text='C',font=('Arial',15)).place(x=300, y=190)
        elif 60<=n1<70:
                Label(f3, text='D',font=('Arial',15)).place(x=300, y=190)
        elif 50<=n1<60:
                Label(f3, text='E',font=('Arial',15)).place(x=300, y=190)
        
def r2():
        Label(f3, text='Grade in science:',font=('Arial',15)).place(x=0, y=230)
        n3=int(g.get())
        if n3<50 :
                Label(f3, text='F',font=('Arial',15)).place(x=300, y=230)
        elif 90<=n3<100:
                Label(f3, text='A',font=('Arial',15)).place(x=300, y=230)
        elif 80<=n3<90:
                Label(f3, text='B',font=('Arial',15)).place(x=300, y=230)
        elif 70<=n3<80:
                Label(f3, text='C',font=('Arial',15)).place(x=300, y=230)
        elif 60<=n3<70:
                Label(f3, text='D',font=('Arial',15)).place(x=300, y=230)
        elif 50<=n3<60:
                Label(f3, text='E',font=('Arial',15)).place(x=300, y=230)

def r3():
        Label(f3, text='Grade in english:',font=('Arial',15)).place(x=0, y=270)
        n4=int(h.get())
        if n4<50 :
                Label(f3, text='F',font=('Arial',15)).place(x=300, y=270)
        elif 90<=n4<100:
                Label(f3, text='A',font=('Arial',15)).place(x=300, y=270)
        elif 80<=n4<90:
                Label(f3, text='B',font=('Arial',15)).place(x=300, y=270)
        elif 70<=n4<80:
                Label(f3, text='C',font=('Arial',15)).place(x=300, y=270)
        elif 60<=n4<70:
                Label(f3, text='D',font=('Arial',15)).place(x=300, y=270)
        elif 50<=n4<60:
                Label(f3, text='E',font=('Arial',15)).place(x=300, y=270)
        
def r4():
        Label(f3, text='Grade in language:',font=('Arial',15)).place(x=0, y=310)
        n5=int(i.get())
        if n5<50 :
                Label(f3, text='F',font=('Arial',15)).place(x=300, y=310)
        elif 90<=n5<100:
                Label(f3, text='A',font=('Arial',15)).place(x=300, y=310)
        elif 80<=n5<90:
                Label(f3, text='B',font=('Arial',15)).place(x=300, y=310)
        elif 70<=n5<80:
                Label(f3, text='C',font=('Arial',15)).place(x=300, y=310)
        elif 60<=n5<70:
                Label(f3, text='D',font=('Arial',15)).place(x=300, y=310)
        elif 50<=n5<60:
                Label(f3, text='E',font=('Arial',15)).place(x=300, y=310)       
def r5():
    n=int(e.get())
    n1=int(f.get())
    n3=int(g.get())
    n4=int(h.get())
    n5=int(i.get())
    t1=str(n+n1+n3+n4+n5)
    t2=int(n+n1+n3+n4+n5)
    t3=int(t2/5)
    Label(f3, text='Total Marks Optained:    '+t1,font=('Arial',20)).place(x=450, y=150)
    Label(f3, text='Overall Grade:   ',   font=('Arial',20)).place(x=450, y=200)

    if t3<50 :
                Label(f3, text='F',font=('Arial',20)).place(x=750, y=200)
    elif 90<=t3<100:
                Label(f3, text='A',font=('Arial',20)).place(x=750, y=200)
    elif 80<=t3<90:
                Label(f3, text='B',font=('Arial',20)).place(x=750, y=200)
    elif 70<=t3<80:
                Label(f3, text='C',font=('Arial',20)).place(x=750, y=200)
    elif 60<=t3<70:
                Label(f3, text='D',font=('Arial',20)).place(x=750, y=200)
    elif 50<=t3<60:
                Label(f3, text='E',font=('Arial',20)).place(x=750, y=200)       

#first slide
Label(f1,text='Grade Calculator',font=('Arial',50,'bold'),bd=1).grid(row=1, column=0)
Label(f1, text='        Enter your name:                    ',font=('Arial',30)).grid(row=2, column=0)
a=Entry(f1,bd=5,font=('arial'))
Label(f1, text='      Enter your rollno:                  ',font=('Arial',30)).grid(row=3, column=0)
b=Entry(f1,bd=5,font=('arial'))
Label(f1, text='        Enter your class:                    ',font=('Arial',30)).grid(row=4, column=0)
c=Entry(f1,bd=5,font=('arial'))
Label(f1, text='      Enter your sec:                    ',font=('Arial',30)).grid(row=5, column=0)
d=Entry(f1,bd=5,font=('arial'))
Button(f1, text='Continue', command=lambda:raise_frame(f2),width=15,height=3).grid(row=6,column=1)
a.grid(row=2, column=1)
b.grid(row=3, column=1)
c.grid(row=4, column=1)
d.grid(row=5, column=1)
                                                                      


#second slide
Label(f2,text='(out of 100)',font=('Arial',40,'bold'),bd=1).grid(row=1, column=0)
Label(f2, text=' Enter your marks in maths:          ',font=('Arial',30)).grid(row=2,column=0)
e=Entry(f2,bd=5,font=('arial'))
Label(f2, text=' Enter your marks in social:          ',font=('Arial',30)).grid(row=3, column=0)
f=Entry(f2,bd=5,font=('arial'))
Label(f2, text='  Enter your marks in science:           ',font=('Arial',30)).grid(row=4, column=0)
g=Entry(f2,bd=5,font=('arial'))
Label(f2, text=' Enter your marks in english:         ',font=('Arial',30)).grid(row=5, column=0)
h=Entry(f2,bd=5,font=('arial'))
Label(f2, text='  Enter your marks in language:         ',font=('Arial',30)).grid(row=6, column=0)
i=Entry(f2,bd=5,font=('arial'))
Button(f2, text='Continue', command=lambda:raise_frame(f3),width=15,height=3).grid(row=7, column=1)
e.grid(row=2, column=1)
f.grid(row=3, column=1)
g.grid(row=4, column=1)
h.grid(row=5, column=1)
i.grid(row=6, column=1)


raise_frame(f1)
root.mainloop()
