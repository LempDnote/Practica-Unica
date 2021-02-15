const tabla = document.querySelector('#Tabla tbody');

function Datos(){
    fetch("archivo.json")
    .then(respuesta => respuesta.json())
    .then(archivo => {
        archivo.forEach(Listado =>{
            const row = document.createElement('tr');
            row.innerHTML += `
                <td>${Listado.Listado}</td>
            `;
            tabla.appendChild(row);
        });       
    })
}
Datos()