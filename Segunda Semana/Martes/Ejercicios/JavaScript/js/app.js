var miElementoDOM = document.getElementById("miParrafo");
document.getElementById("insertando").innerHTML = "Vamos a agregar contenido de p aqui" + miElementoDOM.innerHTM;

var arregloP = document.getElementsByTagName("p");
alert("Mensaje de alerta" + arregloP.length + "<p> elelementos de este documento");
document.getElementById("insertando").innerHTML = '<span>' + 'El segundo parrafo, con indice 1:' +arregloP[1].innerHTML;+'</span>'

var listaClase = document.getElementsByClassName("miClase");
listaClase[0].style.color = 'red';

document.getElementById("cambiandoAtributo").src="img/2.png";

/*¿Qué etiqueta es el padre?*/

var lista = document.getElementById("miUl");
/*Las listas empiezan en 1*/
lista.removeChild(lista.childNodes[3]);

/*
	appendChild()
	replaceChild()
	createElement()
*/
//Es solo para clases
//document.getElementById("cambiaClase").className +="miDivAmarillo";
/*element.getElementoByID("cambiaClase").setAttribute("src","ruta");*/
/*Escribir el atributo en concreto que queremos cambiar*/
document.getElementByID("cambiaClase").setAttribute("class","miDivAmarillo");