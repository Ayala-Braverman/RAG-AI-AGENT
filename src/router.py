def route_question(question):

    q = question.lower()

    if "list" in q or "all" in q:
        return "structured"

    if "latest" in q or "recent" in q:
        return "structured"

    return "semantic"