# This code randomly generates surnames for my MemoryLab lesson

from faker import Faker
import random

# Initialize Faker
fake = Faker()

def generate_surnames(char_count, n = 20):
    surnames = set()

    # Generate surnames untill we have enough with the specified character count
    while len(surnames) < n:
        name = fake.last_name()
        if len(name) == char_count:
            surnames.add(name)

    return list(surnames)

# Get the number of characters from the user
char_count = int(input("Enter the number of characters in the surname: "))

# Generate and print the surnames
generated_surnames = generate_surnames(char_count)
print("Generated Surnames:", generated_surnames)