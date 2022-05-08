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


  const determineHeading = () =>{
    if(priceDifference.includes('-')){
      return `Here's what spending ${priceDifference.replace('-', '')} less will do for you`
    } else{
      return `Here's what an extra ${priceDifference} will get you`
    }
  }

  const determineHorsepowerChange = () =>{
    if(left.trim.dollars_per_horsepower > right.trim.dollars_per_horsepower){
      const horsepowerDifference = intToMoney(left.trim.dollars_per_horsepower, right.trim.dollars_per_horsepower)
      return `You're spending ${horsepowerDifference} less per unit of horsepower`
    } else{
      const horsepowerDifference = intToMoney(right.trim.dollars_per_horsepower, left.trim.dollars_per_horsepower)
      return `You're spending ${horsepowerDifference} more per unit of horsepower`
    }
  }

  const determineTorqueChange = () =>{
    if(left.trim.dollars_per_torque > right.trim.dollars_per_torque){
      const torqueDifference = intToMoney(left.trim.dollars_per_torque, right.trim.dollars_per_torque)
      return `You're spending ${torqueDifference} less per lb-ft of torque`
    } else{
      const torqueDifference = intToMoney(right.trim.dollars_per_torque, left.trim.dollars_per_torque)
      return `You're spending ${torqueDifference} more per lb-ft of torque`
    }
  }

  const determineRangeChange = () =>{
    if(left.trim.dollars_per_mile > right.trim.dollars_per_mile){
      const rangeDifference = intToMoney(left.trim.dollars_per_mile, right.trim.dollars_per_mile)
      return `You're spending ${rangeDifference} less per mile of range`
    } else{
      const rangeDifference = intToMoney(right.trim.dollars_per_mile, left.trim.dollars_per_mile)
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