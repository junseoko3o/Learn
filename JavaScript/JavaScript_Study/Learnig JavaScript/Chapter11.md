# 예외와 에러처리
- 에러는 누구나 예상할 수 있는 것
- 예외는 예상치 못한 에러

## Error 객체
```javascript
const err = new Error('invalid email');
```

- 인스턴스를 만드는 것만으로는 아무 일도 일어나지 않는다. 단지 에러와 통신하는 수단일뿐!

```javascript
function validateEmail(email) {
    return email.match(/@/) ? email : new Error('invalid email');
}
```
```javascript

const email = 'abc@abc.com'
const validatedEmail = validateEmail(email);

if (validatedEmail instanceof Error) {
    console.error('error');
} else {
    console.log('good')
}
```
- instanceof 연산자를 써서 Error 인스턴스가 반환됐는지 확인
- 에러메세지는 message 프로퍼티에 있다.
- 예외 처리에서 더 자주 사용됨.

## try/catch 와 예외처리
```javascript
function validateEmail(email) {
    return email.match(/@/) ? email : new Error('invalid email');
}

const email = null;

try {
    const validatedEmail = validateEmail(email);
    if(validatedEmail instanceof Error) {
        console.error('error');
    } else {
        console.log('good');
    }
} catch(err) {
    console.error(`${err.message}`)
}
```

- 실행 흐름은 에러가 일어나는 즉시 catch 블록으로 이동한다. 즉, if 문은 실행되지 않는다.
- 에러가 일어나지 않으면 catch 블록은 실행되지 않는다.

## 에러 일으키기
- 직접 에러를 일으켜서 예외 처리 작업을 시작할 수도있다.
- 자바스크립트는 에러를 일으 킬때 꼭 객체가 아닌 숫자나 문자열 등 어떤 값이든 catch 절에 넘길 수 있다.
```javascript
function billPay(amount, payee, account) {
    if (amount > account.balance) {
        throw new Error('insufficient funds');
    account.tranfer(payee, amount);
    }
}
```
- throw를 호출하면 현재 함수는 즉시 실행을 멈춘다. 따라서 위 예제 에서는 account.transfer가 호출되지 않는다.


## 예외 처리와 호출 스택
- 호출스택
  - 완료되지 않은 함수가 쌓이는 것
- 에러는 호출스택 어디에서든 캐치할 수 있다. 이 에러를 캐치 하지 않으면 자바스크립트 인터프리터는 프로그램을 멈춘다.

## try...catch...finally
- 에러가 일어나지 않으면 실행되지 않는 catch 블록은 안전하지 않다. 
- 이런 상황에서 finally 블록이 필요하다. 
- finally 블록은 에러가 일어나든, 일어나지 않든 반드시 호출된다.

```javascript
try{
    console.log('this line is executed');
    throw new Error('oops');
    console.log('this line is not');
} catch (err) {
    console.log('there was an error');
} finally {
    console.log('always excuted');
    console.log('perform cleanup here')
}
```

## 요약
- 예외는 catch 블록을 만날 때까지 스택을 거슬러 올라가야 하므로 자바스크립트 인터프리터가 예외를 계속 추적하고 있어야한다.
- 프로그램을 일부러 멈추려 하는게 아니라면, 예외를 일으켰다면 반드시!!! 캐치 해야한다!!!
- 캐치 꼭하자!!!!!!! 
- 예외처리는 예상할 수 없는 상황에 대비한 마지노선으로 생각하고, 예상할 수 있는 에러는 조건문으로 처리하는것이 최선이다!
