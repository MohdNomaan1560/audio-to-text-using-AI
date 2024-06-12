# Code
import speech_recognition as sr

def audio_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something:")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Error connecting to Google Speech Recognition service: {e}")
        return None

# Example usage
audio_text = audio_to_text()
print(f"Converted Text: {audio_text}")


# Code
import openai

openai.api_key = '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'

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

# Example usage
chat_output = chat_with_gpt("Convert this text to audio:")
print(f"ChatGPT Output: {chat_output}")

# Code
from gtts import gTTS
import os

def text_to_audio(text):
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")
    os.system("mpg321 output.mp3")  # Use mpg321 or other player of your choice

# Example usage
text_to_audio("This is the ChatGPT response.")

# Code for a basic Tkinter GUI
import tkinter as tk

def on_button_click():
    audio_text = audio_to_text()
    chat_output = chat_with_gpt(audio_text)
    text_to_audio(chat_output)

# Create the main window
window = tk.Tk()
window.title("Audio to Text and ChatGPT")

# Create a button
button = tk.Button(window, text="Start Conversation", command=on_button_click)
button.pack(pady=20)

# Start the GUI event loop
window.mainloop()

