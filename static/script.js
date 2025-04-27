const video = document.getElementById("video");
const resultDiv = document.getElementById("result");
const captureButton = document.getElementById("captureButton");

async function setupWebcam() {
    const stream = await navigator.mediaDevices.getUserMedia({ video: {} });
    video.srcObject = stream;
}

async function loadModels() {
    await faceapi.nets.ssdMobilenetv1.loadFromUri('/models');
    await faceapi.nets.faceLandmark68Net.loadFromUri('/models');
    await faceapi.nets.faceRecognitionNet.loadFromUri('/models');
}

captureButton.addEventListener('click', async () => {
    const detections = await faceapi.detectAllFaces(video).withFaceLandmarks().withFaceDescriptors();
    if (detections.length > 0) {
        const labeledFaceDescriptors = [
            new faceapi.LabeledFaceDescriptors('Pessoa1', [new Float32Array(128)]) // Exemplo com pessoa fictícia
        ];

        const faceMatcher = new faceapi.FaceMatcher(labeledFaceDescriptors, 0.6);
        const results = detections.map(d => faceMatcher.findBestMatch(d.descriptor));
        
        const name = results[0] ? results[0].label : 'Desconhecida';
        resultDiv.textContent = `Face reconhecida como: ${name}`;
    } else {
        resultDiv.textContent = 'Nenhuma face detectada!';
    }
});

setupWebcam();
loadModels();
