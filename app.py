from flask import Flask, render_template_string
import os

app = Flask(__name__)

HTML = """ 
<!DOCTYPE html>
<html>
<head>
    <title>Be My Valentine 💘</title>
    <style>
        body { font-family: Arial, sans-serif; background: linear-gradient(135deg, #ff9a9e, #fad0c4); text-align: center; padding-top: 80px; }
        h1 { color: white; font-size: 42px; }
        button { font-size: 20px; padding: 12px 30px; margin: 20px; border: none; border-radius: 30px; cursor: pointer; position: relative; }
        .yes { background-color: #4CAF50; color: white; }
        .no { background-color: #f44336; color: white; }
        #result { margin-top: 30px; font-size: 24px; color: white; }
        img { margin-top: 20px; width: 260px; border-radius: 15px; }
    </style>
</head>
<body>
<h1>Will you be my Valentine? 💖</h1>
<button class="yes" onclick="yesClicked()">Yes 💃</button>
<button class="no" id="noBtn" onclick="noClicked()">No 😬</button>
<div id="result"></div>
<script>
    let noCount = 0;
    const noBtn = document.getElementById("noBtn");
    function randomPosition(button) {
        const x = Math.random() * (window.innerWidth - button.offsetWidth);
        const y = Math.random() * (window.innerHeight - button.offsetHeight - 100);
        button.style.position = 'absolute';
        button.style.left = x + 'px';
        button.style.top = y + 'px';
    }
    noBtn.addEventListener("mouseover", () => { randomPosition(noBtn); });
    function noClicked() {
        noCount++;
        document.getElementById("result").innerHTML = `<p>😿 Meow Meow Meow 😿</p>
        <img src="https://media.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif">`;
    }
    function yesClicked() {
        document.getElementById("result").innerHTML = `<p>YAYYYY!! 💖🕺</p>
        <img src="https://media.giphy.com/media/l0MYt5jPR6QX5pnqM/giphy.gif">`;
    }
</script>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8888))
    app.run(host="0.0.0.0", port=port)
