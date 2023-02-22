#ชื่อโปรแกรม writefile.py 
#1เก็บข้อมูลแบบเขียนทับ
# with open('data.txt','w',encoding='utf-8') as file:
#     file.write('hello world')
#2เก็บข้อมูลแบบจัดเก็บไปเรื่อยๆ

def writtedata():
    with open('data.txt','w',encoding='utf-8') as file:
        file.write('How are you?')
        
def adddata(text):
    with open('add-data.txt','a',encoding='utf-8') as file:
        #file.write(text)ข้อมูลจะต่อท้ายอันเก่าที่บันทึก
        file.writelines(text + '\n')#เขียนแยกเป็นบรรทัด  

#adddata('ซื้อข้าวต้มกระดูกหมูรสเลิศ'),('ซื้อเหนียวหมูน้าแต้ว'),('Buy Lilacs 10 EUR'),('Buy Dogwood 15 EUR'),('Buy Lamb Ear 12 EUR'),('Buy Ranuculus 15 EUR')

def readdata():
    with open('add-data,txt',encoding='utf-8') as file:
        #data = file.read() อ่านข้อมูลทั้้งหมด
        data = file.readlines() #export to list
        print(data)
        
readdata()