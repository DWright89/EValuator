import logo from './logo.svg';
import './App.css';
import React, { useState, useEffect } from 'react'
import {Routes, Route, Link } from "react-router-dom";
import { ChakraProvider } from '@chakra-ui/react'

import Index from "./components/Index.js"
import TopBar from "./components/TopBar.js"
import ManufacturerList from './components/ManufacturerList.js';
import CarForm from "./components/CarForm.js"
import CarShow from "./components/CarShow.js"
import CarCompare from "./components/CarCompare.js"
import LandingPage from './components/LandingPage';
import CarTable from './components/CarTable'

function App() {
 

  

  return (
    <ChakraProvider>

      
      <div className="App">
          <TopBar />
        <header className="App-header">
        
          <Routes>
              <Route exact path="/" element={<LandingPage />} />
              <Route exact path="/index" element={<Index />}/>
              <Route exact path="/manufacturers" element={<ManufacturerList />} />
              <Route exact path="/carform" element={<CarForm />} />
              <Route exact path="/carshow" element={<CarShow />} />
              <Route exact path="/compare" element={<CarCompare />} />
              <Route exact path="/table" element={<CarTable />} />
          </Routes>
        
         
        
        
        
        </header>
      </div>
    </ChakraProvider>
  );
}

export default App;
