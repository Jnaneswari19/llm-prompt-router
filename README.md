
# LLM Prompt Router

A lightweight **Python-based LLM Prompt Router** that classifies user prompts by intent and routes them to specialized AI personas.
The system demonstrates how modern AI applications perform **intent detection, prompt routing, and structured logging**.

---

## Project Overview

This project simulates how AI assistants handle different types of user requests by routing them to specialized expert prompts.

Instead of relying on a single monolithic prompt, the system follows a **two-step architecture**:

1. **Intent Classification** – A lightweight LLM call determines the user's intent.
2. **Prompt Routing** – The system routes the request to a specialized expert persona to generate the response.

This design improves **response quality, scalability, and maintainability** compared to using a single general-purpose prompt.

---

## Features

* Intent classification using a lightweight LLM call
* Prompt routing to specialized expert personas
* Interactive command-line interface (CLI)
* Request logging for monitoring and debugging
* Docker support for containerized execution
* Modular Python project architecture

---

## Supported Intents

| Intent  | Example Input                             |
| ------- | ----------------------------------------- |
| code    | Write a Python function to reverse a list |
| data    | What is the average of 10, 20, 30?        |
| writing | Improve this sentence                     |
| career  | Job interview preparation tips            |
| unclear | Help me                                   |

Each intent is mapped to a **dedicated expert persona prompt**.

---

## Project Structure

```
llm-prompt-router
│
├── app.py              # Main application entry point
├── classifier.py       # LLM intent classification
├── router.py           # Prompt routing logic
├── prompts.py          # Expert persona prompts
├── logger.py           # Request logging
├── test_inputs.py      # Sample prompts for testing
│
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker container configuration
│
├── route_log.jsonl     # Stored interaction logs
├── .env.example        # Environment variable template
├── .gitignore
└── README.md
```

---

## How It Works

The system processes user queries using the following pipeline:

```
User Input
     ↓
LLM Intent Classifier
     ↓
Intent + Confidence Score
     ↓
Prompt Router
     ↓
Expert Persona Prompt
     ↓
LLM Response Generation
     ↓
Log Interaction
```

### Step-by-step workflow

1. The user enters a query.
2. The **intent classifier (LLM)** analyzes the message and determines the intent.
3. The **router selects the corresponding expert persona prompt**.
4. The system generates a response using the LLM.
5. The interaction is **logged for monitoring and debugging**.

---

## Running the Project Locally

### Step 1 — Navigate to the project folder

```
cd llm-prompt-router
```

### Step 2 — Install dependencies

```
pip install -r requirements.txt
```

### Step 3 — Configure environment variables

Create a `.env` file:

```
OPENAI_API_KEY=your_openai_api_key_here
```

### Step 4 — Run the application

```
python app.py
```

---

## Example Interaction

Example CLI session:

```
User: Write a Python function to reverse a list

Detected Intent: code (confidence: 0.94)

Assistant:

def reverse_list(lst):
    return lst[::-1]
```

Exit the program with:

```
exit
```

---

## Logging

All interactions are stored in:

```
route_log.jsonl
```

Example log entry:

```json
{
  "timestamp": "2026-03-11 20:56:38",
  "intent": "code",
  "confidence": 0.94,
  "user_message": "Write a Python function to reverse a list",
  "final_response": "def reverse_list(lst): return lst[::-1]"
}
```

This log file helps track routing decisions and analyze system behavior.

---

## Running with Docker

### Build Docker image

```
docker build -t llm-router .
```

### Run container

```
docker run -it llm-router
```

This allows the application to run in a **portable containerized environment**.

---

## Technologies Used

* Python
* OpenAI API
* Docker
* JSON logging
* Command Line Interface (CLI)

---

## Future Improvements

Possible enhancements include:

* Confidence threshold for intent detection
* Manual intent override (e.g., `@code fix this bug`)
* Web interface using Flask or FastAPI
* Advanced analytics for routing performance
* Integration with additional AI models

---

## Learning Outcomes

This project demonstrates:

* Prompt routing architecture
* LLM-based intent classification
* Modular Python application design
* Logging and observability
* Containerized deployment with Docker

---

## Author

Developed by **Jnaneswari** as a mini LLM routing system project demonstrating how AI systems classify and route user prompts efficiently.

