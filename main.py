from flask import Flask, render_template_string
import os

app = Flask(__name__)

TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Environment Variables</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 20px; }
        table { width: 100%; border-collapse: collapse; }
        th, td { border: 1px solid black; padding: 8px; text-align: left; }
        th { background-color: #f2f2f2; }
    </style>
</head>
<body>
    <h1>Environment Variables</h1>
    <table>
        <tr><th>Variable</th><th>Value</th></tr>
        {% for key, value in envs.items() %}
        <tr><td>{{ key }}</td><td>{{ value }}</td></tr>
        {% endfor %}
    </table>
</body>
</html>
"""


@app.route("/")
def index():
    envs = dict(os.environ)
    return render_template_string(TEMPLATE, envs=envs)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
