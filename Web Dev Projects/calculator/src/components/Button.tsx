import React from "react";

interface ButtonProps {
  digit: string;
  handleAddDigits?: (pressedDigit: string) => void;
  className?: string;
  
}

const Button = ({
  digit,
  className,
  handleAddDigits,
  
}: ButtonProps) => {
  return (
    <button className={className} onClick={() => { handleAddDigits?.(digit)} }>
      {digit}
    </button>
  );
};

export default Button;
