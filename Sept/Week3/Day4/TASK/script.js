// 1. student mark- total and percentage

function calculateMarks() {
    let m1 = 80;
    let m2 = 75;
    let m3 = 90;
    let m4 = 85;
    let m5 = 70;
    let total = m1 + m2 + m3 + m4 + m5;
    let percentage = total / 5;

    console.log("Total Marks:", total);
    console.log("Percentage:", percentage + "%");
}

calculateMarks();

// 2. product discount

function calculateDiscount() {
    let price = 1200;
    let discountPercent = 15;
    let discount = price * discountPercent / 100;
    let finalPrice = price - discount;

    console.log("Discount Amount:", discount);
    console.log("Final Price:", finalPrice);
}

calculateDiscount();

// 3. Square and cube

function squareCube() {
    let num = 5;
    let square = num ** 2;
    let cube = num ** 3;

    console.log("Square:", square);
    console.log("Cube:", cube);
}

squareCube();

// 4. positive , negative and zero

function checkNumber() {
    let num = -10;

    if (num > 0) {
        console.log("Positive");
    } else if (num < 0) {
        console.log("Negative");
    } else {
        console.log("Zero");
    }
}

checkNumber();

// 5.student grade

function gradeSystem() {
    let marks = 85;

    if (marks >= 90 && marks <= 100) {
        console.log("Grade A");
    } else if (marks >= 80 && marks <= 89) {
        console.log("Grade B");
    } else if (marks >= 70 && marks <= 79) {
        console.log("Grade C");
    } else if (marks >= 60 && marks <= 69) {
        console.log("Grade D");
    } else {
        console.log("Fail");
    }
}

gradeSystem();

// 6. even or odd 

function evenOdd() {
    let num = 10;

    if (num % 2 === 0) {
        console.log("Even");
    } else {
        console.log("Odd");
    }
}

evenOdd();

// 7. largest of three numbers

function largestNumber() {
    let a = 25;
    let b = 40;
    let c = 30;

    if (a >= b && a >= c) {
        console.log("Largest:", a);
    } else if (b >= a && b >= c) {
        console.log("Largest:", b);
    } else {
        console.log("Largest:", c);
    }
}

largestNumber();

// 8. print pattern

function printPattern() {
    for (let i = 1; i <= 5; i++) {
        let pattern = "";

        for (let j = 1; j <= i; j++) {
            pattern += j;
        }

        console.log(pattern);
    }
}

printPattern();

// 9. divisible by both 3 and 5
function divisibleByBoth() {
    let count = 0;

    for (let i = 1; i <= 100; i++) {
        if (i % 3 === 0 && i % 5 === 0) {
            console.log(i);
            count++;
        }
    }

    console.log("Count:", count);
}

divisibleByBoth();

// 10. factorial
function factorial() {
    let num = 5;
    let fact = 1;

    for (let i = 1; i <= num; i++) {
        fact = fact * i;
    }

    console.log("Factorial:", fact);
}

factorial();

// 11. Multiplication

function multiplicationTable(num) {
    for (let i = 1; i <= 10; i++) {
        console.log(num + " × " + i + " = " + (num * i));
    }
}

multiplicationTable(5);

// 12. sum

function sum(a, b) {
    return a + b;
}

console.log(sum(10, 20));

// 13. ATM solution

let balance = 10000;

function deposit(amount) {
    balance = balance + amount;
    console.log("Amount Deposited: ₹" + amount);
    console.log("Current Balance: ₹" + balance);
}


function checkBalance() {
    console.log("Current Balance: ₹" + balance);
}

