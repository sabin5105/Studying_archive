alert( Number("   123   ") ); // 123
alert( Number("123z") );      // NaN ("z"를 숫자로 변환하는 데 실패함)

alert( Number(true) );        // 1
alert( Number(false) );       // 0

alert( Boolean(1) ); // 숫자 1(true)
alert( Boolean(0) ); // 숫자 0(false)

alert( Boolean("hello") ); // 문자열(true)
alert( Boolean("") ); // 빈 문자열(false)

alert( Boolean("0") ); // true
alert( Boolean(" ") ); // 공백이 있는 문자열도 비어있지 않은 문자열이기 때문에 true로 변환됩니다.


// quiz
// 형 변환이란 무엇인가?
// 형 변환의 대표적인 예시 두 가지를 설명하라.
// 문자, 숫자, 불린형의 변환에 대하여 설명하라.