## 디자인 패턴
- 프로그램을 설계할 때 발생했던 문제점들을 객체 간의 상호 관계 등을 이용하여 해결할 수 있도록 하나의 규약 형태로 만들어 놓은 것.
  
### 싱글톤 패턴
- 하나의 클래스에 오직 하나의 인스턴스만 가지는 패턴
- 하나의 클래스를 기반으로 여러 개의 개별적인 인스턴스를 만들 수 있지만, 그렇게 하지 않고 하나의 클래스를 기반으로 단 하나의 인스턴스를 만들어 이를 기반으로 로직을 만드는데 쓰이며, 보통 데이터베이스 연결 모듈에 많이 사용.
- 하나의 인스턴스를 만들어 놓고 해당 인스턴스를 다른 모듈들이 공유하며 사용하기 때문에 인스턴스를 생성할 때 드는 비용이 줄어드는 장점. 하지만 의존성이 높어진다는 단점도 존재.

### 자바스크립트의 싱글톤 패턴
- JS에는 리터럴 {} 또는 new Object로 객체를 생성하게 되면 다른 어떤 객체와도 같지 않기 때문에 이 자체만으로 싱글톤 패턴을 구현할 수 있다.

```javascript
class Singleton {
  constuctor() {
    if (!Singleton.instance) {
      Singleton.instance = this;
    }
    return Singleton.instance;
  }
  getInstance() {
    return this.instance;
  }
}
const a = new Singleton();
const b = new Singleton();
console.log(a === b); // true
```
- Singleton.instance라는 하나의 인스턴스를 가지는 Singleton 클래스를 구현한 모습. 이를 통해 a와 b는 하나의 인스턴스를 가지게 된다.

### 데이터베이스 연결 모듈
```javascript
const URL = 'mongodb://localhost:27017/kundolapp';
const createConnection = url => ({
  "url": url,
});
class DB {
  constructor(url) {
    if (!DB.instance) {
      DB.instance = createConnection(url);
    }
    return DB.instance;
  }
  connect() {
    return this.instance;
  }
}
const a = new DB(URL);
const b = new DB(URL);
console.log(a === b); // true
```
  

### 자바에서의 싱글톤 패턴
- JAVA로 싱글톤 패턴을 구현하는 7가지 방법 참고
