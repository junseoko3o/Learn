# 제어문
## while 루프
```javascript

let funds = 50; // 시작 조건

while (funds > 1 && funds < 100) {
    
    
}
```

- 위 코드를 실행하면 영원히 끝나지 않는다. funds는 50에서 시작하고 늘어나거나 줄어들지 않으니 조건은 계속 맞기 때문이다.

## 블록문
- 제어문은 아니지만 제어문과 함께 쓰인다.

```javascript
{ // 블록문을 시작
    console.log("statement 1");
    console.log("statement 2");
} // 블록문 끝

console.log("statement 3")
```

- 1,2 는 블록 안에 있다. 유효한 문법이지만 무의미.
- 블록 문이 유용해지는것은 제어문과 함께 쓰일 때이다.

```javascript
let funds = 50;

while(funds > 1 && funds < 100) {
    funds = funds + 2; 
    funds = funds - 1;
}
```
- 이 while루프에는 끝이 있다. 루프가 반복될 때마다 funds는 2만큼 늘어나고 1만큼 줄어든다.결국 1이 늘어난다. 그러다보면 결국 100이 되면서 루프는 끝이난다.


## 공백
- 대부분 자바스크립트는 줄바꿈 문자를 포함해, 추가 공백을 신경쓰지 않는다. 
```javascript
while(funds > 1 && funds < 100) 

funds = funds + 2;

// 위 코드는 두 문 사이에 연관이 있다는 느낌을 받기 어렵다. 피해야함!!!
```

```javascript
// 줄바꿈 없음
while(funds > 1 && funds < 100) funds = funds + 2;

//줄바꿈 없이 문 하나를 블록 안에
while(funds > 1 && funds < 100) {funds = funds + 2;}
```

- 문 하나만 쓸 때는 블록을 생략해도 괜찮지만, 들여쓰기는 항상 의미가 명확히 드러나도록 써야한다.

```javascript
// 이렇게 절대 하지 말것!
if(funds > 1 ) {
    console.log("hihi");
    console.log("hello");
}else 
    console.log("bye")


// 이렇게도 하지말 것
if (funds > 1)
    console.log("hihi");
else {
    console.log("hello");
    console.log("bye");
}
```
- 같은 if 문 안에서 블록 문과 블록 없는 문을 섞어 쓰지 말아야한다!!!

## 보조함수
```javascript
// m 이상 n 이하의 무작위 정수를 반환
function rand(m, n) {
    return m + Math.floor((n - m + 1)* Math.random());
}

//크라운 앤 앤커 게임 여섯가지 도형 중 하나 무작위 반환
function randFace() {
    return ["crown", "anchor", "heart", "spade", "club", "diamond"]
        [rand(0,5)]
}
```

## if ... else 문
- while문과 달리 if...else 문 자체에는 반복 기능이 없다. 판단하고, 그에 따라 움직인다.
```javascript
const bets = { crouwn:0, anchor:0, heart: 0, spade: 0, club: 0, diamond: 0};

let totalBet = rand(1, funds);

if (totalBet === 7) {
    totalBet = funds;
    bets.heart = totalBet;
}else {
    
}
funds = funds - totalBet;
```

## do...while 루프
- 시작하면서 조건을 검사하지 않고 마지막에 검사한다. 
- 루프 바디를 최소 한 번은 실행하려 할 때 사용한다.
```javascript
let remaining = totalBet;

do {
    let bet = rand(1, remaining);
    let face = randFace();
    bets[face] = bets[face] + bet;
    remaining = remaining - bet;
} while(remaining > 0);
```

## for 루프
- while 루프나 do...while 루프 모두 for 루프로 고쳐 쓸 수 있다.
- 잘 어울리는 경우는 어떤 일을 정해진 숫자만큼 반복하려할 때, 특히 그 일을 지금 몇 번째 하는지 알아야 할 때이다.
- 루프를 제어하는 모든 요소가 한 곳에 있어서 편리하다.
```javascript
const hand = [];

//      초기화       조건       표현식
for(let roll = 0; roll < 3; roll ++) {
    hand.push(randFace());
}
```

## if 문
- if...else 문에서는 모든 분기가 행동으로 연결됐지만, if 문에서는 분기 중 하나만 행동으로 연결된다.

```javascript
let winnings = 0;

for(let die = 0; die < hand.length; die++) {
    let face = hand[die];
    if (bet[face] > 0) winnings = winnings + bets[face];
}

funds = funds + winnings;
```
- 여기서 3보다 작은지 확인하지 않고 hand.length 보다 작은지 확인했다. 

## 전체 
```javascript
// m 이상 n 이하의 무작위 정수를 반환
function rand(m, n) {
    return m + Math.floor((n - m + 1) * Math.random());
}

// 크라운 앤 앵커 게임의 여섯 그림 중 하나에 해당하는 문자열을 무작위로 반환한다.
function randFace() {
    return ["crown", "anchor", "heart", "spade", "club", "diamond"]
        [rand(0,5)];
}

let funds = 50; // 시작 조건
let round = 0;

while(funds > 1 && funds < 100) {
    round++;
    console.log(`round ${round}:`);
    console.log(`\tstarting funds: ${funds}p`);
    
    // 돈을 건다.
    let bets = { crown: 0, anchor: 0, heart: 0, spade:0, club: 0, diamond: 0};
    let totalBet = rand(1, funds);
    
    if(totalBet === 7) {
        totalBet = funds;
        bets.heart = totalBet;
    } else {
        //판돈 나누기
        let remaining = totalBet;
        
        do{
            let bet = rand(1, remaining);
            let face = randFace();
            bets[face] = bets[face] + bet;
            remaining = remaining - bet;
        } while (remaining > 0)
    }
    
    funds = funds - totalBet;
    console.log('\tbets:' + Object.keys(bets).map(face => `${face}: ${bets[face]} pence`).join(',') + `(total: ${totalBet} pence`)
    
    
    //주사위 굴리기
    const hand = [];
    for(let i = 0; i < 3; i++) {
        hand.push(randFace());
    }
    
    console.log(`\thand: ${hand.join(',')}`);
    
    // 딴 돈 가져오기
    let winnings =0;
    
    for(let i = 0; i < hand.length; i++) {
        let face = hand[i];
        if(bets[face] > 0 ) {
            winnings = winnings + bets[face];
        }
    }
    
    funds = funds + winnings;
    console.log(`\twinnings: ${winnings}`);
}
console.log(`\tending funds: ${funds}`)
```

## 제어문의 예외
- break
  - 루프 중간에 빠져나간다.
- continue
  - 루프에서 다음 단계로 바로 건너뛴다.
- return
  - 제어문을 무시하고 현재 함수를 즉시 빠져 나간다.
- throw
  - 예외 핸들러에서 반드시 처리해야 할 예외를 일으킨다. 예외 핸들러는 현재 제어문 바깥에 있어도 상관 없다.


## if...else 문을 체인으로 연결하기
```javascript
if(new Date().getDay() === 3) { // newDate().getDay()는 현재 요일에 해당하는 숫자를 반환한다. 0은 일요일
    totalBet = 1;
} else if (funds === 7) {
    totalBet = funds;
} else {
    console.log('nononononononono')
}
```

## switch 문
- 조건 하나로 여러 가지 중 하나를 선택할 수 있다. 다양하게 나뉘는 조건 사용
```javascript
switch(expression) {
    case value1:
        // expression 을 평가한 결과가 value1일 때 실행된다.
        break;
    case value2:
        // expression을 평가한 결과가 value2일 때 실행된다.
        break;
    case valueN:
        break;
    default:
        // expression을 평가한 결과에 맞는 것이 없을 때 실행된다.
        break;
}
```
- 같은 조건일 경우 break 없는 case절 사용가능하다.
- default 뒤에는 case가 없으므로 break문이 없어도 되지만 항상 사용하는게 좋은 습관이다.
- 언제든 break문을 주석처리할 수 있으므로 break 없는 case절을 이요하더라도 항상 break 문을 쓰는 습관을 들여야한다.

## for...in 루프
- 객체의 프로퍼티에 루프를 실행하도록 설계된 루프
```javascript
for (variable in object)
    statement
```

## for...of 루프
```javascript
for (variable of object)
    statement
```
- 이터러블 객체에 모두 사용할 수 있는 범용적 루프
- 배열에 루프를 실행해야 하지만 각 요소의 인덱스를 알 필요는 없을 때 알맞음

## 유용한 제어문 패턴
- continue 문을 사용해 조건 중첩 줄이기
  - 특정 조건이 맞을때만 루프 바디를 실행할 때가 많다. 즉, 반복문 안에 조건문을 쓰는 경우
```javascript
while(funds > 1 && funds < 100) {
    let totalBet = rand(1, funds);
    if(totalBet === 13) {
        console.log("unlucky")
        continue; // 이 사이에 continue문을 써서 구조를 간결하게 만든다. 루프 바디가 많을때 효과적
    } 
    // else {
    //     
    // }
}
```
- 위와 같은 경우를 제어문 중첩이라 부른다. while 루프의 바디에서 할 일은 대부분 else절이 있고, if 절이 하는 일은 console.log를 호출 하기만 한다.

## break나 return 문을 써서 불필요한 연산 줄이기
- break 문을 쓰면 원하는 것을 찾는 즉시 루프에서 빠져나갈 수 있다.
```javascript
let firstPrime = null;
for(let n of bigArrayOfNumbers) {
    if(isPrime(n)) {
        firstPrime = n;
        break;
    }
}
```
- 이 루프 안에 함수가 있었다면 break 대신 return 문을 써도 된다.

## 루프를 완료한 뒤 인데스 값 사용
- break 문을 써서 루프를 일찍 종료했을 때 인덱스 변수의 값이 필요할 때가 있다.
- for 루프가 끝나도 인덱스 변수의 값은 그대로 유지된다는 점을 활용할 수 있다.

```javascript
let i = 0;
for(; i < bigArrayOfNumbers.length; i++) {
    if(isPrime(bigArrayOfNumbers[i])) break;
}
if( i === bigArrayOfNumbers.length) console.log('No Prime Numbers');
else console.log(`First prime number found at position ${i}`)
```

