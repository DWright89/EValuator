import React from 'react'
import {Link} from 'react-router-dom'

const TopBar = (props) =>{

  return(<div className="topBar">
  
      <Link to="/compare">Compare</Link>
   
    <Link to="/index">Index?</Link>
  
    <Link to="/manufacturers">Manufacturers</Link>
  
    <Link to="/carform">Car Form</Link>
    
    <Link to ="/carshow">Car Show</Link>
 
  </div>

  )
}

export default TopBar