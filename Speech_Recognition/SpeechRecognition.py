import gensim.downloader as api
import speech_recognition as sr

# Load the Word2Vec model (this may take a while on the first run)
print("Loading word2vec model...")
word2vec = api.load("word2vec-google-news-300")

# Global variable for volume control
current_volume = 50

# Command functions
def play_music():
    print("Playing music.")

def pause_music():
    print("Pausing music.")

def resume_music():
    print("Resuming music.")

def next_song():
    print("Skipping to the next song.")

def previous_song():
    print("Going back to the previous song.")

def increase_volume():
    global current_volume
    current_volume = min(100, current_volume + 5)
    print(f"Increasing volume to {current_volume}.")

def decrease_volume():
    global current_volume
    current_volume = max(0, current_volume - 5)
    print(f"Decreasing volume to {current_volume}.")

def mute_audio():
    print("Muting audio.")

def unmute_audio():
    print("Unmuting audio.")

# Command list and function mapping
commands = [
    "play music",
    "pause music",
    "resume music",
    "next song",
    "previous song",
    "increase volume",
    "decrease volume",
    "mute audio",
    "unmute audio",
]

command_map = {
    "play music": play_music,
    "pause music": pause_music,
    "resume music": resume_music,
    "next song": next_song,
    "previous song": previous_song,
    "increase volume": increase_volume,
    "decrease volume": decrease_volume,
    "mute audio": mute_audio,
    "unmute audio": unmute_audio,
}

# Find the closest command based on similarity
def find_closest_command(recognized_command):
    best_command = None
    highest_similarity = -1
    for target_command in commands:
        try:
            similarity = word2vec.n_similarity(recognized_command.split(), target_command.split())
            if similarity > highest_similarity:
                highest_similarity = similarity
                best_command = target_command
        except KeyError:
            continue
    return best_command

# Execute the recognized command
def execute_command(recognized_command):
    closest_command = find_closest_command(recognized_command)
    if closest_command:
        print(f"Executing command: {closest_command}")
        function = command_map.get(closest_command)
        if function:
            function()
    else:
        print("No similar command found.")

# Recognize speech and process commands in real-time
def recognize_and_execute_live():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    print("Listening for live commands... Press 'Ctrl+C' to stop.")

    while True:
        try:
            with microphone as source:
                recognizer.adjust_for_ambient_noise(source)
                print("Say a command:")
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)

            command_text = recognizer.recognize_google(audio)
            print("Recognized command:", command_text)
            execute_command(command_text)
        except sr.UnknownValueError:
            print("Could not understand the audio. Try again.")
        except sr.RequestError as e:
            print(f"Request error from Google Speech Recognition service; {e}")
        except Exception as ex:
            print(f"Error: {ex}")

# Run the live command recognizer
recognize_and_execute_live()
