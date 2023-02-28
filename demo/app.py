import flask
import pickle
import pandas as pd

pickled_model = pickle.load(open('model.pkl', 'rb'))
#pickled_model.predict(X_test)