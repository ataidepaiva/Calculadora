let tape = [];
let display = document.getElementById('display');
let historyList = document.getElementById('history');

function appendNumber(number) {
  display.value += number;
}

function calculate() {
  let result = eval(display.value);
  tape.push(display.value + ' = ' + result);
  historyList.innerHTML = tape.map(item => '<li>' + item + '</li>').join('');
  display.value = result;
}

function clearDisplay() {
  display.value = '';
}

document.addEventListener('keydown', function(event) {
  if (event.code === 'NumpadEnter') {
    calculate();
  } else if (event.code === 'NumLock') {
    if (event.getModifierState('NumLock')) {
      tape = [];
      display.value = '';
      historyList.innerHTML = '';
    } else {
      calculate();
    }
  }
});
