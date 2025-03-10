# pip install transformers torch
# 25Gb download!!!

from transformers import AutoModelForCausalLM, AutoTokenizer

# Load pre-trained model and tokenizer
model_name = "EleutherAI/gpt-j-6B"
model = AutoModelForCausalLM.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)


def generate_response(prompt, chat_history=[], max_length=500):
    chat_history.append(prompt)
    inputs = tokenizer.encode(" ".join(chat_history), return_tensors="pt")
    outputs = model.generate(inputs, max_length=max_length, num_return_sequences=1,
                             no_repeat_ngram_size=2, top_p=0.9, temperature=0.6)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    chat_history.append(response)
    return response, chat_history


def chat():
    print("ChatGPT-like Chatbot. Type 'exit' to end the conversation.")
    chat_history = []
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break
        response, chat_history = generate_response(user_input, chat_history)
        print(f"Bot: {response}")


if __name__ == "__main__":
    chat()
