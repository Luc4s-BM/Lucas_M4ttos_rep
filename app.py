from flask import Flask, request, jsonify
import cv2
import numpy as np
from tensorflow.keras.models import load_model  # type: ignore # Modificado para usar o Keras do TensorFlow
import base64
from io import BytesIO
from PIL import Image

app = Flask(__name__)

# Carregar o modelo pré-treinado (use o seu modelo, aqui é um exemplo com FaceNet)
facenet_model = load_model('facenet_keras.h5')

# Função para converter a imagem base64 para um array numpy
def decode_base64_image(data):
    img_data = base64.b64decode(data.split(",")[1])
    img = Image.open(BytesIO(img_data))
    return np.array(img)

# Função para detectar a face usando o OpenCV
def detect_face(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    if len(faces) == 0:
        return None
    x, y, w, h = faces[0]
    face_image = image[y:y+h, x:x+w]
    return face_image

# Função para obter o embedding da face
def get_face_embedding(face_image):
    face_image = cv2.resize(face_image, (160, 160))
    face_image = np.expand_dims(face_image, axis=0)
    face_image = (face_image / 255.0) * 2.0 - 1.0
    embedding = facenet_model.predict(face_image)
    return embedding

# Função para reconhecer a face
def recognize_face(face_embedding):
    # Exemplo de banco de dados com embeddings conhecidos
    known_face_embeddings = {
        'Pessoa1': np.random.rand(1, 128),
        'Pessoa2': np.random.rand(1, 128),
    }
    min_distance = float('inf')
    person_name = None
    for name, known_embedding in known_face_embeddings.items():
        distance = np.linalg.norm(face_embedding - known_embedding)
        if distance < min_distance:
            min_distance = distance
            person_name = name
    return person_name

@app.route('/recognize', methods=['POST'])
def recognize():
    try:
        data = request.get_json()
        img_data = data['image']
        
        # Decodificar a imagem base64
        image = decode_base64_image(img_data)
        
        # Detectar a face
        face_image = detect_face(image)
        
        if face_image is None:
            return jsonify({'error': 'Nenhuma face detectada na imagem'})
        
        # Obter o embedding da face
        face_embedding = get_face_embedding(face_image)
        
        # Reconhecimento da face
        person_name = recognize_face(face_embedding)
        
        if person_name:
            return jsonify({'name': person_name})
        else:
            return jsonify({'error': 'Face não reconhecida'})
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
