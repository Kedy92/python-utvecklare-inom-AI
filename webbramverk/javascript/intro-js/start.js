// function DoSomething(){

// }

// const DoSomething = () => {

// }

// // ----------------------------------

// export default DoSomething;

// export const DoSomething = () => {

// }


// this is important for reat :

// const MyComponent = () => {
//     return <div></div>
// }  
// -------------------------

// in reat this takes way too much space:
// let age = 10;
// let name = "pedro";

// if (age > 10) {
//     name = "pedro"
// }
// else {
//     name = "Jack"
// }

// So now the tornary way(this wy tornary comes to the space. they 
// basicly shorthand notation for doing if statement 
// or if else statement) an e.g below:

// let age = 16;
// let name = age>16 && "Pedro"; // this right here is saying let name
// pedro if the condition (age>16) is true
// another way to di this is:

// let name = age>16 ? "pedro" : "jack";
// why is This actually useful? Well in reat you're finding your
//self retourning html. So if have components like this:

// const Component = () => {
//     return age > 10 ? <div>pedro</div> : <div>jack</div> ;
} // this is very useful in reat.

// Now we're going to go through Objects. this very importante in reat.
// objec is known as dictionary in python . in javascript it calls object

// const person = {
//     name: "Pedro",
//     age: 20,
//     isMaried: false,
// };

// this not a good way to do this:
// const name = person.name
// const age = person.age
// const isMaried = person.isMaried
// -----------you can do this in this for the bettre------------

// const {name, age, isMaried} = person; 

// const person = {
//     name: "Pedro",
//     age: "20",
//     isMaried: false,
// };

// lets say that we want create another person but exactly refered to
// to our now person. so lets see would i copy the object abose but change
// some proprieties on it. you can do it by doing this thing:👇
//(this not only for object, but you can do this for lot of thing in js )

// this means i want keep everything in the above object, but i can more 
// contents in it and change
// const person2 = {...person, name: "Jack"}//now person2 will be extly the
// like person, but the propiety (name) is different. 
// this i extremly useful. you will this in like array too, 
// because it works the same way with array  

// If E.g if an array here :

// const names =["Pedro", "jack", "Jessica"];

// const names2 = [...names, "Joe"];

// next and definitly important stuff to know is be able to work with
// 3 fondomental of javascripts array functions.
// this is: .map(), .filter() 
//and .reduce()(this last is not too must in use so we focus those first two )

// So what exxactly the: .map() and filter() functiones. e.g👇

// let names = ["Pedro", "Jessica", "Carol"];

// this going to generat a header for each element in the liste of 
// array (names)   👍😆. So this how you would render or display your 
// website lists in react
names.map((name) => {
    return<h1> {name} </h1> 
})

// the filter function image the list about has some more Pedro(more element):

let names = ["Pedro", "Jessica", "Carol", "Pedro","Pedro" ];

names.filter((name) => {
    return name !== "Pedro"
})

// the last concept that needs to know. Async + Await + Fetch, 
// They are fondamental for any kind of webbdeloppement application
// . not just for javascript or react. the raison for that is because 
//  it is working with API. and most websites nowerday 
// have to communicate wiht api in some sort of way.
// So the concepte is you have to be able to work with promisses 
// and asycinc await. you will be requesting data. 
// and you need to be able to handle the data you receive in th way that 
//will work correctly. Then you also need to know how to fetch data. 
// and that where the fetch-tapi comes in. In react there is mutiple 
// ways to fetch data from an API. 