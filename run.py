from app import app
from app.api.user import views

@app.route('/', methods=['GET'])
def index():
    return "Welcome try the other endpoints in postman, find the repo here https://github.com/hadijahkyampeire/Maintainance-Tracker"


if __name__ == '__main__':

    app.run(debug=True)