from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'Hello World'


@app.route('/')
def homeCount():
    if 'homeCount' not in session:
        session['homeCount'] = 0
    if 'homeCount' in session:
        session['homeCount'] += 1
    if 'counter' not in session:
        session['counter'] = 0
    # if 'counter' in session:
    #     session['counter'] += 1
    return render_template('index.html', counter = session['counter'], homeCount = session['homeCount'])

@app.route('/destroy_session')
def reset():
    # session.clear()
    session.pop('counter')
    return redirect('/')

@app.route('/increment2')
def inc2():
    if 'counter' in session:
        session['counter'] += 2
    return redirect('/')

@app.route('/custom_inc', methods=['POST'])
def custom_inc():
    if 'counter' in session:
        session['counter'] += (int(request.form['customInc']))
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)