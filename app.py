from flask import Flask,render_template,request,redirect,url_for
app = Flask(__name__) ## it creates instance of the flask which creates WSGI
#########

##jinga 2 template engine

## {{}} - expressions to directly output in html
## {% ....%}, conditional statement/ for loops
## {# ...#} for comments


#####
@app.route("/")
def welcome():
    return "<html><h1>Welcome to Baveet's page</H1></html>"
## in order to create a seperate html page, we need to redirect from here and so we have to use render_template!
## by default its get request method!
@app.route("/index",methods=['GET'])
def index():
    return render_template('index.html')
## render_template runs the template engine JINJA2 !!!!!
@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/form',methods=['GET','POST'])
## Requests capture whether its get or post request!
def forms():
    if request.method == 'POST':
    ### now retrive the info from ""ID"" tag from html!
        name = request.form['name']
        return f'Hello bhosda : {name}'
    return render_template('form.html')  
## in html, action tag is used for redirecting to the url provided!, so i entered /xyz, then on clicking submit, i would be redirected to xyz!
@app.route('/submit',methods=['GET','POST'])
## Requests capture whether its get or post request!
def submit():
    if request.method == 'POST':
    ### now retrive the info from ""ID"" tag from html!
        name = request.form['name']
        return f'Hello: {name}'
    return render_template('form.html') 
 
## Variable Rule, providing parameter and restricting type

@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score >= 50:
        res = "PASS"
    else:
        res = "FAIL"
    return render_template('result.html', results = res)

@app.route('/result_check/<float:score>')
def result_check(score):
    res = ""
    if score >= 50:
        res = "PASS"
    else:
        res = "FAIL"
    d = {'score' : score, 'result' : res}
    return render_template('finalresult.html', results = d)

@app.route('/getresults',methods = ['GET'])
def getresults():
    return render_template('getresults.html')

@app.route('/finalscore',methods=['POST','GET'])
def finalscore():
    avg_score = 0
    if request.method == 'POST':
        avg_score+=float(request.form['maths'])
        avg_score+=float(request.form['science'])
        avg_score+=float(request.form['c'])
        avg_score+=float(request.form['datascience'])
        avg_score/=4

    ## redirecting to result_check site
    return redirect(url_for('result_check',score = avg_score))   
    ## url_for builds dynamic URLs

if __name__ == "__main__":
    app.run(debug=True)