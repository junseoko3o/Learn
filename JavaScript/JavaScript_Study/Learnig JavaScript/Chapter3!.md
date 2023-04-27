## 데이터
- 데이터 타입
  - 우리에게 익숙한 형태인 숫자와 텍스트, 날짜 등

## 변수
- variable 
- 이름이 붙은 값으로, 언제든 바뀔수 있다.
- JavaScript
  - var
    - 예전에는 var로만 가능했었다. 
    - 중복으로 계속 선언하고 값을 넣어도 에러가 나지 않는다.즉, 재선언,재할당이 전부 가능하다.
    - 유연한 변수 선언이 가능은 하지만 중복 선언의 위험이 더 크다.
    - 함수 레벨 스코프
  - let
    - 재선언 안되지만 재할당은 가능하다.
    - 블록 레벨 스코프 (중괄호)
  - const
    - 재선언, 재할당이 불가능하다.
    - 블록 레벨 스코프 (중괄호)

## 변수와 상수 중 어떤것을 써야할까?
- 될 수 있으면 변수보다는 상수를 쓰는것이 좋다. 데이터의 값이 아무때나 바뀌는 것보다는, 고정된 값이 이해하기 쉽다.
- 상수를 사용하면 값을 바꾸지 말아야 할 데이터에서 실수로 값을 바꾸는 일이 줄어든다.
- 가능한 상수를 쓰되, 상황에 따라서 적절하게 변수로 사용하자!

## 식별자 이름
- 변수와 상수,함수 이름을 식별자(identifier)라고 한다. 식별자에게는 몇가지 규칙이 있다.
  - 반드시 글자나 $, _ 로 시작해야 한다.
  - 글자와 숫자,달러기호,밑줄만 쓸수 있다.
  - 유니코드 문자도 사용이 가능하다.
  - 예약어는 식별자로 쓸 수 없다.
- 대표적으로 카멜케이스(camelCase)와 스네이크 케이스(snake_case)가 존재한다.
- 표기법은 무엇을 써도 좋지만 일관성은 꼭 지켜주자.

## 리터럴
- literal
- 값을 프로그램 안에서 직접 지정한다는 의미이다.
- 리터럴과 식별자의 차이
  - ex) room1 변수에 값 conference_room_a 를 할당한 것을 생각해보자.
  - room1은 변수를 가리키는 식별자이다. 그리고 conference_room_a 는 문자열 리터럴인 동시에 room1의 값이다.
  - 자바스크립트는 따옴표를 통해 리터럴과 식별자를 구별한다. 식별자는 숫자로 시작할 수 없으므로 숫자에는 따옴표가 필요 없다.
  
```javascript
let room1 = "conference_room_a" // 따옴표 안은 리터럴이다.

let currentRoom = room1 // currentRoom의 값은 room1의 값 ("conference_room_a")과 같다.

currentRoom = conference_room_a; // error conference_room_a란 식별자는 존재하지 않는다.

// 식별자를 써야하는 곳, 다시 말해 값이 필요한 곳에는 어디든지 리터럴을 쓸 수 있다.
```

## 원시 타입과 객체
- 자바스크립트의 값은 원시 값(primitive) 또는 객체(object) 이다.
- 문자열과 숫자 같은 원시 타입은 불변(immutable)이다.
- 원시타입의 종류
  - 숫자
  - 문자열
  - 불리언
  - null
  - undefined
  - Symbol
- 객체의 종류
  - Array
  - Date
  - RegExp
  - Map과 WeakMap
  - Set과 WeakSet
  - 마지막으로 원시 타입 중 숫자와 문자열, 불리언에는 각각 대응하는 객체 타입인 Number,String,Boolean이 있다. (얘네는 대응하는 원시 값에 기능을 제공하는 역할을 한다.)

## 숫자
- 자바스크립트는 실제 숫자의 근사치를 저장할 때 IEEE-764배정도 부동소수점 숫자 형식을 사용한다.
- 이 형식을 더블 이라고 한다.
- 자바스크립트는 10진수, 2진수, 8진수, 16진수 네 가지 숫자형 리터럴을 인식한다.
- 어떠한 리터럴 형식을 사용하더라도 결국 숫자는 더블 형식으로 저장된다.

## 문자열
- String은 텍스트 데이터이다. 
- 자바스크립트 문자열은 Unicode 텍스트이다.
- 유니코드는 텍스트 데이터에 관한 표준이며, 사람이 사용하는 언어 대부분의 글자와 심볼에 해당하는 코드 포인트를 포함하고 있다.
- 자바스크립트 문자열 리터럴
  - '' , " ", `` 을 사용한다. 

## 이스케이프
- 텍스트로 만들어진 프로그램에서 텍스트 데이터를 사용할 때는 항상 텍스트 데이터와 프로그램 자체를 구별할 방법이 필요하다. 이때 문자열을 따옴표 안에 쓰는 방법이 있다.
- \ 역슬래시를 써서 따옴표를 이스케이프 하면 문자열이 끝나지 않았다고 자바스크립트에게 알릴 수 있다.
```javascript
const a = "He looked up and said \"don't do that!\" to Max.";
const b = 'He looked up and said "don\'t do that!" to Max.';
```

- \ 는 자기 자신을 이스케이프할 수 있다.
```javascript
const c = "In JavaScript, use \\ as an escape character in strings.";
```
- 큰 따옴표를 쓸지 작은 따옴표를 쓸지는 스스로 정하면 된다. 
- 텍스트에는 아포스트로피 등의 이유로 큰 따옴표를 쓰는것을 추천!
- 자바스크립트 문자열 안에 HTML을 쓸 때는 반대로 작은 따옴표를 쓴다.
  - HTML 문자열을 작은 따옴표로 감싸면 속성값에 큰 따옴표를 쓸 수 있기 떄문이다.

## 특수문자
- \ 는 따옴표를 이스케이프할 때만 쓰지는 않는다. 줄바꿈 문자처럼 화면에 표시되지 않는 일부 특수문자나 임의의 유니코드 문자를 나타낼 때도 사용한다.
```shell
\n 줄바꿈문자 "Line1\nLine2"

\r 캐리지리턴 "Windows line 1\r\nWindows line 2"

\t 탭 "Speed:\t60kph"

\' 작음따옴표 "Don\'t"

\" 큰따옴표 'Sam said \"hello\".'

\` 빽틱 `New in ES6: \` strings.`

\$ 달러 `New in ES6: ${interpolation}`

\\ 역슬래시 "Use \\\\ to represent \\!"
```

## 템플릿 문자열
- 값을 문자열 안에 써야하는 일은 비일비재하다. 이때 문자열 병합을 통해 변수나 상수를 문자열 안에 쓸 수 있다.
```javascript
let currentTemp = 19.5;

const message = "The current temperature is " + currentTemp + "\u00b0C";
```

- 문자열의 정해진 위치에 값을 채워 넣는 방법.
- 문자열 템플릿에는 큰따옴표나 작은 따옴표를 쓰지 않고 백틱을 사용한다.
````javascript
let currentTemp = 19.5;

const message = `The current temperature is ${currentTemp}\u00b0C`;
````

## 불리언
- true 와 false 두 가지 값 밖에 없는 데이터 타입.

## 심볼
- 유일한 토큰을 나타내기 위한 데이터 타입.
- 항상 유일하다. 다른 어떤 심볼과도 일치하지 않는다. 
- 자바스크립트의 심볼을 만들 때 new 키워드를 사용할 수 없으며, 대문자로 시작하는 식별자는 new와 함께 쓴다는 불문율의 예외임을 기억!
```javascript
const RED = Symbol("The color of a sunset!");
const ORANGE = Symbol("The color of a sunset!");
RED === ORANGE // false -> 심볼은 모두 서로 다르다.
```

## null & undefined
- null 
  - 프로그래머에게 허용된 데이터 타입
- undefined
  - 자바스크립트 자체에서 사용
  - 아직 값이 ㅈ어지지 않은 변수의 동작을 고의로 흉내낼때 뿐
  - 변수를 선언하기만하고 명시적으로 값을 할당하지 않으면 그 변수에는 기본적으로 undefined가 할당된다.
```javascript
let currentTemp; // 암시적으로 undefined
const targetTemp = null; // 아직 모르는 값
currentTemp = 19.5; // 이제 값이 있음
currentTemp = undefined; // currentTemp에는 초기화되지 않은듯 권상하지 않음
```

## 객체
- 객체의 콘텐츠는 property or member라고 부른다. property는 이름(키와 값으로 구성된다)
- property는 반드시 문자열 또는 심볼이어야 하며, 값은 어떤 타입이든 상관 없고 다른 객체여도 상관 없다.
```javascript
const sam1 = {
    name: 'Sam',
    age: 4,
};

const sam2 = {name: 'Sam', age:4} 

const sam3 = {
    name: 'Sam',
    classification: { // property의 값도 객체가 될 수 있다.
        kingdom: 'Anamalia',
        phylum: 'Chordata',
        class: 'Mamalia'
    }
}
```
- sam1 과 sam2의 propert는 같지만 서로 다른 객체이다. sam3의 classfication property는 그 자체가 객체이다.
- 접근
  - sam3.classification.kingdom;
- 객체에는 함수를 담을 수도 있다.
```javascript
sam3.speak = function() {
    return "Meow!";
}

sam3.speak(); // "Meow!"
```
- delete 연산자
```javascript
delete sam3.classification; // classification 트리 전체가 삭제
delete sam3.speak; // speak 함수 삭제
```

## 배열
- 배열 크기는 고정되지 않는다. 언제든 요소를 추가하거나 제거할 수 있다.
- 요소의 데이터 타입을 가리지 않는다. 즉, 문자열만 쓸 수 있는 배열이라던가 숫자만 쓸 수 있는 배열 같은 개념이 아예 없다.
- 배열 요소는 0으로 시작
```javascript
const a1 = [1, 2, 3, 4]; // 숫자로 구정된 배열
const a2 = [1, 'two', 3, null] // 여러 타입 구성 배열
const a3 = [ // 여러줄로 정의한 배열
    "abc",
    "def",
    "ghi",
]

const a4 = [ // 객체가 들어있는 배열
  { name: 'abc' , age: 4},
  { name: 'def', age: 14},
]

const a5 = [ // 배열이 들어있는 배열
    [1,3,5],
    [2,4,5],
]
```
- 배열에는 요소 숫자를 반환하는 length property가 있다.
```javascript
const arr = [ 1 , 2, 3];
arr.length; // 3
```
## 날짜
```javascript
const now = new Date();
now; // Fri Dec 16 2022 09:20:16 GMT +0900 (KST)
```

## 정규표현식
```javascript
// 이메일 정규식
const email = /\b[a-z0-9._-]+@[a-z_-]+(?:\.[a-z+]+\b/;
```

## 맵과 셋
- Map 
  - 객체와 마찬가지로 키와 값을 연결하지만, 특정 상황에서 객체보다 유리하다.
- Set
  - 배열과 비슷하지만 중복이 허용되지 않는다.

## 데이터 타입 변환
- 숫자로 바꾸기
```javascript
const numStr = "123";
const num = Number(numStr);

// 숫자로 바꿀 수 없는 문자열은 NaN이 반환된다.

const a = parseInt("16 volts", 10) // "volts"는 무시된다. 10진수 16
const b = parseInt("3a", 16); // 16진수 3a를 10진수로 바꾼다 결과 58
const c = parseFloat("15.5 kph") // "kph"는 무시된다. parseFloat는 항상 기수가 10이라고 가정한다.
```
- 
- 불리언 으로 변환
```javascript
const n = 0 // 거짓 같은 값
const b1 = !!n; // false
const b2 = Boolean(n) //false
```
- 문자열로 반환
```javascript
const n = 33;
n; // 33 숫자
const s = n.toString();
s; // "33" 문자열
```

## Summary
- 자바스크립트에는 문자열, 숫자, 불리언, null, undefined, Symbol 여섯 가지 원시타입과 객체 타입이 있다.
- 자바스크립트의 모든 숫자는 배정도 부동소수점 숫자(더블)이다.
- 배열은 특수한 객체이며, 객체와 마찬가지로 매우 강력하고 유연한 데이터 타입이다.
- 날짜, 맵, 셋, 정규표현식 등 자주 사용할 다른 데이터 타입들은 특수한 객체 타입이다.
