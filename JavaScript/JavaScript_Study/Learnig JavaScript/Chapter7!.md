# 스코프
- 변수와 상수, 매개변수가 언제 어디서 정의 되는지 결정

## 스코프와 존재
- 가시성 visibility 라고도 불리는 스코프는 프로그램의 현재 실행 중인 부분, 즉 실행 컨텍스트에서 현재 보이고 접근할 수 있는 식별자들을 말한다.
- 반면 존재한다는 말은 그 식별자가 메모리가 할당된 무언가를 가리키고 있다는 

## 정적 스코프와 동적 스코프
```javascript
function f1() {
    console.log('1');
}
function f2() {
    console.log('2');
}

f2();
f1();
f2();
```

- 정적으로 보면 이 프로그램은 단순히 위에서 아래로 읽어내리는 문의 연속이다.
- 하지만 실행하면 다르다. f1이 f2보다 먼저 정의 됐지만 f2의 함수 바디가 실행된 다음 f1으로, 다시 f2로 넘어간다.

- 자바스크립트의 스코프는 정적이다. 

```javascript
const x = 3;

function f() {
    console.log(x);
    console.log(y);
}
// new scope
{
    const y = 5;
    f();
}
```
- 변수 x는 함수 f를 정의할 때 존재하지만, y는 그렇지 않다. y는 다른 스코프에 존재한다.
- 다른 스코프에서 y를 선언하고 그 스코프에서 f를 호출하더라도, f를 호출하면 x는 그 바디 안의 스코프에 있지만 y는 그렇지 않다 -> 정적 스코프
- 정적스코프
  - 전역,블록,함수

## 전역 스코프
- 전역 스코프에서 선언된 것들은 전역 변
```javascript
let name = "abc"; // 전역
let age = 25;

function greet() {
    console.log(`hi, ${name}`)
}

function getBirthDay() {
    return new Date().getFullYear() - age;
}

// let user = {             -> 정보를 단일 객체에 보관하는 방법이 더 낫다.
//     name = 'abc';
//     age = 25,
// };
```

- 전역 스코프에 의존하지 않게
```javascript
function greet(user) {
    console.log(`hi, ${user.name}`);
}
function getBirthYear(user) {
    return new Date().getFullYear() - user.age;
 }
```
- 이제 이 함수들은 모든 스코프에서 호출할 수 있고, 명시적으로 user를 전달 받았다. 
- 스케일이 커질수록 전역스코프에 의존하지 않는것이 중요


## 블록 스코프
- let, const는 식별자를 블록 스코프에서 선

## 함수,클로저, 정적 스코프
- 클로저
  - 함수가 특정 스코프에 접근할 수 있도록 의도적으로 그 스코프에서 정의하는 경우
  - 스코프를 함수 주변으로 좁히는 것

```javascript
let globalFunc; // 정의 되지 않은 전역함수
{
    let blockVar = 'a'; //블록 스코프 변수
    globalFunc = function() {
        console.log(blockVar);
    }
}
globalFunc(); // a
```
- globalFunc는 블록 안에서 값을 할당 받았다. 이 블록 스코프와 그 부모인 전역 스코프가 클로저를 형성한다.
- globalFunc를 어디서 호출하든, 이 함수는 클로저에 들어있는 식별자에 접근할 수 있다.
- 스코프 안에서 함수를 정의햇고, 해당 함수는 스코프 밖에서도 참조할 수 있으므로 자바스크립트는 스코프를 계속 유지한다.
- 스코프 안에서 함수를 정의하면 해당 스코프는 더 오래 유지
- 접근할 수 없는것에 접근
```javascript
let f;
{
    let o = {note : 'Safe'};
    f = function() {
        return o;
    }
}
let oRef = f();
oRef.note = 'Not so safe after all';
```
- 일반적으로 자신의 스코프에 없는 것들에는 접근할 수 없다. 함수를 정의해 클로저를 만들면 접근할 수 없었던 것들에 접근할 방법이 생김!

## 함수 스코프와 호이스팅
- 원래코드
```javascript
var x = 3;
if ( x === 3) {
    var x = 2;
    console.log(x);
}
console.log(x);
```

- 자바스크립트 해석 코드
```javascript
var x;
x = 3;
if (x === 3) {
    x = 2;
    console.log(x);
}
console.log(x);
```
- var문을 두번 썻지만 변수 x는 하나이다. 

## 함수 호이스팅
- 함수를 선언하기 전에 호출 가능
```javascript
f(); // 'f'

function f() {
    console.log('f');
}
```
- 변수에 할당한 함수표현식은 끌어올리지 않는다.
```javascript
f();

let f = function() { // ReferrenceError : f
    console.log('f');
}
```

## 사각지대 temporal dead zone
- let으로 선언하는 변수는 선언하기 전까지 존재하지 않는다는 직관적 개념
- 스코프 안에서 변수의 사각지대는 변수가 선언되기 전의 코드

```javascript
if (typeof x === 'undefined') {
    console.log('x is not exist or undefined')
} else { 
    // x를 사용해도 안전
}
```

- 하지만 이걸 let으로 변수를 선언하면 안전하지 못하다.
```javascript
if(typeof x === 'undefined') {
    console.log('x is not exist or undefined');
} else {
    // x를 사용해도 안전
}
let x = 5;
```

## 스트릭트 모드
- 암시적 전역변수 허용하지 않는다. 엄격하게!!!봐줌


