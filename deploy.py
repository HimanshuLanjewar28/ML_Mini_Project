from flask import Flask, render_template, request 
import pickle

app = Flask(__name__)

#load the model
model = pickle.load(open('student_performance_Predictor.sav', 'rb'))

@app.route('/')
def home():
    result = ''
    return render_template('index.html', **locals())


@app.route('/predict', methods=['POST', 'GET'])
def predict():
    gender = int(request.form['gender'])
    race_ethnicity = int(request.form['race_ethnicity'])
    parental_level_of_education = int(request.form['parental_level_of_education'])
    lunch = int(request.form['lunch'])
    test_preparation_course = int(request.form['test_preparation_course'])
    
    result = model.predict([[gender, race_ethnicity, parental_level_of_education, lunch, test_preparation_course]]) [0].round(2)
    return render_template('index.html', **locals())


if __name__ == '__main__':
    app.run(debug=True)