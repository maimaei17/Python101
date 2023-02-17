from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GM = Tk()
GM.title('โปรแกรมบันทึกข้อมูล')
GM.geometry('870x600')

L1 = Label(GM,text='เกมน่าสนใจประจำเดือนกุมภาพันธ์',font=('JasmineUPC',36),fg='#00425A')
L1.place(x=210,y=70)

##########

FB1 = LabelFrame(GM,text='1 - 7 กุมภาพันธ์ 2023')
FB1.place(x=70,y=200)

def Btn1():
    text = 'Deliver Us Mars\n(PC, PS4, PS5, Xbox One, Xbox Series X/S)'
    messagebox.showinfo('2 กุมภาพันธ์ 2023',text)

B1 = ttk.Button(FB1,text='2 กุมภาพันธ์ 2023',command=Btn1)
B1.pack(ipadx=20,ipady=10)

def Btn2():
    text = 'Dead Island 2\n(PC, PS4, PS5, Xbox One, Xbox Series X/S)'
    messagebox.showinfo('3 กุมภาพันธ์ 2023',text)

B2 = ttk.Button(FB1,text='3 กุมภาพันธ์ 2023',command=Btn2)
B2.pack(ipadx=20,ipady=10)

###############

FB2 = LabelFrame(GM,text='8 - 14 กุมภาพันธ์ 2023')
FB2.place(x=270,y=200)

def Btn3():
    text = 'Hogwarts Legacy\n(PC, PS5, Xbox Series X/S)'
    messagebox.showinfo('11 กุมภาพันธ์ 2023',text)

B3 = ttk.Button(FB2,text='11 กุมภาพันธ์ 2023',command=Btn3)
B3.pack(ipadx=20,ipady=10)

def Btn4():
    text = 'Wanted: Dead\n(PC, PS4, PS5, Xbox One, Xbox Series X/S)'
    messagebox.showinfo('14 กุมภาพันธ์ 2023',text)

B4 = ttk.Button(FB2,text='14 กุมภาพันธ์ 2023',command=Btn4)
B4.pack(ipadx=20,ipady=10)

#################

FB3 = LabelFrame(GM,text='15 - 21 กุมภาพันธ์ 2023')
FB3.place(x=470,y=200)

def Btn5():
    text = 'Wild Hearts\n(PC, PS5, Xbox Series X/S)'
    messagebox.showinfo('17 กุมภาพันธ์ 2023',text)

B5 = ttk.Button(FB3,text='17 กุมภาพันธ์ 2023',command=Btn5)
B5.pack(ipadx=20,ipady=10)

def Btn6():
    text = 'Atomic Heart\n(PC, PS4, PS5, Xbox One, Xbox Series X/S)\n\nLike A Dragon: Ishin!\n(PC, PS4, PS5, Xbox One, Xbox Series X/S)'
    messagebox.showinfo('21 กุมภาพันธ์ 2023',text)

B6 = ttk.Button(FB3,text='21 กุมภาพันธ์ 2023',command=Btn6)
B6.pack(ipadx=20,ipady=10)

###################

FB4 = LabelFrame(GM,text='22 - 28 กุมภาพันธ์ 2023')
FB4.place(x=670,y=200)

def Btn7():
    text = 'Company of Heroes 3\n(PC)\n\nSons of the Forest\n(PC)'
    messagebox.showinfo('23 กุมภาพันธ์ 2023',text)

B7 = ttk.Button(FB4,text='23 กุมภาพันธ์ 2023',command=Btn7)
B7.pack(ipadx=20,ipady=10)

###################

GM.mainloop()
