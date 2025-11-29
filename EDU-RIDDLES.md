# Riddling Educational Hooks for Void-Language and WIMP

Use these bite-sized riddles to introduce concepts, seed issues, motivate exercises, or make PRs and docs more playful. Each entry includes: the riddle, a one-line answer, the learning objective, and suggested places to use it.

---

## 1) README Icebreaker — "The Tiny Interpreter"
Riddle:
"I am written in JS but speak my own tongue; give me a file and watch a sentence become sung. What am I?"

Answer: Void-Language's interpreter

Learning goal: Introduce what Void is and explain the interpreter/run flow.

Where to use: Void README intro, repo description, demo page header.

Teacher note: Follow the riddle with a one-line example command (node ./src/interpreter.js examples/hello.void) so curious readers try it right away.

---

## 2) Quickstart Prompt — "The Manual in the Machine"
Riddle:
"I live between man and shell: terse pages in roff, small and swell. I teach the commands yet never shout—find me where help is typed without a doubt. Who am I?"

Answer: WIMP's roff man pages / documentation

Learning goal: Teach contributors that WIMP uses roff/formatted man-style docs and where to find usage instructions.

Where to use: WIMP README snippet, man-page header, CONTRIBUTING.md.

Teacher note: Link to the man file and show a sample `man ./wimp.1` command or `nroff -man wimp.1 | less`.

---

## 3) Issue-starter — "A Bug as a Puzzle"
Riddle:
"A whisper in the log, a mismatch in the run; numbers that should dance instead stop having fun. Trace me where the interpreter counts—what's wrong and how hard is the amount?"

Answer: A failing arithmetic example in Void interpreter

Learning goal: Encourage issue reporters to include failing example programs and expected output.

Where to use: Issue template / issue body starter.

Teacher note: Append a checklist for reproduction: steps to run, sample code, expected vs actual.

---

## 4) Workshop Icebreaker — "Particles and Programs"
Riddle:
"I am tiny, interactive, and multiply on each beat; I bounce in your browser or shuffle in your sheet. Merge my spirit with a tiny language's mind — what kind of demo will you find?"

Answer: A web demo combining WIMP's particle visualization with Void code (e.g., code controls particles)

Learning goal: Show how to integrate Void's JS runtime with WIMP's visual outputs for interactive demos.

Where to use: Workshop slides, live-coding demo, "examples/" readme.

Teacher note: Provide starter code: a Void program that emits simple commands consumed by a JS particle renderer.

---

## 5) Code-kata prompt — "The Minimal Compiler"
Riddle:
"Take tokens from a whisper, shape them into a plan; return a tidy answer that a tiny VM can scan. What are you building?"

Answer: A tokenizer/parser/compiler stage for Void

Learning goal: Teach lexical analysis and parsing by asking participants to implement a tokenizer or AST for a small subset.

Where to use: CONTRIBUTING.md, learning exercises, GitHub Discussions.

Teacher note: Give trivial input and expected token list; include unit-test skeletons.

---

## 6) PR Description Opener — "Patch for the Manuals"
Riddle:
"A sentence added, a comma freed; someone reads faster now than need. The docs now sing a tune more clear—what did the PR do here?"

Answer: Improved WIMP roff docs / fixed a typo and added usage example

Learning goal: Make PRs feel helpful and visible; remind reviewers to check docs.

Where to use: PR templates or first-line PR descriptions.

Teacher note: Keep the rest of the PR body actionable: what changed, why, how to test.

---

## 7) Classroom Assignment — "Map of a New Tongue"
Riddle:
"I have few words but many rules, I run on engines and teach new tools. Give me examples, edge cases too; find where syntax breaks and document the view."

Answer: Create a short spec + test-suite for a Void feature

Learning goal: Exercises in language spec writing, test-driven design, and docs.

Where to use: Syllabus, lab handout, classroom GitHub repo.

Teacher note: Provide a rubric and a starter template for tests in the repo's test/ folder.

---

## 8) Social / Teaser Tweet — "A Tiny Tease"
Riddle:
"Made a tiny language that whispers in JS and a set of particle demos that dance in roff—guess which one teaches compilers and which one draws the skies? 😉"

Answer: Void teaches compilers (JS), WIMP draws particle demos (roff-man docs)

Learning goal: Create curiosity and community pull for both projects.

Where to use: Tweets, Mastodon posts, GitHub release notes.

Teacher note: Link to a live demo or the README for quick onboarding.

---

## 9) Interactive Challenge — "Manpages &amp; Machines"
Riddle:
"A manual old as terminals, hidden under a newer crown; convert the roff into a web that users can browse around. What is the task?"

Answer: Convert WIMP's roff docs into HTML docs (or generate HTML man-pages)

Learning goal: Teach content-to-HTML conversion, tooling like pandoc or groff-&gt;html pipelines.

Where to use: Good first issue or "help wanted" task in WIMP.

Teacher note: Provide command-line examples and desired output snippets.

---

## 10) Reflection Prompt — "Why We Build"
Riddle:
"I exist not to scale the world nor to rule the cloud's domain; I am a narrow mirror—what we learn from the pain. What do we call this practice?"

Answer: Learning-by-building / educational experimental project

Learning goal: Encourage a README "Why this exists" section that frames both repos as learning artifacts.

Where to use: Both repos' README and CONTRIBUTING sections.

Teacher note: Add a short paragraph about learning objectives and suggested next steps for contributors.

---

## How to use this file
- Paste single riddles into README subheadings, PR titles, or issue templates.
- Use the "Where to use" suggestions to target the audience.
- Replace specific command examples to match your actual file locations and scripts.

---

## License and attribution
You may adapt these riddles; consider adding a short note in each repo acknowledging the playful/educational intent so contributors match tone.
