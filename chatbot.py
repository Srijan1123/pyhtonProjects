import openai

# Your valid OpenAI API key here (keep it secret!)
openai.api_key = "sk-hiKLThWZFcPhDpYhZst5chm3lk5dZfUzMncdudBss29xu5I2k0D1s5mGKD9JQmNsOEplMMxD4BPjT3BlbkFJCTKhqSyfq1k-dUSc7UVOAe7AHxNxCI7-d3nEom4UMPDsRMQA4ifx2M1Y3n6CMeGzPBHjKz6LoA"

class ProChatBot:
    def __init__(self):
        self.conversation = []

    def ask(self, user_input):
        self.conversation.append({"role": "user", "content": user_input})

        try:
            response = openai.chat.completions.create(
                model="gpt-3.5-turbo",  # changed from gpt-4 to gpt-3.5-turbo
                messages=self.conversation,
                max_tokens=500,
                temperature=0.7,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0.6,
            )
            reply = response.choices[0].message.content
            self.conversation.append({"role": "assistant", "content": reply})
            return reply

        except Exception as e:
            if "401" in str(e) or "invalid_api_key" in str(e):
                return "Authentication failed: Invalid API key. Please check your key."
            return f"An error occurred: {e}"

def main():
    bot = ProChatBot()
    print("ProChatBot: Hi! I'm your AI assistant. Ask me anything or type 'exit' to quit.")

    while True:
        user_input = input("You: ").strip()
        if user_input.lower() in {"exit", "quit", "bye"}:
            print("ProChatBot: Goodbye! Have a great day.")
            break

        reply = bot.ask(user_input)
        print(f"ProChatBot: {reply}\n")

if __name__ == "__main__":
    main()
