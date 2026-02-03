from flask import Flask
from markupsafe import Markup

app = Flask(__name__)

@app.route("/")
def valentine():
    html_content = Markup("""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Be My Valentine 💘</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    background: linear-gradient(135deg, #ff9a9e, #fad0c4);
                    text-align: center;
                    padding-top: 80px;
                }
                h1 {
                    color: white;
                    font-size: 42px;
                }
                button {
                    font-size: 20px;
                    padding: 12px 30px;
                    margin: 20px;
                    border: none;
                    border-radius: 30px;
                    cursor: pointer;
                    position: relative;
                }
                .yes { background-color: #4CAF50; color: white; }
                .no { background-color: #f44336; color: white; }
                #result {
                    margin-top: 30px;
                    font-size: 24px;
                    color: white;
                }
            </style>
        </head>
        <body>
            <h1>Will you be my Valentine? 💖</h1>
            <button class="yes" onclick="yesClicked()">Yes 💃</button>
            <button class="no" id="noBtn" onmouseover="randomPosition(this)" onclick="noClicked()">No 😬</button>
            <div id="result"></div>

            <script>
                function randomPosition(button) {
                    const x = Math.random() * (window.innerWidth - button.offsetWidth);
                    const y = Math.random() * (window.innerHeight - button.offsetHeight - 100);
                    button.style.position = 'absolute';
                    button.style.left = x + 'px';
                    button.style.top = y + 'px';
                }

                function noClicked() {
                    document.getElementById('result').innerText = '😿 Meow Meow Meow 😿';
                }

                function yesClicked() {
                    document.getElementById('result').innerText = 'YAYYYY!! 💖🕺';
                }
            </script>
        </body>
        </html>
    """)
    return html_content

# Start server for testing
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)
