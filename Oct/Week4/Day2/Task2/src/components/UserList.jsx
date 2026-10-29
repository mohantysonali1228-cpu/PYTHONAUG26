import React from "react";
import { toast } from "react-toastify";

function UserList({ users, onEdit, onDelete }) {
  const handleEdit = (user) => {
    onEdit(user);
    toast.info(`Editing ${user.name}`);
  };

  const handleDelete = (id) => {
    onDelete(id);
  };

  return (
    <div className="users-container">
      <h2>All Users</h2>

      {users.length === 0 ? (
        <p>No users found.</p>
      ) : (
        <div className="table-wrapper">
          <table>
            <thead>
              <tr>
                <th>ID</th>
                <th>Name</th>
                <th>Email</th>
                <th>Username</th>
                <th>Actions</th>
              </tr>
            </thead>

            <tbody>
              {users.map((user) => (
                <tr key={user.id}>
                  <td>{user.id}</td>
                  <td>{user.name}</td>
                  <td>{user.email}</td>
                  <td>{user.username}</td>

                  <td>
                    <button onClick={() => handleEdit(user)}>
                      Edit
                    </button>

                    <button
                      className="delete-btn"
                      onClick={() => handleDelete(user.id)}
                    >
                      Delete
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      )}
    </div>
  );
}

export default UserList;