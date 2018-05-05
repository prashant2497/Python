from tkinter import *
prashant=Tk()
count=0
def addrec():
    f=open('text_database.txt','a')
    Player_Name=s1.get()
    Team_Name=s2.get()
    Goal_Scored=s3.get()
    Assists=s4.get()
    Matches_Played=s5.get()
    f.writelines(Player_Name.ljust(20)+Team_Name.ljust(10)+Goal_Scored.ljust(30)+Assists.ljust(15)+Matches_Played.ljust(15)+"\n")
    f.close()
def nextrec():
    f=open('text_database.txt','r')
    i=0
    global count
    while(i<=count):
        l=f.readline()
        i=i+1
    l1=l.split()
    # print(l1[0],l1[1])  # If we want to print on console screen
    s1.set(l1[0]) 
    s2.set(l1[1])
    s3.set(l1[2])
    s4.set(l1[3])
    s5.set(l1[4])
    count=count+1
    f.close()
def prev():
    f=open('text_database.txt','r')
    i=0
    global count
    while(i<=count):
        l=f.readline()
        i=i+1
    l1=l.split()
    # print(l1[0],l1[1])  # If we want to print on console screen
    s1.set(l1[0]) 
    s2.set(l1[1])
    s3.set(l1[2])
    s4.set(l1[3])
    s5.set(l1[4])
    count=count-1
    f.close()  
def up():
    Player_Name=s1.get()
    Team_Name=s2.get()
    Goal_Scored=s3.get()
    Assists=s4.get()
    Matches_Played=s5.get()
    f=open("text_database.txt","r")
    h=f.readlines()
    f.close()
    f=open("text_database.txt","w")
    flag=0
    for i in h:
        j=i.split()
        if(j[0]!=Player_Name):
            f.writelines(j[0].ljust(20)+j[1].ljust(10)+j[2].ljust(30)+j[3].ljust(15)+j[4].ljust(15)+"\n")
        else :
            f.writelines(Player_Name.ljust(20)+Team_Name.ljust(10)+Goal_Scored.ljust(30)+Assists.ljust(15)+Matches_Played.ljust(15)+"\n")
            flag=1
    f.close()
def delete():
    k=[s1.get(), s2.get(), s3.get(), s4.get(), s5.get()]
    f=open("text_database.txt","r")
    h=f.readlines()
    f.close()
    f=open("text_database.txt","w")
    for i in h:
        j=i.split()
        if(j!=k):
            f.writelines(j[0].ljust(20)+j[1].ljust(10)+j[2].ljust(30)+j[3].ljust(15)+j[4].ljust(15)+"\n")
    f.close()
def search():
    k=s1.get()
    f=open("text_database.txt","r")
    h=f.readlines()
    for i in h:
        j=i.split()
        if(j[0]==k):
            s1.set(j[0])
            s2.set(j[1])
            s3.set(j[2])
            s4.set(j[3])
            s5.set(j[4])
    f.close()
def lr():
    Player_Name=s1.get()
    Team_Name=s2.get()
    Goal_Scored=s3.get()
    Assists=s4.get()
    Matches_Played=s5.get()
    f=open('text_database.txt','r')
    a=0
    b=0
    for i in f:
        a=a+1
    f.seek(0)
    h=f.readlines()
    l=list(h)
    j=l[a-1].split()
    h=f.readline()
    m=h.split() 
    Player_Name.set(j[0]) 
    Team_Name.set(j[1]) 
    Goal_Scored.set(j[2]) 
    Assists.set(j[3]) 
    Matches_Played.set(j[4])
    f.close()
def fr():
    f=open('text_database.txt','r')
    l=f.readlines
    l1=l[0].split()
    s1.set(l1[0]) 
    s2.set(l1[1])
    s3.set(l1[2])
    s4.set(l1[3])
    s5.set(l1[4])
s1=StringVar()
s2=StringVar()
s3=StringVar()
s4=StringVar()
s5=StringVar()
l0=Label(prashant,text="---------Football Stats--------")
l1=Label(prashant,text="Player_Name")
l2=Label(prashant,text="Team_Name")
l3=Label(prashant,text="Goal_Scored ")
l4=Label(prashant,text="Assists.")
l5=Label(prashant,text="Matches_Played")
t1=Entry(prashant,textvariable=s1)
t2=Entry(prashant,textvariable=s2)
t3=Entry(prashant,textvariable=s3)
t4=Entry(prashant,textvariable=s4)
t5=Entry(prashant,textvariable=s5)
l0.grid(row=1,column=2)
l1.grid(row=2,column=1)
l2.grid(row=3,column=1)
l3.grid(row=4,column=1)
l4.grid(row=5,column=1)
l5.grid(row=6,column=1)
t1.grid(row=2,column=2)
t2.grid(row=3,column=2)
t3.grid(row=4,column=2)
t4.grid(row=5,column=2)
t5.grid(row=6,column=2)
b1=Button(prashant,text="Next", command=nextrec)
b2=Button(prashant,text="Add", command=addrec)
b3=Button(prashant,text="Delete", command=delete)
b4=Button(prashant,text="Search", command=search)
b5=Button(prashant,text="Up", command=up)
b7=Button(prashant,text="Last Record", command=lr)
b6=Button(prashant,text="First Record", command=fr)
b8=Button(prashant,text="Previous", command=prev)
b1.grid(row=2,column=3)
b2.grid(row=3,column=3)
b3.grid(row=4,column=3)
b4.grid(row=5,column=3)
b5.grid(row=6,column=3)
b6.grid(row=7,column=1)
b7.grid(row=7,column=2)
b8.grid(row=7,column=3)
prashant.mainloop()