from flask import Flask, render_template, request, url_for, redirect
import config

app = Flask(__name__)
config_object = config.DevelopmentConfig
app.config.from_object(config_object)


@app.route('/')
def home():
    return render_template("index.html", title=app.config["APP_TITLE"], map_key=app.config["GOOGLE_MAP_KEY"])


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        return redirect(url_for("home"))
    else:
        return redirect(url_for("home"))


@app.route('/logout')
def logout():
    pass


if __name__ == '__main__':
    app.run()