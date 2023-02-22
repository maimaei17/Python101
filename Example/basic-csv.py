import csv

def writecsv(datalist):
    with open('data.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file) #fw = file writer
        fw.writerow(datalist) # datalist = ['pen', 'pencil', 'eraser']
        
#data = ['ข้าวเหนียวหมูปิ้ง',30,'6.00 น']
#writecsv(data)

def readcsv():
    with open('data.csv',encoding='utf-8',newline='') as file:
        fr = csv.reader(file)
        data = list(fr)
    return data
data = readcsv()
print(data)