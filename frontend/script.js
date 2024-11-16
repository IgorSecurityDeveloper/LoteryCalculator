document.getElementById('table').addEventListener('change', function () {
    const fileName = this.files.length > 0 ? this.files[0].name : "Nenhum arquivo selecionado";
    document.getElementById('file-name').textContent = fileName;
  });

  async function analisar() {
    const fileInput = document.getElementById('fileInput');
    if (!fileInput.files[0]) {
        alert('Selecione um arquivo!');
        return;
    }

    const data = new FormData();
    data.append('caminho_arquivo', fileInput.files[0].name);

    const response = await fetch('/analisar', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ caminho_arquivo: fileInput.files[0].name }),
    });

    const result = await response.json();
    document.getElementById('result').innerText = JSON.stringify(result, null, 2);
}