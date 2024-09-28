function App() {}

window.onload = function(event) {
    var app = new App();
    window.app = app;  // Hacer que app esté disponible globalmente
}

App.prototype.processingButton = function(event) {
    console.log("Botón presionado");

    const btn = event.currentTarget;
    const carruselList = event.currentTarget.parentNode;
    const track = event.currentTarget.parentNode.querySelector('#track');
    const carrusel = track.querySelectorAll('.carrusel');

    const carruselWidth = carrusel[0].offsetWidth;
    const trackWidth = track.offsetWidth;
    const listWidth = carruselList.offsetWidth;

    let leftPosition;
    track.style.left === "" ? leftPosition = 0 : leftPosition = parseFloat(track.style.left.slice(0, -2)) * -1;

    // Verificar si es el botón anterior o siguiente
    btn.dataset.button === "button-prev" ? prevAction(leftPosition, carruselWidth, track) : nextAction(leftPosition, trackWidth, listWidth, carruselWidth, track);
}

let prevAction = (leftPosition, carruselWidth, track) => {
    // Asegurarse de no sobrepasar el límite izquierdo
    if (leftPosition > 0) {
        track.style.left = `${-1 * (leftPosition - carruselWidth)}px`;
    } else {
        track.style.left = `0px`;  // Volver al inicio si está al límite
    }
}

let nextAction = (leftPosition, trackWidth, listWidth, carruselWidth, track) => {
    // Asegurarse de no sobrepasar el límite derecho
    if (leftPosition < (trackWidth - listWidth)) {
        track.style.left = `${-1 * (leftPosition + carruselWidth)}px`;
    }
}


