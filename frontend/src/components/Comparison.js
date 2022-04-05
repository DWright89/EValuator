import React from 'react'
import {Box} from '@chakra-ui/react'
import {ArrowRightIcon} from '@chakra-ui/icons'

import StatsCompare from "./StatsCompare.js"

const Comparison = (props) =>{
  const {left, right} = props




const iconManager = (value) =>{
  if(value > 0){
    if(value < 50){
      return <ArrowRightIcon color="yellow.500" />
    }if(value > 50 && value < 100){
      return <ArrowRightIcon color="orange.500" />
    }if(value > 100){
      return <ArrowRightIcon color="red.500" />
    }
  }
  if(value < 0){
    if(value > -50){
      return <ArrowRightIcon color="green.100" />
    }if(value < -50 && value > -100){
      return <ArrowRightIcon color="green.300" />
    }if(value < -100){
      return <ArrowRightIcon color="green.500" />
    }
  }
}

  const priceDifference = (right.trim.price / left.trim.price *100 - 100).toFixed(2)
  const priceIcon = iconManager(parseInt(priceDifference))

  const priceDifferenceDollars = (right.trim.price - left.trim.price).toLocaleString('en-US', {
    style: 'currency',
    currency: 'USD',
  });



  const batteryDifference = (right.trim.kwh / left.trim.kwh * 100 - 100).toFixed(2)
  const batteryIcon = iconManager((parseInt(batteryDifference)) *-1)

  const rangeDifference = (right.trim.range / left.trim.range * 100 - 100).toFixed(2)
  const rangeIcon = iconManager((parseInt(rangeDifference)) *-1)

  const accelerationDifference = (right.trim.acceleration / left.trim.acceleration * 100 - 100).toFixed(2)
  const accelerationIcon = iconManager(parseInt(accelerationDifference))

  const horsepowerDifference = (right.trim.horsepower / left.trim.horsepower * 100 - 100).toFixed(2)
  const horsepowerIcon = iconManager((parseInt(horsepowerDifference) *-1))

  const torqueDifference = (right.trim.torque / left.trim.torque * 100 - 100).toFixed(2)
  const torqueIcon = iconManager((parseInt(torqueDifference)) *-1)

  const weightDifferenceInt = right.trim.weight - left.trim.weight
  const weightDifference = (right.trim.weight / left.trim.weight * 100 - 100).toFixed(2)
  const weightIcon = iconManager(weightDifferenceInt)


  const mpgeDifference = (right.trim.mpge / left.trim.mpge * 100 - 100).toFixed(2)
  const mpgeIcon = iconManager(parseInt(mpgeDifference) *-1)

  const kwh100miDifference = (right.trim.kwh100mi / left.trim.kwh100mi * 100 - 100).toFixed(2)
  const kwh100miIcon = iconManager(parseInt(kwh100miDifference))
  //NOW DO THE SAME FOR MPGE AND KWH100MI


  return(
    <Box className="card" maxW='m'  borderRadius='lg'
    bg='#5b6170'  p={4} color='white'>
      <h4>
        All comparisons are from left to right
      </h4>
      <p>
        {priceIcon}
        Price: {priceDifference}% ({priceDifferenceDollars})
        {priceIcon}
      </p>
      <p>
        {batteryIcon}
      Battery: {batteryDifference}%
      {batteryIcon}
      </p>
      <p>
        {rangeIcon}
        Range: {rangeDifference}%
        {rangeIcon}
      </p>
      <p>
        {accelerationIcon}
        0-60: {accelerationDifference}%
        {accelerationIcon}
      </p>
      <p>
        {horsepowerIcon}
        Horsepower: {horsepowerDifference}%
        {horsepowerIcon}
      </p>
      <p>
        {torqueIcon}
        Torque: {torqueDifference}%
        {torqueIcon}
      </p>
      <p>
        {weightIcon}
        Weight: {weightDifference} ({weightDifferenceInt}lbs)
        {weightIcon}
      </p>
      <p>
        {mpgeIcon}
        MPGe: {mpgeDifference}%
        {mpgeIcon}
      </p>
      <p>
        {kwh100miIcon}
        KW/h/100mi: {kwh100miDifference}%
        {kwh100miIcon}

      </p>
      
      <StatsCompare left={left} right={right} priceDifference={priceDifferenceDollars}/>
    </Box>
  )
}

export default Comparison