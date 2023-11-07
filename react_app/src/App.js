import logo from './logo.svg';
import 'bootstrap/dist/css/bootstrap.min.css';
import './App.css';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import AuthForm from './Pages/AuthForm';
import RegistrationForm from './Pages/RegistrationForm';
import NotFoundPage from './Pages/NotFoundPage';
import WorkPage from './Pages/WorkPage';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<AuthForm />} />
        <Route path="/registration" element={<RegistrationForm />} />
        <Route path="/work" element={<WorkPage />} />
        <Route path="*" element={<NotFoundPage />} />
      </Routes>
    </Router>
  );
}

export default App;
