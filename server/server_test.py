from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def www():
    names = ['david', 'moshe', 'yitschak', 'shlomo']
    return render_template('home.html',
                           title='my_names', items=names)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
