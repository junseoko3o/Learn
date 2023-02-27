# 상품 구매 개수 따라 할인율 결정되는 모듈
# 1개 5%, 2개 10%, 3개 15%, 4개 20%, 5개이상 25%

import productSale as dc

if __name__ == '__main__':
  flag = True
  gs = []
  
  while flag:
    selectNum = int(input('1. 구매 2. 종료'))
    
    if selectNum == 1:
      price = int(input('상품 가격 입력: '))
      gs.append(price)
      
    elif selectNum == 2:
      result = dc.calTotalPrice(gs)
      flag = False
    
    else:
      print('오류')

print(f'할인율: {result[0]}%')
print(f'합계: {result[1]}원')
      