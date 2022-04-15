import translate

from flask import Flask, request, render_template, jsonify

app = Flask(__name__)


@app.route('/')
def home_page():
    return render_template("home.html")


@app.route("/translation")
def translation_page():
    return render_template("translationPage.html")


@app.route("/translation/piglatin", methods=["POST"])
def translate_to_pig_latin():
    user_input = request.form["words"]
    translation = translate.translate_to_piglatin(user_input)

    return render_template("translationPage.html", translated=translation, original=user_input)


@app.route("/translation/piglatin/json", methods=["POST"])
def translate_to_pig_latin_json():
    user_input = request.form["words"]
    translation = translate.translate_to_piglatin(user_input)
    data = {
        "original": user_input,
        "translated": translation
    }

    return jsonify(data)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8081, debug=True)
