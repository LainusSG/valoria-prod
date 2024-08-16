
console.log("holita")
function readURL(input) {
    if (input.files && input.files[0]) {
      var reader = new FileReader();
      reader.onload = function(e) {
        // Asignamos el atributo src a la tag de imagen
        $('#imagenmuestra').attr('src', e.target.result);
      }
      reader.readAsDataURL(input.files[0]);
    }
  }
  
  // El listener va asignado al input
  $("#file-upload").change(function() {
    readURL(this);
  });

