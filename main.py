from classifier import classify_intent
from router import route_and_respond


def main():

    print("LLM Prompt Router")
    print("Type 'exit' to quit.\n")

    while True:

        user_input = input("User: ")

        if user_input.lower() == "exit":
            break

        result = classify_intent(user_input)

        intent = result["intent"]
        confidence = result["confidence"]

        print(f"Detected Intent: {intent}")
        print(f"Confidence: {confidence}\n")

        response = route_and_respond(intent, user_input)

        print("Assistant:")
        print(response)
        print()


if __name__ == "__main__":
    main()