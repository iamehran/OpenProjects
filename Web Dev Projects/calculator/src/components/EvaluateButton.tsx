import React from 'react'


interface EvaluateButtonProps{
    equalDigit: string;
    className?: string;
    handleEvaluation:()=>void;


}

const  EvaluateButton = ({equalDigit ,className ,handleEvaluation}:EvaluateButtonProps) =>  {
  return (
    <button className={className} onClick={() => { handleEvaluation()} }>
      {equalDigit}
    </button>
  )
}

export default EvaluateButton