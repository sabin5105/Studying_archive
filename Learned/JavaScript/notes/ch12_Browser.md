## 브라우저 객체 모델

### 브라우저 객체
브라우저 객체
|객체|설명|
|:---:|:---:| 
|window|브라우저 창을 나타내는 객체|
|screen|브라우저 창의 크기 정보를 나타내는 객체|
|location|현재 페이지의 주소 정보를 나타내는 객체|
|history|현재 페이지를 방문한 이력 정보를 나타내는 객체|
|navigator|브라우저의 정보를 나타내는 객체|
|document|현재 페이지의 문서 객체를 나타내는 객체|

## window 객체
**브라우저 창을 나타내는 객체**
* 새로운 화면을 열거나 웹 브라우저의 크기를 변경하는 등의 일
* 대표적으로 경고 출력을 하는 경고창과 입력을 하는 프롬프트를 제공

### 함수
|함수|설명|
|:---:|:---:|
|alert(message)|경고창을 출력|
|confirm(message)|확인창을 출력|
|prompt(message, temp_char)|입력창을 출력| 

```js
const input = prompt('input', 'default');

alert(input);
```

## screen 객체
**브라우저 창의 크기 정보를 나타내는 객체**

### 속성
|속성|설명|
|:---:|:---:|
|screen.width|브라우저 창의 너비|
|screen.height|브라우저 창의 높이|
|screen.availWidth|브라우저 창의 너비(메뉴, 툴바 등을 제외)|
|screen.availHeight|브라우저 창의 높이(메뉴, 툴바 등을 제외)|
|screen.colorDepth|색상의 비트 수|
|screen.pixelDepth|화면의 픽셀 수|

## location 객체
**현재 페이지의 주소 정보를 나타내는 객체**

### 속성
|속성|설명|
|:---:|:---:|
|location.href|현재 페이지의 주소|
|location.protocol|현재 페이지의 프로토콜|
|location.host|현재 페이지의 호스트|
|location.port|현재 페이지의 포트|
|location.pathname|현재 페이지의 경로|
|location.search|현재 페이지의 쿼리|
|location.hash|현재 페이지의 해시|

### 메소드
|메소드|설명|
|:---:|:---:|
|location.assign(url)|url로 이동|
|location.reload()|현재 페이지를 새로고침|
|location.replace(url)|url로 이동(이전 페이지 기록 X)|

```js
// 1초에 한 번씩 새로고침
setInterval(function(){
    location.reload();
}, 1000);
```
## history 객체

**현재 페이지를 방문한 이력 정보를 나타내는 객체**
### 메소드
|메소드|설명|
|:---:|:---:|
|history.back()|이전 페이지로 이동|
|history.forward()|다음 페이지로 이동|

## navigator 객체
**브라우저의 정보를 나타내는 객체**
* 웹 페이지를 실행하는 웹 브라우저 정보가 들어있음
* 사용자의 웹 브라우저, 운영체제를 구분할 수 있음

### 속성
|속성|설명|
|:---:|:---:|
|navigator.appName|브라우저 이름|
|navigator.appVersion|브라우저 버전|
|navigator.userAgent|브라우저 정보|
|navigator.platform|운영체제|
|navigator.language|언어|

```js
let output = '';
output += 'appName: ' + navigator.appName + '\n';
output += 'appVersion: ' + navigator.appVersion + '\n';
output += 'userAgent: ' + navigator.userAgent + '\n';
output += 'platform: ' + navigator.platform + '\n';
output += 'language: ' + navigator.language + '\n';
alert(output);

if (navigator.userAgent.toLowerCase().indexOf('iphone') >= 0 
    || navigator.userAgent.toLowerCase().indexOf('ipad') >= 0 
    || navigator.userAgent.toLowerCase().indexOf('ipod') >= 0 
    || navigator.userAgent.toLowerCase().indexOf('android') >= 0) {alert('mobile')};
else
    {alert('desktop')};
```

## document 객체
**현재 페이지의 문서 객체를 나타내는 객체**

### 속성
|속성|설명|
|:---:|:---:|
|document.title|현재 페이지의 제목|
|document.URL|현재 페이지의 주소|
|document.domain|현재 페이지의 도메인|
|document.referrer|이전 페이지의 주소|
|document.lastModified|현재 페이지의 마지막 수정 시간|

### 메소드
|메소드|설명|
|:---:|:---:|
|document.write()|문서에 문자열을 출력|
|document.open()|문서를 열어서 쓰기|
|document.close()|문서를 닫음|
|document.getElementById()|id 속성으로 요소를 찾음|
|document.getElementsByName()|name 속성으로 요소를 찾음|
|document.getElementsByTagName()|태그 이름으로 요소를 찾음|
|document.getElementsByClassName()|클래스 이름으로 요소를 찾음|
|document.querySelector()|CSS 선택자로 요소를 찾음|
|document.querySelectorAll()|CSS 선택자로 요소를 찾음|

```js
// css 선택자로 요소를 찾음
// h1 tag 중 첫 번째 요소를 찾아, 그 요소의 내용을 바꿈
document.querySelector('h1').style.color = 'red';
```