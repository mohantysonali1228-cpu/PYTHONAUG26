let loginForm = document.getElementById("loginForm");

loginForm.addEventListener("submit", function (e) {

    e.preventDefault();

    let email = document.getElementById("email").value.trim();

    let password =
        document.getElementById("password").value;

    let message =
        document.getElementById("message");


    if (!email || !password) {

        message.textContent =
            "Please enter email and password.";

        return;
    }


    let user = JSON.parse(
        localStorage.getItem("registeredUser")
    );


    if (!user) {

        message.textContent =
            "User not registered. Please register first.";

        return;
    }


    if (user.email !== email) {

        message.textContent =
            "Invalid email.";

        return;
    }


    if (user.password !== password) {

        message.textContent =
            "Invalid password.";

        return;
    }


    message.textContent =
        "Login successful! Welcome " + user.name;

    loginForm.reset();

});