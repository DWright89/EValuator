import React from 'react'

import CarForm from "./CarForm.js"
import Card from "./Card.js"

const CarShow = (props) =>{

    const getCar = (oneCar) =>{
      console.log("Now it's up here")
      console.log(oneCar)
    }
  return(
    <CarForm getCar={getCar}/>
  )
}

export default CarShow