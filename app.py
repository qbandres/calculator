#develoment flask qbandres

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('app.html')

#Form Submission Route
@app.route('/calc', methods = ['PoST'])
def send(valor=sum):
    if request.method == 'POST':
        num1 = request.form['num1']
        num2 = request.form['num2']
        operation = request.form['operation']
        
        if operation == 'add':
            sum = float(num1)+float(num2)
            return render_template('app.html',result=sum)
        
        elif operation == 'subtract':
            sum = float(num1)-float(num2)
            return render_template('app.html',result=sum)

        elif operation == 'multiply':
            sum = float(num1)*float(num2)
            return render_template('app.html',result=sum)

        elif operation == 'divide':
            sum = float(num1)/float(num2)
            return render_template('app.html',result=sum)
        elif operation == 'power':
            sum = float(num1)**float(num2)
            return render_template('app.html',result=sum)
        else:
            return render_template('app.html')


if __name__ == '__main__':
    app.debug = True
    app.run()