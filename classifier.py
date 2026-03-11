def classify_intent(message: str) -> dict:
    msg = message.lower()

    code_keywords = [
        "python","code","function","program","algorithm",
        "sort","list","loop","variable","bug","error"
    ]

    data_keywords = [
        "data","dataset","average","mean","median","statistics"
    ]

    writing_keywords = [
        "rewrite","improve","grammar","sentence","paragraph","writing"
    ]

    career_keywords = [
        "career","job","resume","interview","skills"
    ]

    math_keywords = [
        "solve","equation","math","calculate","algebra","+","-","*","/","="
    ]

    general_keywords = [
        "explain","what","define","concept","theory","machine learning"
    ]

    if any(word in msg for word in code_keywords):
        return {"intent": "code", "confidence": 0.9}

    if any(word in msg for word in data_keywords):
        return {"intent": "data", "confidence": 0.9}

    if any(word in msg for word in writing_keywords):
        return {"intent": "writing", "confidence": 0.9}

    if any(word in msg for word in career_keywords):
        return {"intent": "career", "confidence": 0.9}

    if any(word in msg for word in math_keywords):
        return {"intent": "math", "confidence": 0.9}

    if any(word in msg for word in general_keywords):
        return {"intent": "general", "confidence": 0.8}

    return {"intent": "unclear", "confidence": 0.5}