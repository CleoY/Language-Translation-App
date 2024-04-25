from openai import OpenAI
from flask import Flask

app = Flask(__name__)
client = OpenAI()

@app.route("/hello/")
def hello():
  return "Hi"

# user_input = '''
# Review "我很恨喜歡蘋果。"
# '''

@app.route("/translate/")
# def translate(user_input):
def translate():
  translationSetup = '''
  For all of the following commands, please give results in the specified JSON formats.
  When I type "Translate x to English", I want you to translate x into English, giving me the pinyin, English definition, and 1 example sentence in traditional Chinese with English translations. JSON list: pinyin, English_definition, exSentenceChinese, sentencePinyin, translation.
  When I type "Translate x to Chinese", I want you to translate x into traditional Chinese, giving me the characters, pinyin, synonyms, and 1 example sentence for the Chinese word with English translations. JSON list: characters, pinyin, synonyms, exSentenceChinese, sentencePinyin, translation.
  When I type "Review x", I want you to make any necessary corrections to my grammar and spelling, or even give me suggestions for a better way to say what I mean. JSON list: original, corrected, suggestionNotes.
  '''
  user_input = '''
    Review "我很恨喜歡蘋果。"
    '''

  chat_completion = client.chat.completions.create(
      messages=[{
          "role": "system",
          "content": translationSetup
      }, {
          "role": "assistant",
          "content": user_input
      }],
      response_format={"type": "json_object"},
      model="gpt-4-1106-preview")

  result = chat_completion.choices[0].message.content
  print(result)
  return result



app.run()
# app.run(host="0.0.0.0", port=8000)