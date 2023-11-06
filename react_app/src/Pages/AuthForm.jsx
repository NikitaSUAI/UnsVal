import React, { useState } from 'react';
import { Form, Button } from 'react-bootstrap';

const AuthForm = () => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [isRegistering, setIsRegistering] = useState(false);

 const handleSubmit = (e) => {
    e.preventDefault();
    // Дополнительная логикаработки отправки формы
  };

  return (
    <Form onSubmit={handleSubmit}>
      <Form.Group controlId="formEmail">
        <Form.Label>Email</Form.Label>
        <Form.Control 
          name="email"
          placeholder="Введите ваш email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />
      </Form.Group>

      <Form.Group controlId="formPassword">
        <Form.Label>Пароль</Form.Label>
       <Form.Control
          type="password"
          placeholder="Введите ваш пароль"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
        />
      </Form.Group>

      {!isRegistering && (
        <Button variant="primary" type="submit">
          Войти
        </Button>
      )}

      {isRegistering && (
        <Button variant="primary" type="submit">
          Зарегистрироваться
        </Button>
      )}

      <Button
        variant="link"
        onClick={() => setIsRegistering(!isRegistering)}
      >
        {isRegistering ? 'Уже есть аккаунт? Войти' : 'Ещё не зарегистрированы?'}
      </Button>
    </Form>
  );
};

export default AuthForm;
