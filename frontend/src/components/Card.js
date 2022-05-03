import React from 'react'
import { Box, Divider } from "@chakra-ui/react"

import apiURL from "../constants/imagePath"

const Card = (props)=>{
  const {manufacturer, car, trim, stats} = props.car
  const price = (trim.price).toLocaleString('en-US', {
    style: 'currency',
    currency: 'USD',
  });

  const finalDrive = ()=>{
    if(trim.rwd){
      return 'RWD'
    }
    if(trim.fwd){
      return 'FWD'
    }
    if(trim.awd){
      return 'AWD'
    }
  }

  return(
    <Box className="card" maxW='sm' borderRadius='lg'
          bg='#5b6170'  p={4} color='white' >
        <h3>{manufacturer.name} {car.model} {trim.trim}</h3>
        <img src={`${apiURL}/static/images/${car.image}`} alt="A Car"></img>
        <br />
        {price}
        <Divider/>
        <p>Battery Capacity - {trim.kwh}KW/H</p>
        <p>Range - {trim.range}mi</p>
        <p>Drive - {finalDrive()}</p>
        <p>0-60 - {trim.acceleration} sec</p>
        <p>Horsepower - {trim.horsepower}</p>
        <p>Torque - {trim.torque} ft-lbs</p>
        <p>Weight - {trim.weight} lbs</p>
        <p>MPGe - {trim.mpge}</p>
        <p>KW/h:100mi - {trim.kwh100mi}</p>
        <p>Cargo Capacity - {car.cargo} cu-ft</p>
        <Divider/>
        <p>${stats.dollarPerHorsepower}/Horsepower</p>
        <p>${stats.dollarPerTorque}/Lb-ft torque</p>
        <p>${stats.dollarPerMile}/Mile of range</p>
        
    </Box>
  )
}

export default Card