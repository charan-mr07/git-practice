# My Git & GitHub Learning Notes

## Day 1 — July 11, 2026

**What I did:**
- Installed Git, configured user.name and user.email
- Created a local repo using git init
- Created test.py and made my first commit
- Created a GitHub repo named "git-practice"
- Connected local repo to GitHub using git remote add
- Pushed my first commit to GitHub
- Added a README.md directly on GitHub

**Commands learned:**
- git init
- git config --global user.name
- git config --global user.email
- git status
- git add .
- git commit -m "message"
- git remote add origin
- git branch -M main
- git push -u origin main

**Key learning:**
- Git = tool on my laptop that tracks changes
- GitHub = website that hosts my git repos online

## Day 2 — July 12, 2026

What I did:
- Day 1 was only about Git & GitHub basics (no Python yet)
- Since I already know basic Python, today I started practicing 
  small Python problems and committing them using Git
- First practice: Variable swap without using a third variable

Concept practiced:
- Method 1: Tuple unpacking → a, b = b, a
- Method 2: Arithmetic (+ and -) → x = x+y, y = x-y, x = x-y

Goal: Build a daily habit of practicing Python + committing to GitHub

## Day 3 — July 13, 2026

What I did:
- Learned and practiced about Data Types in Python
- Explored how Python automatically detects the type of a variable
- Practiced using type() function to check data types

## Day 4 — July 14, 2026

What I did:
- Fixed my entire repo folder structure (major cleanup)
- Found that "day 1" folder had git repo (.git) inside it instead of the root
  - Moved .git folder from "day 1" to root level using Move-Item
  - Moved day2 and day3 folders out of day1, into root level
  - Moved test.py, README.md, notes.md into a proper "day 1" folder for consistency
  - Verified with git status that everything was tracked as "renamed" (clean history)
  - Committed and pushed the fix successfully

- Practiced if-elif-else conditionals
  - Wrote a program to check if a number is positive, negative, or zero
  - First attempt had a bug: used nested if instead of elif
  - Nested if = each condition checked only if the outer one was true (wrong logic)
  - elif = all conditions checked at the same level, only one runs (correct logic)
  - Fixed the code by aligning if-elif-else at the same indentation
  - Tested with 0, positive, and negative numbers — all worked correctly

Achievement unlocked today:
- Learned to debug and fix a real folder/repo structure issue independently 
- Learned the difference between nested if and elif through a real mistake
- First time fixing a logic bug by understanding indentation in Python

Note: I used an AI chatbot as a guide to help me understand and fix the 
issues I ran into today. I made sure to understand the reasoning behind 
each fix rather than just copying solutions, which helped me learn Git 
internals and Python logic more deeply.