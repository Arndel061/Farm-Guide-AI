from mock_ai import get_remedy

def main():
    print("🌱 Welcome to FarmGuard AI 🌱")
    print("Describe the issue with your farm or crops (e.g., 'My maize has yellowing leaves'):\n")

    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("FarmGuard AI: Goodbye! 👋")
            break

        response = get_remedy(user_input)
        print("FarmGuard AI:", response)

if __name__ == "__main__":
    main()
