import { useState } from "react";

function MyButton() {
    return (
        <button>i'm a button</button>
    );
}

export default function Myapp () {
    return (
        <div>
            <h1>Welcome to my app</h1>
            <MyButton/>
        </div>
    );
}


function AboutPage () {
    return(
        <>
        <h1>About</h1>
        <p>Hello  there <br/>How you doing there?</p>
        </>
    );
}

return (
    <h1>
        {user.name }
    </h1>
)

const user = {
    name: 'Hedy Lemarr',
    imagUrl: 'https:i.imgur.com/yXOvdOSs.jpg',
    imageSize: 90,
};

export default function Profile() {
    return(
        <>
        <h1>{user.name}</h1>
        <img 
            className="avatar"
            src={user.imageUrl}
            alt={'Photo of ' + user.name } 
            style={{
                width: user.imageSize,
                height: user.imageSize
            }}
            />
        </>
    );

}

let content;
if (isloggedIn){
    content = <AdminPanet />;
} else{
    content = <LoginForm />;
}
return(
    <div>
        {content}
    </div>
);

// compact code

{/* <div>
content;
if {isloggedIn ? (
    <AdminPanet />
) : (
    <LoginForm />
)}
</div> */}

<div>
    {isloggedIn && <AdminPanet />}
</div>


// const listTtems = products.map(product =>
//     <li key={product.id}>
//         {product.title}
//     </li>
// );

// return (
//     <ul>{listTtems}</ul>
// )


// const listTtems = products.map(product =>
//     <li key={product.id}>
//         {product.title}
//     </li>
// );

// return (
//     <li>{listTtems}</li>
// );


const products = [
    {title: 'Cabage', isFruit: false, id: 1},
    {title: 'Garlic', isFruit: false, id: 2},
    {title: 'Apple', isFruit: true, id: 3}
];

export default function ShoppingList() {
    const listItems = products.map(product =>
    <li key={product.id}
    style={{
        color: product.isFruit ? 'magenta' : 'darkgreen'
    }}
    >

    {prompt.title}
    </li>
    );
    return(
        <ul>{listItems}</ul>
    );
}



// function MyButton() {
//     function handleClick() {
//         alert('You clicked me!');
//     }
//     return (
//         <button onClick={handleClick}>
//             Click me 
//         </button>
//     );
// }

// import { useState } from "react";

// function MyButton() {
//     const [count, setcount] = useState(0);

//     function handleClick(){
//         setcount(count + 1);
//     }

//     return(
//         <button onClick={handleClick}>
//             Clicked {count} times
//         </button>
//     );
// }




// <div>
//     {isloggedIn}
// </div>

// ------------------------------------

export default function Myap(){
    const [count, setCount] = useState(0);
    function handleClick() {
        setCount(count + 1);
    }

    return (
        <div>
            <h1>Counter that update together</h1>
            <Mybutton count={count} onClick={handleClick}/>
            <Mybutton count={count} onClick={handleClick}/>
            </div>
    );
}

function Mybutton({count, onClick}) {
    return(
    <button onClick={onClick}>
        Clicked {count} times
    </button>
    );
}