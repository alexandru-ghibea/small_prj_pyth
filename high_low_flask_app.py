from flask import Flask
import random

secret_number = random.choice(range(0, 10))
print(secret_number)
app = Flask(__name__)


@app.route('/')
def home():
    return "<h1> Guess a number between 0 and 9 </h1>" \
           "<img src='https://media1.giphy.com/media/4JVTF9zR9BicshFAb7/giphy.gif?cid=ecf05e47fcf7aqckgqeym99r8snw2ggv5d7dcrmuo9cs5qsu&rid=giphy.gif&ct=g'>"


@app.route("/<int:number>")
def user_guess(number):
    if number > secret_number:
        return "<h1 style='color: red'> To high. Try again !</h1> " \
               "<img src='https://media2.giphy.com/media/vyTnNTrs3wqQ0UIvwE/200.webp?cid=ecf05e473hzjf5ew3d93k736aqpycm5muwuubtaw3murju2j&rid=200.webp&ct=g'>"
    elif number < secret_number:
        return "<h1 style='color: blue'> To low. Try again </h1> " \
               "<img src='https://media0.giphy.com/media/IevhwxTcTgNlaaim73/200w.webp?cid=ecf05e47yb8hgois809aorcfp2guy3nt0af3tk4pvat8v1bi&rid=200w.webp&ct=g'>"
    elif number == secret_number:
        return "<h1 style=color:purple'> You found me! </h1> " \
               "<img src='https://media1.giphy.com/media/dYZuqJLDVsWMLWyIxJ/200w.webp?cid=ecf05e47w056bf24357jfbhpylsmqkzi5wbgvmbsde2njt8q&rid=200w.webp&ct=g'>"

    else:
        return "<h1 style=color:green'> Please select a number from 0 to 9 only ! </h1>"

if __name__ == "__main__":
    app.run(debug=True)


