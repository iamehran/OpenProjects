import { createSlice, PayloadAction } from "@reduxjs/toolkit";

// interface of the state of the app
interface CalculatorState {
  currentOperand: string;
  prevOperand: string;
  operation: string;
  overwrite: boolean;
}

// default state
const initialState: CalculatorState = {
  currentOperand: "",
  prevOperand: "",
  operation: "",
  overwrite: false,
};

//function  to give results based on the operation choosen
const Evaluate = ({
  currentOperand,
  prevOperand,
  operation,
}: CalculatorState) => {
  const current = parseFloat(currentOperand);
  const prev = parseFloat(prevOperand);
  //return empty string if both operands ane not numbers
  if (isNaN(current) || isNaN(prev)) return "";

  let result: string | number = "";

  // handle the individual arithmetic operar=tions
  switch (operation) {
    case "+":
      result = prev + current;
      break;
    case "-":
      result = prev - current;
      break;
    case "×":
      result = prev * current;
      break;

    case "÷":
      result = prev / current;
      break;
  }

  return result.toString();
};

//Digit Slice in the redux toolkit
export const digitSlice = createSlice({
  name: "CalculatorState",
  initialState,

  reducers: {
    //handle adding digit behind the other when clicked
    addDigit: (state, action: PayloadAction<string>) => {
      if (state.overwrite) {
        return {
          ...state,
          overwrite: false,
          currentOperand: action.payload,
        };
      }
      if (state.currentOperand === "0" && action.payload === "0") {
        return state;
      }
      if (state.currentOperand.includes(".") && action.payload === ".") {
        return state;
      }

      const addedDigit: string = `${state.currentOperand || " "}${
        action.payload
      }`;
      return { ...state, currentOperand: addedDigit };
    },

    //clearing the screen
    clearDigit: (state) => {
      return {
        ...state,
        currentOperand: "",
        prevOperand: "",
        operation: "",
      };
    },

    //delete last digit
    removeLastDigit: (state) => {
      const remainingDigit: string = `${state.currentOperand.slice(0, -1)}`;

      return { ...state, currentOperand: remainingDigit };
    },

    //choose operation whether + - *
    chooseOperation: (state, action: PayloadAction<string>) => {
      if (state.currentOperand === "" && state.prevOperand === "") {
        return state;
      }

      if (state.currentOperand === "") {
        return {
          ...state,
          operation: action.payload,
        };
      }

      if (state.prevOperand === "") {
        return {
          ...state,
          currentOperand: "",
          prevOperand: state.currentOperand,
          operation: action.payload,
        };
      }

      return {
        ...state,
        prevOperand: Evaluate(state),
        currentOperand: "",
        operation: action.payload,
      };
    },

    //when user clicks =
    performEvaluation: (state) => {
      if (
        state.operation === "" ||
        state.currentOperand === "" ||
        state.prevOperand === ""
      ) {
        return state;
      }

      return {
        ...state,
        currentOperand: Evaluate(state),
        prevOperand: "",
        operation: "",
        overwrite: true,
      };
    },
  },
});

//sending our actions to be used in App.tsx
export const {
  addDigit,
  clearDigit,
  removeLastDigit,
  chooseOperation,
  performEvaluation,
} = digitSlice.actions;

export default digitSlice.reducer;
