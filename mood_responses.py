def mood_response(mood):
    mood = mood.lower()
    if mood == "happy":
        return "That's great to hear! Keep smiling! 😊"
    elif mood == "sad":
        return "I'm sorry to hear that. I hope things get better soon. 💖"
    elif mood == "excited":
        return "Awesome! Excitement is contagious! 🎉"
    elif mood == "angry":
        return "Take a deep breath. It's going to be okay. 🧘‍♂️"
    elif mood == "tired":
        return "Make sure to get some rest. You deserve it. 😴"
    else:
        return "That's an interesting mood. I hope you have a good day regardless! 🌟"