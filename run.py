from app import app

@app.route('/', methods=['GET'])
def index():
    return "Welcome"


if __name__ == '__main__':

    app.run(debug=True)