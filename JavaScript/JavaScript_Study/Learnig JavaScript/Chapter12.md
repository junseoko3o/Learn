# 이터레이터와 제너레이터
- 이터레이터
    - 지금 어디 있는지 파악할 수 있도록 돕는다는 면에서 일종의 책갈피와 비슷한 개념
    - 배열은 이터러블 객체의 좋은
    - 독립적이다. 새 이터레이터를 만들 때마다 처음에서 시작한다. 그리고 각각 다른 요소를 가리키는 이터레이터 여러 개를 동시에 사용할 수도 있다.


## 이터레이션 프로토콜
- 모든 객체를 이터러블 객체로 바꿀 수 있다.
```javascript
class Log {
    constructor() {
        this.messages = [];
    }
    add(message) {
        this.messages.push({ message, timestamp: Data.now()});
    }
    [Symbol.iterator](){
        return this.messages.values();
    }
}
```
- value와 done프로퍼티가 있는 객체를 반환하는 next 메서드를 가진 객체를 반환한다면 그 클래스의 인스턴스는 이터러를 객체 라는뜻

## 제너레이터
- 이터레이터를 사용해 자신의 실행을 제어하는 함수
- 제너레이터와 일반 함수 차이점
    - 언제든 호출자에게 제어권을 넘길 수 있다.
    - 호출한 즉시 실행되지는 않지만 이터레이터를 반환하고, 이터레이터의 next 메서드를 호출함에 따라 실행된다.
- 제너레이터를 만들 때는 function키워드 뒤에 애스터리스크(*)를 붙인다.
- return 외에 yield 키워드 사용

```javascript
function* rainbow() {
    yield 'red';
    yield 'orange';
    //....
}

const it = rainbow();
it.next(); 
it.next();
```

- rainbow 제너레이터는 이터레이터를 반환하므로 for...of 루프에서 사용 가능

## 제너레이터와 return
- return 문을 사용하면 그 위치와 관계없이 done은  true가 되고, value 프로퍼티는 return 이 반환하는 값이 된다.


## 요약
- 이터레이터는 배열이나 객체처럼 여러 가지 값을 제공할 수 있는 컬렌션의 동작 방식을 표준화함
- 제너레이터를 사용하면 함수를 훨씬 더 유연하고 효율적으로 사용할 수 있다. 제너레이터는 모든 연산을 지연시켰다가 필요할 때만 수행하게 만들 수 있다.