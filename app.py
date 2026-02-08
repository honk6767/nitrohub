import os

print("🚗 Starting INSANE‑GEN FILE CREATOR...")
print("🏎️ Buckle up. This script accelerates from 0 to folders in 2 seconds.")
print("😈 Warning: excessive folder creation may cause tire smoke.")

BASE_DIR = os.getcwd()

structure = {
    "templates": {
        "index.html": """<!DOCTYPE html>
<html>
<head>
    <title>IGNITION ARCADE</title>
    <link rel="stylesheet" href="/static/style.css">
</head>
<body>
    <h1>🔥 IGNITION ARCADE 🔥</h1>
    <p>Press start. Floor it. No brakes.</p>
    <button onclick="alert('VROOM 🏎️ LOGIN')">Login</button>
    <button onclick="alert('SKRRRT 🏁 SIGN UP')">Sign Up</button>
    <button onclick="alert('GUEST MODE: NO SEATBELT 😈')">Guest</button>

    <script src="/static/game.js"></script>
</body>
</html>
"""
    },
    "static": {
        "game.js": """console.log("🏎️ Game engine warming up...");
console.log("⛽ Fuel injected.");
console.log("😈 INSANE‑GEN MODE READY.");

let speed = 0;

function accelerate() {
    speed += 50;
    console.log("VROOOOM! Speed:", speed);
    if (speed > 9000) {
        console.log("🚓 Physics police are after you.");
    }
}

setInterval(accelerate, 1000);
""",
        "style.css": """body {
    background: black;
    color: lime;
    font-family: monospace;
    text-align: center;
}

button {
    padding: 15px;
    margin: 10px;
    font-size: 18px;
    cursor: pointer;
    background: red;
    color: white;
    border: none;
}

button:hover {
    background: orange;
}
"""
    },
    "requirements.txt": "flask\ngunicorn\n"
}

app_py_content = """from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    print("🏁 Engine started.")
    print("😈 INSANE‑GEN MODE ENABLED.")
    app.run(host="0.0.0.0", port=5000)
"""

def create_structure(base, struct):
    for name, content in struct.items():
        path = os.path.join(base, name)
        if isinstance(content, dict):
            os.makedirs(path, exist_ok=True)
            print(f"📁 Folder created: {name} (fresh tires installed)")
            create_structure(path, content)
        else:
            with open(path, "w") as f:
                f.write(content)
            print(f"📄 File created: {name} (oil changed)")

# Create everything
create_structure(BASE_DIR, structure)

# Overwrite app.py with Flask app AFTER creating structure
with open(os.path.join(BASE_DIR, "server.py"), "w") as f:
    f.write(app_py_content)

print("✅ ALL FILES CREATED SUCCESSFULLY.")
print("🏎️ Project is now street‑legal (mostly).")
print("😈 Next step: deploy and make physics cry.")
print("🚗 If this crashes, blame the brakes. There are none.")
