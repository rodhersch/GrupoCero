function confirmarEliminar(id) {
  Swal.fire({
<<<<<<< HEAD
    title: "¿Estás seguro?",
    text: "No podrás deshacer este cambio",
=======
    title: "Estas seguro?",
    text: "No podrás deshacer este cambio!",
>>>>>>> 854fc337b84d02f50086dcf3c6f5c6a577c7a0e7
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#3085d6",
    cancelButtonColor: "#d33",
<<<<<<< HEAD
    confirmButtonText: "Sí, eliminar",
    cancelButtonText: "Cancelar",
  }).then((result) => {
    if (result.isConfirmed) {
      window.location.href = "/eliminar-proveedor/" + id;
=======
    confirmButtonText: "Si, Elimínalo!",
    cancelButtonText: "Cancelar",
  }).then((result) => {
    if (result.isConfirmed) {
      window.location.href = "/eliminar_proveedor/" + id;
>>>>>>> 854fc337b84d02f50086dcf3c6f5c6a577c7a0e7
    }
  });
}
