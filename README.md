# Bridgeword Puzzle Solver
#### **<ins>Description:**<ins>

This project consists of 3 files:
- brideword_puzzle.py
- requirements.txt
- README.md

The program is a **"Bridgeword Puzzle Solver"** which solves bridgeword puzzles (in German).

A bridgeword puzzle is a type of crossword puzzle often found in magazines etc.  
Bridgeword Puzzle Example:

| Puzzle | Word 1 | Gap | Word 2 |
| -------|------------|------|-----------|
| Puzzle 1 | WEIN | _ _ _ _ _ | GURKE | 
| Puzzle 2 | HALB | _ _ _ _ _ _ | KRAFT | 
| Puzzle 3 | FAUST| _ _ _ _ | RIEMEN | 
| Puzzle 4 | RUHE | _ _ _ _ | GEBER | 

1. ESSIG (=> WEINESSIG, ESSIGGURKE)
2. RECHTS (=> HALBRECHTS, RECHTSKRAFT)
3. KEIL (=> FAUSTKEIL, KEILRIEMEN)
4. GELD (=> RUHEGELD, GELDGEBER)

=> word 1 + gap word = first compound  
=> gap word + word 2 = second compound

---

#### **<ins>Usage:<ins>**

`python brideword_puzzle.py`

This program is an "Interactive console program" and functions through `input()`.

The whole program can be stopped at any time by pressing `Ctrl + C` or `Ctrl + D`.

---

#### **<ins>Features:<ins>**
- solving bridgeword puzzles (in German)

---

#### **<ins>Functioning:<ins>**

The script starts off by importing different libraries, listed in the requirements.txt file, as well as creating lists that will be needed later on.

As the program starts, a welcome message is printed and the user is prompted to type in the amout of puzzles they want to be solved.

After that, the user types in `word 1`, the `gap count`, and `word 2` for each puzzle.

The program will now search for the right solutions (in the database of German words and compounds) and print them out. If no completely right solutions are found, some potentials will be printed out for the manual review.

The program will then stop through `sys.exit()`.

<br>


