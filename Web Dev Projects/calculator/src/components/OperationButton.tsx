import React from 'react'

interface OperationButtonProps {

    className?: string; 
    operation: string;
    handleChooseOperation?:(pressedOperation:string)=>void


}

const OperationButton = ({className , operation ,handleChooseOperation}:OperationButtonProps)=> {
  return (
    <button className={className} onClick={() => { handleChooseOperation?.(operation) } }>
    {operation}
  </button>
  )
}

export default OperationButton