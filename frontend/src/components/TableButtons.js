import React, { useState, useEffect } from 'react'
import { IconButton, HStack } from '@chakra-ui/react'

import {TriangleUpIcon, TriangleDownIcon} from '@chakra-ui/icons'

const TableButtons = (props)=>{
  const { name, handleClick } = props
  return(<>
    <IconButton backgroundColor='#282c34' name={name}  value="true" variant='unstyled' size='xs' color="green.500" onClick={handleClick} icon={<TriangleUpIcon />}></IconButton>
    <IconButton backgroundColor='#282c34' name={name} value="false" variant='unstyled' size='xs' color="red.500" onClick={handleClick} icon={<TriangleDownIcon />}></IconButton>
    </>
  )
}

export default TableButtons