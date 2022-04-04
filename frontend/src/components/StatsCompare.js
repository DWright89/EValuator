import React from 'react'
import {Box} from "@chakra-ui/react"

const StatsCompare = (props) =>{
  const {left, right, priceDifference} = props

  const intToMoney = (a, b) =>{
    return (a - b).toLocaleString('en-US', {
      style: 'currency',
      currency: 'USD',
    });
  }

  const cheaperCheck = ()=>{
    if(left.dollarPerHorsepower > right.dollarPerHorsepower ){
      return "Left is more"
    } else{
      return "Right is more"
    }
  }

  const determineHeading = () =>{
    if(priceDifference.includes('-')){
      return `Here's what spending ${priceDifference.replace('-', '')} less will do for you`
    } else{
      return `Here's what an extra ${priceDifference} will get you`
    }
  }

  const determineHorsepowerChange = () =>{
    if(left.stats.dollarPerHorsepower > right.stats.dollarPerHorsepower){
      const horsepowerDifference = intToMoney(left.stats.dollarPerHorsepower, right.stats.dollarPerHorsepower)
      return `You're spending ${horsepowerDifference} less per unit of horsepower`
    } else{
      const horsepowerDifference = intToMoney(right.stats.dollarPerHorsepower, left.stats.dollarPerHorsepower)
      return `You're spending ${horsepowerDifference} more per unit of horsepower`
    }
  }

  const determineTorqueChange = () =>{
    if(left.stats.dollarPerTorque > right.stats.dollarPerTorque){
      const torqueDifference = intToMoney(left.stats.dollarPerTorque, right.stats.dollarPerTorque)
      return `You're spending ${torqueDifference} less per lb-ft of torque`
    } else{
      const torqueDifference = intToMoney(right.stats.dollarPerTorque, left.stats.dollarPerTorque)
      return `You're spending ${torqueDifference} more per lb-ft of torque`
    }
  }

  const determineRangeChange = () =>{
    if(left.stats.dollarPerMile > right.stats.dollarPerMile){
      const rangeDifference = intToMoney(left.stats.dollarPerMile, right.stats.dollarPerMile)
      return `You're spending an extra ${rangeDifference} per mile of range`
    } else{
      const rangeDifference = intToMoney(right.stats.dollarPerMile, left.stats.dollarPerMile)
      return `It will cost an extra ${rangeDifference} per mile of range`
    }
  }

  const horsepowerValue = determineHorsepowerChange()
  const torqueValue = determineTorqueChange()
  const rangeValue = determineRangeChange()

  const heading = determineHeading()



  return(
    <Box>
      <p>{heading}</p>
      <p>{horsepowerValue}</p>
      <p>{torqueValue}</p>
      <p>{rangeValue}</p>
    </Box>
  )
}

export default StatsCompare