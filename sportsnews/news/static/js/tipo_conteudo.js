document.addEventListener('DOMContentLoaded', function() {
  const formsetDiv = document.getElementById('conteudo-formset');
  const addBtn = document.getElementById('add-conteudo-btn');
  const totalForms = document.querySelector('#id_conteudo-TOTAL_FORMS');

  function atualizarTipoCampos(bloco) {
    const tipoSelect = bloco.querySelector('select[name$="-tipo"]');
    const textoDiv = bloco.querySelector('.campo-texto');
    const imagemDiv = bloco.querySelector('.campo-imagem');
    const videoDiv = bloco.querySelector('.campo-video');

    // Ocultar todos
    textoDiv.style.display = 'none';
    imagemDiv.style.display = 'none';
    videoDiv.style.display = 'none';

    if (!tipoSelect) return;

    const valor = tipoSelect.value;

    if (valor === 'texto') textoDiv.style.display = 'block';
    else if (valor === 'imagem') imagemDiv.style.display = 'block';
    else if (valor === 'video') videoDiv.style.display = 'block';
  }

  function initPreviewImagem(bloco) {
    const inputImagem = bloco.querySelector('input[type="file"][name$="-imagem"]');
    const preview = bloco.querySelector('.preview-img'); // Use uma classe para preview dentro do bloco

    if (!inputImagem || !preview) return;

    inputImagem.addEventListener('change', function() {
      const file = this.files[0];
      if (file) {
        const reader = new FileReader();

        reader.onload = function(e) {
          preview.setAttribute('src', e.target.result);
          preview.style.display = 'block';
        }

        reader.readAsDataURL(file);
      } else {
        preview.setAttribute('src', '#');
        preview.style.display = 'none';
      }
    });
  }

  function initBloco(bloco) {
    atualizarTipoCampos(bloco);
    const tipoSelect = bloco.querySelector('select[name$="-tipo"]');
    tipoSelect.addEventListener('change', () => atualizarTipoCampos(bloco));

    initPreviewImagem(bloco);
  }

  // Inicializa todos os blocos visíveis (normalmente só o primeiro)
  const blocos = formsetDiv.querySelectorAll('.conteudo-bloco');
  blocos.forEach(bloco => {
    if (!bloco.classList.contains('d-none')) {
      initBloco(bloco);
    }
  });

  addBtn.addEventListener('click', () => {
    let total = parseInt(totalForms.value);
    if (total >= 100) return;

    let novoBloco = blocos[0].cloneNode(true);

    novoBloco.querySelectorAll('input, select, textarea').forEach(el => {
      if (el.type === 'checkbox' || el.type === 'radio') {
        el.checked = false;
      } else {
        el.value = '';
      }
    });

    // Limpar campos ocultos 'id' para evitar conflito
    novoBloco.querySelectorAll('input[type="hidden"]').forEach(hiddenInput => {
      if (hiddenInput.name.endsWith('-id')) {
        hiddenInput.value = '';
      }
    });

    const erros = novoBloco.querySelectorAll('.alert.alert-danger');
    erros.forEach(e => e.remove());

    novoBloco.querySelectorAll('input, select, textarea, label').forEach(el => {
      if (el.name) {
        el.name = el.name.replace(/\d+/, total);
      }
      if (el.id) {
        el.id = el.id.replace(/\d+/, total);
      }
      if (el.htmlFor) {
        el.htmlFor = el.htmlFor.replace(/\d+/, total);
      }
    });

    const deleteCheckbox = novoBloco.querySelector('input[type="checkbox"][name$="-DELETE"]');
    if (deleteCheckbox) {
      deleteCheckbox.checked = false;
      deleteCheckbox.closest('.form-check').style.display = 'none';
    }

    // Remove imagem antiga (preview) do bloco clonado
    const imgPreview = novoBloco.querySelector('.preview-img');
    if (imgPreview) {
      imgPreview.setAttribute('src', '#');
      imgPreview.style.display = 'none';
    }

    novoBloco.classList.remove('d-none');

    totalForms.value = total + 1;

    formsetDiv.appendChild(novoBloco);

    initBloco(novoBloco);
  });
});
