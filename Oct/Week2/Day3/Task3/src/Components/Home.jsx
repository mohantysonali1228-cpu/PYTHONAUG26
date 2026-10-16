
import { useTheme } from "../ThemeContext";

export default function Home() {
  const { theme } = useTheme();

  return (
    <main
      className={`flex min-h-[70vh] flex-col items-center justify-center p-10 ${
        theme === "dark"
          ? "bg-gray-800 text-white"
          : "bg-gray-100 text-gray-900"
      }`}
    >
      <h2 className="mb-4 text-4xl font-bold">
        Welcome to My Website!
      </h2>

      <p className="text-lg">
        This application uses React useContext and useState.
      </p>

      <p className="mt-3">
        Current Theme: {theme === "dark" ? "Dark Mode" : "Light Mode"}
      </p>
    </main>
  );
}
