from llama_index.core import SimpleDirectoryReader
import os


def load_documents():

    reader = SimpleDirectoryReader(
        input_dir="data",
        required_exts=[".md"],
        recursive=True
    )

    documents = reader.load_data()

    for doc in documents:

        file_path = doc.metadata["file_path"]

        tool_name = os.path.basename(os.path.dirname(file_path))

        file_name = os.path.basename(file_path)

        doc.metadata = {
            "tool": tool_name,
            "file_name": file_name,
            "path": file_path
        }

    return documents


if __name__ == "__main__":

    docs = load_documents()

    print("Number of documents:", len(docs))

    for doc in docs:

        print("\n---- Document ----")
        print(doc.metadata)
        print(doc.text[:200])