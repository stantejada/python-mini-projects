# FlashCard App

## 1. Project Overview
### Project title: 
Cantonese Flashcard Learning App
### Developer:
Diego Tejada
### Date:
10/06/2025
### Technology
Python - Tkinter GUI, CSV Data Source

### Description
This project aims to build an interactive desktop flashcard application for learning Cantonese vocabulary. It allow user to review words, meaning, pronunciation and some examples in a csv file. User will be able to flip each card to reveal meaninng and mark weather they know or not the word.

### Project Objectives
- Create a funtional, user-friendly flashcard system.
- Implement efficient data loading and interation using csv file
- Provide a study experience that simulates real flashcards
- Track user progress dynamically (known.unknown words)
- Apply modular design principles and event-driven GUI programming

### Project Scope
**In Scope**
- Reading vocabulary data from csv file
- Displaying words and meanings on flashcards
- Flipping between front and back views
- Tracking known and unknown words within a session
- Providing a simple, aesthetic user interface using using tkinter

**Out Scope**
- Online Sync or DB integration
- Speech pronunciation or audio playback
- Complex data analytics or spaced repetition algorithms
- Multiuser profile managment

### Funtional Requirements
| Feature | Description | Priority|
|---------|-------------|---------|
| Load CSV Data      | Import vocabulary data with columns for Word, Meaning, Pronunciation, etc. | High         |
| Display Flashcard  | Show one word per card in the UI.                                          | High         |
| Flip Card          | Toggle between “front” (Word) and “back” (Meaning + Sentence).             | High         |
| Mark Known/Unknown | Let the user indicate whether they know a word.                            | High         |
| Random Selection   | Present words in random order for variety.                                 | Medium       |
| Session Progress   | Track remaining words dynamically.                                         | Medium       |
| End Message        | Notify the user when all words are reviewed.                               | Low          |


### System Design
**Architecture**
Frontend: Tkinter GUI
Backend: Python Logic for Data Processing
Data Source: CSV

**Main Components**
1. Data module
- Read and prepares data from csv
- Store words in a list or dictionary
2. Logic Module
- Controls card selection, flipping and process
3. UI Module
- Display current card
- Update based on user actions

### Development Plan
| **Phase**        | **Task**                                        | **Tools / Skills** | **Expected Output** |
| ---------------- | ----------------------------------------------- | ------------------ | ------------------- |
| 1. Setup         | Prepare CSV and basic Tkinter window.           | Python, Pandas     | Base structure      |
| 2. Data Handling | Load and validate CSV data.                     | CSV / Pandas       | Word list ready     |
| 3. Card Logic    | Implement next, flip, known, unknown functions. | Python             | Functional core     |
| 4. GUI Design    | Add Canvas, Buttons, Layout, Colors.            | Tkinter            | Working UI          |
| 5. Testing       | Test navigation and error handling.             | Manual testing     | Stable app          |
| 6. Polish        | Improve readability, optional progress message. | Design/UI          | Final version       |
