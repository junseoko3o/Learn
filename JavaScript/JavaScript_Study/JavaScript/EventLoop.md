# JavaScript Event Loop
- 싱글스레드 기반으로 동작하는 자바스크립트
- 이벤트 루프를 기반으로 하는 싱글 스레드 Node.js

## JavaScript Engine
- JavaScript를 해석하는 JavaScript Engine과 웹 브라우저에 화면을 그리는 Rendering Engine은 다른것이다. 
- RenderingEngine(LayoutEngine)은 HTML과 CSS로 작성된 마크업 관련한 코드들을 콘텐츠로서 웹 페이지에 redering 하는 역할을 한다.
- JavaScript Engine 이란 JavaScript로 작성한 코드를 해석하고 실행하는 인터프리터다.
- 주로 웹 브라우저에서 이용되지만 node.js라는게 등장하면서 server side에선 V8과 같은 Engine이 이용된다.

## V8
### Call Stack
- JavaScript는 단 하나의 호출스택을 사용한다. 이러한 특징 때문에 함수가 실행되는 방식을 Run to Completion 라고 한다.
- 이는 하나의 함수가 시랭되면 이 함수의 실행이 끝날 때까지 어떤 task도 수행될 수 없다는 의미이다.
- 요청이 들어올 때마다 해당 요청을 순차적으로 호출 스택에 담아 처리한다. 메서드가 실행될 때 Call Stack에 새로운 프레임이 생기고 push 되고 메서드의 실행이 끝나면 해당 프레임은 pop되는 원리이다.

```javascript
function abc(b) {
    let a = 10;
    return a + b;
}

function cdf(x) {
    let y = 2;
    return a(x + y);
}
console.log(b(1));
```

- cdf 라는 함수를 호출 했으니 cdf에 해당하는 스택 프레임이 형성되고 그 안에는 y와 같은 local variable과 arguments가 함께 생성된다.
- 그리고 cdf는 abc함수를 호출하고 있다. 아직 cdf 함수가 종료되지 않았으니 pop되지 않고 호출된 abc 함수가 Call Stack에 push된다.
- abc 함수에서는 a+b라는 값을 return 하면서 함수의 역할을 모두 마쳤으므로 stack에서 pop된다. 
- 다시 cdf함수로 돌아와 abc함수로부터 빧을 값을 return 하면서 cdf함수도 종료되고 stack에서 pop된다.

### Task Queue (Event Queue)
- JavaScript 런타임환경에서는 처리해야하는 Task들을 임시 저장하는 대기 큐가 존재한다.
- Call Stack이 비어졌을 때 먼저 대기열에 들어온 순서대로 수행된다.
```javascript
setTimeout(() => {
    console.log('1');
},0);
console.log('2');

// 2
// 1
```
- JavaScript 에서 비동기로 호출되는 함수들은 Call Stack에 쌓이지 않고 Task Queue에 enqueue된다. 
- JavaScript에서는 이벤트에 의해 실행되는 함수들이 비동기로 실행된다. Web API영역에 따로 정의되어 있는 함수들은 비동기로 실행된다.


```javascript
function test1() {
    console.log('test1');
    test2();
}

function test2() {
    let timer = setTimeout(() => {
        console.log("test2");
    },0);
    test3();
}

function test3() {
    console.log("test3");
}

test1();
```
- 일단 test1()이 찍힌다. 그리고 test2()가 호출되면서 setTimeout 함수가 실행되고 Call Stack에 들어갔다 바로 빠져나온다.
- 내부에 걸려있던 익명함수는 Call Stack에 들어가서 바로 실행되지 않는다. 이 핸들러는 call stack영역이 아닌 event queue영역으로 들어간다.
- test3 함수가 Call Stack으로 들어간다.
- test3()까지 console에 찍히고 작업을 모두 마친 test3 함수가 Call Stack에 들어가서 pop 된다.
- test2 함수와 test1 함수까지 Call Stack에서 pop 된다.
- 이 때 이벤트 루프의 Call Stack이 비어있게 된다.
- 이 시점에 queue의 head에서 하나의 event를 가져와 Call Stack에 넣는다.(setTimeout 내부에 있는 익명함수)

- test3 -> test2 -> test1 이 마저 끝나고 나서 이벤트 루프에 의해 하나의 event가 dequeue된 다음 Call Stack으로 들어가서 실행된다.
- 이벤트에 걸려있는 핸들러는 절대 먼저 실행될 수 없다.


### 참고
```javascript
while (queue.waitForMessage()) {
    queue.processNextMessage();
}
```
- 이벤트 루프는 현재 실행중인 테스크가 없는지와 테크스 큐에 테스크가 있는지를 반복적으로 확인한다.
- 큐에 메세지 즉 처리해야할 이벤트 또는 테스크가 존재하면 while-loop안에 들어가 해당하는 이벤트를 처리하거나 작업을 수행한다.
- 다시 큐로 돌아와 새로운 이벤트가 존재하는지 파악한다.
- Event Queue에서 대기하고 있는 Event들은 한 번에 하나씩 Call Stack으로 호출되어 처리된다.

### 비동기 요약
- Stack 이라는 공간에서 코드 한 줄씩 실행을 해준다
- 실행 중 변수를 만나면 Heap이라는 공간에 저장되어있다.
- Stack은 한 번에 코드 한 줄만 실행한다. 즉, 싱글 쓰레드
- setTimeout 같은건 바로 실행할 수 없다 n초 후에 실행되니까
- 이걸 잠깐 대기실에 제껴두고 실행을 해야만 정상 작동한다.
- 대기실에 대표적으로 보내는 코드는 Ajax, 이벤트리스너,setTimeout 등등
- n초 후에 다시 대기실에서 Stack으로 빼와야한다.
- 이게 Queue
- 여기엔 대기가 끝난 코드들이 하나씩 줄을 서있다. 대기가 끝난걸 하나씩 뽑아다 Stack으로 넘긴다.
- 이건 조건이 있는데, Stack이 텅 비어있을 때만 보내서 실행해준다. 즉, Stack에 코드들이 다 실행이 적상적으로 됐을때!
- setTimeout 이런거 0초고 나발이고 일단 대기실로 보낸다. 0초라 해서 Stack에 계속 남아있는게 아니다 참고!
