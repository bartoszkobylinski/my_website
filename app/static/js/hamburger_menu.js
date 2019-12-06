function myFunction() {
    var hamburger = document.getElementById("navigation");
    if (hamburger.className === "nav") {
      hamburger.className += " responsive";
    } else {
      hamburger.className = "nav";
    }
  }