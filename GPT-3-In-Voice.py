import speech_recognition as sr
import openai
from gtts import gTTS           #文字を音声に変換
from playsound import playsound #音声を再生
import os

#GPT-3のAPIキーをここに
OPENAI_API_KEY = ''

def play_sound(answer):
    tts = gTTS(text=answer,lang="ja")
    tts.save('voice.mp3')
    playsound("voice.mp3")
    os.remove("voice.mp3")

def send_openai(question):
    # GPT-3のAPIキーを設定する
    openai.api_key = OPENAI_API_KEY

    # GPT-3を使用して文章を生成する
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=question,
        max_tokens=1024,
        temperature=0.5,
    )

    # 生成した文章を表示する
    print("[*]回答")
    texts = ''.join([choice['text'] for choice in response.choices])
    print(texts)
    #play_sound(answer) #回答を音声に変換して再生
    
    
def main():
    while True:
        # 音声を読み込む
        r = sr.Recognizer()
        with sr.Microphone() as source:
            audio = r.listen(source)

        try:
            # 音声を文字列に変換する
            text = r.recognize_google(audio, language='ja-JP')
            print("「",text,"」")
            if "終了" in text:
                break
            send_openai(text)
        except:
            print("[*]音声入力なし")
            pass
    
if __name__ == '__main__':
    main()
