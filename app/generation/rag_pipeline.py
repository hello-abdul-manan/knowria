from app.generation.llm import generate_answer

def run_rag(query, retriever):
    """Retrieve documents, build context and generate answer."""

    # Retrieve relevant documents from vector store
    docs = retriever.invoke(query)

    # Combine document contents into a single context string
    context = "\n\n".join(doc.page_content for doc in docs)

    # Create prompt
    prompt = f"""
    Answer the question using the context below:
    
    Context:
    {context}
    
    Question:
    {query}
    """

    # Generate final answer using LLM
    return generate_answer(prompt)
