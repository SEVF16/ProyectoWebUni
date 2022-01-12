tinymce.init({
    selector: '#desc-txt',
    height: 200,
    menubar: false,
    plugins: [
      'advlist autolink lists link image charmap print preview anchor',
      'searchreplace visualblocks code fullscreen',
      'insertdatetime media table paste code help wordcount'
    ],
    toolbar: 'undo redo | formatselect | ' +
    'bold italic backcolor | alignleft aligncenter ' +
    'alignright alignjustify | bullist numlist outdent indent | ' +
    'removeformat | help',
    content_style: 'body { font-family:Helvetica,Arial,sans-serif; font-size:14px }'
  });

const mostrarPersonaje = function(){
    
    const molde = document.querySelector(".molde-detalle").cloneNode(true);
    Swal.fire({
        html: molde.innerHTML
    })
};
const cargarProductos = function(){
    const contenedor = document.querySelector("#contenedor-personajes");
    const molde = document.querySelector(".molde-personaje");
    let copia = molde.cloneNode(true); 
    for (var i = 0; i < 9; i++) {
    copia.querySelector(".btn-ver-producto").addEventListener("mouseover", mostrarPersonaje);
    contenedor.appendChild(copia);
    }
};


document.addEventListener("DOMContentLoaded", ()=>{

    cargarProductos();
});

const artistas = [];
const eliminar = async function(){

    let res = await Swal.fire({
        title: "¿Desea eliminar el registro?",
        showCancelButton: true,
        confirmButtonText: "Eliminar artista"
      });
      if(res.isConfirmed){
        //1.-Saber qué botón fué el que se apretó
      
        //2.-Sacar el número del boton
        let nro = this.nro;
        //3.-Eliminar el pokémon de la lista
        artistas.splice(nro,1);
        //4.-Recargar la tabla
        cargarTabla();
      }else{
        Swal.fire("Operación cancelada");
      }
    };

const cargarTabla = () =>{
    let tbody = document.querySelector("#tbody-artista");
    // tbody.innerHTML = "";

    for(let i = 3; i < artistas.length; i++){
        let a = artistas[i];
        let tr = document.createElement("tr");
        let tdNombre = document.createElement("td");
        let tdEstilo = document.createElement("td");
        let tdNro = document.createElement("td");
        let tdNrObras = document.createElement("td");
        let tdAcciones = document.createElement("td");

        tdNombre.innerText = a.nombre;
        tdNombre.classList.add("text-center");
        tdEstilo.innerText = a.estilo;
        tdEstilo.classList.add("text-center");
        tdNrObras.innerText = a.nrObras;
        tdNrObras.classList.add("text-center");
        tdNro.innerText = i + 1;

        let boton = document.createElement("button");
        boton.nro = i;
        boton.addEventListener("click", eliminar);
        boton.innerText = "Eliminar registro";
        boton.classList.add("btn", "btn-danger");
        tdAcciones.appendChild(boton);
        tdAcciones.classList.add("text-center");

        tr.appendChild(tdNro);
        tr.appendChild(tdNombre);
        tr.appendChild(tdEstilo);
        tr.appendChild(tdNrObras);
        tr.appendChild(tdAcciones);
        tbody.appendChild(tr);
    };
};

document.querySelector("#form-artista").addEventListener('submit', (e)=>{
    e.preventDefault();

    let nombre = document.querySelector("#nombre-txt").value;
    let estilo = document.querySelector("#estilo-select").value;
    let nrObras = document.querySelector("#obras-select").value;
    let esValido = true;
    document.querySelector("#nombre-txt").classList.remove("is-invalid");

    if(nombre.trim() == ""){
        document.querySelector("#nombre-txt").classList.add("is-invalid");
        esValido = false;
    }

    if(esValido){
        let artista = {};
        artista.nombre = nombre;
        artista.estilo = estilo;
        artista.nrObras = nrObras;

        artistas.push(artista);
        cargarTabla();
        Swal.fire("Registro exitoso", "Nuevo artista registrado", "info");
    }
});


document.querySelector("#limpiar-btn").addEventListener("click", () =>{
    //limpiar elementos
    //limpiar un nombre
    document.querySelector("#nombre-txt").value = "";
    document.querySelector("#estilo-select").value = "1";
    document.querySelector("#obras-select").value = "1";
  });




