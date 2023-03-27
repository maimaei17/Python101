import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk,Image

##################CSV##########
import csv

def writecsv(datalist):
    with open('customerInformation.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file)
        fw.writerow(datalist)

def readcsv():
    with open('customerInformation.csv',encoding='utf-8',newline='') as file:
        fr = csv.reader(file)
        data = list(fr)
    return data
data = readcsv()
print(data)

#################################

FS = tkinter.Tk()
FS.title("โปรแกรมการสั่งช่อดอกไม้")
# FS.geometry('1200x500')

frame = ttk.Frame(FS)
frame.pack()

Name_label = tkinter.Label(frame, text="MUUMUU's Flower Shop",font=('JasmineUPC',28),fg='#F886A8')
Name_label.grid(row=0, column=0)

# bouquet info
bouquet_info_frame = tkinter.LabelFrame(frame, text="ข้อมูลช่อดอกไม้",font=('JasmineUPC',14), fg='#D86511')
bouquet_info_frame.grid(row=1,column=0)

bouquet_type_label = tkinter.Label(bouquet_info_frame, text="ลักษณะช่อ",font=('JasmineUPC',12))
bouquet_type_label.grid(row=2, column=0)
bouquet_type_combobox = ttk.Combobox(bouquet_info_frame, values=["", "Cascade", "Posy", "Round", "Crescent", "Nosegay", "Presentation", "Basket", "Shower"])
bouquet_type_combobox.grid(row=3, column=0)

bouquet_color_label = tkinter.Label(bouquet_info_frame, text="โทนสี",font=('JasmineUPC',12))
bouquet_color_label.grid(row=2, column=1)
bouquet_color_combobox = ttk.Combobox(bouquet_info_frame, values=["", "White/Ivory/Creme", "Earth Tone", "Yellows", "Peach", "Orange", "Muave/Dusty", "Pink", "Red", "Burgundy/Plum", "Purple/Lavender", "Blue", "Green", "Pastel"])
bouquet_color_combobox.grid(row=3, column=1,ipadx=60)

special_flower_label = tkinter.Label(bouquet_info_frame, text="*ดอกไม้ที่ต้องการเป็นพิเศษ",font=('JasmineUPC',12))
special_flower_label.grid(row=4, column=0)
special_flower_entry = tkinter.Entry(bouquet_info_frame)
special_flower_entry.grid(row=4, column=1, ipadx=70)

# Card
card_label = tkinter.Label(bouquet_info_frame, text="การ์ดอวยพร",font=('JasmineUPC',12))
card_check = ttk.Combobox(bouquet_info_frame, values=["", "แนบการ์ด", "ไม่แนบการ์ด"])
card_label.grid(row=5,column=0)
card_check.grid(row=6,column=0)

card_detail_label = tkinter.Label(bouquet_info_frame, text="ข้อความอวยพร")
card_detail_entry = tkinter.Entry(bouquet_info_frame)
card_detail_label.grid(row=5,column=1)
card_detail_entry.grid(row=6,column=1,ipadx=70)

# form control
for widget in bouquet_info_frame.winfo_children():
    widget.grid_configure(padx=16, pady=5)

# customer info
customer_info_frame = tkinter.LabelFrame(frame, text="ข้อมูลลูกค้า",font=('JasmineUPC',14), fg='#783030')
customer_info_frame.grid(row=2,column=0, padx=20,pady=20)

customer_n_label = tkinter.Label(customer_info_frame, text="ชื่อ - สกุล",font=('JasmineUPC',12))
customer_n_label.grid(row=1, column=0)
customer_tel_label = tkinter.Label(customer_info_frame, text="เบอร์ติดต่อ",font=('JasmineUPC',12))
customer_tel_label.grid(row=1, column=1)

customer_n_entry = tkinter.Entry(customer_info_frame)
customer_n_entry.grid(row=2, column=0)
customer_tel_entry = tkinter.Entry(customer_info_frame)
customer_tel_entry.grid(row=2, column=1)

shipping_label = tkinter.Label(customer_info_frame, text="การรับสินค้า",font=('JasmineUPC',12))
shipping_label.grid(row=1, column=2)
shipping_combobox = ttk.Combobox(customer_info_frame, values=["","มารับเอง","นำส่งสินค้า"])
shipping_combobox.grid(row=2, column=2)

# receiver info
receiver_label= tkinter.Label(customer_info_frame, text="ข้อมูลที่อยู่ผู้รับ",font=('JasmineUPC',14))
receiver_label.grid(row=3,column=0)

receiver_n_label = tkinter.Label(customer_info_frame, text="ชื่อผู้รับ",font=('JasmineUPC',12))
receiver_n_label.grid(row=4, column=0)
receiver_n_entry = tkinter.Entry(customer_info_frame)
receiver_n_entry.grid(row=5, column=0)

receiver_date_label = tkinter.Label(customer_info_frame, text="วัน/เวลา(จัดส่ง/มารับ)",font=('JasmineUPC',12))
receiver_date_label.grid(row=4, column=1)
receiver_date_entry = tkinter.Entry(customer_info_frame)
receiver_date_entry.grid(row=5, column=1)

# add receiver
receiver_bldg_label = tkinter.Label(customer_info_frame, text="สำนักงาน/อาคาร",font=('JasmineUPC',12))
receiver_bldg_label.grid(row=6, column=0)
receiver_bldg_entry = tkinter.Entry(customer_info_frame,width=70)
receiver_bldg_entry.grid(row=7, columnspan=3)

receiver_number_label = tkinter.Label(customer_info_frame, text="เลขที่",font=('JasmineUPC',12))
receiver_number_label.grid(row=8, column=0)
receiver_number_entry = tkinter.Entry(customer_info_frame)
receiver_number_entry.grid(row=9, column=0)

receiver_villageNo_label = tkinter.Label(customer_info_frame, text="หมู่ที่",font=('JasmineUPC',12))
receiver_villageNo_label.grid(row=8, column=1)
receiver_villageNo_entry = tkinter.Entry(customer_info_frame)
receiver_villageNo_entry.grid(row=9, column=1)

receiver_lane_label = tkinter.Label(customer_info_frame, text="ตรอก/ซอย/ถนน",font=('JasmineUPC',12))
receiver_lane_label.grid(row=8, column=2)
receiver_lane_entry = tkinter.Entry(customer_info_frame)
receiver_lane_entry.grid(row=9, column=2)

receiver_sub_district_label = tkinter.Label(customer_info_frame, text="ตำบล/แขวง",font=('JasmineUPC',12))
receiver_sub_district_label.grid(row=10, column=0)
receiver_sub_district_entry = tkinter.Entry(customer_info_frame)
receiver_sub_district_entry.grid(row=11, column=0)

receiver_district_label = tkinter.Label(customer_info_frame, text="อำเภอ/เขต",font=('JasmineUPC',12))
receiver_district_label.grid(row=10, column=1)
receiver_district_entry = tkinter.Entry(customer_info_frame)
receiver_district_entry.grid(row=11, column=1)

receiver_province_label = tkinter.Label(customer_info_frame, text="จังหวัด",font=('JasmineUPC',12))
receiver_province_label.grid(row=10, column=2)
receiver_province_entry = tkinter.Entry(customer_info_frame)
receiver_province_entry.grid(row=11, column=2)

receiver_postcode_label = tkinter.Label(customer_info_frame, text="รหัสไปรษณีย์",font=('JasmineUPC',12))
receiver_postcode_label.grid(row=12, column=0)
receiver_postcode_entry = tkinter.Entry(customer_info_frame)
receiver_postcode_entry.grid(row=13, column=0)

receiver_tel_label = tkinter.Label(customer_info_frame, text="เบอร์ติดต่อ",font=('JasmineUPC',12))
receiver_tel_label.grid(row=12, column=1)
receiver_tel_entry = tkinter.Entry(customer_info_frame)
receiver_tel_entry.grid(row=13, column=1)

# form control
for widget in customer_info_frame.winfo_children():
    widget.grid_configure(padx=8, pady=5)

from datetime import datetime

def confirm_data():
    t = datetime.now().strftime('%Y%m%d %H%M%S')
    # bouquet
    bouquet_type = bouquet_type_combobox.get()
    bouquet_color = bouquet_color_combobox.get()
    special_flower = special_flower_entry.get()
    card = card_check.get()
    card_detail = card_detail_entry.get()
    # customer order
    customer_name = customer_n_entry.get()
    customer_tel = customer_tel_entry.get()
    shipping = shipping_combobox.get()
    # receiver
    receiver_name = receiver_n_entry.get()
    receiver_date = receiver_date_entry.get()
    receiver_bldg = receiver_bldg_entry.get()
    receiver_number = receiver_number_entry.get()
    receiver_villageNo = receiver_villageNo_entry.get()
    receiver_lane = receiver_lane_entry.get()
    receiver_sub_district = receiver_sub_district_entry.get()
    receiver_district = receiver_district_entry.get()
    receiver_province = receiver_province_entry.get()
    receiver_postcode = receiver_postcode_entry.get()
    receiver_tel = receiver_tel_entry.get()
    
    information = [t,
                   # bouquet
                   ("bouquet type: ", bouquet_type),
                   ("bouquet color: ", bouquet_color),
                   ("special flower: ", special_flower),
                   ("card: ", card),
                   ("card_detail: ", card_detail),
                   
                   # customer order
                   ("customer name: ", customer_name),
                   ("customer tel: ", customer_tel),
                   ("shipping: ", shipping),
                   
                   # receiver
                   ("receiver name: ", receiver_name),
                   ("receiver date: ", receiver_date),
                   ("receiver bldg: ", receiver_bldg),
                   ("receiver number: ", receiver_number),
                   ("receiver villageNo: ", receiver_villageNo),
                   ("receiver lane: ", receiver_lane),
                   ("receiver sub district: ", receiver_sub_district),
                   ("receiver district: ", receiver_district),
                   ("receiver province: ", receiver_province),
                   ("receiver postcode: ", receiver_postcode),
                   ("receiver tel: ", receiver_tel)]
    writecsv(information)
    
    text = 'บันทึกข้อมูลเรียบร้อยแล้ว'
    messagebox.showinfo('SAVE!',text)

    

# save btn
button = tkinter.Button(frame, text="บันทึกข้อมูล",bg='#FC9483', fg='#fff', font=('JasmineUPC',15), width=30, command= confirm_data)
button.grid(row=20, column=0, padx=20, pady=10)

FS.mainloop()