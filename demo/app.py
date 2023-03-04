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
    Print('Hi')
    if flask.request.method == 'POST':
        # Extract the input
        
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
        input_variables = pd.DataFrame([[HighBP, HighChol, CholCheck, BMI, Smoker, Stroke, HeartDiseaseorAttack, PhysActivity, Fruits, Veggies, HvyAlchoholConsump, AnyHealthcare, NoDocbcCost, GenHlth, MentHlth, PhysHlth, DiffWalk, Sex, Age, Education, Income]],
                                       columns=['HighBP', 'HighChol', 'CholCheck', 'BMI', 'Smoker', 'Stroke', 'HeartDiseaseorAttack', 'PhysActivity', 'Fruits', 'Veggies', 'HvyAlchoholConsump', 'AnyHealthcare', 'NoDocbcCost', 'GenHlth', 'MentHlth', 'PhysHlth', 'DiffWalk', 'Sex', 'Age', 'Education', 'Income'],
                                       dtype=float,
                                       index=['input'])

        # Get the model's prediction
        prediction = model.predict(input_variables)[0]
    
        # Render the form again, but add in the prediction and remind user
        # of the values they input before
        return flask.render_template('main.html',
                                     original_input={'HighBP': HighBP,
                                                     'HighChol':HighChol,
                                                     'BMI': BMI,
                                                     'Smoker': Smoker,
                                                     'Stroke': Stroke,
                                                     'HeartDiseaseorAttack': HeartDiseaseorAttack,
                                                     'PhysActivity':PhysActivity,
                                                     'Fruits': Fruits,
                                                     'Veggies': Veggies,
                                                     'HvyAlchoholConsump': HvyAlchoholConsump,
                                                     'AnyHealthcare': AnyHealthcare,
                                                     'NoDocbcCost':NoDocbcCost,
                                                     'GenHlth': GenHlth,
                                                     'MentHlth': MentHlth,
                                                     'PhysHlth': PhysHlth,
                                                     'DiffWalk': DiffWalk,
                                                     'Sex':Sex,
                                                     'Age': Age, 
                                                     'Education':Education,
                                                     'Income':Income},
                                     result=prediction,
                                     )

if __name__ == '__main__':
    app.run()
    