# 함수
- 하나의 단위로 실행되는 문의 집합
```javascript
function sayHello() { // 함수 선언
    // 함수 바디 (중괄호)
    
    console.log('1');
    console.log('2');
    
    // 닫는 중괄호로 끝
}

sayHello(); // 함수 호출
```

## 반환 값
```javascript
function getGreeting() {
    return "hi"; // 반환 값 퉤
}

getGreeting(); // 함수 호출은 반환 값
```
- return 을 명시적으로 호출하지 않으면 반환 값은 undefined

## 호출과 참조
- 함수도 객체이다. 따라서 넘기거나 할당이 가능하다.
- 예를들어 함수를 변수에 할당하면 다른 이름으로 함수를 호출할 수 있다.
```javascript
const f = getGreeting;
f();

// 객체 프로퍼티에 할당 가능
const o = {};
o.f = getGreeting;
o.f();
```

## 함수와 매개변수
- 함수를 호출하면서 정보를 전달할 때는 함수 매개변수를 이용한다.
- 매개변수는 함수가 호출되기 전에는 존재하지 않는다는 점을 제외하면 일반적인 변수랑 마찬가지이다.
```javascript
function avg(a,b) {
    return (a+b)/2;
    
    // a, b를 정해진 매개변수라고 한다. 함수가 호출되면 정해진 매개변수는 값을 받아 실제 매개변수가 된다.
}

avg(5, 10); // 7.5
```
- 함수 안에서 매개변수에 값을 할당해도 함수 바깥에 있는 어떤 변수에도 아무런 영향이 없다. 
- 하지만 함수 안에서 객체 자체를 변경하면, 그 객체는 함수 바깥에서도 바뀐점이 반영된다.

```javascript
function f(o) {
    o.message = `f 안에서 수정 (이전 값 : ${o.message}`;
}

let o = {
    message: "초기 값"
};

console.log(`f를 호출하기 전: o.message="${o.message}"`); // 초기 값
f(o);
console.log(`f를 호출한 다음: o.message="${o.message}"`); // f안에서 수정 이전값~
```

- 원시 값은 불변이므로 수정할 수 없다. 원시 값을 담은 변수는 수정할 수 있지만 원시 값 자체는 바뀌지 않는다.반면 객체는 바뀔 수 있다.

## 객체 프로퍼티인 함수
- 객체의 프로퍼티인 함수를 메서드 라고 불러서 일반적인 함수와 구별한다. 

## 함수 표현식과 익명함수
- 익명함수에는 함수에 식별자가 주어지지 않는다.
- 식별자가 없다면 어떻게 호출할까? -> 함수표현식

```javascript
const f = function() {
    // ...
}
```
- 결과론적으론 함수 선언과 동등
- 나중에 호출할 생각으로 함수를 만든다면 함수 선언을 쓰고, 다른 곳에 할당하거나 다른 함수에 넘길 목적으로 함수를 만든다면 함수 표현식을 쓰면 된다.


## 화살표 표기
- function 생략가능
- 함수에 매개변수가 단 하나 뿐이라면 괄호도 생략 가능
- 함수 바디가 표현식 하나라면 중괄호와 return 문도 생략 가능

```javascript
const f1 = function() {return "hi"}

const f1 = () => "hi"

////////////////////////////////

const f2 = function(name) {
    return 'h'
}

const f2 = name => 'hi'

//////////////////////////////

const f3 = function(a, b) {
    return a + b;
}

const f3 = (a,b) => a + b;
```

- 중요한 차이 
  - this가 다른 변수와 마찬가지로 정적으로 묶인다.
  - 화살표 함수를 사용하면 내부 함수 안에서 this를 사용할 수 있다.
  - 객체 생성자로 사용할 수 없다.








