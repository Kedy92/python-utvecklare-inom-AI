
import { Link } from "react-router-dom";

export default function Header() {
  return (
    <header className="container relative flex items-center h-20 mx-auto">
      <img
        src="https://www.utvecklarakademin.se/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Fshort_logo_transparent.0790d1fb.png&w=96&q=75"
        alt=""
        className="h-14"
      />
      <div className="flex items-center ml-auto">
        <ul className="flex justify-around w-50">
       
          <Link className="hover:underline hover:text-gray-500" to="/">Home</Link>
          <Link className="hover:underline hover:text-gray-500" to="/contact">Contact</Link>
          <Link className="hover:underline hover:text-gray-500" to="/about">About</Link>
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
  );
}
