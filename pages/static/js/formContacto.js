const contactos = [];

document.querySelector("#form-contacto").addEventListener('submit', (e)=>{
    e.preventDefault();

    let correoCont = document.querySelector("#correo-cto").value;
    let nombreCont = document.querySelector("#nombre-cto").value;
    let mensajeCont = document.querySelector("#msje-cto").value;
    let esValido = true;

    document.querySelector("#correo-cto").classList.remove("is-invalid");
    document.querySelector("#nombre-cto").classList.remove("is-invalid");
    document.querySelector("#msje-cto").classList.remove("is-invalid");

    if(nombreCont.trim() == ""){
        document.querySelector("#nombre-cto").classList.add("is-invalid");
        esValido = false;
    }else if(correoCont.trim() == ""){
        document.querySelector("#correo-cto").classList.add("is-invalid");
        esValido = false;
    }else if(mensajeCont.trim() == ""){
        document.querySelector("#msje-cto").classList.add("is-invalid");
        esValido = false;
    };
        
    if(esValido){
        let contactoCte = {}

        contactoCte.nombre = nombreCont;
        contactoCte.correo = correoCont;
        contactoCte.mensaje = mensajeCont;
    
        contactos.push(contactoCte);
        Swal.fire("Gracias por escribirnos =)", "Pronto nos contactaremos de vuelta", "info");

        document.querySelector("#nombre-cto").value = "";
        document.querySelector("#correo-cto").value = "";
        document.querySelector("#msje-cto").value = "";
    };

});