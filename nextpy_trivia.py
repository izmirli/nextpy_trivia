"""Trivia Game - next.py course forum's challenge.

Make sure questions.json file is in same directory as this file.
Please install colorama package. Can be done by:
    pip install colorama

Usage:
    python nextpy_trivia.py
"""
import json
import random
import os
import colorama

QUESTIONS_FILE = 'questions.json'
ATTEMPTS = 5
STYLE = {
    'yellow': colorama.Fore.LIGHTYELLOW_EX,
    'cyan': colorama.Fore.LIGHTCYAN_EX,
    'green': colorama.Fore.LIGHTGREEN_EX,
    'red': colorama.Fore.RED,
    'white': colorama.Fore.WHITE,
    'clear': colorama.Style.RESET_ALL,
    'bold': '\033[1m',
}


def read_questions_file(q_file: str) -> list:
    """Read a JSON questions file and return questions data in a list.

    File expected to be in this format:
    * Top-level "questions" key holding a list of questions dictionaries.
    * Each dictionary mast hold (at least) these keys: question, answer, hint.
    * Values of "question" and "hint" will be strings. Value of "answer" will be a list of strings.
    {"questions": [{"question": "", "answer": ["", ...], "hint": ""}, ...]}

    :param q_file: path to the JSON questions file
    :return: a list of dicts
    """
    try:
        with open(q_file, 'r', encoding='utf8') as file_handle:
            data = json.load(file_handle)
    except FileNotFoundError:
        print(style_text(f"Fail to fined a questions file with the name: '{q_file}'", 'red', bold=True))
        print('Make sure it is in the same directory as this file (nextpy_trivia.py)\n')
        raise SystemExit

    return data['questions']


def greet(num_of_questions: int):
    """Print game's opening message.

    :param num_of_questions: the numbers of questions in this game
    :return: None
    """
    clear_screen()
    print(style_text('Wellcome to my next.py trivia game!', 'yellow', bold=True))
    instructions = f"""
You will be asked {num_of_questions} questions. You got up to {ATTEMPTS} attempts to give the right answer.
For each question you can get one clue (which is considered as an attempt).
Goal is to give the right answer with the least number of attempts.
"""
    print(instructions)


def clear_screen():
    """Make system call to clear screen (by OS identification).

    :return: None
    """
    os.system('cls' if os.name == 'nt' else 'clear_screen')  # noqa: S605


def right_answer(given_answer: str, answers: list) -> bool:
    """Check if given answer has one of the right answers in it.

    :param given_answer: the answer to check
    :param answers: list of right answers
    :return: True if a right answer, False otherwise
    """
    for answer in answers:
        if answer.casefold() in given_answer:
            return True

    return False


def run_single_question(q_data: dict, q_num: int) -> int:
    """Handle all interactions of a single question.

    :param q_data: a dict with: question, answer, and clue
    :param q_num: number of this question in the overall game
    :return: number of attempts it took for the right answer, or zero if no more attempts
    """
    attempt = 0
    clue_used = False
    while attempt < ATTEMPTS:
        print(f"\nQuestion #{q_num}: {style_text(q_data['question'], 'cyan')}")
        if not clue_used:
            print('Type "help" for a clue (will be considered as an attempt)')

        while True:
            answer = input(f"Your answer ({attempt + 1}/{ATTEMPTS}): ").strip().casefold()
            if answer == '':
                print("You didn't input anything. Please enter your answer. To quit enter 'exit'")
            elif answer in ('quit', 'exit'):
                print(f"\n{STYLE['bold']}Quitting game{STYLE['clear']}\n")
                raise SystemExit
            else:
                break

        attempt += 1
        if answer in ('help', 'clue', 'hint'):
            if clue_used:
                print("You've already asked for the clue before...")
            print(f"Hint: {q_data['hint']}")
            clue_used = True
            continue
        if right_answer(answer, q_data['answer']):
            print(style_text("You are right! ", 'green', bold=True) +
                  f"({attempt} attempt{'s' if attempt > 1 else ''})")
            return attempt
        else:
            print(f"{STYLE['red']}Wrong answer{STYLE['clear']}{' try again' if attempt < ATTEMPTS else ''}")

    print(style_text(f"You failed to give the right answer in {ATTEMPTS} attempts", 'red', bold=True))
    return 0


def end_game(results: list):
    """Print end game message with a final score.

    :param results: the number of attempts for each question
    :return: None
    """
    unanswered_questions = results.count(0)
    overall_attempts = sum(results)
    avg_attempts_per_q = (overall_attempts + unanswered_questions * 10) / len(results)
    score = 10 - avg_attempts_per_q if unanswered_questions else 11 - avg_attempts_per_q
    score_color = 'red' if score < 6 else 'white'
    if score >= 9:
        score_color = 'green'
    print(style_text('\n -= Game Over =- ', 'yellow', bold=True))
    print(f"You answered {len(results) - unanswered_questions} out of {len(results)} questions.")
    print(style_text(f"Your score is: {score:.1f} (max is 10)", score_color, bold=True))


def style_text(text: str, color: str, bold: bool = False) -> str:
    """Style the given text with colorama.

    :param text: the text to style
    :param color: the color to use
    :param bold: true if style should be bold
    :return: the styled text
    """
    style = STYLE['bold'] if bold else ''
    style += STYLE[color]
    return style + text + STYLE['clear']


def main():
    """Pre-game setup & main loop.

    :return: None
    """
    colorama.init()
    questions_data = read_questions_file(QUESTIONS_FILE)
    random.shuffle(questions_data)
    greet(len(questions_data))

    results = []
    for i, q_data in enumerate(questions_data):
        result = run_single_question(q_data, i + 1)
        results.append(result)

    end_game(results)


if __name__ == '__main__':
    main()
