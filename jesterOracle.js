const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});

const responses = [
  "Hmm... sounds like a race condition in your soul.",
  "Try rebooting your sense of identity.",
  "That’s not a bug, it’s a metaphor.",
  "404: Motivation not found.",
  "Ah yes, classic user error... also known as life."
];

readline.question("Ask the jester your question: ", (q) => {
  const reply = responses[Math.floor(Math.random() * responses.length)];
  console.log("\n🎭 Jester says: " + reply);
  readline.close();
});
