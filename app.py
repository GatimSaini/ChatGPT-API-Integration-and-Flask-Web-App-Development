from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Homepage route
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        question = request.form['question']
        response = chat(question)
        return render_template('results.html', question=question, response=response)
    return render_template('index.html')

# ChatGPT API call
def chat(question):
    # Make an API call to ChatGPT and return the response
    api_key = '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'
    url = 'https://api.openai.com/v1/chat/completions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {api_key}'
    }
    data = {
        'model': 'gpt-3.5-turbo',
        'messages': [{'role': 'system', 'content': 'You are a helpful assistant.'},
                     {'role': 'user', 'content': question}]
    }
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        result = response.json()
        return result['choices'][0]['message']['content']
    except requests.exceptions.RequestException as e:
        return f'Error: {e}'

if __name__ == '__main__':
    app.run(debug=True)
