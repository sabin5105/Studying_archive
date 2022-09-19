/*
    prompt는 사용자에게 입력을 받는 창을 띄워줍니다.
    prompt(title, default);
*/
let age = prompt('나이를 입력해주세요.', 100);

alert(`당신의 나이는 ${age}살 입니다.`); // 당신의 나이는 100살입니다.


/*
    confirm은 확인/취소 버튼을 가진 창을 띄워줍니다.
    확인을 누르면 true, 취소를 누르면 false를 반환합니다.
*/

let isBoss = confirm("당신이 주인인가요?");

alert( isBoss ); // 확인 버튼을 눌렀다면 true가 출력됩니다.


// quiz
// 브라우저가 제공하는 사용자와 상호작용할 수 있는 세 가지 함수는 무엇인가?