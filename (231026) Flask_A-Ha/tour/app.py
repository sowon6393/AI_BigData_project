from flask import Flask, render_template, request
import os
import pandas as pd 
import numpy as np
from tqdm import tqdm
from konlpy.tag import Okt
from collections import Counter
from tqdm import tqdm
from sklearn.feature_extraction.text import CountVectorizer
import folium


# data = pd.read_csv('../project/data_2.csv') => vscode에서 상대경로 인식 안됨
data = pd.read_csv("C:/Users/KDP-26-/Desktop/big_data/Flask/project/data_2.csv")
del data['Unnamed: 0']


def tour(input_data):
    global data

    cv = CountVectorizer()  
    dtm = cv.fit_transform(data['nouns'])

    vocab = cv.get_feature_names_out()
    df_dtm = pd.DataFrame(dtm.toarray(), columns=vocab)

    def make_cosine(a, b):
        return np.dot(a,b) / (np.linalg.norm(a) * np.linalg.norm(b))
    okt=Okt()
    t = okt.normalize(input_data)
    # 명사 추출
    nouns = okt.nouns(t)
    # 1글자 단어 삭제 
    input_data = [word for word in nouns if len(word) > 1]
    input_data = [' '.join(input_data)]

    sample=cv.transform(input_data).toarray().reshape(len(df_dtm.columns),)

    box = []
    for target in tqdm(df_dtm.iloc):
        cosine = make_cosine(target, sample)
        box.append(cosine)

    data['유사도분석'] = box

    return data.sort_values("유사도분석", ascending=False)['관광지'][:5]

# input_data = '남자친구랑 가을에 단풍구경하면서 산책 할 곳'
# print(tour(input_data))
# --------------------------------------------------------------------------

app = Flask(__name__)
template_dir = os.path.join(os.path.dirname(__file__),'templates')

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/result1.html')
def new_page1():
    return render_template('result1.html')

# 전역변수 지정
tour1, tour2, tour3, tour4, tour5 = '', '', '', '', ''
tour_add1, tour_add2, tour_add3, tour_add4, tour_add5 = '', '', '', '', ''
tour_idx1, tour_idx2, tour_idx3, tour_idx4, tour_idx5 = '', '', '', '', ''


@app.route('/process', methods=['GET','POST'])
def process():
    global data
    global tour1, tour2, tour3, tour4, tour5
    global tour_add1, tour_add2, tour_add3, tour_add4, tour_add5
    global tour_idx1, tour_idx2, tour_idx3, tour_idx4, tour_idx5

    input = request.form.get('input_data')

    tour_s = tour(input)
    tour1=tour_s.iloc[0]
    tour2=tour_s.iloc[1]
    tour3=tour_s.iloc[2]
    tour4=tour_s.iloc[3]
    tour5=tour_s.iloc[4]

    tour_add1=data[data['관광지']==tour1]['주소'].iloc[0].replace('\xa0','')
    tour_add2=data[data['관광지']==tour2]['주소'].iloc[0].replace('\xa0','')
    tour_add3=data[data['관광지']==tour3]['주소'].iloc[0].replace('\xa0','')
    tour_add4=data[data['관광지']==tour4]['주소'].iloc[0].replace('\xa0','')
    tour_add5=data[data['관광지']==tour5]['주소'].iloc[0].replace('\xa0','')

    tour_idx1=data[data['관광지']==tour1]['주소'].index[0]
    tour_idx2=data[data['관광지']==tour2]['주소'].index[0]
    tour_idx3=data[data['관광지']==tour3]['주소'].index[0]
    tour_idx4=data[data['관광지']==tour4]['주소'].index[0]
    tour_idx5=data[data['관광지']==tour5]['주소'].index[0]

    return render_template('result2.html',**{"tour1":tour1, 
                                             "tour2":tour2,
                                             "tour3":tour3,
                                             "tour4":tour4,
                                             "tour5":tour5,
                                             "tour_add1":tour_add1,
                                             "tour_add2":tour_add2,
                                             "tour_add3":tour_add3,
                                             "tour_add4":tour_add4,
                                             "tour_add5":tour_add5,
                                             "input_data":input
                                             })



# 전역변수 지정
tour_=''
tour_add=''
tour_idx=''
top10_=''

@app.route('/info1', methods=['GET','POST'])
def info1():
    global data
    global tour1, tour_add1, tour_idx1, tour_, tour_add, tour_idx, top10_

    top10=data[data['관광지']==tour1]['top10'].iloc[0].split()  

    tour_idx = tour_idx1
    top10_ = top10
    tour_=tour1
    tour_add = tour_add1

    def map(tour):
        tour_loc = (data[data['관광지']==tour].iloc[0]['latitude'], data[data['관광지']==tour].iloc[0]['longitude']) 
        m = folium.Map(location=[tour_loc[0], tour_loc[1]], zoom_start=12)
        folium.Marker(location=tour_loc, tooltip=tour).add_to(m)

        m.save('./static/map.html')

    map(tour1)

    return render_template('tour.html',**{"tour":tour1,
                                             "tour_add":tour_add1,
                                             "ret_1":top10[0],
                                             "ret_2":top10[1],
                                             "ret_3":top10[2],
                                             "ret_4":top10[3],
                                             "ret_5":top10[4],
                                             "ret_6":top10[5],
                                             "ret_7":top10[6],
                                             "ret_8":top10[7],
                                             "ret_9":top10[8],
                                             "ret_10":top10[9]
                                             })

@app.route('/info2', methods=['GET','POST'])
def info2():
    global data
    global tour1, tour_add1, tour_idx1, tour_, tour_add, tour_idx, top10_

    top10=data[data['관광지']==tour2]['top10'].iloc[0].split()  

    tour_idx = tour_idx2
    top10_ = top10
    tour_=tour2
    tour_add = tour_add2

    def map(tour):
        tour_loc = (data[data['관광지']==tour].iloc[0]['latitude'], data[data['관광지']==tour].iloc[0]['longitude']) 
        m = folium.Map(location=[tour_loc[0], tour_loc[1]], zoom_start=12)
        folium.Marker(location=tour_loc, tooltip=tour).add_to(m)

        m.save('./static/map.html')

    map(tour2)

    return render_template('tour.html',**{"tour":tour2,
                                             "tour_add":tour_add2,
                                             "ret_1":top10[0],
                                             "ret_2":top10[1],
                                             "ret_3":top10[2],
                                             "ret_4":top10[3],
                                             "ret_5":top10[4],
                                             "ret_6":top10[5],
                                             "ret_7":top10[6],
                                             "ret_8":top10[7],
                                             "ret_9":top10[8],
                                             "ret_10":top10[9]
                                             })

@app.route('/info3', methods=['GET','POST'])
def info3():
    global data
    global tour1, tour_add1, tour_idx1, tour_, tour_add, tour_idx, top10_

    top10=data[data['관광지']==tour3]['top10'].iloc[0].split()  

    tour_idx = tour_idx3
    top10_ = top10
    tour_=tour3
    tour_add = tour_add3

    def map(tour):
        tour_loc = (data[data['관광지']==tour].iloc[0]['latitude'], data[data['관광지']==tour].iloc[0]['longitude']) 
        m = folium.Map(location=[tour_loc[0], tour_loc[1]], zoom_start=12)
        folium.Marker(location=tour_loc, tooltip=tour).add_to(m)

        m.save('./static/map.html')

    map(tour3)

    return render_template('tour.html',**{"tour":tour3,
                                             "tour_add":tour_add3,
                                             "ret_1":top10[0],
                                             "ret_2":top10[1],
                                             "ret_3":top10[2],
                                             "ret_4":top10[3],
                                             "ret_5":top10[4],
                                             "ret_6":top10[5],
                                             "ret_7":top10[6],
                                             "ret_8":top10[7],
                                             "ret_9":top10[8],
                                             "ret_10":top10[9]
                                             })

@app.route('/info4', methods=['GET','POST'])
def info4():
    global data
    global tour1, tour_add1, tour_idx1, tour_, tour_add, tour_idx, top10_

    top10=data[data['관광지']==tour4]['top10'].iloc[0].split()  

    tour_idx = tour_idx4
    top10_ = top10
    tour_=tour4
    tour_add = tour_add4

    def map(tour):
        tour_loc = (data[data['관광지']==tour].iloc[0]['latitude'], data[data['관광지']==tour].iloc[0]['longitude']) 
        m = folium.Map(location=[tour_loc[0], tour_loc[1]], zoom_start=12)
        folium.Marker(location=tour_loc, tooltip=tour).add_to(m)

        m.save('./static/map.html')

    map(tour4)

    return render_template('tour.html',**{"tour":tour4,
                                             "tour_add":tour_add4,
                                             "ret_1":top10[0],
                                             "ret_2":top10[1],
                                             "ret_3":top10[2],
                                             "ret_4":top10[3],
                                             "ret_5":top10[4],
                                             "ret_6":top10[5],
                                             "ret_7":top10[6],
                                             "ret_8":top10[7],
                                             "ret_9":top10[8],
                                             "ret_10":top10[9]
                                             })

@app.route('/info5', methods=['GET','POST'])
def info5():
    global data
    global tour1, tour_add1, tour_idx1, tour_, tour_add, tour_idx, top10_

    top10=data[data['관광지']==tour5]['top10'].iloc[0].split()  

    tour_idx = tour_idx5
    top10_ = top10
    tour_=tour5
    tour_add = tour_add5

    def map(tour):
        tour_loc = (data[data['관광지']==tour].iloc[0]['latitude'], data[data['관광지']==tour].iloc[0]['longitude']) 
        m = folium.Map(location=[tour_loc[0], tour_loc[1]], zoom_start=12)
        folium.Marker(location=tour_loc, tooltip=tour).add_to(m)

        m.save('./static/map.html')

    map(tour5)

    return render_template('tour.html',**{"tour":tour5,
                                             "tour_add":tour_add5,
                                             "ret_1":top10[0],
                                             "ret_2":top10[1],
                                             "ret_3":top10[2],
                                             "ret_4":top10[3],
                                             "ret_5":top10[4],
                                             "ret_6":top10[5],
                                             "ret_7":top10[6],
                                             "ret_8":top10[7],
                                             "ret_9":top10[8],
                                             "ret_10":top10[9]
                                             })



@app.route('/to_create_img', methods=['GET','POST'])
def to_create_img():
    global tour_, tour_add, tour_idx, top10_

    return render_template('create_img.html', ai_img=tour_idx, **{"tour":tour_,
                                             "tour_add":tour_add,
                                             "ret_1":top10_[0],
                                             "ret_2":top10_[1],
                                             "ret_3":top10_[2],
                                             "ret_4":top10_[3],
                                             "ret_5":top10_[4],
                                             "ret_6":top10_[5],
                                             "ret_7":top10_[6],
                                             "ret_8":top10_[7],
                                             "ret_9":top10_[8],
                                             "ret_10":top10_[9]
                                             })



if __name__ == '__main__':
    app.run(debug=True)


