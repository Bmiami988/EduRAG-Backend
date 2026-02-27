from groq import Groq
from app.core.config import GROQ_API_KEY
from app.services.vectorstore_service import get_vectorstore

client = Groq(api_key=GROQ_API_KEY)

def run_rag(question: str, mode: str):

    vectorstore = get_vectorstore()
    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})
    docs = retriever.invoke(question)

    context = "\n\n".join([doc.page_content for doc in docs])

    difficulty_prompt = f"""
    Detect difficulty of this question:
    {question}
    Respond with: beginner, intermediate, or advanced.
    """

    difficulty = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": difficulty_prompt}]
    ).choices[0].message.content.strip()

    final_prompt = f"""
    You are EduRAG Tutor.

    Mode: {mode}
    Difficulty: {difficulty}

    Context:
    {context}

    Question:
    {question}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": final_prompt}]
    )

    return response.choices[0].message.content, difficulty