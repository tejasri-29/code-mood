from textblob import TextBlob
import random

challenges = {
    "positive": ["Build a weather app", "Create a portfolio website", "Design a fun JS game"],
    "neutral": ["Implement a stack in Python", "Practice string manipulation", "Solve a binary tree problem"],
    "negative": ["Take a break and build a simple to-do app", "Write a motivational quote generator", "Do an easy HTML project"]
}

mood_input = input("How are you feeling today? (Text or emoji): ")
mood = TextBlob(mood_input).sentiment.polarity

if mood > 0.1:
    mood_type = "positive"
elif mood < -0.1:
    mood_type = "negative"
else:
    mood_type = "neutral"

suggestion = random.choice(challenges[mood_type])
print(f"\nYou're feeling {mood_type}. Here's a coding challenge:\n👉 {suggestion}")
