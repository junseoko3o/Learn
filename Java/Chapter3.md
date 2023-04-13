## 연산자
### 산술 연산자
- +,-,*,/,% 5가지로 구성되어있다.
- %는 나머지 값을 구하는 연산자로 Modulo라고 불린다

```java
class 연산 {

    public static void 산술연산자() {
        int var1 = 1;
        int var2 = 2;

        System.out.println("var1 + var2 =" + (var1 + var2));
        System.out.println("var1 - var2 =" + (var1 - var2));
        System.out.println("var1 * var2 =" + (var1 * var2));
        System.out.println("var1 / var2 =" + (var1 / var2));
        System.out.println("var1 % var2 =" + (var1 % var2));


        double var3 = 1;
        double var4 = 2;

        System.out.prinln("var3 / var4 =" + (var3 / var4));
    }
}
```
- var1 + var2 = 3
- var1 - var2 = -1
- var1 * var2 = 2
- var1 / var2 = 0
- var1 % var2 = 1
- var3 / var4 = 0.5

---

- int 자료형을 사용했을 경우 1/2 는 0.5 라는 결과값이 나와야하지만 int 타입은 소수점은 표현하지 않기 때문에 .5가 나오지 않고 0 이라는 결과값이 나온다.
- double 자료형을 사용하면 0.5라는 결과를 얻을 수 있다.


### 비트 연산자
- Java에서는 정수타입에 대해서 비트와 비트 시프트 연산을 제공하는데 이를 비트 연산자라고 한다.
- 비트연산이라는 의미는 우리가 사용하는 정수 타입은 사실 컴퓨터가 이해할 수 있도록 2진수 형식으로 표현된다.
- 이진수 조각 하나하나를 비트라고 표현하고, 비트연산은 이 조각들마다 연산을 수행한다.
- 비트연산이 산술연산보다 속도는 빠르지만 가독성이 떨어지므로 정말 성능개선이 필요한 부분에만 사용해야 한다.
<img src = "https://media.vlpt.us/images/junseokoo/post/3cb0a0cc-3d75-473f-95a0-43106cce5d22/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-01-18%2019.03.52.png">

```java
class 연산 {
    
    public static void 비트연산자() {
        // int자료형은 8Byte 이므로 32비트로 표현된다.
        // 0000 0000 0000 0000
        // 연산 설명을 편의를 위해 앞의 12자리는 제외하고 실제 값이 표현되는 마지막 4자리만 표시한다.
        
        int var1 = 3;
        int var2 = 5;
        
        System.out.println("var1 & var2 = " + (var1 & var2));
        System.out.println("var1 | var2 = " + (var1 | var2));
        System.out.println("var1 ^ var2 = " + (var1 ^ var2));
        System.out.println("var1 >> = " + (var1 >> 1));
        System.out.println("var1 << = " + (var1 << 1));
        
        
    }
    
}

```
- var1 & var2 = 1
- var1 | var2 = 7
- var1 ^ var2 = 6
- var1 >> = 1
- var1 << = 6


```java
class 연산 {
    public static void 비트연산자 {
        // 참고로 부호비트도 고려해야 합니다.
        byte a = 0b00001010; //  10  (0|0001010)
        byte b = 0b00101000; //  40  (0|0101000)
        byte c = -0b00001010; // -10 (1|1110110)

// ~ 연산자(1의 보수를 만들어줌)
        System.out.println(~a); // 1|1110101 => -11 여기에 1을 더하면 -10이 됩니다.(2의 보수)
        System.out.println(~c); // 0|0001001 => 9   여기에 1을 더하면 10이 됩니다.

// & 연산자
        System.out.println(a & b); // 0|0001000 => 8
        System.out.println(a & c); // 0|0000010 => 2
        System.out.println(b & c); // 0|0100000 => 32

// | 연산자
        System.out.println(a | b); // 0|0101010 => 42
        System.out.println(a | c); // 1|1111110 => -2
        System.out.println(b | c); // 1|1111110 => -2

// ^ 연산자(다른 경우에만 1)
        System.out.println(a ^ b); // 0|0100010 => 34
        System.out.println(a ^ c); // 1|1111100 => -4
        System.out.println(b ^ c); // 1|1011110 => -34
    }
}

```

#### And(&)
- 같은 위치의 값 모두 1일 경우에 값이 1이 된다.
- 결과값으로 1 (0001)

#### OR(|)
- 같은 위치의 값 중 하나라도 1일 경우 값이 1이 된다.
- 결과값으로 7 (0001)

#### XOR(^)
- 같은 위치의 값 중 한개만 1이어야 1이 된다.
- 결과값으로 6(0110)

#### Right Shift (>>)
- 값을 오른쪽으로 shift 시킨다.
- 결과값으로 1

#### Left Shift (<<)
- 값을 왼쪽으로 shift 시킨다.
- 결과값으로 6

#### 단항 연산자
- +를 붙이면 양수 값을 나타낸다. 생략가능
  를 붙이면 음수 값을 나타낸다.
- ++를 붙이면 값을 1씩 증가시킨다. 이는 피연산자의 위치에 따라 의미가 살짝 달라진다. 오른쪽에 위치할 경우 식을 평가하기 전 증가 시키고 왼쪽에 위치하는 경우 식을 평가한 후에 증가 시킨다.
- --를 붙이면 1씩 감소시킨다. 피연산자의 위치에 따란 의미는 위와 동일

```java
class 연산자 {
    public static void 단항연산자 {

        int result = +1;
        System.out.println(result); // 1

        result--;
        System.out.println(result); // 0

        result++;
        System.out.println(result); // 1

        for (int i = 0; i < 3; i++) {
            System.out.println(++result); // 2, 3, 4
        }

        System.out.println(result); // 4(이미 이전에 증가해서 그대로 출력된다.)

        for (int i = 0; i < 3; i++) {
            System.out.println(result++); // 4, 5, 6
        }

        System.out.println(result); // 7(마지막에 증가한다.)
        
    }
}

```
### 관계 연산자
- 피연산자가 같은지(==), 같지 않은지(!=), 큰지(>) ,  크거나 같은지 (>=) ,작은지 (<) , 작거나 같은지(<=) 비교하는 연산자
- 단, 문자열의 동등성을 비교할 때에는 equals() 메서드르사용해야한다.

```java
class 연산 {
    public static void 관계연산자() {
        
        int a = 7;
        int b = 11;
        
        System.out.println(a == b); // false
        System.out.println(a != b); // true
        System.out.println(a > b); // false
        System.out.println(a >= b); // false
        System.out.println(a < b); // true
        System.out.println(a <= b); // true
    }
}
```
### 논리 연산자
- 피연산자로 boolean 값을 받으며, 이는 평가의 결과가될 수 있다. 보통 식이 전달되는 경우가 많음
- && 연산자
  - 두 연산결과가 참인지 판단. 둘 중 하나라도 거짓이라면 거짓을 반환시켜준다.
  - 왼쪽 피연산자가 거짓이면 오른쪽의 피연산자는 평가하지 않는다.
- ||연산자
  - 두 연산결과 중 한 쪽만 참이어도 참을 반환한다.
  - 왼쪽의 피연산자가 참이라면 오른쪽의 피연산자는 평가하지 않는다.
- !연산자
  - 피연산자를 하나만 받는 단항 연산자이며 true를 false로 , false를 true로 변경한다.
  - 식 평가 방향은 오른쪽에서 왼쪽!
- 그이외의 평가하지않는것 (short circuit evaluation)
  - 식의 평가를 수행하지 않기 때문에 조금 더 빠른 결과를 얻을 수 있다.

```java
class 연산자 {
    private static void 논리연산자() {
        boolean var1 = true;
        boolean var2 = true;
        boolean var3 = false;
        boolean var4 = false;

        System.out.println("var1 && var2"); // true
        System.out.println(var1 && var2);   
        System.out.println("var1 && var3"); // false
        System.out.println(var1 && var3);  
        System.out.println("var1 || var3"); // true
        System.out.println(var1 || var3);
        System.out.println("var3 || var4"); // false
        System.out.println(var3 || var4);
    }
}
```

### instance of
- 타입 비교 연산자이다. 이를 이용해 객체가 클래스의 인스턴스, 하위클래스의 인스턴스 또는 특정 인터페이스를 구현하는 클래스의 인스턴스인지 테스트할 수 있다.
- instanceof는 상속을 받은 클래스와 상속을 한 클래스도 true가 된다.
- 마찬가지로 interface와 implements 받은 클래스도 결과는 true

```java
public class Main {

  public static void main(String[] args) {
    Animal animal1 = new Animal();
    Animal animal2 = new Cat();

    System.out.println("animal1 is instanceof Animal: " + (animal1 instanceof Animal)); // true
    System.out.println("animal1 is instanceof Cat: " + (animal1 instanceof Cat)); // false
    System.out.println("animal1 is instanceof Meowable: " + (animal1 instanceof Meowable)); // false

    System.out.println("animal2 is instanceof Animal: " + (animal2 instanceof Animal)); // true
    System.out.println("animal2 is instanceof Cat: " + (animal2 instanceof Cat)); // true
    System.out.println("animal2 is instanceof Meowable: " + (animal2 instanceof Meowable)); // true
  }
}

class Animal {}
interface Meowable {}
class Cat extends Animal implements Meowable {}
```


### assignment(=) operator
- 할당 연산자는 연산자 오른쪽의 값을 연산자 왼쪽의 피연산자에게 할당한다.
- 식의 평가방향은 오른쪽에서 왼쪽
- int x = 0;
  - 위와 같은 연산자는 x라는 이름을 가진 변수 공간에 0이라는 int형 리터럴을 할당한다. 또한 객체도 할당할 수 있다.
- Animal animal = new Cat();
  - 위와 같은 식은 animal 이라는 Animal 타입 참조변수에 새로 만들어진 Cat 인스턴스의 참조를 할당한다.
- 주의할 점은 할당할 수 없는 리터럴과 같은 값은 왼쪽 피연산자가 될 수 없다.

```java
class 연산 {
  private static void assignmentTest() {
    int a = 8;
    int b = 3;

    System.out.println("a = b -> " + (a = b));      //            3
    System.out.println("a += b -> " + (a += b));    // a = a + b  6
    System.out.println("a -= b -> " + (a -= b));    // a = a - b  3
    System.out.println("a *= b -> " + (a *= b));    // a = a * b  9
    System.out.println("a /= b -> " + (a /= b));    // a = a / b  3
    System.out.println("a %= b -> " + (a &= b));    // a = a & b  3
  }
}
```
#### 복합문(Compound Statement) ,  복합 할당 (Compound assignment)
- 다른 연산자와 할당 연산자를 결합한다.
- a = a + 1;
  - a가 중복된다. 그래서 이를 간단하게 나타내기 위한 표현
  - a += 1; 로 바꿀수 있다.

```java
public static void main(String[] args) {
  int a = 0;

  a = a + 1;
}
```
```java
public static void main(java.lang.String[]);
  Code:
     0: iconst_0
     1: istore_1
     2: iload_1
     3: iconst_1
     4: iadd
     5: istore_1
     6: return

```
```java
public static void main(String[] args) {
  int a = 0;

  a += 1;
}
```
```java
 public static void main(java.lang.String[]);
    Code:
       0: iconst_0
       1: istore_1
       2: iinc          1, 1
       5: return
```

- 둘의 바이트코드가 다른것을 확인할 수 있다.

### 화살표(->) 연산자
- Java8에서 추가된 람다 표현식의 한 부분이다.
- 람다 표현식
  - 단일 메서드 인터페이스인 경우 간결하게 표현할 수 있는 방식이다.
  - 함수형 프로그래밍에서 가장 중요한 부분이며, 이를 도입함으로써 자바는 함수형 언어로도 가능하게 되었다. 이는 일부 익명 클래스를 간단히 표현할 수 있는 방법이라고도 볼 수 있다.
  - 또한 @FrunctionalInterface 애노테이션을 붙인 인터페이스의 구현체로도 사용할 수 있다.
  - 메서드가 매개변수로 전달되는 것이 가능하고, 결과로 반환되는 것도 가능하게 해준다.
- (파라미터) -> { Body } 형태로 작성한다.

```java
class lamda {
  private static void lamdaTest() {
    Test1 test1 = new Test1();
    test1.addTestInterface(new TestInterface() {
      @Override
      public void addTestListener(Object o) {
        System.out.println("add Test lister = " + o);
      }
    });
    test1.callInterface("not use lamda");


    Test1 test2 = new Test1();
    test2.addTestInterface(testLister -> {
      System.out.println("add Test lister lamda = " + testLister);
    });
    test2.callInterface("use lamda");
  }
}
```
- add Test lister = not use lamda
- add Test Lister lamda = use lamda
- 위의 2가지 코드로직은 같은 기능을 수행한다.
- 이처럼 람다표현식을 사용하면 소스를 간결화할 수 있다.


### 3항 연산자
- ?:는 논리 연산자의 일종으로 피연산자를 세 개를 받는 유일한 연산자이기에 삼항 연산자로 불린다.
- 이는 if -else 문과 비슷하게 보이며, 한 줄로 간단하게 표현할 수 있다.
- 조건 ? 참일때 값 : 거짓일때 값 의 표현으로 사용한다.

```java
class Main {
    private static void 삼항연산자() {
        
        String a = "a";
        
        System.out.println("a == a ->" + (a == "a" ? true : false));        //true
        System.out.println("a == b ->" + (a == "b" ? true : false));        //false
        
        // 1)과 동일하게 작동
      if (a == "a") {
          return true;
      } else {
          return false;
      }
    }
}
```
- [조건] ? [조건이 참인경우 실행] : [조건이 거짓인 경우 실행]
- 3개의 피연산자인 경우에만 사용하는것을 추천
- 아래 코드는 3항 연산자를 두 번 사용한 코드
```java
boolean c = a == "b" ? a == "c" ? false : true :false;
```
- 가독성 DOWN


### 연산자 우선순위
- 식을 평가할 때 많은 영향을 미친다. 우선순위에 따라서 의도한 대로 프로그램이 동작하지 않을 수 있기 때문이다.
- 할당 연산자를 제외한 모든 이항 연산자는 왼쪽에서 오른쪽으로 평가되며, 할당 연산자는 오른쪽에서 왼쪽으로 평가한다.

1. 최우선연산자 : . [] ()
2. 단한연산자 : ! ~ +/- ++/-- (cast)
3. 산술연산자 : + - * / %
4. 시프트연산자 : << >> >>>
5. 관계연산자 : > < <== >== == !=
6. 비트연산자 : & ^ |
7. 논리연산자 : && ||
8. 삼항연산자 : 조건항 ? 항1 : 항2
9. 배정대입연산자 : = += -= *= /= %= <<= >>= ^= &= |=
10. 후위형증감연산자 : ++ /--
11. 순차연산자 : ,

<img src = "https://media.vlpt.us/images/junseokoo/post/78327eb8-4de9-4ca5-9642-86749a622b2d/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-01-19%2017.48.05.png" width="300">

- 실제 프로그래밍 세계에서는 헷갈릴 가능성이 높으므로 () 로 먼저 수행하고 싶은 식을 묶어주는 것이 가독성 등의 여러 관점에서 더 좋다.
- 대신 자주 나오는 연산자들의 우선순위는 알아두자!

### (optional) Java13. switch 연산자
- 해당 Feature의 이름은 Switch Expressions 이다.
- 즉 단일 값으로 평가되는 하나의 표현식이다.
- 여기서 또 하나 추가된 표현으로는 "arrow case" 레이블이 있는데, 기존 swirch 문의 break 문 없이도 아래로 떨어지는것을 방지 해준다.
- 값을 지정하기 위해선 break문 대신에 yield 문을 사용해야 한다.
- 이전의 Switch 문과 비교

```java
public enum Day { SUNDAY, MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY, SATURDAY; }

// ...

public class Main {
  public static void main(String[] args) {
    int numLetters = 0;
    Day day = Day.WEDNESDAY;
    switch (day) {
      case MONDAY:
      case FRIDAY:
      case SUNDAY:
          numLetters = 6;
          break;
      case TUESDAY:
          numLetters = 7;
          break;
      case THURSDAY:
      case SATURDAY:
          numLetters = 8;
      case WEDNESDAY:
          numLetters = 9;
          break;
      default
          throw new IllegalStateException("Invalid day: " + day);
    }
    System.out.println(numLetters);
  }
}
```

- numLetters 라는 변수 대신에 그냥 바로 return 해주는것이 좋을것 같다.
- break; 를 사용하지 않는 편이 더 좋을것 같다. 특히 break;를 까먹으면 잘못될 수 있다.
- 이제 Switch Expressions를 사용
```java
Day day = Day.WEDNESDAY;
System.out.println(
      switch (day) {
          case MONDAY, FRIDAY, SUNDAY -> 6;
          case TUESDAY                -> 7;
          case THURSDAY, SATURDAY     -> 8;
          case WEDNESDAY              -> 9;
          default -> throw new IllegalStateException("Invalid day: " + day);
      }
);
```

- 훨씬 가독성이 좋아짐.
- 새로운 case 레이블은  `case label_1, label_2, ..., label_n -> expression; | throw-statement;| block 
- Java 런타임은 arrow 왼편의 레이블 중 아무거나 매치가 되면, 그 오른쪽에 위치한 코드를 실행시키고, 아래로 떨어뜨리지 않는다.
- switch 표현식의 다른 코드와 문을 실행시키지 않습니다.
- 만약 코드의 오른쪽에 위치한 것이 표현식이라면, 표현식의 값이 switch 표현식의 값이 된다.

```java
int numLetters = 0;
Day day = Day.WEDNESDAY;
switch (day) {
    case MONDAY, FRIDAY, SUNDAY -> numLetters = 6;
    case TUESDAY                -> numLetters = 7;
    case THURSDAY, SATURDAY     -> numLetters = 8;
    case WEDNESDAY              -> numLetters = 9;
    default -> throw new IllegalStateException("Invalid day: " + day);
};
System.out.println(numLetters);
```
- 위와 같이 식으로 변수게 값을 할당해 줄수도 있고

```java
Day day = Day.WEDNESDAY;
int numLetters = switch (day) {
    case MONDAY:
    case FRIDAY:
    case SUNDAY:
        System.out.println(6);
        yield 6;
    case TUESDAY:
        System.out.println(7);
        yield 7;
    case THURSDAY:
    case SATURDAY:
        System.out.println(8);
        yield 8;
    case WEDNESDAY:
        System.out.println(9);
        yield 9;
    default:
        throw new IllegalStateException("Invalid day: " + day);
};
System.out.println(numLetters);
```

- 위와 같은 식으로 "clon case" 레이블을 사용할 수도 있다. 여기서 yield문은 한 개의 인자를 받아 switch 표현식의 값으로 제공한다.
- 되도록이면 "arrow case" 레이블을 사용하는것이 좋다. break 문을 신경쓰거나 yield 문을 신경쓰지 않을 수 있도록 해준다.
- "arrow case" 레이블의 경우 여러 명령문이나 코드를 작성하려면 블록으로 묶어준 다음 yield 문으로 값을 제공해줘야 한다.

