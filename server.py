from flask import Flask, request

app = Flask(_name_)
flags = {}

@app.route('/sendflag/<flag_number>', methods=['POST'])
def send_flag(flag_number):
    flag = request.get_data(as_text=True)
    flags[flag_number] = flag
    return f"Flag {flag_number} primit."

@app.route('/getflag/<flag_number>', methods=['GET'])
def get_flag(flag_number):
    return flags.get(flag_number, "Niciun flag disponibil.")

if _name_ == "_main_":
    app.run(host="0.0.0.0", port=8080)
