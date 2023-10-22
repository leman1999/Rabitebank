// function selectOption(element) {
//   const selectOption=element.innerText;
//   const actionButton = element.closest('.input-group').querySelector('.btn');
//   actionButton.innerText= selectOption;
// }
function selectOption(element) {
  const selectedOption = element.innerText;
  const dropdownToggle = document.querySelector('.dropdown-toggle');
  const selectedOptionInput = document.getElementById('selected-option');

  dropdownToggle.innerText = selectedOption;
  selectedOptionInput.value = selectedOption;
}
function showsuccesmessage(){
  alert("Əmanət sorğunuz qəbul edildi!");
  window.location.href("emanetler");
}

  function formatPhoneNumber() {
    const input = document.getElementById('phoneNumber');
    let number = input.value;
  number = number.replace(/\D/g, '');

  const firstPart = number.substring(0, 3);
  
  const secondPart = number.substring(3, 5);
  
  const thirdPart = number.substring(5, 7);
    input.value =`${firstPart} ${secondPart} ${thirdPart}`;
}

