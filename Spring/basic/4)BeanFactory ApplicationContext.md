## BeanFactory
- 스프링 컨테이너의 최상위 인터페이스.
- 스프링 빈을 관리하고 조회하는 역할 담당.
- getBean() 제공.

## ApplicationContext
- BeanFactory기능을 모두 상속받아서 제공.
- 부가기능
  - 메시지소스를 활용한 국제화 기능. (MessageSource)
    - 한국에서 들어오면 한국어, 영어권 국가에서 들어오면 영어로.
  - 환경변수 (EnvironmentCapable)
    - 로컬, 개발, 운영등을 구분해서 처리.
  - 애플리케이션 이벤트 (ApplicationEventPublisher)
    - 이벤트를 발행하고 구독하는 모델을 편리하게 지원.
  - 편리한 리소스 조회 (ResourceLoader)
    - 파일, 클래스패스, 외부 등에서 리소스를 편리하게 조회.


ApplicationContext는 BeanFactory의 기능을 상속 받으며, 빈 관리기능 + 편리 부가 기능을 제공한다.
BeanFactory를 직접 사용할 일은 거의 없다. 부가기능이 포함된 ApplicationContext를 사용한다.
이 두가지를 우리는 스프링 컨테이너라고 한다.



### 다양한 설정 형식 지원 - 자바코드 XML
- 스프링 컨테이너는 다양한 형식의 설정 정보를 받아드릴 수 있게 유연하게 설계되어 있다.
  - 자바코드, XML, Groovy 등등


### 애노테이션 기반 자바 코드 설정 사용
- new AnnotationConfigApplicationContext(AppConfig.class)
- AnnotationConfigApplicationContext 클래스를 사용하면서 자바 코드로된 설정 정보를 넘기면 된다.

### XML
- 최근은 잘 사용하지 않지만 많은 레거시 프로젝트들이 XML로 되어있고, XML사용하면 컴파일 없이 빈 설정 정보를 변경할 수 있는 장점도 있다.
- GenericXmlApplicationContext 를 사용하면서 xml 설정 파일을 넘기면 된다.

```java
public class XmlAppContext {

    @Test
    void xmlAppContext() {
        ApplicationContext ac = new GenericXmlApplicationContext("appConfig.xml");
        MemberService memberService = ac.getBean("memberService", MemberService.class);
        assertThat(memberService).isInstanceOf(MemberService.class);
    }
}
```

```xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xsi:schemaLocation="http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd">

<!--    xml로 빈 등록 AppConfig랑 완전 같은 내용임-->
    <bean id="memberService" class="Springbasic.core.member.MemberServiceImpl" >
        <constructor-arg name="memberRepository" ref="memberRepository" />
    </bean>

    <bean id="memberRepository" class="Springbasic.core.member.MemoryMemberRepository" />

    <bean id="orderService" class="Springbasic.core.order.OrderServiceImpl">
        <constructor-arg name="memberRepository" ref="memberRepository" />
        <constructor-arg name="discountPolicy" ref="discountPolicy" />
    </bean>


    <bean id="discountPolicy" class="Springbasic.core.discount.RateDiscountPolicy" />
</beans>
```


## 스프링 빈 설정 메타 정보 BeanDefinition (추상화)
- 역할과 구현을 개념적으로 나눈 것.
- 스프링 컨테이너는 자바 코드인지, XML인지 상관없이 BeanDefinition을 알고 있으면 된다.
- @Bean, <bean> 당 각각 하나씩 메타 정보가 생성 된다.


- AnnotationConfigApplicationContext는 AnnotationBeanDefinitionReader를 사용해서 AppConfig.class를 읽고 BeanDefinition을 생성한다.
- GenericXmlApplicationContext는 XmlBeanDefinitionReader를 사용해서 appConfig.xml 설정 정보를 읽고 BeanDefinition을 생성한다.
- 새로운 형식의 정보가 추가 되면, XxxBeanDefinitionReader를 만들어서 BeanDefinition을 생성한다.

### BeanDefinition
- BeanClassName
  - 생성할 빈의 클래스명 (자바 설정 처럼 팩토리 역할의 빈을 사용하면 없음)
- factoryBeanName
  - 팩토리 역할의 빈을 사용할 경우 이름
- factoryMethodName
  - 빈을 생성할 팩토리 메서드 지정
- Scope
  - 싱글톤 (기본값)
- lazyInit
  - 스프링 컨테이너를 생성할 때 빈을 생성하는 것이 아니라, 실제 빈을 사용할 때 까지 최대한 생성을 지연처리 하는지 여부
- InitMethodName
  - 빈을 생성하고, 의존관계를 적용한 뒤에 호출되는 초기화 메서드 명
- DestoryMethodName
  - 빈의 생명주기가 끝나서 제거하기 직전에 호출되는 메서드 명
- Constructor arguments, Properties
  - 의존관계 주입에서 사용한다.(자바 설정 처럼 팩토리 역할의 빈을 사용하면 없음)