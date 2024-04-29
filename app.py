from openai import OpenAI
from flask import Flask, render_template, request

app = Flask(__name__)
client = OpenAI()

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/translate', methods=['POST'])
def translate():
  translationSetup = '''
  For all of the following commands, please give results in the specified JSON formats.
  When I type "Translate x to English", I want you to translate x into English, giving me the pinyin, English definition, and 1 example sentence in traditional Chinese with English translations. JSON list: pinyin, English_definition, exSentenceChinese, sentencePinyin, translation.
  When I type "Translate x to Chinese", I want you to translate x into traditional Chinese, giving me the characters, pinyin, synonyms, and 1 example sentence for the Chinese word with English translations. JSON list: characters, pinyin, synonyms, exSentenceChinese, sentencePinyin, translation.
  When I type "Review x", I want you to make any necessary corrections to my grammar and spelling, or even give me suggestions for a better way to say what I mean. JSON list: original, corrected, suggestionNotes.
  '''
  user_input = request.form['user_input']
  # You can use the user_input here to send it to the GPT-3 model
  # For example:
  chat_completion = client.chat.completions.create(
    messages=[{
        "role": "system",
        "content": translationSetup
    }, {
        "role": "assistant",
        "content": user_input
    }],
    response_format={"type": "json_object"},
    model="gpt-4-1106-preview"
  )
  result = chat_completion.choices[0].message.content
  return render_template('home.html', user_input=user_input, chat_response=result)

if __name__ == '__main__':
    app.run(debug=True)

# from openai import OpenAI
# from flask import Flask, render_template, request

# app = Flask(__name__)
# client = OpenAI()

# @app.route('/hello/')
# @app.route('/hello/<name>')
# def hello(name=None):
#     return render_template('hello.html', name=name)

# # @app.route("/hello/")
# # def hello():
# #   return "Hi"

# user_input = '''
# Review "我很恨喜歡蘋果。"
# '''

# @app.route('/')
# def homePage():
#    return render_template('home.html')


# @app.route('/go', methods=['POST'])
# def chat():
#   user_input = request.form['user_input']
#   # You can use the user_input here to send it to the GPT-3 model
#   translationSetup = '''
#   For all of the following commands, please give results in the specified JSON formats.
#   When I type "Translate x to English", I want you to translate x into English, giving me the pinyin, English definition, and 1 example sentence in traditional Chinese with English translations. JSON list: pinyin, English_definition, exSentenceChinese, sentencePinyin, translation.
#   When I type "Translate x to Chinese", I want you to translate x into traditional Chinese, giving me the characters, pinyin, synonyms, and 1 example sentence for the Chinese word with English translations. JSON list: characters, pinyin, synonyms, exSentenceChinese, sentencePinyin, translation.
#   When I type "Review x", I want you to make any necessary corrections to my grammar and spelling, or even give me suggestions for a better way to say what I mean. JSON list: original, corrected, suggestionNotes.
#   '''
  
#   chat_completion = client.chat.completions.create(
#     messages=[{
#         "role": "system",
#         "content": translationSetup
#     }, {
#         "role": "assistant",
#         "content": user_input
#     }],
#     response_format={"type": "json_object"},
#     model="gpt-4-1106-preview"
#   )

#   result = chat_completion.choices[0].message.content
  
#   # chat_response = response.choices[0].text.strip()
#   return render_template('home.html', user_input=user_input, chat_response=result)


# if __name__ == '__main__':
#     app.run(debug=True)


# # @app.route("/results/<user_input>")
# # # def translate(user_input):
# # def translate(user_input):
# #   translationSetup = '''
# #   For all of the following commands, please give results in the specified JSON formats.
# #   When I type "Translate x to English", I want you to translate x into English, giving me the pinyin, English definition, and 1 example sentence in traditional Chinese with English translations. JSON list: pinyin, English_definition, exSentenceChinese, sentencePinyin, translation.
# #   When I type "Translate x to Chinese", I want you to translate x into traditional Chinese, giving me the characters, pinyin, synonyms, and 1 example sentence for the Chinese word with English translations. JSON list: characters, pinyin, synonyms, exSentenceChinese, sentencePinyin, translation.
# #   When I type "Review x", I want you to make any necessary corrections to my grammar and spelling, or even give me suggestions for a better way to say what I mean. JSON list: original, corrected, suggestionNotes.
# #   '''
# # #   user_input = '''
# # #     Review "我很恨喜歡蘋果。"
# # #     '''

# #   chat_completion = client.chat.completions.create(
# #       messages=[{
# #           "role": "system",
# #           "content": translationSetup
# #       }, {
# #           "role": "assistant",
# #           "content": user_input
# #       }],
# #       response_format={"type": "json_object"},
# #       model="gpt-4-1106-preview")

# #   result = chat_completion.choices[0].message.content
# #   print(result)
# #   return result



# # app.run(debug=True)
# # # app.run(host="0.0.0.0", port=8000)