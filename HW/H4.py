from tkinter import *
from tkinter import ttk
from tkinter import messagebox

##################CSV#############################################################
import csv

def writecsv(datalist):
    with open('H4.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file)
        fw.writerow(datalist)

def readcsv():
    with open('H4.csv',encoding='utf-8',newline='') as file:
        fr = csv.reader(file)
        data = list(fr)
    return data
data = readcsv()
print(data)

###################################################################################

GM = Tk()
GM.title('โปรแกรมบันทึกข้อมูล')
GM.geometry('870x800')

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
FB2.place(x=70,y=350)

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
FB3.place(x=70,y=500)

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
FB4.place(x=70,y=650)

def Btn7():
    text = 'Company of Heroes 3\n(PC)\n\nSons of the Forest\n(PC)'
    messagebox.showinfo('23 กุมภาพันธ์ 2023',text)

B7 = ttk.Button(FB4,text='23 กุมภาพันธ์ 2023',command=Btn7)
B7.pack(ipadx=20,ipady=10)

###################
########SECTION RIGHT######################
LF1 = ttk.LabelFrame(GM,text='เกมที่สนใจ')
LF1.place(x=400,y=200)

v_data = StringVar() #ตัวแปรพิเศษที่ใช้กับข้อความใน GUI
E1 = ttk.Entry(LF1,textvariable=v_data,font=('Angsana New',18))
E1.pack(padx=10,pady=10)

LF2 = ttk.LabelFrame(GM,text='กรอกอีเมลเพื่อรับข้อเสนอสุดพิเศษ')
LF2.place(x=400,y=300)

v_data1 = StringVar() #ตัวแปรพิเศษที่ใช้กับข้อความใน GUI
E2 = ttk.Entry(LF2,textvariable=v_data1,font=('Angsana New',18))
E2.pack(padx=10,pady=10)

from datetime import datetime

def SaveData():
    t = datetime.now().strftime('%Y%m%d %H%M%S')
    data = v_data.get() #ดึงข้อมูลจากตัวแปร v_data มาใช้งาน
    data1 = v_data1.get()
    text = [t,data,data1] # [เวลา,ข้อมูลที่ได้จากการกรอก]
    writecsv(text) #บันทึกลง csv
    text = 'บันทึกข้อมูลเรียบร้อยแล้ว' #แสดงข้อมูลเสยๆ
    messagebox.showinfo('SAVE!',text) #แสดงข้อมูลเสยๆ
    v_data.set('') #เคลียร์ข้อมูลที่อยู่ในช่องกรอก
    v_data1.set('') #เคลียร์ข้อมูลที่อยู่ในช่องกรอก
    
B4 = ttk.Button(LF2,text='รับข้อเสนอพิเศษ',command=SaveData)
B4.pack(ipadx=20,ipady=10)

GM.mainloop()
