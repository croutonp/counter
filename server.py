from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "bop to the top"



# @app.route('/')
# def index():
#     count = int(request.cookies.get('visitors count', 0))
#     count = f"{count+1}"
    
#     return render_template("index.html")

@app.route('/')
def vistors_count():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 1


    return render_template("index.html")
  
@app.route('/click')
def click():
    if 'count' in session:
        session['count'] += 1
    else:
        session['count'] = 1
    return redirect('/')


@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

@app.route('/form', methods=['POST'])
def form():
    x = request.form['name']
    session['count'] += int(x) - 1
    
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)