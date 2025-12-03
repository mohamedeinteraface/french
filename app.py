from flask import Flask, render_template

app = Flask(__name__)

# ===== Page d'accueil =====
@app.route("/")
def index():
    return render_template("index.html")

# ===== Lettres A-Z =====
@app.route("/letters")
def letters():
    letters_data = []
    for i in range(ord('A'), ord('Z') + 1):
        char = chr(i)
        letters_data.append({
            "char": char,
            "image": f"{char.lower()}.png",
            "sound": f"{char.lower()}.mp3"
        })
    return render_template("letters.html", letters=letters_data)

# ===== Chiffres 1-99 =====
@app.route("/numbers")
def numbers():
    numbers_data = []
    for i in range(1, 100):
        numbers_data.append({
            "num": str(i),
            "image": f"{i}.png",
            "sound": f"{i}.mp3"
        })
    return render_template("numbers.html", numbers=numbers_data)

# ===== NEW : Words (A1 - A2 - B1 - B2) =====
@app.route("/words")
def words():

    words_data = {
        "A1": [
            {"word": "pomme", "image": "pomme.png", "sound": "pomme.mp3"},
            {"word": "chat", "image": "chat.png", "sound": "chat.mp3"},
            {"word": "maison", "image": "maison.png", "sound": "maison.mp3"},
        ],
        "A2": [
            {"word": "hôpital", "image": "hopital.png", "sound": "hopital.mp3"},
            {"word": "voiture", "image": "voiture.png", "sound": "voiture.mp3"},
        ],
        "B1": [
            {"word": "appartement", "image": "appartement.png", "sound": "appartement.mp3"},
            {"word": "ordinateur", "image": "ordinateur.png", "sound": "ordinateur.mp3"},
        ],
        "B2": [
            {"word": "développement", "image": "developpement.png", "sound": "developpement.mp3"},
            {"word": "amélioration", "image": "amelioration.png", "sound": "amelioration.mp3"},
        ]
    }

    return render_template("words.html", words=words_data)

if __name__ == "__main__":
    app.run(debug=True)

