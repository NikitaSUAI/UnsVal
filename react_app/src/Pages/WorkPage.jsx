import React, { useState } from 'react';
import axios from 'axios';
import Config from '../config.js';
import "../Styles/styles.css";

const AnswerForm = () => {
  const [userid, setUserid] = useState("");
  const [line, setLine] = useState("");
  const [result, setResult] = useState("");

  const handleInputChange = (event) => {
    setLine(event.target.value);
  };

  const handleLogout = () => {
    document.cookie = 'token=; Max-Age=-99999999;'; // Удаляем токен из куки
    console.log("Token removed from the cookie. Logging out...");
  };

  const handleSubmit = async () => {
    const requestBody = {
      userid: "СЮДА ВАШ АЙДИШНИК",
      line: line
    };

    try {
      const response = await fetch(Config.serverURL + 'api/answer/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(requestBody)
      });
      const data = await response.json();
      setResult(JSON.stringify(data)); // Отображение результата запроса
    } catch (error) {

      setResult('Ошибка при отправке запроса');
    }
  };

  return (
    <div>
      <header class="p-3 bg-primary text-white">
        <div class="container">
          <div class="d-flex flex-wrap align-items- justify-content-end justify-content-lg-start"> 
            <div className="text-end">
              <a href="/" className="btn btn-outline-light" onClick={handleLogout}> Logout </a> 
            </div>

          </div>
        </div>
      </header>
      <main style={{ display: "flex", flexDirection: "column", alignItems: "center", marginTop: "2em" }}>
        <div className="mb-3" style={{ width: "40%" }}>
          <textarea type="text" className="form-control" value={line} onChange={handleInputChange} />
        </div>
        <div className="mb-3">
          <button onClick={handleSubmit} className="btn btn-primary">Отправить</button>
        </div>
        <div className="mb-3">
          <textarea value={result} readOnly className="form-control" rows="3" />
        </div>
      </main>
    </div>
  );
};

export default AnswerForm;
