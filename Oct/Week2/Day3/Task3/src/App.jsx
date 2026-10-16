
import { ThemeProvider } from "./ThemeContext";
import Navbar from "./Components/Navbar";
import Home from "./Components/Home";
import Footer from "./Components/Footer";

export default function App() {
  return (
    <ThemeProvider>
      <div className="min-h-screen">
        <Navbar />
        <Home />
        <Footer />
      </div>
    </ThemeProvider>
  );
}
