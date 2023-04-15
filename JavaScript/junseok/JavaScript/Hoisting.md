# Scope
- 함수레벨 블록레벨의 렉시컬 스코프 규칙을 따른다. (ES6 기준)

## Scope Level
- 자바스크립트는 전통적으로 함수 레벨 스코프를 지원했고, 블록 레벨 스코프는 지원하지 않았다.이는 ES6 부터!!

### 함수 레벨 스코프
- var 키워드로 선언된 변수나, 함수 선언식으로 만들어진 함수는 함수 레벨 스코프를 갖는다. 즉 , 함수 내부 전체에서 유효한 식별자가 된다.
```javascript
function foo() {
    if(true) {
        var color = 'blue';
    }
    console.log(color); // blue
}
foo();
```
- 만약 var color가 블록 레벨 스코프였다면 , color는 if문이 끝날때 파괴되고 에러가 발생한다.
- 하지만 color는 함수레벨의 스코프이기 때문에 foo 함수 내부 어디에서든 에러 발생없이 참조가 가능한 것이다.


### 블록 레벨 스코프
- let, const
```javascript
function foo() {
    if(true) {
        let color = 'blue';
        console.log(color); // blue
    }
    console.log(color); // Refference Error
}
foo();
```
- 중괄호 범위!!!
- 함수 레벨 스코프는 블록 레벨 스코프 보다 더 많은 혼란을 야기한다!!!

## 렉시컬 스코프
- 보통 동적 스코프 (Dynamic Scope)와 비교한다.
- 동적 스코프는 프로그램의 런타임 도중의 실행 컨텍스트나 호출 컨텍스트에 의해 결정된다.
- 렉시컬 스코프는 소스코드가 작성된 그 문맥에서 결정된다.
- 렉시컬 스코프 규칙을 따르는 자바스크립트의 함수는 호출 스택과 관계없이 각각의 대응표를 소스코드 기준으로 정의하고 있고, 런타임에 그 대응표를 변경시키지 않는다.


# Hoisting
- var keyword로 선언된 모든 변수 선언은 호이스트 된다.
- 변수의 정의가 그 범위에 따라 선언과 할당으로 분리되는 것을 의미한다.
- 즉, 변수가 함수 내에서 정의되었을 경우, 선언이 함수의 최상위로, 함수 바깥에서 정의되었을 경우, 전역 컨텍스트의 최상위로 변경이 된다.

```javascript
function getX() {
    console.log(x); // undefined
    var x = 100;
    console.log(x); // 100
}
getX();

// 작동순서 코드 재구성
function getX() {
    var x;
    console.log(x);
    x = 100;
    console.log(x);
}
getX();
```
- 다른 언어의 경우엔 변수 x를 선언하지 않고 출력하려 하면 오류
- 하지만 자바스크립트에서는 undefined 를 출력한다.
- var x = 100; 이 코드에서 var x; 를 호이트스 하기 때문이다.

- 선언문은 항시 자바스크립트 엔진 구동시 가장 최우선으로 해석하므로 호이스팅 되고, 할당 구문은 런타임 과정에서 이루어지기 때문에 호이스팅 되지 않는다.
- 함수가 자신이 위치한 코드에 상관없이 함수 선언문 형태로 정의한 함수의 유효범위는 전체 코드의 맨 처음부터 시작한다.
- 함수 선언이 함수 실행 부분보다 뒤에 있더라도 자바스크립트 엔진이 함수 선언을 끌어올리는 것을 의미한다. 함수 호이스팅은 함수를 끌어올리지만 변수의 값을 끌어 올리지 않는다.

```javascript
foo();
function foo() {
    console.log('hi');
};
// hi
```
- foo 함수에 대한 선언을 호이스팅하여 global 객체에 등록시키기 때문에 hi가 제대로 출력된다.

```javascript
foo();
var foo = function(){
    console.log('hi')
};
// foo is not a function
```
- 함수 표현은 함수 리터럴을 할당하는 구조이기 때문에 호이스팅 되지 않으며 그렇기 떄문에 런타임 환경에서 Type Error가 출려된다.
