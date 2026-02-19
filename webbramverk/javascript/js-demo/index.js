// first in demo here. commented for generate products
// -------------------------------------------------

// let itemsInCart = 0;

// document.getElementById("buy").addEventListener("click", function () {
//   // Show the cart if it's hidden
//   const cart = document.getElementById("cart");
//   const isHidden = cart.classList.contains("hidden");

//   if (isHidden === true) {
//     cart.classList.remove("hidden");
//   }

//   // Update the count
//   itemsInCart += 1;
//   document.getElementById("items").textContent = itemsInCart;
// });

// document.getElementById("remove").addEventListener("click", function () {
//   if (itemsInCart >= 1) {
//     itemsInCart -= 1;
//     document.getElementById("items").textContent = itemsInCart;
//   }
// });

// -----------------------------------------


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
  {
    image: "https://media.istockphoto.com/id/483960103/photo/blank-black-t-shirt-front-with-clipping-path.jpg?s=612x612&w=0&k=20&c=d8qlXILMYhugXGw6zX7Jer2SLPrLPORfsDsfRDWc-50=",
    alt: "Front of dog's Basic Tee in black.",
    name: "Better Tee",
    color: "Black",
    price: "$55",
  },
];

let itemsInCart = 0;

// Render the products when the page loads
generateProductGrid(products);

// Cart functionality
document.getElementById("buy").addEventListener("click", function () {
  const cart = document.getElementById("cart");
  const isHidden = cart.classList.contains("hidden");

  isHidden && cart.classList.remove("hidden");

  itemsInCart += 1;
  document.getElementById("items").textContent = itemsInCart;
});

document.getElementById("remove").addEventListener("click", function () {
  if (itemsInCart >= 1) {
    itemsInCart -= 1;
    document.getElementById("items").textContent = itemsInCart;
  }
});