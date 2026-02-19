export function generateProductGrid(products) {
    const gridContainer = document.querySelector(".grid");
  
    // Clear existing content
    gridContainer.innerHTML = "";
  
    // Using for loop
    for (let i = 0; i < products.length; i++) {
      const product = products[i];
  
      const productElement = `
        <div class="relative group">
          <div class="w-full overflow-hidden bg-gray-200 rounded-md min-h-80 aspect-w-1 aspect-h-1 group-hover:opacity-75 lg:aspect-none lg:h-80">
            <img src="${product.image}" alt="${product.alt}" class="object-cover object-center w-full h-full lg:h-full lg:w-full" />
          </div>
          <div class="flex justify-between mt-4">
            <div>
              <h3 class="text-sm text-gray-700">
                <a href="#">
                  <span aria-hidden="true" class="absolute inset-0"></span>
                  ${product.name}
                </a>
              </h3>
              <p class="mt-1 text-sm text-gray-500">${product.color}</p>
            </div>
            <p class="text-sm font-medium text-gray-900">${product.price}</p>
          </div>
        </div>
      `;
  
      gridContainer.innerHTML += productElement;
    }
  }
  