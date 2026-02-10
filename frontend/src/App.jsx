import { useEffect, useState } from "react";

function App() {
  const [facts, setFacts] = useState([]);
  const [error, setError] = useState("");

  useEffect(() => {
    fetch(
  "https://flask-facts-backend-praveen-htbpf8dkgqbxbjds.centralindia-01.azurewebsites.net/api/facts"
)
      .then((res) => {
        if (!res.ok) {
          throw new Error("API error");
        }
        return res.json();
      })
      .then((data) => setFacts(data))
      .catch((err) => setError(err.message));
  }, []);

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h1>Facts List</h1>

      {error && <p style={{ color: "red" }}>{error}</p>}

      <ul>
        {facts.map((item) => (
          <li key={item.id}>{item.fact}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;
