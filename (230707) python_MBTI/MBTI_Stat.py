DEBUG=True

dirpath='C:\\Users\\KDP-26-\\Desktop\\EXAM for PYTHON\\미니프로젝트_박소원\\result\\'
file_total=dirpath+f'result_mbti_total.txt'
if DEBUG : pass


# txt 파일에 저장된 누적 데이터 읽어오기 =======================================================================================
# dict 타입으로 받아서 피설문자의 info가 동일한 경우 가장 최근 데이터를 저장

with open(file_total, 'r', encoding='utf-8') as file:
    mbti_dict = {}
    line = file.readline()

    while line:
        key, value = line.strip().split('-')
        mbti_dict[key.strip()] = value.strip()
        line = file.readline()

#print(f'\nmbti_dict => {mbti_dict}')


# MBTI별 결과값 count =========================================================================================================

count={} # {MBTI : 갯수,...}로 저장
values=list(mbti_dict.values()) # MBTI만 list 생성
mbti_list=['ISTJ','ISFJ','INFJ','INTJ','ISTP','ISFP','INFP','INTP','ESTP','ESFP','ENFP','ENTP','ESTJ','ESFJ','ENFJ','ENTJ']

for m in mbti_list:
    count[m]=values.count(m)


count = sorted(count.items(), key=lambda x: x[1], reverse=True) # value(갯수)로 내림차순 정렬

#print(f'\ncount => {count}')

# MBTI 순위 ===================================================================================================================

rank={count[0]:1} # {MBTI : 순위,...}로 저장

# 동률일 시 공동 순위
for a in range(1,len(count)):
    rank_v=list(rank.values())
    if count[a][1]==count[a-1][1]:
        rank[count[a]]=rank_v[a-1]
    else :
        rank[count[a]]=len(rank_v)+1

#print(f'\nrank => {rank}\n')

rank_i=list(rank.items())

print('====전체 순위====')
for m in range(len(count)):
    print(f'{rank_i[m][1]:>2}위 : {rank_i[m][0][0]} ({rank_i[m][0][1]}명)')


# 각 항목 별 비율 =============================================================================================================

E,I,S,N,T,F,J,P=0,0,0,0,0,0,0,0

for a in range(len(count)):
    if count[a][0][0]=='E':
        E += count[a][1]
    elif count[a][0][0]=='I':
        I += count[a][1]
    if count[a][0][1]=='S':
        S += count[a][1]
    elif count[a][0][1]=='N':
        N += count[a][1]
    if count[a][0][2]=='T':
        T += count[a][1]
    elif count[a][0][2]=='F':
        F += count[a][1]
    if count[a][0][3]=='J':
        J += count[a][1]
    elif count[a][0][3]=='P':
        P += count[a][1]

print('\n============== 항목별 전체 비율 ==============')
print(f'E 외향형 : {E*100/(E+I):<5.2f}% {round(E*10/(E+I))*"●"}{(10-round(E*10/(E+I)))*"○"} {I*100/(E+I):<5.2f}% : I 내향형')
print(f'S 감각형 : {S*100/(S+N):<5.2f}% {round(S*10/(S+N))*"●"}{(10-round(S*10/(S+N)))*"○"} {N*100/(S+N):<5.2f}% : N 직관형')
print(f'T 사고형 : {T*100/(T+F):<5.2f}% {round(T*10/(T+F))*"●"}{(10-round(T*10/(T+F)))*"○"} {F*100/(T+F):<5.2f}% : F 감정형')
print(f'J 판단형 : {J*100/(J+P):<5.2f}% {round(J*10/(J+P))*"●"}{(10-round(J*10/(J+P)))*"○"} {P*100/(J+P):<5.2f}% : P 인식형\n')



