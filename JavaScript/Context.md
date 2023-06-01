1. **실행 컨텍스트란?**
    1. 스택 vs 큐
        
        ![(이미지 출처 : [https://velog.io/@leejuhwan/스택STACK과-큐QUEUE](https://velog.io/@leejuhwan/%EC%8A%A4%ED%83%9DSTACK%EA%B3%BC-%ED%81%90QUEUE))](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/13ecd27d-f865-4f0a-b782-2992a3eabdc8/Untitled.png)
        
        (이미지 출처 : [https://velog.io/@leejuhwan/스택STACK과-큐QUEUE](https://velog.io/@leejuhwan/%EC%8A%A4%ED%83%9DSTACK%EA%B3%BC-%ED%81%90QUEUE))
        
    2. 콜 스택(call stack)
        1. 실행 컨텍스트란 **실행할 코드에 제공할 환경 정보**들을 모아놓은 객체 
        2. 모아서 어디에? —> 콜 스택에
        3. 가장 위에 쌓여있는 컨텍스트와 관련된 코드를 실행하는 방법으로 코드의 환경 및 순서를 보장
        4. 컨텍스트의 구성 방법
            1. 전역공간
            2. eval()함수
            3. **함수(우리가 흔히 실행컨텍스트를 구성하는 방법)**
            4. 실행컨텍스트 구성 예시
                
                ```jsx
                // ---- 1번
                var a = 1;
                function outer() {
                	function inner() {
                		console.log(a); //undefined
                		var a = 3;
                	}
                	inner(); // ---- 2번
                	console.log(a);
                }
                outer(); // ---- 3번
                console.log(a);
                ```
                
            5. 코드실행 → 전역(in) → 전역(중단) + outer(in) → outer(중단) + inner(in) → inner(out) + outer(재개) → outer(out) + 전역(재개) → 전역(out) → 코드종료
    3. 실행 컨텍스트 객체
        1. 생성(활성화) 시점 : 한 ‘실행 컨텍스트’가 콜 스택의 맨 위에 쌓이는 순간이 곧 현재 실행할 코드에 관여하게 되는 시점
        2. 생성 시점. 즉, 활성화 시점에 JS 엔진은 해당 컨텍스트에 관련된 코드를 실행하는데 필요한 환경 정보들을 수집해서 실행 컨텍스트 객체에 저장
        3. 실행컨텍스트에 담기는 정보
            1. VariableEnvironment
                1. 현재 컨텍스트 내의 식별자 정보
                2. 외부 환경 정보
                3. 선언 시점 LexicalEnvironment의 **snapshot**
            2. LexicalEnvironment
                1. VariableEnvironment와 동일하나 변경사항이 실시간으로 반영
            3. ThisBinding
                1. this 식별자가 바라봐야할 객체
2. **VariableEnvironment, LexicalEnvironment 개요**
    1. VE와 LE의 비교
        1. 담기는 내용 : 동일
        2. 스냅샷 유지여부
            1. VE : 유지
            2. LE : 유지X
        3. 실행 컨텍스트를 생성할 때, VE에 정보를 먼저 담은 다음, 이를 그대로 복사해서 LE를 만들고 이후에는 주로 LE를 활용
    2. 구성요소
        1. VE, LE모두 동일하며, ‘environmentRecord’와 ‘outerEnvironmentReference’로 구성
        2. environmentRecord(=record)
        3. outerEnvironmentReference(=outer)
3. **LexicalEnvironment(1) - environmentRecord와 호이스팅**
    1. 개요
        1. 현재 컨텍스트와 관련된 코드의 식별자 정보들이 저장(수집)
        2. 수집 대상 정보 : 함수에 지정된 매개변수 식별자, 함수 자체, var로 선언된 변수 식별자 등
        3. 컨텍스트 내부를 처음부터 끝까지 **순서대로** 훑어가며 수집
    2. 호이스팅
        1. 변수정보 수집을 모두 마쳤더라도 아직 실행 컨텍스트가 관여할 코드는 실행 전의 상태임(JS 엔진은 코드 실행 전 이미 모든 변수정보를 알고 있는 것)
        2. 변수 정보 수집 과정을 이해하기 쉽게 설명한 **‘가상 개념’**
    3. 호이스팅 규칙
        1. 매개변수 및 변수에 대한 호이스팅
            
            ```jsx
            //action point 1 : 매개변수 다시 쓰기(JS 엔진은 똑같이 이해한다)
            //action point 2 : 결과 예상하기
            //action point 3 : hoisting 적용해본 후 결과를 다시 예상해보기
            
            function a (x) {
            	console.log(x);
            	var x;
            	console.log(x);
            	var x = 2;
            	console.log(x);
            }
            a(1);
            ```
            
        2. 함수 선언의 호이스팅
            
            ```jsx
            //action point 1 : 결과 값 예상해보기
            //action point 2 : hoisting 적용해본 후 결과를 다시 예상해보기
            
            function a () {
            	console.log(b);
            	var b = 'bbb';
            	console.log(b);
            	function b() { }
            	console.log(b);
            }
            a();
            ```
            
        3. 함수 선언문, 함수 표현식
            1. 함수 정의의 3가지 방식
                
                ```jsx
                function a () { /* ... */ } // 함수 선언문. 함수명 a가 곧 변수명
                a(); // 실행 ok
                
                var b = function () { /* ... */ } // (익명 함수 표현식. 변수명 b가 곧 변수명
                b(); // 실행 ok
                
                var c = function d () { /* ... */ } // 기명 함수 표현식. 변수명은 c, 함수명은 d
                c(); // 실행 ok
                d(); // 에러!
                ```
                
            2. 함수 선언문, 함수 표현식
                
                ```jsx
                console.log(sum(1, 2));
                console.log(multiply(3, 4));
                
                function sum (a, b) { // 함수 선언문 sum
                	return a + b;
                }
                
                var multiply = function (a, b) { // 함수 표현식 multiply
                	return a + b;
                }
                ```
                
                1. 함수 선언문을 주의해야 하는 이유
                    
                    ```jsx
                    ...
                    
                    console.log(sum(3, 4));
                    
                    function sum (x, y) {
                    	return x + y;
                    }
                    
                    ...
                    ...
                    
                    var a = sum(1, 2);
                    
                    ...
                    
                    function sum (x, y) {
                    	return x + ' + ' + y + ' = ' + (x + y);
                    }
                    
                    ...
                    
                    var c = sum(1, 2);
                    
                    console.log(c);
                    ```
                    
                2. 만약 함수 표현식이었다면…?
                    
                    ```jsx
                    ...
                    
                    console.log(sum(3, 4));
                    
                    var sum = function (x, y) {
                    	return x + y;
                    }
                    
                    ...
                    ...
                    
                    var a = sum(1, 2);
                    
                    ...
                    
                    var sum = function (x, y) {
                    	return x + ' + ' + y + ' = ' + (x + y);
                    }
                    
                    ...
                    
                    var c = sum(1, 2);
                    
                    console.log(c);
                    ```
                    
    
4. **LexicalEnvironment(2) - 스코프, 스코프 체인, outerEnvironmentReference(=outer)**
    1. 주요 용어
        1. 스코프
            1. 식별자에 대한 유효범위
            2. 대부분 언어에서 존재하며, JS에서도 존재(es5 / es6는 조금 다름)
        2. 스코프 체인
            1. 식별자의 유효범위를 안에서부터 바깥으로 차례로 검색해나가는 것
        3. outerEnvironmentReference(이하 outer)
            1. 스코프 체인이 가능토록 하는 것(외부 환경의 참조정보)
    2. 스코프 체인
        1. outer는 현재 호출된 함수가 선언될 당시의 LexicalEnvironment를 참조
        2. ex) A함수 내부에 B함수 선언 → B함수 내부에 C함수 선언(Linked List)
        3. 결국 전역 컨텍스트의 LexicalEnvironment를 참조
        4. 오직 자신이 선언된 시점의 LexicalEnvironment를 참조하고 있으므로, 가장 가까운 요소부터 차례대로 접근 가능
        5. 결론 : 무조건 스코프 체인 상에서 가장 먼저 발견된 식별자에게만 접근이 가능
            
            ```jsx
            var a = 1;
            var outer = function() {
            	var inner = function() {
            		console.log(a);
            		var a = 3;
            	};
            	inner();
            	console.log(a);
            };
            outer();
            console.log(a);
            ```
            
    3. 전역변수와 지역변수
        1. 전역변수 : 전역 공간에서 선언한 변수
        2. 지역변수 : 함수 내부에서 선언한 변수