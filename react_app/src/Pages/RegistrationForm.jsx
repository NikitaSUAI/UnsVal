import React, { useState } from 'react';
import axios from 'axios';
import Config from '../config.js';
import { useNavigate } from 'react-router-dom';
import { setCookie } from '../Cook.js';
import "../Styles/styles.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faEye, faEyeSlash } from "@fortawesome/free-solid-svg-icons";
const RegistrationForm = () => {
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    let navigate = useNavigate();
    const [showPassword, setShowPassword] = useState(false);
    const [credentials, setCredentials] = useState({ username: "", email: "", password: "", confirmPassword: "" });
    const [errorMessage, setErrorMessage] = useState(null);

    const handleTogglePassword = () => {
        setShowPassword(!showPassword);
    };

    const handleChange = (event) => {
        const { name, value } = event.target;
        setCredentials(prevState => ({ ...prevState, [name]: value }));
        setErrorMessage(""); 
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
        handleRegistration(event);
    };

    const handleRegistration = async (event) => {
        event.preventDefault();
        const response = await fetch(Config.serverURL + 'api/registration/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                username: credentials.username,
                email: credentials.email,
                password: credentials.password
            }),
        });
        if (!response.ok) {
            const data = await response.json();
            setErrorMessage(JSON.stringify(data)); 
            return; 
        }
        const data = await response.json();
        // Successful registration
        setCookie('token', data.key, 7);
        navigate('/work');
    };


    return (
        <div id="login-form" style={{ display: 'flex', justifyContent: 'center', flexDirection: 'column' }}>
            <h1 style={{ textAlign: 'center' }}>Registration</h1>
            <form onSubmit={handleSubmit}>
                <label htmlFor="username">Username:</label>
                <input type="text" id="username" name="username" className="input-field" onChange={handleChange} />
                <label htmlFor="email">Email:</label>
                <input type="email" id="email" name="email" className="input-field" onChange={handleChange} />
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
                <input type="submit" value="Submit" onClick={handleSubmit} />
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

