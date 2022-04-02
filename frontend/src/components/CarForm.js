import React, { useState, useEffect } from 'react'
import { Link } from 'react-router-dom'

const CarForm = (props) => {
  const [manufacturer, setManufacturer] = useState('')
  const [car, setCar] = useState('')
  const [trim, setTrim] = useState('')
  const [isLoading, setIsLoading] = useState(true)
  const [isCarLoading, setIsCarLoading] = useState(true)
  //state for car
  //state for trim?

  const [fetchedManufacturers, setFetchedManufacturers] = useState([])
  const [fetchedCars, setFetchedCars] = useState([])
  const [fetchedTrims, setFetchedTrims] = useState([])

  //get all manufacturers, store in state
  //list of <options> of their .names
  //form with a <select>


  const handleManufChange = (event) => {
    console.log(event.currentTarget.value)
    setManufacturer(event.currentTarget.value)
  }

  const handleCarChange = (event) => {
    setCar(event.currentTarget.value)
  }

  const handleTrimChange = (event) => {
    setTrim(event.currentTarget.value)
  }

  const handleSubmit = (event) => {
    event.preventDefault()
    const oneCar = {manufacturer, car, trim}
    props.getCar(oneCar)
  }

  const manufOptions = fetchedManufacturers.map((manufacturer) => {
    return (
      <option key={manufacturer.id} value={manufacturer}>{manufacturer.name}</option>
    )
  })

  const carOptions = fetchedCars.map((car) => {
    return (
      <option key={car.id} value={car}>{car.model}</option>
    )
  })

  const trimOptions = fetchedTrims.map((trim) => {
    return (
      <option key={trim.id} value={trim}>{trim.trim}</option>
    )
  })

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
        setManufacturer(body[0])
      } catch (error) {
        console.error("Error in maunfacturer all ", error)
      }
    }
    getManufacturers()
  }, [])


  useEffect(() => {


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
          setCar(body[0])
        }

      } catch (error) {
        console.error("Error in get cars, ", error)
      }
    }

    getCars(manufacturer.name)
  }, [manufacturer])

  //this one gets trims!
  useEffect(() => {
    console.log("It's trying to get trims")
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
          setTrim(body[0])
        }
      } catch (error) {
        console.error("Error in trims: ", error)
      }
    }

    getTrims(manufacturer.name, car.model)
  }, [car])

  //make the form start with a default value of '-' LATER
  return (<div className="carForm">
    <form onSubmit={handleSubmit}>
      <label>Manufacturer:</label>
      <select onChange={handleManufChange}>
        {manufOptions}
      </select>
      <br />
      <label>Model:</label>
      <select onChange={handleCarChange}>
        {carOptions}
      </select>
      <br />
      <label>Trim:</label>
      <select onChange={handleTrimChange}>
        {trimOptions}
      </select>
      <button>Get me the car</button>
    </form>

    <Link to="/">Go Back</Link>
  </div>

  )
}

export default CarForm