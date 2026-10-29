
import { useEffect, useState } from "react";
import axios from "axios";
import { toast } from "react-toastify";

const API = "http://localhost:5000/users";

function Register({ editUser, fetchUsers, cancelEdit }) {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");

  useEffect(() => {
    setName(editUser?.name || "");
    setEmail(editUser?.email || "");
  }, [editUser]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const user = { name, email };

      if (editUser) {
        await axios.put(`${API}/${editUser.id}`, user);
        toast.success("User updated successfully!");
      } else {
        await axios.post(API, user);
        toast.success("User registered successfully!");
      }

      setName("");
      setEmail("");
      cancelEdit();
      fetchUsers();
    } catch (error) {
      console.error(error);
      toast.error("Unable to save user. Check the server.");
    }
  };

  return (
    <div>
      <h2>{editUser ? "Update User" : "Register User"}</h2>

      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Enter Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />

        <br /><br />

        <input
          type="email"
          placeholder="Enter Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />

        <br /><br />

        <button type="submit">
          {editUser ? "Update" : "Register"}
        </button>

        {editUser && (
          <button
            type="button"
            onClick={() => {
              setName("");
              setEmail("");
              cancelEdit();
              toast.info("Edit cancelled");
            }}
          >
            Cancel
          </button>
        )}
      </form>
    </div>
  );
}

export default Register;
