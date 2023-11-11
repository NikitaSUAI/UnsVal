import React, { useState } from "react";
import "../Styles/styles.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faEye, faEyeSlash } from "@fortawesome/free-solid-svg-icons";
import Config from '../config.js';
import { useNavigate } from 'react-router-dom';
import { setCookie } from '../Cook.js';
const AuthForm = () => {
  const [showPassword, setShowPassword] = useState(false);
  const [error, setError] = useState("");
  let navigate = useNavigate();
  // Сохраняем в куки токен нашего пользователя 
  const handleTogglePassword = () => {
    setShowPassword(!showPassword);
  };

  const handleFormSubmit = async (event) => {
    event.preventDefault();
    const username = event.target.username.value;
    const password = event.target.password.value;
    const response = await fetch(Config.serverURL + 'api/login/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        username: username,
        password: password
      }),
    });

    const data = await response.json();
    if (response.ok) {
      setCookie('token', data.key, 7);

      navigate('/work');
    } else {
      // Handle error response
      setError("Failed to log in. Please check your credentials.");
      console.error('Error:', data);
    }
  };

  return (
    <div id="login-form">
      <h1>Login</h1>
      <form onSubmit={handleFormSubmit}>
        <label htmlFor="username">Username:</label>
        <input type="text" id="username" name="username" className="input-field" />
        <label htmlFor="password">Password:</label>
        <div className="password-input">
          <input
            type={showPassword ? "text" : "password"}
            id="password"
            name="password"
            className="input-field"
          />
          <button type="button" onClick={handleTogglePassword}>
            {showPassword ? (
              <FontAwesomeIcon icon={faEyeSlash} />
            ) : (
              <FontAwesomeIcon icon={faEye} />
            )}
          </button>
        </div>
        <input type="submit" value="Submit" />

        <br></br><br></br>
        <p className="signup-link">
          New on our platform?
          <a href="/registration">Create an account</a>  {/* Замените # на ссылку на регистрацию */}
        </p>
        {error && <p style={{ color: 'red' }}>{error}</p>} {/* Display error message */}
      </form>
    </div>
  );
};

export default AuthForm;
