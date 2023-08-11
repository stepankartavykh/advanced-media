from flask import Flask
from module import get_data_sites

app = Flask(__name__)


@app.route("/")
def start_page():
    return f"{get_data_sites()}"
