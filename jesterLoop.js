const jesterThoughts = [
  "Why does 0 == '0', but 0 !== '0'?",
  "I declared a var and it declared me back.",
  "Sometimes I console.log just to feel seen.",
  "This loop has no purpose, and that's the point."
];

function startVoidDance() {
  let i = 0;
  while (true) {
    console.log(jesterThoughts[i % jesterThoughts.length]);
    i++;
    if (Math.random() > 0.9999) {
      throw new Error("The jester has left the terminal.");
    }
  }
}

startVoidDance();
