import React, { useState } from 'react'

import CarForm from "./CarForm.js"
import Card from "./Card.js"

const CarShow = (props) =>{
  const [car, setCar] = useState(false)
  const [isSubmitted, setIsSubmitted] = useState(false)

  
  const getCar = (oneCar) =>{
    setCar(oneCar)
    setIsSubmitted(true)
    props.setCar(oneCar)
  }
  return(<>
  <CarForm getCar={getCar}/>
  {isSubmitted && <Card car={car}/>}
  
  </>
  )
}

export default CarShow