import { useEffect, useState } from "react";
import Login from "./Login";
import Homepage from "./Homepage";
import "./App.css";

function App() {

  const [user, setUser] = useState({
    username: undefined,
    password: undefined,
    success: false,
    validate: true,
  });

  return (
    <div>
      <Homepage user={user} setUser={setUser}/>
      <Login user={user} setUser={setUser}/>
    </div>
  );
}

export default App;
