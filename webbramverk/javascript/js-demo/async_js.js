// Delayed message using setTimeout (asynchronous)
document.getElementById("delayBtn").addEventListener("click", function () {
    const output = document.getElementById("output");
    output.innerHTML = "<p>Wait for 3 seconds...</p>";
  
    setTimeout(function () {
      output.innerHTML +=
        "<p>Delayed Message: This shows up after 3 seconds!</p>";
    }, 3000);
  });
  
  // Fetching data from an API (asynchronous with async/await)
  document.getElementById("fetchBtn").addEventListener("click", async function () {
    const output = document.getElementById("output");
    output.innerHTML = "<p>Fetching products...</p>";
  
    try {
      const response = await fetch("https://fakestoreapi.com/products");
      const products = await response.json();
  
      output.innerHTML = "<p>Products fetched successfully!</p>";
  
      products.forEach((product) => {
        output.innerHTML += `<p>${product.title} - $${product.price}</p>`;
      });
    } catch (error) {
      output.innerHTML = "<p>Error fetching products!</p>";
    }
  });