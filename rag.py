from pathlib import Path

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


PRODUCT_FILE = Path("data/products.txt")


def load_products():
    loader = TextLoader(
        str(PRODUCT_FILE),
        encoding="utf-8"
    )

    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    return splitter.split_documents(documents)


def search_products(question: str):
    documents = load_products()

    results = []

    for document in documents:
        if any(
            word.lower() in document.page_content.lower()
            for word in question.split()
        ):
            results.append(document.page_content)

    return "\n\n".join(results[:3])