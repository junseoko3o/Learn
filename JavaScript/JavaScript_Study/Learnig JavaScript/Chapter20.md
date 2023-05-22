# Node

## 모듈
- 패키지를 만들고 코드를 네임스페이스로 구분하는 메커니즘이다.
- exports 프로퍼티에 무엇을 할당하든, 모듈은 그것을 내보낸다.


# Node.js & Express

- Node.js 는 2009년에 릴리즈 되었다. 그 전까지는 자바스크립트는 프론트엔드에서만 사용하는 언어라는 인식이 강했고, 실제로 그랬다. 웹 시장이 커질 때 동적 페이지를 다루기 위해HTML내의 <script> 태그로 삽입하여 주로 사용했다. 하지만 브라우저에 삽입된 소스코드가 그대로 노출되고 보안에 취약하다는 인식이 있었고 사용은 많이 하지만 그냥 스크립트언어 라는 괄시를 받았다. 이후 Node.js 의 등장으로 자바스크립트를 이용하여 서버를 구동할 수 있게 되었다.
- 프론트엔드와 백엔드에서 같은 언어를 사용한다는 것은 큰 장점이다. 같은 개발자가 풀스택으로 개발할 경우 생산성을 향상시켜주고, 프론트엔드/백엔드가 분리되어 있다 하더라도 커뮤니케이션 비용을 줄여준다. Node.js의 등장으로 자바스크립트는 당당히 하나의 언어로 인정받게 되었다. 2008년 구글은 크롬 브라우저를 출시하면서 자체 개발한 자바스크립트 엔진인 V8을 크롬에 내장했다. V8의 뛰어난 성능은 자바스크립트는 느리다 라는 인식을 바꾸어 주었다.

- Node.js 는 NPM(Node Package Manager) 이라고 하는 패키지 또는 라이브러리 관리 시스템을 가지고 있다. 누구나 자신이 만든 Node.js 기반 라이브러리를 등록하여 다른 사람들이 사용하게 공개할 수 있다. 비공개도 가능

- 싱글쓰레드에서 구동되는 non-blocking I/O 이벤트 기반 비동기 방식
    - 작업 요청이 한번에 들어올 때 각 작업을 처리하기 위한 쓰레드를 만들고 할당하는 방식을 멀티쓰레드 방식이라고 한다. 멀티 쓰레드 방식은 여러 작업을 동시에 처리하므로 작업 처리속도가 빠른 장점이 있지만, 공유 자원을 관리하는 노력이 많이 들고 잘못 작성된 동기화로 인해 락에서 빠져나오지 못하는 경우가 발생하기 쉽다. 쓰레드가 늘어날 때 마다 메모리를 소모하게 되므로 메모리 관리 역시 중요하다.
    - 이에 비해 Node.js는 하나의 쓰레드에서 작업을 처리한다.
    - 사실 애플리케이션 단에서는 단일 쓰레드이지만 백그라운드에서는 쓰레드 풀을 구성해 작업을 처리한다.개발자가 직접 쓰레드 풀을 관리하지 않고 플랫폼, 정확히는 Node.js 에 포함된 libuv가 그 역할을 하기 때문에 개발자는 단일 쓰레드에서 동작하는 것처럼 이해하기 쉬운 코드를 작성할 수 있다. 웹 서버를 운용할 때는 코어(CPU)를 분산해서 관리하므로 실제 작업은 여러개의 코어에서 별개로 처리된다.
    - Node.js는 이렇게 들어온 작업을 앞의 작업이 끝날때까지 기다리지않고 비동기로 처리한다. 입력은 하나의 쓰레드에서 받지만 순서대로 처리하지 않고 먼저 처리된 결과를 이벤트로 반환해주는 방식이다.

- Node.js 장단점
    - 단점은 아무래도 컴파일러 언어의 처리속도에 비해 그 성능이 떨어진다. 하지만 서버의 성능은 꾸준히 발전하고 있고, V8엔진의 성능이 계속 향상되고 있어 왠만한 웹 애플리케이션을 만들기에는 손색이 없다. 이벤트 기반 비동기 방식으로 복잡한 기능을 구현하다 보면 여러 이벤트를 동시에 처리하는 경우 콜백지옥에 빠지는 경우가 있는데 ES6에서 Promise가 도입되면서 간결한 표현으로 작성할 수 있게 되었다. 그리고 후에 async/await 기능이 추가되면서 비동기 동작을 마치 동기로 처리하는 것 처럼 코드를 작성할 수 있게 되었다.

- 여기서 libuv?
    - 비동기 입출력, 이벤트 기반에 초점을 맞춘 라이브러리

## 이벤트 루프

- 6개의 단계(Phase)가 있다. 각 단계는 단계마다 처리해야하는 콜백 함수를 담기 위한 큐를 가지고 있다. 화살표는 각 단계가 전이되는 방향을 뜻하지만 이후에 설명하듯 반드시 다음 단계로 넘어가는 것은 아니다.
- 자바스크립트 코드는 idle & prepare 단계를 제외한 어느 단계에서나 실행될 수 있다.
- nextTickQueue와 microTaskQueue는 이벤트 루프의 구성요소는 아니고 이 큐에 들어 있는 작업 역시 이벤트 루프가 어느 단계에 있는지 실행될 수 있다.
- 이 과정에서 생성된 콜백들이 각 단꼐에 존재하는 큐에 들어가게 되는데 메인 모듈의 실행을 완료한 다음 이벤트 루프를 계속 실행할 지 결정한다. 만약 큐가 모두 비어서 더 이상 수행할 작업이 없다면 Node.js는 루프를 빠져나가고 프로제스를 종료한다.


- Timer 단계
    - 이벤트 루프는 Timer 단계에서 시작한다. Timer 단계의 큐에는 setTimeout이나 setInterval과 같은 함수를 통해 만들어진 타이머들을 큐에 넣고 실행한다.
    - now-registeredTime ≥ delta 인 값을 가지는 타이머들이 큐에 들어간다. 여기서 delta는 setTimeout(() ⇒ {}, delta) 와 같이 타이머가 등록된 시각에서 얼마만큼 시간이 흐른후에 동작해야 하는 지를 나타내는 값이다.
    - 즉, 대상 타이머들은 이미 실행할 시간이 같거나 지났다는 뜻이다. 타이머들은 최소 힙 으로 관리된다. 힙을 구성할 때 기준으로 실행할 시각이 가장 적게 남은 타이머가 힙의 루트가 된다. Timer 단계에서 최소 힙에 들어있는 타이머들을 순차적으로 찾아 실행한 후 힙을 재구성한다.

- Pending(i/o) 콜백 단계
    - 이 단계의 큐에 들어있는 콜백들은 현재 돌고 있는 루프 이전의 작업에서 큐에 들어온 콜백이다. 예를들어 TCP 핸들러 내에서 비동기의 쓰기 작업을 한다면, TCP 통신과 쓰기 작업이 끝난 후 해당 작업의 콜백이 큐에 들어온다. 또 에러 핸들러 콜백도 pending_queue로 들어오게 된다.
    - Timer 단계를 거쳐 pending 콜백 단계에 들어오면 이전 작업들의 콜백이 pending_queue에서 대기중인지를 검사한다. 만약 실행 대기 중이라면 시스템 실행 한도에 도달할 때까지 꺼내 실행한다.

- Idle, Prepare 단계
    - 매 틱(Tick, 매 단계가 이동하는것을 의미) 마다 실행 된다. Prepare 단계는 매 폴링마다 그 전에 실행된다. 이 두 단계는 Node.js의 내부 동작을 위한 것이다.

- Poll 단계
    - 이벤트 루프 중 가장 중요한 단계, Poll 단계에서는 새로운 I/O 이벤트를 가져와서 관련 콜백을 수행한다. 예를들어 소켓 연겨로가 같은 새로운 커넥션을 맺거나 파일 읽기와 같이 데이터 처리를 받아들이게 된다. 이 단계가 가지고 있는 큐는 watch_queue이다.
    - 이 단계에 진입한 후 watch_queue가 비어 있지 않다면 큐가 비거나 시스템 실행 한도에 다다를 떄까지 동기적으로 모든 콜백을 실행한다. 만약 큐가 비게되면 Node.js는 곧바로 다음 단계로 이동하지 않고 check_queue, pending_queue, closing_callbacks_queue에 남은 작업이 있는지 검사한 뒤에 다음단계로 이동한다. 만약 큐가 모두 비어서 해야할 작업이 없다면 잠시 대기 하게 된다. 이때 대기시간은 타이머 최소 힙의 첫번째 타이머를 꺼내 지금 실행할 수 있는 상태라면 그 시간만큼 대기한 후 다음단계로 디오한다.
    - 이렇게 하는 이유는 타이머 단계로 바로 넘어간다 해도 어차피 첫번째 타이머를 수행할 시간이 되지 않았기 때문에 이벤트 루프를 한 번 더 돌아야하므로 Poll 단계에서 시간을 보내는 것이다.

- Check 단계
    - setImmediate의 콜백만을 위한 단계이다. 역시 큐가 비거나 시스템 실행 한도에 도달할 때까지 콜백을 수행한다.

- Close 콜백 단계
    - socket.on(’close’, () ⇒ {}) 과 같은 close나 destory 이벤트 타입의 콜백이 여기서 처리된다. 이벤트 루푸틑 Close 콜백 단계를 마치고 나면 다음 루프에서 처리해야하는 작업이 남아 있는지 검사한다. 만약 작업이 남아있다면 Timer 단계부터 한 번 더 루프를 돌게 되고 아니라면 루프를 종료한다.

- nextTickQueue과 microTaskQueue
    - nextTickQueue는 process.nextTick() API의 콜백들을 가지고 있으며, microTaskQueue는 Resolve된 Promise의 콜백을 가지고 있다. 이 두개의 큐는 기술적으로 이벤트 루프의 일부가 아니다. 즉, libuv 라이브러리에 포함된 것이 아니라 Node.jsdp 포함된 기술이다. 이 두 큐에 들어 있는 콜백은 단계를 넘어가는 과정에서 먼저 실행된다.next는 micro 보다 높은 우선순위를 가지고 있다.

## 웹브라우저 동작원리

### Stack, Queue

```jsx
console.log(1+1); // 1빠
setTimeout(function() { // 3빠
    console.log(2+2)
},1000)
console.log(3+3); // 2빠
```

- 해보면 일반적 프로그래밍 동작방식과 다르다.
    - Stack 이라는 공간에 코드 한줄 한줄 실행을 해준다.
    - 실행중 변수를 만나면 Heap이란 공간에 저장되어있다.
    - Stack은 한번에 코드 한줄만 실행한다. 싱글쓰레드 이다.
    - setTimeout 같은건 바로 실행할 수가 없다. n초 후에 실행을 해야하니까!
    - 이걸 잠깐 대기실에 제껴두고 실행을 해야지만 정상 작동을 한다.
    - 대기실 보내는 코드들
        - Ajax, 이벤트리스너, setTimeout 등등
    - n초 후에 다시 대기실에서 Stack으로 빼와야한다.
    - 이게 Queue 이다.
    - 여기엔 대기가 끝난 코드들이 하나씩 줄을 서있다. 대기가 끝난걸 하나씩 뽑아다 Stack으로 준다.
    - 이건 조건이 있는데 Stack이 텅 비어있을때만 보내서 실행해준다.즉 Stack에 코드들이 다 실행이 정상적으로 됐을때!!!
    - setTimeout 이런거 0초고 나발이고 일단 대기실로 보낸다. 0초라고해서 Stack에 계속 남아있는게 아님!
    - Stack을 바쁘게 하지마십쇼
    - Queue를 바쁘게 하지 마십쇼

  ## 자바스크립트는 동기적? 비동기적?

- 원래 동기적으로 실행이 된다. 즉 한번에 한줄씩 순서대로 ㄱㄱ
- 가끔 비동기 처리도 가능하다.-
    - 뭐 setTimeout, 이벤트리스너,ajax 함수 이런거 쓰면 되긴함.
