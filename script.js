
function analyzeImage() {
  const resultBox = document.getElementById('resultBox');
  const diagnosis = document.getElementById('diagnosis');
  const remedy = document.getElementById('remedy');

  // Simulated AI response
  diagnosis.textContent = "Disease: Early Blight";
  remedy.textContent = "Remedy: Apply wood ash and soap mixture every morning. Locally available.";

  resultBox.style.display = 'block';
}

document.getElementById('imageUpload').addEventListener('change', function(event) {
  const preview = document.getElementById('preview');
  const file = event.target.files[0];
  if (file) {
    preview.src = URL.createObjectURL(file);
  }
});
