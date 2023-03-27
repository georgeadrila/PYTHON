import openai
from langdetect import detect

openai.api_key = "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"

# Initialize conversation history
history = []

# Function to generate a completion
def generate_completion(prompt):
    response = openai.Completion.create(
        engine="davinci-codex",
        prompt=prompt,
        max_tokens=1048,
        temperature=0.5,
        stop=["\n"],
    )
    return response.choices[0].text.strip()


if __name__ == "__main__":
    while True:
        # Get input from the terminal
        user_input = input("You: ")

        # if detect(user_input) != 'en':
        #     print("ChatGPT: Only talk to me in English 😂.")
        #     continue

        # Append user input to conversation history
        history.append(user_input)

        # Generate a completion based on the conversation history
        prompt = "\n".join([f"Q: {h}\nA:" for h in history])
        completion = generate_completion(prompt)

        # Print the completion as the reply from ChatGPT
        print("ChatGPT:", completion)

