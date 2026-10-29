
import { useEffect, useState } from "react";
import axios from "axios";
import Register from "./components/Register";
import UserList from "./components/UserList";



const API = "http://localhost:5000/users";

function App() {
  const [users, setUsers] = useState([]);
  const [editUser, setEditUser] = useState(null);

  const fetchUsers = async () => {
    try {
      const response = await axios.get(API);
      setUsers(response.data);
    } catch (error) {
      console.error("Error fetching users:", error);
    }
  };

  useEffect(() => {
    fetchUsers();
  }, []);

  return (
    <div style={{ padding: "30px", fontFamily: "Arial" }}>
      <h1>Axios CRUD Operations</h1>

      <Register
        editUser={editUser}
        fetchUsers={fetchUsers}
        cancelEdit={() => setEditUser(null)}
      />

      <hr />

      <UserList
        users={users}
        fetchUsers={fetchUsers}
        setEditUser={setEditUser}
      />
    </div>
  );
}

export default App;
