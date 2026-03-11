from logger import log_route


def route_and_respond(intent, message):

    msg = message.lower()

    if intent == "code":

        if "sort" in msg:
            response = """You can sort a list in Python like this:

numbers = [5, 2, 8, 1]
numbers.sort()
print(numbers)
"""

        elif "factorial" in msg:
            response = """Python factorial example:

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
"""

        elif "function" in msg:
            response = """Example Python function:

def greet(name):
    print("Hello", name)

greet("Alice")
"""

        else:
            response = "To write Python code, define functions using the 'def' keyword."

    elif intent == "data":
        response = """Average = (sum of values) / (number of values)

Example:
(10 + 20 + 30) / 3 = 20
"""

    elif intent == "writing":
        response = "Please provide the sentence or paragraph you want me to improve."

    elif intent == "career":
        response = """Job interview tips:
1. Practice coding problems
2. Prepare projects to discuss
3. Review core concepts
4. Practice mock interviews
"""

    elif intent == "math":
        response = "To solve equations, isolate the variable. Example: 5x + 10 = 35 → x = 5."

    elif intent == "general":
        response = "This is a general knowledge question. Provide a clear explanation of the topic."

    else:
        response = "Your request is unclear. Please provide more details."

    log_route(intent, 0.9, message, response)

    return response