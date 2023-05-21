## Spring

- Spring이란?
    
    Java언어 기반의 프레임워크 이고 좋은 객체 지향 애플리케이션을 개발할 수 있게 도와주는 프레임 워크이며,스프링 프레임워크, 스프링 부트와 함게 스프링 데이터, 스프링 세션, 스프링 시큐리티, 스프링 RestDocs,스프링 배치 , 스프링 클라우드 등과 함께 사용된다.
    
- 스프링 3대 요소와 각각 특징  및 스프링부트의 장점
    
    스프링 3대요소
    
    - 제어의 역전 (Ioc, Inversion of Control) / 의존성주입 (DI, Dependency Injection)
        - 제어의 역전
            - 메서드나 객체의 호출작업을 개발자가 결정하는것이 아닌 외부에서 결정되는것 이다.
        - 의존성 주입
            - 제어의 역행이 일어날 때 스프링이 내부에 있는 객체들간의 관계를 관리할 때 사용하는 기법.
    - 관점 지향 프로그래밍 (AOP, Aspect Oriented Programming)
        - Java의 OOP를 더욱 OOP 답게 사용할 수 있게 도와준다.
        - OOP인 Java는 객체를 재사용함으로써 반복되는 코드의 양을 굉장히 많이 줄일 수 있었는데, 객체의 재사용에도 불구하고 반복되는 코드를 없앨 수 없었다.로그,권한체크,인증,예외처리 등 필수적으로 해야하기 때문에 소스에서 반복될 수 없는 부분도 있다. AOP는 이런 문제를 해결해 준다.
    - 서비스 추상화 (PSA, Portable Service Abstraction)
        - 환경의 변화와 관계없이 일관될 방식의 기술 접근환경을 제공하려는 추상화 구조이다.
        - Spring은 Spring Web MVC, Spring Transaction,Spring Cache등의 다양한 PSA제공
    
    스프링 부트의 장점
    
    - Tomcat같은 웹 서버를 내장함으로써 스프링 프레임워크와 달리 웹 서버를 설치하지 않아도 된다.
    - 단독으로 실행하도록 스프링 애플리케이션을 쉽게 생성해줌
    - 간단한 빌드 구성을 위한 starter 종속성 제공
        - Starter가 프로젝트를 구성하는 필요한 라이브러리를 자동으로 구성함으로써 편의성을 증대 시킴
    - 스프링과 써드 파티 라이브러리의 자동구성
        - 스프링 프레임워크의 버전을 확인하고 해당 버전과 호환성이 좋은 외부 라이브러리를 자동으로 구성하므로 개발자가 다양한 라이브러리의 버전을 확인할 필요성을 없앰
- 의존성을 주입하는 방법
    
    Spring은 @Autowired 애노테이션을 이용한 다양한 의존성 주입 방법을 제공한다. DI를 주입하는 3가지방법이 있다.
    
    - 생성자 주입
        - 생성자에 @Autowired 애노테이션을 붙여 의존성을 주입받을 수 있다.
        - Spring4.3 부터는 클래스의 생성자가 하나이고 그 생성자로 주입받을 객체가 빈으로 등록되어 있다면 생성자 주입에서 @Autowired를 생략할 수 있다.
    - 필드 주입
        - 변수 선언부에 @Autowired 애노테이션을 붙인다.
    - Setter 주입
        - Setter메소드에 @Autowired 애노테이션을 붙인다.
- 생성자 주입의 장점
    - 생성자 호출시점에 딱 1번만 호출되는 것이 보장 된다.
    - 객체를 생성할 때 딱 1번만 호출되므로 이후에 호출되는 일이 없다. 따라서 불변하게 설계할 수 있다.
    - NPE 방지
    - Immutable 객체 생성
    - 순환참조 방지
- AOP 용어 말해보세요
    - Joinpoint
        - Advice를 적용가능한 지점
    - Pointcut
        - Joinpoint의 부분 집합으로, Advice가 적용되는 Joinpoint를 나타낸다.
    - Advice
        - Aspect를 언제 핵심 코드에 적용할 지 정의
        - Before Advice
            - 대상 객체의 메서드 호출 전에 공통 기능 실행
        - After Returning Advice
            - 대상 객체의 메서드가 예외 없이 실행된 이후에 공통기능 실행
        - After Throwing Advice
            - 대상 객체의 메서드를 실행하는 도중 예외가 발생한 경우 공통기능 실행
        - After Advice
            - 대상 객체의 메서드 실행 후 공통기능 실행
        - Around Advice
            - 대상 객체의 메서드 실행 전/후, 예외발생 시점에 공통기능 실행
    - Weaving
        - Advice를 핵심 코드에 적용하는 것
    - Aspect
        - 여러 객체에 공통으로 적용되는 기능 (공통기능)
- AOP적용 방법
    - 컴파일
        - 자바 파일을 클래스 파일로 만들때 조작된 바이트 코드를 생성하여 적용
    - 로드타임
        - JVM이 클래스를 로딩하는 시점에 추가하여 로딩(로드 타임 위빙)
    - 런타임
        - JVM이 클래스를 로딩한 후 Bean을 생성할 때 해당 클래스의 프록시빈을 생성하여 적용
- Bean이란?
    
    Spring Ioc 컨테이너가 관리하는 자바 객체이다.
    
- Bean을 등록하기 위한  방법
    - xml에 직접 설정하기
        - 모든 빈을 직접 등록하고 의존성도 모두 작성해야하기 때문에 번거로움
    - Component Scan
        - @Component 가 붙은 객체를 스캔해 등록한다. @Service, @Repository, @Controller, @Configuration 들은 모두 @Component를 상속받고 있기 때문에 등록된 클래스들은 스프링 컨테이너에 자동으로 생성되고 스프링 빈으로 등록된다.
    - 자바 설정 파일 (Java Config )
        - ApplicationContext의 구현체 **AnnotationConfigApplicationContext**을 생성할 때 설정파일의 클래스를 넣어주면 된다.
        - **xml = ClassPathXmlApplicationContext**
        
              **java config 파일 = AnnotationConfigApplicationContext**
        
    - @SpringBootApplication
        - @SpringBootApplication 은 @Configuration 과 @ComponentScan 을 이미 상속받고 있기 때문에 클래스들이 등록될 수 있도록 제공하고 있다. 때문에 개발자가 특별한 선언을 하지 않아도 Component 관련 애노테이션만을 붙여주면 auto-scan되어 빈이 등록되게 된다.
- Bean의 Scope의 개념
    
    빈이 사스프링 컨테이너에서 존재할 수 있는  범위인데, 빈이 앱이 구동되는 동안 한개만 만들어서 쓸것인지 HTTP요청마다 생성해서 쓸 것인지 등을 결정하는 것
    
- Transactional어노테이션 이란?
    
    해당 어노테이션이 적용되는 메서드를 하나의 트랜잭션으로 묶어주는 역할을 한다.
    
- 스프링 MVC란?
    - Spring 프레임워크에서 제공하는 웹 모듈이다.
    - Model-View-Controller의 약자로 기본 시스템 모듈을 MVC로 나누어 구현되어있다.
- MVC로 개발할때의 장단점
    - 장점
        - 유연하고 확장하기 쉽다
        - 유지보수 비용 절감
    - 단점
        - Model과 View의 완벽한 분리가 어렵다.
        - 기본기능 설계를 위해 클래스들이 많이 필요하기 때문에 복잡할 수 있다.
- 우리가 클라이언트 요청을 받아서 컨트롤러에서 서비스 레이아웃까지 이루어지는데 클라이언트 요청이 Controller에 도착할때까지 스프링 MVC가 처리 해줄텐데, 이때까지의 과정을 설명해라 (MVC동작과정)
    - 1) DispatcherServlet이 모든 웹 브라우저로부터의 요청을 받는다.
    - 2) DispatcherServlet은 HandlerMapping으로 부터 주어진 request를 처리할 수 있는 Handler객체를 가져온다.
    - 3) 가져온 Handler를 실행(invoke) 시킬 수 있는 HandlerAdapter객체를 가져온다.
    - 4) 만약 해당 Controller를 처리할 Handler객체에 적용할 interceptor가 존재한다면 모든 interceptor객체의 preHandle메소드를 호출한다.
    - 5) HandlerAdapter객체를 통해 실제 컨트롤러의 메소드를 실행 후 ModelAndView를 얻는다.
    - 6) 만약 해당 Controller를 처리할 Handler객체에 적용할 interceptor가 존재한다면 모든 interceptor객체의 postHandle메소드를 호출한다.
    - 7) DispatcherServlet은 5번 과정에서 얻은 ModelAndView를 통해 view name을 ViewResolver에게 전달하여 응답에 필요한 View객체를 얻어온다.
    - 8) DispatcherServlet은 7번 과정에서 얻은 View객체에 5번 과정에서 얻은 ModelAndView의 Model을 파라미터로 넘겨주어 render메소드를 호출하여 페이지 렌더링을 수행한다.
    - 9) DispatcherServlet은 렌더링된 페이지를 response로 사용자에게 리턴한다.
- Controller 와 RestController의 차이
    - HTTP  Response Body가 생성되는 방식의 차이가 있다.
    - @Controller는 View기술을 사용하지만, @RestController는 객체를 반환하기만 하면 객체 데이터는 Json/xml 형식의 HTTP 응답을 직접 작성하게 된다.
    - Controller 는 view를 리턴 하고 (ResponseBody를 사용해 객체 리턴가능) , RestController 는 데이터를 리턴한다.
- 필터와 인터셉터의 차이
    
    필터에서는 스프링과 무관하게 전역적으로 처리해야하는 작업들을 처리할 수 있고,웹 애플리케이션에 전반적으로 사용되는 기능을 구현하기에 적딩하다. ServeletRequest/ServletResponse 객체를 조작할 수 있다는점에서 인터셉터보다 강력한 기숧이다.
    
    인터셉터에서는 클라이언트의 요청과 관련되어 전역적으로 처리해야 하는 작업들을 처리할 수 있다.
    
    컨트롤러로 넘겨주기 위한 정보를 가공하기에 용이하다.
    
- Spring Transaction이 어떻게 작동하는지?
    
    Transaction은 스프링 AOP Proxy를 통해 처리가 된다.
    
    - CGLIB(bytecode생성)
        - 클래스에 대한 Proxy가 가능
        - 처음 호출 되었을때 동적으로 bytecode를 생성하여 이후 호출에서는 재사용한다.
    - JDK Proxy(Reflection)
        - 인터페이스에 대한 Proxy만을 지원
        - JVM에 의하여 Intercept한 다음 invoke 메서드를 호출할 때 JDK의 reflection을 이용하여  호출
        - Proxy를 사용할 때 실행속도를 저하시키는 원인
- Spring배치와 스케줄러란?
    - 스프링 배치
        - 배치는 일괄처리 라는 의미이다. 그리고 스프링에서 배치 작업단위를 Job이라고 부른다. 스프링에서는 배치 작업이 원활하게 진행되도록 관련기능을 제공한다. 대용량 배치와 트랜잭션 기능을 간단하게 구현할 수 있다.
        
    - Quartz 스케줄러
        - 스케줄러란 단순히 잡을 특정 시간마다 실행되도록 도와주는 프로그램을 의미한다. Quartz스케줄러는 크게 3가지로 이루어져 있다.
            - 실행하고자 하는 Job
            - job의 실행 주기를 나타내는 trigger
            - 트리거들을 스케줄러로 만드는 scheduler
        - 사용방법
            - pom.xml에 관련 dependency추가
            - job으로 batch 작업을 진행할 서비스 구현
            - context.xml 에 job을 정의할 jobDetailFactoryBean,jobDetail과 연결해 실행주기를 정의할 cronTriggerFactoryBean, 트리거를 스케줄러로 생성해줄 SchedulerFactoryBean 3가지를 설정한다.
        
    - 스프링 스케줄러
        - 스프링 3.1버전 부터 스프링에서 제공해주는 스케줄러이다. Quartz보다 스케줄러를 디테일하게 사용하도록 하진 않지만 구현이 매우 간단하다.
            - xml파일에 스케줄러 설정
                - xml파일 상위 xmlns 설정
                - <context-component-scan /> 설정
                - <task: scheduler id=’스케줄러id’ /> 설정 -job으로 작업할 서비스를 스케줄러로 설정
                - <task:scheduler ref=’스케줄러id’ /> 설정 -job 실행주기 설정
                - <task:annotation-driven scheduler = ‘스케줄러 id’ />
            - 어노테이션 방법
                - xml파일 상위에 xmlns설정
                - <context-component-scan /> 설정
                - xml 파일에 <task:annotation-driven /> 설정 추가
                - job으로 사용될 서비스 메서드명에 @Scheduler(cron설정) 추가
                
                참고 
                
                [https://www.youtube.com/watch?v=_nkJkWVH-mo&list=PLgXGHBqgT2TtGi82mCZWuhMu-nQy301ew&index=16&ab_channel=%EC%9A%B0%EC%95%84%ED%95%9CTech](https://www.youtube.com/watch?v=_nkJkWVH-mo&list=PLgXGHBqgT2TtGi82mCZWuhMu-nQy301ew&index=16&ab_channel=%EC%9A%B0%EC%95%84%ED%95%9CTech)
                
- Spring 생명주기에 대해 설명
    - 생명주기 언제 생성되고 언제 소멸되는가?
        - Spring 프레임워크에서 지원해주는 인터페이스 구현하는 방법과 bean 객체에 속성을 추가하는 방법이 있다.
        - DB인증 등의 어떤 절차의 인증이 필요할 때 사용
    
    - 스프링 컨테이너 생명주기
        - 컨테이너 생성 시점은 bean 객체 생성 시점과 같다고 볼 수 있다.
        - 생성 : new 객체로 컨테이너 생성,
        - 소멸 : 컨테이너.close() 해주는 시점, 이 때 컨테이너 안에 있던 bean 객체도 같이 소멸
        
    - bean 객체 생명주기
        - 객체 생성 - 초기화 - 사용 - 소멸
        - 스프링 컨테이너와 같다.
- Spring 버전 별 특성에 대해서 설명
    
    ### Spring 3.2.X
    
    - `Java 5`의 기능(제네릭, 가변 매개변수 등)을 사용하여 개정되었다.
        - 이로 인해서 `BeanFactory` 등 핵심 API가 업데이트 되었다.
    - `@Async` 주석을 통해 비동기 메서드 호출을 지원하기 시작했다.
    - 하나의 `Spring.jar`로 제공하던 것을 여러 `Spring` 모듈의 `jar` 파일로 나누어 제공하기 시작했다.(ex : `spring-core`, `spring-web` 등)
    - `SPEL(Spring Expression Language)` 가 도입되어 `XML`및 `Annotation` 기반 `Bean`정의에서 사용할 수 있게 되었다.
        - 이로 인해서 외부 프로퍼티 파일이나 환경변수에서 값을 가져오기 쉬워졌다.
    - `Java` 클래스로부터 `@Configuration`, `@Bean` 등의 `Annotation`을 사용해서 직접 메타 데이터를 설정하고, DI 지원을 받을 수 있다.
    - `OXM(Object Xml Mapping)`을 사용하여 `Bean`을 `XML`형태로 관리할 수 있게 되었다.
    - `Rest API` 에 대한 지원이 추가되었다.
        - 서버로서는 기존 `MVC Framework` 레벨에서 `Annotation` 기반 확장이 추가되었다.
        - 클라이언트로서는 `RestTemplate` 을 추가해 지원한다.
    - `H2`등의 `Embeded Database`를 지원한다.
    - 2016년 12월 31일부로 개발 및 지원이 종료되었다.
    
    ### Spring 4.3.X
    
    - `Java 8` 기능을 완전히 지원하기 시작하였다.
        - `Java 6`, `Java 7` 의 고유 기능들에 대해서도 각각 지원한다.
    - `Starter Pack`의 등장으로 초기 설정이 보다 용이해졌다.
    - `Groovy` 를 통한 `Bean` 설정이 가능하다.
    - `Core Container` 들의 기능 지원이 확대되었다.
        - 예를 들어, `Spring Data Repository` 를 사용하고 있다면 간단한 구현으로 주입할 수 있다. (`@Autowired Repository<Customer> customerRepository`)
        - `meta-annotation` 지원과 함께 `custom-annotation` 을 만들 수 있다.
        - `Bean` 관리가 더 용이해졌다.
            - `@Order` 어노테이션을 통해 배열과 리스트 형태의 `Bean`을 정렬 할 수 있다.
            - `@Lazy` 어노테이션을 통해 `Lazy Injection`이 가능하다.
    - `@RestController` 등 Web 개발 도구의 지원이 강화되었다.
    - `WebSocket`이나 `STOMP` 등의 프로토콜을 지원하여 양방향 통신이 가능하다.
    - 테스트 환경이 개선되어 `Framework` 레벨에서 테스트 유틸리티를 지원한다.(ex. `AopTestUtils`, `ReflectionTestUtils(개선)`)
    - 2020년 12월 31일부로 개발 및 지원이 종료될 예정이다.
    
    ### Spring 5.X
    
    - 전체 프레임워크가 `Java 8` 을 기반 소스코드로 삼으며, 제네릭과 람다 등을 통해 가독성이 향상 되었다.
    - `JDK 9`와도 완벽 호환된다.
    - `Jackson 2.9`, `Protobuf 3`, `Reactor 3.1`과의 호환 추가
    - `Spring WebFlux` 추가, 비동기와 넌-블로킹 이벤트 루프 모델 사용 가능
    - `Kotlin` 지원
    - `Junit 5` 지원
    - `5.0.x` 버전은 2020년 10월까지 지원되며, `5.1.x` 버전과 `5.2.x` 버전은 각각 2020년 10월, 2021년 말까지 활발히 개발될 것이다. `5.3.x` 버전은 알파버전으로, 2024년까지 지원이 제공된다.
- IoC와 DI에 대해 설명
    - DI (Dependency Injection)
        - **스프링이 다른 프레임워크와 차별화되어 제공하는 의존 관계 주입 기능**으로,**객체를 직접 생성하는 게 아니라 외부에서 생성한 후 주입 시켜주는 방식**이다.
        - **DI(의존성 주입)를 통해서 모듈 간의 결합도가 낮아지고 유연성이 높아진다.**
            - 첫번째 방법은 A객체가 B와 C객체를 New 생성자를 통해서 직접 생성하는 방법
            - 두번째 방법은 **외부에서 생성 된 객체를 setter()를 통해 사용하는 방법**이다.
    
    - IoC(Inversion of Control)
        - 메서드나 객체의 호출작업을 개발자가 결정하는 것이 아니라, 외부에서 결정되는 것
        - 객체의 의존성을 역전시켜 객체 간의 결합도를 줄이고 유연한 코드를 작성할 수 있게 하여 가독성 및 코드중복,유지보수를 편하게 할 수 있게 한다.
        - 기존 순서
            - 객체생성 → 의존성 객체 생성(클래스 내부에서 생성) → 의존성 객체 메서드 호출
        - 스프링 순서
            - 객체생성 → 의존성 객체 주입(스스로가 만드는것이 아닌 제어권을 스프링에게 위임하여 스프링이 만들어 놓은 객체를 주입) → 의존성 객체 메서드 호출
- Container란?
    - 인스턴스 생명주기를 관리하며, 생성된 인스턴스들에게 추가적인 기능을 제공하도록 하는 것
    - 객체의 생성과 소멸을 컨트롤
    
    ### Servlet Container
    
    - 웹서버와 통신하기 위하여 소켓을 생성하고, 특정 포트에 리스닝하고, 스트림을 생성하는 등의 복잡한 일들을 할 필요가 없게 해준다.
    - servlet의 생성부터 소멸까지의 일련의 과정(Lifer Cycle) 관리
    - 대표적인 Servlet Container - Tomcat
    
    ### Spring Container
    
    - 자바 객체를 담고 있다.
    - 언제든지 스프링 컨테이너로부터 객체를 가져와 사용할 수 있다.
    - Bean들의 생명주기 관리
    - Spring Container는 어플리케이션을 구성하는 Bean들을 관리하기 위해 IoC 사용
- Service, Controller , Repository Annotation의 차이점
    - Component
        - Spring에서 관리되는 객체임을 표시하기 위해 사용되는 가장 기본적인 어노테이션이다. 즉 scan-auto-detection 과 dependency injection을 사용하기 위해 사용되는 가장 기본 어노테이션
    - Controller
        - Web MVC 코드에 사용되는 어노테이션 @RequestMapping 어노테이션을 해당 어노테이션 밑에서만 사용할 수 있다.
    - Repository
        - 다 알고 있듯이 data repository를 나타내는 어노테이션이다. Repository는 플랫폼 특정 exception을 잡아 Spring의 unchecked exception으로 뱉어내준다.
    - Service
        - 비즈니스 로직이나 repository layer 호출하는 함수에 사용된다. 다른 어노테이션과 다르게 Component에 추가된 기능은 없다.
        
        ### **일반적으로 컴포넌트 클래스들에 @Component를 붙일 수 있지만, @Repository, @Service, @Controller를 붙인다면 도구들이 클래스들을 처리하는데 더 적합하도록 할 수 있고 관점(aspects)에 더 연관성을 부여할 수 있다. - AOP 를 통한 처리가 쉽게 가능하다**
        
- 서비스와 컴포넌트의 차이
    - @Component는 어떤 스프링이 관리하는 컴포넌트를 나타내는 일반적인 스테레오 타입이다.
        
        좀더 세부적인 유스 케이들을 위하여 @Component의 구체화된 형태로 @Repository, @Service,  @Controller들이 있다.
        
    - 컴포넌트 클래스들에 @Component를 붙일 수 있지만, @Repository, @Service, @Controller를 붙인다면  도구들이 클래스들을 처리하는데 더 적합하도록 할 수 있고 관점(aspects)에 더 연관성을 부여할 수 있다.
    
- ControllerAdvice란?
    
    @ControllerAdvice는 클래스의 경로를 검색해서 오류를 캐치할 구현 클래스를 만들게 도와준다. 일반적으로 @Controller 또는 @RestController가 선언된 클래스들에서 발생한 예외를 감지하고 적절한 응답을 만들어 낼 때 사용한다.
    

## DB

- 아이솔레이션 레벨이란?
    - 트랜잭션 격리수준이란 동시에 여러 트랜잭션이 처리될 때 , 트랜잭션끼리 얼마나 서로 고립되어 있는지를 나타내는 것이다.
    - 특정 트랜잭션이 다른 트랜잭션에 변경한 데이터를 볼 수 있도록 허용할지 말지를 결정한다.
    - 트랜잭션 격리 수준
        - READ UNCOMMITTED
            - 각 트랜잭션에서의 변경내용이 COMMIT이나 ROLLBACK 여부와 상관없이 다른 트랜잭션 값을 읽을 수 있다.
            - 정합성에 문제가 많은 격리수준 이기 떄문에 사용하지 않는것을 권장
            - COMMIT이 되지 않는 상태여도 Update된 값을 다른 트랜잭션에서 읽을 수 있다.
                - DIRTY READ현상 발생
                    - 트랜잭션이 작업이 완료되지 않았는데도 다른 트랜잭션에서 볼 수 있게 되는 현상
        - READ COMMITTED
            - RDB에서 대부분 기본적으로 사용되고 있는 격리 수준이다.
            - Dirty Read와 같은 현상은 발생하지 않는다.
            - 실제 테이블 값을 가져오는 것이 아니라 Undo영역에 백업된 레코드에서 값을 가져온다.
                - 하나의 트랜잭션내에서 똑같은 SELECT 쿼리를 실행했을 때는 항상 같은 결과를 가져와야하는 REPEATABLE READ 의 정합성에 어긋난다.
                - 데이터의 정합성은 깨지고, 버그는 찾기 어려워진다 (주로 금전적 처리에서 발생)
        - REPEATABLE READ
            - MYSQL에서는 트랜잭션마다 트랜잭션 ID를 부여하여 트랜잭션 ID보다 작은 트랜잭션 번호에서 변경한 것만 읽게 된다.
            - Undo 공간에 백업해두고 실제 레코드 값을 변경한다.
                - 백업된 데이터는 불필요하다고 판단하는 시점에 주기적으로 삭제한다.
                - Undo에 백업된 레코드가 많아지면 MYSQL 서버의 처리 성능이 떨어질 수 있다.
                - 이러한 변경방식은 MVCC(Multi Version Concurrency Control) 라고 부른다.
                    - PHANTOM READ
                        - 다른 트랜잭션에서 수행한 변경 작업에 의한 레코드가 보였다 안보였다 하는 현상
                        - 이를 방지하기 위해서는 쓰기 잠금을 걸어야한다.
        - SERIALIZABLE
            - 가장 단순한 격리 수준이지만 가장 엄격한 격리수준
            - 성능 측면에서는 동시 처리성능이 가장 낮다.
            - PHANTOM READ가 발생하지 않는다. 하지만 거의 사용하지 않는다.
- 만약 내가 만든 서비스가 데이터조회에 대한 요청보다 데이터를 저장하는 요청이 많다고 가정할때 이것에 대한 퍼포먼스를 향상시키기 위해서 DB관점에서 어떤방식으로 풀어나아갈 것인가?
    
    여러개를 한꺼번에 모아서 저장한다..?
    
- 위의 질문에서 DB접근을 반드시 해야하는 경우라면 DB에 어떤 기능을 사용할것인가?
- DB의 Transaction 의 개념과 특징
    
    **트랜잭션이란?**
    
    데이터베이스의 상태를 변경시키기 위해 수행하는 작업 단위이다. 예를들어 SELECT, UPDATE, INSERT, DELETE 와 같은 행동을 말한다.
    
    **트랜잭션의 특징 4가지** (ACID: ****데이터베이스 트랜젝션이 안전하게 수행된다는 것을 보장하기 위함)
    
    - 원자성(Atomic): 트랜잭션 내에서는 모든 연산이 모두 완료되거나 모두 실패하거나 둘 중 한 가지 상태를 보증한다. (어떤 이유로든 시도하는 변경 내역이 실패하면 전체 연산은 중단되고 마치 아무런 변경사항도 없는 것처럼 보인다.)
    - 일관성(Consistent): 데이터베이스가 변경되면 처리결과가 유효하며 일관된 상태로 유지된다.
    - 독립성(Isolation): 여러 트랜잭션이 간섭 없이 동시에 작동할 수 있다. 이는 어떤 트랜잭션 중에 이뤄진 모든 중간 상태 변경이 다른 트랜잭션에 보이지 않게 하는 방법으로 달성된다.
    - 영속성(Durable): 일단 트랜잭션이 완료되고 나면 시스템 오류가 발생하는 상황에서도 데이터가 손실되지 않고 영구적으로 반영됨을 보장한다.
    
    **트랜잭션 제어를 위한 명령어**
    
    - Commit: 모든 부분작업이 정상적으로 완료하면 이 변경사항을 한꺼번에 DB에 반영한다.
    - SavePoint: 현재까지의 트랜잭션을 특정 이름으로 지정한다.
    - Rollback: 부분 작업이 실패하면 트랜잭션 실행 전으로 되돌린다. SAVEPOINT가 있으면 그 위치까지 되돌아간다.
    
- DB와 통신을 위해 SQL을 다뤘을텐데 DML이란?
    
    **DML이란?**
    
    Data Manipulation Language, 데이터 조작어, 테이블의 행과 열을 조작하는 언어 (ex. SELECT, INSERT, UPDATE, DELETE)
    
    **DDL이란?**
    
    Data Definition Language, 데이터 정의어, 데이터 생성, 수정, 삭제 등 데이터의 전체 골격을 결정하는 언어 (ex. CREATE, ALTER, DROP, TRUNCATE)
    
    **DCL이란?**
    
    Data Control Language, 데이터 제어어, DB에 접근하거나 객체에 권한을 주는 등의 역할을 하는 언어 (ex. GRANT, REVOKE, COMMIT, ROLLBACK)
    
- 파티셔닝이란?
    
    큰 table이나 index를, 관리하기 쉬운 partition이라는 작은 단위로 물리적으로 분할하는 것
    
- 파티셔닝의 장/단점과 종류
    
    **장점**
    
    데이터 검색시 필요한 부분만 탐색하고 파티션 단위로 I/O 분산 및 백업/복구가 가능함으로 **성능이 증가**한다. 또한 전체 데이터가 분산관리되어짐으로 전체 데이터가 한번에 손실 될 가능성이 적어 **가용성이 향상**된다.
    
    **단점**
    
    테이블간 JOIN에 대한 비용이 증가하고 테이블과 인덱스를 별도로 파티셔닝 할 수 없다. 데이터를 입렵받았을 경우 어디에 넣어야 하는지에 대한 연산 오버헤드가 발생 할 수 있다.
    
    **파티셔닝의 종류**
    
    - **수평(horizontal) 파티셔닝**
        - **Row 단위로 자른다.** 즉 하나의 큰 테이블을 같은 스키마를 가지는 여러개의 작은 테이블로 나누는 것이다.
        - Schema를 복제한 후 샤드키를 기준으로 데이터를 나눈다.
    - **수직(vertical) 파티셔닝**
        - **특정 컬럼을 기준으로 쪼개서 저장하는 형태**이다. RDBS에서 제 3정규와 비슷한 개념이나, 파티셔닝은 이미 정규화 된 데이터를 분리하는 과정이다.
        - 자주 사용하는 컬럼 등을 분리시켜 성능을 향샹 시킬 수 있다.
    
- DB조인 종류
    
    **조인이란?**
    
    여러 테이이블에 흩어져 있는 정보 중 사용자가 필요한 정보만 가져와서 가상의 테이블처럼 만들어서 결과를 보여주는 것으로 2개의 테이블을 조합하여 하나의 열로 표현하는 것
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/64f0ab7c-f51f-4387-a4b6-d36a1af55a1d/Untitled.png)
    
    **조인의 종류**
    
    - Inner Join
        
        조인이 되는 키를 기준으로 둘 이상의 테이블에 존재하는 데이터를 조회하는 것(교집합). Null인 데이터는 포함되지 않는다.
        
    - Outer Join
        
        두테이블에서 지정된 쪽(Left or Right or Full)의 모든 결과를 보여주면서 반대쪽에 매칭되는 쪽까지 보여주는 것(합집합). Null값까지 포함한다.
        
    - Cross Join (카테시안 곱)
        
        Join 조건절을 아무것도 적지 않거나 조건을 잘못 기술 했을 때 모든 데이터를 가져오게 되는 현상
        
    - Natural Join
        
        데이터베이스 내부적으로 두 테이블에서 동일한 컬럼명으로 데이터가 일치하는 결과값을 표현한다.
        
    - Self Join
        
        외부 테이블이 아닌 하나의 테이블을 중복으로 사용하여 두 테이블간의 연관관계를 표현한다.
        
- Left Join과 Left Outer Join의 차이
    
    OUTER를 생략하여 LEFT JOIN 으로 줄여쓴다. 결론적으로 LEFT JOIN과  LEFT OUTER JOIN은 완전히 동일합니다.
    
- Inner Join과 Outer Join 차이
    
    A 와 B에 대한 Inner Join은 A와 B의 교집합을, Outer Join은 A와 B의 합집합을 조회하게 된다.
    
- RDB와 NoSQL의 차이
    
    **RDBMS**
    
    RDB(Relational Database): 관계형 데이타 모델에 기초를 둔 데이타베이스. 관계형 데이타 모델이란 데이타를 구성하는데 필요한 방법 중 하나로 모든 데이타를 2차원의 테이블 형태로 표현해준다. 데이타의 독립성이 높고, 고수준의 데이타 조작언어(DML)을 사용하여 결합, 제약, 투영 등의 관계 조작에 의해 비약적으로 표현능력을 높일 수 있다. 또한 이들의 관계 조작에 의해 자유롭게 구조를 변경할 수 있다.
    
    - 데이터의 관계를 Foreign Key 등으로 정의하고 이를 이용해 Join 등의 관계형 연산을 함
    - 하나의 고성능 머신에 데이터 저장 (수직적 확장)
    - 테이블 스키마 변경 불가
    - 대부분의 데이터베이스에서 안정적으로 사용 가능
    
    **NOSQL(Not Only SQL)**
    
    데이터베이스는 기존의 관계형 데이터베이스보다 더 융통성있는 데이터 모델을 사용하고 데이터의 저장 및 검색을 위한 특화된 메커니즘을 제공 합니다. 이를 통해 NoSQL 데이터베이스는 단순 검색 및 추가작업에 있어서 매우 최적화된 키 값 저장 기법을 사용하여 응답속도나 처리효율 등에 있어서 매우 뛰어난 성능을 나타냅니다.
    
    - 데이터 간의 관계를 정의하지 않음
    - 일반적인 서버 수십 대를 연결해 데이터를 저장 및 처리하는 구조 (수평적 확장)
    - 테이블 스키마 유동적
    - 대용량 데이터 처리에 좋음
    
- DB와 File System의 차이
    
    **파일시스템**
    
    각각의 어플리케이션이 독립적으로 자료를 파일형태로 배치하고 관리하는, 전통적인 데이터 처리 시스템. 대부분의 경우 데이터 파일과 어플리케이션이 1:1로 대응되는 특징을 가지고 있다. 따라서 응용프로그램과 data 간에 상호 의존성, 종속성이 높다. 데이터의 보안, 공유, 중복성, 무결성문제가 있다.
    
    **데이터베이스**
    
    데이터베이스는 어떤 일에 관련되거나 필요한 데이터들의 집합을 말하며 이를 관리하기위한 프로그램이 DBMS(data base management system) 데이터베이스 관리 시스템이다. 각자의 컴퓨터로 개별적으로 응용프로그램을 유지하고, 데이터는 단일의 데이터베이스에 저장되어 관리되므로 파일 시스템의 보안, 공유, 중복성, 무결성문제를 해소할 수 있다.
    
- 플러시를해도 DB에 바로 반영되지 않는 이유
    
    플러시는 영속성 컨텍스트의 변경 내용을 데이터베이스에 동기화하는 작업인데 이때 쓰기 지연 SQL 저장소에 모인 쿼리를 데이터베이스에 보낸다. 이렇게 영속성 컨텍스트의 변경 내용을 데이터베이스에 동기화한 후에 실제 데이터베이스 트랜잭션을 커밋한다. flush가 먼저 동작하고 (데이터베이스에 동기화한 후에) 실제 데이터베이스 트랜잭션을 커밋하는 것이다. 즉, 커밋이 시행되어야 실제 db에 반영이 되는 것이다.
    
    **플러시의 동작과정**
    
    1. 영속성 컨텍스트에서 변경을 감지한다. (Dirty Checking) 
    2. 연속성 컨텍스트의 엔티티와 스냅샷 비교하여 수정된 엔티티 조회한다.
    3. 수정된 Entity를 쓰기 지연 SQL 저장소에 등록한다. 
    4. 쓰기 지연 SQL 저장소의 Query를 DB에 전송한다. (등록, 수정, 삭제 Query)
- RDS의 특징 설명
    
    **AWS에 RDS를 구성하는 방법**
    
    - 관리형 서비스인 아마존 RDS를 이용
        
        RDS(Relational Database Service): 클라우드에서 관계형 데이터베이스를 간편하게 설정, 운영, 확장이 가능하도록 지원하는 웹 서비스. 데이터베이스 소프트웨어 패치, 데이터베이스 백업 혹은 시점 복구 활성화와 같은 복잡한 관리 프로세스들을 자동으로 관리할 수 있다.  또한 스토리지와 iops(단위 시간당 읽기/쓰기 횟수) 확장이 용이하다.
        
    - EC2인스턴스에 RDBMS를 직접 설치
        
        직접 DB서버를 설치 및 관리하는 것으로 local 서버 환경을 AWS의 가상환경으로 옮긴 것 이외에는 크게 차이점이 없다. 그러므로 OS와 RDBMS를 자유롭게 선택하고 설정할 수 있는 장점이 있다. 하지만 OS와 DB환경을 사용자가 직접 관리해줘야 하는 부담이 있다. 인프라 운영을 위한 어플리케이션, 제대로 설계된 자동화 그리고 데이터베이스 전문 관리 팀이 있는 기업의 경우 RDS가 꼭 필요하지 않을 수 있다.
        
    
    (add. RDS와 EC2를 연동하는 목적: 서버와 DB를 분리하는 방식으로 하나의 서버가 고장이 나도 즉시 다른 서버를 새로 추가하여 교체가능하여 DB의 정보가 손상될 위험이 적다. )
    
- 스키마란 무엇인가?
    
    데이터베이스의 구조와 제약조건에 대한 명세
    
    - 외부 스키마 : 사용자나 응용프로그래머 관점에서 데이터베이스의 논리적 구조를 정의해 놓은 것.
    - 개념 스키마 : DB 전체적인 논리적 구조
    - 내부 스키마 : DB 전체적인 물리적 구조 , DBA가 관리한다.
- MySQL 의 WHERE 와 Having의 차이
    
    where은 기본적인 조건절로서 우선적으로 모든 필드를 조건에 둘 수 있다. 하지만 having은 group by 된 이후 특정한 필드로 그룹화 되어진 새로운 테이블에 조건을 줄 수 있다.
    
    ```css
    **select** **from** 테이블명 **where** 조건절
    ```
    
    ```css
    **select** **from** 테이블명 **group** **by** 필드명 **having** 조건절
    ```
    
- SQL Injection이란
    
    보안상의 취약점을 이용하여, 임의의 SQL 문을 주입하고 실행되게 하여 데이터베이스가 비정상적인 동작을 하도록 조작하는 공격.
    
    입력 값에 대한 검증, Prepared Statement 구문사용, Error Message 노출 금지, 웹 방화벽 사용과 같은 조치로 대응할 수 있다.
    
- Index란
    
    추가적인 쓰기 작업과 저장 공간을 활용하여 데이터베이스 테이블의 검색 속도를 향상시키기 위한 자료구조.
    
    테이블을 조회하는 속도와 그에 따른 성능을 향상시키고 전반적인 시스템의 부하를 줄일 수 있다.
    
    - 규모가 작지 않은 테이블
    - INSERT, UPDATE, DELETE가 자주 발생하지 않는 컬럼
    - JOIN이나 WHERE 또는 ORDER BY에 자주 사용되는 컬럼
    - 데이터의 중복도가 낮은 컬럼
    
    등에 적합하다.
    
- Statement, PrepareStatement 차이
    
    가장 큰 차이점은 캐시(cache) 사용여부이다.
    
    1) 쿼리 문장 분석
    
    2) 컴파일
    
    3) 실행
    
    Statement를 사용하면 매번 쿼리를 수행할 때마다 1) ~ 3) 단계를 거치게 되고, PreparedStatement는 처음 한 번만 세 단계를 거친 후 캐시에 담아 재사용을 한다. 만약 동일한 쿼리를 반복적으로 수행한다면 PreparedStatment가 DB에 훨씬 적은 부하를 주며, 성능도 좋다.
    
- 효과적으로 쿼리를 저장하는 방법
    1. 순서를 생각하자.
    - 내가 보여주려는 결과는 어느 테이블에 있는지
    - 결과를 뽑기위해 하나의 테이블을 사용하지 않으므로 내가 원하는 결과를 가지고 있는 테이블 나열
    - 나열된 테이블 중 주테이블이 무엇인지
    - 원하는 결과의 값들은 무엇이 있는지
    1. Form부터 풀자.
- Replication이란?
    
    물리적으로 다른 두 대 이상의 DBMS를 나눠서 동일한 데이터를 저장하는 방식. 예를들어 Master 서버를 데이터의 원본서버, Slave서버를 백업서버로 지칭한다. 기본적으로 데이터 안정성을 목적으로 하고, Slave Database를 생성하여 Query의 대부분인 Select 수행의 부하를 낮춤으로써  Read(Select) 성능 향상 효과를 얻을 수 있다. 데이터의 억세스 시간이 중요한 읽기쓰기 SQL 작업은 마스터 서버에 접속하여 수행하고, 데이터의 억세스 시간이 중요하지 않는 ‘읽기전용’ 작업은 리플리카 서버에 접속하여 수행하도록 한다.
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/70955e1f-66cd-409e-9f69-9bd883ff5fe2/Untitled.png)
    
- 샤딩 이란?
    
    **수평적 파티셔닝**의 한 종류로 수평적 파티셔닝과 비교하여 다른점은 파티셔닝은 단일 DBMS내에서의 데이터 분할 정책이고, 샤딩은 분할된 여러 데이터베이스 서버로 데이터를 분할하는 방법이다. 샤딩은 인덱스의 크기를 줄이고, 작업 동시성을 늘린다. 샤딩을 구성하게되면 샤드의 수만큼 노드가 존재하며, 서버가 여러대 존재하므로 부하를 적절히 분산할 수 있는 장점이 있다.
    
    (수평적 파티셔닝이란 스키마(schema)가 같은 데이터를 두 개 이상의 테이블에 나누어 저장(컬럼이 아닌 데이터기준으로 분할)하는 디자인을 말한다. )
    
    **해시 샤딩(Hash Sharding):** 해시 함수를 사용해 샤드키를 나누는 방식
    
    **다이나믹 샤딩(Dynamic Sharding):** Locator Service를 통해 샤드키를 구성하는 방식
    
    **Entity Group:** 관계가 되어있는 엔티티를 같은 샤드내에 구성하는 방식
    
    (샤드키'는 나눠진 샤드 중 어떤 샤드를 선택할 지 결정하는 키로, 샤드키 결정 방식에 따라 샤딩 방법이 나뉘게 된다.)
    
- Storage Enigne 이란?
    
    **데이터베이스 엔진**(database engine) 또는 **스토리지 엔진**(storage engine)은 [데이터베이스 관리 시스템](https://ko.wikipedia.org/wiki/%EB%8D%B0%EC%9D%B4%ED%84%B0%EB%B2%A0%EC%9D%B4%EC%8A%A4_%EA%B4%80%EB%A6%AC_%EC%8B%9C%EC%8A%A4%ED%85%9C)(DBMS)이 데이터베이스에 대해 데이터를 삽입, 추출, 업데이트 및 삭제(CRUD 참조)하는 데 사용하는 기본 소프트웨어 컴포넌트이다. 데이터베이스 엔진을 조작할 때 DBMS 고유의 사용자 인터페이스를 이용하는 방법과 포트 번호를 통해하는 방법이 있다. 대부분의 데이터베이스 관리시스템은 DBMS 의 사용자 인터페이스를 통하지 않고, 사용자가 내장된 엔진과 상호작용을 할 수 있는 자신만의 [애플리케이션 프로그래밍 인터페이스](https://ko.wikipedia.org/wiki/%EC%95%A0%ED%94%8C%EB%A6%AC%EC%BC%80%EC%9D%B4%EC%85%98_%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D_%EC%9D%B8%ED%84%B0%ED%8E%98%EC%9D%B4%EC%8A%A4)(API)를 포함하고 있다.
    
    - 서버 엔진이 필요한 물리적인 데이터를 가져오는 장치
    - 
    
    ![https://media.vlpt.us/images/junseokoo/post/728495a8-408d-41d9-909a-423606d249d4/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-01-03%2003.39.37.png](https://media.vlpt.us/images/junseokoo/post/728495a8-408d-41d9-909a-423606d249d4/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-01-03%2003.39.37.png)
    

## JPA

- ORM이란?
    
    Object Relational Mapping, 객체-관계 매핑, 객체와 관계형 DB의 데이터를 자동으로 매핑(연결)해주는 것.
    
    객체 지향 프로그래밍은 클래스를 사용하고, 관계형 데이터베이스는 테이블을 사용한다. 이때 객체 모델과 관계형 모델 간에 불일치가 존재하게되는데 ORM을 통해 객체 간의 관계를 바탕으로 SQL을 자동으로 생성하여 불일치를 해결한다.
    
    **ORM의 장점**
    
    객체 지향적인 코드로 인해 더 직관적이고 비즈니스 로직에 더 집중할 수 있게 도와준다.
    
    재사용 및 유지보수의 편리성이 증가한다.
    
    DBMS에 대한 종속성이 줄어든다.
    
- JPA란?
    - Java 진영에서 ORM(Object-Relational Mapping) 기술 표준으로 사용하는 인터페이스 모음
    - 자바 어플리케이션에서 관계형 데이터베이스를 사용하는 방식을 정의한 인터페이스
    - 인터페이스 이기 때문에 Hibernate, OpenJPA 등이 JPA를 구현함
- JPA를 사용하였을때 장점
    
    JPA는 반복적인 CRUD SQL을 처리해준다. JPA는 매핑된 관계를 이용해서 SQL을 생성하고 실행하는데, 개발자는 어떤 SQL이 실행될지 생각만하면 되고, 예측도 쉽게 할 수 있다. 추가적으로 JPA는 네이티브 SQL이란 기능을 제공해주는데 관계 매핑이 어렵거나 성능에 대한 이슈가 우려되는 경우 SQL을 직접 작성하여 사용할 수 있다.
    
    JPA를 사용하여 얻을 수 있는 가장 큰 것은 SQL아닌 객체 중심으로 개발할 수 있다는 것이다. 이에 따라 당연히 생산성이 좋아지고 유지보수도 수월하다. 또한 JPA는 패러다임의 불일치도해결하였다.
    
- JPA를 사용하는 이유,
    
    **생산성**
    
    자바 컬렉션에 객체를 저장하듯이 JPA에게 저장할 객체를 전달하면 된다. SQL을 작성하고 JDBC API를 사용하는 반복 행위는 JPA가 대신해 준다.
    
    **유지 보수**
    
    엔티티에 필드를 추가하거나 삭제해도 수정해야 할 코드가 줄어 든다. 특히 이전에 작성하던 SQL과 JDBC API를 JPA가 대신 처리해 준다.
    
    **패러다임 불일치 해결**
    
    JPA는 상속, 연관 관계, 객체 그래프 탐색, 비교 등 패러다임의 불일치를 해결해 준다.
    
    **성능**
    
    JPA 의 성능 최적화 기능 제공
    
    **데이터 접근 추상화와 벤더 독립성**
    
    JPA는 데이터 접근 계층을 제공해서 애플리케이션이 특정 데이터베이스 기술에 종속되지 않도록 한다.
    
    **표준**
    
    JPA는 자바 진영의 ORM 기술 표준이므로 다른 구현 기술로 손쉽게 변경이 가능하다.
    
- JPA, Hibernate, Spring Data JPA 의 차이
    
    **JPA**란 ****자바 ORM에 대한 API 표준 명세이고, 인터페이스의 모음이다. JPA는 말 그대로 인터페이스이고 특정 기능을 하는 라이브러리가 아니다. 자바 어플리케이션에서 관계형 데이터베이스를 어떻게 사용해야 하는지를 정의하는 한 방법일 뿐이다. ****따라서 구현체가 없고, 사용하기 위해서는 ORM프레임워크를 선택해야하는데 그중 가장 대중적인 것이 하이버 네이트이다. 
    
    **Hibernate**는 JPA라는 명세의 구현체이다. 즉, javax.persistence.EntityManager와 같은 인터페이스를 직접 구현한 라이브러리이다.
    
    **Spring Data JPA**는 Spring에서 제공하는 모듈 중 하나로, 개발자가 JPA를 더 쉽고 편하게 사용할 수 있도록 도와준다. 이는 JPA를 한 단계 추상화시킨 Repository라는 인터페이스를 제공함으로써 이루어진다. Spring Data JPA가 JPA를 추상화했다는 말은, Spring Data JPA의 Repository의 구현에서 JPA를 사용하고 있다는 것이다.
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c1a1462c-151a-4d3d-8774-133c41e79ad0/Untitled.png)
    
- 패러다임의 불일치를 해결해준다는 것은 어떤 의미인가?
    
    어플리케이션이 발전하면서 내부의 복잡성은 커짐.
    
    **객체지향 프로그래밍**은 추상화, 캡슐화, 정보은닉, 상속, 다형성 ****등 시스템의 복잡성을 제어할 수 있는 다양한 정치들을 제공. **관계형 데이타베이스**는 데이터 중심으로 구조화, 집합적인 사고 필요. 추상화, 상속 다형성 같은 개념이 없다.
    
    이러한 패러다임이 일치하지 않는 상황에서 객체를 데이터베이스에 저장해야 한다. 이 때문에 객체 지향적으로 코드를 설계하지 못하고 테이블에 맞게 객체를 설계해야 하는데, 이러한 패러다임의 불일치를, 개발자가 객체지향적으로 코드를 설계할수있게끔, JPA를 이용하여 해소 할 수 있다.
    
- 영속성 컨텍스트란?
    
    엔티티 클래스에서 만들어지는 엔티티를 영구 저장하고 관리하는 환경. 애플리케이션과 DB 사이에서 객체를 보관하는 가상의 DB 역할을 한다. Entity Manager를 통해 엔티티를 저장하거나 조회하면, Entity Manager는 영속성 컨텍스트에 엔티티를 보관하고 관리한다.
    
    - 영속성 컨텍스트는 엔티티를 식별자 값(@Id)으로 구분하므로 영속 상태는 식별자 값이 반드시 있어야 한다.
    - 영속성 컨텍스트에 엔티티를 저장할 때 바로 데이터베이스에 저장되는 것이 아니라, 1차 캐시에 엔티티를 생성하고, 쓰기 지연 SQL 저장소에 쿼리문을 생성해서 저장한다. 이렇게 쌓인 쿼리문은 flush( )가 실행될 때 데이터베이스에 반영된다.
- 영속성 컨텍스트에 저장되는것이 Entity인데 Entity의 생명주기에 대해서 설명
    
    ① 비영속(new/transient)
    
    - 엔티티 객체가 만들어져서 아직 저장되지 않은 상태로, 영속성 컨텍스트와 전혀 관계가 없는 상태
    
    ② 영속(managed)
    
    -  엔티티가 영속성 컨텍스트에 저장되어, 영속성 컨텍스트가 관리할 수 있는 상태
    
    ③ 준영속(detached)
    
    - 엔티티가 영속성 컨텍스트에 저장되어 있다가 분리된 상태로, 영속성 컨텍스트가 더 이상 관리하지 않는 상태
    
    ④ 삭제(removed)
    
    - 엔티티를 영속성 컨텍스트와 데이터베이스에서 삭제
    
- DB에서 데이터를 조회할 때 영속성 컨텍스트에서 저장되는 과정 설명
    1. 조회 시 처음 1차 캐시에 해당 데이터가 있는지 탐색을 한다. -> 만약 있으면 바로 리턴
    2. 조회 결과 1차 캐시에 데이터가 없으면 데이터베이스에 접근해 값을 탐색한다.
    3. 탐색 결과를 바로 리턴하는 것이 아닌 다음 탐색에서 재사용할 수 있도록 1차 캐시에 저장한다.
- Pageable
    
    Pageable 인터페이스는 Paging 하기 위한 파라미터들을 담은 PageRequest 같은 객체에 접근하기 위한 역할을 한다. 이 매개변수를 통해 Paging 하기 위한 정보를 담은 객체가 들어오게 되고 이것을 통해 자동적으로 Paging에 필요한 데이터를 처리하여 반환한다.
    
- 역정규화를 하는 이유?
    
    역정규화(=반정규화)란 정규화를 통해 분리되었던 릴레이션을 다시 통합하거나 분할하여 구조를 재조정하는 과정이다.  
    
    디스크 I/O량이 많아 조회 시 성능이 저하 또는 테이블끼리의 경로가 너무 멀어 조인으로 인한 성능 저하가 예상 되거나 , 칼럼을 계산하여 조회할 때 성능이 저하 될 것이 에상되는 경우 반정규화를 수행하게 된다. 일반적으로 조회에 대한 처리 성능이 아주 중요하다고 판단될 때 부분적으로 반 정규화를 고려하게 된다. 
    
    역정규화의 종류로는 릴레이션 역정규화와 속성 역정규화가 있다.
    
- JPA FetchType?
    
    JPA가 하나의 엔티티를 조회할 때 연관관계에 있는 객체들을 어떻게 가져올 것인지를 나타내는 설정값
    
    - Eager 전략
        - 연관관계에 있는 엔티티들을 모두 가져온다
    - Lazy 전략
        - 연관관계에 있는 엔티티를 가져오는 게 아닌 getter로 접근할 때 가져온다
    
    [JPA 의 Fetch Type 과 친해지기](http://jaynewho.com/post/39)
    
- JPA사용할 때랑 직접 SQL을 사용할 때의 차이
    - JPA
        - RDB의 종류에 상관 없이 사용 가능. DB 변경이나 코드 재활용에 용이
        - 기본적인 CRUD 제공과 페이징 처리 등 상당수가 구현되어 있어 비즈니스 로직에 더 집중 가능
        - 테이블 생성, 변경 등 엔티티 관리가 간편
        - SQL에 집중할 필요가 없어 빠른 개발
    - SQL(MyBatis)
        - JPA에 비해 쉬움
        - SQL의 세부적인 내용 변경 시 좀 더 간편
        - 동적 쿼리 사용 시 JPA보다 간편하게 구현 가능
    
    [JPA와 MyBatis의 차이 (ORM과 SQL Mapper)](https://dreaming-soohyun.tistory.com/entry/JPA%EC%99%80-MyBatis%EC%9D%98-%EC%B0%A8%EC%9D%B4-ORM%EA%B3%BC-SQL-Mapper)
    
- ManyToOne을 쓴이유는? 반대편에서 OneToMany를 쓸수 도 있지 않나?
- JPA에서 PK는 어떻게 설정하나요?
    - 직접 할당
        - @Id 어노테이션 사용
    - 자동 생성
        - @GeneratedValue 어노테이션 사용
            - IDENTITY : @GeneratedValue(strategy = GenerationType.IDENTITY) 추가
            - SEQUENCE : @GeneratedValue(strategy = GenerationType.SEQUENCEW) 추가
            - 사용 예시
            
            ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ca190eab-97f7-4bc6-a5c0-16323c6706aa/Untitled.png)
            
    
    [[JPA] 기본 키(PK) 매핑](https://sinau.tistory.com/48)
    
- DTO를 사용하는 이유
    
    실무에서 데이터를 한 번 요청할 때 많은 비용이 든다. 비용을 줄이기 위해 요청 횟수를 줄여야하는데 JAVA에서는 반환 값을 여러개로 할 수도 없다. 이것을 해결하기 위해 요청에 대한 모든 데이터를 DTO에 담아 반환한다.
    
    [DTO란 무엇인가, VO와의 비교](https://kafcamus.tistory.com/13)
    
- N + 1 문제에 대해 설명
    - N+1문제
        - 연관관계가 설정된 엔티티를 조회할 때, 조회된 데이터의 개수만큼 연관관계의 조회 쿼리가 추가로 발생하여 데이터를 읽어오게 된다
    - FetchType을 Eager에서 Lazy로 바꾸면 될까?
        - 아니다. FetchType을 Lazy로 바꾼다고 해도 달라지는 건 없다. 단지 N+1 문제 발생 시점을 연관관계 데이터를 사용하는 시점으로 미룰지, 아니면 초기 데이터 로드 시점에 가져오는지의 차이가 있는 것 뿐이다.
    - N + 1 문제 발생 원인
        - findAll()은 무조건 ‘SELECT * FROM 테이블이름’ SQL만 실행하기 때문에 연관관계 데이터를 무시하고 오로지 해당 엔티티 기준으로 쿼리를 조회한다. 연관된 엔티티 데이터가 필요할 경우, FetchType으로 조회를 별도로 호출하게 된다.
    - 해결 방법
        - 대표적으로는 Fetch join이 있다. 하지만 JpaRepository에서는 제공하지 않아 JPQL을 작성해야 한다.
        - Fetch join에는 단점이 있다. FetchType을 사용할 수 없고, 페이징 쿼리를 사용할 수 없다. 페이징을 사용할 수 없는 이유는 하나의 쿼리로 필요한 모든 데이터를 가져오기 때문에 페이징 단위로 가져오는 것이 불가능하다.
    
    [N+1 문제](https://incheol-jung.gitbook.io/docs/q-and-a/spring/n+1)
    
- Entity를 설계할때 주의할 점
    - 가급적 setter 사용 금지
        - 변경 포인트가 많아 유지보수가 어렵다
    - 모든 연관관계는 지연로딩(FetchType.Lazy)로 설정
        - 즉시로딩(Eager)은 예측이 어렵고 어떤 쿼리가 실행될지 추적하기 어렵다.
    - 컬렉션은 필드에서 초기화
        - 컬렉션은 필드에서 바로 초기화하는 것이 안전한다
        - 하이버네이트는 엔티티를 영속화할 때 컬렉션을 감싸서 하이버네이트가 제공하는 내장 컬렉션으로 변경한다. 만약 get하는 임의의 메소드에서 컬렉션을 잘못 생성하면 하이버네이트 내부 메커니즘에 문제가 발생할 수 있다.
    - 테이블, 컬럼명 생성 전략
        - 스프링부트에서 하이버네이트 기본 매핑 전략을 변경하기 때문에 실제 테이블 필드명과 다르다
        - 하이버네이트 : 엔티티의 필드명 그대로 테이블의 컬럼명으로 사용
        - 스프링 부트 신규 설정 (엔티티(필드) 테이블(컬럼))
            1. 카멜 케이스 언더스코어(memberPoint member_point)
            2. .(점) _(언더스코어)
            3. 대문자 소문자
    - 핵심 비즈니스 로직은 데이터를 가지고 있는 쪽에 구현
        - 객체 지향적인 코드를 위해서
        - getter로 가져와서 변경하는 방식은 응집성을 떨어뜨린다
    
    [[JPA] 엔티티 설계시 주의점](https://velog.io/@haron/JPA-%EC%97%94%ED%8B%B0%ED%8B%B0-%EC%84%A4%EA%B3%84%EC%8B%9C-%EC%A3%BC%EC%9D%98%EC%A0%90)
    

## Java

- 자바의 기본 자료형의 종류
    - 논리 자료형
        - boolean
    - 문자 자료형
        - char
    - 정수 자료형
        - byte, short, int, long
    - 실수 자료형
        - float, double
    
    [[JPA] 엔티티 설계시 주의점](https://velog.io/@haron/JPA-%EC%97%94%ED%8B%B0%ED%8B%B0-%EC%84%A4%EA%B3%84%EC%8B%9C-%EC%A3%BC%EC%9D%98%EC%A0%90)
    
- 객체란 무엇이며 객체 지향이란 무엇인가? (4가지특징과 5대원칙 설명)
    - 객체
        - 클래스에 정의된 내용대로 메모리에 생성된 것
    - 객체지향
        - 프로그래밍에서 필요한 데이터를 추상화시켜 상태와 행위를 가진 객체를 만들고 그 객체들 간의 유기적인 상호작용을 통해 로직을 구성하는 프로그래밍 방법
        - 4가지 특징
            - 추상화
                - 실제 세상을 객체화하는 것이 아닌, 필요한 정보만을 중심으로 간소화하는 것
            - 캡슐화
                - 객체에 필요한 데이터나 기능을 책임이 있는 객체에 그룹화시켜주는 것
            - 상속
                - 상위 클래스의 기능을 하위 클래스에서도 사용할 수 있게 해주는 것
            - 다형성
                - 객체간의 관계를 유연하게 해주는 것
                
                [객체지향 주요특징 4가지](https://youngjinmo.github.io/2021/04/features-of-oop/)
                
        - 5대 원칙
            - 단일 책임 원칙(Single Responsibility Principe)
                - 하나의 클래스는 하나의 책임만 가져야 한다
                - 변경사항이 있을 때, 어플리케이션의 파급 효과가 적으면 SRP 원칙을 잘 따른 것이다
            - 개방 폐쇄 원칙(Open Closed Principle)
                - 높은 응집도와 낮은 결합도
                - 높은 응집도
                    - 하나의 모듈/클래스가 하나의 책임에만 집중되어있다는 뜻
                - 낮은 결합도
                    - 하나의 변경이 발생할 때 다른 모듈과 객체로 변경에 대한 요구가 낮은 상태
            - 리스코프 치환 원칙(Liskov Substitution Principle)
                - 객체는 프로그램의 정확성을 깨지 않으면서 하위 타입의 인터페이스로 바꿀 수 있어야 한다
            - 인터페이스 분리 원칙(Interface Segragation Principle)
                - 범용 인터페이스 하나보다는 특정 클라이언트를 위한 여러 개의 인터페이스 분리가 더 좋다
            - 의존관계 역전 원칙(Dependency Inversion Principle)
                - 프로그래머는 구체화가 아니라 추상화에 의존해야 한다.
                - 인터페이스에 의존하라는 의미이다.
            
            [객체지향 설계 원칙 5가지](https://youngjinmo.github.io/2021/04/principles-of-oop/)
            
- 객체지향을 사용한 이유
    
    객체지향을 사용하면 코드의 중복을 어느정도 높일 수 있고, 코드의 역할 분담을 좀 더 확실하게 할 수 있어서 가독성을 높일 수 있다
    
- 오버로딩과 오버라이딩의 차이
    - 오버로딩(Overloading)
        - 같은 이름의 메소드를 여러 개 가지면서 매개변수의 유형과 개수가 다르도록 정의하는 기술
    - 오버라이딩(Overriding)
        - 상위 클래스가 가지고 있는 메소드를 하위 클래스가 재정의해서 사용하는 기술
    
    [오버로딩과 오버라이딩 차이와 예제](https://private.tistory.com/25)
    
- 기본 생성자는 언제 필요한가?
    
    항상 필요하다. 객체는 생성자 없이 생성이 불가능하다. 생성자를 아무것도 안 적은 채 컴파일을 하면 기본 생성자가 자동으로 생성된다. 사용자 정의 생성자를 만들어줬을 때 기본 생성자를 직접 적어줘야 한다. 컴파일러가 자동으로 생성해주지 않는다.
    
    [](https://zoosso.tistory.com/312)
    
- 형변환이란?
    - 형변환(캐스팅, casting)
        - 변수 또는 상수의 타입을 다른 타입으로 변환하는 것
        - 프로그램에서 값의 대입이나 연산을 수행할 때는 같은 타입끼리만 가능하다. 그래서 연산을 수행하기 전에 같은 타입으로 만들어야 하는데, 변수나 상수를 다른 타입으로 변환하는 것을 ‘형변환’이라고 한다
        - 자동 형변환
            - 개발자가 지정하지 않아도 자동으로 이루어진다
            - 작은 그릇을 큰 그릇에 데이터를 옮겨담아야 손실 없이 그대로 보존된다
                
                ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/df698061-94aa-4b15-8d7a-05a71a31f8c8/Untitled.png)
                
        - 강제 형변환(명시적 형변환)
            - 개발자가 명시해야만 이루어진다
            - 큰 데이터 타입에서 작은 데이터 타입으로 옮길 때 데이터의 손실이 발생할 수도 아닐수도 있다. 데이터의 손실이 일어난다면 정확한 연산을 할 수없기 때문에 강제 형변환 시 주의해야 한다.
        
        [](https://keep-cool.tistory.com/14)
        
- Static이란?
    - static 키워드 사용
        - 메모리에 한 번 할당되어 프로그램이 종료될 때 해제되는 것
        - 우리가 만든 클래스는 메모리 중 static 영역에 생성되고, new 연산자를 통해 생성한 객체는 heap 영역에 생성된다
        - heap 영역의 메모리는 garbage collector를 통해 수시로 관리를 받는다
        - static 영역의 메모리는 모든 객체가 공유하는 메모리라는 장점을 갖지만, garbage collector의 관리 영역 밖이기 때문에 static을 자주 사용하면 프로그램의 종료 시까지 메모리가 할당된 채로 존재하므로 시스템에 악영향을 주게 된다
        - static 변수
            - 메모리에 고정적으로 할당되어, 프로그램이 종료될 때 해제되는 변수
            - 메모리에 한 번 할당되므로 여러 객체가 해당 메모리를 공유하게 된다.
        - static 메소드
            - 객체의 생성 없이 호출이 가능하고, 객체에서는 호출이 불가능하다
            - 예: java.util.Math
    
    [[java/자바] Static 이란? Static 정리](https://mi-nya.tistory.com/251)
    
- 참조자료형이란?
    - 주소를 가지고 있는 변수
    - 기본 자료형을 제외한 나머지 타입은 모두 참조 자료형 변수이다
    - 참조 자료형은 객체의 주소를 저장한다
    
    [자바 ! 변수 (기본자료형, 참조자료형, 자료의 형변환)](https://programmingyoon.tistory.com/3)
    
- 어노테이션이란?
    - 어노테이션
        - 자바에서 사용될 때의 어노테이션은 코드 사이에 주석처럼 쓰여서 특별한 의미/기능을 수행하도록 하는 기술이다. 즉, 프로그램에게 추가적인 정보를 제공해주는 메타데이터(meta data: 데이터를 위한 데이터)라고 볼 수 있다
    - 어노테이션의 용도
        - 컴파일러에게 코드 작성 문접 에러를 체크하도록 정보 제공
        - 소프트웨어 개발툴이 빌드나 배치 시 코드를 자동으로 생성할 수 있도록 정보 제공
        - 실행 시(런타임 시) 특정 기능을 실행하도록 정보 제공
    
    [Java에서 어노테이션(Annotation) 이란 무엇인가에 대해 알아보자.](https://honeyinfo7.tistory.com/56)
    
- 인스턴스 변수와 클래스 변수에 차이
    - 클래스 변수(Static 멤버)
        - 클래스 내에 static 키워드로 선언된 변수
        - 처음 JVM이 실행되어 클래스가 메모리에 올라갈 때부터 프로그램이 종료될 때까지 유지
        - 클래스가 여러 번 생성되어도 static 변수는 딱 한번만 생성
        - 동일한 클래스의 모든 객체들에 의해 공유된다
    - 인스턴스 변수(Non-static 멤버)
        - 클래스 내에 선언된 변수
        - 객체 생성 시 매번 새로운 변수 생성
        - 클래스 변수와 달리 공유되지 않는다
    
    [[java] 클래스변수, 인스턴스 변수 차이(static변수와 non Static변수)](https://sujinhope.github.io/2021/03/03/Java-%ED%81%B4%EB%9E%98%EC%8A%A4%EB%B3%80%EC%88%98,-%EC%9D%B8%EC%8A%A4%ED%84%B4%EC%8A%A4-%EB%B3%80%EC%88%98-%EC%B0%A8%EC%9D%B4(Static%EB%B3%80%EC%88%98%EC%99%80-Non-Static%EB%B3%80%EC%88%98).html)
    
- Final 키워드란? 그리고 언제 사용하는지
    - final
        - 변수에 사용되면 값을 변경할 수 없는  상수가 되고, 메소드에 사용되면 오버라이딩을 할 수 없게 되고, 클래스에 사용되면 자신을 확장하는 자손 클래스를 정의하지 못하게 된다
        
        [[Java] final 키워드 간단하게 정리하기](https://devlog-wjdrbs96.tistory.com/369)
        
    - 언제 사용하는지?
        - 불변 객체에 정의 후 값을 재할당하지 않을 때 사용
        - 상수(const)에서 많이 사용
        
        [java final 의 의미, 언제 사용할까?](https://mycup.tistory.com/366)
        
- non-static멤버와 static 멤버의 차이
    
    인스턴스 변수와 클래스 변수에 차이와 동일
    
- 컬렉션 프레임워크 List말고 다른 인터페이스는 뭐가 있는가?
    - collection framework
        - 다수의 데이터를 쉽고 효과적으로 처리할 수 있는 표준화된 방법을 제공하는 클래스의 집합
        - java의 interface를 사용하여 구현된다
    - 주요 인터페이스
        - List 인터페이스
            - Collection 인터페이스를 상속받는다
            - 순서가 있는 데이터의 집합으로, 데이터의 중복을 허용한다
        - Set 인터페이스
            - Collection 인터페이스를 상속받는다
            - 순서가 없는 데이터의 집합으로, 데이터의 중복을 허용하지 않는다
        - Map 인터페이스
            - 구조상의 차이로 인해 Collection 인터페이스를 상속받지 않고 별도로 정의되었다
            - 키와 값의 한 쌍으로 이루어지는 데이터의 집합으로, 순서가 없다
            - 키의 중복은 허용하지 않지만, 값은 중복될 수 있다
        
        [코딩교육 티씨피스쿨](http://www.tcpschool.com/java/java_collectionFramework_concept)
        
- List인터페이스의 구현체 두 가지
    - Vector 클래스
        - ArrayList와 동일한 내부구조를 가진다
        - 동기화된(synchronized) 메소드로 구성되어 있다
            
            ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/9685a2c5-64b0-427b-adfb-9340ae08c87d/Untitled.png)
            
        - 멀티 스레드 환경에서 안전하게 객체를 추가/삭제할 수 있다. 즉, 스레드에 안전하다(Thread Safe)라고 말한다
        - 동기화 되어있기 때문에 ArrayList보다는 객체를 추가/삭제하는 과정이 느릴 수 밖에 없다
        
        ```java
        // String 객체를 관리하는 Vector 객체 생성 
        List<String> list = new Vector<>(); 
        // 객체 추가 
        list.add("hello"); 
        // 객체 제거 
        list.remove(0);
        ```
        
    - LinkedList 클래스
        - ArrayList에는 내부 배열에 객체를 저장해서 인덱스로 관리하지만, LinkedList는 인접 참보를 링크해서 체인처럼 관리한다
        - LinkedList에서 특정 인덱스의 객체를 제거하게 되면 제거되는 인덱스의 앞 뒤 링크만 변경되고 나머지 링크는 변경되지 않는다
        
        ```java
        // LinkedList 객체 생성 
        List<String> list = new LinkedList<>();
        ```
        
    
    [Java 리스트(List) 컬렉션 종류 ArrayList, Vector, LinkedList](https://lelecoder.com/78)
    
- 자바의 Array와 ArrayList의 차이
    
    
    |  | Array | ArrayList |
    | --- | --- | --- |
    | 사이즈 | 초기화 시 고정
    int[] myArray = new int[6]; | 초기화 시 사이즈를 표시하지 않음. 유동적
    ArrayList<Integer> myArrayList = new ArrayList<>(); |
    | 속도 | 초기화 시 메모리에 할당되어 속도가 빠르다 | 추가 시 메모리를 재할당하여 속도가 느리다 |
    | 변경 | 사이즈 변경 불가 | 추가/삭제 가능
    add(), remove() |
    | 다차원 | 가능
    int[][][] multiArray = new int[3][3][3]; | 불가능 |
    
    [[JAVA] Array와 ArrayList 차이와 사용법](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=sangrime&logNo=220622445166)
    
- Array나 List를 그대로 쓰면 되는데 왜 굳이 Stack이나 Queue로 쓰는지?
    
    데이터를 효율적으로 저장하고 관리해서 메모리를 효율적으로 사용하기 위해
    
    (효율성과 관리의 편의성 때문)
    
    [[TIL] 자료구조, Stack, Queue](https://velog.io/@brian_kim/TIL-%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-Stack-Queue)
    
- Exception 클래스가 있는데 Exception은 크게 두 가지로 나뉜다 이 두 가지는 무엇인가?
    - compile checked Exception 계열
        - 컴파일 시 예외처리 유무를 검사하는 클래스 계열
        - IOException, SQLException 등
        - 예외처리 필수. 반드시 명시적으로 예외처리를 해야한다
    - compile unchecked Exception 계열
        - 컴파일 시 예외처리 유무를 검사하지 않는 클래스 계열
        - 예외처리 선택. 대부분 발생되는 예외가 **개발자의 부주의한 코드** 작업으로 발생하기 때문에 컴파일 시 예외처리 유무를 검사하지 않는다
        - 예: 값을 0으로 나누기, null값으로 메소드 호출, 배열의 크기보다 큰 인덱스 값으로 접근
        - 프로그램의 종료로 이어진다
    
    [Exception 클래스 - Exception Class 분류, 클래스 설명](https://codedragon.tistory.com/4461)
    
- Exception과 Error의 차이
    - Exception
        - 실행 도중 중단될 정도로 큰 문제가 아닐 때 발생
        - Checked Exception, Unchecked Exception 두 종류의 예외가 존재한다
        - Checked Exception
            - 실행하기 전에 예측 가능한 SQLException이나 FileNotFoundException 등을 말한다
        - Unchecked Exception
            - 실행하고 난 후에 알 수 있는 ArrayIndexOutOfBoundException, NullPointerException 등을 말한다
    - Error
        - 런타임에서 실행 시 발생
        - 전부 예측 불가능한 Unchecked Error에 속한다
        - Exception과 다르게 에러가 발생할 경우 코드를 고치지 않고서는 해결 불가능
        - 예: StackOverflowError, OutOfMemoryError
    
    [자바 Error Exception 차이 정리](https://wakestand.tistory.com/99)
    
- 리터럴 (Literal) 이란?
    - 프로그램에서 직접 표현한 값
    - 소스코드의 고정된 값을 대표하는 용어
    - 정수 리터럴
        - 10진수(ex: 15), 8진수(ex: **0**15), 16진수(ex: **0x**15), 2진수(ex: **0b**0101)
    - 실수 리터럴
        - 소수점 형태나 지수 형태로 표현한 값
        - 숫자 뒤에 f(float)나 d(double)을 명시적으로 붙이기도 한다
        - float같은 경우는 f를 꼭 붙여야 하고 double은 생략 가능하다
        
        ```java
        float h = 0.1234f;
        double i = .1234D;
        ```
        
    - 문자 리터럴
        - 단일 인용부호(’’)로 문자를 표현한다
        
        ```java
        char a = 'H';
        char b = "한";
        char c = \uae00;(유니코드값)
        
        (\u다음에 4자리 16진수로, 2바이트의 유니코드(Unicode))
        ```
        
    - 문자열 리터럴
        - 문자열은 **기본타입이 아니다**.
        - ( " " )로 문자열을 표현한다
        
        ```java
        String lter = "JAVA";
        lter + 26 = "lter26" 
        ```
        
    - 논리 타입 리터럴, 외 리터럴
        - boolean 타입 변수에 치환하거나 조건문에 이용
    
    ```java
    boolean a = true;
    boolean b = 10 > 0; (여기선 b값이 true)
    boolean c = 0;
    
    (C와 달리 boolean 타입으론 1,0을 참,거짓으로 사용 불가)**
    ```
    
    - null 리터럴은 레퍼런스에 대입해서 사용한다. 기본 타입에는 사용이 불가하고 String같은 경우에는 사용 가능하다.
    
    ```java
    *int a = null;(에러)
    String str = null;
    str = "JAVA";
    ```
    
    [[JAVA]자바_리터럴(literal)이란?](https://mine-it-record.tistory.com/100)
    
- String의 특징
    - 문자열을 만들 때 두 가지 방법
        - 문자열 리터럴을 지정하는 방법
            - String str1 = "abc" ;     String str2 = "abc";
        - String 클래스의 생성자를 사용해서 만드는 방법
            - String str3 = new String("abc");    String str4 = new String("abc");
        
        equals(String s)를 사용했을 때는 두 문자열의 내용("abc")을 비교하기 때문에 두 경우
        
        str1.equals(str2)과 str3.equals(str4)는 모두 true를 갖는다.
        
        그러나 String 클래스의 생성사를 이용한 String인스턴스의 경우에는 new연산자에 의해서 메모리할당이 이루어지기 때문에 항상 새로운 String인스턴스가 생성된다.
        
        ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/c6883587-7f29-4df6-ac3d-6ea3afc7a396/Untitled.png)
        
    
    문자열 리터럴을 지정한 방법에서 str1 과 str2 변수는 같은 주소 0x100(abc주소)를 가리키고 있기 때문에 str1==str2 경우에도 true가 나오는것이다.
    
    반면 str3과 str4는 각각 new 연산자로 인해 새로운 메모리가 각각 할당되게 되는것이다.
    
- 객체와 클래스란 ?
    - 클래스
        - 객체를 정의해 놓은 것, 객체의 설계도 또는 틀
        - 객체를 생성하는 데 사용
    - 객체
        - 실제로 존재하는 것, 사물 또는 개념
        - 객체가 가지고 있는 기능과 속성에 따라 용도가 달라진다
    
    [JAVA - 클래스와 객체(Class and Object) | Cremazer](https://cremazer.github.io/java-Class-and-Object/)
    
- 생성사 주입과 필드 주입의 차이(스프링인데?)
    - 필드 주입은 빈을 먼저 생성한 후에 의존성 주입을, 생성자 주입은 빈을 생성할 때 의존성 주입을 하게 된다.
    - 생성자 주입을 사용하면 객체 변이 방지, 순환 참조 조기 발견, 테스트 코드 작성에 유리한 등의 이점이 있고, lombok을 사용하면 필드 주입과 비교하여도 코드를 깔끔하게 작성할 수 있다.
    
    [필드 주입과 생성자 주입](https://velog.io/@ysh096/%ED%95%84%EB%93%9C-%EC%A3%BC%EC%9E%85%EA%B3%BC-%EC%83%9D%EC%84%B1%EC%9E%90-%EC%A3%BC%EC%9E%85)
    
- 접근제어자에는 무엇이 있으며 각각의 차이
    - `private` : 같은 클래스 내에서만 접근 가능
    - `default` : 같은 패키지 내에서만 접근 가능
    - `protected` : 같은 패키지 내에서, 그리고 다른 패키지의 자손 클래스에서 접근 가능
    - `public` : 접근 제한이 전혀 없다.
    
    [[JAVA] 접근제어자 (Access Modifier)](https://88240.tistory.com/448)
    
- 인터페이스와 추상클래스의 차이
    - 추상 클래스
    
    클래스를 설계도라 하면, 추상 클래스는 미완성 설계도라 할 수 있다.
    
    추상 메서드를 선언하여 상속을 통해 자손 클래스에서 완성하도록 한다. 그리고 상속을 위한 미완성 클래스이기 때문에 객체를 생성 할 수 없다.
    
    - 추상 클래스 규칙
    1. 추상 클래스는 abstract를 붙여 표현한다.
    2. new를 통해 객체를 직접 생성할 수 없다.
    3. 메소드에 abstract를 사용하면 interface의 메소드와 같이 구현 부분은 없다.
    4. abstract로 선언한 메소드는 자식 클래스에서 반드시 구현해야 한다.
    
    - 인터페이스
    
    추상 클래스보다 추상화가 높다. 밑그림만 그려진 기본 설계도라 할 수 있다. 그리고 추상 클래스와 다르게 다중상속(구현)이 가능하다.
    
    - 인터페이스 규칙
    1. 추상 클래스처럼 불완전한 것이기에 그 자체만으로 사용되기 보다 다른 클래스를 작성하는데 도움을 준다.
    2. 일반 메서드 또는 멤버 변수를 구성원으로 가질 수 없다.
    3. 모든 멤버 변수는 public static final 이어야 하며 생략 가능하다.
    4. 모든 메서드는 public abstract이어야 하며 생략 가능하다.
    5. JDK 1.8 부터 static 메서드와 default 메서드를 사용할 수 있다.
    
    인터페이스에서 default 메서드를 구현 할 수 있는데 두개 인터페이스를 다중 상속하는 경우 default 메소드가 중복 되면 어떻게 될까?
    
    동일한 default 메소드가 있다면 무조건 오버라이딩하게 되어 있다.
    
- Checked Exception과 UnCheckedException 이란?
    
    ![105691109-2cda9400-5f40-11eb-9003-a14873c2eaf2.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/99a43ebf-7430-4885-b1c2-c43e5c41bfc4/105691109-2cda9400-5f40-11eb-9003-a14873c2eaf2.png)
    
    자바 에러 클래스의 계층 구조에서 RuntimeException의 하위 클래스들은 Uncheck Exception이라 하고, RuntimeException의 하위 클래스가 아닌 Exception 클래스의 하위 클래스들을 Checked Exception이라 한다.
    
    - Checked Exception
    
    Checked Exception의 특징은 반드시 에러 처리를 해야 한다. (try/catch or throw)
    
    ex) FileNotFoundException, ClassNotFoundException
    
    - Uncheck Exception
    
    RuntimeException의 하위 클래스들을 의미합니다. Checked Exception과 달리 에러 처리를 강제하지 않습니다. 말 그대로 실행 중에 발생할 수 있는 예외를 의미합니다.
    
    ex)ArrayIndexOutOfBoundsException, NullPointerException
    
    ![105691015-0d436b80-5f40-11eb-994d-58c55b8d47b8.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fcf03552-c750-4df6-9687-2a18dea7f99b/105691015-0d436b80-5f40-11eb-994d-58c55b8d47b8.png)
    
    - 임의의 예외 클래스를 만들어 예외 처리를 하는 경우가 많을 것인데, try-catch로 묶어줄 필요가 있을 경우에만 Exception 클래스를 확장합니다.
    - 일반적으로 실행시 예외를 처리할 수 있는 경우에는 RuntimeException 클래스를 확장해 Unchecked Exception을 사용하는 것이 좋다.
- Call by Reference와 Call by Value의 차이
    
    call by value 인자로 받은 값을 복사하여 처리, call by reference 인자로 받은 값의 주소를 참조하여 직접 값에 영향
    
    1. call by value (값에 의한 호출)
    - 함수가 호출될 때 메모리 공간에 임시의 공간이 생성된다. 그리고 함수가 종료되면 사라진다.
    - 함수 호출시 전달되는 변수의 값을 복사하여 함수의 인자로 전달한다.
    - 함수에 전달되는 인자의 데이터 타입에 따라 (기본자료형/참조자료형) 함수 호출 방식이 달라진다.
    
    1. call by reference (참조에 의한 호출)
    - 함수가 호출될 때 메모리 공간 안에 함수를 위한 별도의 임시 공간 생성
    - 함수 호출시 인자로 전달되는 변수의 래퍼런스를 전달(해당 변수를 가르킨다.)
    - 함수 안에서 인자의 값이 변경되면, 함수 호출시에 있던 변수들도 값이 바뀐다.
- Collection이란?
    
    데이터의 집합, 그룹을 의미
    
    데이터, 자료구조인 컬렉션과 이를 구현하는 클래스를 정의하는 인터페이스를 제공한다.
    
    ![99B88F3E5AC70FB419.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/fb2ae825-deae-4e84-b09f-666f5f3f55a2/99B88F3E5AC70FB419.png)
    
    Collection 인터페이스는 List, Set, Queue로 크게 3가지 상위 인터페이스로 분류, 그리고 Map의 경우 Collection 인터페이스를 상속받고 있지 않지만 Collection으로 분류된다.
    
    | 인터페이스 | 구현 클래스 | 특징 |
    | --- | --- | --- |
    | Set | HashSet
    TreeSet | 순서를 유지하지 않는 데이터의 집합으로 데이터의 중복을 허용하지 않는다. |
    | List | LinkedList
    Vector
    ArrayList | 순서가 있는 데이터의 집합으로 데이터의 중복을 허용 |
    | Queue | LinkedList
    PriorityQueue | List와 유사 |
    | Map | Hashtable
    HashMap
    TreeMap | key, value의 쌍으로 이루어진 데이터의 집합으로 순서는 유지되지 않으며 key의 중복을 허용하지 않으나 value의 중복은 허용 |
- Collection종류와 각각의 장/단점
    - ArrayList
    
    동적 배열을 제공, 표준 배열보다 느릴 수 있지만 배열에서 많은 움직임이 필요한 프로그램에서 유용
    
    - LinkedList
    
    요소가 연속 된 위치에 저장되지 않고 모든 요소가 데이터 부분과 주소 부분이 있는 별도의 객체 저장, 포인터와 주소를 사용해서 데이터를 가져온다.
    
    - Vector
    
    동적 배열을 제공하고, 표준 배열보다 느리지만 많은 움직임이 필요한 프로그램에서 유용, ArrayList와 유사.
    
    하지만 차이점은 Vector은 동기화가 되고, ArrayList는 동기화가 되지 않는다.
    
    - Stack
    
    스택 클래스 모델 및 스택 데이터 구조를 구현할 때 주로 사용, 후입선출을 기본 원칙으로 한다.
    
    - PriorityQueue
    
    우선 순위에 따라 객체를 처리할 때 사용, 선입선출 기본으로 하지만 우선 순위에 따라 먼저 처리해야할 것이 있다면 우선 순위 합을 기반으로 처리
    
    - ArrayDeque
    
    크기가 조정되는 배열이고 양쪽 끝에서 요소를 추가하고 제거하는 구조
    
    - HashSet
    
    입력되는 데이터는 동일한 순서로 삽입되는 것을 보장하지 않는다.
    
    null 요소 삽입을 허용
    
    - LinkedHashSet
    
    HashSet와 유사하지만 차이점은 데이터를 저장하는 순서를 유지
    
    - TreeSet
    
    Tree를 사용하여 저장, 데이터의 순서는 오름차순으로 유지
    
    - HashMap
    
    데이터를 키-값 형태로 저장, HashMap의 데이터에 접근하려면 키를 알고 있어야 접근이 가능하다.
    
    HashMap는 Hashing이라는 기술을 사용하는데 해싱은 인덱싱 및 검색 작업이 더 빨라지도록 키에 산술적인 연산을 적용하여 항목이 저장되어 있는 테이블의 주소를 계산하여 항목에 접근하는 방식
    
- 계층간의 데이터교환시 Map을 사용해선 안되는 이유
    - 직관성이 떨어진다.
    
    어떤 데이터가 전달되고, 어떤 데이터를 담고 있는지 계속해서 추적하게 된다. 코드를 분석하지 않고서는 예상하기 어렵다.
    
    - 안전성이 떨어진다.
    
    VO 객체를 사용할 경우 컴파일 에러가 나겠지만, Map 객체를 사용할 경우 컴파일 단계에서 에러가 나지 않는다. 때문에 오타 때문에 코드의 안전성이 떨어지고 개발 생산성을 떨어뜨린다.
    
    - 타입캐스팅 필요로 인한 비용과 코드 가독성 저하
    
    VO 객체의 경우 필드의 타입이 이미 정의되어 있다. Map의 경우엔 어떤 타입의 데이터가 담길지 모른다. 그래서 데이터를 꺼내서 사용할 경우 Map는 계속해서 타입캐스팅이 필요하다.
    
- HashMap과 HashTable의 차이점
    
    Map인터페이스를 상속받아 구현되어 키와 값으로 관리하는 자료구조이다.
    
    - 동기화
    
    HashMap는 동기화를 지원하지 않는다. 반면 다중 스레드 환경에서는 HashTable은 동기화를 지원하기 때문에 실행 환경에 따라 구분하여 사용하면 된다. 하지만 새로운 버전의 자바에서는 HashMap를 활용하고 동기화가 필요한 시점에서는 ConcurrentHashMap를 사용하는 것이 더 좋다.
    
    - 반환값
    
    HashMap는 저장된 요소들의 순회를 위해 Fail-Fast Iterator를 반환, Hashtable은 Enumeration을 반환
    
    Enumeration은 컬렉션 프레임워크 이전에 사용되던 인터페이스로 Iterator 사용을 권장한다. Iterator은 remove() 메소드가 추가되었다. 그리고 다른 스레드에서 해당 자료에 요소를 삽입, 삭제, 수정이 발생하면 ConcurrentModificationException을 발생시켜 일관성을 보장한다. 이를 Fail-Fast Iterator 이라 한다.
    
    ConcurrentHashMap의 경우 Map의 복사본을 참조하는 Iterator를 반환하며 다시 반환받은 시점에 Map에 수정이 있을 경우 해당 Iterator는 반영되지 않는다. 따라서 ConcurrentModificationException 또한 발생하지 않는다. 다중 스레드 상황에서 해당 Map의 무결성을 보장한다.
    
- Java의 Garbage Collection 처리방법
    1. JVM GC 동작 순서
    - Heap 영역에 존재하는 객체들에 대해 접근 가능하지 확인
    - GC Root에서 부터 참조값을 따라가며 접근 가능한 객체들에 Mark하는 과정을 진행
    - Mark 되지 않은 객체, 접근할 수 없는 객체는 제거 대상이 되고, 해당 객체들을 제거
        
        ![997FE9375DDCC3920C.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/b11cfabe-7329-47dc-b8a8-580c44fe4201/997FE9375DDCC3920C.png)
        
        ![img.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/2b7cecda-0131-4fb2-8620-5c59e20c6297/img.png)
        
    
    1. GC Root가 될 수 있는 대상
    - JVM 메모리의 Stack 영역에 존재하는 참조 변수
    - 메소드 영역의 static 데이터
    - JIN에 의해 생성된 객체들
    
    1. Serial GC
    
    Young 영역과  Old 영역이 연속적으로 처리되며 하나의 CPU 사용, 이 처리를 수행할 때 Stop-the-world 라고 표현, 가장 단순한 방식의 싱글 스레드로 동작한다. 싱글 스레드로 동작하여 느리고, 그 만큼 Stop-the-world 시간이 다른 GC에 비해 길다.  보통 실무에서 사용 안함
    
    살아있는 객체들이 Eden 영역에 있다. → Eden 영역이 꽉자면 To Survivor 영역으로 살아있는 객체가 이동한다. Survivor 영역에 들어가기에 너무 큰 객체는 Old 영역으로 이동한다. → To Survivor 영역이 꽉 찼을 경우, Eden 영역이나 From Survivor 영역에 남아 있는 객체들은 Old영역으로 이동
    
    이후에 Old영역이나 Perm 영역에 있는 객체들은 Mark-sweep-compact 콜렉션 알고리즘을 따른다. 
    
    - Mark-sweep-compact 알고리즘
    1. Old 영역으로 이동된 객체들 중 살아 있는 객체를 식별
    2. Old 영역의 객체들을 훑는 작업을 수행하여 쓰레기 객체를 식별
    3. 필요없는 객체들을 지우고 살아 있는 객체들을 한 곳으로 모은다.
    
    1. Parallel GC
    
    Young 영역에서 별렬로 처리한다. 많은 CPU를 사용하기 때문에 GC의 부하를 줄이고 애플리케이션의 처리량을 증가시킬 수 있다. java8의 default GC, Mark-sweep-compact 알고리즘 사용
    
    1. Parallel Compacting GC
    
    Old영역 GC에서 새로운 알고리즘을 사용
    
    Parallel GC는 Young 영역에 대해서만 멀티 스레드 방식을 사용했다면, Parallel Old GC 는 Old 영역까지 멀티스레드 방식을 사용, Old 영역의 GC는 다음의 3단계를 거친다.
    
    - Mark 단계 : 살아있는 객체를 식별하여 표시해 놓는 단계
    - Sweep 단계 : 이전에 GC를 수행하여 컴팩션된 영역에 살아 있는 객체의 위치를 조사하는 단계
    - Compact 단계 : 컴팩션을 수행하는 단계, 수행 이후에는 컴팩션된 영역과 비어 있는 영역으로 나뉜다.
    
    1. Concurrent Mark-Sweep GC
    
    stop the world로 java application이 멈추는 현상을 줄이고자 만든 GC 로 객체를 한번에 찾지 않고 나눠서 찾는 방식 사용.
    
    이 방식은 low-latency collector로도 알려져 있으며, 힙 메모리 영역의 크기가 클 때 적합하다. Young 영역에 대한 GC는 병렬 콜렉터와 동일하다.
    
    - Initial Mark : GC Root 가 참조하는 객체만 마킹
    - Concurrent Mark : 참조하는 객체를 따라가며, 지속적으로 마킹
    - Remark : concurrent mark 과정에서 변경된 사항이 없는지 다시 한번 마킹하며 확정하는 과정
    - Concurrent Sweep : 접근할 수 없는 객체를 제거하는 과정
- JVM의 구조
    
    JVM 크게 4가지로 구성된다고 할 수 있다.
    
    - Class Loader
    - Execution Engine
    - Garbage Collector
    - Runtime Data Area
    
    ### **자바의 실행방식**
    
    위에 그림에서 보이는 것처럼 자바 애플리케이션의 실행에서 Java 컴파일러가 먼저 동작을 수행한다.
    
    Java 컴파일러는 .java 파일을 모두 JVM이 사용할 수 있는 .class 파일로 컴파일 한다. 이 시점이 컴파일 타임이다.
    
    이후 JVM을 실행하면서 런타임 시점이 시작된다.
    
    JVM 내부에서는 애플리케이션을 실행하기 위해 Execution Engine이 필요한 클래스들을 Class Loader에 요청하고 Class Loader가 바이트코드의 .class에서 가져와 메모리에 올린다. (로컬 디스크에서 .class 파일을 가져올 수도 있지만 네트워크를 통해서 가져올 수 있다. - URLClassLoader)
    
    가져오는 클래스들의 바이트 코드들이 이상이 없는지, 자바의 보안 규칙을 위배하지 않는지 검사를 한다. (자바는 네트워크를 통하여 전송된 자바 프로그램이 컴퓨터를 훼손시키는 것을 방지 하기 위해 엄격한 보안 규칙을 갖고있다.)
    
    그 다음으로 Execution Engine이 메모리에 올라온 바이트코드를 실행하면서 애플리케이션이 실행된다. 계속 이러한 동작을 하면서 애플리케이션이 동작한다.
    
    ### **Class Loader**
    
    자바 애플리케이션이 실행되기 이전 Java 컴파일러는 Java 소스 파일을 .class 파일(바이트 코드)로 컴파일해준다. 그 이후 실행하면서 필요한 바이트 코드 파일들을 메모리에 올려야 하는데 이 일을 하는 것이 Class Loader이다.
    
    즉, Class Loader 는 class 파일을 JVM이 운영체제로부터 할당받은 메모리 영역 (Runtime Data Area)에 적재하는 역할을 한다.
    
    ### **Execution Engine**
    
    Class Loader에 의해 메모리에 적재된 바이크 코드의 클래스들을 기계어로 변경해 명령어 단위(Operation Code)로 실행하는 역할을 한다.
    
    자바는 인터프리터 방식을 사용하는데, 인터프리터 방식은 한줄 한줄 읽어들여야 하는 방식이여서 컴파일 방식에 비해 느리다. 그래서 자바는 컴파일과 인터프리터 방식을 모두 사용한다. 바로 JIT 컴파일러이다.
    
    JIT 컴파일러는 처음 바이트 코드를 읽을 때에는 인터프리터 방식으로 한줄 한줄 씩 읽고 반복되는 바이트 코드를 또 읽게되면 캐싱해둔 곳에서 이미 기계어로 바꾼 내용을 가져다가 쓴다.
    
    ### **Garbage Collector**
    
    Garbage Collector는 Heap 메모리 영역에 생성된 객체들 중에 참조되지 않은 객체들을 제거하는 역할을 한다.
    
    GC(Garbage Collection) 의 발생은 일정하게 정해져 있지 않기 때문에 언제 객체를 정리할지는 알 수 없다. 즉 바로 참조가 없어지자마자 작동하는 것이 아니다.
    
    [🔗 GC의 자세한 동작](https://err0rcode7.github.io/java/2021/05/12/%EA%B0%80%EB%B9%84%EC%A7%80%EC%BB%AC%EB%A0%89%EC%85%98.html)을 참고하길 바란다.
    
    ### **Runtime Data Area**
    
    JVM의 메모리 영역으로 Java 애플리케이션 실행시 사용되는 데이터를 적재하는 영역이다. 크게 5가지 영역으로 구분된다.
    
    - Heap
    - Method
    - Stack
    - PC register
    - Native Method Stack
    
    ### **Heap**
    
    - 인스턴스화 된 모든 클래스 인스턴스와 배열을 저장을 하는 공간이다.
    - 모든 JVM 스레드에 공유되는 공유 자원이기도 하다.
    - Heap에 저장된 할당된 메모리 회수 권한은 무조건 가비지 컬렉터에 의해서만 회수가 가능하다.
    
    ### **Method**
    
    - 클래스 수준의 정보를 저장하는 공간이다.
        - 타입 정보
        - 필드 정보(필드 타입, 필드 수정자)
        - 메서드 정보(메서드의 메타 데이터)
        - 런타임 상수 풀
        - 클래스 변수
    - 모든 JVM 스레드에 공유되는 공유 자원이다.
    - 사실 논리적으로 Heap 영역에 포함되는 영역이다.
    
    ### **PC register**
    
    - 쓰래드가 생성될때마다 생성되는 영역으로 Program Counter 즉, 현재 쓰레드가 실행되는 부분의 주소와 명령을 저장하고 있는 영역이다. 이것을 이용해서 여러 쓰레드를 제어한다.
    - JVM은 Stacks-Base 방식으로 작동한다. CPU에 직접 Instruction을 수행하지 않고 Stack에서 Operand를 뽑아내 이를 별도의 메모리 공간에 저장하는 방식을 취한다. 이러한 메모리 공간을 PC register라고 한다.
    
    ### **Native Method Stack**
    
    - 자바 외 언어로 작성된 네이티브 코드를 위한 메모리 영역이다. 보통 C/C++ 등의 코드를 수행하기 위한 스택이다.
    - JNI를 통해 표준에 가까운 방식으로 구현이 가능하다.
- Java Map 인터페이스 구현체의 종류
    - HashTable
    
    Map interface를 implements 한 클래스, 중복을 허용하지 않는다. Map의 특징인 key와 value의 쌍으로 이루어지며, key 도는 value 값은 null을 허용하지 않는다.
    
    - HashMap
    
    Map interface를 implements 한 클래스, 중복을 허용하지 않는다. Map의 특징인 key와 value의 쌍으로 이루어 지며, key또는  value 값이 null을 허용한다.
    
    내부적으로 Entty<K, V>[] Entry의 array로 되어 있다. array에 index는 내부 해쉬 함수를 통해 계산된다.
    
    - TreeMap
    
    중복을 허용하지 않는다. SortedMap을 implements 하여 key 값들에 대한 정렬이 이루어진다.
    
- Javs Set 인터페이스 구현체의 종류
    - HashSet
    
    해싱을 이용해서 구현, 데이터 중복으로 저장할 수 없고, 순서를 보장하지 않는다. equals()나 hashCode()를 오버라이딩 해서, 인스턴스가 달라도 동일 객체를 구분해 중복 저장을 막는다.
    
    - TreeSet
    
    이진탐색트리의 형태로 데이터 저장, 데이터 추가, 삭제는 시간이 더 걸리지만 검색, 정렬이 뛰어나다. 기본적으로 오름차순 정렬
    
    - LinkedHashSet
    
    HashSet 클래스를 상속받은 LinkedList 이다. 데이터에 삽입된 순서대로 데이터 관리
    
- Java List 인터페이스 구현체의 종류
    - LinkedList
    
    노드간에 연결을 통해 리스트로 구현된 객체, 노드는 내부적으로 데이터 필드와 다음 노드를 가리키는 주소 필드를 가진다. 노드의 주소 필드로 이어져 있는 구조, 데이터의 검색은 순차적으로 일어난다. 때문에 인덱스를 이용해 검색하는 ArrayList에 비해 검색 성능이 떨어진다. 삽입/삭제 시 노드의 주소지만 변경하면 되므로 성능이 좋다.
    
    - ArrayList
    
    데이터를 배열 구조로 가지고 있는 객체, 내부적으로 인덱스를 가지고 있어 검색이 용이, 데이터의 추가 또는 수정, 삭제 시 내부적으로 임시공간을 만들어 데이터를 저장한다. 때문에 대량의 데이터를 추가 또는 수정, 삭제할 때 성능이 저하된다.
    
    - Vector
    
    java 1.0 부터 있던 리스트 객체로 배열 형태, 데이터 추가시 공간을 두배로 확보하기에 메모리 사용 증가, 동기화가 항상 이루어지기 때문에 하나의 스레드가 하나의 자원을 이용하는 경우 성능이 저하된다.
    
- Java Reflection이란?
    
    클래스, 인터페이스, 메소드들을 찾을 수 있고, 객체를 생성하거나 변수를 변경할 수 있고 메소드를 호출할 수도 있다.
    
    JVM에서 실행되는 애플리케이션의 런타입 동작을 검사하거나 수정할 수 있는 기능이 필요한 프로그램에서 사용, 쉽게 말해 클래스의 구조를 개발자가 확인 할 수 있고, 값을 가져오거나 메소드를 호출하는데 사용, 스프링 프레임워크,  ORM기술인 하이버네이트, jackson 라이브러리 등에서 사용.
    
    스프링에서 런타임 시에 개발자가 등록한 빈을 애플리케이션에서 가져와 사용한다.
    
- Stream이란?
    
    java 8에서 추가한 streams 은 람다를 활용할 수 있는 기술 중 하나, java 8 이전에는 배열 또는 컬렉션 인스턴스를 다루는 방법은 for/foreach 문을 돌면서 요소 하나씩을 꺼내서 다루는 방법이었다. 간단한 경우라면 상관없지만 로직이 복잡해질수록 코드의 양이 많아져 여러 로직이 섞이게 되고, 메소드를 나눌 경우 루프를 여러번 도는 경우가 발생한다.
    
    streams은 데이터의 흐름 입니다. 배열 또는 컬렉션 인스턴스에 함수 여러 개를 조합해서 원하는 결과를 필터링하고 가공된 결과를 얻을 수 있습니다. 또한 람다를 이용해서 코드의 양을 줄이고 간결하게 표현할 수 있습니다. 즉, 배열과 컬렉션을 함수형으로 처리할 수 있습니다.
    
- 롬복이 생성하는 메서드가 어느 시점에 생성 되는지?
    
    lombok은 자바 컴파일 시점에서 특정 어노테이션으로 해당 코드를 추가, 코드의 가독성 및 유지보수에 많은 도움을 준다.
    
- 람다란?
    
    람다 함수는 프로그래밍 언어에서 사용되는 개념으로 익명 함수를 지칭
    
    - 장점
    1. 코드의 간결성 : 불필요한 반복문의 삭제가 가능하며 복잡한 식을 단순하게 표현할 수 있다.
    2. 지연연산 수행 : 지연연상을 수행 함으로써 불필요한 연산을 최소화 할 수 있다.
    3. 병렬처리 가능 : 멀티 쓰레드를 활용하여 병렬처리를 사용 할 수 있다.
    
    - 단점
    1. 람다식의 호출이 까다롭다
    2. 람다 stream 사용 시 단순 for문 또는 while문 사용 시 성능이 떨어진다.
    3. 불필요하게 너무 사용하게 되면 오히려 가독성을 떨어 뜨린다.
- String 을 ==으로 비교하면 안되는이유
    
    == 연산자와 equals() 메소드의 가장 큰 차이점은 == 연산자는 비교하고자 하는 두개의 대상의 주소값을 비교하고, equals 메소드는 비교하고자 하는 두개의 대상의 값 자체를 비교한다.
    
    기본 타입 int, char 등은 Call by value 형태로 기본적으로 대상의 주소값을 가지지 않는 형태 입니다. Call by Reference 형태로 생성 시 주소값이 부여됩니다.  그렇기에 String 타입을 선언했을 때는 같은 값을 부여하더라도 서로간의 주소값이 다릅니다.
    
    ![다운로드.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7546fb8e-6f40-448b-a08d-e57ea41a1f63/다운로드.png)
    
- Java의 세 가지 변수에 대해 JVM메모리와 연관지어 설명
    
    java는 크게 전역변수, 지역변수로 구분, 전역변수는 클래스변수, 인스턴스 변수로 세분화
    
    ![캡처.PNG](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/793b2c21-58be-4cd8-a200-6b9b522125fd/캡처.png)
    
- Servlet Dispacher란?
    
    가장 앞단에서 HTTP 프로토콜로 들어오는 모든 요청을 가장 먼저 받아 적합한 컨트롤러에 위임해주는 프론트 컨트롤러, 공통적인 작업을 먼저 처리한 후에 해당 요청을 처리해야 하는 세부 컨트롤러를 getBean()으로 가져오고, 정해진 메소드를 실행
    
    해당 어플리케이션으로 들어오는 모든 요청을 핸들링 해주고 공통 작업을 처리, 하지만 모든 요청을 처리하다보니 이미지나 HTML/CSS/JavaScript 등과 같은 정적 파일에 대한 요청마저 모두 가로채는 까닭에 정적 자원을 불러오지 못하는 상황도 발생
    
    2가지 해결법 제시
    
    1. 정적 자원에 대한 요청과 애플리케이션에 대한 요청 분리
    
    /apps 의 url로 접근 하면 Dispatcher Servlet이 담당
    
    /resources의 url로 접근하면 정적인 요청
    
    하지만 모든 요청을 이런 식으로 하면 직관적인 설계가 될 수 없다.
    
    1. 애플리케이션에 대한 요청을 탐색하고 없으면 정적 자원에 대한 요청 처리
    
    Dispatcher Servlet에서 해당 요청에 대한 컨트롤러를 찾을 수 없는 경우에 2차적으로 설정된 자원 경로를 탐색하여 자원을 찾아낸다. 이렇게 영역을 분리하면 효율적인 리소스 관리를 지원할 뿐 아니라 추후에 확장을 용이하게 해준다.
    
- POJO란?
    
    Plain Old Java Object, 해석하면 오래된 방식의 간단한 자바 오브젝트, 중량 프레임워크들을 사용하게 되면서 해당 프레임워크에 종속된 무거운 객체를 만들게 된 것에 반발해서 사용되게 된 용어이다. 오래된 방식이란 쉽게 말해 특정 ‘기술’에 종속되어 동작하는 것이 아닌 순수한 자바 객체를 말합니다.
    
    예를 들어 ORM이 새롭게 등장 했을 때, ORM 기술을 사용하고 싶다면 ORM프레임워크를 사용해야 했습니다. 만약 자바가 ORM 기술을 사용하기 위해 Hibernate 프레임워크를 직접 의존하는 순간 POJO라고 할 수 없습니다. 특정 기술에 종속되었기 때문입니다.
    
    특정 기술과 환경에 종속되어 의존하게 된 자바는 코드의 가독성이 떨어져 유지보수에 어려움이 발생합니다. 또한 확장성이 매우 떨어지는 단점이 있습니다. 이 말은 객체지향 설계의 장점들을 잃어버리게 된다는 것입니다.
    
    - 특정 기술을 사용하고 싶다면? PSA
    
    스프링에서 정한 표준 인터페이스가 있기에 특정 기술을 사용 가능합니다. 스프링 개발자들은 ORM 기술을 사용하기 위해 JPA 표준 인터페이스를 정해 두었습니다. 그리고 여러 ORM 프레임워크들은 이 JPA라는 표준 인터페이스 아래 구현되어 실행 됩니다. 이것이 스프링이 새로운 엔터프라이즈 기술을 도입하면서도 POJO를 유지하는 방법입니다. 이 방법을 스프링의 PSA라 합니다.
    
    - 진정한 POJO란?
    
    토비의 스프링에서는 이렇게 말합니다.
    
    특정 기술규약과 환경에 종속되지 않으면 모두 POJO라 할 수 있을까? 아니다. 
    
    진정한 POJO란 객체지향적인 원리에 충실하면서, 환경과 기술에 종속되지 않고 필요에 따라 재활용될 수 있는 방식으로 설계된 오브젝트를 말한다.
    
- Getter와 Setter를 사용하는 이유
    
    데이터를 보호하기 위해 사용한다. 
    

## 기술

- JWT 란?
    
    기존 로그인은 쿠키/세션을 이용하는 경우가 많다. 
    
    하지만 IT 인프라 구성에 많은 변화가 생겨 쿠키/세션 기반 인증 아키텍쳐는 현재 요구사항을 만족하지 못한다.
    
    쿠키는 정보를 클라이언트에 저장하고, 세션은 정보를 서버에 저장한다. 이때 보안에 취약한 쿠키 대신 세션을 사용하는데 세션을 사용하는데 있어 하나의 서버가 아닌 많은 서버를 운영하는 데 있어 정보의 동기화 문제가 발생한다. 세션을 각 서버에 저장하지 않고 세션 전용 서버, DB에 저장 한다 해도 모든 요청 시 DB에 부하가 발생 할 수 있다.
    
    JWT는 필요한 모든 정보를 자체적으로 가지고 있습니다. 토큰에 대한 기본 정보, 전달 할 정보, 그리고 토큰이 검증됐다는 signature를 포함한다.
    
    - 단점
    1. 토큰 자체에 정보가 있다는 사실은 양날의 검
    2. 토큰에 정보를 저장하기 때문에 정보가 많아지면 토큰의 길이가 길어져 네트워크에 부하를 준다.
    3. stateless에서는 불편할 수 있다. 한 번 만들어진 토큰은 서버에서 제어가 불가능하다. 토큰을 삭제할 수 있는 방법이 없기 때문에 만료시간을 넣어준다.
- OAuth2란?
    
    인증을 위한 개방형 표준 프로토콜 입니다.
    
    프로토콜에서는 Third-Party 프로그램에서 리소스 소유자를 대신하여 리소스 서버에서 제공하는 자원에 대한 접근 권한을 위임하는 방식을 제공
    
    구글, 페이스북, 카카오, 네이버 등에서 제공하는 간편 로그인 기능도 OAuth2 프로토콜 기반의 사용자 인증 기능을 제공
    
    용어
    
    - Authentication : 인증, 접근 자격이 있는지 검증하는 단계
    - Authorization : 인가, 자원에 접근할 권한을 부여, 인가가 완료되면 리소스 접근 권한이 담긴 Access Token이 클라이언트에게 부여
    - Access Token : 리소스 서버에게서 리소스 소유자의 보호된 자원을 획득할 때 사용되는 만료 기간이 있는 Token
    - Refresh Token : Access Token 만료시 이를 갱신하기 위한 용도로 사용, 일반적으로 Access Token보다 만료 기간이 깁니다.
- JWT와 OAuth의 관계
- 소셜로그인 구현 방식
- JWT와 OAuth2.0의 차이
- XSS공격을 어떻게 방어했는지 (React에서도 방어를 해주는데)
    
    lucy-xss-servelter-filter를 설정하여 XML 설정만으로 XSS 방어가 가능해진다. 그리고 일일히 치환 로직을 추가할 필요 없는 자바 서블릿 필터 기반의 라이브러리이다 (게팅은 안했지만.. 근데 서블릿 기반이라 request raw body로 넘어가는 JSON에 대해서는 적용이 안된다고 함 ; ; )
    https://github.com/naver/lucy-xss-servlet-filter
    
- AcceessToken과 RefreshToken 이란 무엇이며 발급과정을 설명
    
    AccessToken이란 httpRequest의 authorization헤더에 있는 사용자의 인증을 위한 정보를 포함한 토큰을 말하며 , 이 토큰을 검증해 사용자 인증을 거치고 API요청에 대한 응답을 사용자에게 전송한다.
    Refresh토큰은 Access토큰을 재발급 하는 용도로 사용되는 토큰이다. 
    
    발급과정 : 사용자가 로그인 요청을 하게 되면 응답으로 AccessToken과 RefresToken을 발급하게 되며, 이때 RefreshToken은 별도의 저장소(db, redis ..)에 저장한다. 사용자가 데이터를 요청할때마다 accessToken을 통한 인증을 하며, AccessToken의 유효기간이 만료가 되면 
    서버에서 클라이언트에게 만료가 됐음을 특정에러코드를 통해 알려주고, 이를 갱신하기 위해 클라이언트에서 서버로 엑세스토큰 재발급을 refreshToken과 함께 요청한다. 서버는 전달받은 refreshToken이 유효한지 확인하고, 저장소에 있던 원본 refreshToken과 비교하여 같은 지 확인한다. 유효한 refreshToken이라면 accessToken을 재발급 해주고, refreshToken도 만료되었다면 로그인을 다시하고 accessToken과 refreshToken을 새로 발급해준다. 
    
- 실시간 알람 기능 (겟팅 컨텝) 작동원리
- 이미지 업로드를 백엔드에서 관리한 이유와 EC2가 아닌 S3에서 관리한이유 (컨텝,카페왕 ,겟팅도함??)
    
    
- QueryDSL을 왜썻나요? (겟팅 컨텝)
    
    JPA로만으로 해결하지 못하는 복잡한 쿼리/동적 쿼리를 해결할 수 있다. 
    
- 정규화와 반정규화의 특징 및 차이
    
    정규화 : 관계형 디비에서 중복을 최소화 하기 위해 데이터를 구조화하는 작업이다. 
    기본적으로 데이터 중복성을 제거해주기 때문에(테이블을 쪼개주기때문에) 성능 자체는 향상되는 특징을 가지고 있다. 정규화를 하면 정합성과 데이터 무결성이 보장된다. 그에 따라 입력Create 수정Update 삭제Delete의 성능은 향상되고 조회Read의 경우 나빠질수도 있고 좋아질 수도 있다. 
    but 그만큼 테이블 조인이 많이 발생하기 때문에 그에 따른 성능저하가 나타날 수 있음.
    
    반정규화 : 데이터 모델을 통합하는 프로세스( 정규화의 완죤 반대군)
    반정규화를 하면 테이블이 단순화 되며 성능이 향상되는 반면, 정합성과 데이터 무결성이 보장되지 않을 수 있다. 반정규화는 의도적으로 중복을 만들어 Read검색 성능을 향상시킨다. 하지만 속성이 각기 다른 테이블에 중복되어 나타나기 때문에 입력Create 수정Update 삭제Delete의 성능은 낮아진다. 
    
    + (intergrity)데이터의 무결성 - 데이터의 LifeCycle동안 데이터가 얼마나 완전하고, 일관되며, 정확한지를 나타내는 정도이다
    
- Redis는 왜 언제 사용하는지?
    
    운영중인 웹 서버에 키 값 형태의 데이터 타입을 처리해야 하고, I/O(입출력)가 빈번히 발생해 다른 저장방식을 사용하면 효율이 떨어지는 경우에 사용한다 
    
    [https://www.youtube.com/watch?v=mPB2CZiAkKM&ab_channel=%EC%9A%B0%EC%95%84%ED%95%9CTech](https://www.youtube.com/watch?v=mPB2CZiAkKM&ab_channel=%EC%9A%B0%EC%95%84%ED%95%9CTech)
    
- Redis의 장/단점
    
    장점 : 
    1. 빠른성능
    **인메모리**(컴퓨터의 메인메모리 RAM) 에 데이터를 올려 사용하며 SSD(Solid State Drive-메모리반도체에 데이터저장), HDD(HardDiskDrive)같은 저장공간에서 데이터를 가져오는것보다 훨씬 빠르다
    2. 
    value값으로 String, List, Set, Sorted set, Hash 등 **다양한 데이터 타입**을 지원하며, 리스트 , 배열 형식의 데이터 처리에 특화, 리스트형 데이터의 입력과 삭제가 MySQL보다 10배 정도 빠르다. 
    3. 메모리를 활용하면서 **영속적인 데이터를 보존** - 명시적으로 삭제, expire를 설정하지 않으면 데이터가 삭제되지 않는다. 스냅샷(기억장치)기능을 제공하여 메모리의 내용을 .*rdb파일로 저장해서 해당 시점으로 복구 가능!!
    
    단점: 
    
    용량 - 인메모리 저장 스토어기 때문에 메인 데이터베이스로 사용하기에는 무리가 있다. 그렇다고 큰 용량을 구매하자니 비용이 발생한다. 
    
    인메모리 데이터 스토어임. physical Memory이상을 사용하면 문제가 당연히 발생. 
    
    죽었을때 swap이 한번이라도 발생된 페이지는 그 메모리페이지에 접근하기 위한 키가 디스크를 계속 접근하기 때문에 속도가 엄청 느려진다(레이턴시 발생) . 해결하기 위해서는 프로세스를 재 실행해야한다.
    
- Redis Failover 를 하기위한 방법과 특징
    
    failover - 서버, 시스템, 네트워크 등에서 이상이 생겼을 때 예비 시스템으로 자동 전환되는 기능.장애 극복 기능
    
    레디스는 단일 인스턴스만으로도 충분히 운영이 가능하지만, 물리 머신이 가진 메모리의 한계를 초과하는 데이터를 저장하고 싶거나, failover에 대한 처리를 통해 HA(고가용성High Availability)를 보장하려면 Sentinel 이나 Cluster 등의 **운영모드**를 선택해서 사용해야 한다. 
    
- Redis Sentinel 동작방식 (이거 그냥넣어봄 아래랑)
    - Sentinel 인스턴스 과반 수 이상이 Master 장애를 감지하면 Slave 중 하나를 Matser로 승격시키고 기존의 Master는 Slave로 강등시킨다.
    - Slave가 여러개 있을 경우 Slave가 새로운 Master로부터 데이터를 받을 수 있도록 재구성된다
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/e6fc9fbc-092a-4819-8eb1-1aee6d7d2256/Untitled.png)
    
- Redis Cluster 동작방식
    
    [https://www.letmecompile.com/redis-cluster-sentinel-overview/](https://www.letmecompile.com/redis-cluster-sentinel-overview/)
    sharding : 하나의 거대한 데이터베이스나 네트워크 시스템을 여러개의 조각으로 나누어 분산 저장하여 관리하는 것. 샤딩을 통해 나누어 진 블록들의 구간을 샤드라고 부른다.
    
    해시 슬롯 : CRC-16 해시 함수를 이용해 key를 정수로 변환하고 해당 정수값을 16,385로 모듈 연산한 값
    
     → Redis Cluster는 여러 Redis 서버에 데이터를 자동으로 샤딩해주는 기술이다. 그리고 자동 장애 조치 기능(Automatic Failover)이 있다. 
    
    해시슬롯을 이용해 데이터를 샤딩한다. Master가 죽을 경우 Master의 Slave는 gossip Protocol을 통해 Master의 죽음을 파악하고, Slave중 하나가 Master로 승격된다. 중단없는 서비스를 제공. 기존 Master가 다시 살아나면 새로운 Master의 Slave가 된다
    
    - 클러스터는 센티넬보다 더 발전된 형태라고 합니당 센티넬은 One Master 구조이기 때문에 데이터 사이즈가 커지면 스케일 UP을 해야하는데, 클러스터는 스케일 OUT이 가능하니 추후 확장성을 위해서 Cluster를 사용하는것이 좋다고 하네욧ㅎ
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/33dce518-25b7-4efa-9823-cc82f17897a6/Untitled.png)
    
- Pub/Sub이란 ? (컨텝) 그리고 Redis Pub/sub 사용한 이유 ( 보강해욧?))
    
    publish/subscribe 메시지 기반의 미들웨어 시스템을 말한다.
    메시지를 보내고(publish) 이를 받는(subscribe) 형태의 통신
    스프링에서는 Spring - Data - Redis 모듈을 로드함으로써 쉽게 pub/sub을 구현할 수 있었음.
    

## 알고리즘

- DFS 와 BFS 의 차이
- 그래프와 트리의 차이
- 빅오 표기버에 대해 설명
- Dynamic Programming이란?
    
    복잡한 문제를 간단한 여러 개의 문제로 나누어 푸는 방법이다. 즉 , 큰 문제를 작은문제로 나누어 푸는 문제를 일컫는말이다. 작은 문제가 반복이 일어날 경우, 같은 문제는 구할때마다 정답이 같을때 동적프로그래밍을 사용할 수 있다. 
    

## 네트워크

- HTTP와 HTTPS의 차이
    
    SSL 인증서에 있다. SSL인증서는 사용자가 사이트에 제공하는 정보를 암호화 한다. 
    SEO품질에도 있다. https로 전환하게 되면 검색엔진최적화(SEO)에 있어도 큰 혜택을 볼 수 있다. 
    
- HTTPS의 단점
    
    설치 및 인증서를 유지하는데 추가 비용이 발생한다, 암호화하는 과정이 웹서버에 부하를 주며, http에 비해 속도가 느리고 인터넷 연결이 끊긴 경우 재인증 시간이 소요
    
- HTTP의 메서드 종류, 언제 사용하는지,서버단의 리소스를 사용할 때는 무엇을 사용하는지
    
    GET
    HEAD
    POST
    PUT
    DELETE
    CONNECT
    OPTIONS
    TRACE
    PATCH
    
- HTTP 상태코드 아는대로 설명
    
    -1XX : (정보) 요청을 받았으며 프로세스를 계속 한다.
    
    -2XX:(성공) 요청을 성공적으로 받았으며 인식했고 수용했다.
    
    -3XX:(리다이랙션) 요청 완료를 위해 추가 작업 조치가 필요하다
    
    -4XX:(클라이언트오류)요청의 문법이 잘못 되었거나 요청을 처리할 수 없다.
    
    - 4XX
        
        400:잘못된요청
        401:권한없음.인증실패
        403:금지됨. 인가실패
        404:서버가 요청한 페이지를 찾을수 없음. 존재하지 않는 페이지에 대한 요청
        
    
    -5XX:(서버오류)서버가 명백히 유효한 요청에 대해 충족을 실패했다.
    
    - 5XX
        
        500:내부 서버 오류
        501:서버에 요청을 수행할 수 있는 기능이 없음. 서버가 요청 메소드를 인식하지 못할때
        
- TCP/IP 란 ? 4계층에대해서도 설명해봐
    
    TCP(Transmission Control Protocol) :
    
    인터넷 프로토콜 슈트중 TCP와 IP가 가장 많이 쓰이기 때문에 TCP/IP 프로토콜 슈트라고도 한다. TCP는 네트워크 계층 중 (OSI7계층) 전송 계층에서 사용하는 프로토콜로서, 장치들 사이에 논리적인 접속을 성립하기 위하여 연결을 설정하여 신뢰성을 보장하는 **연결형 서비스**이다. (송신자의 수신자를 연결해준다 - UDP와의 차이)
    
    TCP/IP를 말한다는 것은 송신자가 수신자에게 IP주소를 사용하여 데이터를 전달하고, 그 데이터가 제대로 갔는지, 너무 빠르지는 않았는지, 제대로 받았다고 연락은 오는지에 대한 이야기를 하는것이다(so sweet...)
    
    Transport Layer(OSI 7계층중 4Layer)
    
    저기 초록색 칸 ㅎㅎ
    저기가 송신자와 수신자의 논리적 연결을 담당하는 부분이며, 신뢰성 있는 연결을 유지할 수 있는지 도와준다. Endpoint(사용자)간의 연결을 생성하고 데이터를 얼마나 보냈는지 제대로 받았는지 등을 확인한다. TCP랑  UDP가 대표적임
    
    ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/cc6da962-06e2-4eea-901d-265fe6db85dd/Untitled.png)
    
- URL과 URI의 차이점
    
    URI(Uniform Resource Identifier)은 URL(Uniform Resource Locator)의 상위 개념이고, URL은 하위 개념이다.URL은 어떻게 리소스를 얻을 것이고 어디에서 가져와야 하는지 명시하는 URI이다.
    +URN은 리소스를 어떻게 접근할것인지 명시하지 않고 경로와 리소스 자체를 특정하는 것을 목표로 하는 URI이다.
    
- DNS란?
    
    domain name System
    사람이 읽을 수 있는 도메인 이름을 머신이 읽을 수 있는 IP주소로 변환하는것
    
- CDN이란?
    
    Content Delivery Network - 지리적 제약 없이 전 세계 사용자에게 빠르고 안전하게 콘텐츠를 전송하는 콘텐츠 전송 기술. 서버와 사용자 사이의 물리적인 거리를 줄여 콘텐츠 로딩에 소요되는 시간을 최소화한다. 각 지역에 캐시서버(PoP, Points of Presence)를 분산 배치해서, 근접한 사용자의 요청에 원본서버가 아닌 캐시서버가 콘텐츠를 전달한다.
    
- Rest란?
    
    지은님 화이팅!!
    
    http URI를 통해 자원을 명시하고, method를 통해 자원에 대한 crud operation을 적용하는 것을 의미
    or
    분산 시스템 설계를 위한 아키텍쳐 스타일(제약조건의 집합)
    
    + soap(simple object Access Protocol) : 다른 언어로 다른 플랫폼에서 빌드된 애플리케이션이 통신할 수 있도록 설계된 최초의 표준 프로토콜이다. (REST와의 차이는 SOAP은 프로토콜이지만, REST는 프로토콜이 아니다. 얘는 원칙 세트임)
    
- Restful API란?
    
     REST 아키텍쳐 원칙을 모두 만족하는 API...
    REST에서 젤 중요한 항목!!
    1.URI는 정보의 자원을 표현한다
    2. 자원에 대한 행위는 HTTP Method(GET. POST. PUT .DELETE)로 표현한다.
    
- REST를 사용하는 이유 **분산시스템**
    
    거대한 애플리케이션을 모듈, 기능별로 분리하기 쉬워졌다.
    Restful API를 서비스하기만 하면 어떤 다른 모듈 도는 애플리케이션이라도 Restful API를 통해 상호간의 통신을 할 수 있기 때문
    
    웹페이지를 위한 HTML 및 이미지 등을 보내던 것과 달리 이제는 데이터만 보내면 여러 클라이언트에서 해당 데이터를 적절하게 보내주기만 하면 된다. Restful API를 사용하면서 데이터만 주고 받기 때문에 여러 클라이언트가 자유롭고 부담없이 데이터를 이용할 수 있다. (????????)서버도 요청한 데이터만 깔끔하게 보내주면 되기 때문에 가볍고 유지보수성도 좋다
    
- SSH란?
    
    Secure Shell , 원격 호스트에 접속하기 위해 사용되는 보안 프로토콜
    SSH를 구성하는 색심은 열쇠 key이다. 사용자랑 서버는 각각 키를 보유하고 이 키를 통해 연결 상대를 인증하고 안전하게 데이터를 주고 받는것
    
- 쉘이란?
    
    shell?
    사용자의 명령어를 해석하고 운영체제가 알아들을 수 있게 지시해주는것임, **사용자와 커널(운영체제의 핵심. 시스템의 모든것을 통제. 하드웨어에 직접적으로 명령내림)을 이어주는 것**
    윈도우에선는 cmd로 Mac에서는Ternimal로 셸을 실행할 수 있음
    
    + 셸이랑 터미널/콘솔은 다른 의미임. 셸은 글자를 입력하여 컴퓨터에 명령할 수 있도록 하는 프로그램이며, 셸을 실행하기 위해 글자 입력을 받아 컴터에 전달하거나 컴퓨터의 출력을 글자 화면에 쓰는 프로그램임. 일종의 셸의 도구ㅎ
    
- 2개 이상의 서버가 존재할때 유의해야할 점
    
    ?????????????????????????????
    

## 디자인 패턴

- 디자인 패턴이란?
    
    기존 환경 내에서 반복적으로 일어나는 문제들을 어떻게 풀어나갈 것인가에 대한 일종의 솔루션 같은 것입니다. 디자인 패턴 계의 교과서로 불리는 **[GoF의 디자인패턴]**에서는 객체지향적 디자인 패턴의 카테고리를 **"생성 패턴(Creational Pattern)"**, **"구조 패턴(Structural Pattern)"**, **"행동 패턴(Behavioral Pattern)"** 3가지로 구분하고 있습니다.
    
- GoF 디자인 패턴의 종류
    
    디자인 패턴 - 프로그래밍 할때에 문제를 해결하고자 코드의 구조들을 일정한 형태로 만들어
    재이용하기 편리하게 만든 일정한 패턴
    
    GOF 디자인 패턴 - 네명의 컴퓨터과학 연구자들이 소개한 대표적인 디자인패턴 방식
    
    GOF 디자인 패턴의 종류 - 1. 생성패턴 2. 구조 패턴 3. 행위 패턴 
    
- 스트래티지 패턴이란?
    
    
    - 행위를 클래스로 캡슐화해 동적으로 행위를 자유롭게 바꿀 수 있게 해주는 패턴
    같은 문제를 해결하는 여러 알고리즘이 클래스별로 캡슐화되어 있고 이들이 필요할 때 교체할 수 있도록 함으로써 동일한 문제를 다른 알고리즘으로 해결할 수 있게 하는 디자인 패턴
    - 전략을 쉽게 바꿀 수 있도록 해주는 디자인 패턴이다.
    
    - 특히 게임 프로그래밍에서 게임 캐릭터가 자신이 처한 상황에 따라 공격이나 행동하는 방식을 바꾸고 싶을 때 스트래티지 패턴은 매우 유용하다.
    [https://gmlwjd9405.github.io/2018/07/06/strategy-pattern.html](https://gmlwjd9405.github.io/2018/07/06/strategy-pattern.html)
- 싱글턴 패턴이란?
    
    애플리케이션이 시작될때 어떤 클래스가 최초 한번만 메모리를 할당하는것 이라고한다.
    
    내가공부한것중에서 서블릿이 이렇게 동작한다고 하는데 클라이언트가 서버에게 어느서블릿을 최초로 요청했을시에 메모리를 할당하고(객체를 만들고), 다음요청부턴 새로 만드는것이아닌 기존에 있던 객체를 사용하는것이다.
    
    이와 반대인것이 CGI프로그램 이라고 하는것인데, CGI프로그램은 클라이언트로 요청이 있을때마다 독립적인 프로세스가 만들어진다. 서버에 3개의 요청이있으면 3개의 프로세스가 만들어지고, 하나의 프로세스를 띄우기 위해 필요한 데이터가 5라고 가정하면 15만큼의 데이터가 메모리에 로딩되는데, 이런 실행방식은 사용자의 요청이 빈번한 웹 서비스로는 적합하지 않다. 그래서 싱글톤을 사용하는 것이라고한다. 싱글톤은 동시요청이 오면 스레드로 처리한다고하는데 스레드도 한번 공부해봐야겠다.
    
- 커맨드 패턴이란?
    
    커맨드 패턴은 객체의 행위( 메서드 )를 클래스로 만들어 캡슐화 하는 패턴입니다.
    
    즉, 어떤 객체(A)에서 다른 객체(B)의 메서드를 실행하려면 그 객체(B)를 참조하고 있어야 하는 의존성이 발생합니다.
    
    그러나 커맨드 패턴을 적용하면 의존성을 제거할 수 있습니다.
    
    [https://victorydntmd.tistory.com/295](https://victorydntmd.tistory.com/295)
    
- 옵서버 패턴이란?
    
    옵저버 패턴(observer pattern)은 객체의 상태 변화를 관찰하는 관찰자들, 즉 옵저버들의 목록을 객체에 등록하여 상태 변화가 있을 때마다 메서드 등을 통해 객체가 직접 목록의 각 옵저버에게 통지하도록 하는 디자인 패턴이다. 주로 분산 이벤트 핸들링 시스템을 구현하는 데 사용된다. 발행/구독 모델로 알려져 있기도 하다.
    
    [https://pjh3749.tistory.com/266](https://pjh3749.tistory.com/266)
    
- 데커레이터 패턴이란?
    
    데커레이터는 어떤 기능에 추가적으로 기능을 덧붙이고 싶은 경우, 그 기능들을 Decorator로 만들어서 덧붙이는 방식입니다.
    
    [https://victorydntmd.tistory.com/297](https://victorydntmd.tistory.com/297)
    
- 템플릿 메서드 패턴이란?
    
    어떤 작업을 처리하는 일부분을 서브 클래스로 캡슐화해 전체 일을 수행하는 구조는 바꾸지 않으면서 특정 단계에서 수행하는 내역을 바꾸는 패턴
    [https://gmlwjd9405.github.io/2018/07/13/template-method-pattern.html](https://gmlwjd9405.github.io/2018/07/13/template-method-pattern.html)
    
- 팩토리 메서드 패턴이란?
    
    객체 생성 처리를 서브 클래스로 분리 해 처리하도록 캡슐화하는 패턴
    [https://gmlwjd9405.github.io/2018/08/07/factory-method-pattern.html](https://gmlwjd9405.github.io/2018/08/07/factory-method-pattern.html)
    
- 추상팩토리 패턴이란?
    
    서로 관련이 있는 객체들을 통째로 묶어서 팩토리 클래스로 만들고, 이들 팩토리를 조건에 따라 생성하도록 다시 팩토리를 만들어서 객체를 생성하는 패턴
    
    [https://victorydntmd.tistory.com/300](https://victorydntmd.tistory.com/300)
    
- 컴퍼지트 패턴이란?
    
    여러 개의 객체들로 구성된 복합 객체와 단일 객체를 클라이언트에서 구별 없이 다루게 해주는 패턴
    [https://gmlwjd9405.github.io/2018/08/10/composite-pattern.html](https://gmlwjd9405.github.io/2018/08/10/composite-pattern.html)
    

## 운영체제 (OS)

- 운영체제란?
    
    운영체제(Operating System)는 컴퓨터 시스템의 자원들을 효율적으로 관리하며, 사용자가 컴퓨터를 편리하고, 효과적으로 사용할 수 있도록 환경을 제공하는 여러 프로그램의 모임
    
- osi 7계층
    
    **[제 1계층] 물리 계층(Physical Layer):** 시스템의 물리적 전기적 표현을 나타내는 층위입니다. 케이블 종류, 무선 주파수 링크, 핀, 전압 등의 물리적인 요건을 의미합니다. 라우터나 스위치의 전원이 켜져있는지, 케이블이 제대로 연결되어있는지 여부 등에 모두 1계층인 물리 계층에 해당되는 이야기입니다.
    
    **[제 2계층] 데이터 링크 계층(Data Link Layer):** 데이터 링크 계층은 직접적으로 연결된 두 개의 노드 사이에 데이터 전송을 가능하게 하고, 물리 계층에서 발생한 오류를 수정하기도 합니다. 또한 대부분의 스위치는 바로 2계층인 데이터 링크 계층에서 작동합니다.
    
    **[제 3계층] 네트워크 계층(Network Layer):** 네트워크의 핵심인 라우팅(데이터가 가야 할 길을 찾는 기능)의 대부분이 3계층인 네트워크 계층에서 작동합니다. 이 계층은 여러 대의 라우터들을 바탕으로 데이터를 패킷 단위로 잘게 쪼개어 전송하는 층위에 해당합니다. 데이터가 전송될 수 있는 수 많은 경우의 수 중 가장 효율적인 라우팅이 방법을 찾는 것 또한 이 단계에서 가능해집니다.
    
    **[제 4계층] 전송 계층(Transport Layer):** 전송 계층은 보내고자 하는 데이터의 용량과, 속도, 목적지를 처리합니다. 전송 계층에 가장 대표적인 것은 전송 제어 프로토콜(TCP)입니다. TCP는 인터넷 프로토콜(IP) 위에 구축되기 때문에 TCP/IP로 알려져 있습니다.
    
    **[제 5계층] 세션 계층(Session Layer):** 5계층에서 실제 네트워크 연결이 이뤄집니다. 두 대의 기기가 ‘대화’하기 위해서는 하나의 ‘세션’이 열려야만 합니다. 세션 계층에서는 프로세스간의 통신을 제어하고, 통신과정이 진행될 때 동기화를 유지하는 역할을 합니다.
    
    **[제 6계층] 표현 계층(Presentation Layer):** 응용프로그램 형식을 네트워크 형식으로 변환하거나 그 반대의 경우가 일어나는 계층이 표현 계층입니다. 6계층은 응용프로그램 혹은 네트워크를 위해 데이터를 ‘표현’하는 계층에 해당합니다. 대표적인 예로 데이터를 안전하게 주고 받기 위해 암호화하고 복호화 하는 과정이 필요한데 이러한 과정이 바로 표현 계층인 6계층에서 이루어집니다.
    
    **[제 7계층] 응용 계층(Application Layer):** 마지막 응용 계층은 사용자가 네트워크에 접근할 수 있도록 인터페이스를 제공하는 계층입니다. 사용자에게 가장 직접적으로 보이는 부분이 바로 이 응용 계층에 해당하는 것입니다. 구글의 크롬과 같은 브라우저나 스카이프, 아웃룩 등의 응용프로그램이 이 응용 계층에서 동작합니다.
    
    [https://www.sharedit.co.kr/posts/7482](https://www.sharedit.co.kr/posts/7482)
    
- Thread와 Process의 차이
    
    **Process**
    
    프로세스는 각각 독립된 메모리 영역(Code, Data, Stack, Heap의 구조)을 할당받는다.
    기본적으로 프로세스당 최소 1개의 스레드(메인 스레드)를 가지고 있다.
    
    **Thread**
    
    스레드는 한 프로세스 내에서 동작되는 여러 실행의 흐름으로, 프로세스 내의 주소 공간이나 자원들(힙 공간 등)을 같은 프로세스 내에 스레드끼리 공유하면서 실행된다.
    
    [https://gmlwjd9405.github.io/2018/09/14/process-vs-thread.html](https://gmlwjd9405.github.io/2018/09/14/process-vs-thread.html)
    
- Multi-Thread,Multi-proccess를 쓴다면 주로 언제?
    
    [https://wooody92.github.io/os/멀티-프로세스와-멀티-스레드/](https://wooody92.github.io/os/%EB%A9%80%ED%8B%B0-%ED%94%84%EB%A1%9C%EC%84%B8%EC%8A%A4%EC%99%80-%EB%A9%80%ED%8B%B0-%EC%8A%A4%EB%A0%88%EB%93%9C/)
    
    멀티프로세스 - 하나의 프로세스가죽어도 다른 프로세스는 멀쩡함 (안정적임)
    
    멀티 스레드 - 프로세스를 생성하여 자원을 할당하는 시스템 콜이 줄어 자원을 효율적으로 관리, 하지만 하나의 스레드에 문제가생기면 프로세스에 문제가 생길수도있음 (자원효율성 증대, 안정성 떨어짐)
    
- 동기화 객체의 종류
    - 크리티컬 섹션 (CriticalSection)
        - 주요 보호 대상은 전역 객체이고 Lock, UnLock을 사용하여 자원의 동기화를 유지시킨다.
        - 한 시스탬 내에서 여러 스레드가 실행 중이라고 하더라도 실제로 CPU를 점유하여 연산을 하는 스레드는 하나이다. 코어가 두개라면 두 스레드가, 네 개라면 네 스레드가 동시에 실행 중일수 있다. 여러 스레드는 운영체제가 정하는 스케쥴에 따라 컨텍스트 스위칭을 하면서 실행된다는 것이 더 중요하다.
        - 크리티컬 섹션 객체로 보호하는 대상은 주로 전역 객체이다. 그중에서도 메모리와 관련된 대상은 반드시 그렇게 해야 멀티스레드 환경에서 문제가 되지 않는다.
    - 뮤텍스 (Cmutex)
        - CMutex 클래스는 커널 뮤텍스를 객체화한 MFC클래스이다. 스레드와 프로세스를 동기화 시키는데도 사용한다. 일반적으로 스레드를 동기화 시킬때에는 뮤텍스가 아니라 크리티컬 섹션을 사용할 것을 권장한다. 이유는 뮤텍스가 동기화를 하는데 드는 비용이 크리티컬 섹션에 비해 크기 때문이다. 그렇다고 체감하기는 어렵지만 효율적으로 프로그래밍 하려면 고려해야하는 영역이다.
    - **세마포어(Semaphore)**
        - 크리티컬 섹션이나 뮤텍스가 한 번에 한 스레드나 프로세스만 특정 리소스에 접근할 수있었던 것과달리동시에 여러 스레드나 프로세스가 특정 리소스에 접근할수 있도록 임의로 허용치를 정할 수 있다. 만일 10개의 스레드가 동시에 실행되는 멀티스레드 시스템에서 3개의 스레드만 리소스에 동시 접근이 가능하다면 일럴때 적합한 동기화 객체가 바로 세마포어이다.
        - 서버 응용 프로그램에서 이런 구조가 절시하게 필요하다. 만일 동시에 최대 1000명까지 처리하는 서버가 있다고가정할대 일반 서비스의 경우에는 1000명 클라이언트 모두에게 서비스가가능하지만 특정 서비스만큼은 동시 접속을 10명까지로 서시브 제한을 두어야할 수도 있다. 이럴 경우에는 세마포어는 최선의 동기화 방법이 된다.
- 동기 비동기 차이
    
    **동기방식 (Synchronous)**
    
    요청을 보낸 후 응답(=결과)를 받아야지만 다음 동작이 이루어지는 방식이다.
    
    어떠한 일을 처리할 동안 다른 프로그램은 정지한다.
    
    **비동기 방식 (Asynchronous)**
    
    요청을 보낸  후 응답(=결과)와는 상관없이 다음방식이 동작하는 방식이다.
    
- 메모리 관리 전략
    
    **1) 연속 메모리 할당**
    
    - 프로세스를 메모리에 연속적으로 할당하는 기법
    - 할당과 제거를 반복하다보면 Scattered Holes가 생겨나고 이로 인한 외부 단편화가 발생
    
    (1) 연속 메모리 할당에서 외부 단편화를 줄이기 위한 할당 방식
    
    a. 최초 적합(First fit)
    
    - 가장 처음 만나는 빈 메모리 공간에 프로세스를 할당
    - 빠름
    
    b. 최적 적합(Best fit)
    
    - 빈 메모리 공간의 크기와 프로세스의 크기 차이가 가장 적은 곳에 프로세스를 할당
    
    c. 최악 적합(Worst fit)
    
    - 빈 메모리 공간의 크기와 프로세스의 크기 차이가 가장 큰 곳에 프로세스를 할당
    - 이렇게 생긴 빈 메모리 공간에 또 다른 프로세스를 할당할 수 있을 거라는 가정에 기인
    
    **2) 페이징(Paging)**
    
    - 메모리 공간이 연속적으로 할당되어야 한다는 제약조건을 없애는 메모리 관리 전략
    - 논리 메모리는 고정크기의 페이지, 물리메모리는 고정크기의 프레임 블록으로 나누어 관리
    - 프로세스가 사용하는 공간을 논리 메모리에서 여러 개의 페이지로 나누어 관리하고, 개별 페이지는 순서에 상관없이 물리 메모리에 있는 프레임에 매핑되어 저장
    - MMU(Memory Management Unit)의 재배치 레지스터 방식을 활용해 CPU가 마치 프로세스가 연속된 메모리에 할당된 것처럼 인식하도록 함
    - 내부 단편화 발생
    
    **3) 세그멘테이션(Segmentation)**
    
    - 페이징 기법과 반대로 논리 메모리와 물리 메모리를 같은 크기의 블록이 아닌, 서로 다른 크기의 논리적 단위인 세그먼트로 분할
    - 외부 단편화 발생
    
    **4) 세그멘테이션 페이징 혼용 기법**
    
    - 페이징과 세그멘테이션도 각각 내부 단편화와 외부 단편화가 발생
    - 페이징과 세그멘테이션을 혼용해 이러한 단편화를 최대한 줄이는 전략
    - 프로세스를 세그먼트(논리적 기능 단위)로 나눈 다음 세그먼트를 다시 페이지 단위로 나누어 관리
    - 매핑 테이블을 두 번 거쳐야하므로 속도가 느려짐
- 가상 메모리란?
    
    가상 메모리 또는 가상 기억 장치는 메모리 관리 기법의 하나로, 기계에 실제로 이용 가능한 기억 자원을 이상적으로 추상화하여 사용자들에게 매우 큰 메모리로 보이게 만드는 것을 말한다
    
- 데드락의 개념과 조건
    
    교착 상태란 두 개 이상의 작업이 서로 상대방의 작업이 끝나기 만을 기다리고 있기 때문에 결과적으로 아무것도 완료되지 못하는 상태를 가리킨다.
    
    데드락이 발생하기 위한 조건은 크게 4가지로 말할 수 있습니다.
    
    - **상호 배제**
        - **한 번에 프로세스 하나만 해당 자원을 사용할 수 있다**. 사용 중인 자원을 다른 프로세스가 사용하려면 요청한 자원이 해제될 때까지 기다려야 한다.
    - **점유 대기**
        - 자원을 최소한 하나 보유하고, 다른 프로세스에 할당된 자원을 점유하기 위해 대기하는 프로세스가 존재해야 한다.
    - **비선점**
        - 이미 할당된 자원을 강제로 빼앗을 수 없다(비선점).
    - **순환 대기**
        - 대기 프로세스의 집합이 순환 형태로 자원을 대기하고 있어야 한다.
    
- 외부 단편화와 내부 단편화
    
    [https://m.blog.naver.com/rbdi3222/220623825770](https://m.blog.naver.com/rbdi3222/220623825770)
    
- 메모리 구조
    
    ### **1. Stack 영역**
    
    메모리의 Stack 영역은 함수의 호출과 관계되는 **지역변수(local variable)와 매개변수(parameter)**가 저장되는 영역이다.
    
    Stack 영역은 함수의 호출과 함께 할당되며, 함수의 호출이 완료되면 소멸한다.
    
    이렇게 Stack 영역에 저장되는 **함수의 호출 정보**를 **스택 프레임(stack frame)**이라고 한다.
    
    Stack 영역은 **푸시(push)** 동작으로 데이터를 저장하고, **팝(pop)** 동작으로 데이터를 인출한다.
    
    이러한 Stack은 **후입선출(LIFO, Last-In First-Out)** 방식에 따라 동작하므로, 가장 늦게 저장된 데이터가 가장 먼저 인출된다.
    
    Stack 영역은 **메모리의 높은 주소에서 낮은 주소의 방향**으로 할당된다.
    
    Stack 영역이 높은 주소에서부터 주소값을 채워 내려오다가 Heap 영역을 침범하는 경우 **Stack Overflow**가 발생한다.
    
    ### **2. Heap 영역**
    
    메모리의 Heap 영역은 **사용자가 직접 관리**할 수 있는 (+ 관리해야 하는) 메모리 영역이다.
    
    Heap 영역은 사용자에 의해 메모리 공간이 **동적으로 할당되고 해제**된다. ([위키피디아 메모리 동적 할당](https://ko.wikipedia.org/wiki/%EB%8F%99%EC%A0%81_%EB%A9%94%EB%AA%A8%EB%A6%AC_%ED%95%A0%EB%8B%B9) 참고)
    
    Heap 영역은 **메모리의 낮은 주소에서 높은 주소의 방향**으로 할당된다.
    
    Heap 영역이 Stack 영역을 침범하는 경우 **Heap Overflow**가 발생한다.
    
    ### **3. Data 영역 / BSS 영역**
    
    메모리의 Data 영역은 프로그램의 **전역변수(global variable)와 정적변수(static variable)**가 저장되는 영역이다.
    
    RAM의 Data 영역에는 ROM의 Data 영역에서 복사된 초기화된 전역변수와 정적변수가 저장되어 있다.
    
    Data 영역은 **프로그램의 시작과 함께 할당**되며, 프로그램이 종료되면 소멸한다.
    
    전역변수와 정적변수를 선언할 때 **값을 초기화했으면 Data 영역**에 생성되고, **초기화하지 않았으면 BSS 영역**에 생성된다.
    
    BSS 영역은 프로그램 실행을 시작하기 전에 **OS 커널에 의해** **0으로 자동 초기화**된다.
    
    전역변수와 정적변수를 프로그램 내에서 초기화하지 않아도 0으로 자동 초기화되는 이유가 이 때문이다.
    
    BSS는 Block Started by Symbol의 약자다.
    
    더보기
    
    ### **4. Code 영역**
    
    메모리의 Code 영역은 **실행할 프로그램의 코드**가 저장되는 영역으로 **Text 영역**이라고도 부른다.
    
    CPU는 코드 영역에 저장된 명령어를 하나씩 가져가서 처리한다.
    
- 커널이란?
    
    커널은 다음과 같은 4가지 기능을 수행합니다.
    
    1. **메모리 관리:** 메모리가 어디에서 무엇을 저장하는 데 얼마나 사용되는지를 추적합니다.
    2. **프로세스 관리:** 어느 프로세스가 중앙 처리 장치(CPU)를 언제 얼마나 오랫동안 사용할지를 결정합니다.
    3. **장치 드라이버:** 하드웨어와 프로세스 사이에서 중재자/인터프리터의 역할을 수행합니다.
    4. **시스템 호출 및 보안:** 프로세스의 서비스 요청을 수신합니다.
- CPU 스케줄링이란? 대표적으러 뭐가있는지?
    
    프로세스(Process)가 구동하려면 다양한 시스템 자원이 필요하다. 대표적으로 CPU(중앙처리장치)와 입출력장치가 있는데, 최고의 성능을 내기 위해 자원을 어떤 프로세스에 얼마나 할당하는지 정책을 만드는 것
    
    **선점스케줄링**
    
    - CPU가 어떤 프로세스에 의해 점유 중일 때, 우선 순위가 높은 프로세스가 CPU를 차지할 수 있음
    
    **비선점 스케줄링**
    
    —위 와 반대
    
- 시스템콜이란?
    
    운영 체제의 커널이 제공하는 서비스에 대해, 응용 프로그램의 요청에 따라 커널에 접근하기 위한 인터페이스이다.
    
    - 종류
        - 프로세스 컨트롤
            - 프로세스 생성 및 종료
            - 메모리에 로드, 실행
            - 프로세스 속성 값 확인, 지정
            - wait 이벤트, signal 이벤트
            - 메로리 할당
        - 파일 메니지먼트
            - 파일 생성, 파일 삭제
            - 열기, 닫기
            - 읽기, 쓰기, Reposition
            - 파일 속성 값 확인, 지정
        - 디바이스 매니지먼트
            - 디바이스 요청 및 해제
            - 읽기, 쓰기, Reposition
            - 디바이스 속성 확인, 지정
            - 비 물리적인 디바이스 해제 및 장착
        - 정보 관리
            - 시간 확인, 시간 지정
            - 시스템 데이터 확인, 지정
            - 프로세스, 파일, 디바이스 속성 가져오기
            - 프로세스, 파일, 디바이스 속성 설정하기
        - 커뮤니케이션
            - 커뮤니케이션 연결 생성 및 삭제
            - 메시지 송신, 수신
            - 상태 정보 전달
            - remote 디바이스 해제 및 장착
        - 보안
            - Permission 획득
            - Permission 설정

## 테스트 코드

- JUnit이란?
    
    junit이란 java의 단위 테스트(Unit Test) 도구이다. 테스트 결과를 문서로 남기는 것이 아니라 Test Class 자체를 남겨 리팩토링을 하거나 소스코드가 변해도 해당 코드가 제대로 동작하는지 테스트 코드를 가지고 그대로 테스트 할 수도 있고, 미래에 이 기능을 맡게될 개발자에게 테스트 방법 및 클래스의 histroy를 넘겨줄 수도 있다. 하나의 jar파일로 되어있다.
    
- Mock이란?
    
    Mock 이란 ? -  단위테스트코드를 작성하다 보면  Controller→Service→Repository 이런식으로 의존성이 있을때 Service 단위테스트를 하려면 어쩔수없이 Repository까지 써야하는 상황이 오는데 이렇게되면 단위테스트와는 안맞게된다. Service하나만을 테스트 해야하는데 Repository까지 써야하는 상황이니까. 그래서 가짜 Repository역할을 하는 객체를 Mock이라고 부름.
    
- 테스트 코드의 장점 및 어떤 생각하면서 작성하는지?
    - **실행가능 설명서** : 엑셀 문서같이 테스트 결과여부 기록이 아닌 실제로 메서드가 요구사항대로 작동하는지 확인가능하다.
    - **테스트 시간 단축** : 불필요하게 수작업으로 할 필요가 없다. 코드상에서 테스트할 값만 넣으면 끝난다.
    - **유연성 제공 :** 수정사항이 생겨도 기존 기능들에 영향을 주는지 손쉽게 확인할 수 있다. 사이드이펙트에 대한 대비가 쉬워진다.
    - **재사용성 가능 :** 가장 큰 장점이다. 코드만 실행하면 테스트가 끝난다
    
    해당 기능의 모든 테스트케이스를 생각하면서 작성한다.
    
- 테스트 코드 작성 시 중요하게 생각한 부분 및 중요성
    
    
- TDD란 무엇이며 장단점은?
    
    테스트코드를 작성하면서 설계하는 방식
    
    # **TDD 개발 방식의 장점**
    
    ### **보다 튼튼한 객체 지향적인 코드 생산**
    
    TDD는 코드의 재사용 보장을 명시하므로 TDD를 통한 소프트웨어 개발 시 기능 별 철저한 모듈화가 이뤄진다.
    
    이는 종속성과 의존성이 낮은 모듈로 조합된 소프트웨어 개발을 가능하게 하며 필요에 따라 모듈을 추가하거나 제거해도 소프트웨어 전체 구조에 영향을 미치치 않게 된다.
    
    ### **재설계 시간의 단축**
    
    테스트 코드를 먼저 작성하기 때문에 개발자가 지금 무엇을 해야하는지 분명히 정의하고 개발을 시작하게된다. 또한 테스트 시나리오를 작성하면서 다양한 예외사항에 대해 생각해 볼 수 있다. 이는 개발 진행 중 소프트웨어의 전반적인 설계가 변경되는 일을 방지할 수 있다.
    
    ### **디버깅 시간의 단축**
    
    이는 유닛 테스팅을 하는 이점이기도하다. 예를 들면 사용자의 데이터가 잘못 나온다면 DB의 문제인지, 비즈니스 레이어의 문제인지 UI의 문제인지 실제 모든 레이어들을 전부 디버깅 해야하지만, TDD의 경우 자동화 된 유닛 테스팅을 전제하므로 특정 버그를 손 쉰게 찾아낼 수 있다.
    
    ### **테스트 문서의 대체 가능**
    
    주로 SI 프로젝트 진행 과정에서 어떤 요소들이 테스트 되었는지 테스트 정의서를 만든다. 이것은 단순 통합 테스트문서에 지나지 않는다. 하지만 TDD를 하게 될 경우 테스팅을 자동화 시킴과 동시에 보다 정확한 테스트 근거를 산출 할 수 있다.
    
    ### **추가 구현의 용의함**
    
    개발이 완료된 소프트웨어에 어떤 기능을 추가할 때 가장 우려되는 점은 해당 기능이 기존 코드에 어떤 영향을 미칠지 알지 못한다는 것이다. 하지만 TDD의 경우 자동화된 유닛 테스팅을 전제하므로 테스트 기간을 획기적으로 단축시킬 수 있다.
    
    > 이러한 TDD의 장점에도 불구하고 모두가 이 개발 프로세스를 따르는 것은 아니다. 그 이유는 무엇일까?
    > 
    
    # **TDD 개발 방식의 단점**
    
    ### **가장 큰 단점은 바로 생산성 저하이다.**
    
    개발 속도가 느려진다고 생각하는 사람이 많기 때문에 TDD에 대해 반신반의 한다.
    
    왜냐하면 처음부터 2개의 코드를 짜야하고 중간중간 테스트를 하면서 고쳐나가야하기 때문이다.
    
    TDD 방식의 개발 시간은 일반적인 개발 방식에 비해 대략 10~30% 정도로 늘어난다.
    
    SI 프로젝트에서는 소프트웨어의 품질보다는 납기일 준수가 훨씬 중요하기 때문에 TDD 방식을 잘 사용하지 않는다.
    
- TDD를 어떻게 생각하시나요?
    
    저한텐 아직 어려운 방식인것 같습니다.
    

---

## 기타

- 레이어드 아키텍처란?
    
    구성요소들이 수평적인 레이어로 조직화되어 있응 다층 구조이다. 대부분의 소프트웨어를 구성하는 일반적인 방법이며 모든 구성요소가 연결되어 있지만 독립적인 방식이다. 
    
    - Presentation Layer
        - 최종 사용자에게 UI를 제공하거나 클라이언트로 응답을 다시 보내는 역할을 담당하는 모든 클래스 포함한다. 즉 API의 엔드포인트를 정의하고 전송된 HTTP요청들을 읽어 들이는 로직을 구현한다.
    - Business Layer
        - 접근성,보안,인증과 같은 로직이 해당 계층에서 발생한다. ESB(Enterprise Service Bus), 미들웨어, 유효성 검사등을 수행한다.
        - 실제 시스템이 구현해야하는 로직들을 이 레이어에서 구현한다.
    - Persistence Layer
        - 이 계층은 DAO,ORM등을 포함한다. 데이터베이스에서 데이터를 저장,수정,불러 들이는 등 데이터 베이스와 관련된 로직을 구현한다.
    - Database Layer
        - 모든 데이터베이스가 저장되는 레이어
    
    특징 - 하위 레이어에 의존한다.
    
- 함수형 프로그래밍이란 무엇인가?
    
    함수를 이용한 프로그래밍으로, 함수를 인자값으로 사용하거나 리턴값으로 사용할 수 있으며, 가변 데이터를 지양하고 순수 함수를 만들어 모듈화 수준을 높이는 프로그래밍 패러다임중 하나이다.
    
- 템플릿 엔진이란?
    
    템플릿 양식과 특정 데이터 모델에 따른 입력 자료를 합성하여 결과 문서를 출력하는 소프트웨어(또는 소프트웨어 컴포넌트)를 말합니다.
    
    **웹 템플릿 엔진(Web Template Enging)**
    
    - **웹 문서가 출력되는 템플릿 엔진을 말합니다.**
    - 즉, **웹 템플릿 엔진은  웹 템플릿들(Web Templates)과 웹 컨텐츠 정보(Content Information)를 처리하기 위해 설계된 소프트웨어**입니다.
- 프레임워크와 라이브러리의 차이
    - 프레임워크
        - 소프트웨어 어플리케이션이나 솔루션의 개발을 수월하게 하기 위해 소프트웨어의 구체적 기능들에 해당하는 부분의 설계와 구현을 재사용 가능하도록 협업화된 형태로 제공하는 소프트웨어 환경을 말한다.
    - 라이브러리
        - 소프트웨어를 개발할 때 컴퓨터 프로그램이 사용하는 비휘발성 자원의 집합니다.개발자가 개발하는데 필요한 것들을 모아둔 도구들의 나열로 필요할 때 호출하여 사용하는 방식을 취하고 있다.
    - 차이
        - 흐름에 대한 제어권한이 어디에 있느냐에 차이이다. 프레임워크는 전체적인 흐름을 자체적으로 가지고 있으며, 프로그래머가 그 안에 필요한 코드를 작성하는 반면 라이브러리는 사용자가 흐름에 대해 제어를 하며 필요한 상황에 가져다 쓰는 것이다. 즉 프레임워크에는 제어의 역전이 적용되어 있다.
- JSON이 무엇인가? JSON은 자료구조인가 String인가 아니면 뭐임?
    
    # JSON (JavaScript Object Notation)
    
    - JavaScript Object Notation라는 의미의 축약어로 데이터를 저장하거나 전송할 때 많이 사용되는 **경량의 DATA 교환 형식**
    - Javascript에서 객체를 만들 때 사용하는 표현식을 의미한다.
    - JSON 표현식은 사람과 기계 모두 이해하기 쉬우며 용량이 작아서, 최근에는 JSON이 XML을 대체해서 데이터 전송 등에 많이 사용한다.
    - JSON은 데이터 포맷일 뿐이며 어떠한 통신 방법도, 프로그래밍 문법도 아닌 단순히 데이터를 표시하는 표현 방법일 뿐이다.
    
    ## JSON 특징
    
    - 서버와 클라이언트 간의 교류에서 일반적으로 많이 사용된다.
    - 자바스크립트 객체 표기법과 아주 유사하다.
    - 자바스크립트를 이용하여 JSON 형식의 문서를 쉽게 자바스크립트 객체로 변환할 수 있는 이점이 있다.
    - **JSON 문서 형식은 자바스크립트 객체의 형식을 기반으로 만들어졌다.**
    - 자바스크립트의 문법과 굉장히 유사하지만 **텍스트 형식일 뿐**이다.
    - 다른 프로그래밍 언어를 이용해서도 쉽게 만들 수 있다.
    - 특정 언어에 종속되지 않으며, 대부분의 프로그래밍 언어에서 JSON 포맷의 데이터를 핸들링 할 수 있는 라이브러리를 제공한다.
- 애자일 방법론
    
    **절차보**다는**사람** 즉 고객이 중심이 되어 다양한 현실 변화에 유연하고 신속하게 적응하면서 효율적으로 시스템을 개발할 수 있는 방법론입니다. 프로젝트 개발 후반부라도 고객의 요구사항을 적극 반영하고, 작동하는 소프트웨어를 고객에게 자주 전달하여 고객의 요구사항에 신속하게 적용해야 합니다.
    
    - 특징
        
        1) 애자일에 적합한 환경 : 고객의 요구사항이 자주 변동되는 경우 애자일에 적합합니다.
        
        2) 고객 참여도 : 고객이 프로세스에 협력하기 때문에 고객과 신속한 피드백이 가능합니다.
        
        3) 업무 모듈화 : 프로젝트를 여러부분으로 나누어 점진적으로 개발하며 신속하고 반복된 주기로 수행할 수 있습니다.
        
        4) 소규모에 적합 : 요구사항이 명확하지 않은 경우 또는 소규모 개발에 적합한 소프트웨어 방법론입니다.
        
- 좋은 코드란 무엇인가?
    
    제한된 자원을 목적에 맞게 효율적으로 사용해 문제를 해결하는 코드가 **좋은 코드**
    
    - **코드를 처음 보는 사람도 쉽게 따라가며 읽을 수 있을 것**
    - **내 의식의 흐름을 기억하지 않아도 언제든 원하는 기능을 다시 찾아갈 수 있을 것**
    - **5년 뒤에 내가 다시 보더라도 금세 이해할 수 있을 것**
    - **새로운 기능을 추가하더라도 크게 구조변경이 없을 것**
- Git: **merge --squash와 rebase의 차이점**