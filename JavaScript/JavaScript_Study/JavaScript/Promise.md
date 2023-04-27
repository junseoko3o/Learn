# Promise
- 콜백이 중첩되는 경우(콜벡헬)가 발생하면서, 이를 해결할 방안으로 등장!
- Promise 패턴을 사용하면 비동기 작업들을 순차적으로 진행하거나, 병렬로 진행하는 등의 컨트롤이 보다 수월해진다.
- 또한 예외처리에 대한 구조가 존재하기 때문에 오류 처리 등에 대해 보다 가시적으로 관리 가능!
- 그러니까 Promise 쓰면 then만 하지말고 꼭 catch로 에러도 잡아주자!


```javascript
let promiseEx = function (param) {
    return new Promise(function (resolve, reject) { // promise 객체에서 파라미터로 익명함수를 받고 그 익명함수는 resolve와 reject를 파라미터로 받음
        
        // 비동기 표현
        window.setTimeout(() => {
            // 파라미터가 참이면
            if (param) {
                // 해결
                resolve('resolve');
            }
            // 거짓이면
            else {
                // 실패
                reject(Error('failed'));
            }
        },3000)
    })
}

// Promise 실행
promiseEx(true) // promise 함수를 호출해서 Promise 객체가 리턴된다. 
    .then(JSON.parse) // 에러 유발시킴 promiseEx에서 만든 객체는 성공또는 실패시 String을 리턴하기 때문
    .catch ( () => { // 그래서 여기서 에러를 잡아준다.
        alert('체이닝 중간에 에러!');
    })
    .then( text => { // 위에 catch에서 걸려서 여기 then으로 이동하지 못함.
        console.log(text);
    })
```

- promise state
  - pending
    - 아직 수행중인 상태 fulfilled 혹은 reject 되게 전 상태
  - fulfilled
    - 수행된 상태
  - rejected
    - 실패된 상태
  - settled
    - 수행이되고 실패가 되든 성공이되든 일단 결론이 난 상태


## Promise.all 
- 여러개의 비동기 작업들이 존재하고 이들이 모두 완료되었을 때 작업을 진행하고 싶을때 사용!

```javascript
let promise1 = new Promise((resolve, reject) => {
    setTimeout(() => {
        
        console.log('첫번째 Promise 완료');
        resolve('11111');
    }, 3000)
});

let promise2 = new Promise((resolve, reject) => {
    setTimeout( () => {
        console.log('두번째 Promise 완료');
        resolve('222222');
    }, 2000)
});

Promise.all([promise1, promise2]).then( valuse => {
    console.log('모두 완료', valuse);
})

// 결과
// 두번째 Promise 완료
// 첫번째 Promise 완료
// 모두 완료 [ '11111', '222222' ]
```
- 두번째 Promise가 완료된 뒤에 첫번째 Promise가 완료되면 최종적으로 전체값을 보여준다.

## return 하지 않고 바로 new Promise 생성
- Promise 객체에 파라미터로 넘겨준 익명함수는 즉각 실행된다.

- 위의 코드를 return 하는 형태로 변경
```javascript
let promise1 = function () {
    return new Promise((resolve, reject) => {
        setTimeout(() => {

            console.log('첫번째 Promise 완료');
            resolve('11111');
        }, 3000)
    });
}


let promise2 = function () {
    return new Promise((resolve, reject) => {
        setTimeout(() => {

            console.log('두번째 Promise 완료');
            resolve('222222');
        }, 2000)
    });
}


// Promise.all([promise1, promise2]).then( valuse => {
//   console.log('모두 완료', valuse);
// })

Promise.all([promise1(), promise2()])
    .then( values => {
    console.log('모두 완료', values)
})

```
- 위의 예시는 그 위의 예시와 같이 Promise.all을 사용할 수 없다. 
- 위의 주석처럼 사용하면 Promise 객체가 아니기 때문에 에러가 나온다. 