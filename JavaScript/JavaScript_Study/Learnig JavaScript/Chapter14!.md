# 비동기적 프로그래밍
- 자바스크립트는 단일 스레드에서 동작한다. 즉, 한 번에 한 가지 일만 할 수 있다.
- 처음에는 콜백이 있었고, 프로미스가 뒤를 이었으며 마지막은 제너레이터이다. 
- 제너레이터  자체는 비동기적 프로그래밍을 지원하지 않는다.  
- 제너레이터를 비동기적으로 사용하려면 프로미스나 특수한 콜백과 함께 사용해야 한다. 
- 비동기적 테크닉을 사용해야 하는 경우
  - Ajax 호출을 비롯한 네트워크 요청
  - 파일을 읽고 쓰는 등의 파일시스템 작업
  - 의도적으로 시간 지연을 사용하는 기능(ex 알람)

## 콜백
- 콜백 함수는 일반적으로 다른 함수에 넘기거나 객체의 프로퍼티로 사용한다. 보통 익명 함수로 사용
- setTimeout은 콜백의 실행을 지정된 밀리초 만큼 지연하는 내장 함수
```javascript
console.log('before time');

function f() {
    console.log('after time')
}
setTimeout(f, 60*1000)
console.log('i happen after setTimeout')
console.log('me too')

// before timeout
// i happen~
// me too
// after timeout
```
- 비동기적 실행의 가장 큰 목적은 어떤 것도 차단하지 않는다는 것이다. 

## setInterval 과 claer Interval
- setTimeout은 콜백 함수를 한 번만 실행하고 멈추지만 setInterval은 콜백을 정해진 주마다 호출하며 clearInterval을 사용할때까지 멈추지 않는다.

```javascript
const start = new Date();
let i = 0;
const intervalid = setInterval(function() {
    let now = new Date();
    if(now.getMinutes() !== start.getMinutes() || ++i > 10)
        return clearInterval(intervalid);
    console.log(`${i}: ${now}`);
}, 5 * 1000)
```
- 10회째가 될 때까지 5초마다 콜백을 실행한다. setInterval이 ID를 반환한다. 이 ID을 써서 실행을 멈출 수 있다.
- claerInterval은 setInterval이 반환하는 ID를 받아 타임아웃을 멈춘다

## Promise
- 콜백의 단점을 해결하려는 시도 속에서 만들어졌다.
- Promise 기반 비동기적 함수를 호출하면 그 함수는 Promise 인스턴스를 반환한다.
- Promise는 fulfilled하거나, rejected하거나 단 두가지 뿐이다.
- 성공이든 실패든 단 한번만 일어난다. settled
- Promise는 객체이므로 어디든 전달할 수 있다.

- Promise 만들기
```javascript
const myPromise = new Promise( (resolve, reject) => {
    setTimeout(() => {
        resolve(1);
    }, 1000);
});

myPromise
    .then( n => {
    console.log(n)
    })
    .catch(err => {
        console.log(err);
    })

```
## Promise Chain
- Promise는 체인으로 연결할 수 있다는 장점이 있다. 즉, Promise가 완료되면 다른 Promise를 반환하는 함수를 즉시 호출 가능

```javascript
const EventEmitter = require('events').EventEmitter;

class Countdown extends EventEmitter {
    constructor(seconds, superstitious) {
        super();
        this.seconds = seconds;
        this.superstitious = !!superstitious;
    }
    go() {
        const countdown = this;
        const timeoutIds = [];
        return new Promise(( resolve, reject) => {
            for(let i = countdown.seconds; i >=0 ; i--) {
                timeoutIds.push(setTimeout(() => {
                    if(countdown.superstitious && i === 13) {
                        timeoutIds.forEach(clearTimeout);
                        return reject(new Error('hey!!!!'));
                    }
                    countdown.emit('tick', i);
                    if( i === 0) reslove();
                }, (countdown.seconds - i) * 1000));
            }
        })
    }
}


function launch() {
    return new Promise((resolve, reject) => {
        console.log('Lift off!');
        setTimeout(() => {
            resolve('In orbit');
        }, 2*1000)
    })
}

const c = new Countdown(5);
    .on('tick', i => console.log(i + '...')); // 체인으로 연결
    
c.go()
        .then(launch)
        .then( msg =>  {
            console.log(msg);
        })
        .catch(err => {
            console.error('problem..')
        })

```

- promise chain을 사용하면 모든 단계에서 에러를 캐치할 필요는 없다. 체인 어디에서든 에러가 생기면 체인 전체가 멈추고 catch핸들러가 동작한다.
- 카운트 다운을 15초로 바꿔서 실행 해보면 launch는 실행되지 않는다.

## 결정되지 않는 Promise 방지
- Promise는 기본적으로 비동기적 코드를 단순화하고 콜백이 두 번 이상 실행되는 문제를 방지한다.
- 하지만 resolve나 reject를 호출하는 걸 잊어서 프라미스가 결정되지 않는 문제까지 자동으로 해결하지는 못한다.
- 에러가 일어나지 않아 이런 실수는 찾기 매우 어렵다. 
- 그래서 결정되지 않은 프라미스를 방지하는 한 가지 방법은 프라미스에 타임아웃을 건다.
- 충분한 시간이 지났는데도 프라미스가 결정되지 않으면 자동으로 실패하게 만드는 것이다.

- 프라미스에 타임아웃을 거는 함수
```javascript
function addTimeout(fn, timeout) {
    if(timeout === undefined) timeout = 1000; // 타임아웃 기본값
    return function(...args) {
        return new Promise((resolve, reject) => {
            const tid = setTimeout(reject, timeout, new Error('promise time out'));
          fn(...args)
                  .then(function(...args) {
                      clearTimeout(tid);
                      resolve(...args);
                  })
                  .catch(function(...args) {
                      clearTimeout(tid);
                      reject(...args);
                  });
        });
    }
}
```
- promise에 타임아웃을 걸기 위해서는 함수를 반환하는 함수가 필요하다.

## Promise.all
- 배열로 받은 프라미스가 모두 완료될 때 완료가 된다. 가능하다면 비동기적 코드를 동시에 실행.
- 반환하는 프라미스에는 매개변수로 주어진 각 프라미스의 완료 값이 배열에 들어있던 순서대로 들어온다.


## 요약
- 자바스크립트의 비동기적 실행은 콜백을 통해 이루어진다.
- 프라미스를 콜백 대신 사용할 수 있는건 아니다. 프라미스 역시 결국 콜백을 사용
- 프라미스는 콜백이 여러 번 호출되는 문제를 해결(콜백헬)
- 콜백을 여러 번 호출해야 한다면 이벤트와 결합하는 방법을 생각할 수 있다. (프라미스도 함께 사용 가능)
- 프라미스는 반드시 결정된다는 보장은 없다. 하지만 프라미스에 타임아웃을 걸면 이 문제가 해결 된다.
- 프라미스와 제너레이터 실행기를 결합하면 비동기적 실행의 장점을 유지한채로 동기적 사고방식으로 문제해결 가능
- 제너레이터를 써서 동기적인 사고방식으로 문제를 해결할 때는 프로그램의 어느 부분을 동시에 실행할 수 있는지는 봐야함. 동시에 실행할 수 있는 부분은 Promise.all 사용
- 제너레이터 실행기를 직접 만드는 고생을 하지 말고 co나 Koa를 쓰자
- 노드 스타일 콜백을 프라미스로 바꾸는 고생도 필요 없다. Q를 쓰자
- 제너레이터 실행기를 쓰면 예외처리도 익숙한 방식으로 할 수 있다.