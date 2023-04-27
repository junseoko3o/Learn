# 객체와 객체지향 프로그래밍

## prototype
- 자바스크립트는 객체지향 언어이다. 하지만 기타 다른 언어와는 다르게 클래스가 존재하지 않았다. ES6에 class가 생겼지만 문법적일뿐 결국 프로토타입을 통해 상속을 흉내내는것이다.
- 때문에 프로토타입 기반언어라고 부른다.

### 객체 생성시 일어나는일
- 모든 함수는 객체이다. 때문에 prototype 프로퍼티를 가지고 있다.
- 함수 객체와 프로토타입 객체는 서로를 바라고 있다는점이다. 

### 프로토타입 체이닝
```javascript
function Car(name, wheels) {
    this.name = name;
    this.wheels = wheels;
}

Car.prototype.gasoline = function x() {
    return x + 'L Charge'
}
// car 객체 생성
let benz = new Car('benz', 4);
let audi = new Car('audi', 4);
```
- 객체를 생성하면 Car()생성자 함수와 프로토타입 객체도 함께 생성된다.
- 또한 new 키워드를 이용해 benz와 audi 객체를 생성한다.
- 여기서 new 객체 또한 프로토타입 객체를 참조하게 된다.
- __proto__는 프로토타입 객체를 연결한다.
- 두 객체에 gasoline()이 정의되어 있지는 않지만 참조되어 있는 프로토타입 객체의 gasoline()이 있기 때문에 가능한일
  - console.log(benz.gasoline(1)); -> 1 L Charge

### 정리
- 자바스크립트는 gasoline()을 호출하게되면 먼저 객체 내부에서 값을 스캔한다.
- 만약에 값이 없므녀 __proto__ 혹은 [[prototype]] 링크 라고 불리는걸 타고 부모 역할을 하는 프로토타입 객체를 스캔한다.
- 이렇게 자바스크립트는 상속기능을 `흉내` 내서 사용 가능하다.
- 요약
  - __proto__ 속성은 모든 객체들이 가지고 있다.
  - __proto__ 속성은 자신의 상위 역할을 하는 최상단 프로토타입을 가리킨다.
  - 특정 속성을 찾을때 상위 프로토타입을 타고 올라가 스캔하는데 이를 체이닝이라 한다.
  - 최상위 프로토타입은 Object의 Prototype Object이다. 여기까지 값을 스캔하고 없으면 Undefined를 출력한다.

## 프로퍼티 나열
- 객체 프로퍼티에는 순서가 없다.

## for...in
```javascript
const SYM = Symbol();

const o = {
    a: 1,
    b: 2,
    c: 3,
    [SYM]: 4,
}

for(let prop in o) {
    if (!o.hasOwnProperty(prop)) 
        continue;
    console.log(`${prop}: ${o[prop]}`)
}
```
- for...in 을 배열에 사용할 수도 있겠지만 배열에는 일반적인 for 루프나 forEach를 사용하자


## Object.keys
```javascript
const SYM = Symbol();

const o = {
    a: 1,
    b: 2,
    c: 3,
    [SYM]: 4,
}

Object.keys(o).forEach( prop => console.log(`${prop}: ${o[prop]}`))
```
- 객체의 프로퍼티 키를 배열로 가져와야 할때는 Object.keys가 편리하다.
- 객체에서 x로 시작하는 프로퍼티 모두 가져온다?
```javascript
const o = {
    apple: 1,
    xochitl: 2,
    ballon: 3,
    guitar: 4,
    xylophone: 5,
};

Object.keys(o).filter(prop => prop.match(/^x/))
              .forEach(prop => console.log(`${prop}: ${o[prop]}`));
```

## 객체지향 프로그래밍
- 클래스
  - 추상적이고 범용적
- 인스턴스
  - 구체적이고 한정적
- 기능
  - 메서드
- 클래스 메서드
  - 클래스에 속하지만 특정 인스턴스에 묶이지는 않는 기능


## 클래스와 인스턴스 생성
```javascript
class Car {
    constructor() {
        
    }
}

// 인스턴스를 만들 때에는 new 키워드 사용
const car1 = new Car();
const car2 = new Car();

// 객체가 클래스의 인스턴스인지 확인하는 instanceof 연산자
car1 instanceof Car // true
car1 instanceof Array //false
```

```javascript
class Car {
    constructor(make, model) {
        this.make = make;
        this.model = model;
        this.userGears = ['P', 'N', 'R', 'D'];
        this.userGear = this.userGears[0];
    }
    shift(gear) {
        if(this.userGears.indexof(gear) < 0) {
            throw new Error(`Ivalid gear: ${gear}`);
         this.userGear = gear;
        }
    }
}

const car1 = new Car('Tesla', 'Model S');
const car2 = new Car('Porche', 'panamera');
car1.shift('D');
car2.shift('R');
```

## 클래스는 함수다
```javascript
function Car(make, model) {
    this.make = make;
    this.model = model;
    this._userGears = ['P', 'N', 'R', 'D'];
    this._userGear = this.userGears[0];
}
// 밑줄이 붙은 프로퍼티에 접근하려고하네? 접근제한 방편!

// class Es6Car{}            // type of Es6Car
// function Es5Car {}       // function
```

## 프로토타입
- 클래스의 인스턴스에서 사용할 수 잇는 메서드라고 하면 그건 프로토타입 메서드를 말한다.
- 모든 함수에는 prototype 이라는 특별한 프로퍼티가 있다. 일반적인 함수에서는 프로토타입을 사용할 일이 없지만, 객체 생성자로 동작하는 함수에서는 프로토타입이 대단히 중요!
  - 객체 생성자, 즉 클래스는 항상 첫글자를 대문자로 표기!

- 함수의 prototype 프로퍼티가 중요해지는 시점은 new 키워드로 새 인스턴스를 만들었을 때이다.
- new 키워드로 만든 새 객체는 생성자의 prototype 프로퍼티에 접근할 수 있다.
- 객체 인스턴스는 생성자의 prototype 프로퍼티를 __proto__ 프로퍼티에 저장한다.
  - __proto__
    - 자바스크립트의 내부 동작 방식에 영향을 미친다. 
    - 충분히 이해하기 전까진 손대지 말것..

- 프로토타입에서 중요한 것은 독적 디스패치라는 메커니즘이다. 여기서 디스패치는 메서드 호출과 같은 의미이다.
- 객체의 프로퍼티나 메서드에 접근하려 할 때 그런 프로퍼티나 메서드가 존재하지 않으면 자바스크립트는 객체의 프로토타입에서 해당 프로퍼티나 메서드를 찾는다.
- 클래스의 인스턴스는 모두 같은 프로토타입을 공유하므로 프로토타입에 프로퍼티나 메서드가 있다면 해당 클래스의 인스턴스는 모두 그 프로퍼티나 메서드에 접근할 수 있다.

- 자바스크립트는 먼저 인스턴스를 체크하고, 거기에 없으면 프로토타입을 체크한다.

### 프로토타입 체인
- prototype 객체는 기본적인 속성으로 constructor와 __proto__를 가지고 있다.
- 프로토타입 체인은 __proto__ 의 특징을 이용하여, 상위 객체의 프로퍼티나 메서드를 차례로 검색하는것.
- 즉, 특정 객체의 프로퍼티나 메서드 접근시 자신의 것 뿐아니라 상위 객체의 것도 접근해서 사용가능

- 모든 프로토타입 체이닝의 종점은 Object.prototype (Object는 가장 상위 객체)

```javascript
class Human {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    sleep() {
        console.log(`${this.name} 잔다`)
    }
    eat(food) {
        console.log(`${this.name}이 ${food} 먹어`)
    }
}

// new 키워드로 생성자 함수를 불러 인스턴스 생성
let jun = new Human('jun', 30);
jun; // {name : 'jun', age: 30}
jun.sleep(); // jun 자고있어.
jun.eat(apple); // jun이 apple 먹어
```
- name,age 프로퍼티를 갖는 객체인데 어떻게 sleep, eat 메서드를 쓸 수 있을까
  - __proto__ 에 상위객체인 Human의 링크를 담고 있어 상위 메서드를 불러다 사용하기 떄문이다.

- Human 클래스와 프로토타입과의 관계
  - 모든 function에는 프로토타입 속성이 있다.
    - Human.prototype에 sleep() 메서드가 있는거임
  - 인스턴스를 생성하는 과정을 instantiation
    - new 키워드로 인스턴스 생

## 정적 메서드
- 이 메서드는 특정 인스턴스에 적용되지 않는다.
- 정적 메서드에서 this 인스턴스가 아니라 클래스 자체에 묶인다.
- 하지만 일반적으로 정적 메서드에는 this 대신 클래스 이름을 사용하는 것이 좋은 습관!!


## 상속
- 클래스의 인스턴스는 클래스의 기능을 모두 상속한다.
- 객체의 프로토타입에서 메서드를 찾지 못하면 자바스크립트는 프로토타입의 프로토타입을 검색한다.
- 자바스크립트는 조건에 맞는 프로토타입을 찾을 때까지 프로토타입 체인을 계속 거슬러 올라간다.
- 그러다 결국 못찾으면 그때서야 에러를 일으킨다.
- 클래스의 계층 구조를 만들 때 프로토타입 체인을 염두에 두면 효율적인 구조를 만들 수 있다.
- 즉, 프로토타입 체인에서 가장 적절한 위치에 메서드를 정의!!

```javascript
class Vehicle {
    constructor() {
        this.passengers = [];
        console.log("created");
    }
    addPassenger(p) {
        this.passengers.push(p);
    }
}

class Car extends Vehicle {
    constructor() {
        super();
        console.log('car created');
    }
    deployAirbags() {
        console.log('Bwoosh');
    }
}
```

- extends 키워드는 Car를 Vehicle의 서브클래스로 만든다.
- super() 는 슈퍼클래스의 생성자를 호출하는 특별한 함수이다.
  - 서브클래스에서는 이 함수를 반드시!!!!!! 호출 해야한다.호출 안하면 에러가 난다.
- 상속은 단방향이다. Car클래스의 인스턴스는 Vehicle 클래스의 모든 메서드에 접근할 수 있지만, 반대는 불가능


## 다형성
- 객체지향 언어에서 여러 슈퍼클래스의 멤버인 인스턴스를 가리키는 말이다.
```javascript
class Moto extends Veicle {}

const c = new Car();
const m = new Moto();
// c instance of Car; // ture
// c instanceof Vehicle; // ture
// m instanceof Car; // false
// m instanceof Moto; // true
// m instanceof Vehicle; // ture
```

- 자바스크립트에는 객체가 클래스의 인스턴스인지 확인하는 instanceof 연선자가 있다. 이 연산자를 속일 수도 있지만 prototype 과 __proto__ 프로퍼티에 손대지 않았다면 정확한 결과를 기대!

- 자바스크립트의 모든 객체는 루트 클래스인 Object의 인스턴스이다.
- 즉 객체 o에서 o instanceof Object는 항상 true이다. 모든 객체가 Object의 인스턴스인 것은 toString 같은 중요한 메서드를 상속하기 위해서이다.


