import React, {useState, useEffect} from 'react'
import {Link} from 'react-router-dom'


//import Manufacturer from '../../models/manufacturer.js'

const ManufacturerList = (props) =>{
const [manufacturers, setManufacturers] = useState([])

  const getManufacturers = async()=>{
    try{ const response = await fetch("http://localhost:8080/v1/manufacturers")
    if (!response.ok) {
      console.log(response.headers)
      const errorMessage = `${response.status} (${response.statusText})`
      const error = new Error(errorMessage)
      throw (error)
    }
      const body = await response.json()
      console.log(body)
      setManufacturers(body)
    }catch(error){
      console.error("Error in maunfacturer all ", error)
    }
  }

  const manufacturerList = manufacturers.map((manuf) =>{
    return (
      <>
        <li key={manuf.id}>
          {manuf.name}
        </li>
      </>
    )
  })

  useEffect(()=>{
    getManufacturers()
  }, [])

  return ( <>
  <p>Manuf list</p>
  <ul>
    {manufacturerList}
  </ul>
  <Link to="/">Go Back</Link>
  </>
  )
}

export default ManufacturerList