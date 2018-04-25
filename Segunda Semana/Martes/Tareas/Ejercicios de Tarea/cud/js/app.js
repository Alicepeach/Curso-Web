var list = document.createElement("nuevoNodo");
var id = prompt('Escribe : add = añadir, rem = quitar, mod = modificar');
 if(id == 'add'){
    var text = prompt('Ingrese el texto que desea agregar', '');
    document.getElementById("add").appendChild(list);
    var crearNodo = document.createTextNode(text);
    list.appendChild(crearNodo);
}else if(id == 'rem'){
    var elim = prompt("Ingrese el numero que desea eliminar");
    document.getElementById("rem").removeChild(list.childNodes[elim]);  
}else if(id == 'mod'){
    var reem = prompt('Ingrese el texto que va a reemplazar');
    var nuevo = prompt('Ingrese el texto nuevo');
    var niu = document.createTextNode(nuevo);
    document.getElementById("mod").replaceChild(reem, niu);
  }