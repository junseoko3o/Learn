- 클라이언트로부터 요청을 받으면 요청에 맞는 정적 파일을 응답해주는 HTTP Web Server로 활용
- Reverse Proxy Server로 활용 → WAS 서버의 부하를 줄일 수 있는 로드밸런서로 활용

### 구조

- 하나의 Master Process와 다수의 Worker Process로 구성되어 실행
- Master Process
    - 설정 파일을 읽고, 유효성 검사, Worker Process 관리
- Worker Process
    - 모든 요청 처리
- 이벤트 기반 모델을 사용하며, Worker Process 사이에 요청을 효율적으로 분배하기 위해서 OS에 의존적인 메커니즘

### 설정

- Nginx 모듈 동작은 coufiguration 파일에 있는 directives에 의해 제어된다.
- simple directive
    - 이름,값이 있고 세미콜론으로 끝난다.
    
    ```bash
    worker_process 1;
    ```
    
- block directive
    - simple directive의 구조에 블록을 감싼 형태
    
    ```bash
    events {
    	worker_process 1024;
    }
    ```
    
    - block directive는 해당 directive 안에 또 다른 block directive가 포함될 수 있다.
    
    ```bash
    http {
      server {
    
        location / {
          root /path/to/html ;
        }
    
        location /images/ {
          root /path/to/image ;
        }
    
      }
    }
    ```
    
    - nclude 지시어는 특정 파일을 포함하는 기능을 수행. 파일의 내용은 지시어가 있는 바로 그 위치에 해당 파일 내용이 삽입.
    
    ```bash
    
    http {
        # mime.types 파일을 읽어들인다. (단일 파일을 include)
        include       /etc/nginx/mime.types;
    
        # /etc/nginx/conf.d 디렉토리 아래 있는 .conf 파일을 모두 읽어 들임 (특정 디렉토리의 모든 파일을 include)
        include /etc/nginx/conf.d/*.conf;
    }
    ```
    

### main 설정

- /etc/nginx/nginx.conf

```bash
# worker 프로세스를 실행할 사용자 설정
# - 이 사용자에 따라 권한이 달라질 수 있다.
user  nginx;
# 실행할 worker 프로세스 설정
# - 서버에 장착되어 있는 코어 수 만큼 할당하는 것이 보통, 더 높게도 설정 가능
worker_processes  1;

# 오류 로그를 남길 파일 경로 지정
error_log  /var/log/nginx/error.log warn;
# NGINX 마스터 프로세스 ID 를 저장할 파일 경로 지정
pid        /var/run/nginx.pid;

# 접속 처리에 관한 설정을 한다.
events {
    # 워커 프로레스 한 개당 동시 접속 수 지정 (512 혹은 1024 를 기준으로 지정)
    worker_connections  1024;
}

# 웹, 프록시 관련 서버 설정
http {
    # mime.types 파일을 읽어들인다.
    include       /etc/nginx/mime.types;
    # MIME 타입 설정
    default_type  application/octet-stream;

    # 엑세스 로그 형식 지정
    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
                      '$status $body_bytes_sent "$http_referer" '
                      '"$http_user_agent" "$http_x_forwarded_for"';

    # 엑세스 로그를 남길 파일 경로 지정
    access_log  /var/log/nginx/access.log  main;

    # sendfile api 를 사용할지 말지 결정
    sendfile        on;
    #tcp_nopush     on;

    # 접속시 커넥션을 몇 초동안 유지할지에 대한 설정
    keepalive_timeout  65;

    # (추가) nginx 버전을 숨길 수 있다. (보통 아래를 사용해서 숨기는게 일반적)
    server_tokens off

    #gzip  on;

    # /etc/nginx/conf.d 디렉토리 아래 있는 .conf 파일을 모두 읽어 들임
    include /etc/nginx/conf.d/*.conf;
}
```

- http 블록
    - http 블록은 HTTP 부분과 관련된 모듈의 지시어와 블록을 정의하며, server와 location의 루트 블록이라고 할 수 있다. http, server, location 블록은 계층 구조를 가지고 있다. 많은 지시어가 각 블록에서 동시에 사용될 수 있는데, http 블록의 내용은 server 블록의 기본값이 되고, server 블록의 내용은 location 블록의 기본값이 된다. 만약 상위 블록에서 선언된 지시어를 하위 블록에서 다시 선언하면 상위의 지시어는 무시된다. http 블록 안에 한 개 이상의 server 블록을 선언할 수 있다.
- **server 블록**
    - server 블록은 하나의 호스트를 선언하는데 사용하며, http 블록 안에서만 사용할 수 있다. server 블록에는 한 개 이상의 location 블록을 선언할 수 있다.
- **location 블록**
    - location 블록에는 server 블록 안에 정의되며, 특정 URL을 처리하는 방법을 정의. 예를 들면 http://example.com/hello/1 과 http://example.com/world/1 접근하는 요청을 다르게 처리하고 싶을 때 사용.
- **events 블록**
    - events 블록은 네트워크의 작동 환경을 설정하는 지시어를 제공한다. 이벤트 블록의 지시어는 이벤트 블록에서만 사용할 수 있고, http, server, local 블록과는 상속 관계를 갖지 않는다. 아래의 지시어들은 반드시 events 블록 안에서만 사용해야 한다.
        - accept_mutex
            - LISTEN 소켓을 오픈하기 위한 accept 뮤텍스의 사용/해제를 설정.
            
            ```bash
            accept_mutex on;
            ```
            
        - accept_mutex_delay
            - 자원 획득을 다시 시도하기 전에 작업자 프로세스가 기다려야 하는 시간을 정의. accept_mutex 지시어가 off 로 설정되어 있으면 이 값은 사용되지 않는다.
            
            ```bash
            accept_mutex_delay 500ms;
            ```
            
        - worker_connections
            - Worker Process 가 동시에 처리할 수 있는 접속자 수를 정의. worker_processes * worker_connections = 최대 접속자 수
            
            ```bash
            worker_connections 1024;
            ```
            

## Reverse Proxy

### 무엇?

- 리버스 프록시란 외부 클라이언트에서 서버로 접근 시, 중간에서 중개자 역할을 하여 내부 서버로 접근할 수 있도록 도와주는 서버

- **보안**
    - 외부 사용자로부터 내부망에 있는 서버의 존재를 숨길 수 있다. 모든 요청은 리버스 프록시 서버에서 받으며, 매핑되는 내부 서버로 요청을 전달한다. 또한 Nginx는 SSL 설정도 가능.
- **로드밸런싱**
    - 리버스 프록시 서버가 내부 서버에 대한 정보를 알고 있으므로, 각 서버의 상태에 따라 부하를 분산시키며 요청을 전달할 수 있다.
    
    ```bash
    http {
        server {
            listen 80;
            location / {
                proxy_pass http://127.0.0.1:8081;
            }
        }
    }
    ```
    
    - 만약에 listen 지시어를 사용하지 않으면 default 값인 80 port로 설정된다.

## docker compose
- docker host mode로 nginx 실행
```bash
version: "3.9"
services:
  proxy:
    container_name: nginx
    image: nginx:stable-alpine
    volumes:
      - "./conf.d:/etc/nginx/conf.d"
      - "./logs:/var/log/nginx/"
      - "./cache:/var/cache/nginx"
      - "./nginx.conf:/etc/nginx/nginx.conf"
    network_mode: host
```