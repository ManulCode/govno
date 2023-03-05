from flask import Flask, render_template, request
import markovify
import random

app = Flask(__name__)


def train_model():
    with open('database.txt', 'r') as f:
        text = f.read()
    return markovify.Text(text)


text_model = train_model()


def log_request(user_input):
    with open('database.txt', 'a') as f:
        f.write(user_input + '\n')


@app.route('/', methods=['GET', 'POST'])
def index():
    bot_output = ""
    if request.method == 'POST':
        user_input = request.form['user_input']
        log_request(user_input)
        while not bot_output:
            try:
                
                n_words = random.randint(1, 10)
                
                bot_output = ' '.join(text_model.make_short_sentence(100, tries=100, max_words=n_words).split())
            except:
                
                pass
    return render_template('index.html', bot_output=bot_output)

if __name__ == '__main__':
    app.run(port=3000, host="0.0.0.0")
