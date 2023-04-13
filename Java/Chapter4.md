- 자바에서는 조건에 따라 실행되도록 하는 문법인 선택문 (if-then , if-then-else , switch), 반복해 실행되도록 하는 문법인 반복문 (for , while , do-while) 이 있으며, 분기를 수행하는 문법 (break , continue , return) 이 있다.


### 선택문
#### if 문
- 조건이 맞으면 if 내부 코드 실행
- 조건이 아니면 if문 밖 코드 실행

```java
int a = 4;
if(a==4) { // a가 4가 맞으면 밑에 있는 코드 실행
    System.out.println("a=4"); 
}
```

#### if-else문
```java
int a = 4;
if(a == 4) { // a가 4가 맞으면 밑에 코드 실행
    System.out.println("a=4");
     } 
    else { // 위 조건문이 실행되지 않으면 else문으로 실행
        System.out.println("a=4가 아님")
        }
```

- 모든 if문에 괄호를 사용하는 것을 추천한다. 일반적으로 코드의 취약성이 높아지는것이라고 생각하고,문장이 두 줄이 될 경우 중괄호를 추가해주어야 할 뿐더러 잊기도 쉽기 때문
#### Switch 문
- 하나의 식 값에 따라 여러 조건으로 나눌경우 if문을 사용하면 보기가 복잡하다.
- 식이 case 값과 일치하면 실행문을 실행한뒤 break를 만나면 switch문을 빠져나온다
- 만약 어떤 case문으로도 분기하지 못하면 default문 실행

```java
switch(조건식){
     case 값1:
     실행 코드
     break;
     case 값2:
     실행 코드
     break;
     case 값3:
     실행 코드
     break;
     default: case에 해당하는 값이 없을 때 실행할 코드 
      break;        
}
/*
case 값의 개수는 임의로 설정 가능
break : 코드가 실행되다가 break를 만나면,
바로 실행을 중지하고 해당 loop에서 빠져나옴 
*/
```
- switch 문 표현식은 byte,short,int,long,enum 우형,String 및 Byte, Short,Int 및 Long과 같은 일부 래퍼 유형일 수 있다.
  - 단, switch 표현식에서만 wrapper 허용하고 , case에는 wrapper를 허용하지 않는다.
- switch() 대괄호 사이에 변수 또는 표현식을 넣을 수 있다.
  - float는 두 개의 부동소수점 숫자를 비교하는 것은 x와 y의 십진수 등가가 정확하지 않을 수 있어 허용하지 않는다.
- 케이스 값은 리터럴 또는 상수여야 한다. 케이스 값 유형은 표현식 유형이어야 한다.
- 각 케이스는 고유해야 한다.
- 각 케이스에서는 선택적인 break 문이 있다.
- 어떤경우에도 break 문을 사용하지 않으면 break 문에 도달할 때까지 다음 case로 실행이 계쏙된다.
- switch문 케이스에 해당하는 경우가 없으면 default가 실행된다. default 케이스에는 break문이 필요하지 않다.

```java
char grade = 'B';

        switch(grade){
        case 'A':
        System.out.println("제일 높은 등급입니다");
        break;

        case 'B':
        System.out.println("두번째 높은 등급입니다");
        break;

        case 'C':
        System.out.println("세번째 높은 등급입니다");
        break;

default:
        System.out.println("잘못된 등급입니다");
        }
```

- grade가 case B의 값과 일치하기 때문에 두번쨰 높은등급 출력

```java
public class StringSwitchDemo {

  public static int getMonthNumber(String month) {

    int monthNumber = 0;

    if (month == null) {
      return monthNumber;
    }

    switch (month.toLowerCase()) {
      case "january":
          monthNumber= 1;
          break;
      case "february":
          monthNumber = 2;
          break;
      case "march":
          monthNumber = 3;
          break;
      case "april":
          monthNumber = 4;
          break;
      case "may":
          monthNumber = 5;
          break;
      case "june":
          monthNumber = 6;
          break;
      case "july":
          monthNumber = 7;
          break;
      case "august":
          monthNumber = 8;
          break;
      case "september":
          monthNumber = 9;
          break;
      case "october":
          monthNumber = 10;
          break;
      case "november":
          monthNumber = 11;
          break;
      case "december":
          monthNumber = 12;
          break;
      default:
          monthNumber = 0;
          break;
    }

    return monthNumber;
  }

  public static void main(String[] args) {

    String month = "August";

    int returnedMonthNumber = StringSwitchDemo.getMonthNumber(month);

    if (returnedMonthNumber == 0) {
      System.out.println("Invalid month");
    } else {
      System.out.println(returnedMonthNumber);
    }
  }
}
```
- Java SE 7 이후 버전부터는 String 객체를 switch문의 평가식으로 사용할 수 있습니다. 다음의 예제는 각 달의 이름으로 숫자 값을 구하는 것입니다.
- 위 코드의 결과는 8을 출력한다.
- switch 평가식의 String은 String.eqaul 메서드를 이용해 비교된다. 이 과정에서 toLowerCase 메서드를 통해 case의 구분없이 비교하게 된다.
- 가급적이면 String과 같이 객체를 Switch로 사용할 때는 NullPointerException 을 주의해야 한다
- null을 체크하는 로직을 꼭 추가하자!


### 반복문
#### while 및 do-while 문
- while문은 조건이 true인 동안 계속해서 블록안의 문장을 반복한다.
```java
while(expression) {
    statement(s)
        }
```
- while 문은 boolean 값을 리턴하는 표현식을 평가한다. 표현식이 true로 평가되면 while문은 while문의 블록 안에 있는 문장을 실행한다. while문은 false가 될 때까지 평가하고,블록안의 항목을 반복한다.

```java
class While문 {
    public static void main (String[] args) {
        int count = 1;
        while (count < 11) {
          System.out.println("Count is : " + count);
          count++;
        }
        }
        }
```
- 1부터 10까지 print
- 조건문에 true를 입력해 무한루프를 만들수도 있다.
```java
while(true) {
    //코드
        }
```

- 자바는 do-while 문법도 제공한다.
```java
do {
    statement(s)
        }while (expression);
```

- do-while문과 while문의 차이는 조건식의 평가와 반복되는 부분의 순서에 있다.
- while문은 식을 먼저 평가하고 반복한다.
- do-while문은 일단 한번 실행하고 반복여부를 평가한다.
- 즉 do-while문은 적어도 한 번의 실행을 보장하게 된다.

#### for
- 범위 반복을 하는 간결한 방법을 제공한다. 
```java
for (initializaion; termination; increment) {
    statement(s)
        }
```

- 주의점!!
  - initialization 표현식은 루프를 초기화한다. 이것은 루프가 실행되기 전 한번만 실행된다.
  - termination 표현식이 false 값으로 평가될 때까지 반복한다.
  - increment 표현식은 반복이 끝날 때마다 실행된다. 이 값은 증가하거나 감소하게 할 수 있다.
```java
class For문 {
    public static void main(String[] args) {
        for (int i = 1; i < 11; i ++) {
          System.out.println("count is:" + i);
        }
    }
}
```
- i 가 어떻게 선언되고,초기화되며,어떤 방식으로 평가되고, 증가하는 지를 알아야 한다.
- 이 변수가 루프 외부에서 필요하지 않는 경우 초기화 식에서 선언하는 것이 좋다.
- 그렇게 하면 변수가 딱 사용되는 범위만큼 수명을 갖게되고, 오류가 줄어들 수 있다.
- for 문에서는 i,j,k 와 같은 변수들이 주로 사용된다.
- 모두비우면 무한루프가 된다.
```java
for(;;) {
    //코드
        }
```

- enhanced for 문은 배열이나 컬렉션 같이 연속된 정보를 접근하는 방법이다. 
- for 문보다 훨씬 간결하고 읽기 쉽다.

```java
class EnhancedFor문 {
    public static void main(String[] args) {
        int[] number = {1,2,3,4,5,6,7,8,9,10};
        
        for(int item : number){
          System.out.println(item);
        }
    }
}
```

- 가능하면 이 형식을 사용하는것이 좋다. 가독성이 좋고 내부적으로 iterator 를 사용하는 경우 인덱스를 통한 접근보다 빠른 경우가 있기 때문이다.
