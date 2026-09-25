document.getElementById("studentForm").onsubmit = function(event) {

    event.preventDefault();

    
    let name = document.getElementById("name").value;
    let email = document.getElementById("email").value;
    let phone = document.getElementById("phone").value;
    let course = document.getElementById("course").value;
    let confirmPassword = document.getElementById("confirmPassword").value;

   let gender = document.querySelector(
        'input[name="gender"]:checked'
    );

    if (name == "") {
        alert("Please enter your name");
        return;
    }

    if (email == "") {
        alert("Please enter your email");
        return;
    }

    if (phone == "") {
        alert("Please enter your phone number");
        return;
    }

    if (gender == null) {
        alert("Please select your gender");
        return;
    }

    if (course == "") {
        alert("Please select a course");
        return;
    }

    if (password == "") {
        alert("Please enter your password");
        return;
    }

    
    if (confirmPassword == "") {
        alert("Please confirm your password");
        return;
    }

    if (password != confirmPassword) {
        alert("Passwords do not match");
        return;
    }

    let student = {
        name: name,
        email: email,
        phone: phone,
        gender: gender.value,
        course: course,
        password: password
    };

    
    let  students = JSON.parse(localStorage.getItem("students"));

    if (students == null) {
        students = [];
    }

    students.push(student);

    localStorage.setItem("students", JSON.stringify(students));

    document.getElementById("message").innerHTML =
        "Registration Successful!";

    document.getElementById("studentForm").reset();


    
};