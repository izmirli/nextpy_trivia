# next.py forum's Trivia Challenge

## Basic Info

**Target:** Build a trivia game.

**Deadline:** 7-apr-2022

~~**Format:** Python program as one `exe` file~~

**Submission:** https://forms.gle/SpHJmyzRmBw2HyyF7

[Original forum message](https://courses.campus.gov.il/courses/course-v1:CS+GOV_CS_nextpy102+2_2021/discussion/forum/course_g8/threads/622e3abd66f1c54aef000260) 

## Usage

#### Pre-requests

1. Make sure _**questions.json**_ file is in same directory as _**nextpy_trivia.py**_ file.
2. Install colorama package. Can be done with this command: `pip install colorama`

#### Running the game

On your terminal, make sure you're in the directory of `nextpy_trivia.py` file, and run this command:

`python nextpy_trivia.py`

## Requirements 

1. Have at least 4 questions. The questions have to be creative.
2. Display each question to the user and let him answer or ask for a hint.
3. Count the number of attempts to get the right answer. Asking for a hint is considered as an attempt.
4. Display the number of attempts after each the number of attempt.
5. Move to next question after getting the right answer.
6. Attempt will be considered as correct, even if the right answer is just part of the given input.
7. If a hint is asked for more than once, display that he already did that and display the hint again. 
This is considered as another attempt.

#### Examples

```text
Question: How many letters are in the word 'OK'?
'help' for a clue.
2 letters
Attempt 1 :Wrong- try again.
Question: How many letters are in the word 'OK'?
'help' for a clue.
```

```text
Question: How many letters are in the word 'OK'?
'help' for a clue.
help
Attempt 1 write the number in words.
Question: How many letters are in the word 'OK'?
help
You've run out of clues
Attempt 2 The clue is: write the number in words.
Question: How many letters are in the word '0K'?
```

```text
Question: How many letters are in the word 'OK'?
'help' for a clue.
help
Attempt 1 write the number in words.
Question: How many letters are in the word 'OK'?
Two letters
You win!
It took you 2 attempts.
```


### How to Convert a Python project to exe file 
https://www.youtube.com/watch?v=bqNvkAfTvIc
