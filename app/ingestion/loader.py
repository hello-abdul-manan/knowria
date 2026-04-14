from langchain_community.document_loaders import PyPDFLoader, TextLoader

def load_document(file_path: str):
    """Load a PDF or text file and return LangChain documents."""

    # Choose loader based on file type
    if file_path.endswith(".pdf"):
        loader = PyPDFLoader(file_path)
    else:
        loader = TextLoader(file_path)

    # Load and return documents
    return loader.load()
