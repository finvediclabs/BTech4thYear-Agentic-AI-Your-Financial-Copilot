from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Intentional bug: API key is not set correctly
openai.api_key = None  # BUG: Should be set from environment or config

def ask_financial_question(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are a financial assistant."},
                  {"role": "user", "content": question}]
    )
    return response['choices'][0]['message']['content']

@app.route('/', methods=['GET', 'POST'])
def index():
    answer = None
    if request.method == 'POST':
        question = request.form.get('question')
        if question:
            try:
                answer = ask_financial_question(question)
            except Exception as e:
                answer = f"Error: {str(e)}"
    return render_template('index.html', answer=answer)

if __name__ == '__main__':
    app.run(debug=True)
