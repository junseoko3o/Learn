## 클래스
- 객체지향 프로그래밍(OOP)에서 가장 기본이 되는 Class는 필드를 선언할 수 있고, 생성자를 가져야하며, 메서드를 선언할 수 있다.
- 정의 
  - 객체를 정의 해놓은 것
- 용도
  - 객체를 생성하는데 사용된다.
- 클래스와 객체의 관계는 제품 설계도와 제품과의 관계라할 수 있다.

```java
ublic class Bicycle {

  // Bicycle 클래스는 3개의 필드를 가지고 있습니다.
  // 클래스에 선언된 필드와 함수들을 통틀어 멤버라고 합니다.
  // 아래의 필드는 멤버 변수라고도 부르고, 속성(property)이라고도 합니다,
  // 일반적으로 객체지향 프로그래밍을 할 때는 private 접근제어자로 속성을 감춥니다.
  public int cadence;
  public int gear;
  public int speed;

  // 다음은 생성자라고 불리는 문법입니다.
  // 생성자는 특수한 형태로, 인스턴스를 초기화 할 때 사용하는 문법입니다.
  // 생성자가 만약 존재하지 않는다면 기본 생성자(매개변수를 받지 않는)가 생성됩니다.
  // 생성자는 클래스와 이름이 같아야 합니다.
  // this 키워드는 생성되는 인스턴스를 가리킵니다. (혼란을 방지하기 위해 사용합니다.)
  public Bicycle(int startCadence, int startSpeed, int startGear) {
    this.cadence = startCadence;
    this.speed = startSpeed;
    this.gear = startGear;
  }

  // Bicycle 클래스는 4개의 메서드를 가집니다.
  public void setCadence(int newValue) {
    this.cadence = newValue;
  }

  public void setGear(int newValue) {
    this.gear = newValue;
  }

  public void applyBrake(int decrement) {
    this.speed -= decrement;
  }

  public void speedUp(int increment) {
    this.speed += increment;
  }
}
```
- 마지막 메서드 두 개는 객체지향적이라고 볼 수 있다. 외부에서 setter로 속도를 조절하는 것이 아니라, 객체가 직접 자신의 속성을 의미있게 변경하도록 했기 때문

---

- 클래스의 선언에는 필드,생성자,메서드 정의가 포함될 수 있다. 
- 필드
  - 인스턴스 필드에 한하여, 각 인스턴스의 속성을 나타낸다. 클래스 필드의 경우에는 클래스 레벨에서의 속성을 나타낸다.
- 생성자
  - 새로운 객체를 생성하는 용도
- 메서드
  - 클래스와 그 객체의 행동을 구현하는 용도
- 변수 
  - 하나의 데이터를 저장할 수 있는 공간
- 배열 
  - 같은 종류의 여러데이터를 하나의 집합으로 저장할 수 있는 공간
- 구조체
  - 서로 관련된 여러 데이터를 종류에 관계없이 하나의 집합으로 저장할 수 있는 공간
- 클래스 선언에 포함될 수 있는 요소
  - public,private 등의 제어자들
  - 첫 글자가 대문자인 클래스명
  - 상위 클래스가 있는 경우 extends 키워드 다음에 상위클래스의 이름을 붙인다. 클래스는 단 하나의 상위클래스만 상속할 수 있다. 자바는 다중상속을 지원하지 않는다.
  - implements 키워드 뒤에 인터페이스들의 목록이 올 수 있다. 클래스는 여러 인터페이스를 동시에 구현할 수 있다.
  - 중괄호로 클래스 본문을 선언한다.

### 클래스를 정의하는법
```java
class 클래스이름 {
    
}
```
```java
class 클래스이름 extends SCLASS implements INTERFACE {
    
}
```

- 클래스 정의할 때 가지는 속성
  - 접근제어자
  - 클래스이름
  - (없을수있음) sclass - 상위 클래스
  - (없을수있음) interface
  - 클래스의 바디 {} 안
    - 생성자
    - 멤버변수
    - 메서드

### 객체 만드는법 (new)
- 클래스의 객체가 만들어진 것을 인스턴스를 만들었다고 한다
  - 변수만 선언한 것은 인스턴스를 생성한 것이 아니다.
```java
public class Prac {
    public static void main(String[] args) throws  ClassNotFoundException {
        MadeClass mc;
    }
}
```
- 이러면 변수만 선언
- 인스턴스를 생성하기 위해서는 new 를 사용해야한다.
  - new 뒤에는 클래스의 생성자 메서드가 온다
```java
MadeClass mc = new MadeClass();
```

- new는 객체를 생성하고 객체 주소를 반환한다.
- 참조변수에는 이 객체 주소가 저장된다.
- 참조변수를 가지고 객체에 접근할 수 있다.
- 참조변수아 연결이 끊긴 객체는 gc가 정리한다.
- 생성한 객체를 변수에 반드시 저장할 필요는 없다. 속성 값을 바로 도출할 수 있다.
```java
int height = new Rectangle().height;
```

### 메서드 정의하는 방법
```java
public double calculateAnser (double wingSpan , int numberOfEngines,
        double length, double grossTons) {
    //do the calculation here
        }
```

- 구성요소
  - 접근제어자
  - return 타입
  - 메서드 이름
  - 파라미터 리스트 ()안
  - (예외던지면) 던질 예외 리스트
  - 메서드 바디 {} 안
  - 필수요소는 메서드의 리턴타입, 이름 ,{}, ()
- 메서드 오버로딩
  - 한 클래스 내에 동일한 명의 메서드가 있을 수 있다.
```java
public class DataArtist {
    public void draw (String s){
        
    }
    public void draw (int i) {
        
    }
    public void draw (double f) {
        
    }
    public void draw(int i , double f) {
        
    }
}
```

- 파라미터 리스트가 달라야 함

### 생성자 정의하는 법
- 생성자 
  - 인스턴스가 생성될 때마다 호출되는 인스턴스 초기화 메서드
    - 생성자 이름은 클래스의 이름과 같다
    - 생성자는 반환값이 없다
    - 생성자는 인스턴스를 초기화 할 때 필요한 작업들을 정리해 주는 것이고 인스턴스를 만드는 것은 new zldnjem
- 클래스 Bicycle 의 생성자
```java
public Bicycle (int startCadence, int startSpeed , int startGear) {
    gear = startGear;
    cadence = startCadence;
    speed - startSpeed;
        }
```
- 위의 생성사 사용 예시
```java
Bicycle myBike = new Bicycle(30,0,8);
```
- 클래스에 생성자를 작성하지 않을 수도 있다.
  - 컴파일러가 자동으로 생성. 인자가 없는 default 생성자 생성
  - 기본 생성자는 sclass의 인자가 없는 생성자를 호출
- 생성자를 private로 선언하고 팩토리 메서드를 둬서 객체를 생성

### this 키워드
- 현재 객체 내에서 메서드나 생성자에서 해당 객체를 호출하기 위해 사용
- static에서는 사용할 수 없다
- 필드 호출할 떄 사용
```java
public class Point {
    public int x = 0;
    public int y = 0;
    
    //constructor
  public Point(int x , int y) {
      this. x = x;
      this.y = y;
      
  }
}
```

- 같은 클래스 내에 다른 생성자를 호출할 경우
```java
public class Rectangle {
    private int x,y;
    private int width, height;
    
    public Rectangle() {
        this(0,0,1,1);
        
    }
    public Rectangle (int width, int height) {
        this(0,0,width,height);
    }
    
    public Rectangle(int x , int y , int width, int height){
        this.x = x;
        this.y = y;
        this.width = width;
        this.height = height;
    }
}
```