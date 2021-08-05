# import a library  
from flask import Flask,render_template,request
import joblib

# instace of an app
app=Flask(__name__)

model=joblib.load('dib_79.pkl')

@app.route('/')
def hello():
    return "Welcome"

@app.route('/home')
def homepage():
    return render_template("home.html")

@app.route('/welcome')
def welcomepage():
    return render_template("welcome.html")

@app.route('/bologs')
def bologspage():
    return render_template("bologs.html")

@app.route('/home/diabetic')
def d1():
    return render_template("diabetic.html")

@app.route('/home/bmi')
def d2():
    return render_template("bmi.html")

@app.route('/home/bmr')
def d3():
    return render_template("bmr.html")

#Diabetic Code Start
@app.route('/blog1',methods=['POST'])
def contact1():  
    preg= request.form.get('Pregnancies')
    plas= request.form.get('PlasmaGlucose')
    pres= request.form.get('BloodPresssure')
    skin= request.form.get('SkinThickness')
    test= request.form.get('Insulin')
    mass= request.form.get('BMI')
    pedi= request.form.get('DiabetesPedigree')
    age= request.form.get('Age')    

    print(preg,plas,pres,skin,test,mass,pedi,age)
    
    pred=model.predict([[int(preg),int(plas),int(pres),int(skin),int(test),int(mass),int(pedi),int(age)]])
    if pred[0]==1:
        output="diabetic"
    else:
        output="Not diabetic"
    return render_template('diabeticresult.html',predicted_text=f'The person is {output}')

#Diabetic Code End


# BMI Code Start
@app.route('/blog2',methods=['POST'])
def contact2():  
    Weight= request.form.get('Weight')
    Height= request.form.get('Height')
       
    print(Weight,Height)
    c=0
    c=float(Weight)/(float(Height)*float(Height))    
    if  c<20:
        output="Under weight"
    elif(c>=20 and c <=25):
        output="Fit"
    else:
       output="Overweight" 
    return render_template('bmiresult.html',predicted_text=f'Your BMI value is {c} and you are {output}.')
# BMI Code End

# BMR Code Start

@app.route('/blog3',methods=['POST'])
def contact3():  
    weight= request.form.get('Weight')
    height= request.form.get('Height')
    gender= request.form.get('Gender')
    age= request.form.get('Age')
    print(weight,height,gender,age)
    
    if gender=="Male":
       output=88.362 + (13.397 * float(weight)) + (4.799 * float(height))-(5.677 *float(age))
    elif gender=="Female":
       output=447.593 + (9.247 * float(weight)) + (3.098 * float(height))-(4.330 * float(age))
    return render_template('bmrresult.html',predicted_text=f'Your BMR value is {output}')
# BMR Code End
#  run the app
if __name__=='__main__':
    app.run(debug=True,host="0.0.0.0",port=8080)

