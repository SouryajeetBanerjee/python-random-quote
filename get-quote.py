import random

# List of motivational quotes
quotes = [
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. - Winston Churchill",
    "Your time is limited, so don’t waste it living someone else’s life. - Steve Jobs",
    "Hardships often prepare ordinary people for an extraordinary destiny. - C.S. Lewis",
    "Don’t watch the clock; do what it does. Keep going. - Sam Levenson",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt"
]

# Function to generate a random quote
def generate_quote():
    return random.choice(quotes)

# Display the motivational quote
if __name__ == "__main__":
    print("Here is your motivational quote:")
    print(generate_quote())
