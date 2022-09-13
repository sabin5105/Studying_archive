//-------------------- callback function --------------------//
function ask(question, yes, no) {
    if (confirm(question)) yes()
    else no();
  }
  
  function showOk() {
    alert( "동의하셨습니다." );
  }
  
  function showCancel() {
    alert( "취소 버튼을 누르셨습니다." );
  }
  
  // 사용법: 함수 showOk와 showCancel가 ask 함수의 인수로 전달됨
  ask("동의하십니까?", showOk, showCancel);


//-------------------- arrow function ----------------------//

let sum = (a, b) => a + b;

/* 위 화살표 함수는 아래 함수의 축약 버전입니다.

let sum = function(a, b) {
  return a + b;
};
*/

alert( sum(1, 2) ); // 3