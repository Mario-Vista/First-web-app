import { useEffect, useState } from "react";
import Homepage from "./Homepage";
import "./App.css";

/**
 * Login component handles both user login and registration.
 * 
 * Props:
 * - user: object containing {username, password, success, validate}
 * - setUser: state setter function to update the user object
 */
export default function Login({ user, setUser }) {

  // Example useEffect commented out: could log user success state on change
  // useEffect(() => { console.log("success: ", user.success) }, [user.success])

  /**
   * Handles login requests.
   * Sends username and password to the backend POST /login endpoint.
   * Updates the user state based on backend response.
   */
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

    // Update the user state with the response from backend
    setUser((prev) => ({
      ...prev,
      username: data.username,
      password: undefined, // Do not store password in state after login
      success: data.success,
      validate: data.validate
    }));
  };

  /**
   * Handles user registration requests.
   * Sends username and password to the backend POST /signup endpoint.
   * Updates the user state based on backend response.
   */
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

    // Update the user state with the response from backend
    setUser((prev) => ({
      ...prev,
      username: data.username,
      password: undefined, // Clear password for security
      success: data.success,
      validate: data.validate
    }));
  };

  return (
    <>
      {/* If user is not logged in, show login form */}
      {!user.success && (
        <div className="login-container">
          <h2 className="login-title">MyApp</h2>

          {/* Username input field */}
          <div className="login-field">
            <label htmlFor="username">Username</label>
            <input
              id="username"
              type="text"
              placeholder="Enter username"
              onChange={(event) => {
                setUser((prev) => ({ ...prev, username: event.target.value }));
              }}
            />
          </div>

          {/* Password input field */}
          <div className="login-field">
            <label htmlFor="password">Password</label>
            <input
              id="password"
              type="password"
              placeholder="Enter password"
              onChange={(event) => {
                setUser((prev) => ({ ...prev, password: event.target.value }));
              }}
            />
          </div>

          {/* Login button triggers handleLogin */}
          <button className="login-button" onClick={handleLogin}>
            Login
          </button>

          {/* Sign up button triggers handleRegister */}
          <button className="login-button" onClick={handleRegister}>
            Sign up
          </button>

          {/* Display error message if credentials are invalid */}
          {!user.validate && (
            <div className="login-error">Invalid credentials</div>
          )}
        </div>
      )}
    </>
  );
}
