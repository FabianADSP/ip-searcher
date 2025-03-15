from flask import Flask, request

app = Flask(__name__)  # Folosește __name_ corect

# Dicționar pentru stocarea flagurilor
flags = {}

@app.route('/sendflag/<flag_number>', methods=['POST'])
def send_flag(flag_number):
    flag = request.get_data(as_text=True)
    flags[flag_number] = flag
   return f"Flag {flag_number} primit."

@app.route('/getflag/<flag_number>', methods=['GET'])
def get_flag(flag_number):
   return flags.get(flag_number, " ")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
