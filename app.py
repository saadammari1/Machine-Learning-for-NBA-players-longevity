# coding=utf-8
from flask import Flask, request, redirect,render_template
from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import os
import pickle

app = Flask(__name__)

#loading data and fitting the MinMaxScaler 
df = pd.read_csv("nba_logreg.csv")
df=df.fillna(0.0)

selected_features=['GP', 'MIN', 'PTS', 'FGM','FGA','FG%','FTM','FTA','FT%','OREB','DREB','REB','AST','STL','BLK','TOV']
data= df[selected_features].values
scaler=MinMaxScaler()
dt = scaler.fit_transform(data)

# Loading the trained model
with open('modele_lda.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/')   
def get():
        return render_template('index.html')

@app.route('/predict',methods=['POST'])   
def predict():
        try:
            Input_data = [float(x) for x in request.form.values()]
            X=scaler.transform([Input_data])

            prediction = model.predict(X)

            if prediction == 1:
                    prediction_output = 'Invest !! this player will last for at least 5 years'
            else : 
                    prediction_output = 'Do not invest !! this player will not last for 5 years'

            return render_template("index.html", prediction_text= prediction_output)

        except ValueError as exc:
            return {'error': str(exc)}, 400

        except Exception as error:
            return {'error': str(error)}, 500


if __name__ == "__main__":
    app.run(port=5000,debug=True)
