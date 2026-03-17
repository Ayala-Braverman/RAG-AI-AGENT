from load_data import load_documents
import re

def extract_items():

    docs = load_documents()

    items = {
        "decisions": [],
        "rules": [],
        "warnings": []
    }

    for doc in docs:
        text = doc.text

        # -------------------
        # החלטות (Decision)
        # -------------------
        decision_matches = re.findall(
            r"Decision\s+\d+\s+–\s+(.*?)\n(.*?)(?=\n---|\Z)",
            text,
            re.DOTALL
        )

        for title, content in decision_matches:
            items["decisions"].append({
                "title": title.strip(),
                "summary": content.strip()[:200],
                "source": doc.metadata.get("file_name")
            })

        # -------------------
        # חוקים (Rules)
        # -------------------
        if "rule" in text.lower() or "rtl" in text.lower():
            items["rules"].append({
                "rule": "UI must support RTL",
                "scope": "ui",
                "source": doc.metadata.get("file_name")
            })

        # -------------------
        # אזהרות (Warnings)
        # -------------------
        if "sensitive" in text.lower():
            items["warnings"].append({
                "message": "Sensitive component detected",
                "area": "system",
                "severity": "high",
                "source": doc.metadata.get("file_name")
            })

    return items