## 예외란
- exceptional event의 약어
- 프로그램 실행중에 발생하는 프로그램의 실행의 일반적인 흐름을 방해하는 이벤트
- 메서드 내에 에러가 발생하면, 메서드는 객체를 만들고 런타임 시스템에 전달한다. 이 객체는 예외 객체라고 불리며 에러에 대한 정보와 이에 대한 타입, 에러가 발생한 시점의 프로그램읫 ㅏㅇ태에 대한 정보를 담고 있다. 에외 객체를 생성하여 런타임 시스템에 전달하는것을 예외를 던진다 표현한다.
- 메서드가 예외를 던지면, 런타임 시스템은 해결할 수 있는 무엇을 찾기 위해 시도한다. 예외를 처리할 수 있는 무엇의 집합은 오류가 발생한 메서드를 사용하기 위해 불려진 메서드의 순서가 잇는 리스트이다. 메서드의 리스트는 콜 스택이라고 알려져 있다.
- 예외를 처리하면 기존 처리 기술에 비한 장점
  - 에러를 처리하는 코드와 일반 코드가 분리될 수 있다.
  - 콜 스택을 따라 에러 전파가 가능해 실질적으로 처리가 될 수 있는 지점에서 처리를 해줄 수 있다.
  - 오류를 그룹화 할 수 있고, 분류할 수 있다.


## 자바에서 예외처리 방법 (try,catch,throw,throws,finally)
### try-catch
- 하나의 try블럭 다음에는 하나 이상의 catch블록이 올 수 있다.
- 발생한 예외의 종류와 일치하는 단 한개의 catch블록만 수행된다.
- 발생한 예외의 종류와 일치하는 catch블럭이 없으면 예외는 처리되지 않는다.
- try블럭 내에서 예외가 발생한 경우
  - 발생한 예외와 일치하는 catch블록을 찾는다.
  - 일치하는 catch블럭을 찾게되면 해당 블록 내에 문장들을 수행하고 전체 try-catch문을 빠져나간다.
- 예외가 발생하지 않을 경우
  - catch블럭은 수행되지 않는다.
```java
try {
    // 예외가 발생할 가능성이 있는 코드
}
catch(ArithmeticException el) {
    // ArithmeticException이 발생했을 경우, 처리하는 문장을 작성
}
catch(Exception e2) {
    // ArtimeticException을 제외한 모든 예외가 발생했을 경우
        }
```
- 모든 예외 클래스는 Exception 클래스의 하위로 catch의 예외 타입을 Exception으로 작성하면 모든 예외를 처리할 수 있다.

### throw
- 프로그래머가 고의로 예외를 발생시킬 수 있다.

```java
try {
    Exception e = new Exception ("예외발생");
}
catch(Exception e) {
    System.out.println("에러 메세지:" + e.getMessage());
        }
        
        
// 결과 에러메시지 : 예외발생!
```
- Exception 인스턴스를 생성할 때, 생성자에 String을 넣어주면 이 String이 Exception 인스턴스에 메세지로 저장된다.
- 이러한 성격을 이용해 자바에 정의되어 있지 않은 케이스르 ㄹ예외로 지정해 예외를 발생하고 메세지를 전달할 수 있다.

### throws
- 메서드를 선언부에 작성함으로써 메서드 내에서 발생할 수 있는 예외를 선언할 수 있다. 여러 개의 예외를 선언하려면 쉼표로 구분한다.

```java
void method() throws Excetion1, Exception2 , ...ExceptionN()
```

- 메서드 선언부에 예외를 선언함으로써 이 메서드를 사용하기 위해 어떤 예외들이 처리되어야 하는지 알 수 있다.
- throws Exception으로 선언할 경우 모든 종류의 예외가 발생할 가능성이 있다.
- 이렇게 선언된 예외들은 해당 메서드에서 처리되는 것이 아니라, 자신의 호출한 메서드에게 예외를 전달하여 예외처리를 떠맡긴다.
- 예외를 전달받은 메서드가 또 다시 자신을 호출한 메서드에게 전달할 수 있으며, 이런식으로 계속 전달되다 마지막 main 메서드에서도 예외가 처리되지 않으면 프로그램 전체가 종료된다.

---
- 메소드를 선언할 때 매개 변수 소괄호 뒤에 throws라는 예약어를 적어 준 뒤 예외를 선언하면, 해당 메소드에서 선언한 예외가 발생했을 때 호출한 메소드로 예외가 전달된다.
- 만약 메소드에서 두 가지 이상의 예외를 던질 수 있다면, implements처럼 콤마로 구분하여 예외 클래스 이름을 적어주면 된다.
- try 블록 내에서 예외를 발생시킬 경우에는 throw라는 예약어를 적어 준 뒤 예외 객체를 생성하거나, 생성되어있는 객체를 명시해준다.
- throw한 예외 클래스가 catch 블록에 선언되어 있지 않거나, throws 선언에 포함되어 있지 않으면 컴파일 에러가 발생한다.
- catch 블록에서 예외를 throw 할 경우에도 메소드 선언의 throws 구문에 해당 예외가 정의되어 있어야만한다.

### finally
- try-catch 문의 긑에 선택적으로 덧붙일 수 있으며, 예외의 발생 여부와 상관없이 실행되어야 할 코드를 포함한다.
```java
try{
        // 예외 발생 가능성이 있는 문장들..
        }
        catch (Exception1 e1){
        // Exception1 발생 시 수행되는 문장들
        }
        finally{
        // Exception1 발생과 상관없이 수행되는 문장들
        // finally 블럭은 try-catch 문의 맨 마지막에 위치해야한다.
        }
```
- finally 블럭은 리소스 누수를 막기위한 중요 도구이다. 파일을 닫거나 리소스를 복구할 때, 코드를 finally 블럭에 넣어 리소스가 항상 복구되도록 한다.

## try-with-resources
- 하나 이상의 리소스를 정의하는 try와 관련된 문법.
- 하나 이상의 리소스를 정의할 수 있는데 이 때 유의할 점은 리소스 선언과 반대의 순서로 리소스가 닫힌다는 점이다. 또한 일반적인 try문 처럼 사용될 수 있고, catch, finally는 리소스가 닫힌 후에 실행된다.

```java
try(FileOutputStream out = new FileOutputStream("thewing.txt")) {
        //생략
        } catch(IOException e){
        e.printStackTrace();
        }
```

## 자바가 제공하는 예외 계층 구조
- 자바에서는 실행 시 발생할 수 있는 오류를 클래스로 정의하고 있다. 예외와 에러의 상속계층도는 아래와 같다.
```
Object
- Throwble - Error, Exception 
- Exception -> Runtime Exception
```
- Throwble 은 Object 를 상속하는 예외와 관련된 최상위 클래스이다. 이 클래스의 하위클래스들이 모두 예외 관련 클래스가 된다.
- Throwble은 직계하위로 Error와 Exception을 가지고 있다.


## Exception 과 Error의 차이
- Error 
  - JVM에서 dynamic linking 실패 또는 다른 hard 실패가 JVM에서 발생하면, JVM은 Error를 던진다. 단순한 프로그램은 일반적으로 이것을 catch하거나 던지지 않는다.
- Exception
  - 대부분의 프로그램은 Exception 클래스에서 파생된 객체를 던지고 받는다. Exception은 문제가 발생했음을 나타내지만, 심각한 시스템 문제는 아니다.
  - 작성하는 대부분의 Error가 아닌 Exception을 던지고 받는다.
  - 자바 플랫폼은 Exception클래스의 많은 하위를 두고있다. 이것은 발생할 수 있는 다양한 예외를 나타낸다. 
  - 예를들어 IllegalAccessException의 신호는 일부 메서드가 찾을수 없음을 말하고, NegativeArraySizeException은 배열을 음수 사이즈로 생성하려 할 때 발생한다.
  - Exception에는 서브 클래스 중에서 RuntimeException 이라는 특별한 예외 클래스가 있다. 이는 API의 잘못된 사용을 나타내는 예외를 위해 예약되어 있다.
  - 예를들어 자주 보이는 NullPointerException 은 메서드가 null 참조인 객체의 멤버에 엑세스 하려할 때 발생한다.
  - 클라이언트가 예외를 복구할 수 있다고 판단이 되면 CheckedException , 아니면 UnCheckedException 으로 만들어 보자


## RuntimeException과 RE가 아닌것의 차이
- RuntimeException은 프로그래머의 실수로 발생하는 예외이고, 이외의 모든것은 사용자의 실수와 같은 외적인 요인에 의해 발생하는 예외이다.
- Ex) RE - ArrayIndexOutOfBoundsException, NullPointerException, ClassCastException, ArthmeticException
- Re가 아닌것 - FileNotFoundException, ClassNotFoundException, DataFormException 등

## 커스텀한 예외 만드는 방법
- throw를 할 때, 다른 사람이나 언어가 제공한 예외를 사용할 수 있다. Java는 사용할 수 있는 많은 예외 클래스를 제공하지만 직접 작성할 수도있다.
- Excpetion클래스를 상속 받거나 필요에 따라 알맞는 예외 클래스를 상속받아 만든다. 생성자와 멤버를 추가함으로써 예외를 원하는 방식으로 만들어 사용할 수 있다.

```java
class CustomException extends Exception {
    CustomException(String msg) {
        super(msg);
    }
}
```

- 작성하는 대부분의 프로그램은 Exception의 하위면 충분하다.

## 예외포장
- 애플리케이션은 종종 다른 예외를 던지는 것으로 예외에 대한 응답을 한다. 한 예외가 다른 예외를 발생시키는걸 아는것은 매우 유용할 수 있다.
- 예외 포장은 프로그래머가 이를 수행하는데 도움을 준다.
- Throwble의 다음 메서드와 생성자는 예외 포장을 지원한다.
```java
Throwble getCause()
Throwble initCause(Throwble)
Throwble(String, Throwble)
Throwble(Throwble)
```
- initCause의 Throwble 인자와 Throwble 생성자의 인자는 현재 예외가 어떤 예외에 의해 발생했는지 알려준다. getCause()는 현재 예외의 원인인 예를 반환한다.initCause()는 현재 예외의 원인을 설정한다.

```java
try {
    
}catch (IOException e) {
    throw new SampleException ("Other IOException", e);
        }
```

- 위 예제는 예외 포장의 예이다. 이에는 IOException 이 발생할 경우 새로운 SampleException 예외가 생성이 되며, 원인이 되는 예외를 포장하게 된다.
- 그리고 해당 예외는 다음 상위 레벨의 예외 처리기로 던져진다.
- 이를 좀 더 활용하면 CheckedException을 UnCheckedException으로 포장하여 코드를 보다 깔끔하게 관리할 수 있다. (단, 반드시 처리하기 어려운 예외의 경우에만)
