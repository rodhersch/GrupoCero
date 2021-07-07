function confirmarEliminar(id) {
  Swal.fire({
    title: "¿Estás seguro?",
    text: "No podrás deshacer este cambio",
    icon: "warning",
    showCancelButton: true,
    confirmButtonColor: "#3085d6",
    cancelButtonColor: "#d33",
    confirmButtonText: "Sí, eliminar",
    cancelButtonText: "Cancelar",
  }).then((result) => {
    if (result.isConfirmed) {
      window.location.href = "/eliminar-proveedor/" + id;
    }
  });
}
