let display = document.getElementById('display');

function appendToDisplay(value) {
    display.value += value;
}

function clearDisplay() {
    display.value = '';
}

function deleteLastCharacter() {
    display.value = display.value.slice(0, -1);
}

function calculate(operation) {
    try {
        let expression = display.value;

        if (operation) {
            if (operation === 'power') {
                expression = expression.replace('^', '**');
            }
            if (operation === 'sqrt') {
                expression = `Math.sqrt(${expression})`;
            } else if (operation === 'sin') {
                expression = `Math.sin(${expression})`;
            } else if (operation === 'cos') {
                expression = `Math.cos(${expression})`;
            } else if (operation === 'tan') {
                expression = `Math.tan(${expression})`;
            } else if (operation === 'log') {
                expression = `Math.log10(${expression})`;
            } else if (operation === 'ln') {
                expression = `Math.log(${expression})`;
            } else if (operation === 'factorial') {
                expression = `factorial(${expression})`;
            }

            expression = expression.replace(/[^0-9+\-*/.^()\s]/g, ''); 
            display.value = eval(expression);
        } else {
            let result = eval(display.value);
            display.value = result;
        }
    } catch (e) {
        display.value = 'Error';
    }
}

function factorial(n) {
    if (n === 0 || n === 1) {
        return 1;
    } else {
        return n * factorial(n - 1);
    }
}
