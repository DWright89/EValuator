import React, { useState, useEffect } from 'react'
import {
  Table,
  Thead,
  Tbody,
  Tfoot,
  Tr,
  Th,
  Td,
  TableCaption,
  TableContainer,
} from '@chakra-ui/react'


import TableButtons from './TableButtons'

const CarTable = (props) =>{
  const [cars, setCars] = useState([])
  const [sortOrder, setSortOrder] = useState({stat: "price", direction: true})



const generateTable = () =>{
  const stat = sortOrder.stat
  const sortedCars = cars.sort((a, b)=>{
    if(sortOrder.direction){
      return (b.trim[stat] - a.trim[stat])
    } 
    return (a.trim[stat] - b.trim[stat])
  })
  const tableRows = sortedCars.map((car, index)=>{
    return <Tr key={index}>
      <Td>{car.manufacturer.name} {car.model.model} {car.trim.trim}</Td>
      <Td isNumeric>${car.trim.price}</Td>
      <Td isNumeric>{car.trim.range}</Td>
      <Td isNumeric>{car.trim.horsepower}</Td>
      <Td isNumeric>{car.trim.torque}</Td>
      <Td isNumeric>{car.trim.kwh}</Td>
      <Td isNumeric>{car.trim.kwh100mi}</Td>
      <Td isNumeric>${car.trim.dollars_per_horsepower}</Td>
      <Td isNumeric>${car.trim.dollars_per_torque}</Td>
      <Td isNumeric>${car.trim.dollars_per_mile}</Td>
    </Tr>
  })
  return tableRows
}

  const tableRows = generateTable()
  const handleClick = (event) =>{
    setSortOrder({stat: event.currentTarget.name, direction: Boolean(event.currentTarget.value === 'true')})
  }

 
  useEffect(()=>{

    const getEveryCar = async () =>{
      try{
        const response = await fetch('http://localhost:8080/v1/trims')
        if (!response.ok) {
          const errorMessage = `${response.status} (${response.statusText})`
          const error = new Error(errorMessage)
          throw (error)
        }
        const body = await response.json()
        const newBody = body.map((car)=>{
          car.trim.dollars_per_horsepower = (car.trim.price / car.trim.horsepower).toFixed(2)
          car.trim.dollars_per_torque = (car.trim.price / car.trim.torque).toFixed(2)
          car.trim.dollars_per_mile = (car.trim.price / car.trim.range).toFixed(2)
          return car
        })
        setCars(newBody)
      }catch(error){
        console.error("Error in fetch: ", error)
      }
    }

    getEveryCar()
  }, [])



  return(
    <TableContainer>
    <Table variant='simple' size='sm'>
      <TableCaption>Imperial to metric conversion factors</TableCaption>
      <Thead>
        <Tr>
          <Th>Vehicle</Th>
          <Th isNumeric>Price <TableButtons handleClick={handleClick} name={'price'} /></Th>
          <Th isNumeric>Range <TableButtons handleClick={handleClick} name={'range'}/></Th>
          <Th isNumeric>HP <TableButtons handleClick={handleClick} name={'horsepower'}/></Th>
          <Th isNumeric>TQ<TableButtons handleClick={handleClick} name={'torque'}/></Th>
          <Th isNumeric>kw/h<TableButtons handleClick={handleClick} name={'kwh'}/></Th>
          <Th isNumeric>kw/h / 100mi <TableButtons handleClick={handleClick} name={'kwh100mi'}/></Th>
          <Th isNumeric>$/hp <TableButtons handleClick={handleClick} name={'dollars_per_horsepower'}/></Th>
          <Th isNumeric>$/torque <TableButtons handleClick={handleClick} name={'dollars_per_torque'}/></Th>
          <Th isNumeric>$/mile <TableButtons handleClick={handleClick} name={'dollars_per_mile'}/></Th>
        </Tr>
      </Thead>
      <Tbody>
        {tableRows}
      </Tbody>
      <Tfoot>
      <Tr>
          <Th>Vehicle</Th>
          <Th isNumeric>Price <TableButtons handleClick={handleClick} name={'price'} /></Th>
          <Th isNumeric>Range <TableButtons handleClick={handleClick} name={'range'}/></Th>
          <Th isNumeric>HP <TableButtons handleClick={handleClick} name={'horsepower'}/></Th>
          <Th isNumeric>TQ<TableButtons handleClick={handleClick} name={'torque'}/></Th>
          <Th isNumeric>kw/h<TableButtons handleClick={handleClick} name={'kwh'}/></Th>
          <Th isNumeric>kw/h / 100mi <TableButtons handleClick={handleClick} name={'kwh100mi'}/></Th>
          <Th isNumeric>$/hp <TableButtons handleClick={handleClick} name={'dollars_per_horsepower'}/></Th>
          <Th isNumeric>$/torque <TableButtons handleClick={handleClick} name={'dollars_per_torque'}/></Th>
          <Th isNumeric>$/mile <TableButtons handleClick={handleClick} name={'dollars_per_mile'}/></Th>
        </Tr>
      </Tfoot>
    </Table>
  </TableContainer>
  )
}

export default CarTable
