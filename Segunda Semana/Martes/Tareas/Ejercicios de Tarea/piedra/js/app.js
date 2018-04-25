var persona1;
var persona2;
persona1=prompt('Jugador 1 : ¿Piedra, papel o tijera?','');
persona2=prompt('Jugador 2 : ¿Piedra, papel o tijera?','')
document.write('Jugador 1 elijió :' + persona1 + '\n');
document.write('\nJugador 2 elijió :' + persona2 + '\n');
if(persona1 == persona2){
alert("Ninguno ganó");
}else if(persona1 == 'papel'){
if(persona2 == 'piedra'){
  alert("Ganó el jugador 1")
}else if(persona2 == 'tijera'){
  alert("Ganó el jugador 2")
}
}else if(persona1 == 'piedra'){
if(persona2 == 'tijera'){
  alert("Ganó jugador 1")
}else if(persona2 == 'papel'){
  alert("Ganó el jugador2")
}
}else if(persona1 == 'tijera'){
if(persona2 == 'papel'){
  alert("Ganó jugador 1")
}else if(persona2 == 'piedra'){
  alert("Ganó el jugador2")
}
}else{
alert("No se ingresaron datos para jugar");
}