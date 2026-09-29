
let registerBox = document.querySelector("#registerBox");
let loginBox = document.querySelector("#loginBox");
let registerMessage = document.querySelector("#registerMessage");
let loginMessage = document.querySelector("#loginMessage");
let showLogin = document.querySelector("#showLogin");
showLogin.addEventListener("click", function () {

    registerBox.classList.add("hidden");
    loginBox.classList.remove("hidden");

    registerMessage.innerText = "";
});


let showRegister = document.querySelector("#showRegister");

showRegister.addEventListener("click", function () {

    loginBox.classList.add("hidden");
    registerBox.classList.remove("hidden");

    loginMessage.innerText = "";
});


let registerForm = document.querySelector("#registerForm");
registerForm.addEventListener("submit", function (e) {

    e.preventDefault();
    let name = document.querySelector("#regName").value.trim();
    let email = document.querySelector("#regEmail").value.trim();
    let password = document.querySelector("#regPassword").value;
    let confirmPassword =
        document.querySelector("#confirmPassword").value;

    registerMessage.innerText = "";
    registerMessage.className = "message";
    
    if (name === "") {
        showRegisterMessage("Please enter your name", "error");
        return;
    }


    if (email === "") {
    showRegisterMessage("Please enter your email", "error");
        return;
    }


    if (password === "") {
        showRegisterMessage("Please create a password", "error");
        return;
    }


    if (password.length < 6) {
        showRegisterMessage(
            "Password must contain at least 6 characters",
            "error"
        );

        return;
    }


    if (confirmPassword === "") {
        showRegisterMessage(
            "Please confirm your password",
            "error"
        );

        return;
    }


    if (password !== confirmPassword) {
        showRegisterMessage(
            "Passwords do not match",
            "error"
        );

        return;
    }



    let users = JSON.parse(localStorage.getItem("users")) || [];

    let existingUser = users.find(function (user) {

        return user.email === email;

    });


    if (existingUser) {
        showRegisterMessage(
            "Email already registered!",
            "error"
        );

        return;
    }



    let newUser = {

        name: name,
        email: email,
        password: password

    };

    users.push(newUser);


 

    localStorage.setItem(
        "users",
        JSON.stringify(users)
    );
    
    showRegisterMessage(
        "Registration successful! Please login.",
        "success"
    );
    
    registerForm.reset();
    
    setTimeout(function () {

        registerBox.classList.add("hidden");
        loginBox.classList.remove("hidden");

    }, 1000);

});

let welcomeBox = document.querySelector("#welcomeBox");
let loginForm = document.querySelector("#loginForm");
loginForm.addEventListener("submit", function (e) {

    e.preventDefault();
    let email =
        document.querySelector("#loginEmail").value.trim();

    let password =
        document.querySelector("#loginPassword").value;


    loginMessage.innerText = "";
    loginMessage.className = "message";



    if (email === "") {
        showLoginMessage(
            "Please enter your email",
            "error"
        );

        return;
    }


    if (password === "") {
        showLoginMessage(
            "Please enter your password",
            "error"
        );

        return;
    }



    let users =
        JSON.parse(localStorage.getItem("users")) || [];


let user = users.find(function (user) {

        return user.email === email &&
               user.password === password;

    });
    
    
    if (user) {
         localStorage.setItem(
            "loggedInUser",
            JSON.stringify(user)
        );


        loginBox.classList.add("hidden");
        welcomeBox.classList.remove("hidden");


        document.querySelector("#welcomeText").innerText =
            "Hello " + user.name + "! Welcome to your account.";

        loginForm.reset();

    }



    else {

        showLoginMessage(
            "Invalid email or password!",
            "error"
        );

    }

});



let logoutBtn = document.querySelector("#logoutBtn");
logoutBtn.addEventListener("click", function () {
    localStorage.removeItem("loggedInUser");

    welcomeBox.classList.add("hidden");

    loginBox.classList.remove("hidden");

});



function showPassword(inputId, button) {

    let input = document.querySelector("#" + inputId);


    if (input.type === "password") {

        input.type = "text";

        button.innerText = "Hide";

    }

    else {

        input.type = "password";

        button.innerText = "Show";

    }

}



function showRegisterMessage(message, type) {

    registerMessage.innerText = message;

    registerMessage.classList.add(type);

}



function showLoginMessage(message, type) {

    loginMessage.innerText = message;

    loginMessage.classList.add(type);

}

let loggedInUser =
    JSON.parse(localStorage.getItem("loggedInUser"));


if (loggedInUser) {

    registerBox.classList.add("hidden");

    loginBox.classList.add("hidden");

    welcomeBox.classList.remove("hidden");
    document.querySelector("#welcomeText").innerText =
        "Hello " + loggedInUser.name +
        "! Welcome to your account.";

}