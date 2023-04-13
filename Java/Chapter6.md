### 상속의 특징
- 객체지향(OOP)의  핵심적인 특징 중 하나
- 자바는 단일상속만을 지원한다.
- 단일 상속
  - 하위클래스가 상위클래스로부터 기능을 물려 받는것을 말하며, 가장 일반적인 상속 방법이다.
- 다중 상속
  - 하나의 하위클래스가 여러개의 상위클래스부터 기능을 물려 받는 

```java
class A {
    public void a(){
        
    }
}
class B extends A {
    @Override
    public void a() {
        
    }
    public void b() {
        
    }
}
```

- 특징
  - 상위클래스는 하위클래스에게 필드와 메서드를 물려준다.
  - 하위클래스의 생성자를 호출하는 경우 상위클래스의 생성자와 초기화 블록도 같이 호출된다.
  - 하나의 상위클래스가 여러개의 하위클래스에게 상속받는 것이 가능하다.
  - 상속을 받은 클래스가 상위클래스가 되어 하위클래에게 상속해주는 계층적 상속이 가능하다.
### super키워드
- 상위클래스를 참조할 때 쓰는 키워드
- this 키워드가 객체 자신을 나타내는 키워드였다면, super키워드는 반대로 부모를 나타내는 키워드라 생각하면 된다.
- 상위 클래스의 인스턴스 변수를 참조하는 경우
  - 클래스 A를 상속하고 있는 클래스 B의 a() 메서드를 호출하였을 때 첫번째 출력문은 객체 자신의 b를 참조하지만 2번째 출력문은 super 키워드를 통해 상위클래스인 A의 b 변수를 참조한다.
```java
class A {
    int b = 10;
    public void a() {
      System.out.println("b");
    }
}

class B extends A {
    int b = 50;
    public void a() {
      System.out.println("B a" + b); //b = 50
      System.out.println("B a" + super.b); // b = 10
      super.b();
    }
}
```

- 상위 클래스의 메서드를 호출하는 경우
  - 클래스 A를 상속하고 있는 클래스 B에서 클래스의 A의 a() 메서드를 호출하고 싶은 경우에 super 키워드를 이용해 호출
```java
class A {
    int b = 10;
    public void a() {
      System.out.println("a");
    }
}

class B extends A {
    int b = 50;
    public void a() {
        super.a(); //클래스 A의 a() 메서드 호출
    }
}
```

- 상위 클래스 생성자를 호출하는 경우
  - 클래스 A를 상속하고 있는 클래스 B의 인스턴스가 생성되면 자바에서 자동으로 컴파일 시에 super()메서드를 이용해 클래스 A의 생성자 또한 호출
  - 하지만, 클래스 A의 생성자가 파라미터가 있거나, 명시된 생성자라면 하위 클래스의 생성자에 super(파라미터)와 같은 형식으로 생성자를 반드시 호출해야함

```java
class A{
    int b = 10;
    
    //명시된 생성자
  public A(int b) {
      this.b = b;
  }
  public void a() {
    System.out.println("a");
  }
}

class B extends A {
    int b = 50;
    
    //파라미터를 가지는 생성자가 있는 경우 (상위 클래스)
  public B (int b ) {
      //반드시 명시
    super(b);
  }
  
  public void a() {
    System.out.println("B a" + b);
    System.out.println("B a" + super.b);
    super.a();
  }
}
```
### 메서드 오버라이딩
- 메서드 오버라이딩은 상위클래스를 상속하는 하위 클래스가 상위클래스의 메서드의 기능을 무시하고 새롭게 정의하는 것
- ex) Car 클래스와 Car 클래스를 상속하는 Avante 클래스 

```java
public class Car {
    private int speed = 10;
    private String name = "car";
    
    public int accel() {
        return this.speed + 10;
    }
    
    public void run() {
      System.out.println(name + " is running");
      System.out.println("speed : " + this.speed);
    }
}


public class Avante extends Car {
    private int speed = 50;
    private String name = "Avante";
    
    @Override
  public int accel() {
        return String name = "Avante";
    }
    
    @Override
  public int accel() {
        return this.speed + 50;
    }
    
    @Override
  public void run() {
        super.run();
      System.out.println("after Overriding speed :"+this.speed);
    }
    
    public void call() {
      System.out.println("test not call");
    }
}
```
- Car클래스를 상속하는 Avante 클래스의 run()메서드를 호출하면 super.run()메서드에 의해 상위클래스인 Car클래스의 run() 메서드가 먼저 호출되고, 이후 Avante 클래스의 run() 메서드가 호출됨을 확인
- 상위 클래스 타입으로 Avante 객체를 참조하는 경우와, 하위클래스타입 그대로 객체를 참조하는 경우를 확인해보면 상위 클래스 타입으로 참조하는 경우에는 하위클래스의 call() 메서드를 호출하지 못하지만, 하위 클래스 타입 그대로 참조하는 경우엔 call() 메서드를 호출 할 수 있다.

```java
Car car = new Car();
Car avnate = new Avante();
Avante avante1 = new Avante();

car.run(); //Car 클래스 run() 메서드 호출
santafe.run(); // Avante 클래스의 run() 메서드 호출

avante1.call(); //메서드 호출 가능
avante.call(); //메서드 호출 불가능
```
- 하위클래스에서 오버라이딩한 메서드에서 상위 클래스의 메서드를 호출하고자 한다면 super 키워드를 이용해 호출
- 상위 클래스 타입의 참조변수를 통해 하위 클래스 타입의 인스턴스를 참조하는 경우 상위클래스의 메서드만 호출 가능
---
- Car 클래스에 각각 static 키워드와 final 키워드로 선언된 메서드
- static 메서드의 경우 static 메모리 영역 내에 저장되기 때문에 상속 관계라 하더라도 상속 자체가 되지 않는다.
- final 메서드의 경우 상속은 시키되 상수처럼 기능을 바꾸게 하고 싶지 않을 때 선언하면 오버라이딩이 되지 않게 가능

```java
public class Car {
  private int speed = 10;
  private String name = "car";

  public int accel() {
    return this.speed + 10;
  }

  public void run() {
    System.out.println(name+" is running");
    System.out.println("speed : "+ this.speed);
  }

  public static void stop() {
    System.out.println("stop");
  }

  public final void test() {
    System.out.println("forbid overriding");
  }
}

public class Santafe extends Car{
  private int speed = 50;
  private String name = "Santafe";

  @Override
  public int accel() {
    return this.speed + 50;
  }

  @Override
  public void run() {
    super.run();
    System.out.println("after Overriding speed : "+this.speed);
  }

  public void call() {
    System.out.println("test not call");
  }

  // static 키워드의 경우 상속이 불가능하고, final 키워드의 경우 오버라이딩이 금지된다.
}
```

- 메서드 오버라이딩 규칙
  - 상속 관계에서 성립한다.
  - static 키워드로 선언된 메서드의 경우 static 메모리에서 관리하기 때문에 상속이 불가능하므로 오버라이딩 되지 않는다.
  - final 키워드로 선언된 메서드의 경우 오버라이딩이 불가능하다.
  - private 접근 지정자를 사용하는 경우 상속이 불가능하다.
  - 메서드의 이름, 파라미터 타입, 파라미터 개수, 리턴타입이 모두 동일해야 한다.


### Dynamic Method Dispatch
- 어떤 메서드를 호출할 지를 결정하여 해당 메서드를 실행하는 과정
- 어떤 메서드를 호출할 지를 컴파일시에 결정하는 것이 아닌 런타임 시점에 결정하는 것을 말한다.

```java
Car car = new Avante();
car.run();
```

- Car 클래스 타입 참조 변수가 하위 클래스 Avante 인스턴스를 참조
- 컴파일 시에는 상위 클래스 타입의 참조변수는 Car클래스를 참조하고 있기 때문에 car.run() 메서드를 호출하면 Car 클래스의 run() 메서드를 호출 할 것
- 하지만 런타임시에 Car클래스를 참조하고 있던 변수가 Avante 클래스 타입의 객체를 생성하고 참조하기 떄문에 Avante 클래스의 run() 메서드가 실제로 호출됨을 확인
- 따라서 다이나믹 메서드 디스패치는 참조변수가 컴파잀시에 참조하고 있는 클래스 타입의 메서드와 런타임시 참조하고 있는 클래스 타입의 메서드가 다르기 때문에 런타임 시에 메서드를 결정하여 호출한다.

### 추상클래스
- 연관된 클래스 사이에 비슷한 필드와 메서드를 공통으로 추출하여 만든 클래스
- 예를 들어, 투싼, 산타페, 스포티지가 있다고 생각하자. 각각의 차들은 주행하는 기능, 멈추는 기능이 있을 것이다. 이 때, 공통되는 기능인 주행, 멈춤 기능을 추출하여 자동차라고 칭할 수 있다. 이렇게 만들어진 자동차를 추상 클래스라고 할 수 있다.
- 추상 클래스는 abstract 키워드를 이용하며, 객체를 생성할 수 없다는 특징을 가지고 있다.
- 또한, 추상 메소드를 가지고 있는 클래스라면 반드시 추상 클래스로 정의해야한다.

```java
public abstract class AbstractCar {
    abstract public void run();
    abstract public void stop();
    public void accel() {
        System.out.println("액셀");
    }
}

//추상 메소드 반드시 구현
class Tucson extends  AbstractCar{

    @Override
    public void run() {
        System.out.println("투싼이 달린다");
    }

    @Override
    public void stop() {
        System.out.println("투싼이 멈춘다.");
    }
}

//추상 메소드 반드시 구현
class Sportage extends AbstractCar{

    @Override
    public void run() {
        System.out.println("스포티지가 달린다");
    }

    @Override
    public void stop() {
        System.out.println("스포티지가 멈춘다");
    }
}

```
- 추상 클래스를 사용하는 이유
  - 공통된 메소드와 필드를 통일하여 유지보수 용이 및 통일성 유지
  - 추상 클래스를 가지고 구체 클래스를 구현만 하면 되기 때문에 확장성 용이
  - 인터페이스 처럼 메소드를 구현해야하지만, 추상 클래스에 메소드를 정의하는 것이 가능하기 때문에 모든 추상 메소드 이외에는 구현이 필요한 메소드만 구현하면 된다.

### final 키워드
- 변수, 메소드, 클래스를 변경하지 못하도록 막아주는 키워드이다.
- 변경하지 못하도록 하는 것이기 때문에 반드시 초기화가 필요하다.
- final 클래스 : 상속이 불가능한 클래스이며, 어떤 클래스의 부모 클래스가 될 수 없음을 뜻한다.
```java
public final class FinalClass {
    int x = 10;
    int y = 20;
    int sum() {
        return this.x + this.y;
    }
}

//컴파일 에러 
class Test extends FinalClass {...}
```

- final 메소드 : 상속 시 오버라이딩이 불가능한 메소드를 말한다.
  - sum() 메소드는 오버라이딩이 가능하지만, mul() 메소드는 오버라이딩이 불가능함을 확인할 수 있다.
- final 변수 : 상수라고 불리며, 값을 변경할 수 없고 항상 할당된 값만 사용할 수 있다.
```java
final double PI = 3.141592;
PI = 1.11; //컴파일 에러 
```
### Object 키워드 
- 자바 내 모든 클래스의 최상위 클래스를 말하며 Object 클래스를 제외한 모든 클래스들은 Object 클래스로부터 상속받는다.
- Object 클래스에서 제공하는 모든 메소드들은 자동으로 상속받기 때문에 어떤 클래스에서든지 모두 사용이 가능하다.
- Object 클래스의 메소드
  - boolean equlas(Object obj) : 두 개의 객체를 비교해 결과를 반환
  - String toString() : 현재 객체의 문자열 반환
  - protected Object clone() : 객체를 복사
  - protected void finalize() : GC 직전에 객체의 리소스를 정리
  - Class getClass() : 객체의 클래스 타입 반환
  - int hashCode() : 객체의 코드값 반환
  - void wait() : 스레드를 일시중지
  - void wait(long timeout) : 파라미터에 주어진 시간만큼 스레드를 일시중지
  - void wait(long timeout, int nanos) : 파라미터에 주어진 시간만큼 스레드를 일시 중지
  - void notify() : wait 상태의 스레드를 다시 실행
  - void notifyAll() : wait상태의 모든 스레드를 다시 실행
