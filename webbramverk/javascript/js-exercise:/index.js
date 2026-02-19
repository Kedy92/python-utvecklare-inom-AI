import { generateProductGrid } from "./products.js";

const products = [
    {
      image: "https://media.istockphoto.com/id/483960103/photo/blank-black-t-shirt-front-with-clipping-path.jpg?s=612x612&w=0&k=20&c=d8qlXILMYhugXGw6zX7Jer2SLPrLPORfsDsfRDWc-50=",
      alt: "Front of men's Basic Tee in black.",
      name: "Basic Tee",
      color: "Black",
      price: "$35",
    },
    {
      image: "https://media.istockphoto.com/id/483960103/photo/blank-black-t-shirt-front-with-clipping-path.jpg?s=612x612&w=0&k=20&c=d8qlXILMYhugXGw6zX7Jer2SLPrLPORfsDsfRDWc-50=",
      alt: "Front of girl's Basic Tee in black.",
      name: "Elite Tee",
      color: "Black",
      price: "$45",
    },
  ];
  
  generateProductGrid(products);
  




// let names = ["Tobias", "Hans", "Hanna"];

// names.forEach((name, index) => {
//   console.log(index, name);
// });

// let newNames = names.map((name) => name + " slutet");
// console.log(newNames);

// const students = [
//   { name: "Bob", grade: 72 },
//   { name: "Charlie", grade: 90 },
//   { name: "Diana", grade: 65 },
// ];

// const passingStudents = students.filter((s) => s.grade >= 75);
// console.log(passingStudents);








// let itemsInCart = 0;

// document.getElementById("buy").onclick = function () {
//   let cart = document.getElementById("cart");
//   let hidden = cart.classList.contains("hidden");

//   document.getElementById("remove").addEventListener("click", function () {
//     if (itemsInCart >= 1) {
//       itemsInCart -= 1;
//     }
//     document.getElementById("items").textContent = itemsInCart;
//   });
  
  

//   // Option A: ternary
//   hidden === true ? cart.classList.remove("hidden") : console.log("Not hidden");

//   // Option B (more common in React):
//   // hidden === true && cart.classList.remove("hidden");

//   let items = document.getElementById("items");
//   itemsInCart += 1;
//   items.textContent = itemsInCart;
// };




// document.getElementById("buy").onclick = function () {
//     let cart = document.getElementById("cart");
//     let hidden = cart.classList.contains("hidden");
    
//     // ... rest of buy handler code ...
//     items.textContent = itemsInCart;
//   }; // ← Line 16 - buy handler ends here
  
//   // ADD THE REMOVE HANDLER HERE (after line 16):
//   document.getElementById("remove").onclick = function () {
//     if (itemsInCart >= 1) {
//       itemsInCart -= 1;
//     }
//     document.getElementById("items").textContent = itemsInCart;
//   };