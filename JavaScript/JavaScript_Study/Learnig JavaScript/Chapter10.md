# 맵과 셋
- 맵은 키와 값을 연결한다는 점에서 객체와 비슷
- 셋은 중복을 허용하지 않는다는 점만 제외하면 배열과 비슷

## 맵
- ES6이전 키와 값 연결하려면 객체 사용의 단점
- 프로토타입 체인 때문에 의도하지 않은 연결이 생김
  - 객체 안에 연결된 키와 값이 몇 개나 되는지 쉽게 알아낼 수 없음
  - 키는 반드시 문자열이나 심볼이어야하므로 객체를 키로써서 값과 연결 불가능
  - 객체는 프로퍼티 순서를 전혀 보장하지 않는다.
- 맵에 존재하지 않는 키에 get을 오출하면 undefined 반환
- 맵에 키가 존재하는지 확인하는 has() 메서드 존재
- 맵에 이미 존재하는 키에 set()을 호출하면 값이 교체된다.
- size 프로퍼티는 맵의 요소 숫자를 반환
- keys() 메서드는 맵의 키 반환
- values() 메서드는 값 반환
- entries() 메서드는 첫 번째 요소가 키이고 두 번째 요소가 값인 배열을 각각 반환
- 이들 메서드가 반환하는건 모두 이터러블 객체이기때문에 for...of 루프 사용가능

```javascript
for(let u of userRoles.keys())
    console.log(u.name);

for(let r of userRoles.values())
    console.log(r);

// 맵 분해
for(let [u,r] of userRoles.entries())
    console.log(`${u.name}: ${ur[1]}`)

//entries() 메서드는 맵으 ㅣ기본 이터레이터
for(let [u, r] of userRoles)
    console.log(`${u.name}: ${r}`)
```
- 맵의 요소를 지울 때는 delete() 메서드 사용
- 맵의 요소를 모두 지울 때는 clear() 메서드 사

## 위크 맵
- 맵과의 차이
  - 키는 반드시 객체여야 한다.
  - WaekMap의 키는 가비지 콜렉션에 포함될 수 있다.
  - WaekMap은 이터러블이 아니며 clear() 메서드도 없다.
- WeakMap은 객체 인스턴스의 전용키(private)를 저장하기에 알맞다
```javascript
const SecretHolder =  (function() { // secetholder 인스턴스에 저장한 내용은 가비지 콜렉션에 포함되지 않는다.
    const secret = new WeakMap();
    return class {
        // 비밀 저장
        setSecret(secret) {
            secrets.set(this, secret);
        }
        // 비밀 보려
        getSecret() {
            return secrets.get(this);
        }
    }
})
```

## 셋
- 중복을 허용하지 않는 데이터 집합
- 추가할 때는 add() 메서드
- Map과 마찬가지로 size 프로퍼티 존재
- 장점
  - 추가하려는 것이 셋에 이미 있는지 확인할 필요가 없다. 이미 있다면 아무일도 일어나지 않는다.
- 제거할 때는 delete() 호출
  - 제거에 성공했다면 즉, 셋에 존재 했다면 true 반환, 그렇지 않으면 false 반환

## 위크셋
- 객체만 포함할 수 있다. 
- 이 객체들은 가비지 콜렉션의 대상이 된다.
- 이터러블이 아니다.

## 요약
- 객체를 만드려할 때마다 멈추고, 이 객체를 맵 대신 쓰려하는건지 잘 생각해보자

