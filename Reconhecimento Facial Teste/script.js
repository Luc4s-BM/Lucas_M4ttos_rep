const video = document.getElementById('video');
const startButton = document.getElementById('startButton');
const stopButton = document.getElementById('stopButton');
const captureButton = document.getElementById('captureButton');
const statusDiv = document.getElementById('status');

let stream;

// Ligar a câmera
startButton.onclick = async () => {
    if (!stream) {
        try {
            stream = await navigator.mediaDevices.getUserMedia({ video: true });
            video.srcObject = stream;
            statusDiv.innerText = "Câmera ligada!";
        } catch (err) {
            console.error('Erro ao acessar a câmera:', err);
            statusDiv.innerText = "Erro ao acessar a câmera!";
        }
    }
};

// Desligar a câmera
stopButton.onclick = () => {
    if (stream) {
        const tracks = stream.getTracks();
        tracks.forEach(track => track.stop());
        video.srcObject = null;
        stream = null;
        statusDiv.innerText = "Câmera desligada!";
    }
};

// Capturar a imagem e enviar para o servidor
captureButton.onclick = () => {
    const nome = document.getElementById('nome').value.trim();
    if (!nome) {
        alert("Digite seu nome antes de capturar!");
        return;
    }

    const canvas = document.createElement('canvas');
    canvas.width = video.videoWidth;
    canvas.height = video.videoHeight;
    const ctx = canvas.getContext('2d');
    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);

    const imagemBase64 = canvas.toDataURL('image/jpeg');

    fetch('/capture', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            nome: nome,
            imagem: imagemBase64
        })
    })
    .then(response => response.json())
    .then(data => {
        statusDiv.innerText = data.mensagem;
    })
    .catch(err => {
        console.error('Erro ao capturar rosto:', err);
        statusDiv.innerText = "Erro ao capturar o rosto!";
    });
};
