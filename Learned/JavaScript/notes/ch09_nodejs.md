## 전역 변수

전역 변수 : 모든 곳에서 사용할 수 있는 변수

문자열 자료형의 전역 변수
* `__filename` : 현재 실행 중인 코드의 파일 경로
* `__dirname` : 현재 실행 중인 코드의 폴더 경로

<hr>

## process 객체의 속성과 이벤트

`process` 객체 : 현재 실행 중인 노드 프로세스에 대한 정보를 담고 있는 객체

`노드` : 이벤트 기반의 비동기 I/O를 가진 자바스크립트 런타임

### process 객체의 속성
|속성|설명|
|:---:|:---:|
|`process.env`|컴퓨터 환경 정보를 나타냄|
|`process.version`|Node.js 버전|
|`process.versions`|Node.js와 종속된 프로그램 버전|
|`process.arch`|프로세서의 아키텍처를 나타냄|
|`process.platform`|플랫폼을 나타냄|
|`process.connected`|부모 프로세스와 연결되어 있는지 나타냄|
|`process.execPath`|Node.js 실행 경로|
|`process.execArgv`|Node.js 실행 시의 매개변수|
|`process.argv`|프로세스 실행 시 전달된 매개변수|
|`process.mainModule`|메인 모듈의 정보를 담고 있는 객체|
|`process.release`|Node.js의 컴파일 정보|
|`process.exitCode`|프로세스 종료 코드|

### process 객체의 메소드
|메소드|설명|
|:---:|:---:|
|`process.exit([exitCode = 0])`|프로세스를 종료|
|`process.memoryUsage()`|메모리 사용 정보 객체를 리턴|
|`process.nextTick(callback)`|이벤트 루프가 다른 콜백 함수들보다 nextTick의 콜백 함수를 우선으로 처리|
|`process.uptime()`|현재 프로세스가 실행된 시간을 리턴|

<hr>

## process 객체와 이벤트
### Node.js 이벤트 연결 메소드
|메소드|설명|
|:---:|:---:|
|`on(event, eventHandler)`|이벤트 연결|

### process 객체의 이벤트
|이벤트|설명|
|:---:|:---:|
|`exit`|프로세스가 종료될 때 발생|
|`uncaughtException`|예외가 일어나면 발생|
|`unhandledRejection`|예외가 일어나면 발생|

example
```js
// exit 이벤트 연결
process.on('exit', (code) => {
    console.log(`About to exit with code: ${code}`);
});

// uncaughtException 이벤트 연결
process.on('uncaughtException', (error) => {
    console.error(`예기치 못한 에러(uncaughtException): ${error}`);
});

// error raise manually
error.error.error();

//output
// About to exit with code: 1
// 예기치 못한 에러(uncaughtException): TypeError: Cannot read property 'error' of undefined
```
<hr>

## os module
```js
const os = require('os');
```

### os 모듈의 메소드
|메소드|설명|
|:---:|:---:| 
|`os.hostname()`|컴퓨터의 이름을 리턴|
|`os.type()`|운영체제의 이름을 리턴|
|`os.platform()`|운영체제의 플랫폼을 리턴|
|`os.arch()`|운영체제의 아키텍처를 리턴|
|`os.release()`|운영체제의 버전을 리턴|
|`os.uptime()`|운영체제가 실행된 시간을 리턴|
|`os.loadavg()`|로드 에버리지 정보를 담은 배열 리턴|
|`os.totalmem()`|시스템의 총 메모리를 리턴|
|`os.freemem()`|시스템의 사용 가능한 메모리를 리턴|
|`os.cpus()`|CPU의 정보를 담은 객체를 리턴|
|`os.getNetworkInterfaces()`|네트워크 인터페이스의 정보를 담은 배열 리턴|

<hr>

## url module
```js
const url = require('url');
```

### url 모듈의 메소드
|메소드|설명|
|:---:|:---:|
|`url.parse(urlStr[, parseQueryString = false[, slashesDenoteHost = false]])`|URL 문자열을 URL 객체로 변환|
|`url.format(urlObj)`|URL 객체를 URL 문자열로 변환|
|`url.resolve(from, to)`|매개변수를 조합하여 완전한 URL 문자열을 생성|

```js
const url = require('url');

const URL = url.parse('https://github.com/sabin5105?tab=repositories', parseQueryString = true, slashesDenoteHost = true);

console.log(URL);

//output
// Url {
//   protocol: 'https:',
//   slashes: true,
//   auth: null,
//   host: 'github.com',
//   port: null,
//   hostname: 'github.com',
//   hash: null,
//   search: '?tab=repositories',
//   query: [Object: null prototype] { tab: 'repositories' },
//   pathname: '/sabin5105',
//   path: '/sabin5105?tab=repositories',
//   href: '
// }
```

<hr>

## File System module

```js
 const fs = require('fs');

    fs.readFile('readme.txt', (err, data) => {
        if (err) {
            throw err;
        }
        console.log(data);
        console.log(data.toString());
    });
```

### fs 모듈의 메소드
|메소드|설명|
|:---:|:---:| 
|`fs.readFile(path[, options], callback)`|파일을 비동기적으로 읽음|
|`fs.readFileSync(path[, options])`|파일을 동기적으로 읽음|
|`fs.writeFile(file, data[, options], callback)`|파일에 데이터를 씀|
|`fs.writeFileSync(file, data[, options])`|파일에 데이터를 동기적으로 씀|
|`fs.appendFile(file, data[, options], callback)`|파일의 끝에 데이터를 추가|
|`fs.appendFileSync(file, data[, options])`|파일의 끝에 데이터를 동기적으로 추가|
|`fs.watchFile(filename[, options], listener)`|filename 파일을 감시|
|`fs.unwatchFile(filename[, listener])`|filename 파일의 감시를 중지|

### 비동기 메소드 동작
```js
const fs = require('fs');

// 비동기적으로 파일을 읽음
fs.readFile('readme.txt', (err, data) => {
    if (err) {
        throw err;
    }
    console.log(data);
    console.log(data.toString());
});

// 파일을 읽는 동안 다른 작업을 수행

```

<hr>

## node package manager
```bash
$ npm install <package name>
$ npm install express@4
...
```

<hr>

## request module
```bash
$ npm install request
```

```js
const request = require('request');

request('https://www.google.com', (error, response, body) => {
    console.log('error:', error); // Print the error if one occurred
    console.log('statusCode:', response && response.statusCode); // Print the response status code if a response was received
    console.log('body:', body); // Print the HTML for the Google homepage.
});
```

<hr>

## cheerio module
```bash
$ npm install cheerio
```

```js
const request = require('request');
const cheerio = require('cheerio');

const url = 'https://www.hanbit.co.kr/store/books/new_book_list.html';
request(url, (error, response, body) => {
    if (error) throw error;
    const $ = cheerio.load(body);
    const $books = $('.view_box');
    $books.each((index, book) => {
        const $book = $(book);
        const title = $book.find('.book_tit').text();
        const price = $book.find('.price').text();
        console.log(`${title} ${price}`);
    });
});

//output
// [엉뚱소심 유령 탐정단]  1. 도서관 유령 소동 11,700원
// [엉뚱소심 유령 탐정단]  2. 다락방 유령 사건 11,700원
// 전문가를 위한 C 49,500원
// 손목시계의 교양 22,500원
// ...
```

<hr>

## async module

```bash
$ npm install async
```

```js
const fs = require('fs');
const async = require('async');

async.parellel({
    fileA: (callback) => {
        fs.readFile('fileA.txt', 'utf8', callback);
    },
    fileB: (callback) => {
        fs.readFile('fileB.txt', 'utf8', callback);
    }
    fileC: (callback) => {
        fs.readFile('fileC.txt', 'utf8', callback);
    }
}, (error, results) => {
    if (error) throw error;
    console.log(results.fileA);
    console.log(results.fileB);
    console.log(results.fileC);
)
```