# Closure
- 두 개의 함수로 만들어진 환경으로 이루어진 특별한 객체의 한 종류
- 환경은 클로저가 생성될 때 그 범위에 있던 여러 지역 변수들이 포함된 context를 의미
- 클로저를 통해서 자바스크립트에는 없는 private 속성/메서드, public 속성/메서드 를 구현할 수 있는 방안을 바련할 수 있다.

## 생성방법
- 조건
  - 내부 함수가 익명 함수로 되어 외부 함수의 반환값으로 사용된다.
  - 내부 함수는 외부 함수의 실행환경에서 실행된다.
  - 내부 함수에서 사용되는 변수 x는 외부 함수의 변수 스코프에 있다.

```javascript
function outer() {
    var name = 'closure';
    
    function inner() {
        console.log(name);
    }
    inner();
}
outer();

// closure
```
- outer 함수를 실행시키는 context에는 name이라는 변수가 존재하지 않는다.

```javascript
var name = 'Warning';

function outer() {
    var name = 'closure';
    return function inner() {
        console.log(name);
    };
}

var callFunc = outer();
callFunc();
// closure
```
- callFunc를 클로저라고 한다. callFunc 호출에 의해 name이라는 값이 console에 찍히는데 찍히는 값은 closure이다.
- 즉, outer 함수의 context에 속해있느니 변수를 참조 하는것이다.
- 여기서 outer 함수의 지역변수로 존재하는 name 변수를 자유변수 라고 한다.
- 외부 함수 호출이 종료되더라도 외부 함수의 지역변수 및 변수 스코프 객체의 체인 관계를 유지할 수 있는 구조를 클로저 라고한다.
- 보다 정확히는 외부 함수에 의해 반환되는 내부 함수를 가리키는 말이다.