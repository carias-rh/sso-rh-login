# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os

from flask import Flask, render_template
import subprocess

app = Flask(__name__)

secret = os.getenv('SECRET', default=None)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_otp')
def get_otp():
    # Increment the counter in the "counter" file
    with open('counter', 'r+') as f:
        counter = int(f.read()) + 1
        f.seek(0)
        f.write(str(counter))

    # Execute the command and retrieve the OTP
    counter = str(os.popen("cat ./counter").read())
    process = subprocess.Popen(['oathtool', '--hotp', secret, '-c', counter ], stdout=subprocess.PIPE)
    output, error = process.communicate()

    return output

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(host="0.0.0.0")
