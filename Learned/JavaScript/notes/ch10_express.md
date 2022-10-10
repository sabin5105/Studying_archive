## 요청 및 응답

요청
  * 대상 : 클라이언트 (브라우저)
  * 메세지 : 요청 메세지, 클라이언트가 서버에게
  * 형태 : HTTP 요청 메세지
    * ```GET / HTTP/1.1```
    * URL, Method, Header, Body, Host, User-Agent, Accept, Cookie 등을 포함

응답
  * 대상 : 서버
  * 메세지 : 응답 메세지, 서버가 클라이언트에게
  * 형태 : HTTP 응답 메세지
    * ```HTTP/1.1 200 OK```
    * Status Code, Header, Body, Content-Type, Content-Length, Set-Cookie 등을 포함

<hr>

## 서버 생성 및 실행

기본 메소드
|메소드|설명|
|:---:|:---:| 
|express()|익스프레스 서버 생성|
|createServer()|서버 생성|
|listen()|서버 실행|
|close()|서버 종료|
|...|...|

```js
const express = require('express');
const app = express();

app.use((req, res, next) => {
    res.send('Hello Express');
    next();
});

app.listen(8080, () => {
  console.log('http://127.0.0.1:8080'); // or http://localhost:8080
});
```

<hr>

## 페이지 라우팅

페이지 라우팅 : 클라이언트 요청에 적절한 페이지를 제공하는 기술

페이지 라우팅 메소드
|메소드|설명|
|:---:|:---:|
|get(path, callback)|GET 요청에 대한 페이지 라우팅 / 이벤트 리스너 지정|
|post(path, callback)|POST 요청에 대한 페이지 라우팅 / 이벤트 리스너 지정|
|put(path, callback)|PUT 요청에 대한 페이지 라우팅 / 이벤트 리스너 지정|
|delete(path, callback)|DELETE 요청에 대한 페이지 라우팅 / 이벤트 리스너 지정|
|all(path, callback)|모든 요청에 대한 페이지 라우팅 / 이벤트 리스너 지정|

페이지 라우팅 시 토큰 활용

* `:<토큰 이름>` 형태로 설정 가능
* 토큰은 다른 문자열 변환 입력가능, request 객체의 params 속성으로 전달

```js
 const express = require('express');

 const app = express();

// 토큰 / 이벤트 리스너 지정
 app.get('/page/:id', (reqrest, response) => {
   const id = request.params.id; // 토큰 값

    response.send(`<h1>${id} Page</h1>`); // 응답
 });

// 서버 실행
    app.listen(8080, () => {
    console.log('http://localhost:8080');

// http://localhost:8080/page/10] 접속 시 10 Page 출력
```
<hr>

## 요청과 응답

response 객체 기본 메소드
|메소드|설명|
|:---:|:---:|
|send()|응답 본문 전송|
|status()|응답 상태 코드 전송|
|set()|응답 헤더 설정|

send()
  * 응답 본문 제공
  * 가장 마지막에 실행
  * 두번 실행 불가

```js
const express = require('express');

const app = express();

app.get('*', (request, response) => {
    response.status(404).send('NOT FOUND');
    response.set('Content-Type', 'text/html');
    response.send('Hello Express');
}

app.listen(8080, () => {
    console.log('http://localhost:8080');
});

// http://localhost:8080 접속 시 NOT FOUND 출력, header에 Content-Type: text/html 설정
```

Content-Type
  * 응답 본문의 형식을 지정
  * MIME 타입으로 지정
  * MIME 타입 형식 : text/html, text/plain, application/json, application/xml, image/png, image/jpeg, image/gif, audio/mpeg, video/mp4, application/octet-stream 등
  * type() 메소드로 MIME 타입 지정 가능
    * ex) response.type('text/html');

```js
// image/png 형식으로 응답

const express = require('express');
const app = express();

app.get('/image', (request, response) => {
    response.type('image/png');
    response.sendFile(__dirname + '/image.png');
});

app.listen(8080, () => {
    console.log('http://localhost:8080');
});
```

HTTPS 상태

|HTTPS 상태|설명|예시|
|:---:|:---:|:---:|
|1xx|처리 중|100 Continue|
|2xx|성공|200 OK|
|3xx|리다이렉트|301 Moved Permanently|
|4xx|클라이언트 오류|400 Bad Request|
|5xx|서버 오류|500 Internal Server Error|

상태 코드 지정 : status() 메소드

```js
// 404 상태 코드 지정

const express = require('express');
const app = express();

app.get('*', (request, response) => {
    response.status(404).send('NOT FOUND');
});

app.listen(8080, () => {
    console.log('http://localhost:8080');
});

// http://localhost:8080 접속 시 NOT FOUND 출력
```

request 객체
    * 요청 정보를 담고 있는 객체
    * 요청 헤더, 요청 본문, 요청 파라미터 등의 정보를 제공
  
예시 : https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=express

|분류|값|설명|
|:---:|:---:|:---:|
|프로토콜|https|통신에 사용되는 규칙|
|호스트|search.naver.com|호스트 이름|
|URL|/search.naver|URL 경로|
|쿼리스트링|sm=top_hty&fbm=1&ie=utf8&query=express|쿼리스트링|

```js
// 요청 정보 확인

const express = require('express');
const app = express();

app.get('*', (request, response) => { // *은 모든 경로를 의미
    console.log(request.headers);
    console.log(request.method);
    console.log(request.url);
    console.log(request.query);
    response.send('Hello Express');
});

app.listen(8080, () => {
    console.log('http://localhost:8080');
});

// http://localhost:8080/?name=express 접속 시 request 객체의 정보 출력

// { host: 'localhost:8080', 
// headers: { ... }, 
// method: 'GET', 
// url: '/?name=express', 
// query: { name: 'express' } }
```

<hr>

## 미들웨어

미들웨어
  * request-response 중간에 위치하여 미들웨어에 정의된 로직을 수행하는 함수
  * 정적 파일 제공 시 (이미지, CSS, JS 파일 등) 미들웨어가 필요

미들웨어 설정 메소드
|메소드|설명|
|:---:|:---:|
|use()|미들웨어 설정|

미들웨어 종류
|종류|설명|
|:---:|:---:|
|애플리케이션 레벨 미들웨어|모든 요청에 대해 동작하는 미들웨어|
|라우터 레벨 미들웨어|특정 경로에 대해 동작하는 미들웨어|
|오류 처리 미들웨어|에러가 발생했을 때 동작하는 미들웨어|

```js
const express = require('express');
const app = express();

app.use(express.static(__dirname + '/public')); // 정적 파일 제공 미들웨어

app.get('/', (request, response) => {
    response.send('Hello Express');
});

app.listen(8080, () => {
    console.log('http://localhost:8080');
});

// http://localhost:8080 접속 시 public 폴더의 index.html 파일 출력
```

body-parser 미들웨어
  * 요청 본문을 해석해주는 미들웨어
  * 클라이언트에서 서버로 데이터 전송 (URL 사용)
  * MIME 형식

요청 본문 MIME 형식
|형식|설명|
|:---:|:---:|
|application/x-www-form-urlencoded|폼 전송 방식 (post, put, delete, get...)|
|multipart/form-data|대용량 데이터 전송 시 사용|
|application/json|JSON 형식|

클라이언트가 서버로 데이터를 전송하는 방법
|방법|설명|예시
|:---:|:---:|:---:|
|params 객체|URL 토큰 / 보기 좋음|/user/:id|
|query 객체|URL의 쿼리스트링 / 토큰보다 많은 데이터를 전달 가능|/user?id=1|
|body 객체|대용량 문자열 / 주소에 데이터 기록 X|{id: 1, name: 'express'}|

```js
const express = require('express');
const bodyParser = require('body-parser');
const app = express();

app.use(express.static(__dirname + '/public'));
app.use(morgan('dev')); // 로그 출력 미들웨어
app.use(bodyParser.urlencoded({ extended: false })); // application/x-www-form-urlencoded

// 서버에서 get 후 send
app.get('/', (request, response) => {
    let output = '';
    output += '<form method="post">';
    output += '  <input type="text" name="a" />';
    output += '  <input type="text" name="b" />';
    output += '  <input type="submit" value="전송" />';
    output += '</form>';
    response.send(output);
});

// 서버에서 get한 데이터를 post로 클라이언트에게 전송
app.post('/', (request, response) => {
    response.send(request.body.a + ' ' + request.body.b);
});

// 서버실행
app.listen(8080, () => {
    console.log('http://localhost:8080');
});

// http://localhost:8080 접속 시 폼 전송, 전송 시 입력한 값 출력
```