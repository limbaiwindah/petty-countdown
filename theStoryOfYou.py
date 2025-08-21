from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# 1️⃣ Load model
model_name = "EleutherAI/gpt-neo-2.7B"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Optional: run on GPU if available
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)

# 2️⃣ Initialize base story
base_story = """clouds, time, and i
Guess what my name is.
Because I’m not entirely sure what I am looking at; it floats..."""

# 3️⃣ Start interactive loop
while True:
    # Get user input
    user_input = input("\nTell me about your day: ")

    # Create prompt merging base story + user input
    prompt = f"{base_story}\nUser input: {user_input}\nContinue the story naturally:"

    # Encode prompt
    inputs = tokenizer(prompt, return_tensors="pt").to(device)

    # Generate continuation
    outputs = model.generate(
        **inputs,
        max_new_tokens=150,
        do_sample=True,
        temperature=0.8
    )

    # Decode output
    story_update = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Update base story
    base_story = story_update

    # Show updated story
    print("\n--- Updated Story ---\n")
    print(base_story)
