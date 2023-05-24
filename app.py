# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os

from flask import Flask, render_template
import subprocess

app = Flask(__name__)

secret = str(os.getenv('SECRET'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_otp')
def get_otp():

    # Execute the command and retrieve the OTP
    counter = str(os.popen("cat /var/log/counter").read()).replace('\n', '')
    otp_code = str(os.popen("oathtool --hotp " + secret + " -c " + counter).read()).replace('\n', '')

    counter = int(counter) + 1
    os.popen("echo " + str(counter) + " > /var/log/counter")

    return otp_code

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(host="0.0.0.0")
