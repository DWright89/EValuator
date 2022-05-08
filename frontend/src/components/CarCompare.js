import React, {useState} from 'react'

import CarShow from "./CarShow.js"
import ComparisonWrapper from "./ComparisonWrapper.js"

const CarCompare = (props) =>{
  const [leftCar, setLeftCar] = useState(false)
  const [rightCar, setRightCar] = useState(false)

  const bothCars = Boolean(leftCar && rightCar)

  return(<>
    <div className="leftCar">
      <CarShow setCar={setLeftCar}/>
    </div>
    <div className="comparison">
      <ComparisonWrapper 
      ready={bothCars}
      left={leftCar}
      right={rightCar}/>
    </div>
    <div className="rightCar">
      <CarShow setCar={setRightCar}/>
    </div>
  </>
   
  )
}

export default CarCompare