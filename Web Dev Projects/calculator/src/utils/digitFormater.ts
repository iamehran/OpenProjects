
  //inbuit function to format number
  const INTEGER_FORMATTER = new Intl.NumberFormat("en-us", {
    maximumFractionDigits: 0,
  });

    //format our digits to have commas for thousands and tens of thousands
  export const formatStringtoNumberWithComma = (currentDigit: any) => {
    if (currentDigit === "") return;
    const [integer, decimal] = currentDigit.split(".");
    if (decimal == null) return INTEGER_FORMATTER.format(integer);
    return `${INTEGER_FORMATTER.format(integer)}.${decimal}`;
  };