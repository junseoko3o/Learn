let a = 10;
let b = 22;
let c = 30;
// 하나 
// export default a;


// 여러개 할거면
export {a};
export {b};
export default c;
// 아니면 export를 변수/함수 옆에 써줘도 된다.
// 그리고 변수 이름이 import/export 다 똑같아야함.


