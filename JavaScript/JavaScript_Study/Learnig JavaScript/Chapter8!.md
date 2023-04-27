# 배열
- 배열은 객체와 달리 본길에서 순서가 있는 데이터 집합이며 0으로 시작하는 숫자형 인덱스를 사용
- 자바스크립트의 배열은 비균질적, 한 배열의 요소가 모두 같은 타입일 필요는 없다.
- 배열 리터럴은 대괄호로 만들고, 배열 요소에 인덱스로 접근할 때에도 대괄호
- 모든 배열에는 요소가 몇 개 있는지 나타내는 length 프로퍼티 존재
- 배열에 배열 길이 보다 큰 인덱스를 사용해 요소를 할당하면 자동으로 그 인덱스에 맞게 늘어나며, 빈자리는 undefined로 채워짐
- Array 생성자를 써서 배열을 만들 수도 있지만 경우가 별로 많지 않음

## 배열의 처음이나 끝에서 요소 하나 추가 or 제거
- push, pop
  - 각각 배열의 끝에 요소를 추가하거나 제거
- shift,unshift 
  - 각각 배열의 처음에 요소를 제거하거나 추가

- push 와 unshift는 새 요소를 추가해서 늘어난 길이를 반환
- pop 과 shift는 제거된 요소를 반환


## 배열 끝에 여러 요소 추가
- concat 메서드 

## 배열 일부 가져오기
- slice
  - 매개변수 두 개를 받음
  - 첫 번째 매개변수는 어디서부터 가져올지
  - 두 번째 매개변수는 어디까지 가져올지 지정 (바로 앞 인덱스까지임)
  - 두 번째 매개변수를 생략하면 배열의 마지막까지 반환
  - 음수 인덱스가 사용가능 하며, 음수 인덱스를 쓰면 배열의 끝에서 부터 요소를 센다.

```javascript
const arr = [1, 2, 3, 4, 5];

arr.slice(3); // [4, 5]
arr.slice(1, -2); // [2, 3]
```

## 임이의 위치에 요소 추가하거나 제거
- splice
  - 첫 번째 매개변수는 수정 시작할 인덱스
  - 두 번째 매개변수는 제거할 요소 숫자

```javascript
const arr = [1, 5, 7];

arr.splice(1, 0, 2, 3, 4); // [1, 2, 3, 4, 5, 7]
arr.splice(5, 0, 6); // [1, 2, 3, 4, 5, 6, 7]
arr.splice(1, 2); // [1, 4, 5, 6, 7]
arr.splice(2, 1, 'a', 'b'); // [1, 4, 'a', 'b', 6, 7]
```

## 배열 안에서 요소 교체하기
- copyWithin
  - 첫 번째 매개변수는 복사한 요소를 붙여넣을 위치
  - 두 번째 매개변수는 복사를 시작할 위치
  - 세 번째 매개변수는 복사를 끝낼 위치 (생략 가능)

```javascript
const arr = [1, 2, 3, 4];
arr.copyWithin(1, 2); // [1, 3, 4, 4]
arr.copyWithin(2, 0, 2); // [1, 3, 1, 3]
arr.copyWithin(0, -3, -1); // [3, 1, 1, 3]
```

## 특정 값으로 배열 채우기
- fill
```javascript
const arr = new Array(5).fill(1); // [1, 1, 1, 1, 1] 로 초기화

arr.fill('a'); // ['a', 'a', 'a', 'a', 'a']
arr.fill('b',1); // ['a', 'b', 'b', 'b', 'b']
arr.fill('c', 2, 4); // ['a', 'b', 'c', 'c', 'b']
```


## 배열 정렬과 역순 정렬
- reverse
```javascript
const arr = [1, 2, 3, 4, 5];
arr.reverse(); // [5, 4, 3, 2, 1]

const arr1 = [5, 3, 2, 4, 1];
arr.sort(); // 순서 정렬
```

## 배열 검색
- indexOf
  - 찾고자 하는 것과 정확히 === 하는 첫 번째 요소의 인덱스 반환
- lastIndexOf
  - 배열의 끝에서 부터 검색한다.
- 둘 다 일치하는 것을 찾지 못하면 -1을 반환한다.
```javascript
const o = {
    name: 'jerry'
}
const arr = [1, 5, 'a', o, true, 5, [1,2], '9'];
arr.indexOf(5); // 1
arr.lastIndexOf(5); // 5
arr.indexOf('a'); // 2
arr.indexOf({name: 'jerry'}); // -1
```

- findIndex
  - 일치 하는 것을 못찾을때 -1 을 반환하는건 indexOf와 비슷하지만, 보조 함수를 써서 검색 조건을 지정할 수 있어 더 다양한 상황에서 사용가능
  - 검색을 시작할 인덱스를 지정할 수 없고, 뒤에서 부터 찾는 짝도 없다.

```javascript
const arr = [{ id: 5, name: 'jun'}, { id: 7, name: 'hye'}];

arr.findIndex(o => o.id ===5); // 0
arr.findIndex(o => o.id === 17); // -1
```

- every
  - 배열의 모든 요소가 조건에 맞아야 ture를 반환하며 그렇지 않다면 flase를 반환한다.


## map, filter
- map
  - 배열 요소를 변형한다. 
  - 일정한 형식의 배열을 다른 형식으로 바꿔야 한다?

```javascript
const cart = [
    {
        name: 'jun',
        price: 9
    },
    {
        name: 'jye',
        price: 10
    }
]
const names = cart.map(x => x.name); // jun , jye
const prices = cart.map(x => x.price); // [9,10]
const carts = names.map( (x, i) => ({
    name: x,
    price: prices[i]
}))
```

- filter
  - 필요한 것들만 남길 목적

```javascript
const words = ['spray', 'limit', 'elite', 'exuberant', 'destruction', 'present'];
const result = words.filter(word => word.length > 6);
console.log(result);
// expected output: Array ["exuberant", "destruction", "present"]
```


## reduce
- 배열 자체를 변형한다.
```javascript
const arr = [5, 7, 2, 4];
const sum = arr.reduce( (a, x) => a += x, 0);
```

- 첫 번째 배열 요소 5에서 익명함수 호출한다. a의 초기값은 0이고 x의 값은 5이다. 함수는 a와 x(5)의 합을 반환한다. 이 값은 다음 단계에서 a의 값이 된다.
- 두 번째 배열 요소 7에서 함수를 호출한다. a의 초기값은 이전 단계에서 전달한 5이고, x의 값은 7이다. 함수는 a와 x의 합 12를 반환한다. 이 값은 다음 단계에서 a의 값이 된다.
- 세 번째 배열 요소 2에서 함수를 호출한다. 이 단계에서 a 는 12이고 x는 2이다. 함수는 a와 x의 합인 14를 반환
- 네 번째이자 마지막 배열 요소인 4에서 함수 호출.a 는 14이고, x는 4이다 함수는 a 와 x의 합인 18을 반환하며 이 값은 reduce의 값기고, sum에 할당 된다.