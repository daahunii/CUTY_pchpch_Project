from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import random
import time
import datetime

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
driver.get('http://smart.handong.edu/service/index.php/main/lookup_lists/MjIxMDA2NjE=/v1') #학생식당

# print("korean table")
e = ''
elems_kota1 = ''.join([e.text for e in driver.find_elements_by_xpath('//*[@id="board_area"]/table/thead/tr/th[2]/table[1]/tbody/tr[2]/td')]).split('\n')
elems_kota2 = ''.join([e.text for e in driver.find_elements_by_xpath('//*[@id="board_area"]/table/thead/tr/th[2]/table[1]/tbody/tr[4]/td')]).split('\n')
elems_kota3 = ''.join([e.text for e in driver.find_elements_by_xpath('//*[@id="board_area"]/table/thead/tr/th[2]/table[1]/tbody/tr[7]/td')]).split('\n')
del elems_kota1[0]
del elems_kota2[0]
del elems_kota3[0]

elems_ktable = list
if 1 <= time <= 8:
    elems_ktable = elems_kota1 #아침
elif 9 <= time <= 16:
    elems_ktable = elems_kota2 #점심
elif 17 <= time <= 23:
    elems_ktable = elems_kota3 #저녁
# print(elems_ktable)


# print("\nFry Fry")
elems_fry = ''.join([e.text for e in driver.find_elements_by_xpath('//*[@id="board_area"]/table/thead/tr/th[2]/table[2]/tbody/tr[2]/td[1]')]).split('\n')
del elems_fry[0]
# print(elems_fry)

# print("\nGrace Garden")
elems_gg = ''.join([e.text for e in driver.find_elements_by_xpath('//*[@id="board_area"]/table/thead/tr/th[2]/table[5]/tbody/tr[2]/td[1]')]).split('\n')
del elems_gg[0]
# print(elems_gg)

# print("\nMix Rice")
elems_mix = ''.join([e.text for e in driver.find_elements_by_xpath('//*[@id="board_area"]/table/thead/tr/th[2]/table[6]/tbody/tr[2]/td[1]')]).split('\n')
del elems_mix[0]
# print(elems_mix)


# print("\n=====================================맘스키친=======================================")
driver.get('http://smart.handong.edu/service/index.php/main/lookup_lists/MjIxMDA2NjE=/v2') #맘스키친

# print("맘스키친")
momelems_morning = ''.join([e.text for e in driver.find_elements_by_xpath('//*[@id="board_area"]/table/thead/tr/th[2]/table/tbody/tr[2]/td')]).split('\n')
momelems_lunch = ''.join([e.text for e in driver.find_elements_by_xpath('//*[@id="board_area"]/table/thead/tr/th[2]/table/tbody/tr[4]/td')]).split('\n')
momelems_dinner = ''.join([e.text for e in driver.find_elements_by_xpath('//*[@id="board_area"]/table/thead/tr/th[2]/table/tbody/tr[7]/td')]).split('\n')

moms = list
if 1 <= time <= 8:
    moms = momelems_morning #아침
elif 9 <= time <= 16:
    moms = momelems_lunch #점심
elif 17 <= time <= 23:
    moms = momelems_dinner #저녁
# print(moms)


# print("\n======================================한동라운지=======================================")
driver.get('http://smart.handong.edu/service/index.php/main/lookup_lists/MjIxMDA2NjE=/v3') #라운지

# print("라운지 일반메뉴(for everyone)")
lounelems_lunch = ''.join([e.text for e in driver.find_elements_by_xpath('//*[@id="board_area"]/table/thead/tr/th[2]/table[2]/tbody/tr[2]/td[1]')]).split('\n')
del lounelems_lunch[0]
lounelems_dinner = ''.join([e.text for e in driver.find_elements_by_xpath('//*[@id="board_area"]/table/thead/tr/th[2]/table[2]/tbody/tr[2]/td[2]')]).split('\n')
del lounelems_dinner[0]

lounge = list
if 1 <= time <= 8:
    lounge = lounelems_lunch #아침
elif 9 <= time <= 16:
    lounge = lounelems_lunch #점심
elif 17 <= time <= 23:
    lounge = lounelems_dinner #저녁
# print(lounge)


# print("\n======================================더그레이스 테이블=======================================")
driver.get('http://smart.handong.edu/service/index.php/main/lookup_lists/MjIxMDA2NjE=/v8') #더그레이스 테이블

# print("더그레이스 테이블")
graceelems_lunch = ''.join([e.text for e in driver.find_elements_by_xpath('//*[@id="board_area"]/table/thead/tr/th[2]/table/tbody/tr[4]/td')]).split('\n')
graceelems_dinner = ''.join([e.text for e in driver.find_elements_by_xpath('//*[@id="board_area"]/table/thead/tr/th[2]/table/tbody/tr[7]/td')]).split('\n')

grace = list
if 1 <= time <= 8:
    grace = graceelems_lunch #아침
elif 9 <= time <= 16:
    grace = graceelems_lunch #점심
elif 17 <= time <= 23:
    grace = graceelems_dinner #저녁
# print(grace)


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
def way3():
    ppo = [elems_ktable, elems_fry, elems_gg, elems_mix, lounge]
    ppx = [moms, grace]
    
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
# way()
