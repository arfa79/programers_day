import hashlib

# Function to hash the message using SHA-256
def hash_message(message):
    sha256 = hashlib.sha256()
    sha256.update(message.encode('utf-8'))
    return sha256.hexdigest()

#original message
original_message = """
Happy Programmer's Day to my fellow code wizards! 🎉💻
May your code be bug-free, your coffee be strong, and your debugging skills legendary! 🤓🚀 #HappyProgrammersDay #CodeOn
"""

# Hash the message
hashed_message = hash_message(original_message)

# Provide the public key
public_key = "1f5457153c880353b077bc86a9b1974cbb58922e76ca9e0ef5abace3708c1e1b"

# Combine the hashed message and public key
encrypted_message = f"{hashed_message}\n{public_key}"

# Print the encrypted message
print(encrypted_message)
