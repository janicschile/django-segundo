function laHoraEs () {
    var fecha = new Date();

    var horas = fecha.getHours(),
        minutos = fecha.getMinutes(),
        segundos = fecha.getSeconds(),
        diaSemana = fecha.getDay(),
        dia = fecha.getDate(),
        mes = fecha.getMonth(),
        year = fecha.getFullYear();

    var semana = [
        'Domingo',
        'Lunes',
        'Martes',
        'Miércoles',
        'Jueves',
        'Viernes',
        'Sábado'
    ];

var meses = [
        'Enero',
        'Febrero',
        'Marzo',
        'Abril',
        'Mayo',
        'Junio',
        'Julio',
        'Agosto',
        'Septiembre',
        'Octubre',
        'Noviembre',
        'Diciembre'
    ];

if (dia < 10) {
    dia = "0" + dia
}
var pSemana = document.getElementById('diaSemana')
pSemana.textContent = semana[diaSemana] +", "   
var pDia = document.getElementById('dia')
pDia.textContent = dia

var pMes = document.getElementById('mes')
pMes.textContent = meses[mes]

var mYear = document.getElementById('year')
mYear.textContent = year

if (horas < 10) {
    horas = "0" + horas
}
var pHora = document.getElementById('horas')
pHora.textContent = horas

if (minutos < 10) {
    minutos = "0" + minutos
}
var pMinuto = document.getElementById('minutos')
pMinuto.textContent = minutos

if (segundos < 10) {
    segundos = "0" + segundos
}
var pSegundos = document.getElementById('segundos')
pSegundos.textContent = segundos
}

setInterval(laHoraEs,1000)