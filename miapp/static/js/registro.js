const usuarios = [];

document.querySelector("#formulario").addEventListener('submit', (e)=>{
    e.preventDefault();

    let nombre = document.querySelector("#nombre-txt").value;
    let apellido = document.querySelector("#apellido-txt").value;
    let password = document.querySelector("#pass-password").value;
    let confirmPassword = document.querySelector("#confirmPass-password").value;
    let correo = document.querySelector("#correo-email").value;
    let esValido = true;

    document.querySelector("#nombre-txt").classList.remove("is-invalid");
    document.querySelector("#apellido-txt").classList.remove("is-invalid");
    document.querySelector("#pass-password").classList.remove("is-invalid");
    document.querySelector("#confirmPass-password").classList.remove("is-invalid");
    document.querySelector("#correo-email").classList.remove("is-invalid");

    if(nombre.trim() == ""){
        document.querySelector("#nombre-txt").classList.add("is-invalid");
        esValido = false;
    }else if(apellido.trim() == "") {
        document.querySelector("#apellido-txt").classList.add("is-invalid");
        esValido = false;
    }else if(password.trim() == ""){
        document.querySelector("#pass-password").classList.add("is-invalid");
        esValido = false;
    }else if(confirmPassword !== password ){
        document.querySelector("#confirmPass-password").classList.add("is-invalid");
        esValido = false;
    }else if(correo.trim() == ""){
        document.querySelector("#correo-email").classList.add("is-invalid");
        esValido = false;
    }


    if(esValido){
        let usuario = {};
        usuario.nombre = nombre;
        usuario.apellido = apellido;
        usuario.password = password;
        usuario.correo = correo;

        usuarios.push(usuario);        
        Swal.fire("Felicitaciones!", "Te has registrado exitosamente", "info");
    };
});


