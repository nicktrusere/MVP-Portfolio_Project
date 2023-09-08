from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    sites = ['Huawei_LP1', 'Nokia_LP2', 'Cape_Town_DAS', 'Durban', 'Huawei_LP4']
    return render_template('index.html', site=sites)

@app.route('/site/<st>')
def site(st):
    return "This is " + str(st)

if __name__=="__main__":
    app.run(debug=True)
