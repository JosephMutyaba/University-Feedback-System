document.addEventListener("DOMContentLoaded", function () {
    // Attach an event listener to the delete form
    const deleteForm = document.getElementById("delete-form");
    deleteForm.addEventListener("submit", function (event) {
      event.preventDefault(); // Prevent the form from submitting normally
  
      // Implement your custom delete logic here, for example, using AJAX to make a DELETE request to the server
  
      // After the deletion is successful, you can redirect the user or show a success message
      alert("Feedback deleted successfully!");
    });
  });
  