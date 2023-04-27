# Async/Await
- function 키워드 앞에 async를 붙여주면 되고 function 내부의 promise를 반환하는 비동기 처리 함수 앞에 await을 붙여주기만 하면된다.
- Arrow function에도 사용이 가능하다.
- promise를 더 간결하고 이쁘게
- await
  - promise가 해결될 때까지 기다려주세요...then 대신 사용가능


## Promise의 문제점
- 디버깅
  - then() 을 연쇄적으로 호출하면 몇 번째 then()에서 문제가 발생한건지 혼란스러울 수 있다.
  - then() 메서드 호출부에 break point를 걸고 디버깅하면 화살표 함수로 한 줄 짜리 콜백함수를 넘겼을 경우 break point에서 멈추지 않아 불편하다.
- 예외처리
  - catch() 메서드를 사용해 예외처리를 하는데 비동기 코드만 있으면 괜찮은데, 동기와 비동기가 섞이면 난해하거나 누락하는 경우가 있음
- 들여쓰기
  - then() 메서드의 인자로 넘기는 콜백함수 내에서 조건문이나 반복문을 사용하거나 여러개의 Promise를 병렬로 혹은 중첩해서 호출해야할 경우 가독성이 안좋아진다.

### Promise로 구현
```javascript
function makeRequest() {
    return getData()
        .then(data => {
            if(data && data.needMoreRequest) {
                return makeMoreRequest(data)
                    .then(moreData => {
                        console.log(moreData);
                        return moreData;
                    }).catch((error) => {
                        console.log('Error while makeMoreRequest', error);
                    });
            } else {
                console.log(data);
                return data;
            }
        }).catch((error) => {
            console.log('Error while getData', error);
        });
}
```



### Async/Await으로 구현
```javascript
async function makeRequest() { 
    try {
      const data = await getData();
      if(data && data.needMoreRequest) {
          const moreData = await makeMoreRequest(data);
          console.log(moreData);
          return moreData;
      } else {
          console.log(data);
          return data;
      }
    } catch (error) {
        console.log('Error while getData', error);
    }
}
```

## 한 번더 예제
```javascript
// sleep이란 함수를 만들어서 파라미터로 넣어준 시간 만큼 기다리는 Promise 생성
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms))
}
// process 함수에서 사용 Promise 반환
async function process() {
    console.log('hi');
    await sleep(1000);
    console.log('nice to meet you');
}

process().then( () => {
    console.log('finish!')
})
```

```javascript
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

async function makeError() {
    await sleep(1000);
    const error = new Error();
    throw error;
}

async function process() {
    try {
        await makeError();
    } catch(error) {
        console.error(error);
    }
}
process();
```

## 예외처리
- 사실 await을 써야할 의무는 없다. 단지 쓰지 않는다면 resolved값이 아니라 promise 객체를 가리킬 것이다.
- 비동기 함수가 직접 await해주지 않는다 본인이 직접 await 해야함! 하지않는다면 예상한 값 대신 promise 객체를 받게 될거다.

- 코드 상위 레벨에서 try/catch로 묶어줘야 한다. 동기/비동기 구분 없이 일관되게 예외처리가 가능하다.


