const inputs = document.querySelectorAll("input"),
  button = document.querySelector("button");

// iterate over all inputs
inputs.forEach((input, index1) => {
  input.addEventListener("input", (e) => { // Changed from "keyup" to "input"
    const currentInput = input,
      nextInput = input.nextElementSibling,
      prevInput = input.previousElementSibling;

    // If the input value is not a digit or is longer than 1 digit, clear it
    if (!/^\d$/.test(currentInput.value)) {
      currentInput.value = "";
      return;
    }

    // if the next input is disabled and the current value is not empty
    // enable the next input and focus on it
    if (nextInput && nextInput.hasAttribute("disabled") && currentInput.value !== "") {
      nextInput.removeAttribute("disabled");
      nextInput.focus();
    }

    // if the backspace key is pressed
    if (e.inputType === "deleteContentBackward") { // Changed from "e.key === 'Backspace'" to "e.inputType === 'deleteContentBackward'"
      // iterate over all inputs again
      inputs.forEach((input, index2) => {
        // if the index1 of the current input is less than or equal to the index2 of the input in the outer loop
        // and the previous element exists, set the disabled attribute on the input and focus on the previous element
        if (index1 <= index2 && prevInput) {
          input.setAttribute("disabled", true);
          input.value = "";
          prevInput.focus();
        }
      });
    }

    // If the fourth input (index 3) is not empty and has no disabled attribute, add the 'active' class; otherwise, remove it
    if (!inputs[3].disabled && inputs[3].value !== "") {
      button.classList.add("active");
    } else {
      button.classList.remove("active");
    }
  });
});

// focus the first input (index 0) on window load
window.addEventListener("load", () => inputs[0].focus());
