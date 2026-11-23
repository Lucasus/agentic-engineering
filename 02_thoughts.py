import sys
from llm import llm, print_generation_speed


def add(a, b):      return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b):   return a / b

tools = {"add": add, "subtract": subtract, "multiply": multiply, "divide": divide}

system_message = """add(a: number, b: number) -> number
subtract(a: number, b: number) -> number
multiply(a: number, b: number) -> number
divide(a: number, b: number) -> number
Use tools for every arithmetic operation, one call at a time.
Arguments must be literal numbers, never expressions or nested tool calls.
Wait for TOOL_OUTPUT. Never invent results.
Start with a short THOUGHT about the solution, then use tools. Do not repeat thoughts.
When the tool results answer the question, finish with OUTPUT.
Reply with exactly one line using exactly one of these formats, no Markdown:
THOUGHT: <brief next step, at most 12 words>
TOOL: add(2, 3)
OUTPUT: <answer>
"""


def parse_call(text):
    name, args = text.strip().split("(", 1)
    return name.strip(), [float(arg) for arg in args.split(")", 1)[0].split(",")]


def agent(user_task):
    context = [system_message, "USER: " + user_task]
    print(context[-1])
    while True:
        reply = llm(context)
        context.append(reply)
        print(reply)
        if reply.startswith("OUTPUT:"):
            return reply.removeprefix("OUTPUT:").strip()
        if reply.startswith("THOUGHT:"):
            continue
        try:
            name, args = parse_call(reply.removeprefix("TOOL:"))
            result = tools[name](*args)
        except (ValueError, KeyError, TypeError, ZeroDivisionError) as error:
            result = f"Error: {error}. Use one tool call with two numbers."
        context.append(f"TOOL_OUTPUT: {result}")
        print(context[-1])


if __name__ == "__main__":
    agent(" ".join(sys.argv[1:]) or
          "17 red boxes and 25 blue boxes, with 3 items in each. How many items are there?")
    print_generation_speed()
