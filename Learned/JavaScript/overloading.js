function user(){
    console.log("user()");
}

//overloading - 매개인자 선언과 상관없이 입력값을 넣을 수 있다.
myUser = function(name, age){
    console.log("myUser()",arguments.length); //자바스크립트의 배열은 가변적으로 사용이 가능하다.(java와 큰 차이점)
    console.log(name,age);
    for (var t in arguments){
        console.log(arguments[t],t, typeof arguments[t]); //t는 인덱스 값(키 값)
    }
}

user();
myUser();
myUser("홍길동",10);
myUser(10,20,30,40);