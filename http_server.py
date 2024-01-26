from flask import Flask, request
import os

app = Flask(__name__)

DATA_DIR = "/tmp/data"
FILE_SIZE = 100 * 1024 * 1024  # 100MB

def read_file_content(file_path, line_number=None):
    with open(file_path, 'r') as file:
        if line_number is not None:
            for _ in range(line_number - 1):
                file.readline()
            return file.readline()
        else:
            return file.read()

@app.route('/data', methods=['GET'])
def get_data():
    n = request.args.get('n')
    m = request.args.get('m')

    if n is None:
        return "Parameter 'n' is required.", 400

    file_path = os.path.join(DATA_DIR, f"{n}.txt")

    if not os.path.exists(file_path):
        return f"File {n}.txt not found.", 404

    if m is not None:
        try:
            m = int(m)
            if m <= 0:
                raise ValueError
        except ValueError:
            return "Invalid value for 'm'. It should be a positive integer.", 400
        content = read_file_content(file_path, m)
    else:
        content = read_file_content(file_path)

    return content

if __name__ == '__main__':
    app.run(debug=True,port=1025)
