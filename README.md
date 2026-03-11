# LLM Prompt Router

A lightweight **Python-based LLM Prompt Router** that classifies user prompts by intent and routes them to the appropriate response module.
The system demonstrates how real-world AI systems perform **intent detection, routing, and logging**.

---

# Project Overview

This project simulates how AI assistants route different types of user queries to specialized handlers.

The router analyzes user input and classifies it into different intents such as:

* Code related questions
* Data analysis queries
* Writing or grammar improvement
* Career advice
* Mathematical reasoning
* General knowledge questions

After detecting the intent, the router generates a relevant response and logs the interaction.

---

# Features

* Intent classification using keyword matching
* Routing system for different prompt categories
* Interactive command-line interface (CLI)
* Request logging for monitoring and debugging
* Docker support for containerized execution
* Modular Python architecture

---

# Supported Intents

| Intent  | Example Input                   |
| ------- | ------------------------------- |
| Code    | Write a Python function         |
| Data    | What is the average of 10 20 30 |
| Writing | Improve this sentence           |
| Career  | Job interview tips              |
| Math    | Solve 5x + 10 = 35              |
| General | Explain machine learning        |

---

# Project Structure

```
llm-router-project
│
├── app.py              # Application setup
├── main.py             # CLI interface
├── classifier.py       # Intent classification logic
├── router.py           # Response routing
├── logger.py           # Request logging
├── prompts.py          # Prompt templates
│
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker container configuration
│
├── test_inputs.txt     # Sample prompts for testing
├── route_log.jsonl     # Stored interaction logs
│
├── .env.example        # Environment variable template
├── .gitignore
└── README.md
```

---

# How It Works

The router processes user queries using the following pipeline:

```
User Input
     ↓
Intent Classifier
     ↓
Router
     ↓
Generate Response
     ↓
Log Interaction
```

1. The user enters a query.
2. The classifier determines the query intent.
3. The router selects the appropriate response module.
4. The response is returned to the user.
5. The interaction is logged for monitoring.

---

# Running the Project Locally

### Step 1 — Navigate to the project folder

```
cd llm-router-project
```

### Step 2 — Install dependencies

```
pip install -r requirements.txt
```

### Step 3 — Run the application

```
python main.py
```

### Step 4 — Interact with the router

Example:

```
User: Write a Python function to reverse a list

Detected Intent: code

Assistant:

def reverse_list(lst):
    return lst[::-1]
```

Exit the program with:

```
exit
```

---

# Running with Docker

### Build the Docker image

```
docker build -t llm-router .
```

### Run the container

```
docker run -it llm-router
```

---

# Example Usage

Example session:

```
User: Solve 5x + 10 = 35

Detected Intent: math

Assistant:

5x + 10 = 35
5x = 25
x = 5
```

---

# Logging

All interactions are stored in:

```
route_log.jsonl
```

Example log entry:

```json
{
  "timestamp": "2026-03-11 20:56:38",
  "intent": "math",
  "confidence": 0.9,
  "message": "Solve: 5x + 10 = 35",
  "response": "x = 5"
}
```

This log helps analyze system behavior and improve routing performance.

---

# Technologies Used

* Python
* Docker
* JSON logging
* Command Line Interface (CLI)

---

# Future Improvements

Possible enhancements include:

* Integrating a real LLM API
* Using machine learning for intent classification
* Adding more routing modules
* Building a web-based interface
* Creating analytics dashboards

---

# Learning Outcomes

This project demonstrates:

* Prompt routing architecture
* Intent classification techniques
* Modular Python application design
* Logging and monitoring
* Containerized deployment with Docker

---


# Author

Developed by **Jnaneswari** as a mini LLM routing system project demonstrating how AI systems classify and route user prompts efficiently.
---

