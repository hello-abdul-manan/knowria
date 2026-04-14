from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_documents(documents):
    """Split documents into smaller chunks for processing."""

    # Create text splitter
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

    # Split and return documents
    return splitter.split_documents(documents)
