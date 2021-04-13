var pressedKeys = {};
window.onkeyup = function(e) { pressedKeys[e.keyCode] = false; }
window.onkeydown = function(e) { pressedKeys[e.keyCode] = true; }


var map = L.map('map', {
    center: [38.0353437, -78.5064942],
    zoom: 16
});

map.on("click", function(e) {
    if (pressedKeys[17]) {
        console.log(pressedKeys);
        var marker = new L.Marker([e.latlng.lat, e.latlng.lng]).addTo(map);
        console.log(marker.getLatLng());
        var circle = new L.circle([e.latlng.lat, e.latlng.lng], 250).addTo(map);
        circle.on('mouseover', function() {
            map.dragging.disable();
        });

        circle.on('mouseout', function() {
            map.dragging.enable();
        });

        circle.on({
          'mousedown': function () {
            if (pressedKeys[17]) {
                map.on('mousemove', function (e) {
                  circle.setLatLng(e.latlng);
                });
            }
          }
       }); 
    }
});

map.on('mouseup',function(e){
 map.removeEventListener('mousemove');
})

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
