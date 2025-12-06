# app.py
from moodmusic import recommend_music

print("🎵 MoodMusic Recommendation System 🎵")
print("----------------------------------")

mood = input("How are you feeling today? (happy/sad/stressed/energetic/lonely): ")

recommendations = recommend_music(mood)

print("\nHere are your personalized music suggestions:\n")
for song in recommendations:
    print(f"- {song}")

print("\nEnjoy your music! 🎧")
