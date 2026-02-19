Note: This exercise is meant to be used for a lecture demo and might not make 100% sense to you doing it alone

Start code which includes the boilerplate react code and a fastapi API

[start.zip](attachment:957d68fa-1408-4f5f-8793-c2977f244f42:start.zip)

## Installation av React

```html
npm create vite@latest
npm install tailwindcss @tailwindcss/vite
npm install react-router-dom localforage match-sorter sort-by
```

- Välj ett projektnamn
- Välj React
- Välj Javascript (Du får köra typescript om du absolut vill de)

### Lägg till tailwind

Tailwind uppdaterades nyligen till Tailwind 4 - Overall är det för det mesta bara förbättringar, och förenklaringar av installationsprocessen. Nice! Det för dock att många tutorials online är utdaterade… ouch. 

https://tailwindcss.com/blog/tailwindcss-v4#css-first-configuration

1. npm install tailwindcss @tailwindcss/vite

https://tailwindcss.com/docs/installation/using-vite

1. Kopiera in detta i vite.config.js

```jsx
import tailwindcss from "@tailwindcss/vite";
import react from "@vitejs/plugin-react";
import { defineConfig } from "vite";

// https://vite.dev/config/
export default defineConfig({
  plugins: [tailwindcss(), react()],
});

```

1. Add an import to your css-file
2. 

```
@import "tailwindcss";
```

## API - Small fastapi API for testing using docker

- You need to have docker installed - will create and expose a small fastapi-application

```
docker-compose up --build
docker-compose down

// To remove old data
docker volume rm $(docker volume ls -q --filter name=postgres_data)
api_postgres_data
```

## Goals of this lecture:

- Learn how to use basics of react router 6
- Using the useEffect-hook
- using fetch()
- Basic onChange usage

`pages/Home.jsx`

```jsx
import React, { useState } from "react";
import ProductCard from "../components/ProductCard";

function Home() {
  const products = [
    {
      id: 1,
      name: "Nike Air Max 500",
      brand: "Nike",
      price: 899,
      originalPrice: 999,
      discount: 10,
      features: ["Premium Material", "Cushioned Sole", "Breathable"],
      isInStock: true,
      hasQuickDelivery: true,
      imageUrl:
        "https://dressmann.imgix.net/globalassets/productimages/72134817213482_900_f_m_mh_185_ms_m_t-shirt_solid_v-n___dressmann_4908.jpg",
    },
    {
      id: 2,
      name: "Nike Air Force 1",
      brand: "Nike",
      price: 1199,
      originalPrice: 1399,
      discount: 10,
      features: ["Classic Design", "Leather Upper", "Iconic Style"],
      isInStock: true,
      hasQuickDelivery: true,
      imageUrl:
        "https://dressmann.imgix.net/globalassets/productimages/72134817213482_900_f_m_mh_185_ms_m_t-shirt_solid_v-n___dressmann_4908.jpg",
    },
    {
      id: 3,
      name: "Nike Zoom Pegasus",
      brand: "Nike",
      price: 1299,
      originalPrice: 1499,
      discount: null,
      features: ["Responsive Cushioning", "Engineered Mesh", "Dynamic Fit"],
      isInStock: true,
      hasQuickDelivery: true,
      imageUrl:
        "https://dressmann.imgix.net/globalassets/productimages/72134817213482_900_f_m_mh_185_ms_m_t-shirt_solid_v-n___dressmann_4908.jpg",
    },
    {
      id: 4,
      name: "Nike React Vision",
      brand: "Nike",
      price: 1099,
      originalPrice: 1299,
      discount: 10,
      features: ["React Foam", "Modern Design", "All-Day Comfort"],
      isInStock: true,
      hasQuickDelivery: true,
      imageUrl:
        "https://dressmann.imgix.net/globalassets/productimages/72134817213482_900_f_m_mh_185_ms_m_t-shirt_solid_v-n___dressmann_4908.jpg",
    },
    {
      id: 5,
      name: "Nike Air Max 270",
      brand: "Nike",
      price: 1399,
      originalPrice: 1599,
      discount: 10,
      features: ["Air Unit", "Knit Upper", "Lightweight"],
      isInStock: true,
      hasQuickDelivery: true,
      imageUrl:
        "https://dressmann.imgix.net/globalassets/productimages/72134817213482_900_f_m_mh_185_ms_m_t-shirt_solid_v-n___dressmann_4908.jpg",
    },
    {
      id: 6,
      name: "Nike Air Zoom",
      brand: "Nike",
      price: 1199,
      originalPrice: 1399,
      discount: null,
      features: ["Zoom Air", "Durable Design", "Responsive"],
      isInStock: true,
      hasQuickDelivery: true,
      imageUrl:
        "https://dressmann.imgix.net/globalassets/productimages/72134817213482_900_f_m_mh_185_ms_m_t-shirt_solid_v-n___dressmann_4908.jpg",
    },
    {
      id: 7,
      name: "Nike Free Run",
      brand: "Nike",
      price: 999,
      originalPrice: 1199,
      discount: 10,
      features: ["Flexible Sole", "Minimalist Design", "Natural Motion"],
      isInStock: true,
      hasQuickDelivery: false,
      imageUrl:
        "https://dressmann.imgix.net/globalassets/productimages/72134817213482_900_f_m_mh_185_ms_m_t-shirt_solid_v-n___dressmann_4908.jpg",
    },
    {
      id: 8,
      name: "Nike Metcon",
      brand: "Nike",
      price: 1299,
      originalPrice: 1499,
      discount: 10,
      features: ["Stable Base", "Durable Construction", "Versatile"],
      isInStock: true,
      hasQuickDelivery: false,
      imageUrl:
        "https://dressmann.imgix.net/globalassets/productimages/72134817213482_900_f_m_mh_185_ms_m_t-shirt_solid_v-n___dressmann_4908.jpg",
    },
    {
      id: 9,
      name: "Nike Revolution",
      brand: "Nike",
      price: 899,
      originalPrice: 999,
      discount: 10,
      features: ["Lightweight", "Breathable Mesh", "Foam Cushioning"],
      isInStock: true,
      hasQuickDelivery: true,
      imageUrl:
        "https://dressmann.imgix.net/globalassets/productimages/72134817213482_900_f_m_mh_185_ms_m_t-shirt_solid_v-n___dressmann_4908.jpg",
    },
  ];

  const [cart, setCart] = useState([]);

  function addToCart(product) {
    setCart([...cart, product]);
  }

  return (
    <div className="container mx-auto">
      <div className="flex flex-col h-screen">
        <div className="border-b border-gray-300">
          <header className="container relative flex items-center h-20 mx-auto">
            <img
              src="https://www.utvecklarakademin.se/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fshort_logo_transparent.0790d1fb.png&w=96&q=75"
              alt=""
              className="h-14"
            />
            <div className="flex items-center ml-auto">
              <ul className="flex justify-around w-50">
                <a className="hover:underline hover:text-gray-500" href="/">
                  <li>Home</li>
                </a>
                <a
                  className="hover:underline hover:text-gray-500"
                  href="/contact"
                >
                  <li>Contact</li>
                </a>
                <a
                  className="hover:underline hover:text-gray-500"
                  href="/about"
                >
                  <li>About</li>
                </a>
              </ul>
              <button className="ml-4 flex items-center justify-center px-5 py-1.5 font-medium text-white bg-linear-to-r/srgb from-indigo-500 to-indigo-300 rounded-lg">
                Login
              </button>
              <svg
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 24 24"
                className="md:hidden"
              >
                <path
                  d="M3 6h18M3 12h18M3 18h18"
                  stroke="currentColor"
                  strokeWidth="2"
                  strokeLinecap="round"
                  fill="none"
                />
              </svg>
            </div>
          </header>
        </div>
        <section className="flex-1">
          <div className="absolute right-0 p-4 bg-white border border-gray-300 shadow-lg top-20 w-60 min-h-40">
            Cart
            {cart.map((item) => {
              return <p>{item.name}</p>;
            })}
          </div>
          <div className="container mx-auto">
            <h1 className="mt-10 text-6xl font-bold">UA Products</h1>
            <hr className="my-10 text-gray-300" />
            <div className="grid grid-cols-1 gap-10 px-4 my-20 md:px-2 md:grid-cols-3 lg:grid-cols-4">
              {products.map((product) => {
                return (
                  <ProductCard
                    key={product.id}
                    product={product}
                    setCart={addToCart}
                  ></ProductCard>
                );
              })}
            </div>
          </div>
        </section>
        <footer className="bg-white border-t border-gray-300 h-[300px] flex items-center">
          <div className="grid w-full grid-cols-4 px-10 place-items-center">
            <ul>
              <li>Hem</li>
              <li>Contact</li>
              <li>About</li>
              <li>Login</li>
            </ul>
            <ul>
              <li>Hem</li>
              <li>Contact</li>
              <li>About</li>
              <li>Login</li>
            </ul>
            <ul>
              <li>Hem</li>
              <li>Contact</li>
              <li>About</li>
              <li>Login</li>
            </ul>
            <ul>
              <li>Hem</li>
              <li>Contact</li>
              <li>About</li>
              <li>Login</li>
            </ul>
          </div>
        </footer>
      </div>
    </div>
  );
}

export default Home;

```

Create a utils.js-file in src

- A nice utility function which can help us dynamically add css-classes

```jsx
export function classNames(...classes) {
  return classes.filter(Boolean).join(" ");
}
```

## React router 6

This is how we used to do it, in previous versions:

```jsx
import { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import { Route, BrowserRouter as Router, Routes } from "react-router-dom";
import "./index.css";
import AboutPage from "./pages/About";
import HomePage from "./pages/Home";

createRoot(document.getElementById("root")).render(
  <StrictMode>
    <Router>
      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/about" element={<AboutPage />} />
      </Routes>
    </Router>
  </StrictMode>
);
```

- Vi använder routing för att kunna skapa flera sidor
- Routing görs via javascript och refreshar ej din sida

main.jsx

```jsx
import { createRoot } from "react-dom/client";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import "./index.css";
import HomePage from "./pages/HomePage.jsx";

const router = createBrowserRouter([
]);

createRoot(document.getElementById("root")).render(
  <RouterProvider router={router} />
);

```

`Layout.jsx`

We generally add some kind of component that contains the main components of our app

- Header should always be visible
- Footer should always be visible
- We can add an “Outlet” which will output whatever component

```jsx
import React from "react";
import { Outlet } from "react-router-dom";
import Footer from "./components/Footer";
import Header from "./components/Header";

function Layout() {
  return (
    <div className="flex flex-col min-h-screen">
      <Header></Header>
			   <div>Hello</div>
      <Footer></Footer>
    </div>
  );
}

export default Layout;
```

```python
import { createRoot } from "react-dom/client";
import { createBrowserRouter, RouterProvider } from "react-router-dom";
import "./index.css";
import About from "./pages/About.jsx";
import Layout from "./pages/Layout.jsx";

const router = createBrowserRouter([
  {
    path: "/",
    element: <Layout />,
    children: [
      {
        path: "/",
        element: <Home />,
      },
      {
        path: "/about",
        element: <About />,
      }
    ],
  },
]);

createRoot(document.getElementById("root")).render(
  <RouterProvider router={router} />
);

```

## useEffect - A hook that has many usecases

1. It runs on mount
2. It runs whenever a variable in its dependency array is mutated
3. It runs when the component unmounts

Below, I show you a typical usecase where we use useEffect to fetch some data when the page loads. Meaning, we fetch the data on mount (option 1, we don’t need to use the second and third functions of useEffect)

ProductsPage.jsx

```jsx
import React, { useEffect, useState } from "react";
import { classNames } from "../utils";
import ProductCard from "./ProductCard";

function ProductsPage() {
  const [products, setProducts] = useState([]);
  const [productCart, setProductCart] = useState([]);
  const [hideCart, setHideCart] = useState(false);

  async function fetchProducts() {
    try {
      const response = await fetch("http://localhost:8000/products");
      const data = await response.json();
      console.log(data);
      setProducts(data);
    } catch (error) {
      console.log(error);
    }
  }

  function addProductToCart(product) {
    setProductCart([...productCart, product]);
  }
	
	// The empty array at the end means it will only run when the component mounts
  useEffect(() => {
    fetchProducts();
  }, []);

  return (
    <>
      <div
        className={classNames(
          "fixed p-4 bg-white border border-gray-300 shadow-xl top-5 right-5 w-64 min-h-32 rounded-lg",
          hideCart === true && "hidden"
        )}
      >
        <div className="flex items-center">
          <h3 className="text-lg font-semibold mb-4">Product Cart</h3>
          <div
            className="ml-auto hover:underline cursor-pointer"
            onClick={() => setHideCart(true)}
          >
            Close
          </div>
        </div>
        <ul className="space-y-2">
          {productCart.map((product, index) => (
            <li
              key={index}
              className="flex justify-between items-center p-2 border-b border-gray-200"
            >
              <span>{product.name}</span>
              <span className="text-sm text-gray-500">${product.price}</span>
            </li>
          ))}
        </ul>
        <div className="mt-4">
          <button className="w-full bg-blue-500 text-white py-2 rounded-lg hover:bg-blue-600">
            Checkout
          </button>
        </div>
      </div>
      <div className="grid grid-cols-3 gap-8 my-20">
        {products.map((product, index) => (
          <ProductCard
            product={product}
            handleBuy={addProductToCart}
            key={index}
          />
        ))}
      </div>
    </>
  );
}

export default ProductsPage;

```

## Dynamic routes react-router and useParams

Adding a dynamic route, e.g /products/:productId we can create a detail-page for a product

We get the id for the product from the URL using useParams

productpage.jsx

```jsx
import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";

export default function ProductPage() {
  const { productId } = useParams();
  const [product, setProduct] = useState({});

  useEffect(() => {
    async function fetchProduct() {
      try {
        const response = await fetch(
          `http://localhost:8000/products/${productId}`
        );
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        setProduct(data);
      } catch (error) {
        setError(error.message);
      } 
    }

    fetchProduct();
  }, []);

  return (
    <div className="max-w-4xl mx-auto p-6 bg-white border border-gray-200 rounded-lg shadow-md my-10">
      <div className="flex">
        <img
          className="md:w-1/2 h-64 object-cover rounded-lg"
          src="/t_1.png"
          alt={product.name}
        />
        <div className="md:ml-6 mt-4 md:mt-0 flex flex-col justify-between">
          <div>
            <h1 className="text-3xl font-semibold text-gray-900">
              {product.name}
            </h1>
            <p className="text-gray-700 mt-2">${product.price}</p>
            <p className="text-gray-700 mt-4">{product.description}</p>
            {product.is_in_stock === false && (
              <div className="text-red-500 mt-2">Not in stock</div>
            )}
          </div>
          <button
            onClick={() => alert("Added to cart")}
            className="mt-4 w-full bg-blue-500 text-white py-2 rounded-lg hover:bg-blue-600 transition-colors cursor-pointer"
          >
            Add to cart
          </button>
        </div>
      </div>
    </div>
  );
}

```

## onChange

Vi kan använda onChange-eventet på input-fields för att anropa en funktion när något ändras i input-fältet.

Här kan vi läsa vilka events som finns i forms:

https://react.dev/reference/react-dom/components/input

SearchPage.jsx

```jsx
import React, { useEffect, useState } from "react";
import ProductCard from "../components/ProductCard";
import { classNames } from "../utils";

export default function SearchPage() {
  const [products, setProducts] = useState([]);
  const [productCart, setProductCart] = useState([]);
  const [hideCart, setHideCart] = useState(true);
  const [searchQuery, setSearchQuery] = useState("shirt");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  async function fetchProducts(query = "") {
    setLoading(true);
    setError(null);
    try {
      const endpoint = query
        ? `http://localhost:8000/search/products?query=${query}`
        : `http://localhost:8000/products`;
      const response = await fetch(endpoint);
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const data = await response.json();
      console.log(data);
      setProducts(data);
      console.log("In useEffect");
    } catch (error) {
      console.log(error);
      setError(error.message);
    } finally {
      setLoading(false);
    }
  }

  function addProductToCart(product) {
    setProductCart([...productCart, product]);
  }

  useEffect(() => {
    fetchProducts(searchQuery);
  }, [searchQuery]);

  // Uncomment this version to use the onChange event instead of useEffect
  // function handleSearchChange(event) {
  //   const query = event.target.value;
  //   setSearchQuery(query);
  //   fetchProducts(query);
  // }

  return (
    <>
      <div className="flex justify-center my-4">
        <input
          type="text"
          placeholder="Search for products..."
          className="p-2 border border-gray-300 rounded-lg"
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
          // Uncomment this line to use the onChange event instead of useEffect
          // onChange={handleSearchChange}
        />
      </div>
      <div
        className={classNames(
          "fixed p-4 bg-white border border-gray-300 shadow-xl top-5 right-5 w-64 min-h-32 rounded-lg",
          hideCart === true && "hidden"
        )}
      >
        <div className="flex items-center">
          <h3 className="text-lg font-semibold mb-4">Product Cart</h3>
          <div
            className="ml-auto hover:underline cursor-pointer"
            onClick={() => setHideCart(true)}
          >
            Close
          </div>
        </div>
        <ul className="space-y-2">
          {productCart.map((product, index) => (
            <li
              key={index}
              className="flex justify-between items-center p-2 border-b border-gray-200"
            >
              <span>{product.name}</span>
              <span className="text-sm text-gray-500">${product.price}</span>
            </li>
          ))}
        </ul>
        <div className="mt-4">
          <button className="w-full bg-blue-500 text-white py-2 rounded-lg hover:bg-blue-600">
            Checkout
          </button>
        </div>
      </div>
      <div className="grid grid-cols-3 gap-8 my-20">
        {loading && <div>Loading...</div>}
        {error && <div>Error: {error}</div>}
        {!loading && !error && products.length === 0 && (
          <div>No products found</div>
        )}
        {!loading &&
          !error &&
          products.map((product, index) => (
            <ProductCard
              product={product}
              handleBuy={addProductToCart}
              key={index}
            />
          ))}
      </div>
    </>
  );
}

```