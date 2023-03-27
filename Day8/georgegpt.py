import openai
from langdetect import detect

openai.api_key = "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"

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

        # Generate a completion based on the user input
        prompt = f"Q: {user_input}\nA:"
        completion = generate_completion(prompt)

        # Print the completion as the reply from ChatGPT
        print("GeorgeGPT:", completion)

