from flask import Flask, render_template, request
import os

import pandas as pd 
import numpy as np
import time 
import random
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from konlpy.tag import Okt
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os
import glob

driver=webdriver.Chrome()

def tour_(place1, place2):
    driver.get('https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=%EA%B8%B8%EC%B0%BE%EA%B8%B0')
    driver.implicitly_wait(10)
    # ============================== 출발지 입력 ======================================
    # 잠실역 입력
    elements1 = driver.find_element(By.CLASS_NAME, 'zo6GHr700XMAUNVTWEnm ')
    # elements1.send_keys('제주도' + place1)
    elements1.send_keys(place1)
    driver.find_element(By.CLASS_NAME, 'zo6GHr700XMAUNVTWEnm ').send_keys(Keys.RETURN)

    # 버튼을 클래스명으로 찾아 클릭
    button = driver.find_element(By.CLASS_NAME, 'WoaREZV6R44SyBfahOtV')
    button.click()
    time.sleep(1+random.random())

    # 첫번째 출발지 클릭
    driver.find_elements(By.CLASS_NAME, 'UCpJLMzaonwRmF6xEQOv')

    # =============================== 도착지 입력 ========================================
    # 모든 출발지를 찾음
    departure_buttons = driver.find_elements(By.CLASS_NAME, 'zo6GHr700XMAUNVTWEnm ')

    # 두 번째 출발지를 선택
    if len(departure_buttons) >= 2:
        second_departure = departure_buttons[1]
        # second_departure.send_keys('제주도' + place2)
        second_departure.send_keys(place2)
        second_departure.send_keys(Keys.RETURN)
    else:
        print("There are less than 2 departure buttons.")

    button2 = driver.find_element(By.CLASS_NAME, 'WoaREZV6R44SyBfahOtV')
    button2.click()
    time.sleep(1+random.random())

    driver.find_elements(By.CLASS_NAME, 'IOKpNxitQy3MwBS9rlQW')[1].click()
    time.sleep(1+random.random())

    # ============================ 시간, 거리, 택시, 오일 ===============================
    time_ = driver.find_element(By.CLASS_NAME, 'iNbrs2BfJb0nLeieN0JL').text
    distance_ = driver.find_element(By.CLASS_NAME, 'HaHmThGI2AFvWYo58OD7').text
    taxi_ = driver.find_elements(By.CLASS_NAME, 'JZjYlU8yPktGwrM1zjDR')[0].text.split('원')[0].split()[-1]
    oil_ = driver.find_elements(By.CLASS_NAME, 'JZjYlU8yPktGwrM1zjDR')[0].text.split('원')[1].split()[-1]

    # driver.close()
    # time.sleep(0.5+random.random())

    if '분' in time_:
        hour=time_.split('분')[0]+'분'
        distance_ = float(distance_.replace('k', '').replace('m', ''))
        distance_=distance_
        taxi_=int(taxi_.replace(',', ''))
        oil_=int(oil_.replace(',', ''))
    else :
        hour=time_.split('시간')[0]+'시간'
        distance_ = float(distance_.replace('k', '').replace('m', ''))
        distance_=distance_
        taxi_=int(taxi_.replace(',', ''))
        oil_=int(oil_.replace(',', ''))

    if '시간' in hour:
        if '분' in hour:
            spl=hour.split('시간')
            minute_=int(spl[0])*60+int(spl[1].replace('분',''))
        else:
            spl=hour.split('시간')
            minute_=int(spl[0])*60
    else : minute_=int(hour.replace('분',''))

    return minute_, distance_, taxi_, oil_


def course(start, course1, course2, course3, end):

    lst=[start, course1, course2, course3, end]

    s01=tour_(lst[0], lst[1])
    s02=tour_(lst[0], lst[2])
    s03=tour_(lst[0], lst[3])

    s12=tour_(lst[1], lst[2])
    s13=tour_(lst[1], lst[3])
    s21=tour_(lst[2], lst[1])
    s23=tour_(lst[2], lst[3])
    s31=tour_(lst[3], lst[1])
    s32=tour_(lst[3], lst[2])

    s14=tour_(lst[1], lst[4])
    s24=tour_(lst[2], lst[4])
    s34=tour_(lst[3], lst[4])

    t123 = s01[0] + s12[0] + s23[0] + s34[0]
    t132 = s01[0] + s13[0] + s32[0] + s24[0]
    t213 = s02[0] + s21[0] + s13[0] + s34[0]
    t231 = s02[0] + s23[0] + s31[0] + s14[0]
    t312 = s03[0] + s31[0] + s12[0] + s24[0]
    t321 = s03[0] + s32[0] + s21[0] + s14[0]

    d123 = float(s01[1]) + float(s12[1]) + float(s23[1]) + float(s34[1])
    d132 = float(s01[1]) + float(s13[1]) + float(s32[1]) + float(s24[1])
    d213 = float(s02[1]) + float(s21[1]) + float(s13[1]) + float(s34[1])
    d231 = float(s02[1]) + float(s23[1]) + float(s31[1]) + float(s14[1])
    d312 = float(s03[1]) + float(s31[1]) + float(s12[1]) + float(s24[1])
    d321 = float(s03[1]) + float(s32[1]) + float(s21[1]) + float(s14[1])

    ta123 = s01[2] + s12[2] + s23[2] + s34[2]
    ta132 = s01[2] + s13[2] + s32[2] + s24[2]
    ta213 = s02[2] + s21[2] + s13[2] + s34[2]
    ta231 = s02[2] + s23[2] + s31[2] + s14[2]
    ta312 = s03[2] + s31[2] + s12[2] + s24[2]
    ta321 = s03[2] + s32[2] + s21[2] + s14[2]

    gi123 = s01[3] + s12[3] + s23[3] + s34[3]
    gi132 = s01[3] + s13[3] + s32[3] + s24[3]
    gi213 = s02[3] + s21[3] + s13[3] + s34[3]
    gi231 = s02[3] + s23[3] + s31[3] + s14[3]
    gi312 = s03[3] + s31[3] + s12[3] + s24[3]
    gi321 = s03[3] + s32[3] + s21[3] + s14[3]

    rst_dict={}
    rst_dict['t123'] = t123
    rst_dict['t132'] = t132
    rst_dict['t213'] = t213
    rst_dict['t231'] = t231
    rst_dict['t312'] = t312
    rst_dict['t321'] = t321

    resurt_ = dict(sorted(rst_dict.items(), key=lambda item: item[1]))

    dis_dict={}
    dis_dict['d123'] = d123
    dis_dict['d132'] = d132
    dis_dict['d213'] = d213
    dis_dict['d231'] = d231
    dis_dict['d312'] = d312
    dis_dict['d321'] = d321
    resurt_d= dict(sorted(dis_dict.items(), key=lambda item: item[1]))

    ta_dict={}
    ta_dict['ta123'] = ta123
    ta_dict['ta132'] = ta132
    ta_dict['ta213'] = ta213
    ta_dict['ta231'] = ta231
    ta_dict['ta312'] = ta312
    ta_dict['ta321'] = ta321
    resurt_ta = dict(sorted(ta_dict.items(), key=lambda item: item[1]))

    gi_dict={}
    gi_dict['gi123'] = gi123
    gi_dict['gi132'] = gi132
    gi_dict['gi213'] = gi213
    gi_dict['gi231'] = gi231
    gi_dict['gi312'] = gi312
    gi_dict['gi321'] = gi321
    resurt_gi = dict(sorted(gi_dict.items(), key=lambda item: item[1]))

    order = list(resurt_.keys())[0]

    rst_list=[]
    rst_list.append(lst[0])
    for a in order[1:]:
        rst_list.append(lst[int(a)])
    rst_list.append(lst[-1]) 

    start = rst_list[0]
    course1 = rst_list[1]
    course2 = rst_list[2]
    course3 = rst_list[3]
    end = rst_list[4]

    # 시간 변환
    time_ = list(resurt_.values())[0]
    totaltime = f"{time_//60}시간 {time_%60}분"
    totaldistance=str(list(resurt_d.values())[0])+'km'
    totaltaxi=str(f'{list(resurt_ta.values())[0]:,}')+'원'
    totalgi=str(f'{list(resurt_gi.values())[0]:,}')+'원'

    return totaltime, totaldistance, totaltaxi, totalgi, start, course1, course2, course3, end

# --------------------------------------------------------------------------

app = Flask(__name__)
template_dir = os.path.join(os.path.dirname(__file__),'templates')

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/result1.html')
def new_page1():
    return render_template('result1.html')

@app.route('/process', methods=['GET','POST'])
def process():
    start = request.form.get('start')
    course1 = request.form.get('course1')
    course2 = request.form.get('course2')
    course3 = request.form.get('course3')
    end = request.form.get('end')
    print(start, course1, course2, course3, end)
    print("처리")

    tour = course(start, course1, course2, course3, end)

    _start = tour[4]
    _course1= tour[5]
    _course2= tour[6]
    _course3 = tour[7] 
    _end = tour[8]
    _totaltime = tour[0]
    _totaldistance= tour[1]
    _totaltaxi = tour[2]
    _totalgi= tour[3]

    # 딕셔너리 형태가 아닌 "start" = _start 형식으로 입력해야 함 
    return render_template('result2.html',**{"start":_start,"course1":_course1,
                                           "course2":_course2,
                                           "course3":_course3,
                                           "end":_end,
                                           "totaltime":_totaltime,
                                           "totaldistance":_totaldistance,
                                           "totaltaxi":_totaltaxi,
                                           "totalgi":_totalgi})

if __name__ == '__main__':
    app.run(debug=True)


