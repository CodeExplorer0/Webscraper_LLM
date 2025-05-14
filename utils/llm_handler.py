import ollama

def get_llm_response(file_content, query, model_name):
    prompt = f"File Content:\n{file_content}\n\nUser Query: {query}"
    response = ollama.chat(model=model_name, messages=[{"role": "user", "content": prompt}])
    print("LLM Response:", response['message']['content'])  # Print in terminal
    return response['message']['content']
