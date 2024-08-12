from flask import Flask, request, render_template_string
import os

app = Flask(__name__)


HTML = '''
<!doctype html>
<html>
<body>
    <h1>File Upload</h1>
    <form method="POST" enctype="multipart/form-data">
        <input type="file" name="file">
        <input type="submit" value="Upload">
    </form>
    {% if message %}
    <p>{{ message }}</p>
    {% endif %}
</body>
</html>
'''


UPLOAD_DIR = 'uploads'
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return render_template_string(HTML, message='No file part')
        file = request.files['file']
        if file.filename == '':
            return render_template_string(HTML, message='No selected file')
        if file:
            filename = os.path.join(UPLOAD_DIR, file.filename)
            file.save(filename)
            return render_template_string(HTML, message=f'File {file.filename} uploaded successfully')
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)