from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox 

GUI = Tk()
GUI.title('โปรแกรมบันทึกข้อมูล')
GUI.geometry('400x500') #ขนาดโปรแกรม

L1 = Label(GUI,text='โปรแกรมบันทึกความรู้',font=('Angsana New',24),fg='Red')
L1.place(x=30,y=20)

#B1 = ttk.Button(GUI,text='แสดงจำนวนเงิน') 
#B1.pack(ipadx=20,ipady=20)

#########################################
def Button2():
    text = 'เงินคงเหลือ 600 บาท'
    messagebox.showinfo('เงินในบัญชี',text) #info,warning,error

#FB1 = Frame(GUI)#คล้ายกระดาน
FB1 = LabelFrame(GUI,text='Money') #ใส่ชื่อขอบ
FB1.place(x=100,y=150)


B2 = ttk.Button(FB1,text='แสดงจำนวนเงิน',command=Button2) 
B2.pack(ipadx=20,ipady=10)
#B2.pack(ipadx=20,ipady=10,padx=10,pady=10) ใส่ขอบกรอบ
        
##########################################
def Button3():
    text = 'Python 101, Math, Sci'
    messagebox.showinfo('วิชาที่เรียนวันที่ 10 - 20 ก.พ.',text) #info,warning,error

FB1 = Frame(GUI)
FB1.place(x=100,y=200)


B3 = ttk.Button(FB1,text='สัปดาห์นี้เรียนวิชาอะไรบ้าง',command=Button3) 
B3.pack(ipadx=20,ipady=10)
###########################################


GUI.mainloop()
