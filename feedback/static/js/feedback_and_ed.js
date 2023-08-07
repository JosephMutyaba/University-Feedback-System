
$(document).ready(function() {
    // Check if the name field is empty.
    $("#name").on("blur", function() {
      if ($(this).val() == "") {
        $(this).next().text("Please enter your name.");
      } else {
        $(this).next().text("");
      }
    });
  
    // Check if the email field is valid.
    $("#email").on("blur", function() {
      var emailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
      if (!emailRegex.test($(this).val())) {
        $(this).next().text("Please enter a valid email address.");
      } else {
        $(this).next().text("");
      }
    });
  
    // Show a notification if the form is submitted successfully.
    $(document).on("submit", "form", function(event) {
      event.preventDefault();
  
      // Submit the form data to the server.
      $.ajax({
        url: "/feedback/",
        method: "POST",
        data: $(this).serialize(),
        success: function(data) {
          // Show the notification.
          $("#success").show();
        },
        error: function(error) {
          // Show an error message.
          alert(error.responseText);
        }
      });
    });
  });
  