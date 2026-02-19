import { createRoot } from "react-dom/client";
import "./index.css";
import Home from "./pages/Home";

createRoot(document.getElementById("root")).render(
  <div className="flex flex-col h-screen">
    <header className="h-20 bg-black"></header>
    <div className="flex-auto">
      <Home></Home>
    </div>
    <footer className="h-40 bg-black"></footer>
  </div>
);
