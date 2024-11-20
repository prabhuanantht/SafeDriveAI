# Voice Command Model with Word2Vec and Speech Recognition

This project is a Python-based voice-command system that recognizes spoken commands and performs predefined actions. The model uses the Word2Vec embeddings to find semantically similar commands and integrates the Google Speech Recognition API for live audio input.

---

## Features

- **Real-time Speech Recognition**: Listens to voice commands and processes them live.
- **Semantic Matching**: Matches user commands with a predefined set using Word2Vec for similarity scoring.
- **Predefined Commands**: Supports actions such as playing music, controlling volume, and navigating tracks.
- **Volume Control**: Dynamically adjusts the volume with an internal state.

---

## Prerequisites

1. **Python Version**: Ensure you have Python 3.7 or higher.
2. **Dependencies**: Install the following Python libraries:
   ```bash
   pip install gensim speechrecognition
   ```
3. **Microphone**: A working microphone for capturing live audio input.
4. **Internet Connection**: Required for the Google Speech Recognition API and downloading the Word2Vec model.

---

## Setup Instructions

After cloning the repository:
1. **Install Dependencies**:
   ```bash
   cd Speech_Recognition
   ```
2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Script**:
   ```bash
   python voice_command_model.py
   ```

---

## Usage

### Available Commands:
- **Music Playback**:
  - `play music`
  - `pause music`
  - `resume music`
  - `next song`
  - `previous song`

- **Volume Control**:
  - `increase volume`
  - `decrease volume`
  - `mute audio`
  - `unmute audio`

### Steps:
1. Run the script.
2. Speak any of the available commands into the microphone.
3. The system will recognize and execute the closest matching command.

---

## How It Works

1. **Speech Recognition**: Captures and transcribes audio using the Google Speech Recognition API.
2. **Word2Vec Model**: Uses the `word2vec-google-news-300` model from Gensim to compute the semantic similarity between the transcribed command and predefined commands.
3. **Command Execution**: Maps the best-matching command to its corresponding function.

---

## Example Output

1. **Input**: "Play the music"
   - **Output**: "Executing command: play music"
   - **Action**: Prints "Playing music."

2. **Input**: "Turn up the sound"
   - **Output**: "Executing command: increase volume"
   - **Action**: Prints "Increasing volume to 55."

---

## Troubleshooting

- **Audio Not Recognized**:
  - Ensure your microphone is working and not muted.
  - Reduce background noise for better recognition.
  
- **Command Not Found**:
  - If the command is semantically far from the predefined list, it may not match.

- **Google Speech Recognition Error**:
  - Check your internet connection.
  - Retry after some time as the API may face temporary issues.

---

## Future Enhancements

- Add support for custom commands.
- Integrate natural language understanding for more complex interactions.
- Add GUI or voice feedback for better user experience.

---
