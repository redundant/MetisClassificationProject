from flask import Flask, request, render_template
from joblib import load
import numpy as np

app = Flask(__name__)

my_model = load("rfc_model.joblib")

@app.route('/')
def entry_page():
    return render_template('index.html')

"""['top_vs', 'top_mastery', 'first_brick', 'first_blood',
       'first_dragon', 'first_herald',
       'jungle_vs', 'jungle_mastery', 'mid_vs', 'mid_mastery', 'adc_vs',
       'adc_mastery', 'sup_vs', 'sup_mastery']"""

@app.route("/test", methods=["POST"])
def test():

    try:
        print(str(request))
        result = request.form
        all_keys = set(result.keys())

        top_vs = int(request.form["top_vs"])
        jun_vs = int(request.form["jun_vs"])
        mid_vs = int(request.form["mid_vs"])
        adc_vs = int(request.form["adc_vs"])
        sup_vs = int(request.form["sup_vs"])

        top_mastery = int(request.form["top_mastery"])
        jun_mastery = int(request.form["jun_mastery"])
        mid_mastery = int(request.form["mid_mastery"])
        adc_mastery = int(request.form["adc_mastery"])
        sup_mastery = int(request.form["sup_mastery"])
        
        first_blood = "first_blood" in all_keys
        first_brick = "first_brick" in all_keys
        first_dragon = "first_dragon" in all_keys
        first_herald = "first_herald" in all_keys
        
        model_parameters = [top_vs,top_mastery,first_brick,first_blood,first_dragon,first_herald, \
            jun_vs,jun_mastery,mid_vs,mid_mastery,adc_vs,adc_mastery,sup_vs,sup_mastery]

        prediction = my_model.predict(np.reshape(model_parameters,(1,-1)))

        if prediction[0] == False:
            message = "Try focusing on dragons and bottom lane vision."
        
        if prediction[0] == True:
            message = "You are a true winner."

        return render_template("index.html", message = message)
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run()
