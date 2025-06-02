document
  .getElementById("validationForm")
  .addEventListener("input", function (event) {
    const emailPattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    const passwordPattern = /^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$/;
    const phonePattern = /^\d{3}-\d{3}-\d{4}$/;

    // Validar correo electrónico
    const emailInput = document.getElementById("email");
    const emailError = document.getElementById("emailError");
    if (emailPattern.test(emailInput.value)) {
      emailError.textContent = "Correo válido";
      emailError.className = "success";
    } else {
      emailError.textContent = "Correo inválido";
      emailError.className = "error";
    }

    // Validar contraseña
    const passwordInput = document.getElementById("password");
    const passwordError = document.getElementById("passwordError");
    if (passwordPattern.test(passwordInput.value)) {
      passwordError.textContent = "Contraseña válida";
      passwordError.className = "success";
    } else {
      passwordError.textContent =
        "La contraseña debe tener al menos 8 caracteres, incluyendo letras y números";
      passwordError.className = "error";
    }

    // Validar número de teléfono
    const phoneInput = document.getElementById("phone");
    const phoneError = document.getElementById("phoneError");
    if (phonePattern.test(phoneInput.value)) {
      phoneError.textContent = "Número válido";
      phoneError.className = "success";
    } else {
      phoneError.textContent =
        "El número debe estar en el formato 123-456-7890";
      phoneError.className = "error";
    }
  });
