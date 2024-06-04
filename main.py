from flask import *
from werkzeug.utils import secure_filename
import os
from flask_cors import CORS
from detectionVideo import detectVideo
from detectionImage import detectImage
from downloadVideoAndDetect import download_video_url
import json

app = Flask(__name__)
CORS(app, resources={r"/videoUpload": {"origins": "http://localhost:3000"},
                     r"/imageUpload": {"origins": "http://localhost:3000"},
                     r"/getVideos": {"origins": "http://localhost:3000"},
                     r"/getPhotos": {"origins": "http://localhost:3000"},
                     r"/download-video": {"origins": "http://localhost:3000"},
                     r"/get_detected_video": {"origins": "http://localhost:3000"},
                     r"/get_detected_photo": {"origins": "http://localhost:3000"},
                     r"/play_detected_video": {"origins": "http://localhost:3000"},
                     r"/selectModel": {"origins": "http://localhost:3000"}}, supports_credentials=True)

models = {
    "catAndDog": "catAndDog.pt",
    "yolov8n": "yolov8n.pt",
    "pistol": "pistol.pt",
    "fire": "fire.pt"
}

model_name = ""


@app.route('/selectModel', methods=['POST'])
def select_model():
    global model_name
    # İstekten model adını al
    model_name = request.json['model']
    print(model_name + " model_name")
    if model_name not in models:
        return jsonify({"Mesaj": "Geçersiz model adı"}), 400
    return jsonify({"Mesaj": "Model başarılı bir şekilde seçildi"}), 200


model_name = "pistol"


@app.route('/videoUpload', methods=['POST'])
def success():
    global videoFile
    if request.method == 'POST':
        video = request.files['file']
        filename = secure_filename(video.filename)
        video_path = os.path.join(app.root_path, 'uploaded_videos', filename)
        video.save(video_path)
        videoFile = filename
        detectVideo(filename, model_name + '.pt')
        return jsonify({"Mesaj": "Video başarıyla yüklendi"}), 200


@app.route('/imageUpload', methods=['POST'])
def upload_photo():
    photo = request.files['file']
    image_name = photo.filename
    photo.save(os.path.join('uploaded_photo', image_name))
    detectImage(image_name, model_name + '.pt')
    return jsonify({"Mesaj": "Fotoğraf başarıyla yüklendi"}), 200


@app.route('/download-video', methods=['POST'])  # Youtube linkle videoyu indirp tespit edip kaydeder.
def download_video():
    received_text = request.data.decode("utf-8")
    json_data = json.loads(received_text)
    video_url = json_data['text']
    download_video_url(video_url, model_name + '.pt')
    return jsonify({"Mesaj": "Video başarıyla indirildi ve tespit yapıldı"}), 200


# Buradan sonra get servisleri

UPLOAD_VIDEO_FOLDER = 'detected_videos'


def get_video_names():
    video_names = os.listdir(UPLOAD_VIDEO_FOLDER)
    # .DS_Store dosyasını filtrele (macOS özel)
    video_names = [name for name in video_names if not name.startswith('.')]
    return video_names


@app.route('/getVideos', methods=['GET'])
def get_videos():
    video_names = get_video_names()
    if not video_names:
        return jsonify({"Mesaj": "Video bulunamadı"}), 404
    return jsonify({"videos": video_names}), 200


UPLOAD_PHOTO_FOLDER = 'detected_photo'


def get_photo_names():
    photo_names = os.listdir(UPLOAD_PHOTO_FOLDER)
    # .DS_Store dosyasını filtrele (macOS özel)
    photo_names = [name for name in photo_names if not name.startswith('.')]
    return photo_names


@app.route('/getPhotos', methods=['GET'])
def get_photos():
    photo_names = get_photo_names()
    if not photo_names:
        return jsonify({"Mesaj": "Fotoğraf bulunamadı"}), 404
    return jsonify({"photos": photo_names}), 200


detected_video_path = 'detected_videos'


@app.route('/get_detected_video', methods=['GET'])
def get_video():
    video_name = request.args.get('video_name')
    video_path = os.path.join(detected_video_path, video_name)
    if os.path.exists(video_path):
        return send_file(video_path, as_attachment=True)
    return jsonify({"Mesaj": "Video bulunamadı"}), 404


detected_photo_path = 'detected_photo'


@app.route('/get_detected_photo', methods=['GET'])
def get_photo():
    photo_name = request.args.get('photo_name')
    photo_path = os.path.join(detected_photo_path, photo_name)
    if os.path.exists(photo_path):
        return send_file(photo_path, as_attachment=True)
    return jsonify({"Mesaj": "Fotoğraf bulunamadı"}), 404


if __name__ == "__main__":
    app.run(debug=True)

