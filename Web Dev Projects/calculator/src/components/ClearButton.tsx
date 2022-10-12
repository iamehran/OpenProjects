import React from 'react'

interface ClearButtonProps{
   handleClearDigit:()=> void;
   className?: any; 
   digit: string;
}

const ClearButton = ({handleClearDigit ,className ,digit}:ClearButtonProps) =>  {
  return (
    <button className={`${className} btn--span-two`} onClick={() => { handleClearDigit()} }>
    {digit}
  </button>
  )
}

export default ClearButton