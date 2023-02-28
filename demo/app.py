import flask
import pickle
import pandas as pd

# Use pickle to load in the pre-trained model
model = pickle.load(open('model.pkl', 'rb'))

# Initialise the Flask app
app = flask.Flask(__name__, template_folder='templates')

# Set up the main route
@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        # Just render the initial form, to get input
        return(flask.render_template('main.html'))
    
    if flask.request.method == 'POST':
        # Extract the input
        temperature = flask.request.form['temperature']
        humidity = flask.request.form['humidity']
        windspeed = flask.request.form['windspeed']

        HighBP = flask.request.form['HighBP']
        HighChol = flask.request.form['HighChol']
        CholCheck = flask.request.form['CholCheck']
        BMI = flask.request.form['BMI']
        Smoker = flask.request.form['Smoker']
        Stroke = flask.request.form['Stroke']
        HeartDiseaseorAttack = flask.request.form['HeartDiseaseorAttack']
        PhysActivity = flask.request.form['PhysActivity']
        Fruits = flask.request.form['Fruits']
        Veggies = flask.request.form['Veggies']
        HvyAlchoholConsump = flask.request.form['HvyAlchoholConsump']
        AnyHealthcare = flask.request.form['AnyHealthcare']
        NoDocbcCost = flask.request.form['NoDocbcCost']
        GenHlth = flask.request.form['GenHlth']
        MentHlth = flask.request.form['MentHlth']
        PhysHlth = flask.request.form['PhysHlth']
        DiffWalk = flask.request.form['DiffWalk']
        Sex = flask.request.form['Sex']
        Age = flask.request.form['Age']
        Education = flask.request.form['Education']
        Income = flask.request.form['Income']

        # Make DataFrame for model
        input_variables = pd.DataFrame([[temperature, humidity, windspeed]],
                                       columns=['temperature', 'humidity', 'windspeed'],
                                       dtype=float,
                                       index=['input'])

        # Get the model's prediction
        prediction = model.predict(input_variables)[0]
    
        # Render the form again, but add in the prediction and remind user
        # of the values they input before
        return flask.render_template('main.html',
                                     original_input={'Temperature':temperature,
                                                     'Humidity':humidity,
                                                     'Windspeed':windspeed},
                                     result=prediction,
                                     )

if __name__ == '__main__':
    app.run()