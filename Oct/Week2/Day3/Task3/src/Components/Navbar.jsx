
import { useTheme } from "../ThemeContext";

export default function Navbar() {
  const { theme, lightMode, darkMode } = useTheme();

  return (
    <nav
      className={`flex items-center justify-between p-5 shadow ${
        theme === "dark"
          ? "bg-gray-900 text-white"
          : "bg-white text-gray-900"
      }`}
    >
      <h1 className="text-2xl font-bold">My Website</h1>

      <div className="flex gap-3">
        <button
          onClick={lightMode}
          className="rounded bg-yellow-400 px-4 py-2 text-black"
        >
          Light Mode
        </button>

        <button
          onClick={darkMode}
          className="rounded bg-gray-700 px-4 py-2 text-white"
        >
          Dark Mode
        </button>
      </div>
    </nav>
  );
}
