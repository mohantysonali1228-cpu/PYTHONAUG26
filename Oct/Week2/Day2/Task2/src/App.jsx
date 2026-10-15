
import React, { useState } from "react";

function App() {
  const fields = [
    { name: "name", label: "Full Name", type: "text", placeholder: "Enter your name" },
    { name: "email", label: "Email Address", type: "email", placeholder: "Enter your email" },
    { name: "password", label: "Password", type: "password", placeholder: "Enter your password" },
    { name: "confirmPassword", label: "Confirm Password", type: "password", placeholder: "Confirm your password" },
  ];

  const [formData, setFormData] = useState({
    name: "",
    email: "",
    password: "",
    confirmPassword: "",
  });

  const [message, setMessage] = useState("");
  const [registeredUser, setRegisteredUser] = useState(null);

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    if (
      !formData.name ||
      !formData.email ||
      !formData.password ||
      !formData.confirmPassword
    ) {
      return;
    }

    if (formData.password.length < 6) {
      return;
    }

    if (formData.password !== formData.confirmPassword) {
      return;
    }

    setRegisteredUser({
      name: formData.name,
      email: formData.email,
    });


    setFormData({
      name: "",
      email: "",
      password: "",
      confirmPassword: "",
    });
  };

  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center p-4">
      <div className="w-full max-w-md bg-white p-8 rounded-2xl shadow-lg">
        <h1 className="text-3xl font-bold text-center text-blue-600 mb-2">
          Create Account
        </h1>

        <p className="text-center text-gray-500 mb-6">
          Register to get started
        </p>

        <form onSubmit={handleSubmit} className="space-y-4">
          {fields.map((field) => (
            <div key={field.name}>
              <label className="block text-sm font-medium text-gray-700 mb-1">
                {field.label}
              </label>

              <input
                type={field.type}
                name={field.name}
                placeholder={field.placeholder}
                value={formData[field.name]}
                onChange={handleChange}
                className="w-full border border-gray-300 rounded-lg px-4 py-3 outline-none focus:ring-2 focus:ring-blue-500"
              />
            </div>
          ))}

          <button
            type="submit"
            className="w-full bg-blue-600 hover:bg-blue-700 text-white font-semibold py-3 rounded-lg transition"
          >
            Register
          </button>
        </form>

      

      </div>
    </div>
  );
}

export default App;