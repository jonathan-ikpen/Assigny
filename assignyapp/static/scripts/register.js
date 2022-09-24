// "use strict";

console.log("working");

const mat = document.querySelector(".mat_no");
console.log(mat);
const course = document.querySelector(".course_no");
console.log(course);
// randomNum = Math.random()
mat.value = Date.now();
course.value = Date.now();

console.log(mat.value);
console.log(course.value);

const lecturerbtn = document.querySelector("#lecturer-form");
const studentbtn = document.querySelector("#student-form");

const lecturerForm = document.querySelector("#lecturer-register-form");
const studentForm = document.querySelector("#student-register-form");

lecturerbtn.addEventListener("click", function (e) {
  e.preventDefault();
  console.log("clicked");
  studentForm.style.display = "none";
  lecturerForm.style.display = "grid";
});

studentbtn.addEventListener("click", function (e) {
  e.preventDefault();
  console.log("clicked");
  lecturerForm.style.display = "none";
  studentForm.style.display = "grid";
});
