// 변수는 다음과 같은 선언 흐름을 갖는다
// 선언 -> 초기화 -> 할당
// 변수 선언은 런타임 이전에 먼저 실행된다

let n = 1
{
    let a
    console.log(a)
    a = 2
    console.log(a)
}