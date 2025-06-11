#!/bin/bash
# Tupac Moji Dropper – Bash legacy edition

echo "🎤 Yo, hvor du cruiser?"
read sted

echo "👁️ Hvem spotta du?"
read person

echo "🧠 Hvilken stemning er det?"
read stemning

case $stemning in
  "cool") echo "😎✌️ You just slang'd a moji at $person on $sted." ;;
  "sus") echo "🤨👀 Watchin' from the lowride. No sudden moves." ;;
  "past") echo "😏🕶️ Ghosts of feels. Eyes forward, heart behind." ;;
  "deep") echo "🛣️🌑 Just you, the beat, and unanswered messages." ;;
  *) echo "🎲 Moji unclear. Throwing up 🤷 for the drive-by effect." ;;
esac

