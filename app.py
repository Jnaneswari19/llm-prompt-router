from classifier import classify_intent
from router import route_and_respond
from logger import log_route


def main():

    print("\nLLM Prompt Router Started")
    print("Type 'exit' to quit\n")

    while True:

        message = input("User: ")

        if message.lower() == "exit":
            break

        result = classify_intent(message)

        intent = result["intent"]
        confidence = result["confidence"]

        response = route_and_respond(message, intent)

        print("\nAssistant:", response, "\n")

        log_route(intent, confidence, message, response)


if __name__ == "__main__":
    main()