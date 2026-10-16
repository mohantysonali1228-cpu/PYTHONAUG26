
import { useTheme } from "../ThemeContext";

export default function Footer() {
  const { theme } = useTheme();

  return (
    <footer
      className={`p-5 text-center ${
        theme === "dark"
          ? "bg-black text-white"
          : "bg-white text-gray-700"
      }`}
    >
      <p>© 2026 My Website. All rights reserved.</p>
    </footer>
  );
}
