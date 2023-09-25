## 인터페이스 정의하는 방법
- 인터페이스
  - 추상 메서드,상수만을 선언 가능
  - 다른클래스에서 implements하여 모든 메서드 로직을 강제 구현 시킴
  - 자바는 다중 상속 (extends)가 불가능하여 인터페이스 도입
- tip) interface vs abstract
  - 추상화 메서드 강제성.interface는 모든 메서드가 추상화 메서드이고 abstract 클래스는 일부만 추상화 메서드로 선언 가능
- 정의 방법
```java
interface 인터페이스이름{
    public static final 타입 상수이름 = 값;
    public abstract 메서드이름(매개변수목록);
    // 기타 default 메서드, static 메서드, 중첩 타입 정의
}
```
- Java8 이전에는 추상 메서드와 상수만을 사용하여 implements한 클래스에게 강제 구현 하였다. 하지만 Java8 이후에는 default라는 메서드를 구현할 수 있게 되어서 좀 더 유연한 interface 설계가 가능
- 모든 멤버변수는 public static final (상수)
  - 생략가능
- 메서드 public 선언
  - 인터페이스를 public으로 지정하지 않으면 동일한 패키지에 정의 된 클래스에서만 인터페이스에 액세스 가능
- 인터페이스 사용이유
  - 개발시간 단축
    - 인터페이스를 정해두고 해당 인터페이스를 사용해서 프로그램을 개발하는 동시에 인터페이스에 관한 구체적인 코드 개발 동시 가능
  - 표준화 기능
  - 서로 관계없는 클래스들에게 관계를 맺어 줄 수 있다.
  - 독립적인 프로그래밍이 가능
    - 클래스 선언과 구현을 분리해서 실제 구현에 독립적인 프로그램 작성가능(인터페이스라는 막을 두고 간접관계 형성)

## 인터페이스 구현하는 방법
```java
public class ToyCar implements Car {
    
    @Override // 컴파일러에서 재정의 관련 문제를 예방하기 위해 꼭 사용
    public boolean drive() {
        System.out.println("장난감 자동차가 움직인다.");
        return  true;
    }
    
    public void play() {
        if (this.drive()) {
            System.out.println("장난감 자동차가 잘 움직이네.");
        }
    }
    
    //추가로 정의된 멤버, 메서드 구현
    //인터페이스에 정의되지 않은 것은 인터페이스를 통해서는 확인 불가능
}
```

- 인터페이스는 API로 사용될 수 있다. 일반적으로 내부의 인터페이스를 제외한 외부에서 제공된 인터페이스를 API라고 생각
- API를 사용할 때 내부 동작에는 신경쓰지 않고 어떻게 동작할지에 대한 약속만 신뢰 하는것과 동일


## 인터페이스 레퍼런스를 통해 구현체를 사용하는 방법
```java
class 인터페이스 {
    public static void main (Stirng[] args) {
        Car car = new ToyCar();
        
        car.drive(); // 가능
        car.play(); // 불가능
    }
}
```
- 컴파일 불가
  - play라는 메서드는 ToyCar에 분명이 정의 되어있다. 하지만 Car에서는 해당 메서드에 대해서 모르고 있는 상태
  - 따라서 play메서드를 호출하는 부분을 제거해야 컴파일이 된다.

```java
class 인터페이스 {
    public static void main (String[] args) {
        Car car = new ToyCar();
        
        car.drive();
    }
}
```
- 이러면 바로 ToyCar를 다른 것으로 대체해도 인터페이스의 약속만 지킨다면 코드 변경이 유연해진다.

```java
class 인터페이스 {
    public static void main (String[] args) {
        Car car = new ToyCar();
        
        car.drive();
        ((ToyCar)car).play(); 
    }
}
```


## 인터페이스 상속
- 인터페이스는 인터페이스로부터만 상속 가능
- 다중 상속 가능
  - 인터페이스는 다른 인터페이스를 extends(상속) 할 수 있다. (클래스는 하나의 클래스만 extends 할 수 있음)
  - public interface GroupedInterface extends Interface1,Interface2,Interface3 {}


```java
public interface DoIt {
    void doSomething (int i , double x);
    int doSomethingElse(String s);
}
```
- 인터페이스는 되도록 변경에 신중해야 한다. 처음 정의할 때 부터 모든 가능성을 염두에 두고 인터페이스를 지정해야 한다.
- 굳이 인터페이스에 메서드를 추가해서 잘 동작하던 클래스를 컴파일 에러가 발생하지 않게하는 것이 효과적이고, 필요없는 구현을 할 필요도 없다.


## 인터페이스의 기본 메소드 (Default Method), 자바 8
- 인터페이스의 인스턴스 생성과는 관계없이 인터페이스 타입에서 호출이 가능한 정적 메서드 접근제어자는 public으로 설정되어 있다.
- default 메서드
  - 추상 메서드의 기본적인 구현을 제공하는 메서드로, 추상 메서드가 아니기 때문에 디폴트 메서드가 새롭게 추가되어도 해당 인터페이스를 구현한 클래스를 변경하지 않아도 된다.
  - 앞에 default를 붙이며, 추상 메서드와 달리 일반 메서드처럼 몸동 {}이 있어야한다. 
- default 메서드 충돌 규칙
  - 여러 인터페이스들의 디폴드 메서드 간의 충돌
    - 인터페이스를 구현한 클래스에서 디폴트 메서드를 오버라이딩 해야한다.
  - 디폴트 메서드와 상위 클래스의 메서드 간 충돌
    - 상위 클래스의 메서드가 상속되고,디폴트 메서드는 무시된다.

## 인터페이스의 static 메소드, 자바 8
- static 메서드를 사용할 때에는 인터페이스 타입을 통해서 사용한다.
- 클래스에서 작성하는 방법과 동일하게 작성할 수 있고, 접근 제어자는 항상 public 이며 생략이 가능하다.
- 오버라이딩은 불가능하다.

## 인터페이스의 private 메소드, 자바 9
- Java9 에서는 인터페이스에서도 캡슐화를 지원한다. 정확히는 private 메서드와 private static메서드를 지원하기 시작했다.
- private 메서드의 사용은 인터페이스 내부에서 코드의 재사용성을 향상시킨다. 예를들어 두 개의 default 메서드가 같은 코드를 공유해야하는 경우 중복이 발생하는데 이를 방지할 수 있다.
- private 메서드 특성
  - 메서드 {} 이 있고 abstract이 아니다.
  - 구현체에서 구현할 수 없고 하위 인터페이스에서 상속이 불가능하다.
  - static 메서드도 private 가능
  - private 메서드는 private,abstract,default 또는 static 메서드를 호출할 수 있다. private static은 static 및 static private 메서드만 호출 가능하다.


## Constant Interface
- 오직 상수만 정의한 인터페이스
- 인터페이스에서 변수를 등록할 때 자동으로 public static final이 붙어서 상수처럼 어디에서나 접근 가능
- 하나의 클래스에 여러 개의 인터페이스를 implement할 수 있는데, Constatnt Interface를 implement할 경우, 인터페이스의 클래스명을 네임스페이스로 붙이지 않고 바로 사용 가능
- Anti패턴인 이유
    - 사용하리 장ㄴㅎ을수도 있는 상수를 포함하여 모두 가져오기에 계속 가지고 있어야 함.
    - 컴파일할 때 사용되겠지만, 런타임에는 사용용도가 없다.
    - Binary Code Complatibility을 필요로 하는 프로그램의 경우 새로운 라이브러리를 연결하더라도 상수 인터페이스는 프로그램이 종료되기 전까지 이진 호환성을 보장하기 위해 계속 유지되어야 함
    - IDE가 없으면 상수 인터페이스를 Implement한 클래스에서는 상수를 사용할 때 네임스페이스를 사용하지 않으므로, 해당 상수의 출처를 쉽게 알 수 없다. 또한 상수 인터페이스를 구현한 클래스의 하위 클래스들의 네임스페이스도 인터페이스의 상수들로 오염된다.
    - 인터페이스를 구현해 클래스를 만든다는 것은 해당 클래스의 객체로 어떤 일을 할 수 있는지 클라이언트에게 알리는 행위이다. 상수 인터페이스를 구현한다는 사실은 클라이언트에게는 중요한 정보가 아니다. 단지 클라이언트들을 혼란에 빠드린다.
    - 상수 인터페이스를 Implement한 클래스에 같은 상수를 가질 경우, 클래스에 정의한 상수가 사용되므로 사용자가 의도한 흐름으로 프로그램이 돌아가지 않을 수 있다.
- 따라서 이에 대한 방안으로 import static 구문의 사용 권장
```java
public final class Constants {
    private Constants() {
        
    }
    public static final double PI = 3.14159;
    public static final double PLANCK_CONSTANT = 6.62606896e-34;
    
}
```

```java
import static Constants.PLANCK_CONSTANT;
import static Constants.PI;

public class Calculations {
    public double getReducedPlankConstant() {
        return PLANCK_CONSTANT / (2 * PI);
    }
}
```