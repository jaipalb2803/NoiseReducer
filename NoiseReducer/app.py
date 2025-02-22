from flask import Flask, request, render_template, send_file
import os
import uuid
from noise_reduction import process_audio  # Import your Python logic

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
PROCESSED_FOLDER = 'processed'

# Create necessary folders if they don't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(PROCESSED_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_file():
    if 'audio-file' not in request.files:
        return "No file uploaded!", 400
    
    file = request.files['audio-file']
    if file.filename == '':
        return "No selected file!", 400

    # Save the uploaded file
    file_id = str(uuid.uuid4())  # Unique ID for file
    input_path = os.path.join(UPLOAD_FOLDER, f"{file_id}_{file.filename}")
    file.save(input_path)

    # Process the file
    output_path = os.path.join(PROCESSED_FOLDER, f"{file_id}_reduced_{file.filename}")
    process_audio(input_path, output_path)

    return send_file(output_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
