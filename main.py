import os
import openai
from googletrans import Translator
from gtts import gTTS
import playsound

# Load your API key from an environment variable or secret management service
openai.api_key = "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"


def DiscussionEN():
    promptIni = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: "
    request = input(promptIni)
    promptIni += request + "/nAI:"
    while True:
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=promptIni,
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=[" Human:", " AI:"]
        )
        print("\nAI: "+response["choices"][0]["text"]+"\n")
        new = input("Human:")
        promptIni += " " + \
            response["choices"][0]["text"]+"\nHuman: "+new + "\nAI:"


def DiscussionFR():
    translator = Translator()
    promptIni = "The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: "
    request = input(translator.translate(promptIni, dest='fr').text)
    promptIni += translator.translate(request, dest='en').text + "/nAI:"
    while True:
        response = openai.Completion.create(
            model="text-davinci-002",
            prompt=promptIni,
            temperature=0.9,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0.0,
            presence_penalty=0.6,
            stop=[" Human:", " AI:"]
        )
        print(
            "\nAI: "+translator.translate(response["choices"][0]["text"], dest='fr').text+"\n")
        gTTS(text=translator.translate(
            response["choices"][0]["text"], dest='fr').text, lang="fr", slow=False).save("answer.mp3")
        playsound.playsound("answer.mp3", True)
        new = input("Human:")
        promptIni += " " + \
            response["choices"][0]["text"]+"\nHuman: " + \
            translator.translate(new, dest='en').text + "\nAI:"


DiscussionFR()
