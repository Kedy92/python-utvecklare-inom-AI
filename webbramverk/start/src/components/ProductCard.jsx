import React from "react";

export default function ProductCard({ product, setCart }) {
  return (
    <div key={product.id} className="relative z-20 shadow group">
      {product.discount != null && (
        <div className="absolute p-1 text-sm font-bold text-red-900 bg-red-200 rounded-xl top-4 left-4">
          - {product.discount}%
        </div>
      )}
      <div className="object-cover overflow-hidden bg-gray-100 rounded-t-lg aspect-square">
        <img
          src="https://dressmann.imgix.net/globalassets/productimages/72134817213482_900_f_m_mh_185_ms_m_t-shirt_solid_v-n___dressmann_4908.jpg"
          alt="Product image"
          className="object-cover w-full h-full transition-all"
        />
      </div>
      <div className="px-2 py-4">
        <p className="text-sm text-gray-500">{product.brand}</p>
        <h3 className="font-medium">{product.name}</h3>
        <div className="flex items-end">
          <p className="text-xl font-bold">{product.price} kr</p>
          {product.discount != null && (
            <p className="ml-4 text-gray-400 line-through">
              {product.originalPrice} kr
            </p>
          )}
        </div>

        <div className="flex items-center pt-2 border-t border-gray-100">
          <svg viewBox="0 0 24 24" className="w-4 h-4 text-gray-600">
            <path
              fill="currentColor"
              d="M2.231 8.25h2.282a.75.75 0 0 0 0-1.5H2.231a.75.75 0 0 0 0 1.5m7.519-1.5A.75.75 0 0 0 9 7.5v1.29l-1.32-.33a.75.75 0 0 0-.363 1.456l1.154.288-1.01 1.347a.75.75 0 1 0 1.2.9L9.75 11l1.087 1.45a.749.749 0 1 0 1.2-.9l-1.01-1.346 1.155-.288a.75.75 0 0 0-.364-1.456l-1.318.33V7.5a.75.75 0 0 0-.75-.75m-5.253 4.5a.75.75 0 0 0 0-1.5H.753a.75.75 0 0 0 0 1.5zm.016 3.001a.75.75 0 0 0 0-1.5H2.211a.75.75 0 0 0 0 1.5z"
            />
            <path
              fill="currentColor"
              d="m23.81 11.501-3.367-3.738a.75.75 0 0 0-.558-.248h-3.378V4.497a.75.75 0 0 0-.75-.75H3.712a.75.75 0 0 0 0 1.5l11.299-.004.002 10.513-4.953.004c-.518-.897-1.477-1.508-2.588-1.508s-2.07.61-2.588 1.508H3.712a.75.75 0 1 0 0 1.5h.761a2.999 2.999 0 0 0 5.998 0h5.276l.76.003a2.999 2.999 0 0 0 5.996 0h.75a.75.75 0 0 0 .75-.75v-4.51a.75.75 0 0 0-.193-.502m-16.338 7.25a1.5 1.5 0 1 1 0-2.999 1.5 1.5 0 0 1 0 2.999m12.033 0a1.5 1.5 0 1 1 0-2.999 1.5 1.5 0 0 1 0 2.999m2.997-2.988h-.408c-.518-.899-1.477-1.511-2.59-1.511s-2.07.612-2.589 1.511h-.403l-.003-6.748h3.042l2.951 3.278z"
            />
          </svg>
          {product.hasQuickDelivery ? (
            <span className="ml-2 text-xs text-gray-600">Snabbleverans</span>
          ) : (
            <span className="ml-2 text-xs text-gray-600">Normal leverans</span>
          )}
        </div>
        <div
          onClick={() => setCart(product)}
          className="text-center w-full bg-indigo-600 text-white shadow-lg cursor-pointer px-4 py-2 my-2 hover:bg-indigo-500"
        >
          Buy
        </div>
      </div>
    </div>
  );
}
