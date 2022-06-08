from validator_collection import checkers

email = input("What's your email address? ")
print("Valid" if checkers.is_email(email) else "Invalid")