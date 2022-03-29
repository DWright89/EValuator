import logo from './logo.svg';
import './App.css';
import React, { useState, useEffect } from 'react'
import {Router, Link} from 'react-router-dom'

import Index from "./components/Index.js"

function App() {
  const [cars, setCars] = useState([])

  const getAnything = async() =>{
    const messageOptions = {
      method: "GET",
      headers: {
        "Content-Type": "application/json"
      },
    }
    try{ const response = await fetch('http://localhost:8080/v1/cars', messageOptions)
      if (!response.ok) {
        console.log(response.headers)
        const errorMessage = `${response.status} (${response.statusText})`
        const error = new Error(errorMessage)
        throw (error)
      }
      const body = await response.json()
      setCars(body)
    }
    catch(error){
      console.error("Error ", error)
    }
  }

  useEffect(()=>{
    getAnything()
  }, [])

  const carList = cars.map((car) =>{
    return( <li>{car.make}</li>
    )
  })


  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <Router>
          <Link to="/index" component={Index}>Index </Link>
        </Router>
        <p>
          Edit <code>src/App.js</code> and save to reload.
         
        </p>
        <ul>
          {carList}
        </ul>
      
      </header>
    </div>
  );
}

export default App;
