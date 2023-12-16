import MBTI_question

ei=MBTI_question.ei
sn=MBTI_question.sn
tf=MBTI_question.tf
jp=MBTI_question.jp

mbti=ei[0]+sn[0]+tf[0]+jp[0]
name=MBTI_question.info

DEBUG=True

# vscode에서는 상대경로 적용 안됨
dirpath="C:\\Users\\KDP-26-\\Desktop\\big_data\\EXAM for PYTHON\\미니프로젝트_박소원\\(230707) python_mini_project_MBTI\\result\\"
# dirpath="./result/"

file=dirpath+f'result_mbti_{name}.txt'
file_total=dirpath+f'result_mbti_total.txt'
file_mbti=dirpath+f'result_mbti_{mbti}.txt'
if DEBUG : pass

with open(file, mode='a', encoding='utf-8') as fp:
    fp.write(f'{name} - {mbti}\n')

with open(file_total, mode='a', encoding='utf-8') as fp:
    fp.write(f'{name} - {mbti}\n')

with open(file_mbti, mode='a', encoding='utf-8') as fp:
            fp.write(f'{name}\n')


class RESULT:
    
    def result():
        mbti_content={'ISTJ':['청렴결백 논리주의자','책임강이 강하며 매사에 성실하고 보수적인 편임\n  => 철저함과 확실성으로 좋은 결과를 이끌어내려고 노력함​'],
              'ISFJ':['용감한 수호자','자신의 의무에 최선을 다하며 꾸준한 노력을 함\n  => 차분하고 인내심이 강하며 타인의 감정변화에 주의를 기울임​'],
              'INFJ':['선의의 옹호자','높은 통찰력으로 사람들에게 영감을 주며 공동체의 이익에 집중함\n  => 화합의 의미와 연관성을 잘 이해함​'],
              'INTJ':['용의주도한 전략가','의지가 강하고 독립적이며 분석력이 뛰어남\n  => 독창적이고 창의적인 마인드로 비전을 제시함​'],
              'ISTP':['만능 재주꾼','어떤 상황에도 적응력이 강하며 과묵함\n  => 원인을 체계적으로 분석하고 핵심을 파악하길 잘함​'],
              'ISFP':['호기심 많은 예술가','논쟁과 갈등을 피해 조화로움을 추구함\n  => 온화하고 겸손하며 삶의 여유를 즐길줄 앎​'],
              'INFP':['열정적인 중재자','가치와 조화를 중요시하며 매사에 호기심이 많음\n  => 성실하고 내적 신념이 강하며 개방적임​'],
              'INTP':['논리적인 사색가','문제해결할때 논리적이고 분석적으로 접근함\n  => 지적호기심이 높으며 잠재력과 가능성을 중요시'],
              'ESTP':['모험을 즐기는 사업가','관용적이며 느긋하고 타협에 능하며 상황에 유연하게 대처할수 있음 \n  => 현실적인 문제를 해결하는데 적극적임'],
              'ESFP':['자유로운 영혼의 연예인','타인과의 상호작용을 좋아하며 환경에 빠르게 적응 가능함\n  => 호기심이 많으며 개방적이고 구체적 사실에 초점을 맞춤'],
              'ENFP':['재기발랄한 활동가','풍부한 상상력을 가지며 순발력이 뛰어남\n  => 일상적으로 반복되는 활동에 지루함을 잘 느낌'],
              'ENTP':['논쟁을 즐기는 변론가','다양한 주제에 관심과 도전하는것을 즐김\n  => 박학다식하고 끊임없이 새로운 시도를 함​'],
              'ESTJ':['엄격한 관리자','체계적이고 규칙을 잘 준수함\n  => 논리적인 기준에 충실하며 효율적인 해결책을 제시할 줄 앎​'],
              'ESFJ':['사교적인 외교관','주변 상황과의 조화로운 관계를 통해 목표에 도달하고자 함\n  => 사람에 대한 관심이 높고 친절함​'],
              'ENFJ':['정의로운 사회운동가','타인의 의견을 존중하며 사교적이지만 비판을 받으면 예민해짐\n  => 협동을 좋아하며 다른이와 함께 성장하기를 좋아함​'],
              'ENTJ':['대담한 통솔자','매사에 철저한 준비를 하며 활동적임\n  => 통솔력이 있고 단호하며 계획과 목표를 바탕으로 자신의 비전을 제시함​']}
        
        for rst in mbti_content.items():
            if mbti==rst[0]:
                print(f'\n{name}님의 MBTI는 [{mbti}-{rst[1][0]}] 입니다.')
                print(f'  => {rst[1][1]}\n')

        if ei=='I3':
            print(f'E 외향형 : 0%   ○○○○○○○○○○ 100% : I 내향형 ')
        elif ei=='I2':
            print(f'E 외향형 : 33%  ●●●○○○○○○○  66% : I 내향형 ')  
        elif ei=='E2':
            print(f'E 외향형 : 66%  ●●●●●●●○○○  33% : I 내향형 ')  
        elif ei=='E3':
            print(f'E 외향형 : 100% ●●●●●●●●●●   0% : I 내향형 ')  

        if sn=='N3':
            print(f'S 감각형 : 0%   ○○○○○○○○○○ 100% : N 직관형 ')
        elif sn=='N2':
            print(f'S 감각형 : 33%  ●●●○○○○○○○  66% : N 직관형 ')  
        elif sn=='S2':
            print(f'S 감각형 : 66%  ●●●●●●●○○○  33% : N 직관형 ')  
        elif sn=='S3':
            print(f'S 감각형 : 100% ●●●●●●●●●●   0% : N 직관형 ')  

        if tf=='F3':
            print(f'T 사고형 : 0%   ○○○○○○○○○○ 100% : F 감정형 ')
        elif tf=='F2':
            print(f'T 사고형 : 33%  ●●●○○○○○○○  66% : F 감정형 ')  
        elif tf=='T2':
            print(f'T 사고형 : 66%  ●●●●●●●○○○  33% : F 감정형 ')  
        elif tf=='T3':
            print(f'T 사고형 : 100% ●●●●●●●●●●   0% : F 감정형 ')  

        if jp=='P3':
            print(f'J 판단형 : 0%   ○○○○○○○○○○ 100% : P 인식형 ')
        elif jp=='P2':
            print(f'J 판단형 : 33%  ●●●○○○○○○○  66% : P 인식형 ')  
        elif jp=='J2':
            print(f'J 판단형 : 66%  ●●●●●●●○○○  33% : P 인식형 ')  
        elif jp=='J3':
            print(f'J 판단형 : 100% ●●●●●●●●●●   0% : P 인식형 ')  
        print()

        mbti_match={'ISTJ':['ENFP','ENFJ'],'ISFJ':['ENTP','ENTJ'],'INFJ':['ESTP','ESTJ'],'INTJ':['ESFP','ESFJ'],'ISTP':['ENFJ','ENFP'],
                    'ISFP':['ENTJ','ENTF'],'INFP':['ESTJ','ESTP'],'INTP':['ESFJ','ESFP'],'ESTP':['INFJ','INFP'],'ESFP':['INTJ','INTP'],
                    'ENFP':['ISTJ','ISTP'],'ENTP':['ISFJ','ISFP'],'ESTJ':['INFP','INFJ'],'ESFJ':['INTP','INTJ'],'ENFJ':['ISTP','ISTJ'],'ENTJ':['ISFP','ISFJ']}
        for m in mbti_match.items():
            if mbti==m[0]: 
                print(f'{name}님과 최고의 궁합은 ?\n  => {m[1][0]}\n')
                print(f'{name}님과 최악의 궁합은 ?\n  => {m[1][1]}\n')
                name_list=input('최고의 궁합, 최악의 궁합 누구인지 보러가기 => 0 \n종료 => 그 외\n')
                if name_list=='0' : 
                    file_good=dirpath+f'result_mbti_{m[1][0]}.txt'
                    fp=open(file_good,mode='r',encoding='utf-8')
                    more=fp.read()
                    print(f'[최고의 궁합]\n{more}\n')
                    fp.seek(0)
                    file_good=dirpath+f'result_mbti_{m[1][1]}.txt'
                    fp=open(file_good,mode='r',encoding='utf-8')
                    more=fp.read()
                    print(f'[최악의 궁합]\n{more}\n')
                    fp.seek(0)
                else : 
                    print('종료합니다.')
                    break


RESULT.result()


