"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""

from datetime import date


TESTS = {
    "Basics": [
        {
            "input": [date(2022, 1, 5)],
            "answer": date(2022, 1, 8),
            "explanation": "Wed => Sat"
        },
        {
            "input": [date(2022, 2, 21)],
            "answer": date(2022, 2, 26),
            "explanation": "Mon => Sat"
        },
        {
            "input": [date(2022, 3, 26)],
            "answer": date(2022, 3, 26),
            "explanation": "Sat => Sat"
        },
        {
            "input": [date(2022, 4, 17)],
            "answer": date(2022, 4, 17),
            "explanation": "Sun => Sun"
        },
        {
            "input": [date(2022, 3, 30)],
            "answer": date(2022, 4, 2),
            "explanation": "Sat => Sat"
        },
    ],
    "Extra": [
        {
            "input": [date(2021, 2, 19)],
            "answer": date(2021, 2, 20),
            "explanation": "Fri => Sat"
        },
    ]
}
