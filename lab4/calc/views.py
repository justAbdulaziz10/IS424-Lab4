import math

from django.shortcuts import render


def square_view(request, value):
    try:
        num = float(value)
        if int(num) % 2 != 0:
            raise ValueError("Odd number not accepted")

        result = math.sqrt(num)
        message = f"The square root of {int(num)} is {result}"
    except ValueError:
        num = 0
        result = 0
        message = "Even numbers not accepted, showing the result for input 0"

    return render(request, "calc/result.html", {
        "num": num,
        "result": result,
        "message": message
    })
