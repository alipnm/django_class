const errorsBoxElement = document.getElementsByClassName("errors");
const submitBtnElement = document.getElementById("submitBtn");

let errorCheck = () => {
  console.log("sth");
  for (let i = 0; i < errorsBoxElement.length; i++) {
    const error = errorsBoxElement.item(i);
    if (error.innerHTML) {
      console.log("mozmakhoreydel");
    }
  }
};

submitBtnElement.addEventListener("click", errorCheck);
