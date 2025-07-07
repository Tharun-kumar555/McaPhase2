function showGreeting() {
    var name = document.getElementById("nameInput").value;
    var greeting = "Hello, " + name + "!";
    document.getElementById("greeting").innerText = greeting;
}