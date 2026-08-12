
from agents import function_tool

from constants import NUM_QUESTIONS

answers = [None] * NUM_QUESTIONS

@function_tool
def record_answer(question_index: int, is_correct: bool) -> None:
    """
    Record the user's answer for a specific question.

    Args:
        question_index (int): The index of the question in the questions list.
        is_correct (bool): Whether the user's answer is correct.
    """
    global answers
    if 0 <= question_index < NUM_QUESTIONS:
        answers[question_index] = is_correct
    else:
        print(f"Invalid question index: {question_index}")

@function_tool
def print_status() -> str:
    """
    Returns a string representing the current status of the quiz, showing which questions have been answered correctly, incorrectly, or not answered yet.
    """
    global answers
    result = ""
    for index in range(NUM_QUESTIONS):
        if index >= len(answers):
            result += "[bold yellow]-[/bold yellow] "
        elif answers[index] == True:
            result += "[bold green]✓[/bold green] "
        elif answers[index] == False:
            result += "[bold red]✗[/bold red] "
        else:
            result += "[bold yellow]-[/bold yellow] "
    return result