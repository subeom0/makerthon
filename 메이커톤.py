# -*- coding:utf-8 -*-
import pymysql
from gtts import gTTS
from playsound import playsound
import os
import time

class 코카콜라:
    data1 = [0,0,0]
    data2 = [0,0,0]

class 펩시콜라:
    data1 = [0,0,0]
    data2 = [0,0,0]

class 칠성사이다:
    data1 = [0,0,0]
    data2 = [0,0,0]
    
class 환타:
    data1 = [0,0,0]
    data2 = [0,0,0]

class 포카리스웨트:
    data1 = [0,0,0]
    data2 = [0,0,0]

class 솔의눈:
    data1 = [0,0,0]
    data2 = [0,0,0]

def update코카콜라():
    k = 0
    no = 0
    
    up = pymysql.connect(host = 'localhost', user = 'subeom', password = 'dkstnqja123@',db = '코카콜라')
    update = up.cursor()

    money = "SELECT * FROM 가격" 
    day = "SELECT 기간 FROM 행사정보"   
    event = "SELECT 행사 FROM 행사정보"
	     
    update.execute(money)
    a = update.fetchall()
    print('가격 :'+ str(a[0][0]))

    update.execute(day)
    b = update.fetchall()
    print('기간 :'+ str(b[0][0]))
	    
    update.execute(event)
    c = update.fetchall()
    print('행사 :'+ str(c[0][0]))

#가격정보 받고 처리
    update.execute("select * from 가격")
    코카콜라.data1[0] = update.fetchall()
    if(코카콜라.data2[0] != 코카콜라.data1[0]):
        no = 1
        print('가격변경됨')
        코카콜라.data2[0] = 코카콜라.data1[0]
    else:
        print("가격변경X")
        코카콜라.data2[0] = 코카콜라.data1[0]
#가격정보 처리 끝
        
#기간정보 처리
    update.execute("select 기간 from 행사정보")
    코카콜라.data1[1] = update.fetchall()
    if(코카콜라.data2[1] != 코카콜라.data1[1]):
        no = 1
        print('기간변경됨')
        코카콜라.data2[1] = 코카콜라.data1[1]
    else:
        print("기간변경X")
        코카콜라.data2[1] = 코카콜라.data1[1]
#기간정보 처리 끝
#행사정보 처리
    
    update.execute("select 행사 from 행사정보")
    코카콜라.data1[2] = update.fetchall()
    if(코카콜라.data2[2] != 코카콜라.data1[2]):
        no = 1
        print('행사변경됨')
        코카콜라.data2[2] = 코카콜라.data1[2]
    else:
        print("행사변경X")
        코카콜라.data2[2] = 코카콜라.data1[2]
        
#행사정보 처리 끝        
    if(no == 1):    
        if os.path.isfile("1.mp3"):
            print('remove')
            os.remove("1.mp3")
        if(b[0][0] == '행사가 없습니다'):
            text = '이 제품의 이름은 코카콜라이고 가격은' +str(a[0][0]) + '원 입니다'+' 해당제품은 행사가 없습니다'
            print(text)
        else:    
            text = '이 제품의 이름은 코카콜라이고 가격은' + str(a[0][0]) + '원 입니다' + str(b[0][0]) + '까지' + str(c[0][0]) + '행사를 진행중입니다.'
            print(text)
        tts = gTTS(text=text, lang='ko')
        tts.save("1.mp3")

    update.execute("select * from 위치")
    코카콜라위치 = update.fetchall()
        
    update.close()
    return 코카콜라위치    

def update칠성사이다():

    k = 0
    no = 0
    up = pymysql.connect(host = 'localhost', user = 'subeom', password = 'dkstnqja123@',db = '칠성사이다')
    update = up.cursor()

    money = "SELECT * FROM 가격" 
    day = "SELECT 기간 FROM 행사정보"   
    event = "SELECT 행사 FROM 행사정보"
	     
    update.execute(money)
    a = update.fetchall()
    print('가격 :'+ str(a[0][0]))

    update.execute(day)
    b = update.fetchall()
    print('기간 :'+ str(b[0][0]))
	    
    update.execute(event)
    c = update.fetchall()
    print('행사 :'+ str(c[0][0]))

#가격정보 받고 처리
    update.execute("select * from 가격")
    칠성사이다.data1[0] = update.fetchall()
    if(칠성사이다.data2[0] != 칠성사이다.data1[0]):
        no = 1
        print('가격변경됨')
        칠성사이다.data2[0] = 칠성사이다.data1[0]
    else:
        print("가격변경X")
        칠성사이다.data2[0] = 칠성사이다.data1[0]
#가격정보 처리 끝
        
#기간정보 처리
    update.execute("select 기간 from 행사정보")
    칠성사이다.data1[1] = update.fetchall()
    if(칠성사이다.data2[1] != 칠성사이다.data1[1]):
        no = 1
        print('기간변경됨')
        칠성사이다.data2[1] = 칠성사이다.data1[1]
    else:
        print("기간변경X")
        칠성사이다.data2[1] = 칠성사이다.data1[1]
#기간정보 처리 끝
#행사정보 처리
    
    update.execute("select 행사 from 행사정보")
    칠성사이다.data1[2] = update.fetchall()
    if(칠성사이다.data2[2] != 칠성사이다.data1[2]):
        no = 1
        print('행사변경됨')
        칠성사이다.data2[2] = 칠성사이다.data1[2]
    else:
        print("행사변경X")
        칠성사이다.data2[2] = 칠성사이다.data1[2]
#행사정보 처리 끝
    if(no == 1):    
        if os.path.isfile("2.mp3"):
            print('remove')
            os.remove("2.mp3")
        if(b[0][0] == '행사가 없습니다'):
            text = '이 제품의 이름은 칠성사이다이고 가격은' +str(a[0][0]) + '원 입니다'+' 해당제품은 행사가 없습니다'
            print(text)
        else:    
            text = '이 제품의 이름은 칠성사이다이고 가격은' + str(a[0][0]) + '원 입니다' + str(b[0][0]) + '까지' + str(c[0][0]) + '행사를 진행중입니다.'
            print(text)
        tts = gTTS(text=text, lang='ko')
        tts.save("2.mp3")

    update.execute("select * from 위치")
    칠성사이다위치 = update.fetchall()
        
    update.close()
    return 칠성사이다위치

            
def update펩시콜라():

    k = 0
    no = 0
    up = pymysql.connect(host = 'localhost', user = 'subeom', password = 'dkstnqja123@',db = '펩시콜라')
    update = up.cursor()
    
    money = "SELECT * FROM 가격" 
    day = "SELECT 기간 FROM 행사정보"   
    event = "SELECT 행사 FROM 행사정보"
	     
    update.execute(money)
    a = update.fetchall()
    print('가격 :'+ str(a[0][0]))

    update.execute(day)
    b = update.fetchall()
    print('기간 :'+ str(b[0][0]))
	    
    update.execute(event)
    c = update.fetchall()
    print('행사 :'+ str(c[0][0]))

#가격정보 받고 처리
    update.execute("select * from 가격")
    펩시콜라.data1[0] = update.fetchall()
    if(펩시콜라.data2[0] != 펩시콜라.data1[0]):
        no = 1
        print('가격변경됨')
        펩시콜라.data2[0] = 펩시콜라.data1[0]
    else:
        print("가격변경X")
        펩시콜라.data2[0] = 펩시콜라.data1[0]
#가격정보 처리 끝
        
#기간정보 처리
    update.execute("select 기간 from 행사정보")
    펩시콜라.data1[1] = update.fetchall()
    if(펩시콜라.data2[1] != 펩시콜라.data1[1]):
        no = 1
        print('기간변경됨')
        펩시콜라.data2[1] = 펩시콜라.data1[1]
    else:
        print("기간변경X")
        펩시콜라.data2[1] = 펩시콜라.data1[1]
#기간정보 처리 끝
#행사정보 처리
    
    update.execute("select 행사 from 행사정보")
    펩시콜라.data1[2] = update.fetchall()
    if(펩시콜라.data2[2] != 펩시콜라.data1[2]):
        no = 1
        print('행사변경됨')
        펩시콜라.data2[2] = 펩시콜라.data1[2]
    else:
        print("행사변경X")
        펩시콜라.data2[2] = 펩시콜라.data1[2]
#행사정보 처리 끝
    if(no == 1):    
        if os.path.isfile("3.mp3"):
            print('remove')
            os.remove("3.mp3")
        if(b[0][0] == '행사가 없습니다'):
            text = '이 제품의 이름은 펩시콜라이고 가격은' +str(a[0][0]) + '원 입니다'+' 해당제품은 행사가 없습니다'
            print(text)
        else:    
            text = '이 제품의 이름은 펩시콜라이고 가격은' + str(a[0][0]) + '원 입니다' + str(b[0][0]) + '까지' + str(c[0][0]) + '행사를 진행중입니다.'
            print(text)
        tts = gTTS(text=text, lang='ko')
        tts.save("3.mp3")

    update.execute("select * from 위치")
    펩시콜라위치 = update.fetchall()
        
    update.close()
    return 펩시콜라위치


def update환타():

    k = 0
    no = 0
    up = pymysql.connect(host = 'localhost', user = 'subeom', password = 'dkstnqja123@',db = '환타')
    update = up.cursor()

    money = "SELECT * FROM 가격" 
    day = "SELECT 기간 FROM 행사정보"   
    event = "SELECT 행사 FROM 행사정보"
	     
    update.execute(money)
    a = update.fetchall()
    print('가격 :'+ str(a[0][0]))

    update.execute(day)
    b = update.fetchall()
    print('기간 :'+ str(b[0][0]))
	    
    update.execute(event)
    c = update.fetchall()
    print('행사 :'+ str(c[0][0]))

#가격정보 받고 처리
    update.execute("select * from 가격")
    환타.data1[0] = update.fetchall()
    if(환타.data2[0] != 환타.data1[0]):
        no = 1
        print('가격변경됨')
        환타.data2[0] = 환타.data1[0]
    else:
        print("가격변경X")
        환타.data2[0] = 환타.data1[0]
#가격정보 처리 끝
        
#기간정보 처리
    update.execute("select 기간 from 행사정보")
    환타.data1[1] = update.fetchall()
    if(환타.data2[1] != 환타.data1[1]):
        no = 1
        print('기간변경됨')
        환타.data2[1] = 환타.data1[1]
    else:
        print("기간변경X")
        환타.data2[1] = 환타.data1[1]
#기간정보 처리 끝
#행사정보 처리
    
    update.execute("select 행사 from 행사정보")
    환타.data1[2] = update.fetchall()
    if(환타.data2[2] != 환타.data1[2]):
        no = 1
        print('행사변경됨')
        환타.data2[2] = 환타.data1[2]
    else:
        print("행사변경X")
        환타.data2[2] = 환타.data1[2]
#행사정보 처리 끝
    
    if(no == 1):    
        if os.path.isfile("4.mp3"):
            print('remove')
            os.remove("4.mp3")
        if(b[0][0] == '행사가 없습니다'):
            text = '이 제품의 이름은 환타이고 가격은' +str(a[0][0]) + '원 입니다'+' 해당제품은 행사가 없습니다'
            print(text)
        else:    
            text = '이 제품의 이름은 환타이고 가격은' + str(a[0][0]) + '원 입니다' + str(b[0][0]) + '까지' + str(c[0][0]) + '행사를 진행중입니다.'
            print(text)
        tts = gTTS(text=text, lang='ko')
        tts.save("4.mp3")

    update.execute("select * from 위치")
    환타위치 = update.fetchall()
    
    update.close()
    return 환타위치

def update포카리스웨트():
    k = 0
    no = 0
    up = pymysql.connect(host = 'localhost', user = 'subeom', password = 'dkstnqja123@',db = '포카리스웨트')
    update = up.cursor()
    updatetable = ['가격', '행사정보','행사정보']
    updatefield = ['*','기간','행사']

    money = "SELECT * FROM 가격" 
    day = "SELECT 기간 FROM 행사정보"   
    event = "SELECT 행사 FROM 행사정보"
	     
    update.execute(money)
    a = update.fetchall()
    print('가격 :'+ str(a[0][0]))

    update.execute(day)
    b = update.fetchall()
    print('기간 :'+ str(b[0][0]))
	    
    update.execute(event)
    c = update.fetchall()
    print('행사 :'+ str(c[0][0]))

#가격정보 받고 처리
    update.execute("select * from 가격")
    코카콜라.data1[0] = update.fetchall()
    if(포카리스웨트.data2[0] != 포카리스웨트.data1[0]):
        no = 1
        print('가격변경됨')
        포카리스웨트.data2[0] = 포카리스웨트.data1[0]
    else:
        print("가격변경X")
        포카리스웨트.data2[0] = 포카리스웨트.data1[0]
#가격정보 처리 끝
        
#기간정보 처리
    update.execute("select 기간 from 행사정보")
    포카리스웨트.data1[1] = update.fetchall()
    if(포카리스웨트.data2[1] != 포카리스웨트.data1[1]):
        no = 1
        print('기간변경됨')
        포카리스웨트.data2[1] = 포카리스웨트.data1[1]
    else:
        print("기간변경X")
        포카리스웨트.data2[1] = 포카리스웨트.data1[1]
#기간정보 처리 끝
#행사정보 처리
    
    update.execute("select 행사 from 행사정보")
    포카리스웨트.data1[2] = update.fetchall()
    if(포카리스웨트.data2[2] != 포카리스웨트.data1[2]):
        no = 1
        print('행사변경됨')
        포카리스웨트.data2[2] = 포카리스웨트.data1[2]
    else:
        print("행사변경X")
        포카리스웨트.data2[2] = 포카리스웨트.data1[2]
#행사정보 처리 끝
    if(no == 1):    
        if os.path.isfile("5.mp3"):
            print('remove')
            os.remove("5.mp3")
        if(b[0][0] == '행사가 없습니다'):
            text = '이 제품의 이름은 포카리스웨트이고 가격은' +str(a[0][0]) + '원 입니다'+' 해당제품은 행사가 없습니다'
            print(text)
        else:    
            text = '이 제품의 이름은 포카리스웨트이고 가격은' + str(a[0][0]) + '원 입니다' + str(b[0][0]) + '까지' + str(c[0][0]) + '행사를 진행중입니다.'
            print(text)
        tts = gTTS(text=text, lang='ko')
        tts.save("5.mp3")
        
    update.execute("select * from 위치")
    포카리스웨트위치 = update.fetchall()
     
    update.close()
    return 포카리스웨트위치

def update솔의눈():
    k = 0
    no = 0
    up = pymysql.connect(host = 'localhost', user = 'subeom', password = 'dkstnqja123@',db = '솔의눈')
    update = up.cursor()

    money = "SELECT * FROM 가격" 
    day = "SELECT 기간 FROM 행사정보"   
    event = "SELECT 행사 FROM 행사정보"
	     
    update.execute(money)
    a = update.fetchall()
    print('가격 :'+ str(a[0][0]))

    update.execute(day)
    b = update.fetchall()
    print('기간 :'+ str(b[0][0]))
	    
    update.execute(event)
    c = update.fetchall()
    print('행사 :'+ str(c[0][0]))

#가격정보 받고 처리
    update.execute("select * from 가격")
    솔의눈.data1[0] = update.fetchall()
    if(솔의눈.data2[0] != 솔의눈.data1[0]):
        no = 1
        print('가격변경됨')
        솔의눈.data2[0] = 솔의눈.data1[0]
    else:
        print("가격변경X")
        솔의눈.data2[0] = 솔의눈.data1[0]
#가격정보 처리 끝
        
#기간정보 처리
    update.execute("select 기간 from 행사정보")
    솔의눈.data1[1] = update.fetchall()
    if(솔의눈.data2[1] != 솔의눈.data1[1]):
        no = 1
        print('기간변경됨')
        솔의눈.data2[1] = 솔의눈.data1[1]
    else:
        print("기간변경X")
        솔의눈.data2[1] = 솔의눈.data1[1]
#기간정보 처리 끝
#행사정보 처리
    
    update.execute("select 행사 from 행사정보")
    솔의눈.data1[2] = update.fetchall()
    if(솔의눈.data2[2] != 솔의눈.data1[2]):
        no = 1
        print('행사변경됨')
        솔의눈.data2[2] = 솔의눈.data1[2]
    else:
        print("행사변경X")
        솔의눈.data2[2] = 솔의눈.data1[2]
#행사정보 처리 끝
    if(no == 1):    
        if os.path.isfile("6.mp3"):
            print('remove')
            os.remove("6.mp3")
        if(b[0][0] == '행사가 없습니다'):
            text = '이 제품의 이름은 솔의 눈이고 가격은' +str(a[0][0]) + '원 입니다'+' 해당제품은 행사가 없습니다'
            print(text)
        else:    
            text = '이 제품의 이름은 솔의 눈이고 가격은' + str(a[0][0]) + '원 입니다' + str(b[0][0]) + '까지' + str(c[0][0]) + '행사를 진행중입니다.'
            print(text)
        tts = gTTS(text=text, lang='ko')
        tts.save("6.mp3")

    update.execute("select * from 위치")
    솔의눈위치 = update.fetchall()
        
    update.close()
    return 솔의눈위치

def check():
    n = 0
    list = [btn1,btn2,btn3,btn4,btn5,btn6]
    while(n < 6):
        if(코카콜라위치 == list[n]):
            print(list[n][0][0])
            print(n+1)
            playsound("1.mp3")
        if(칠성사이다위치 == list[n]):
            print(list[n][0][0])
            print(n+1)
            playsound("2.mp3")
        if(펩시콜라위치 == list[n]):
            print(list[n][0][0])
            print(n+1)
            playsound("3.mp3")
        if(환타위치 == list[n]):
            print(list[n][0][0])
            print(n+1)
            playsound("4.mp3")
        if(포카리스웨트위치 == list[n]):
            print(list[n][0][0])
            print(n+1)
            playsound("5.mp3")
        if(솔의눈위치 == list[n]):
            print(list[n][0][0])
            print(n+1)
            playsound("6.mp3")
        n += 1

try:    
    while True:
        up = pymysql.connect(host = 'localhost', user = 'subeom', password = 'dkstnqja123@',db = 'readresult')
        update = up.cursor()
        i = 0
        j = 0
        money = 0
        day = 0
        event = 0
        
        update.execute("select * from btn1")
        btn1 = update.fetchall() # 1

        update.execute("select * from btn2")
        btn2 = update.fetchall() # 2

        update.execute("select * from btn3")
        btn3 = update.fetchall() # 3

        update.execute("select * from btn4")
        btn4 = update.fetchall() # 4

        update.execute("select * from btn5")
        btn5 = update.fetchall() # 5
        print(btn5[0][0])

        update.execute("select * from btn6")
        btn6 = update.fetchall() # 6

        
        print('코카콜라')#1
        코카콜라위치 = update코카콜라() #123456
        print('\n')

        print('칠성사이다')#4
        칠성사이다위치 = update칠성사이다()
        print('\n')  

        print('펩시콜라')#2
        펩시콜라위치 = update펩시콜라()
        print('\n')
        
        print('환타')#5
        환타위치 = update환타()
        print('\n')

        print('포카리스웨트')#6
        포카리스웨트위치 = update포카리스웨트()
        print('\n')

        print('솔의눈')#3
        솔의눈위치 = update솔의눈()
        print('\n')
    
        check()

        time.sleep(0.5)
        

except KeyboardInterrupt:
    print("code down")
    

    
    











    
