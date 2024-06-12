import SpeechRecognition as sr
import openai
import pyttsx3

# Initialize recognizer
r = sr.Recognizer()

# OpenAI API key
openai.api_key = "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"

# Use microphone as input source
with sr.Microphone() as source:
    # Listen for audio
    print("Speak now...")
    audio = r.listen(source)

try:
    # Convert speech to text
    text = r.recognize_google(audio)
    print(f"You said: {text}")
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")

# Send text to ChatGPT
response = openai.Completion.create(
    model="text-davinci-003",
    prompt=text,
    temperature=0.7,
    max_tokens=256
)

# Get ChatGPT output
chatgpt_output = response["choices"][0]["text"]
print(f"ChatGPT response: {chatgpt_output}")

# Initialize speech engine
engine = pyttsx3.init()

# Set speech rate and volume
engine.setProperty("rate", 150)
engine.setProperty("volume", 1)

# Convert text to speech
engine.say(chatgpt_output)

# Play the audio
engine.runAndWait()
