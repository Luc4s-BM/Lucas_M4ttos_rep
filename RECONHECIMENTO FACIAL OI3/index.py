import cv2
import os
import face_recognition
import pickle

# Configurações iniciais
KNOWN_FACES_DIR = 'known_faces'
TOLERANCE = 0.6
FRAME_THICKNESS = 3
FONT_THICKNESS = 2
MODEL = 'hog'  # 'cnn' para GPU ou 'hog' para CPU

# Carregar ou criar banco de dados de faces
try:
    with open('faces_data.pkl', 'rb') as f:
        known_faces = pickle.load(f)
except FileNotFoundError:
    known_faces = {}

# Função para cadastrar novo rosto
def register_face():
    name = input("Digite o nome da pessoa: ")
    
    # Iniciar webcam
    cap = cv2.VideoCapture(0)
    print("Pressione 's' para tirar fotos (20 imagens serão capturadas)")
    
    captures = []
    while len(captures) < 20:
        ret, frame = cap.read()
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Mostrar preview
        cv2.imshow('Cadastrando...', frame)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            face_locations = face_recognition.face_locations(rgb_frame, model=MODEL)
            if face_locations:
                encoding = face_recognition.face_encodings(rgb_frame, face_locations)[0]
                captures.append(encoding)
                print(f"Captura {len(captures)}/20 realizada")
        
    cap.release()
    cv2.destroyAllWindows()
    
    # Salvar no banco de dados
    known_faces[name] = captures
    with open('faces_data.pkl', 'wb') as f:
        pickle.dump(known_faces, f)
    print(f"{name} cadastrado(a) com sucesso!")

# Função para excluir rosto
def delete_face():
    name = input("Digite o nome a ser excluído: ")
    if name in known_faces:
        del known_faces[name]
        with open('faces_data.pkl', 'wb') as f:
            pickle.dump(known_faces, f)
        print(f"{name} removido(a) com sucesso!")
    else:
        print("Nome não encontrado!")

# Função de reconhecimento
def recognize_faces():
    cap = cv2.VideoCapture(0)
    
    while True:
        ret, frame = cap.read()
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Detectar faces
        face_locations = face_recognition.face_locations(rgb_frame, model=MODEL)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)
        
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            name = "Desconhecido"
            
            # Comparar com faces conhecidas
            for person, encodings in known_faces.items():
                matches = face_recognition.compare_faces(encodings, face_encoding, TOLERANCE)
                if True in matches:
                    name = person
                    break
            
            # Desenhar retângulo e nome
            color = [0, 255, 0] if name != "Desconhecido" else [0, 0, 255]
            cv2.rectangle(frame, (left, top), (right, bottom), color, FRAME_THICKNESS)
            cv2.putText(frame, name, (left + 10, bottom + 25), cv2.FONT_HERSHEY_SIMPLEX, 1, color, FONT_THICKNESS)
        
        cv2.imshow('Reconhecimento Facial', frame)
        
        # Sair com 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

# Menu principal
while True:
    print("\n--- Menu Principal ---")
    print("1. Cadastrar novo rosto")
    print("2. Excluir rosto cadastrado")
    print("3. Iniciar reconhecimento")
    print("4. Sair")
    
    choice = input("Escolha uma opção: ")
    
    if choice == '1':
        register_face()
    elif choice == '2':
        delete_face()
    elif choice == '3':
        recognize_faces()
    elif choice == '4':
        break
    else:
        print("Opção inválida!")