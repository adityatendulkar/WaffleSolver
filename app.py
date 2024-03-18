from flask import Flask, render_template
from waffle import Waffle


app = Flask(__name__)

# Create a sample waffle
waffle = Waffle(5, 5)
waffle.set_item(0, 0, 'S', 'right')
waffle.set_item(1, 1, 'E', 'position')
waffle.set_item(2, 2, 'X', 'wrong')



@app.route('/')
def display_waffle():
    return render_template('waffle.html', waffle=waffle)

if __name__ == '__main__':
    app.run(debug=True)