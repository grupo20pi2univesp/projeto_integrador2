// API MAPS

function initMap() {
    // Coordenadas para o centro do mapa
    const center = { lat: -22.610097775135777, lng: -45.180156345735455 };

    // Cria o mapa
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 15,
        center: center,
    });

    // Adiciona um marcador
    const marker = new google.maps.Marker({
        position: center,
        map: map,
        title: "Piquete - São Paulo, Brasil",
    });
}