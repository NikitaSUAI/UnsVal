import React, { useState } from "react";
import "../Styles/styles.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faEye, faEyeSlash } from "@fortawesome/free-solid-svg-icons";

const AuthForm = () => {
  const [showPassword, setShowPassword] = useState(false);

  const handleTogglePassword = () => {
    setShowPassword(!showPassword);
  };

  return (
    <div id="login-form">
      <h1>Login</h1>
      <form>
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
      </form>
    </div>
  );
};

export default AuthForm;
