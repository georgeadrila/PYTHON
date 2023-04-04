import openai
from langdetect import detect

openai.api_key = "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"

# Function to generate a completion
def generate_completion(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
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

