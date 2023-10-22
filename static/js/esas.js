var slider1 = document.getElementById("amount");
var slider2 = document.getElementById("month");
var slider3 = document.getElementById("interest");
var output1 = document.getElementById("demo1");
var output2 = document.getElementById("demo2");
var output3 = document.getElementById("demo3");

output1.innerHTML = slider1.value;
output2.innerHTML = slider2.value;
output3.innerHTML = slider3.value;

slider1.oninput = function() {
  output1.value = this.value;
  var out1=output1;
}
slider2.oninput = function() {
  output2.value = this.value;
  var out2=output2;
}
slider3.oninput = function() {
  output3.value = this.value;
  var out3=output3;
}

const buttonID = document.getElementById("loan-form")
buttonID.addEventListener('click', function(element) {
  element.preventDefault();
  const UIamount = slider1.value;
  const UImonth = slider2.value;
  const UIinterest = slider3.value;

  const principal = parseFloat(UIamount);
  const CalculateInterest = parseFloat(UImonth) / 100 / 12;
  const calculatedPayments = parseFloat(UIinterest)

  //Compute monthly Payment

  const x = Math.pow(1 + CalculateInterest, calculatedPayments);
  const monthly = (principal * x * CalculateInterest) / (x - 1);
  const monthlyPayment = monthly.toFixed(2);

  //Show results

  document.getElementById("monthlyPayment").innerHTML =monthlyPayment + "₼" ;
})




$(document).ready(function() {
  var topp2Wrapper = $(".topp2-wrapper");
  var topp2 = topp2Wrapper.find(".topp2");
  var topp2Offset = topp2Wrapper.offset().top;

  $(window).scroll(function() {
    var scrollTop = $(window).scrollTop();
    if (scrollTop > topp2Offset) {
      navbar.addClass("fixed");
    } else {
      navbar.removeClass("fixed");
    }

  
    if (scrollTop === 0) {
      navbar-wrapper.addClass("at-top");
    } else {
      navbar-wrapper.removeClass("at-top");
    }
  });
});


const navbarWrappers = document.querySelectorAll('.navbar-wrapper');
const modal = document.querySelector('.modal');

// Modal açıldığında, diğer navbarların z-index değerlerini düşürün
function lowerNavbarZIndex() {
  navbarWrappers.forEach(navbar => {
    if (!navbar.classList.contains('active-navbar')) {
      navbar.style.zIndex = '1050';
    }
  });
}






 








