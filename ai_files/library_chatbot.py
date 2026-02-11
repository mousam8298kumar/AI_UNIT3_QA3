import re

def get_response(user_input: str) -> str:
    text = user_input.lower().strip()

    # Exit
    if text in ["bye", "exit", "quit", "goodbye"]:
        return "Thank you for using the Library Assistant. Goodbye!"

    # Greetings
    if re.search(r"\b(hi|hello|hey|good morning|good evening)\b", text):
        return "Hello! How can I help you with library services today?"

    # Library timings
    if re.search(r"\b(timing|library hours|open)\b", text):
        return (
            "The library is open from 9:00 AM to 7:00 PM (Mon–Sat).\n"
            "Sunday is closed."
        )

    # Membership
    if re.search(r"\b(membership|library card|join)\b", text):
        return (
            "To get library membership, please bring a valid ID proof\n"
            "and fill out the membership form at the counter."
        )

    # Book search
    if re.search(r"\b(search book|find book|book availability)\b", text):
        return (
            "You can search for books using the library computer system\n"
            "or ask the librarian for help."
        )

    # Issue book
    if re.search(r"\b(issue book|borrow book|take book)\b", text):
        return (
            "To issue a book, please present your library card\n"
            "at the issue counter."
        )

    # Return book
    if re.search(r"\b(return book|submit book)\b", text):
        return (
            "You can return books at the return counter.\n"
            "Please return on time to avoid fines."
        )

    # Fine enquiry
    if re.search(r"\b(fine|late fee|penalty)\b", text):
        return (
            "Late return fine is ₹2 per day per book.\n"
            "Please clear fines at the counter."
        )

    # Renew book
    if re.search(r"\b(renew|renewal)\b", text):
        return (
            "You can renew books at the counter or through the library system\n"
            "if no one has reserved the book."
        )

    # Default reply
    return (
        "Sorry, I didn't understand that.\n"
        "You can ask about library timings, membership, book search, "
        "issue/return, fine, or renewal."
    )

def library_chatbot():
    print("LibraryBot: Welcome! I am your rule-based Library Assistant 📚")
    print("Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print("LibraryBot:", response)

        if user_input.lower() in ["bye", "exit", "quit"]:
            break

# Run chatbot
library_chatbot()
