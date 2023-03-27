# import pyautogui as a
# import webbrowser
# import time

# #ENGLISH LANGUAGE 
# url = 'https://www.pinterest.com/'
# webbrowser.open(url)
# time.sleep(3)

# a.click(363,153)
# a.write('eustoma flower')
# time.sleep(2)

# a.press('enter')

# #พิมกอปปี้ ไม่เอาคำซ้ำ
# import pyperclip
# import time
# while True:
#     t = pyperclip.paste()
#     if old_text != t:
#         print(t)
#     time.sleep(2)
#     old_text = t

import pyautogui as a
import webbrowser
import pyperclip
import time
from datetime import datetime

url = 'https://google.com'
webbrowser.open(url)
time.sleep(2)

keyword = 'ไก่ฟ้า'
pyperclip.copy(keyword)
time.sleep(2)

a.hotkey('ctrl','v')
time.sleep(2)

a.press('enter')
time.sleep(2)

stamp = datetime.now().strftime('%Y-%m-%d %H%M%S')
file = 'capture-{}.png'.format(stamp)
#path = 'c:\\python311'
a.screenshot(file)