//사용된 변수는 window에 등록되고, 값은 가변적으로 사용이 가능하다. 
var hello = 1234;
hello = "hello";

console.log(typeof hello);
hello= 1234;
console.log(typeof hello);
hello= 1234;
console.log(typeof hello);
hello = new Date(); //생성자 처럼 사용
console.log(typeof hello);
hello = Date(); //메소드처럼 사용하면 결과(return type)을 전달해준다.
console.log(typeof hello);

hello = {name:"man", age:10}; //클래스가 없기 때문에 name, age의 멤버 데이터로 객체를 정의 
console.log(typeof hello);

hello = function(){
    console.log("hello를 값을 지정하는 식별자에서 동작을 정의하는 식별자로 변경");
    //return 필수가 아님 
}
console.log(typeof hello);

//식별자도 type을 변경할 수 있으니 확인하면서 코딩해야한다.!!
alert = function(){ //원래 정의 되어있던 식별자(예: alert)도 overriding할 수 있음
    console.log("구현부 바꾸는거 - overriding");		
}
alert("message");