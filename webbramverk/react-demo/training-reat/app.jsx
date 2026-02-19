// import { useState } from "react";

// export default function Myapp() {
//     return(
//         <div>
//             <h1>Conuters that update separatly</h1>
//             <Mybutton/>
//             <Mybutton/>
//         </div>
//     );
// }

// function Mybutton(){
//     const [count, setcount] = useState(0);

//     function handleClick(){
//         setcount(count + 1);
//     }
//     return(
//         <button onClick={handleClick}>
//             Click {count} times    
//          </button>
//     );
// }

// ------------------------------------

// import {useState} from "react";

// export default function Myapp() {
//     return (
//         <div> 
//             <h1>Counter that update separatly</h1>
//             <MyButton/>
//             <MyButton/>
//     </div>
// );
// }

// function MyButton() {
//     const [count, setCount] = useState(0);

//     function handleClick(){
//         setCount(count + 1);
//     }
//     return (
//         <button onClick={handleClick}>
//             Clicked {count} times
//         </button>
//     );
// }

// -----------------------------------
// import {useState} from "react";

// export default function Myapp() {
//     const [count, setCount] = useState(0);
//     function handleClick(){
//         setCount(count +1);
//     }
//     return(
//         <div>
//             <h1>Counter that update together</h1>
//             <MyButton/>

//             <MyButton/>
//         </div>
//     );
// }

// function MyButton() {
//     return(
//         <button onClick={handleClick}>
//             Clicked {count} times
//         </button>
//     );
// }

// --------------------------

import {useState} from "react";

export default function Myap() {
    const [count, setCount] = useState(0);

    function handleClick() {
        setCount(count + 1);
    }
    return(
        <div>
            <h1>Counter that update together</h1>
            <Mybutton count={count} onClick={handleClick}/>
            <Mybutton count={count} onClick={handleClick}/>
            </div>
    );
}

function Mybutton({count, onClick}) {
    return (
        <button onClick={={onclick}}>
            Clicked {count} times
        </button>
    );
}