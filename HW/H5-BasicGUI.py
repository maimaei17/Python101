from tkinter import *
from tkinter import ttk
from tkinter import messagebox

DS = Tk()
DS.title('Discount')
DS.geometry('500x400')

LH = Label(DS,text="DISCOUNT MUUMUU's Flower Shop",font=('JasmineUPC',28),fg='#00425A')
LH.place(x=60,y=20)
L1 = Label(DS,text='10% OFF of 500 THB',font=('JasmineUPC',18),fg='#F886A8')
L1.place(x=170,y=70)
L2 = Label(DS,text='15% OFF of 800 THB',font=('JasmineUPC',18),fg='#888EDD')
L2.place(x=170,y=100)
L3 = Label(DS,text='20% OFF of 1200 THB',font=('JasmineUPC',18),fg='#826FC9')
L3.place(x=170,y=130)
L4 = Label(DS,text='Over 1200 THB get 30% OFF',font=('JasmineUPC',18),fg='#761878')
L4.place(x=150,y=160)

LF1 = ttk.LabelFrame(DS,text='price: ')
LF1.place(x=150,y=200)

v_price = IntVar()
E1 = ttk.Entry(LF1,textvariable=v_price,font=('Angsana New',18))
E1.pack(padx=10,pady=10)

#price = int(input('price: '))
def disc():
    price = v_price.get()
    if price <= 500:
        dis = price*0.1
        total = price-dis
    elif price <= 800:
        dis = price*0.15
        total = price-dis
    elif price <= 1200:
        dis = price*0.2
        total = price-dis
    else:
        dis = price*0.3
        total = price-dis

    text = ('Total:' ,total,"Discount:",dis)
    messagebox.showinfo('Total Price',text)
    v_price.set('')
    # print('Discount: ',dis)
    # print('Total: ',price-dis)

#disc(price)
B1 = ttk.Button(LF1,text='Cal',command=disc)
B1.pack(ipadx=20,ipady=10)

DS.mainloop()