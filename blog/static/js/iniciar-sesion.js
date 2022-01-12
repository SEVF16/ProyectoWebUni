document.querySelector("#form-login").addEventListener('submit', (e)=>{
    e.preventDefault();

    let correo = document.querySelector("#email-input").value;
    let pass = document.querySelector("#pass-input").value;
    let esValido = true;

    document.querySelector("#email-input").classList.remove("is-invalid");
    document.querySelector("#pass-input").classList.remove("is-invalid");

    if(correo.trim() == ""){
        document.querySelector("#email-input").classList.add("is-invalid");
        esValido = false;
    }else if(pass.trim() == ""){
        document.querySelector("#pass-input").classList.add("is-invalid");
        esValido = false;
    };

    if(esValido){
        Swal.fire("Login exitoso", "success");
    };
});

