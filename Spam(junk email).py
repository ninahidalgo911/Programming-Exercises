#List of common spam words
spam_words = [
    "free", "buy now", "click here", "act now", "urgent",
    "winner", "congratulations", "make money", "cash bonus",
    "extra income", "work from home", "guaranteed", "risk free",
    "limited time", "special offer", "order now", "get it now",
    "offer expires", "credit card", "no credit check", "lose weight",
    "free gift", "free offer", "money back", "no obligation",
    "no purchase necessary", "you have been selected", "100% free",
    "while supplies last", "you are a winner"
]

# checks the email for spam word and give a score
def check_spam(message):
    score = 0
    found_words = []

    message = message.lower()

    for word in spam_words:
        if word in message:
            score += 1
            found_words.append(word)

    return score, found_words

#Gives the email a rating based on spam score
def get_rating(score):
    if score <= 2:
        return "Low likelihood of spam"
    elif score <= 5:
        return "Possible spam"
    else:
        return "High likelihood of spam"

#part that asks the user to enter the email message
def main():
    message = input("Enter an email message: ")
#checking message and rating
    score, found_words = check_spam(message)
    rating = get_rating(score)
#displaying results 
    print("\nSpam Score:", score)
    print("Likelihood:", rating)

    print("Spam words/phrases found:")
    for word in found_words:
        print("-", word)


main()