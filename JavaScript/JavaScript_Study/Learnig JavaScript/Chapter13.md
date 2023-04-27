# 함수와 추상적 사고
## 함수도 객체다
- 자바스크립트 함수는 Function 객체의 인스턴스
- 변수가 함수인지 아닌지 확인하고 싶다면 먼저 typeof를 써보는 편이 좋다.


## IIFE와 비동기적 코드
```javascript
setTimeout( function() {
    console.log('hello');
},1500);
```
- 내장함수 setTimeout() , 첫 번째 매개변수인 함수를 두 번째 매개변수인 밀리초만큼 기다렸다가 실행
- 1.5초 뒤에 hello 출력

## 함수를 가리키는 변수에 저장할 수 있다.
```javascript
const Money = require('math-money')

const oneDollor = Money.Dollar(1);
const Dollar = Money.Dollar;
const towDollars = Dollar(2);  
```


## 배열에 함수를 넣을 수 있다. 
- pipeline[i]는 파이프라인의 i 번째 요소에 접근하고, 그 요소는 함수로 평가 받는다.
- 그러면 괄호를 써서 함수를 호출한다.
- 각 함수에 점point 를 전달하고 반환값을 다시 그 점에 할당한다.

```javascript
const sin = Math.sin;
const cos = Math.cos;
const theta = Math.PI/4;
const zoom = 2;
const offset = [1, -3];

const pipeline = [
    function rotate(p) {
    return {
        x: p.x * cos(theta) - p.y * sin(theta),
        y: p.x * sin(theta) + p.y * cos(theta),
     };
    },
    function scale(p) {
        return { x: p.x * zoom, y: p.y * zoom};
    },
    function translate(p) {
        return { x: p.x + offset[0],  y: p.y + offset[1]};
    },
];

// 이제 pipeline은 2D 변형에 필요한 함수의 배열이다.
// 점 하나를 변형
const p = {x:1, y:1};
let p2 = p;
for( leti = 0; i < pipeline.length; i++) {
    p2 = pipeline[i](p2);
}
// p2는 이제 p1을 좌표 원점 기준으로 45도 회전
// 원점에서 2 단위 만큼 떨으뜨림
// 1단위 오른쪽, 3단위 아래쪽으로 움직인 점 
```

## 함수를 객체의 프로퍼티로 사용할 수 있다.

## 함수를 함수에 전달할 수 있다.
- 함수에 함수를 전달하는 다른 용도는 비동기적 프로그래밍이다. 이런 용도로 전달하는 함수를 보통 콜백!이라고 한다

## 함수가 함수를 반환할 수 있다.
- 미들웨어는 대개 함수를 반환하는 함수 형태로 만들어진다.

## 함수를 매개변수로 받는 함수를 반환하는 것도 가능하다.

## 재귀
- 자기 자신을 호출하는 함수
- 같은 일은 반복하면서 그 대상이 점차 줄어드는 상황에서 재귀를 유용하게 활용 가능
- 큰 목표 작업 하나를 동일하면서 간단한 작업 여러 개로 나눌 수 있을 때 유₩

```javascript
function findNeedle(haystack) {
    if(haystack.length === 0) return "no haystack here";
    if(haystack.shift() === 'needle') return "fount it"
    return fineNeedle(haystack); 
}
findNeedle(['hay', 'hay', 'hay', 'hay', 'needle', 'hay', 'hay'])
```
- 가능한 경우의 수는 haystack이 비어있거나 배열의 첫 번째 요소가 바늘이거나, 배열의 첫 번째요소가 바늘이 아닌경우
- 마지막은 어딘가 바늘이 있을테니 Array.prototype.shift로 배열의 첫 번째 요소를 제거하고 함수 반복

- 재귀 함수에는 종료 조건이 있어야 한다. 종료 조건이 없다면 자바스클립트 인터프리터에서 스택이 너무 깊다고 판단할 때까지 재귀 호출을 계속하다가 프로그램이 멈춘다.

```javascript
// 반복적 사고를 통한 방법 : for 루프
function pow(x, n) {
    let result = 1;
    
    // 반복문 돌면서 x를 n번 곱함
    for (let i = 0; i < n; i++) {
        result *= x;
    }
    return result;
}
console.log(pow(2,3)); // 8

// 재귀적인 사고를 통한 방법: 작업을 단순화하고 자신을 호출
function pow1() {
    if (n === 1) {
        return x;
    } else {
        return x * pow(x, n-1);
    }
}
console.log(pow1(2,3)); // 8
```
- n === 1 일때 
  - 모든 절차가 간단해진다. 명확한 결과값을 즉시 도출해 재귀의 베이스라한다. pow(x,1) 은 x이다.
- n !== 1 일때
  - pow1(x,n)은 x * pow1(x, n-1) 으로 표현가능하다. 이를 재귀단계라한다.
  - 재귀 단계는 n 이 1이 될때 까지 계속 이어진다.



