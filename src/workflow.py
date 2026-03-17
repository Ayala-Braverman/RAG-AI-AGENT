from pinecone_index import create_pinecone_index
from router import route_question
from extract_data import extract_items

print("Loading index...")
index = create_pinecone_index()
query_engine = index.as_query_engine()

# טעינת הנתונים המובנים פעם אחת
structured_data = extract_items()


# ---------------------------
# Validation
# ---------------------------
def validate_question(question):

    if question is None:
        return False, None

    if not isinstance(question, str):
        return False, None

    if question.strip() == "":
        return False, None

    return True, question.strip()


# ---------------------------
# Semantic Retrieve
# ---------------------------
def retrieve(question):

    response = query_engine.query(question)
    return response


# ---------------------------
# Generate Answer (RAG)
# ---------------------------
def generate_answer(response):

    answer = str(response)

    # הוספת מקורות
    sources = []

    if hasattr(response, "source_nodes"):
        for node in response.source_nodes:
            meta = node.metadata
            source = f"{meta.get('tool')} / {meta.get('file_name')}"
            sources.append(source)

    sources_text = "\n".join(set(sources))

    final_answer = answer + "\n\nSources:\n" + sources_text

    return final_answer


# ---------------------------
# Structured Handler
# ---------------------------
def handle_structured_query(question):

    q = question.lower()

    # 📊 החלטות
    if "decision" in q:
        decisions = structured_data.get("decisions", [])

        if not decisions:
            return "No decisions found."

        return "\n\n".join([
            f"- {d['summary']} ({d['source']})"
            for d in decisions
        ])

    # 📏 חוקים
    if "rule" in q or "rtl" in q:
        rules = structured_data.get("rules", [])

        if not rules:
            return "No rules found."

        return "\n\n".join([
            f"- {r['rule']} ({r['source']})"
            for r in rules
        ])

    # ⚠️ אזהרות
    if "warning" in q or "sensitive" in q:
        warnings = structured_data.get("warnings", [])

        if not warnings:
            return "No warnings found."

        return "\n\n".join([
            f"- {w['message']} ({w['source']})"
            for w in warnings
        ])

    return "No structured data found."


# ---------------------------
# Main Workflow
# ---------------------------
def run_workflow(question):

    print("Step: validation")

    is_valid, clean_question = validate_question(question)
    if not is_valid:
        return "❗ Please enter a valid question."

    print("Step: routing")

    route = route_question(clean_question)

    # 🔵 Structured path
    if route == "structured":
        print("Using structured data")
        return handle_structured_query(clean_question)

    # 🟢 Semantic path (RAG)
    print("Using semantic search")

    response = retrieve(clean_question)

    print("Step: generate answer")

    return generate_answer(response)