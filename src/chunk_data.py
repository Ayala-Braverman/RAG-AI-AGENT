from llama_index.core.node_parser import SentenceSplitter
from load_data import load_documents


def chunk_documents(documents):

    parser = SentenceSplitter(
        chunk_size=300,
        chunk_overlap=50
    )

    nodes = parser.get_nodes_from_documents(documents)

    return nodes


if __name__ == "__main__":

    docs = load_documents()

    nodes = chunk_documents(docs)

    print("Number of chunks:", len(nodes))

    for node in nodes[:5]:
        print("\n---- Chunk ----")
        print(node.metadata)
        print(node.text)