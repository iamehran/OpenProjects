import React from 'react'

interface RemoveLastDigitButtonProps{

    handleRemoveLastDigit: ()=>void;
    className?: string; 
   digit: string;

}
const RemoveLastDigitButton = ({handleRemoveLastDigit ,className ,digit}:RemoveLastDigitButtonProps) => {
  return (
    <button className={className} onClick={() => {handleRemoveLastDigit() } }>
    {digit}
  </button>
   
  )
}

export default RemoveLastDigitButton