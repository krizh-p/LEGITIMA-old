// Inline JavaScript for random message display
const authenticMessage = document.getElementById("authentic");
const spoofedMessage = document.getElementById("spoofed");

if (Math.random() < 0.5) {
  authenticMessage.style.display = "block";
} else {
  spoofedMessage.style.display = "block";
}