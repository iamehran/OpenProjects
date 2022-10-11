const previousOperand = document.querySelector(' [data-previousOperand]'),
      currentOperand = document.querySelector('[ data-currentOperand]'),
      numbers = document.querySelectorAll('[data-number]'),
      equalButton = document.querySelector('[data-equal]'),
      deleteButton = document.querySelector('[data-delete]'),
      allclearButton = document.querySelector('[data-allclear]'),
      operations = document.querySelectorAll('[data-operation]');

class Calculator{
    constructor(previousOperand,currentOperand){
       this.previousBox = previousOperand;
       this.currentBox = currentOperand;
       this.currentOperand = '';
       this.previousOperand = '';
    }
    clear(){
       this.currentOperand = ''
       this.currentBox.innerText = ''
       this.previousBox.innerText= ''
    }
    appendNumber(number){
      if(number == '.' && this.currentOperand.includes('.'))return //return nothing 
      const stringNumbers  = new String(number) //converting the number into string 
      this.currentOperand = this.currentOperand+ stringNumbers
    }
    chooseOperation(operation){
       if(this.currentOperand =='')return
       if(this.currentOperand!= ''){
           this.compute()
       }
       this.selectedOperation = operation;
       this.previousOperand = this.currentOperand 
       this.currentOperand = ''
    }
    delete(){
      this.currentOperand = this.currentOperand.toString().slice(0,-1)
    }
    compute(){
       let computation
       this .prev = parseFloat(this.previousOperand)
       this.current = parseFloat(this.currentOperand)
       if(isNaN(this.prev)||isNaN(this.current))return
       switch (this.selectedOperation) {
           case '+':
            computation = this.prev + this.current
            break;
           case '-':       
            computation = this.prev - this.current
            break;
           case '*':
            computation = this.prev * this.current
            break;
           case '÷':
            computation = this.prev / this.current
            break;           
       
       
           default:
              return
       }
       this.currentOperand = computation
       this.previousOperand = ''
       this.selectedOperation = undefined
    }

  getDisplayNumber(number) {
    const stringNumber =new String(number)
    const integerDigits = parseFloat(stringNumber.split('.')[0])
    const decimalDigits = stringNumber.split('.')[1]
    let integerDisplay
    if (isNaN(integerDigits)) {
      integerDisplay = ''
    } else {
      integerDisplay = integerDigits.toLocaleString('en', { maximumFractionDigits: 0 })
    }
    if (decimalDigits != null) {
      return `${integerDisplay}.${decimalDigits}`
    } else {
      return integerDisplay
    }
  }
    updateDisplay(){
        this.currentBox.innerText = this.getDisplayNumber(this.currentOperand)
        if(this.selectedOperation!=null){
            this.previousBox.innerText = `${this.getDisplayNumber(this.previousOperand)} ${this.selectedOperation}`
        }
        else{
            this.previousBox.innerText = ''
        }
    }
}

const calculator =new Calculator(previousOperand,currentOperand);
//event listner for numbers
numbers.forEach(number =>{
    number.addEventListener('click',()=>{
        calculator.appendNumber(number.innerText)
        calculator.updateDisplay()
    })
})

//event listner for opearator
operations.forEach(operator =>{
    operator.addEventListener('click',()=>{
        calculator.chooseOperation(operator.innerHTML)
        calculator.updateDisplay()
    })
})

//event listner for event equalButton
equalButton.addEventListener('click',equal=>{
    calculator.compute()
    calculator.updateDisplay()

})

//clear the display
allclearButton.addEventListener('click',()=>calculator.clear())

//delete last entered number
deleteButton.addEventListener('click',()=>{
    calculator.delete()
    calculator.updateDisplay()
})
     
