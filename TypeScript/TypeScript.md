- Nest, Next는 타입스크립트를 기본 언어로 채택하고 있다. 자바스크립트로 물론 바꿀 수 있지만 타입스크립트의 장점을 누리기 위해 기본 설정으로 사용하길 추천!
- 마이크로소프트에서 개발한 언어이다. 자바스크립트 코드에 타입 시스템을 도입하여 런타임에 에러가 발생할 가능성이 있는 코드를 정적 분석으로 찾아준다. 타입스크립트는 자바스크립트에 구문을 추가하여 만들어 졌다. tsc 명령으로 컴파이랗여 자바스크립트 코드로 변환이 가능하다. 컴파일 후 생성된 자바스크립트는 타입이 없다. 자바스크립트에 원래 타입이 없기 때문인데, 타입스크립트가 제공하는 타입 추론은 타입오류로 인해 런타임에 발생하는 오류를 컴파일 타임에 잡아준다.

```jsx
const user = { 
	firstName: 'Dexter',
	lastName: 'Hello',
	role: 'Developer',
}

console.log(user.name);
// any Property 'name' does not exist on type ~
```

## 변수 선언

[선언키워드] [변수명] : [타입]

- 선언키워드
    - let, var, const로 선언한다.
    - const는 선언후 재할당이 불가능하며 let과 var는 재할당이 가능하여 값을 바꿀 수 있다. let 과 var의 차이는 호이스팅 여부인데 var는 변수를 사용한 후에 선언이 가능하지만 let은 그렇지 못행

```tsx
varA = 1;
var VarA: number;

	let letB: string
	letB = 'let';  // block-scoped variable letB used before its declaration

let letB: string;
```

## 지원하는 타입

- 타입스크립트는 자바스크립트가 가지고 있는 자료형을 모두 포함한다. 자바스크립트의 타입은 기본타임(Primitive value)과 객체형(Object), 함수형(Function)이 있다.
- typeof 키워드를 이용하여 인스턴스의 타입을 알 수 있다.
    - typeof instance === “undefined”

### 기본 타입

- boolean, null, undefined, number, bigint, string, symbol

### 객체 타입

- 속성(Property)을 가지고 있는 데이터 컬렉션이다. 속성은 키와 값으로 표현되는데 값은 다시 자바스크립트의 타입을 가지고 있다.

```tsx
const abc = {
	name: 'hihi',
	age: 21,
	hobby: ['movie', 'billiards'],
}
```

- Date, Array, Map, WeakMap,Set,WeakSet, JSON

### 함수 타입

- 자바스크립트는 함수를 변수에 할당하거나 다른 함수의 인자로 전달할 수 있다. 함수의 결과로 반환할 수도 있다. 언어의 이러한 특징을 일급함수라고 한다.
    - typeof func === “function”

### any / unknown / never

- any
    - 자바스크립트와 같이 어떠한 타입의 값도 받을 수 있는 타입
    - 어떤 타입의 변수에도 할당이 가능하다. 이 특성으로 인해 런타임에 오류를 일으킬 가능성이 있다.
- unknown
    - any 타입과 마찬가지로 어떤 타입도 할당 가능하지만 다른 변수에 할당 또는 사용할 때 타입을 강제하도록 하여 any가 일으키는 오류를 줄여 준다.
- never
    - 어떤 값도 할당할 수 없다. 함수의 리턴 타입으로 지정하면 함수가 어떤 값도 반환하지 않는다는 것을 뜻하고, 다음과 같이 특정 타입의 값을 할당 받지 못하도록 하는데 사용할 수도 있다.
        - typeof NonString<T> = T extends string ? never : T;

## 타입 정의하기

- 기본 타입과 같은 타입을 정의한다는 뜻은 아니고, 위에서 설명한 타입들을 조합하여 타입에 이름을 붙여 사용한다.

```tsx
const user = {
	name: 'hihi',
	age: 21,
}

// 추론된 타입
const user: {
  name: string;
  age: number;
}
```

- 변수에 객체를 바로 할당하지 않고 interface로 정의할 수 있다.

```tsx
interface User {
    name: string;
    age: number;
}

const user: User = {
    name: 'Dexter',
    age: 21,
}
```

- interface는 class로 선언할 수도 있다.

```tsx

class User {
  constructor(name: string, age: number) { }
}

const user: User = new User('Dexter', 21);
```

- 생성자에 선언된 변수는 클래스 멤버변수가 된다. 접근제한자 (public,private)가 없으면 public 변수가 된다. 멤버변수를 사용할 때는 this.name과 같이 this 키워드와 함께 사용

- 타입은 type키워드로 새로운 타입을 만들 수 있다.

```tsx
type MyUser = User;

// MyUser 타입은 기존 User타입을 그대로 사용하지만 내가 사용하는 도메인에 맞는 이름으로바꾼것
```

## 타입 구성하기

- 자바스크립트는 변수에 어떠한 타입의 값도 할당할 수 있다. 일명 덕 타이핑 이라고 한다. 타입스크립트도 여러 타입의 값을 할당할 수 있다. 여러 타입을 조합한 새로운 타입을 가지는 것이다.

- Union 타입
    - 여러 타입을 조합한 타입.
    - getLength 함수의 인자인 obj는 string 또는 string 배열 타입을 가질 수 있다.

```tsx
function getLength(obj: string | string[]) {
	return obj.length;
}

// 유니언 타입을 활용하면 변수가 가질 수 있는 값을 제한할 수도 있다.
type Status = "Ready" | "Waiting";
```

- 타입스크립트는 열거형을 제공한다.

```tsx
enum Status {
	READY = "Ready",
	WAITING = "Waiting",
}
```

## Generic 타입

- 어떠한 타입이든 정의될 수 있지만 호출 되는 시점에 타입이 결정된다.
- 만약 다음과 같이 인자를 그대로 리턴하는 함수가 있다 가정

```tsx
function identitiy(arg: any): any {
	return arg;
}
```

- 이 함수의 반환값은 any로 되어 있기 때문에 arg에 ‘test’ 를 인자로 전달할 경우 전달한 인자의 string 타입이 반환할 때 any가 되어 버린다. 반면 다음과 같이 제네릭 타입을 사용하게 되면 리턴되는 값의 타입은 함수를 호출하는 시점의 인자로 넣은 타입으로 결정되게 할 수 있다.

```tsx
function identitiy<T>(arg: T): T {
	return arg;
}
```

- 제네릭을 선언할 때는 보통 대문자 한글자 사용한다.
- 타입스크립트는 타입을 잘 다룰수록 그 진가를 발휘하는 언어이다.

## 접근 제한자
- public
    - 설정된 멤버(멤버변수, 멤버메서드) 는 상속 및 외부 객체에서의 접근 가능
- protected
    - 설정된 멤버는 자식클래스에서 접근 가능 외부객체는 불가능
- private
    - 현재 내부 클래스에서만 접근 가능