from voice_assistant.speech_recognition import listen
from voice_assistant.text_to_speech import speak
import requests

def process_command(command):
    url = 'http://127.0.0.1:5000/command'
    data = {'command': command}
    response = requests.post(url, json=data)
    print(response.json())
    speak(response.json().get('status'))

if __name__ == "__main__":
    while True:
        command = listen()
        if command:
            process_command(command)
