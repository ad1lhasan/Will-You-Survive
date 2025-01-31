from flask import Flask, request, render_template
import pickle
import numpy as np

# Initialize the Flask app
app = Flask(__name__)

# Load the pre-trained model and scaler
model = pickle.load(open("model.pkl", "rb"))

@app.route('/')
def home():
    return render_template('index.html', prediction_text='')

@app.route('/predict', methods=['POST'])
def predict():
    
    # Retrieve the input values from the form
    age = float(request.form['age'])
    fare = float(request.form['fare'])
    sibsp = float(request.form['sibsp'])
    parch = float(request.form['parch'])

    # Prepare the input data for prediction
    input_data = np.array([[age, fare, sibsp, parch]])

    
    # Make the prediction
    prediction = model.predict(input_data)

    # Get the predicted class
    result= 'You Survived 🎉🥂' if prediction[0]==1 else 'You DIED 💀☠️'
    prediction_text = f"{result}"

    return render_template('index.html', prediction_text=prediction_text)

if __name__ == "__main__":
    app.run(debug=True)
