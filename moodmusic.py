# moodmusic.py
# Simple mood-based music recommendation system

def recommend_music(mood):
    mood = mood.lower()

    playlists = {
        "happy": [
            "Happy – Pharrell Williams",
            "Good Life – OneRepublic",
            "On Top of the World – Imagine Dragons"
        ],
        "sad": [
            "Fix You – Coldplay",
            "Let Her Go – Passenger",
            "Someone Like You – Adele"
        ],
        "stressed": [
            "Weightless – Marconi Union",
            "Breathe – Telepopmusik",
            "Sunset Lover – Petit Biscuit"
        ],
        "energetic": [
            "Can't Stop – Red Hot Chili Peppers",
            "Titanium – David Guetta ft. Sia",
            "Stronger – Kanye West"
        ],
        "lonely": [
            "Talking to the Moon – Bruno Mars",
            "I Want It That Way – Backstreet Boys",
            "Memories – Maroon 5"
        ]
    }

    return playlists.get(mood, ["No playlist available for this mood. Try happy, sad, stressed, energetic, or lonely."])
