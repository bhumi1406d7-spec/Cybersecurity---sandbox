import time

# Whitelist approach: only predefined safe operations are permitted
ALLOWED_COMMANDS = ["print", "add", "sub"]


def sandbox_execute(user_input):
    start_time = time.time()

    # Block potentially unsafe keywords to prevent unauthorized system access
    blocked_keywords = ["import", "os", "sys", "while", "for", "open", "exec", "eval"]

    for word in blocked_keywords:
        if word in user_input:
            return "Error: Unauthorized command detected!"

    try:
       # Enforce execution time limit to avoid resource abuse
        if time.time() - start_time > 2:
            return "Error: Time limit exceeded!"

       # Execute only whitelisted commands using controlled logic
        if user_input.startswith("print"):
            msg = user_input[6:]
            return msg

        elif user_input.startswith("add"):
            parts = user_input.split()
            result = int(parts[1]) + int(parts[2])
            return f"Result: {result}"

        elif user_input.startswith("sub"):
            parts = user_input.split()
            result = int(parts[1]) - int(parts[2])
            return f"Result: {result}"

        else:
            # Reject any command outside the allowed set to maintain sandbox integrity
            return "Error: Command not allowed!"

    except Exception:
        return "Error: Invalid input!"


while True:
    user_input = input("Enter command: ")

    if user_input.lower() == "exit":
        print("Exiting sandbox...")
        break

    output = sandbox_execute(user_input)
    print(output)
