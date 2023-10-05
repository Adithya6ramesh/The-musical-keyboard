import sounddevice as sd
import numpy as np

# Define some constants
INITIAL_FREQUENCY = 440.0  # A4 reference frequency in Hz
HALF_STEP = 2 ** (1 / 12.0)  # Factor to change frequency by a half step

# Initialize note frequency and octave
current_frequency = INITIAL_FREQUENCY

# Define a function to play a note
def play_note():
    duration = 1.0  # in seconds
    t = np.linspace(0, duration, int(duration * 44100), False)
    audio_data = np.sin(2 * np.pi * current_frequency * t)
    sd.play(audio_data, samplerate=44100)

# Main loop
while True:
    play_note()

    # Decrease frequency for the next note
    current_frequency /= HALF_STEP

    # Wait for user input (press any key)
    input("Press Enter to play the next note...")
