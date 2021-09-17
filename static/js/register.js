function validateRegistrationForm() {
	console.log("Testing...")
	return true
	let name = document.getElementById("name").value
	let lastname = document.getElementById("lastname").value
	let sex = document.getElementById("sex").value
	let isMedic = document.getElementById("isMedic").value
	let cedula = document.getElementById("cedula").value
	let email = document.getElementById("email").value
	let password = document.getElementById("password").value
	let confirmPassword = document.getElementById("confirmPassword").value

	if (name == "") {
		alert("Por favor coloca un nombre...")
		document.getElementById("nombre").focus()
		return false
	} else if (lastname == "") {
		alert("Por favor coloca el o los apellidos...")
		document.getElementById("apellidos").focus()
		return false
	} else if (genero == "") {
		alert("No haz seleccionado el genero...")
		document.getElementById("genero").focus()
		return false
	} else if (esMedico == "") {
		alert("¿Eres medico?")
		document.getElementById("esMedico").focus()
		return false
	} else if (email == "") {
		alert("El email no es correcto o no se ha colocado.")
		document.getElementById("email").focus()
		return false
	} else if (contrasenia == "") {
		alert("Coloca una contraseña...")
		document.getElementById("contrasenia").focus()
		return false
	} else if (confirmContrasenia == "") {
		{
			alert("Confirma la contraseña...")
		}
	}
	if (matchContrasenia() == false) {
		alert("Las contraseñas no coinciden")
		return false
	}
	return true
}

function validarEmail() {
	let email = document.getElementById("email").value
	re = /^([\da-z_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$/
	if (!re.exec(email)) {
		alert("email no valido")
	} else return true
}

function matchContrasenia() {
	let contrasenia = document.getElementById("contrasenia").value
	let confirmContrasenia = document.getElementById("confirm_password").value
	if (contrasenia != confirmContrasenia) {
		alert("Las contraseñas no coinciden")
	} else return true
}
