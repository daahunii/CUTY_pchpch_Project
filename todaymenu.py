from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import random
import time
import datetime
from tkinter import *
import tkinter as tk
import tkinter.ttk
import os
from collections import Counter
import tkinter.font

# print(time.time())
# print("현재 시각은", time.localtime(time.time()).tm_hour,"시 입니다") # 범위 0~23시
# bs4로 하나씩 링크를 열지 말고 셀레니움을 통해 클릭으로 넘어가서 한번에 정보 처리!
# /usr/local/bin/chromedriver
# driver = webdriver.Chrome()

#=========================================================================================================
options = Options()
options.add_argument('headless')
driver = webdriver.Chrome("/usr/local/bin/chromedriver", chrome_options=options) # 창 안켜지게 하는 옵션
time = time.localtime(time.time()).tm_hour # 현재 시각

# print("\n=====================================학관=======================================")
driver.get("http://smart.handong.edu/service/index.php/main/lookup_lists/MjIxMDA2NjE=/v1") #학생식당

e = ''
elems_kota1 = ''.join([e.text for e in driver.find_elements_by_xpath('//*[@id="board_area"]/table/thead/tr/th[2]/table[1]/tbody/tr[2]/td')]).split('\n')
elems_kota2 = ''.join([e.text for e in driver.find_elements_by_xpath('//*[@id="board_area"]/table/thead/tr/th[2]/table[1]/tbody/tr[4]/td')]).split('\n')
elems_kota3 = ''.join([e.text for e in driver.find_elements_by_xpath('//*[@id="board_area"]/table/thead/tr/th[2]/table[1]/tbody/tr[7]/td')]).split('\n')
del elems_kota1[0]
del elems_kota2[0]
del elems_kota3[0]

elems_ktable = list
if 0 <= time <= 8:
    elems_ktable = elems_kota1 #아침
elif 9 <= time <= 16:
    elems_ktable = elems_kota2 #점심
elif 17 <= time <= 23:
    elems_ktable = elems_kota3 #저녁

elems_fry = ''.join([e.text for e in driver.find_elements_by_xpath('//*[@id="board_area"]/table/thead/tr/th[2]/table[2]/tbody/tr[2]/td[1]')]).split('\n')
del elems_fry[0]
    
elems_gg = ''.join([e.text for e in driver.find_elements_by_xpath('//*[@id="board_area"]/table/thead/tr/th[2]/table[5]/tbody/tr[2]/td[1]')]).split('\n')
elems_gg = ''.join(elems_gg).split('/') # 야채, 치즈 나누기
del elems_gg[0]

elems_mix = ''.join([e.text for e in driver.find_elements_by_xpath('//*[@id="board_area"]/table/thead/tr/th[2]/table[6]/tbody/tr[2]/td[1]')]).split('\n')
del elems_mix[0]

if len(elems_ktable) == 0:
    elems_ktable.append("-운영없음-")
if len(elems_fry) == 0:
    elems_fry.append("-운영없음-")
if len(elems_gg) == 0:
    elems_gg.append("-운영없음-")
if len(elems_mix) == 0:
    elems_mix.append("-운영없음-")

# print("\n=====================================맘스키친=======================================")
driver.get('http://smart.handong.edu/service/index.php/main/lookup_lists/MjIxMDA2NjE=/v2') #맘스키친

momelems_morning = ''.join([e.text for e in driver.find_elements_by_xpath('//*[@id="board_area"]/table/thead/tr/th[2]/table/tbody/tr[2]/td')]).split('\n')
momelems_lunch = ''.join([e.text for e in driver.find_elements_by_xpath('//*[@id="board_area"]/table/thead/tr/th[2]/table/tbody/tr[4]/td')]).split('\n')
momelems_dinner = ''.join([e.text for e in driver.find_elements_by_xpath('//*[@id="board_area"]/table/thead/tr/th[2]/table/tbody/tr[7]/td')]).split('\n')

if momelems_morning[0] == '' or momelems_morning[0] == '등록된 메뉴가 없습니다.':
    momelems_morning.remove(momelems_morning[0])
if momelems_lunch[0] == '' or momelems_lunch[0] == '등록된 메뉴가 없습니다.':
    momelems_lunch.remove(momelems_lunch[0])
if momelems_dinner[0] == '' or momelems_dinner[0] == '등록된 메뉴가 없습니다.':
    momelems_dinner.remove(momelems_dinner[0])

moms = list
if 0 <= time <= 8:
    moms = momelems_morning #아침
elif 9 <= time <= 16:
    moms = momelems_lunch #점심
elif 17 <= time <= 23:
    moms = momelems_dinner #저녁

if len(moms) == 0:
    moms.append("-운영없음-")

# print("\n======================================한동라운지=======================================")
driver.get('http://smart.handong.edu/service/index.php/main/lookup_lists/MjIxMDA2NjE=/v3') #라운지

lounelems_lunch = ''.join([e.text for e in driver.find_elements_by_xpath('//*[@id="board_area"]/table/thead/tr/th[2]/table[2]/tbody/tr[2]/td[1]')]).split('\n')
del lounelems_lunch[0]
lounelems_dinner = ''.join([e.text for e in driver.find_elements_by_xpath('//*[@id="board_area"]/table/thead/tr/th[2]/table[2]/tbody/tr[2]/td[2]')]).split('\n')
del lounelems_dinner[0]

lounge = list
if 0 <= time <= 8:
    lounge = lounelems_lunch #아침
elif 9 <= time <= 16:
    lounge = lounelems_lunch #점심
elif 17 <= time <= 23:
    lounge = lounelems_dinner #저녁

if len(lounge) == 0:
    lounge.append("-운영없음-")

# print("\n======================================더그레이스 테이블=======================================")
driver.get('http://smart.handong.edu/service/index.php/main/lookup_lists/MjIxMDA2NjE=/v8') #더그레이스 테이블

graceelems_morning = ''.join([e.text for e in driver.find_elements_by_xpath('//*[@id="board_area"]/table/thead/tr/th[2]/table/tbody/tr[2]/td')]).split('\n')
graceelems_lunch = ''.join([e.text for e in driver.find_elements_by_xpath('//*[@id="board_area"]/table/thead/tr/th[2]/table/tbody/tr[4]/td')]).split('\n')
graceelems_dinner = ''.join([e.text for e in driver.find_elements_by_xpath('//*[@id="board_area"]/table/thead/tr/th[2]/table/tbody/tr[7]/td')]).split('\n')

if graceelems_morning[0] == '' or graceelems_morning[0] == '등록된 메뉴가 없습니다.':
    graceelems_morning.remove(graceelems_morning[0])
if graceelems_lunch[0] == '' or graceelems_lunch[0] == '등록된 메뉴가 없습니다.':
    graceelems_lunch.remove(graceelems_lunch[0])
if graceelems_dinner[0] == '' or graceelems_dinner[0] == '등록된 메뉴가 없습니다.':
    graceelems_dinner.remove(graceelems_dinner[0])

grace = list
if 0 <= time <= 8:
    grace = graceelems_morning #아침
elif 9 <= time <= 16:
    grace = graceelems_lunch #점심
elif 17 <= time <= 23:
    grace = graceelems_dinner #저녁

if len(grace) == 0:
    grace.append("-운영없음-")

# print("\n=============================================================================================\n")

# 방법 1. 모든 리스트의 원소들을 합쳐서 진짜 랜덤으로 막 섞어서 하나만 추천한다.
All_list = [elems_ktable, elems_fry, elems_gg, elems_mix, moms, lounge, grace]
def way1():
    choice_list = random.choice(All_list)
    print("랜덤 메뉴 : ",random.choice(choice_list))

# 방법 2. 학관, 맘스, 라운지, 더그테 중 하나를 선택하도록 하고 그 중에서 랜덤으로 추천한다.
def way2():
    print("1.korean table\n2.Fry Fry\n3.Grace Garden\n4.Mix Rice\n5.맘스키친\n6.라운지\n7.더그레이스 테이블")
    where = int(input("장소를 선택해주세요(1,2,3,4,5,6,7) : "))
    if where == 1:
        print("korean table의 추천 메뉴 : ", random.choice(elems_ktable))
    elif where == 2:
        print("Fry Fry의 추천 메뉴 : ", random.choice(elems_fry))
    elif where == 3:
        print("Grace Garden의 추천 메뉴 : ", random.choice(elems_gg))
    elif where == 4:
        print("Mix Rice의 추천 메뉴 : ", random.choice(elems_mix))
    elif where == 5:
        print("맘스키친의 추천 메뉴 : ", random.choice(moms))
    elif where == 6:
        print("라운지의 추천 메뉴 : ", random.choice(lounge))
    elif where == 7:
        print("더그레이스 테이블의 추천 메뉴 : ", random.choice(grace))

# 방법 3. (학관, 라운지) (맘스, 더그테) 푸포 사용 여부에 따라 랜덤 추천한다.
ppo = [elems_ktable, elems_fry, elems_gg, elems_mix, lounge]
ppx = [moms, grace]

def way3():
    
    pp = int(input("푸포를 사용하시나요?(1:사용, 2:사용x) : "))
    if pp == 1:
        sel1 = random.choice(ppo)
        print(random.choice(sel1))
    elif pp == 2:
        sel2 = random.choice(ppx)
        print(random.choice(sel2))

def way():
    print("\n방법 1. 모든 리스트의 원소들을 합쳐서 랜덤으로 막 섞어서 하나만 추천한다.")
    print("방법 2. 학관, 맘스, 라운지, 더그테 중 하나를 선택하도록 하고 그 중에서 랜덤으로 추천한다.")
    print("방법 3. (학관, 라운지) (맘스, 더그테) 푸포 사용 여부에 따라 랜덤 추천한다.\n")
    w = int(input("way1, way2, way3 (1, 2, 3 중 입력) : "))
    if w == 1:
        way1()
    elif w == 2:
        way2()
    elif w == 3:
        way3()


#-----------------------------------------------tkinter--------------------------------------------------

window = Tk()
window.title("Random Menu")
window.resizable(width= 0, height= 0) # 창크기 고정

#################################################

notebook=tkinter.ttk.Notebook(window, width=1200, height=800)
notebook.pack()

#=====================================tab1=============================================
tab1=tkinter.Frame(window)
notebook.add(tab1, text=" Home ")
tab1.config(bg = "black")
photo = PhotoImage(file = "handong.png")
label = Label(tab1, image= photo, bg= "black", fg = "white")
label.pack()
label.place(x = 330, y = 60)

label1 = tkinter.Label(tab1, text = "⌬ Today's menu ⌬",fg = "white", bg = "black" ,font=('Times',45))
label1.pack()
label1.place(x = 295, y = 370)
label2 = tkinter.Label(tab1, text = "- ✨Made by 귀염뽀짝뽀짝✨ -",fg = "white", bg = "black",font = ('Helvetica 18 bold italic',21))
label2.pack()
label2.place(x = 340, y = 450)

#=====================================tab2=============================================

mfont = tkinter.font.Font(family = "Courier", size = 30)
mfont1 = tkinter.font.Font(family = "Courier", size = 17)
tab2=tkinter.Frame(window)
notebook.add(tab2, text=" All ")
tab2.config(bg = "black")
label3 = tkinter.Label(tab2, text = "- Today's menu -",fg = "white" , bg = "black",font=mfont)
label3.pack()

def All_menu():
    bnt = tk.Button(tab2, width = 104, height = 21, state=DISABLED, bg = "gray98", borderwidth=6, relief= "ridge")
    bnt.pack()
    bnt.place(x = 3, y = 46)
    l1 = tkinter.Label(tab2, text = elems_ktable, padx = 100, pady = 10, bg = "gray96")
    l1.config(anchor = W)
    l1.pack(anchor = W)
    l1.place(x = 6, y = 55)
    la1 = tkinter.Label(tab2, text = "✓ KoreanT  :", bg = "gray96")
    la1.config(anchor = W)
    la1.pack(anchor = W)
    la1.place(x = 18, y = 65)
    l2 = tkinter.Label(tab2, text = elems_fry, padx = 100, pady = 10, bg = "gray96")
    l2.config(anchor = W)
    l2.pack(anchor = W)
    l2.place(x = 6, y = 102)
    la2 = tkinter.Label(tab2, text = "✓ FryFry    :", bg = "gray96")
    la2.config(anchor = W)
    la2.pack(anchor = W)
    la2.place(x = 18, y = 112)
    l3 = tkinter.Label(tab2, text = elems_gg, padx = 100, pady = 10, bg = "gray97")
    l3.config(anchor = W)
    l3.pack(anchor = W)
    l3.place(x = 8, y = 149)
    la3 = tkinter.Label(tab2, text = "✓ GraceG    :", bg = "gray97")
    la3.config(anchor = W)
    la3.pack(anchor = W)
    la3.place(x = 18, y = 159)
    l4 = tkinter.Label(tab2, text = elems_mix, padx = 100, pady = 10, bg = "gray98")
    l4.config(anchor = W)
    l4.pack(anchor = W)
    l4.place(x = 6, y = 196)
    la4 = tkinter.Label(tab2, text = "✓ Mix Rice  :", bg = "gray98")
    la4.config(anchor = W)
    la4.pack(anchor = W)
    la4.place(x = 18, y = 206)
    l5 = tkinter.Label(tab2, text = moms, padx = 100, pady = 10, bg = "gray98")
    l5.config(anchor = W)
    l5.pack(anchor = W)
    l5.place(x = 6, y = 243)
    la5 = tkinter.Label(tab2, text = "✓ Moms     :", bg = "gray98")
    la5.config(anchor = W)
    la5.pack(anchor = W)
    la5.place(x = 18, y = 253)
    l6 = tkinter.Label(tab2, text = lounge, padx = 100, pady = 10, bg = "gray98")
    l6.config(anchor = W)
    l6.pack(anchor = W)
    l6.place(x = 8, y = 290)
    la6 = tkinter.Label(tab2, text = "✓ Lounge   :", bg = "gray98")
    la6.config(anchor = E)
    la6.pack(anchor = E)
    la6.place(x = 9, y = 300)
    l7 = tkinter.Label(tab2, text = grace, padx = 100, pady = 10, bg = "gray98")
    l7.config(anchor = W)
    l7.pack(anchor = W)
    l7.place(x = 6, y = 337)
    la7 = tkinter.Label(tab2, text = "✓ GraceT    :", bg = "gray98")
    la7.config(anchor = W)
    la7.pack(anchor = W)
    la7.place(x = 18, y = 347)
All_menu()

label4 = tkinter.Label(tab2, text = "〠 Way1. Randomly choose one of all restaurants's food.",fg = "LightGoldenrod2" , bg = "black",font=mfont1)
label4.pack()
label4.place(x=100, y = 410) 
label5 = tkinter.Label(tab2, text = "〠 Way2. Choose a restaurant and choose randomly.",fg = "LightGoldenrod2" , bg = "black",font=mfont1)
label5.pack()
label5.place(x=100, y = 450)
label6 = tkinter.Label(tab2, text = "〠 Way3. Choose randomly depending on whether you use a foodpoint or not.",fg = "LightGoldenrod2" , bg = "black",font=mfont1)
label6.pack()
label6.place(x=100, y = 490)

#=====================================tab3=============================================
tab3=tkinter.Frame(window)
notebook.add(tab3, text=" Way1 ")
tab3.config(bg = "black")
mfont3 = tkinter.font.Font(family = "Courier", size = 60)
def recommend1():
    choice_list = random.choice(All_list)
    randomfood = Label(tab3, text = random.choice(choice_list), width= 22, height= 5, anchor= CENTER, font=mfont3, borderwidth=0, relief='solid', fg = "cyan4")
    randomfood.pack()
    randomfood.place(x = 75, y = 130)

temp = Label(tab3, text = " ", width= 40, height= 7, anchor= CENTER, font=('Times',45), borderwidth=5, relief='solid')
temp.pack()
temp.place(x = 7, y = 100)
btn1 = Button(tab3, text=" Random ",command= recommend1 , width = 10, height = 2)
btn1.pack()
btn1.place(x = 430, y = 30)


#=====================================tab4=============================================
tab4=tkinter.Frame(window)
notebook.add(tab4, text=" Way2 ")
tab4.config(bg = "black")

temp2 = Label(tab4, text = " ", width= 40, height= 7, anchor= CENTER, font=('Times',45), borderwidth=5, relief='solid')
temp2.pack()
temp2.place(x = 7, y = 140)
from functools import partial
def recommend2(num):
    if num == 1:
        randomfood = Label(tab4, text = random.choice(elems_ktable), width= 23, height= 4, anchor= CENTER, font=mfont3, borderwidth=0, relief='solid', fg = "cyan4")
        randomfood.pack()
        randomfood.place(x = 45, y = 200)
    elif num == 2:
        randomfood = Label(tab4, text = random.choice(elems_fry), width= 23, height= 4, anchor= CENTER, font=mfont3, borderwidth=0, relief='solid', fg = "cyan4")
        randomfood.pack()
        randomfood.place(x = 45, y = 200)
    elif num == 3:
        randomfood = Label(tab4, text = random.choice(elems_gg), width= 23, height= 4, anchor= CENTER, font=mfont3, borderwidth=0, relief='solid', fg = "cyan4")
        randomfood.pack()
        randomfood.place(x = 45, y = 200)
    elif num == 4:
        randomfood = Label(tab4, text = random.choice(elems_mix), width= 23, height= 4, anchor= CENTER, font=mfont3, borderwidth=0, relief='solid', fg = "cyan4")
        randomfood.pack()
        randomfood.place(x = 45, y = 200)
    elif num == 5:
        randomfood = Label(tab4, text = random.choice(moms), width= 23, height= 4, anchor= CENTER, font=mfont3, borderwidth=0, relief='solid', fg = "cyan4")
        randomfood.pack()
        randomfood.place(x = 45, y = 200)
    elif num == 6:
        randomfood = Label(tab4, text = random.choice(lounge), width= 23, height= 4, anchor= CENTER, font=mfont3, borderwidth=0, relief='solid', fg = "cyan4")
        randomfood.pack()
        randomfood.place(x = 45, y = 200)
    elif num == 7:
        randomfood = Label(tab4, text = random.choice(grace), width= 23, height= 4, anchor= CENTER, font=mfont3, borderwidth=0, relief='solid', fg = "cyan4")
        randomfood.pack()
        randomfood.place(x = 45, y = 200)
    else:
        num = 0

def menubtn():
    ktbtn = Button(tab4, text="Korean Table", width= 13, height=2, command= lambda: recommend2(1))
    ktbtn.pack()
    ktbtn.place(x = 20, y = 40)
    ffbtn = Button(tab4, text="Fry Fry", width= 13, height=2, command= lambda: recommend2(2))
    ffbtn.pack()
    ffbtn.place(x = 150, y = 40)
    ggbtn = Button(tab4, text="Grace Garden", width= 13, height=2, command= lambda: recommend2(3))
    ggbtn.pack()
    ggbtn.place(x = 280, y = 40)
    mixbtn = Button(tab4, text="Mix Rice", width= 13, height=2, command= lambda: recommend2(4))
    mixbtn.pack()
    mixbtn.place(x = 410, y = 40)
    momsbtn = Button(tab4, text="Moms Kitchen", width= 13, height=2, command= lambda: recommend2(5))
    momsbtn.pack()
    momsbtn.place(x = 540, y = 40)
    lounbtn = Button(tab4, text="Lounge", width= 13, height=2, command= lambda: recommend2(6))
    lounbtn.pack()
    lounbtn.place(x = 670, y = 40)
    gracebtn = Button(tab4, text="The Grace Table", width= 13, height=2, command= lambda: recommend2(7))
    gracebtn.pack()
    gracebtn.place(x = 800, y = 40)
menubtn()


#=====================================tab5=============================================
mfont4 = tkinter.font.Font(family = "Courier", size = 15)
mfont5 = tkinter.font.Font(family = "Courier", size = 35)
tab5=tkinter.Frame(window)
notebook.add(tab5, text=" Way3 ")
tab5.config(bg = "black")
sketchbook = Button(tab5, width = 1, height = 600)
sketchbook.pack()

def recommend3(num):
    if num == 1:
        sel1 = random.choice(ppo)
        randomfood = Label(tab5, text = random.choice(sel1), width= 18, height= 4, anchor= CENTER, font=mfont5, borderwidth=0, relief='solid', fg = "cyan4")
        randomfood.pack()
        randomfood.place(x = 31, y = 250)
    elif num == 2:
        sel2 = random.choice(ppx)
        randomfood = Label(tab5, text = random.choice(sel2), width= 18, height= 4, anchor= CENTER, font=mfont5, borderwidth=0, relief='solid', fg = "cyan4")
        randomfood.pack()
        randomfood.place(x = 517, y = 250)
    else:
        num = 0

btn1 = Button(tab5, text=" Random ",command = lambda: recommend3(1) , width = 10, height = 2)
btn1.pack()
btn1.place(x = 175, y = 40)

btn2 = Button(tab5, text=" Random ",command = lambda: recommend3(2) , width = 10, height = 2)
btn2.pack()
btn2.place(x = 675, y = 40)

fp1 = Label(tab5, text = "Food Point -> O", width = 35, height = 3, anchor = CENTER, font=mfont4, borderwidth=0, relief='solid', bg = "black", fg = "white")
fp1.pack()
fp1.place(x = 65, y = 85)
fp2 = Label(tab5, text = "Food Point -> X", width = 35, height = 3, anchor = CENTER, font=mfont4, borderwidth=0, relief='solid', bg = "black", fg = "white")
fp2.pack()
fp2.place(x = 565, y = 85)

temp1 = Label(tab5, text = " ", width= 18, height= 7, anchor= CENTER, font=('Times',45), borderwidth=5, relief='solid')
temp1.pack()
temp1.place(x = 15, y = 140)
temp2 = Label(tab5, text = " ", width= 18, height= 7, anchor= CENTER, font=('Times',45), borderwidth=5, relief='solid')
temp2.pack()
temp2.place(x = 505, y = 140)

window.geometry('1000x600+200+100') # 창 열릴 때 위치
window.mainloop()