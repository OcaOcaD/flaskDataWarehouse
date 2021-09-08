function valida_medico()
{
    let nombre = document.getElementById("nombre").value;
    let apellidos = document.getElementById("nombre").value;
    let genero = document.getElementById("nombre").value;
    let esMedico = document.getElementById("nombre").value;
    let email = document.getElementById("email").value;
    let contrasenia = document.getElementById("password").value;
    let confirmContrasenia = document.getElementById("confirm_password").value;

    if(nombre == '')
    {
        alert('Por favor coloca un nombre...');
        document.getElementById('nombre').focus();
        return false;
    }
    else if(apellidos == '')
    {
        alert('Por favor coloca el o los apellidos...');
        document.getElementById('apellidos').focus()
        return false
    }
    else if(genero == '')
    {
        alert('No haz seleccionado el genero...');
        document.getElementById('genero').focus();
        return false;
    }
    else if(esMedico == '')
    {
        alert('¿Eres medico?');
        document.getElementById('esMedico').focus();
        return false;
    }else if (email == '')
    {
        alert('El email no es correcto o no se ha colocado.');
        document.getElementById('email').focus();
        return false;
    }
    else if(contrasenia == '')
    {
        alert('Coloca una contraseña...')
        document.getElementById('contrasenia').focus();
        return false;
    }
    else if (confirmContrasenia == '')
    {
    {alert('Confirma la contraseña...')}
    }
    if(matchContrasenia() == false)
    {
        alert('Las contraseñas no coinciden');
        return false;
    }
    return true;
}

function validarEmail()
{
    let email = document.getElementById('email').value;
    re=/^([\da-z_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$/
	if(!re.exec(email)){
		alert('email no valido');
	}
	else return true;
}

function matchContrasenia()
{
    let contrasenia = document.getElementById('contrasenia').value;
    let confirmContrasenia = document.getElementById('confirm_password').value;
    if(contrasenia != confirmContrasenia)
    {
        alert('Las contraseñas no coinciden');
    }
    else return true;
}
