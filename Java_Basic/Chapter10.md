## Thread 클래스와 Runnable 인터페이스
- Thread 
  - 메모리를 할당 받아 프로그램을 실행하는 단위로서 하나의 프로세스에 여러개의 쓰레드로 구성될 수 있다.
  - 하나의 프로세스를 구성하는 여러 쓰레드는 스택 영역을 제외한 메모리 영역을 서로 공유한다.
  - 스택 메모리
    - 메서드 호출시 전달되는 매개변수, 되돌아갈 주소값 및 메서드 내에서 선언하는 변수 등을 저장하기 위해 사용되는 메모리 공간이기 때문에 쓰레드가 스택 메모리 영역을 독립적으로 가진다는 것은 독립적으로 메서드 호출과 실행이 가능하다는 뜻이다.
  - Java에서 Thread를 생성할 수 있는 방법
    - Thread 클래스를 확장한다.
      - java.lang.Thread 클래스를 상속받아 Thread를 생성해 사용한다. Thread 클래스 내의 여러개 메서중 run() 메서를 오버라이딩 해서 Thread를 사용한다.
  
```java
public class Study extends Thread {
    @Override
  public void run() {
        // 쓰레드 이름 가져오기
      String threadName = Thread.currentThread().getName();
      System.out.println(threadName+ "시작");
      try {
          // 쓰레드 3초 대기
        Thread.sleep(30000);
      }catch (InterruptedException e ) {
        e.printStackTrace();
    }
      System.out.println(threadName + "끝");
    }
}
```
- Runner클래스를 생성해 위에 생성한 Study 객체 쓰레드가 3초동안 대기하는지 확인하는 코드이다.
- join()은 쓰레드가 죽는것을 기다리는 메서드로, 메서드 매개변수로 밀리세컨드를 넣어주면 해당 시간만큼 기다린다.
```java
public class ThreadRunner {
    public static void main(String[] args) {
        LiveStudyThread thread1 = new LiveStudyThread();
        thread1.setName("라이브 스터디 스레드 #1");
        thread1.start();

        int second = 0;
        while(second < 3){
            try {
								//1초동안 스레드가 죽는것을 기다림
                thread1.join(1000);
                second++;
                System.out.println("second : "+second);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}

//실행결과
//Study 스레드 시작
//second : 1
//second : 2
//second : 3 
//Study 스레드 끝
```
- 위 코드를 실행하면 1초마다 초를 출력해주고 3초가 지난후 쓰레드가 끝나는 것을 확인할 수 있다.
    - Runnable 인터페이스를 구현해 사용한다.
      - Thread 클래스를 상속받아 구현한 것과 달리 Runnable 인터페이스를 구현해 동일한 쓰레드 기능을 가진 run() 메서드 작성 해봄
```java
public class LiveStudyRunnable implements Runnable{
    @Override
    public void run() {
        String threadName = Thread.currentThread().getName();
        System.out.println(threadName+" 시작");
        try {
            // 3초가 대기
            Thread.sleep(3000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println(threadName+" 끝");

    }
}
```
- Runnable로 구현한 스레드는 스레드 생성 시 Runnable 타입의 객체로 받은 후 Thread 클래스의 생성자 매개변수로 Runnable 객체를 넣어서 사용한다.

```java
Runnable runnable = new LiveStudyRunnable();
        Thread thread2 = new Thread(runnable) ;
        thread2.run();
        thread2.setName("라이브 스터디 러너블 스레드 #1");

        int second = 0;
        while(second<3){
        try {
        thread2.join(1000);
        second++;
        System.out.println("second : "+second);
        } catch (InterruptedException e) {
        e.printStackTrace();
        }
        }
```

### Runnable 인터페이스 구현 VS Thread 클래스 상속
- 스레드들 선언하는 2가지 방식은 공통적으로 run() 메소드를 오버라이딩하고 해당 메소드 내부의 기능들은 동일한 기능을 하도록 작성할 수 있기 때문에 둘 중 하나를 이용해 선언한다면 동일한 기능을 가진 스레드를 작성할 수 있다. 하지만, Java에서는 하나의 클래스는 한 개의 클래스밖에 상속을 받을 수 없기 때문에 Thread클래스를 상속받아 사용하는 클래스는 다른 클래스를 상속받아 사용하고자 할 때 사용할 수 없다. 반면에 인터페이스는 여러 개의 인터페이스를 구현해 사용할 수 있다.
- 따라서, 자바에서 스레드를 사용할 때에는 일반적으로 Runnable 인터페이스를 구현해 스레드를 사용하고, 해당 클래스에서 필요한 다른 클래스를 상속받아 사용한다고 한다.

## 쓰레드의 상태
- 객체 생성상태
  - 스레드 객체가 생성되고 start() 메서드가 실행되기 이전을 말한다. getState() 메서드의 Thread.State.NEW 열거 상수 상태이다.
- 실행 대기 상태
  - 스레드 스케줄링을 통해 실행되기 이ㅜ해서 대기하는 것을 말한다. getState() 메서드의 Thread.State.RUNNABLE 열거 상수 상태이다.
- 일시 정지 상태
  - 스래드의 실행이 중지되는 상태이다.
  - WATING
    - 다른 스레드가 통지할 때까지 기다리는 상태
  - TIMED_WAITING
    - 주어진 시간동안 기다리는 상태
  - BLOCKED
    - 사용하고자 하는 객체의 락이 풀리길 기다리는 상태
- 종료 상태
  - 스레드가 실행을 마친것을 말하며, getState()메서드의 Thread.State.TERMINATED 열거 상수 상태이다.


## 쓰레드 우선순위
- 하나의 프로세스는 여러개의 스레드를 가질 수 있다. 따라서 스레드의 작업에 스케줄링이 필요하다.
- 자바에서는 스레드 스케줄링 방법으로 우선순위 방법과 Round-Robin 방법을 사용한다.
- 스레드의 우선순위는 1-10까지 높을수록 더 우선순위가 높은 것으로 인식한다. 스레드 생성시 주어지는 Default우선순위는 5이고, 이 우선순위를 바꿔주기 위해서 setPriority() 메서드를 이용해 우선순위를 변경해준다.

