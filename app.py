from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
model = pickle.load(open("bank_rf.pkl", "rb"))


@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")




@app.route("/predict", methods = ["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        # Age
        Age = int(request.form["age"])
        # print(Age)

        # Job
        Job = int(request.form["job"])
        # print(Job)
        
        # Education
        Education = int(request.form["education"])
        # print(Education)
        
        # marital
        Marital = int(request.form["marital"])
        # print(Marital)
        
        # Housing loan
        Hosing Loan = int(request.form["housing"])
        # print(Housing Loan)
        
        # Personal Loan
        Personal Loan = int(request.form["loan"])
        # print(Personal Loan)
        
        # Duration
        Duration = int(request.form["duration"])
        # print(Duration)
        
        # Month
        Month = int(request.form["month"])
        # print(Month)


        prediction=model.predict([[
            
            age,
            job,
            education,
            marital,
            housing,
            loan,
            duration,
            month
        ]])

        output=round(prediction[0],2)

        return render_template('home.html',prediction_text="{}".format(output))


    return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=True)
