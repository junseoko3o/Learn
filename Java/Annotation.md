# Annotation

- @ 은 자바에서 코드사이에 주석처럼 쓰이며 특별한 의미,기능을 수행하도록 하는 기술이다
- 프로그램에게 추가적인 정보를 제공해주는 메타데이터라 볼수있다.(meta data : 데이터를 위한 데이터)
- 용도
- 컴파일러에게 코드 작성 문법 에러를 체크하도록 정보를 제공한다.
- 소프트웨어 개발 툴이 빌드나 배치시 코드를 자동으로 생성할 수 있도록 정보를 제공한다.
- 실행(런타임)시 특정기능을 실행하도록 정보를 제공한다.
- 기본적으로 어노테이션을 사용하는 순서는 아래와 같다.
- 어노테이션을 정의한다.
- 클래스에 어노테이션을 배치 한다.
- 코드가 실행되는 중에 Reflection을 이용하여 추가 정보를 획득하여 기능을 실시한다.

## **Reflection**

- 프로그램이 실행 중에 자신의 구조와 동작을 검사하고,조사하고,수정하는 것이다.
- 프로그래머가 데이터를 보여주고, 다른 포맷의 데이터를 처리하고,통신을 위해 serialization(직렬화)를 수행하고, bundling을 하기 위해 일반 소프트웨어 라이브러리를 만들도록 도와준다.
- Java와 같은 객체 지향 프로그래밍 언어에서 Reflection을 사용하면 컴파일 타임에 인터페이스,필드,메소드의 이름을 알지 못해도 실행중에 클래스,인터페이스,필드 및 메소드에 접근할 수 있다. 또한 새로운 객체의 인스턴스화 및 메소드 호출을 허용한다.
- Spring에서 BeanFactory라는 Container에서 객체가 호출되면 객체의 인스턴스를 생성하게 되는데 이 때 필요하게 된다. 즉 프레임워크에서 유연성있는 동작을 위해 쓰인다.
- Class에 적용된 Annotation정보를 읽으려면 java.lang.Class를 이용하고 필드,생성자,메소드에 적용된 어노테이션 정보를 읽으려면 Class의 메소드를 통해 java.lang.reflect패키지의 배열을 얻어야한다.
- Class.ForName(),getName()등등 여러 메소드로 정보를 얻을 수 있다.

## **Annotation종류**

### **@ComponentScan**

- @Component와 @Service,@Repository,@Controller,@Configuration이 붙은 클래스 Bean을 찾아 Context에 bean등록을 해주는 Annotation이다.

### **@Component**

- 개발자가 직접 작성한 Class를 Bean으로 등록하기 위한 Annotation이다.

### **@Bean**

- 개발자가 직접 제어가 불가능한 외부 라이브러리등을 Bean으로 만들려할 때 사용되는 Annotation이다.
- ArrayList같은 라이브러리등을 Bean으로 등록하기 위해서는 별도로 해당 라이브러리 객체를 반환하는 Method를 만들고 @Bean Annotation을 사용하면 된다.

### **@Autowired**

- 속성(field),setter method,constructor에서 사용하며 Type에 따라 알아서 Bean을 주입해준다.
- 무조건적인 객체에 대한 의존성을 주입시킨다.
- 스프링이 자동적으로 값을 할당한다.
- Bean을 주입받는 방식
- @Autowired
- setter
- 생성자 (@AllArgsConstructor사용)

### **@Controller**

- Spring의 Controller를 의미한다. SpringMVC에서 Controller클래스에 쓰인다.

### **@RestController**

- Spring에서 Controller중 View로 응답하지 않는 Controller를 의미한다.
- method의 반환결과를 JSON형태로 반환한다.
- @ResponseBody역할을 자동적으로 해주는 Annotation이다.
- @Controller + @ResponseBody

### **@Controller vs @RestController**

- @Controller
    - API와 view를 동시에 사용하는 경우에 사용한다.
    - 대신 API서비스로 사용하는 경우에는 @ResponseBody를 사용하여 객체를 반환한다.
    - view화면 return이 주목적 이다.
- @Restcontroller
    - view가 필요없는 API만 지원하는 서비스에서 사용한다.
    - @RequestMapping메소드가 기본적으로 @ResponseBody의미를 가정한다.
    - data(json,xml등) return이 주목적이다.

### **@Service**

- Service Class에 쓰인다.
- 비즈니스 로직을 수행하는 Class라는 것을 나타내는 용도이다.

### **@Repository**

- DataBase에 접근하는 메소드를 가지고 있는 Class에서 쓰인다.

### **@EnableAutoConfiguration**

- Spring Application Context를 만들 때 자동으로 설정하는 기능을 켠다.
- classpath의 내용에 기반해서 자동으로 생성해준다.

### **@Configuration**

- @Configuration을 클래스에 적용하고 @Bean을 해당 Class의 메소드에 적용하면 @Autowired로 Bean을 부를 수 있다.
- **@Required**
- setter method에 적용해주면 Bean생성시 필수 프로퍼티 임을 알린다.
- optional하지 않은 꼭 필요한 속성들을 정의한다.

### **@Value**

- properties에서 값을 가져와 적용할 때 사용한다.
- @Value("${abc}")

### **@SpringBootApplication**

- @Configuration,@EnableAutoConfiguration,@ComponentScan 3가지를 하나의 어노테이션으로 합친 것이다.

### **@RequestMapping**

- 요청 URL을 어떤 메소드가 처리할지 mapping해주는 것이다.
- Controller나 Controller의 method에 적용한다
- 요청을 받는 형식인 GET,POST,PATCH,PUT,DELETE를 정의한다.

### **@CrossOrigin**

- CORS 보안상의 문제로 브라우저에서 리소스를 현재 origin에서 다른곳의 AJAX요청을 방지하는것이다.

### **@Valid**

- 유효성 검증이 필요한 객체임을 지정한다.

### **@RequestBody**

- 요청이 온 데이터를 바로 Class나 model로 매핑하기 위한 것이다.
- POST 나 PUT,PATCH로 요청을 받을때 요청에서 넘어온 body값을 얻어와 매핑한다.

### **@RequestParam**

- @PathVariable과 비슷하다
- request의 parameter에서 가져오는 것이다. method의 파라미터에 사용된다.

### **@PathVariable**

- URL에서 {특정값}을 변수로 받아올 수 있다.
- uri에서 각 구분자에 들어오는 값을 처리해야 할 때 사용한다.

### **@ResponseBody**

- HttpMessageConverter를 이용하여 JSON혹은 xml로 요청에 응답할수 있게 해주는 것이다.
- veiw가 아닌 JSON형식의 값을 응답할 때 사용하는 것이므로 문자열을 리턴하면 그 값을 http response header가 아닌 reponse body에 들어간다.
- 이미 RestController Annotation이 붙어있다면 생략 가능하다.

### **@Transactional**

- 데이터베이스 트랜잭션을 설정하고 싶은 메소드에 어노테이션을 적용하면 메소드 내부에서 일어나느 데이터 베이스 로직이 전부 성공하게 되거나 데이터베이스 접근중 하나라도 실패하면 다시 롤백할 수 있게 해주는 것이다.
- 이미 넣은것을 롤백시키는건 아니며 모든 처리가 정상적으로 됐을때만 DB에 커밋하며 그렇지 않은 경우엔 커밋하지 않는다.
- 비즈니스 로직과 트랜잭션 관리는 대부분 Service에서 관리한다.
- 일반적으로 DB데이터를 등록/수정/삭제 하는 Service메소드는 이걸 필수적으로 가져간다.

## **Lombok**

### **@NoArugsConstructor**

- 기본생성자를 자동으로 추가한다.
- Entity Class를 프로젝트 코드상에서 기본생성자로 생성하는 것은 금지하고 JPA에서 Entity클래서를 생성하는것은 허용하기 위해 추가한다.

### **@AllArgsConstructor**

- 모든 필드 값을 파라미터로 받는 생성자를 추가한다.

### **@RequiredArgsConstructor**

- final이나 @NonNull인 필드 값만 파라미터로 받는 생성자를 추가한다.
- final : 값이 할당되면 더 이상 변경할 수 없다.

### **@Getter**

- Class내 모든 필드의 Getter method를 자동 생성한다.

### **@Setter**

- Class내 모든 필드의 Setter method를 자동 생성한다.
- Controller에서 @RequestBody로 외부에서 데이터를 받는 경우엔 기본생성자+set 메소드를 통해서만 값이 할당 된다.
- 이때만 setter를 허용한다.
- Entity클래스 에서는 Setter를 설정하면 안된다.

### **@ToString**

- Class내 모든 필드의 toString메소드를 자동 생성한다.

### **@EqualsAndHashCode**

- equals와 hashCode method를 오버라이딩 해주는 Annotation이다.
- @EqualsAndHashCode(callSuper = true)
- callSuper속성을 통해 equals와 hashCode메소드 자동 생성 시 상위 클래스의 필드까지 감안할지 안할지에 대해서 설정할 수 있다.
- 즉 callSuper=true로 설정하면 상위 클래스 필드 값들도 동일한지 체크하며 callSuper=false로 설정하면 하위 클래스의 필드값들만 고려한다.

### **@Builder**

- 어느 필드에 어떤값을 채워야 할지 명확하게 정하여 생성 시점에 값을 채워준다.
- Constructor와 Builder의 차이
- 생성시점에 값을 채워주는 역할은 똑같다
- Builder를 사용하면 어느필드에 어떤값을 채워야 할지 명확하게 인지할 수 있다.
- 해당 Class의 Builder패턴 Class를 생성후 생성자 상단에 선언 시 생성자에 포함된 필드만 빌더에 포함된다.

### **JPA Annotation**

- JPA를 사용하면 DB데이터에 작업할 경우 실제 쿼리를 사용하지 않고 Entity클래스의 수정을 통해 작업한다.

### **@Entity**

- 실제 DB의 테이블과 매칭될 Class임을 명시한다.
- 테이블과 링크될 클래스임을 나타낸다.
- Entity Class
- 가장 Core한 클래스로 클래스 이름을 언더스코어 네이빙(_)으로 테이블 이름을 매칭한다.
- SalesManage.java -> sales_manager table
- Controller에서 쓸 DTD는?
- Request와 Response용 DTO는 view를 위한 클래스로 자주 변경이 필요한 클래스이다
- Entity클래스와 DTO클래스를 분리하는 이유는 View Layer 와 DB Layer를 철저하게 역할 분리하기 위해서다
- 테이블과 매핑되는 Entity클래스가 변경되면 여러 클래스에 영향을 끼치게 되는 반면 View와 통신하는 DTO클래스 는 자주 변경되므로 분리해야한다.

### **@Table**

- Entity Class에 매핑할 테이블 정보를 알려준다.
- @Table(name = "USER")
- Annotation을 생략하면 Class이름을 테이블 이름 정보로 매핑한다.

### **@Id**

- 해당 테이블의 PK필드를 나타낸다.

### **@GeneratedValue**

- PK의 생성규칙을 나타낸다.
- 기본값은 AUTO로 MySQL의 auto_increment와 같이 자동증가하는 정수형 값이 된다.

### **@Column**

- 테이블의 컬럼을 나타내며 굳이 선언하지 않더라도 해당 Class의 필드는 모두 컬럼이된다.
- @Column(name = "username")
- 사용하는 이유는 기본값 이외에 추가로 변경이 필요한 옵션이 있을 경우 사용한다.
- 문자열의 경우 VARCHAR(255)가 기본값인데 사이즈를 500으로 늘리고 싶거나 타입을 Text로 변경하고 싶거나 등의 사용한다.