# 날짜와 시
## 날짜, 타임존,타임스탬프,유닉스 시간
- 타임존은 모두 UTC(Coordinated Universal Time)을 기준으로 한 시차로 나뉜다.
- UTC는 GMT(Greenwich Mean Time) 이라고도 불린다.
- new Date(); -> Fri Sep 30 2022 09:00:00 GMT+9099 (KST)

## Date 객체 만들기
- Date 객체는 항상 내부적으로 UTC 기준으로 저장하고, 출력할 때 운영체제에서 정의한 표준시에 맞게 변환한다.

## 날짜 데이터 만들기
### 서버에서 날짜 생성하기
- 서버에서 날짜를 생성할 때는 항상 UTC를 사용하거나 타임존을 명시하는게 좋다.
```javascript
const date = new Date(Date.UTC(2022, 9, 30)); // Sep 30, 2022 UTC

// Date.UTC는 Date의 매개변수를 똑같이 받지만 새로운 Date인스턴스를 반환하지 않고 해당 날짜의 숫자형 값을 반환한다.
```

### 브라우저에서 날짜 생성하기
- 운영체제를 통해 타임존 정보를 알 수 있고, 사용자는 일반적으로 그 지약의 시간을 선호한다.

## 날짜 데이터 전송하기
- 자바스크립트에서 날짜를 전송하는 가장 확실한 방법은 JSON을 사용하는 것이다.
```javascript
const before = { d: new Date() };
before.d instanceof Date // true
const json = JSON.stringify(before);
const after = JSON.parse(json);
```
- 일단 JSON으로 인코드된 날짜는 UTC이다.

## 요약
- 자바스크립트의 날짜는 1970년 1월 1일 UTC로부터 몇 밀리초가 지났는지 나타내는 숫자
- 날짜를 생성할 때는 타임존에 유의할것
- 날짜 형식을 자유롭게 바꿀 수 있어야한다면 Moment.js 사용해보자