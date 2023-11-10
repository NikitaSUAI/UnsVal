import React, { useState } from "react";
import "../Styles/styles.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faEye, faEyeSlash } from "@fortawesome/free-solid-svg-icons";

const RegistrationForm = () => {
    const [showPassword, setShowPassword] = useState(false);
    const [credentials, setCredentials] = useState({ username: "", email: "", password: "", confirmPassword: "" });
    const [errorMessage, setErrorMessage] = useState("");

    const handleTogglePassword = () => {
        setShowPassword(!showPassword);
    };

    const handleChange = (event) => {
        const { name, value } = event.target;
        setCredentials(prevState => ({ ...prevState, [name]: value }));
        setErrorMessage(""); // clear error message when changes occur
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        if (credentials.password !== credentials.confirmPassword) {
            setErrorMessage("Passwords don't match!");
            return;
        }
        if (credentials.password.length < 6) {
            setErrorMessage("Password must be at least 6 characters long!");
            return;
        }
        //Process the registration on server
        console.log(credentials);
    };

    return (
        <div id="login-form" style={{ display: 'flex', justifyContent: 'center', flexDirection: 'column' }}>
            <h1 style={{ textAlign: 'center' }}>Registration</h1>
            <form onSubmit={handleSubmit}>
                <label htmlFor="username">Username:</label>
                <input type="text" id="username" name="username" className="input-field" onChange={handleChange} />

                <label htmlFor="email">Email:</label>
                <input type="email" id="email" name="email" className="input-field" onChxange={handleChange} />


                <label htmlFor="password">Password:</label>
                <div className="password-input">
                    <input
                        type={showPassword ? "text" : "password"}
                        id="password"
                        name="password"
                        className="input-field"
                        onChange={handleChange}
                    />
                    <button type="button" onClick={handleTogglePassword}>
                        {showPassword ? (
                            <FontAwesomeIcon icon={faEyeSlash} />
                        ) : (
                            <FontAwesomeIcon icon={faEye} />
                        )}
                    </button>
                </div>
                <label htmlFor="confirmPassword">Confirm Password:</label>
                <div className="password-input">
                    <input
                        type={showPassword ? "text" : "password"}
                        id="confirmPassword"
                        name="confirmPassword"
                        className="input-field"
                        onChange={handleChange}
                    />
                    <button type="button" onClick={handleTogglePassword}>
                        {showPassword ? (
                            <FontAwesomeIcon icon={faEyeSlash} />
                        ) : (
                            <FontAwesomeIcon icon={faEye} />
                        )}
                    </button>
                </div>

                <p className="error-message" style={{ color: 'red' }}>{errorMessage}</p>

                <input type="submit" value="Submit" />

                <br></br><br></br>
                <p className="login-link" style={{ textAlign: 'center' }}>
                    Already part of our platform?
                    <a href="/">Login to your account</a>
                </p>
            </form>
        </div>
    );
};

export default RegistrationForm;
