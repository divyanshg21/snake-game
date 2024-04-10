document.addEventListener("DOMContentLoaded", function() {
    var canvas = document.getElementById("game-canvas");
    var ctx = canvas.getContext("2d");
  
    fetch("/play")
      .then(function(response) {
        return response.text();
      })
      .then(function(data) {
        console.log(data); // Game over message
      })
      .catch(function(error) {
        console.error("Error:", error);
      });
  
    // Add any additional JavaScript code to handle user input and update the game canvas
  });