
import { useState, useEffect } from "react";
import axios from "axios";

function App() {
  const API = "https://jsonplaceholder.typicode.com/posts";

  const [posts, setPosts] = useState([]);
  const [title, setTitle] = useState("");
  const [body, setBody] = useState("");
  const [editId, setEditId] = useState(null);


  const getPosts = async () => {
    try {
      const response = await axios.get(API);
      setPosts(response.data.slice(0, 10));
    } catch (error) {
      console.error("Fetch error:", error);
    }
  };

  useEffect(() => {
    getPosts();
  }, []);

  
  const addPost = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post(API, {
        title,
        body,
        userId: 1,
      });

      setPosts((prev) => [
        { ...response.data, id: Date.now() },
        ...prev,
      ]);

      setTitle("");
      setBody("");
    } catch (error) {
      console.error("Create error:", error);
    }
  };




  const updatePost = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.put(`${API}/${editId}`, {
        title,
        body,
        userId: 1,
      });

      setPosts((prev) =>
        prev.map((post) =>
          post.id === editId
            ? { ...post, ...response.data }
            : post
        )
      );

      setEditId(null);
      setTitle("");
      setBody("");
    } catch (error) {
      console.error("Update error:", error);
    }
  };


  const deletePost = async (id) => {
    try {
      await axios.delete(`${API}/${id}`);

      setPosts((prev) =>
        prev.filter((post) => post.id !== id)
      );
    } catch (error) {
      console.error("Delete error:", error);
    }
  };



  return (
    <div style={{ maxWidth: "800px", margin: "30px auto" }}>
      <h1>Axios CRUD Operations</h1>

      <form onSubmit={editId !== null ? updatePost : addPost}>
        <input
          type="text"
          placeholder="Enter title"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          required
        />

        <br /><br />

        <textarea
          placeholder="Enter body"
          value={body}
          onChange={(e) => setBody(e.target.value)}
          required
        />

        <br /><br />

        <button type="submit">
          {editId !== null ? "Update Post" : "Create Post"}
        </button>

        {editId !== null && (
          <button type="button" onClick={cancelEdit}>
            Cancel
          </button>
        )}
      </form>

      <hr />

      <h2>All Posts</h2>

      {posts.map((post) => (
        <div
          key={post.id}
          style={{
            border: "1px solid gray",
            padding: "15px",
            marginBottom: "10px",
          }}
        >
          <h3>{post.title}</h3>
          <p>{post.body}</p>

       

          <button onClick={() => deletePost(post.id)}>
            Delete
          </button>
        </div>
      ))}
    </div>
  );
}

export default App;
