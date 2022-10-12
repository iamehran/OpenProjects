import React from "react";
import "./styles.css";

// imports related to redux toolkit and state managemet
import { useDispatch, useSelector } from "react-redux";
import { RootState } from "./store";
import {
  addDigit,
  chooseOperation,
  clearDigit,
  performEvaluation,
  removeLastDigit,
} from "./store/features/digitSlice";

//Components Button
import Button from "./components/Button";
import ClearButton from "./components/ClearButton";
import RemoveLastDigitButton from "./components/RemoveLastDigitButton";
import OperationButton from "./components/OperationButton";
import EvaluateButton from "./components/EvaluateButton";

//utility function
import {formatStringtoNumberWithComma} from "./utils/digitFormater"


function App() {
 
   //digit State
  const digits = useSelector((state: RootState) => state.digits);

  const themeState = useSelector((state:RootState)=> state.theme)

  const dispatch = useDispatch();

  console.log("prevoperand", digits.currentOperand)

 
   //Event handler
  const handleAddDigits = (pressedDigit: string) => {
    dispatch(addDigit(pressedDigit));
    
    console.log(digits.currentOperand);
  };



   let buttonColor:string;

   buttonColor = themeState.darkTheme? "btn--dark":"btn--white"
  

  const handleClearDigit = () => {
    dispatch(clearDigit());
    

  };

  const handleRemoveLastDigit = () => {
    
    dispatch(removeLastDigit());
  };

  const handleChooseOperation = (pressedOperation: string) => {
    dispatch(chooseOperation(pressedOperation));

    console.log("operation clicked", digits.operation);
  };

  const handleEvaluation = () => {
    dispatch(performEvaluation());
  };

 

  return (
    
    // grid container
    <div className="container">
      {/* output screen of calculator */}
      <div className="container__screen">
        
        <div className="container__screen--calculation">
          {formatStringtoNumberWithComma(digits.prevOperand)} {digits.operation}
        </div>

        <div className="container__screen--result">
          {formatStringtoNumberWithComma(digits.currentOperand)}
        </div>
      </div>
        
        
      <ClearButton
        digit="AC"
        className= {buttonColor}
        handleClearDigit={handleClearDigit}
      />
      <RemoveLastDigitButton
        digit="DEL"
        className={buttonColor}
        handleRemoveLastDigit={handleRemoveLastDigit}
      />
   
      <OperationButton
        operation="÷"
        className="btn--cirlcular-border"
        handleChooseOperation={handleChooseOperation}
      />

      <Button
        digit="1"
        className={buttonColor}
        handleAddDigits={handleAddDigits}
      />
      <Button
        digit="2"
        className={buttonColor}
        handleAddDigits={handleAddDigits}
      />
      <Button
        digit="3"
        className={buttonColor}
        handleAddDigits={handleAddDigits}
      />

      <OperationButton
        handleChooseOperation={handleChooseOperation}
        operation="×"
        className="btn--cirlcular-border"
      />

      <Button
        digit="4"
        className={buttonColor}
        handleAddDigits={handleAddDigits}
      />
      <Button
        digit="5"
        className={buttonColor}
        handleAddDigits={handleAddDigits}
      />
      <Button
        digit="6"
        className={buttonColor}
        handleAddDigits={handleAddDigits}
      />

      <OperationButton
        operation="+"
        className="btn--cirlcular-border "
        handleChooseOperation={handleChooseOperation}
      />

      <Button
        digit="7"
        className={buttonColor}
        handleAddDigits={handleAddDigits}
      />
      <Button
        digit="8"
        className={buttonColor}
        handleAddDigits={handleAddDigits}
      />
      <Button
        digit="9"
        className={buttonColor}
        handleAddDigits={handleAddDigits}
      />

      <OperationButton
        operation="-"
        className="btn--cirlcular-border"
        handleChooseOperation={handleChooseOperation}
      />

      <Button
        digit="."
        className={buttonColor}
        handleAddDigits={handleAddDigits}
      />

      <Button
        digit="0"
        className={buttonColor}
        handleAddDigits={handleAddDigits}
      />

      <EvaluateButton
        equalDigit="="
        handleEvaluation={handleEvaluation}
        className=" btn--span-threeTofour btn--cirlcular-border"
      />
    </div>
  );
}

export default App;
