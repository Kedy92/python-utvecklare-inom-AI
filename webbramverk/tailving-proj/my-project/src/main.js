import "./style.css";

const products = [
  { id: 1, title: "T-Shirt", price: 19.99, img: "https://picsum.photos/seed/shirt1/800/1200" },
  { id: 2, title: "T-Shirt", price: 24.99, img: "https://picsum.photos/seed/shirt2/800/1200" },
  { id: 3, title: "T-Shirt", price: 29.99, img: "https://picsum.photos/seed/shirt3/800/1200" },
  { id: 4, title: "T-Shirt", price: 19.99, img: "https://picsum.photos/seed/shirt4/800/1200" },
  { id: 5, title: "T-Shirt", price: 24.99, img: "https://picsum.photos/seed/shirt5/800/1200" },
  { id: 6, title: "T-Shirt", price: 29.99, img: "https://picsum.photos/seed/shirt6/800/1200" },
  { id: 7, title: "T-Shirt", price: 19.99, img: "https://picsum.photos/seed/shirt7/800/1200" },
  { id: 8, title: "T-Shirt", price: 24.99, img: "https://picsum.photos/seed/shirt8/800/1200" },
];

function productCard(p) {
  // NOTE: avoid HTML comments inside template strings (they sometimes mess with students when copy/pasting)
  return `
    <article class="overflow-hidden rounded-2xl bg-white shadow-md ring-1 ring-black/5">
      <div class="aspect-[2/3] bg-slate-100">
        <img
          src="${p.img}"
          alt="${p.title}"
          class="h-full w-full object-cover"
          loading="lazy"
        />
      </div>

      <div class="flex flex-col gap-3 p-4">
        <div class="flex items-center justify-between">
          <h2 class="text-lg font-semibold">${p.title}</h2>
          <span class="text-sm text-slate-500">${p.price.toFixed(2)} SEK</span>
        </div>

        <button
          class="mt-auto inline-flex w-fit items-center justify-center rounded-full bg-purple-600 px-5 py-2 text-white font-semibold hover:bg-purple-500"
          type="button"
        >
          Köp
        </button>
      </div>
    </article>
  `;
}

function render() {
  const app = document.querySelector("#app");

  app.innerHTML = `
    <main class="min-h-screen bg-slate-50">
      <div class="mx-auto max-w-6xl px-6 py-10">
        <header class="text-center">
          <h1 class="text-4xl font-bold">T-Shirt Collection</h1>
          <p class="mt-2 text-slate-600">A small Tailwind grid demo (Vite + Tailwind)</p>
        </header>

        <section class="mt-10 grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
          ${products.map(productCard).join("")}
        </section>
      </div>
    </main>
  `;
}

render();