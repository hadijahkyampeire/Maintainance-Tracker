from flask import render_template
from app import app
from app.api.user import views

@app.route('/', methods=['GET'])
def index():
    return render_template('welcome.html')


if __name__ == '__main__':

    app.run(debug=True)