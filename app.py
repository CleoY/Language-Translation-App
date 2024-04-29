from openai import OpenAI
from flask import Flask, render_template, request
import json

app = Flask(__name__)
client = OpenAI()

@app.route('/')
def home():
  return render_template('home.html')

def translate(prompt, keyword):
  translationSetup = '''
  For the following command, please give results in the specified JSON formats. Any and all Chinese should be traditional characters.
  ''' + prompt
  
  user_input = request.form['user_input']

  chat_completion = client.chat.completions.create(
    messages=[{
      "role": "system",
      "content": translationSetup
    }, {
      "role": "assistant",
      "content": keyword + user_input
    }],
    response_format={"type": "json_object"},
    model="gpt-4-1106-preview"
  )
  result = chat_completion.choices[0].message.content
  result =  json.loads(result)
  return result, user_input


@app.route('/ChineseToEnglish', methods = ['POST'])
def translateChineseToEnglish():
  prompt = '''When I type "Translate x to English", I want you to translate x into English, giving me the pinyin, English definition, and 1 example sentence in traditional Chinese with English translations. JSON list: characters, pinyin, English_definition, exSentenceChinese, sentencePinyin, translation.'''
  result, user_input = translate(prompt, "Translate")
  return render_template("translate.html", user_input=user_input, chat_response=result, ChineseToEnglish = True)


@app.route('/EnglishToChinese', methods = ['POST'])
def translateEnglishToChinese():
  prompt = '''When I type "Translate x to Chinese", I want you to translate x into traditional Chinese, repeating the original English word, giving me the characters, pinyin, synonyms, synonym translations, and 1 example sentence for the Chinese word with English translations. JSON list: original, characters, pinyin, synonyms, synonymTranslations, synonymPinyin, exSentenceChinese, sentencePinyin, translation.'''
  result, user_input = translate(prompt, "Translate")
  return render_template("translate.html", user_input=user_input, chat_response=result, ChineseToEnglish = False)


@app.route('/review', methods = ['POST'])
def review():
  prompt = '''When I type "Review x", I want you to make any necessary corrections to my grammar and spelling, or even give me suggestions for a better way to say what I mean. JSON list: original, corrected, suggestionNotes.'''
  result, user_input = translate(prompt, "Review")
  return render_template("review.html", user_input=user_input, chat_response=result)


if __name__ == '__main__':
  app.run(debug=True)