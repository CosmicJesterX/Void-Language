// 🌀 voidchain-prototype.js
// Simulerer en "blockchain-liknende" brukeropplevelse over HTTP/CLI med OS-basert differensiering

const os = require("os");
const readline = require("readline");
const fs = require("fs");

const visitorId = generateId();
const userOS = os.platform();

const userChainFile = `./voidchain_${visitorId}.json`;

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

// Initial block
let chain = [
  {
    block: 1,
    event: "visitor arrived",
    os: userOS,
    timestamp: new Date().toISOString(),
  },
];

printIntro();

rl.question("Trykk Enter for å fortsette inn i tomrommet... ", () => {
  logNextBlock("initiate void entry");

  rl.question("Hva ønsker du i dag fra voiden? ", (answer) => {
    logNextBlock(`requested: ${answer}`);

    console.log("\n--- RESPONSE FRA VOIDEN ---");
    respondToUser(answer);

    fs.writeFileSync(userChainFile, JSON.stringify(chain, null, 2));
    rl.close();
  });
});

function printIntro() {
  console.log("\n🌀 VELKOMMEN TIL VOIDCHAIN 🌀");
  console.log(`Du er oppdaget som en ${userOS}-bruker.`);
  switch (userOS) {
    case "linux":
      console.log("Du har nøkkelen til shell. Tomrommet åpner seg med respekt.");
      break;
    case "win32":
      console.log("Windows-vandrer, speilet flimrer... voiden tilpasser seg.");
      break;
    case "darwin":
      console.log("Elegant Mac-vesen... du glir inn som en skyggestrek.");
      break;
    default:
      console.log("Ukjent operativsystem, voiden nøler men slipper deg inn.");
  }
}

function logNextBlock(event) {
  chain.push({
    block: chain.length + 1,
    event,
    timestamp: new Date().toISOString(),
  });
}

function respondToUser(input) {
  const lower = input.toLowerCase();
  if (lower.includes("lys")) {
    console.log("✨ Voidens svar: Du ER lyset.");
  } else if (lower.includes("kaffe")) {
    console.log("☕ Voidens svar: Kaffen er allerede drukket. Av deg. Forrige gang.");
  } else {
    console.log("🌀 Voidens svar: Det du søkte, er allerede på vei mot deg.");
  }
}

function generateId() {
  return Math.random().toString(36).substring(2, 10);
}
