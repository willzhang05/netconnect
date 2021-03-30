var map = L.map('map', {
    center: [38.0353437, -78.5064942],
    zoom: 16
});

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

if (window.navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(setPosition);
}

function setPosition(position) {
    const latitude = position.coords.latitude;
    const longitude = position.coords.longitude;
    map.setView(L.latLng(latitude, longitude));
}
