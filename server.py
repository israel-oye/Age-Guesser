from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/')
# def home():
#     from datetime import datetime
#     c_year = datetime.now().year
#     return render_template("index.html", year = c_year)

@app.route('/guess/<name>')
def name_guesser(name):

    age_end_point = "https://api.agify.io"
    gender_end_point = "https://api.genderize.io"

    params = {
        'name': name,
        }
    
    import requests

    age_response = requests.get(url=age_end_point, params=params).json()
    gender_response = requests.get(url=gender_end_point, params=params).json()

    age = age_response["age"]
    gName = age_response["name"].title()
    gender = gender_response["gender"]
    probability = gender_response["probability"]

    return render_template("index.html", input_name=gName, guessed_age=age, gender=gender, prob=probability)

    





if (__name__ == "__main__"):
    app.run(debug=True)