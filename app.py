from flask import Flask
import getpass
import subprocess
from datetime import datetime
import pytz

app = Flask(__name__)

@app.route("/htop")
def htop():
    name = "Pothula Charan Tej Reddy"
    username = getpass.getuser()
    ist = pytz.timezone('Asia/Kolkata')
    current_time = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')
    
    try:
        top_output = subprocess.check_output(["top", "-b", "-n", "1"]).decode("utf-8")
    except Exception as e:
        top_output = f"Error fetching top: {e}"
    
    html = f"""
    <h2>Name: {name}</h2>
    <h2>Username: {username}</h2>
    <h2>Server Time (IST): {current_time}</h2>
    <pre>{top_output}</pre>
    """
    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
