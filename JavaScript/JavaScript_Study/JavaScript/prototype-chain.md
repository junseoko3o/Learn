### 프로토타입 체인에 대해서

아래 코드를 살펴보는 걸로 시작하자 .

```
const profile = {
    name: 'KimTaeOh',
    age: 20
}

console.log(profile.name); // 결과1 : KimTaeOh
console.log(profile.age); // 결과2 : 20
console.log(profile.toString()); // 결과3 : [object Object]
```

결과3이 조금 이상하다 .  
내가 정의한 profile 객체에는 toString 메소드가 존재하지 않는다 .  
그런데 왜 undefined가 아닌 "[object Object]"가 출력될까 ???

정답은 "프로토타입 체인"이다.

다시 아래 코드에서 일어나는 일을 생각해 보자.

```
const profile = {
    name: 'KimTaeOh',
    age: 20
}
```

단순히 리터럴로 객체를 생성하는 문법이지만 자바스크립트 내부에서는 Object.Prototype을 상속받는 일이 발생한다.  
Object.Prototype에는 toString 메소드가 존재한다 .

다시 둘의 관계를 정의해 보자

```
// 자바스크립트 내부에 정의되어 있는 Object.Prototype
Object.Prototype을 = {
    ...
    toString(){
        return "[object Object]"
    }
}

// 리터럴로 객체를 생성하면 자바스크리는 묵시적으로 Object.Prototype을 상속시킨다
const profile = {
    name: 'KimTaeOh',
    age: 20
}

// profile에는 존재하지 않지만 프로토타입에 존재하는 toString메소드를 호출할 수 있다
profile.toString()
```

전통적인 객체지향 프로그래밍의 관점에서 보자면 profile의 부모가 Object.Prototype이라고 할수 있겠다.  
하지만 자바스크립트는 여타 객체지향 프로그래밍과는 다르게 둘의 관계는 그저 연결되어 있을 뿐이며,  
프로퍼티 참조시 연결된 링크를 따라 존재여부를 확인 할 뿐이다 .

이런면에서 부모 자식 보다는 동등하다는 관점이 더 옳다고 보는 것이 좋을 것 같다 .

그럼 profile객체에 toString 메소드가 존재한다면 어떤 일이 발생할까??  
profile객체의 toString메소드가 호출될까 ?  
Object.Prototype의 toString메소드가 호출될까 ?

정답은 당연히도 profile객체의 toString 메소드이다.  
하지만 호출과정은 다른언어의 클래스와는 다르다.  
다시 "프로토타입 체인"이라는 용어에 집중해 보자.

알고리즘은 단순하다 .

1. 객체의 프로퍼티의 존재여부를 판단한다
2. 존재하면 즉시 참조
3. 존재하지 않으면 연결된 프로토타입이 있는지 판단한다.
4. 존재하면 프로토타입에 프로퍼티의 존재여부를 판단한다.
5. 존재하면 즉시 참조

위와 같이 연결된 프로토타입의 체인을 거슬러 올라가며 존재여부를 판단한다 .  
프로토타입 체인의 상위에 동일한 이름이 존재하더라도 알고리즘 2번에 의해 참조되지 않는다 .  
이건 "가림" 이라고 표현하는게 좋겠다.

이제 코드를 작성해 보자

```
// 자바스크립트 내부에 정의되어 있는 Object.Prototype
Object.Prototype = {
    ...
    toString(){
        return "[object Object]"
    }
}

// 리터럴로 객체를 생성하면 자바스크리는 묵시적으로 Object.Prototype을 상속시킨다
const profile = {
    name: 'KimTaeOh',
    age: 20,
    toString(){
        return "Profile Object"
    }
}

// profile 객체에 toString 메소드가 존재하므로 체인을 거슬러 올라가며 프로퍼티를 검색하지 않고 즉시 실행한다 .
// 즉 Object.Prototype의 toString 메소드는 가려졌다 .

console.log(profile.toString()) // 결과 : Profile Obejct
```

마지막으로 그럼 링크는 1:1만 가능한가 ?  
아니다 체인은 무한하게 확장가능하다 ( 그렇다고 무한하게 확장하라는 얘기는 아니다 )

다음 코드를 보자

```

// Object.Prototype을 연결한 a를 생성
const a = {
    onlyA: "onlyA"
}

// a를 연결한 b를 생성
let b = Object.create(a);
b = {
    onlyB: "onlyB"
}

// b를 연결한 c를 생성
let c = Object.create(b);
c = {
    onlyC: "onlyC"
}

// c에 onlyC()이 존재하므로 프로토타입 체인을 뒤지지 않고 즉시 실행
console.log(c.onlyC()) // 결과 : onlyC

// c에 onlyB()이 존재하지 않으므로 링크된 b의 프로퍼티 검색
// b에 onlyB()가 존재하므로 즉시 실행
console.log(c.onlyB()) // 결과 : onlyB

// c에 onlyA()이 존재하지 않으므로 링크된 b의 프로퍼티 검색
// b에 onlyA()가 존재하지 않으므로 링크된 a의 프로퍼티 검색
// a에 onlyA가 존재하므로 즉시 실행
console.log(c.onlyA()) // 결과 : onlyA


// c에 onlyonly()이 존재하지 않으므로 링크된 b의 프로퍼티 검색
// b에 onlyonly()가 존재하지 않으므로 링크된 a의 프로퍼티 검색
// a에 onlyonly()가 존재하지 않으므로 링크된 Object.Prototype의 프로퍼티 검색
// Object.Prototype에 onlyonly가 존재하지 않고 더 링크된 프로토타입이 없으므로 undefined
console.log(c.onlyonly()) // 결과 : undefined

```

### 결론

자바스크립는 상속이 없다 그저 연결된 프로토타입이 있을 뿐이다 .  
용어적으로 상속이라는 표현을 쓰는건 이견이 없으나 프로토타입으로 링크된 동등한 관계라는 것이 더 적절하다고 생각한다.

물론 자바스크립트는 ES6이후부터 Class문법을 공식적으로 지원하기 시작했다 .  
그러나 이는 문법적 설탕에 불과하다 .  
실제 내부 구현은 위에 설명한 프로토타입 체인으로 구현된다는 점을 이해할 필요가 있다 .
