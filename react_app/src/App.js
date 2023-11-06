import logo from './logo.svg';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import AuthForm from './Pages/AuthForm';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<AuthForm />} />
        
      </Routes>
    </Router>
  );
}

export default App;
