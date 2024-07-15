import './App.css'
import Home from './components/Home';
import Trends from './components/Trends';
import Navbar from './components/Navbar'
import ReactDOM from "react-dom/client";
import { BrowserRouter, Routes, Route} from "react-router-dom";
import { useState } from 'react';
import Prod from './components/Prod';
import AdminLogin from './components/AdminLogin';
import Admin from './components/Admin';

function App() {
  const [prod, setProd] = useState()
  const [gender, setGender] = useState()
  

  return (
    <>
      <BrowserRouter>
      <Navbar  />

      <Routes>
        <Route path="/" element={<Home setGender={setGender} />}></Route>
        <Route path="/trends" element={<Trends setProd={setProd} gender={gender}/>}></Route>
        <Route path="/prod" element={<Prod prod={prod}/>}></Route>
        <Route path="/admin-login" element={<AdminLogin />}></Route>
        <Route path="/admin" element={<Admin />}></Route>
      </Routes>
    </BrowserRouter>

    </>
  )
}

export default App
