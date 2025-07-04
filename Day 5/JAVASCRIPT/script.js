function onFormSubmit() {
  const name = document.getElementById("NAME").value.trim();
  const age = document.getElementById("AGE").value.trim();
  const mobile = document.getElementById("MOBILE").value.trim();
  const email = document.getElementById("MailID").value.trim();
  const course = document.getElementById("COURSE").value.trim();

  if (isValid(name, age, mobile, email, course)) {
    alert("Your details are saved successfully!");
    // Optional: you could add code to display the submitted data in a table here
    clearForm();
  }
}

function isValid(name, age, mobile, email, course) {
  // Name validation
  const namePattern = /^[A-Z][a-zA-Z]+$/;
  if (!namePattern.test(name)) {
    alert("Please enter a valid Name where first letter is capital");
    document.getElementById("NAME").focus();
    return false;
  }

  // Age validation
  const ageValue = parseInt(age);
  if (isNaN(ageValue) || ageValue < 0 || ageValue > 1000) {
    alert("Please enter a valid Age between 18 and 100.");
    document.getElementById("AGE").focus();
    return false;
  }

  // Mobile validation
  const mobilePattern = /^[0-9]\d{9}$/;
  if (!mobilePattern.test(mobile)) {
    alert("mobile number should contain 10digits ");
    document.getElementById("MOBILE").focus();
    return false;
  }

  // Email validation
  const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailPattern.test(email)) {
    alert("Please enter a valid Email ID.");
    document.getElementById("MailID").focus();
    return false;
  }

  // Course validation
  const coursePattern = /^[a-zA-Z\s]+$/;
  if (!coursePattern.test(course)) {
    alert("Please enter a valid Course name (letters and spaces only).");
    document.getElementById("COURSE").focus();
    return false;
  }

  return true;
}

function clearForm() {
  document.getElementById("NAME").value = "";
  document.getElementById("AGE").value = "";
  document.getElementById("MOBILE").value = "";
  document.getElementById("MailID").value = "";
  document.getElementById("COURSE").value = "";
  document.getElementById("NAME").focus(); // Set focus to the first field
}

function exitForm() {
  if (confirm("Are you sure you want to exit?")) {
    alert("Exiting the form. (Note: window may not close due to browser restrictions)");
    // window.close(); // Uncomment only if the window is opened via JS
  }
}
