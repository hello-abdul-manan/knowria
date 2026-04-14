def get_retriever(vectorstore):
    """Returns a retriever that fetches top 3 relevant documents."""

    # Convert vector store into a retriever with top-k search
    return vectorstore.as_retriever(search_kwargs={"K": 3})
