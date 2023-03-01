# 국,영,수,과,국사 점수 입력하면 총점을 비롯한 각종 데이터 출력 프로그램
# 과목별 점수를 입력하면, 총점,평균,편차 출력 
# 평균 (국: 85, 영: 82, 수: 89, 과: 75, 국사: 89)
# 편차데이터는 막대그래프로 시각화 
korAvg = 85; engAvg = 82; mathAvg = 89; sciAvg = 75; hisAvg = 89;
totalAvgScore = korAvg + engAvg + mathAvg + sciAvg + hisAvg
avgAvg = int(totalAvgScore / 5)

korea = int(input('국어 점수: '))
english = int(input('영어 점수: '))
math = int(input('수학 점수: '))
science = int(input('과학 점수: '))
history = int(input('국사 점수: '))

totalScore = korea + english + math + science + history
totalAvg = int(totalScore / 5)

korGap = korea - korAvg 
engGap = english - engAvg 
mathGap = math - mathAvg 
sciGap = science - sciAvg 
hisGap = history - hisAvg 

totalGap = totalScore - totalAvgScore
avgGap = totalAvg - avgAvg

print('-' * 70)
print(f'총점: {totalScore}점, {totalGap}, 평균: {totalAvg}, {avgGap}')
print(f'국어: {korea}점, {korGap}, 영어: {english}점, {engGap}, 수학: {math}점, {mathGap}')
print(f'과학: {science}점, {sciGap}, 국사: {history}점, {hisGap}')

print('-' * 70)

str = '+' if korGap > 0 else '-'
print('국어 편차: {}({})'.format(str * abs(korGap), korGap))
str = '+' if engGap > 0 else '-'
print('영어 편차: {}({})'.format(str * abs(engGap), engGap))
str = '+' if mathGap > 0 else '-'
print('수학 편차: {}({})'.format(str * abs(mathGap), mathGap))
str = '+' if sciGap > 0 else '-'
print('과학 편차: {}({})'.format(str * abs(sciGap), sciGap))
str = '+' if hisGap > 0 else '-'
print('국사 편차: {}({})'.format(str * abs(hisGap), hisGap))

str = '+' if totalGap > 0 else '-'
print('총점 편차: {}({})'.format(str * abs(totalGap), totalGap))
str = '+' if avgGap > 0 else '-'
print('평균 편차: {}({})'.format(str * abs(avgGap), avgGap))