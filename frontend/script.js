document.getElementById('table').addEventListener('change', function () {
    const fileName = this.files.length > 0 ? this.files[0].name : "Nenhum arquivo selecionado";
    document.getElementById('file-name').textContent = fileName;
  });