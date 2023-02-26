# 과목별 점수 입력 합격여루 모듈 (평균60점이상 합, 40점 이하 과락)

import passFail as pf

if __name__ == '__main__':
  sub1 = int(input('과목1 점수: ')) 
  sub2 = int(input('과목2 점수: ')) 
  sub3 = int(input('과목3 점수: ')) 
  sub4 = int(input('과목4 점수: ')) 
  sub5 = int(input('과목5 점수: ')) 
  
  pf.exampleResult(sub1, sub2, sub3, sub4, sub5)