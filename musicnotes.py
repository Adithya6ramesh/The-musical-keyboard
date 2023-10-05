import winsound

# Define a dictionary to map note names to frequencies
notes = {
    'C': 261.63,
    'D': 293.66,
    'E': 329.63,
    'F': 349.23,
    'G': 392.00,
    'A': 440.00,
    'B': 493.88
}

# Define a function to play a note for a given duration
def play_note(note, duration):
    frequency = notes[note]
    winsound.Beep(int(frequency), int(duration * 1000))

# Continuous input and play notes until user exits
while True:
    user_input = input("Enter a letter ('Q' to quit): ").upper()
    
    if user_input == 'Q':
        break
    
    if user_input in notes:
        play_note(user_input, 1)  # Play the note for 1 second
    else:
        print("Invalid input. Please enter a valid letter from A to G or 'Q' to quit.")
