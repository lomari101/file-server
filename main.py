from flask import Flask, request, send_from_directory
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    files = os.listdir(UPLOAD_FOLDER)
    links = [f"<li><a href='/files/{f}'>{f}</a></li>" for f in files]
    return f"""
    <h2>📁 الملفات:</h2>
    <ul>{''.join(links)}</ul>
    <form method="POST" action="/upload" enctype="multipart/form-data">
        <input type="file" name="file" />
        <button type="submit">رفع</button>
    </form>
    """

@app.route('/upload', methods=['POST'])
def upload():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(os.path.join(UPLOAD_FOLDER, uploaded_file.filename))
    return "✅ تم رفع الملف! <a href='/'>رجوع</a>"

@app.route('/files/<filename>')
def files(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
