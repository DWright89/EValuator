import React, {useState} from 'react'
import {Box, Button } from '@chakra-ui/react'

import Comparison from "./Comparison.js"

const ComparisonWrapper = (props) =>{
  const [clicked, setClicked] = useState(false)

  const testButton = () => setClicked(true)
  const button = (<Button size="s" onClick={testButton}>This is going to be the button</Button>)
  const notReady = <p>Select two cars to compare them</p>
  

 

  return(<>
    {props.ready? button : notReady}
    {clicked?  <Comparison left={props.left} right={props.right}/> : ''}
  </>
    
  )
}

export default ComparisonWrapper