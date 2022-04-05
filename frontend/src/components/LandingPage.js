import React from 'react'
import {Link} from 'react-router-dom'
import {Button} from '@chakra-ui/react'


const LandingPage = (props) =>{

  const evaluator = <Button size="md">
                      <Link to="/compare">Go EValuate some cars</Link>
                    </Button>

  return(<div className="landing">
    <h1>Welcome to EZ-EV</h1>
    <br />
    <p>Where all your dreams of comparing electric vehicles can come true.</p>
    {evaluator}
  </div>

  )
}

export default LandingPage