# 국,영,수 점수 입력 후 총점, 평균, 최고점수 과목, 최저점수 과목, 최고점수와 최저 차이 출력
korean = int(input('국어 점수 : '))
english = int(input('영어 점수 : '))
math = int(input('수학 점수 : '))
  
totalScore = korean + english + math
print(f'총점 : {totalScore}')
avg = totalScore / 3
print(f'평균 점수 : %.2f' % avg)
print(f'평균 다른 방식 : {avg: .2f}')

maxScore = korean
maxSubject = '국어'
if english > maxScore:
  maxScore = english
  maxSubject = '영어'

if math > maxScore:
  maxScore = math
  maxSubject = '수학'
  
minScore = korean
minSubject = '국어'
if minScore > english:
  minScore = english
  minSubject = '영어'
  
if minScore > math:
  minScore = math
  minSubject = '수학'

difScore = maxScore - minScore
  
print(f'최고 점수 : {maxScore}, 과목명 : {maxSubject}')
print(f'최저 점수 : {minScore}, 과목명 : {minSubject}')
print(f'최고/최저 차이 : {difScore}')

