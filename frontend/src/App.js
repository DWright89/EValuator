import logo from './logo.svg';
import './App.css';
import React, { useState, useEffect } from 'react'
import {Routes, Route, Link } from "react-router-dom";

import Index from "./components/Index.js"
import ManufacturerList from './components/ManufacturerList.js';
import CarForm from "./components/CarForm.js"
import CarShow from "./components/CarShow.js"

function App() {
 

  

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
      
         <Routes>
            <Route exact path="/index" element={<Index />}/>
            <Route exact path="/manufacturers" element={<ManufacturerList />} />
            <Route exact path="/carform" element={<CarForm />} />
            <Route exact path="/carshow" element={<CarShow />} />
         </Routes>
       
     
        <p>
         <Link to="/index">Index?</Link>
        </p>
        <p>
         <Link to="/manufacturers">Manufacturers</Link>
        </p>
        <p>
          <Link to="/carform">Car Form</Link>
        </p>
        <p>
          <Link to ="/carshow">Car Show</Link>
        </p>
       
       
      
      </header>
    </div>
  );
}

export default App;
