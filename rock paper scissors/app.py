from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = 'supersecretkey'

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!", 0, 0
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!", 1, 0
    else:
        return "Computer wins!", 0, 1

@app.route('/', methods=['GET', 'POST'])
def play_game():
    if 'user_score' not in session:
        session['user_score'] = 0
    if 'computer_score' not in session:
        session['computer_score'] = 0

    user_score = session['user_score']
    computer_score = session['computer_score']
    result = ''

    if request.method == 'POST':
        if request.form.get('choice'):
            user_choice = request.form['choice']
            computer_choice = random.choice(['rock', 'paper', 'scissors'])
            result, user_points, computer_points = determine_winner(user_choice, computer_choice)
            user_score += user_points
            computer_score += computer_points
            session['user_score'] = user_score
            session['computer_score'] = computer_score
        elif request.path == '/reset':
            session['user_score'] = 0
            session['computer_score'] = 0

    return render_template('index.html', user_score=user_score, computer_score=computer_score, result=result)

@app.route('/reset', methods=['POST'])
def reset_scores():
    session['user_score'] = 0
    session['computer_score'] = 0
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
