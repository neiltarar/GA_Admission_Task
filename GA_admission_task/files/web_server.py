from flask import Flask, render_template, request

app= Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
database={'admin':'admin'}

@app.route("/main")
def main():
    return render_template('main.html')

@app.route("/project_1")
def project1():
    return render_template('project1.html')

@app.route("/project_2")
def project2():
    return render_template('project2.html')

@app.route("/project_3")
def project3():
    return render_template('project3.html')

@app.route("/color_switcher_challenge")
def traficlights():
    return render_template('traficlights.html')

@app.route('/form_login', methods=['POST','GET'])
def login():
    username=request.form['username']
    pwd=request.form['password']
    if username not in database:
        return render_template('index.html', info = 'Invalid user')
    else:
        if database[username] != pwd:
            return render_template('index.html', info = 'Invalid password')
        else:
            return render_template('main.html')
if __name__ == '__main__':
    app.run(host="192.168.0.140", port=9000, debug=True) #(ssl_context=('cert.pem', 'key.pem')) #'ssl_context' activates https
