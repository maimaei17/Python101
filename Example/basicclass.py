class School: # ชื่อคลาสควรเป็นคำนามขึ้นต้นตัวใหญ่
    # Atrricute ควรตั้งชื่อเป็นชนิดคำนามคือคำวิเศษ ถ้ามีสองคำตัวแรกขึ้นต้นตัวเล็กตัวหลังใช้ตัวใหญ่
    schoolName = 'ลุงวิศวะกร สอนคำนวณ'
    
    # Constructor ฟังก์ชันตัวหนึ่งที่สามารถกำหนดค่าเริ่มต้นให้มันได้
    def __init__(self, subject='Python Programming'):  # self = keyword ตัวแปรที่อยู่ในคลาส ใช้เมื่อตัวแปรกับพารามิเตอร์ชื่อเดียวกันในคลาส
        print('ให้แสดงข้อความนี้ เมื่อมีการสร้าง Instance')
        self.subject = subject
    
    # Method ควรตั้งชื่อเป็นคำกริยา
    def hello(self):
        print('Hello welcome everyone')
        
    def teach(self):
        print(f'โรงเรียนนี้เปิดสอนวิชา : {self.subject}')

class Student(School): # การสืบทอดคลาส
    def __init__(self, fullname, level, scores, subject):
        super().__init__(subject) # ใช้สำหรับการเรียก attribute และ method จากคลาสแม่
        self.fullname = fullname
        self.level = level
        self.scores = scores
        
    def checkGrade(self):
        if self.scores >= 80:
            print(f'วิชา {self.subject} ได้เกรด A')
        elif self.scores >= 70:
            print(f'วิชา {self.subject} ได้เกรด B')
        elif self.scores >= 60:
            print(f'วิชา {self.subject} ได้เกรด C')
        elif self.scores >= 50:
            print(f'วิชา {self.subject} ได้เกรด D')
        else:
            print(f'วิชา {self.subject} ได้เกรด F')
        
# Instance
# school1 = School('Pygame') #หากมีการใส่ค่าอื่นจะดึงส่วนนี้มาใช้
# print(f'ชื่อโรงเรียน : {school1.schoolName}')
# school1.hello()
# school1.teach()
print('===================================')
student01 = Student('สมชาย ขายไก่ทอด', 12, 75, 'Math')
student01.hello()
print(f'ชื่อโรงเรียน {student01.schoolName}')
print(f'ชื่อนักเรียน {student01.fullname}')
print(f'ระดับชั้น {student01.level}')
print(f'คะแนนสอบ {student01.scores}')
student01.checkGrade()
print('===================================')
student02 = Student('สมหญิง ปิ้งไข่', 10, 68, 'Python Programming')
student02.hello()
print(f'ชื่อโรงเรียน {student02.schoolName}')
print(f'ชื่อนักเรียน {student02.fullname}')
print(f'ระดับชั้น {student02.level}')
print(f'คะแนนสอบ {student02.scores}')
student02.checkGrade()
print('===================================')
student03 = Student('ศรีนวบ กวนน้ำ', 11, 89, 'Physics')
student03.hello()
print(f'ชื่อโรงเรียน {student03.schoolName}')
print(f'ชื่อนักเรียน {student03.fullname}')
print(f'ระดับชั้น {student03.level}')
print(f'คะแนนสอบ {student03.scores}')
student03.checkGrade()