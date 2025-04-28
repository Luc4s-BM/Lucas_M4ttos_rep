from flask import Flask, render_template, Response, request, jsonify
import cv2
import mediapipe as mp
import numpy as np
import pickle
import os

app = Flask(__name__)

# Inicializar Mediapipe
mp_face_detection = mp.solutions.face_detection
mp_face_mesh = mp.solutions.face_mesh
mp_drawing = mp.solutions.drawing_utils

webcam = cv2.VideoCapture(0)
webcam.set(3, 1280)
webcam.set(4, 720)

DATA_FILE = "face_data.pkl"

# Carregar dados existentes
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "rb") as f:
        data = pickle.load(f)
        known_face_embeddings = data["embeddings"]
        known_face_names = data["names"]
else:
    known_face_embeddings = []
    known_face_names = []

face_detector = mp_face_detection.FaceDetection(model_selection=1, min_detection_confidence=0.5)
face_embedder = mp_face_mesh.FaceMesh(static_image_mode=True, max_num_faces=1, refine_landmarks=True, min_detection_confidence=0.5)

def get_face_embedding(face_image):
    """Extrai embedding facial usando MediaPipe Face Mesh"""
    results = face_embedder.process(face_image)
    if results.multi_face_landmarks:
        landmarks = results.multi_face_landmarks[0].landmark
        return np.array([[lm.x, lm.y, lm.z] for lm in landmarks]).flatten()
    return None

def compare_faces(embedding, threshold=0.5):
    """Compara as faces"""
    if not known_face_embeddings:
        return None
    distances = np.linalg.norm(known_face_embeddings - embedding, axis=1)
    min_index = np.argmin(distances)
    if distances[min_index] < threshold:
        return known_face_names[min_index]
    return None

def save_data():
    """Salva os dados no arquivo"""
    with open(DATA_FILE, "wb") as f:
        data = {
            "embeddings": known_face_embeddings,
            "names": known_face_names
        }
        pickle.dump(data, f)

@app.route('/')
def index():
    return render_template('index.html')

def gen_frames():
    while True:
        success, frame = webcam.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/capture', methods=['POST'])
def capture():
    name = request.form.get('name')
    if not name:
        return jsonify({"status": "error", "message": "Nome não fornecido."})

    success, frame = webcam.read()
    if not success:
        return jsonify({"status": "error", "message": "Erro ao capturar o frame."})

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    results = face_detector.process(rgb_frame)
    if not results.detections:
        return jsonify({"status": "error", "message": "Nenhum rosto detectado."})

    for detection in results.detections:
        box = detection.location_data.relative_bounding_box
        ih, iw, _ = frame.shape
        x = int(box.xmin * iw)
        y = int(box.ymin * ih)
        w = int(box.width * iw)
        h = int(box.height * ih)

        y = max(0, y - int(h * 0.15))
        h += int(h * 0.3)
        x = max(0, x - int(w * 0.15))
        w += int(w * 0.3)

        face_roi = rgb_frame[y:y+h, x:x+w]
        embedding = get_face_embedding(face_roi)

        if embedding is not None:
            known_face_embeddings.append(embedding)
            known_face_names.append(name)
            save_data()
            return jsonify({"status": "success", "message": f"Rosto de {name} salvo com sucesso!"})

    return jsonify({"status": "error", "message": "Erro ao processar o rosto."})

if __name__ == '__main__':
    app.run(debug=True)
