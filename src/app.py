import gradio as gr
from workflow import run_workflow


def chat(message, history):
    """
    פונקציית הצ'אט הראשית
    """

    # 🛑 חסימת קלט לא תקין (קריטי!)
    if message is None:
        return "❗ Please enter a valid question."

    if not isinstance(message, str):
        return "❗ Invalid input type."

    if message.strip() == "":
        return "❗ Please enter a valid question."

    # 🔁 הרצת ה-workflow
    response = run_workflow(message)

    return response


# 🎯 ממשק צ'אט
demo = gr.ChatInterface(
    fn=chat,
    title="DocInsight RAG",
    description="Ask questions about your project documentation"
)


if __name__ == "__main__":
    demo.launch()