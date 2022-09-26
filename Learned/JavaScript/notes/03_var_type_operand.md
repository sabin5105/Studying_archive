# variable & data type & operand

## 변수 선언 규칙
* var, let 사용 / 상수 선언 시 const
* camelCase 사용

**나이 계산 프로그램**
```javascript
function calc(){
    var currentYear = 2022;
    var birthYear = prompt("태어난 연도 입력","YYYY");
    var age;
    age = currentYear - birthYear;
    document.querySelector("#result").innerHTML = "당신의 나이는 " + age + "세 입니다.";
}
```