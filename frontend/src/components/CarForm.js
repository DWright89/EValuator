import React, { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'
import { Button } from '@chakra-ui/react'

const CarForm = (props) => {
  const [manufacturer, setManufacturer] = useState('')
  const [car, setCar] = useState('')
  const [trim, setTrim] = useState('')
  const [isLoading, setIsLoading] = useState(true)
  const [isCarLoading, setIsCarLoading] = useState(true)
  const [noCar, setNoCar] = useState(true)
  
  const [fetchedManufacturers, setFetchedManufacturers] = useState([])
  const [fetchedCars, setFetchedCars] = useState([])
  const [fetchedTrims, setFetchedTrims] = useState([])



  const handleManufChange = (event) => {
    setCar('')
    setFetchedCars([])
    setTrim('')
    setFetchedTrims([])
    const newManufacturer = fetchedManufacturers.filter((thing)=> thing.id == event.currentTarget.value)[0]
    setManufacturer(newManufacturer)
    getCars(newManufacturer.name)
  }

  const handleCarChange = (event) => {
    setTrim('')
    setFetchedTrims([])
    const newCar = fetchedCars.filter((car)=> car.id == event.currentTarget.value)[0]
    setCar(newCar)
    getTrims(manufacturer.name, newCar.model)
  }

  const handleTrimChange = (event) => {
    const newTrim = fetchedTrims.filter((trim)=> trim.id == event.currentTarget.value)[0]
    
    setTrim(newTrim)
  }
 
  const getStats = (price, horsepower, torque, range) =>{
    const dollarPerHorsepower = (price/horsepower).toFixed(2)
    const dollarPerTorque = (price/torque).toFixed(2)
    const dollarPerMile = (price/range).toFixed(2)
    return {dollarPerHorsepower, dollarPerTorque, dollarPerMile}
  }

  const handleSubmit = (event) => {
    event.preventDefault()
    if(manufacturer && car && trim){
      const stats = getStats(trim.price, trim.horsepower, trim.torque, trim.range)
      const oneCar = {manufacturer, car, trim, stats}
      props.getCar(oneCar)
    } 
  }

  const manufOptions = fetchedManufacturers.map((manufacturer) => {
    return (
      <option key={manufacturer.id} value={manufacturer.id}>{manufacturer.name}</option>
    )
  })

  const carOptions = fetchedCars.map((car) => {
    return (
      <option key={car.id} value={car.id}>{car.model}</option>
    )
  })

  const trimOptions = fetchedTrims.map((trim) => {
    return (
      <option key={trim.id} value={trim.id}>{trim.trim}</option>
    )
  })

  const getCars = async (manufacturer) => {
    try {
      if (isLoading === false) {
        console.log(manufacturer)
        console.log("isLoading: ", isLoading)
        const response = await fetch(`http://localhost:8080/v1/cars/${manufacturer}`)
        if (!response.ok) {
          const errorMessage = `${response.status} (${response.statusText})`
          const error = new Error(errorMessage)
          throw (error)
        }
        const body = await response.json()
        setFetchedCars(body)
        setIsCarLoading(false)
        //setCar(body[0])
        setTrim('')
      }

    } catch (error) {
      console.error("Error in get cars, ", error)
    }
  }

  const getTrims = async (make, model) => {
    try {
      if (isCarLoading === false) {
        console.log("isCarLoading: ", isCarLoading)
        const response = await fetch(`http://localhost:8080/v1/trims/${make}/${model}`)
        if (!response.ok) {
          const errorMessage = `${response.status} (${response.statusText})`
          const error = new Error(errorMessage)
          throw (error)
        }
        const body = await response.json()
        setFetchedTrims(body)
        //setTrim(body[0])
      }
    } catch (error) {
      console.error("Error in trims: ", error)
    }
  }

  //this should be useRef
  useEffect(() => {
    const getManufacturers = async () => {
      try {
        const response = await fetch("http://localhost:8080/v1/manufacturers")
        if (!response.ok) {
          console.log(response.headers)
          const errorMessage = `${response.status} (${response.statusText})`
          const error = new Error(errorMessage)
          throw (error)
        }
        const body = await response.json()

        setFetchedManufacturers(body)
        setIsLoading(false)
        //setManufacturer(body[0])
      } catch (error) {
        console.error("Error in maunfacturer all ", error)
      }
    }
    getManufacturers()
    
  }, [])


  return (<div className="carForm">
    <form>
      <label>Manufacturer:</label>
      <select onChange={handleManufChange} defaultValue="-">
        <option>Select Manufacturer</option>
        {manufOptions}
      </select>
      <br />
      <label>Model:</label>
      <select onChange={handleCarChange} defaultValue="-">
        <option>Select Car</option>
        {carOptions}
      </select>
      <br />
      <label>Trim:</label>
      <select onChange={handleTrimChange}>
        <option>Select Trim</option>
        {trimOptions}
      </select>
      <br/>
      <Button size='sm' onClick={handleSubmit}>Get me the car</Button>
    </form>

    <Link to="/">Go Back</Link>
  </div>

  )
}

export default CarForm