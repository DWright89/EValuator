import React from 'react'
import {Link} from 'react-router-dom'
import { Button } from '@chakra-ui/react'



const TopBar = (props) =>{

  const compare = <Button size="s"> 
                    <Link to="/compare">Compare two cars</Link>
                  </Button>

const show = <Button size="s"> 
              <Link to="/carshow">Check out one car</Link>
              </Button>

  return(<div className="topBar">
    {compare}
    {show}
  </div>

  )
}

export default TopBar