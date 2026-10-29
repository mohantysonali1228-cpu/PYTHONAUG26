
import axios from "axios";
import { toast } from "react-toastify";

const API = "http://localhost:5000/users";

function UserList({ users, fetchUsers, setEditUser }) {
  const deleteUser = async (id) => {
    try {
      await axios.delete(`${API}/${id}`);
      toast.success("User deleted successfully!");
      fetchUsers();
    } catch (error) {
      console.error(error);
      toast.error("Unable to delete user.");
    }
  };

  return (
    <div>
      <h2>All Users</h2>

      <table border="1" cellPadding="10">
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
            <th>Actions</th>
          </tr>
        </thead>

        <tbody>
          {users.length === 0 ? (
            <tr>
              <td colSpan="4">No users found</td>
            </tr>
          ) : (
            users.map((user) => (
              <tr key={user.id}>
                <td>{user.id}</td>
                <td>{user.name}</td>
                <td>{user.email}</td>
                <td>
                  <button onClick={() => setEditUser(user)}>
                    Edit
                  </button>{" "}

                  <button onClick={() => deleteUser(user.id)}>
                    Delete
                  </button>
                </td>
              </tr>
            ))
          )}
        </tbody>
      </table>
    </div>
  );
}

export default UserList;
