// access with dot notation or bracket notation

function User(name) {
  // this = {};  (빈 객체가 암시적으로 만들어짐)

  // 새로운 프로퍼티를 this에 추가함
  this.name = name;
  this.isAdmin = false;

  // return this;  (this가 암시적으로 반환됨)
}

let user = new User("보라");

console.log(user.name); // 보라
console.log(user.isAdmin); // false