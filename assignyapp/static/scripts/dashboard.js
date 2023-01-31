const goBtn = document.querySelector(".send-btn");
console.log(goBtn);
goBtn.addEventListener("click", (e) => {
  console.log(e);
  confirm("You can't edit this assignment after submitting? ");
  location.href = "/dashboard?=true";
});
