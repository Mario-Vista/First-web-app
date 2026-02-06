import { useEffect, useState } from "react";
import Homepage from "./Homepage";
import "./App.css";

export default function Login({user,setUser}) {
  

  // useEffect(()=>{console.log("success: ", user.success)},[user.success])

  const handleLogin = async (e) => {
    const response = await fetch("http://localhost:8000/login", {
      method: "POST",
      headers: {
        "Content-type": "application/json",
      },
      body: JSON.stringify({
        username: user.username,
        password: user.password,
      }),
    });
    const data = await response.json();
    setUser((prev) => ({
      ...prev,
      username: data.username,
      password: undefined,
      success: data.success,
      validate:data.validate
    }));
  };

  const handleRegister = async (e) => {
    const response = await fetch("http://localhost:8000/signup", {
      method: "POST",
      headers: {
        "Content-type": "application/json",
      },
      body: JSON.stringify({
        username: user.username,
        password: user.password,
      }),
    });
    const data = await response.json();
    setUser((prev) => ({
      ...prev,
      username: data.username,
      success: data.success,
      password: undefined,
      validate:data.validate
    }));
  };

  return (
    <>
      {!user.success && (
        <div className="login-container">
          <h2 className="login-title">Login</h2>

          <div className="login-field">
            <label htmlFor="username">Username</label>
            <input
              id="username"
              type="text"
              placeholder="Inserisci username"
              onChange={(event) => {
                setUser((prev) => ({ ...prev, username: event.target.value }));
              }}
            />
          </div>

          <div className="login-field">
            <label htmlFor="password">Password</label>
            <input
              id="password"
              type="password"
              placeholder="Inserisci password"
              onChange={(event) => {
                setUser((prev) => ({ ...prev, password: event.target.value }));
              }}
            />
          </div>

          <button className="login-button" onClick={handleLogin}>
            Login
          </button>

          <button className="login-button" onClick={handleRegister}>
            Sign up
          </button>
          {!user.validate && (
            <div className="login-error">Credenziali non valide</div>
          )}
        </div>
      )}
    </>
  );
}
