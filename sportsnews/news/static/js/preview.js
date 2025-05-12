document.addEventListener("DOMContentLoaded", function () {
    const input = document.getElementById("id_imagem");
    const preview = document.getElementById("preview-img");
  
    if (input) {
      input.addEventListener("change", function () {
        const file = this.files[0];
        if (file) {
          const reader = new FileReader();
  
          reader.onload = function (e) {
            preview.setAttribute("src", e.target.result);
            preview.style.display = "block";
          }
  
          reader.readAsDataURL(file);
        } else {
          preview.setAttribute("src", "#");
          preview.style.display = "none";
        }
      });
    }
  });
  