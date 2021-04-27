function getDistance(origin, destination) {
    // return distance in meters
    var lon1 = toRadian(origin[1]),
        lat1 = toRadian(origin[0]),
        lon2 = toRadian(destination[1]),
        lat2 = toRadian(destination[0]);

    var deltaLat = lat2 - lat1;
    var deltaLon = lon2 - lon1;

    var a = Math.pow(Math.sin(deltaLat/2), 2) + Math.cos(lat1) * Math.cos(lat2) * Math.pow(Math.sin(deltaLon/2), 2);
    var c = 2 * Math.asin(Math.sqrt(a));
    var EARTH_RADIUS = 6371;
    return c * EARTH_RADIUS * 1000;
}

function toRadian(degree) {
    return degree * Math.PI/180;
}

var pressedKeys = {};
window.onkeyup = function(e) { pressedKeys[e.keyCode] = false; }
window.onkeydown = function(e) { pressedKeys[e.keyCode] = true; }



var interestMarker = null;
var interestCircle = null;
var enableSetMarker = false;
var enableSetRadius = false;

var dragStart = null;

function setCircle(e) {
    if (interestCircle == null) {
        interestCircle = new L.circle(e.latlng, 0).addTo(map);
        interestCircle.on('mouseover', function() {
            map.dragging.disable();
        });

        interestCircle.on('mouseout', function() {
            map.dragging.enable();
        });
        interestCircle.on("mousedown", function(e) {
            dragStart = interestCircle.getLatLng();
        });
    } else {
        interestCircle.setLatLng(e.latlng);
    }
}

function setMarker(e) {
    if (interestMarker == null) {
        interestMarker = new L.Marker(e.latlng).addTo(map);

        interestMarker.on('mouseover', function() {
            map.dragging.disable();
        });

        interestMarker.on('mouseout', function() {
            map.dragging.enable();
        });

        interestMarker.on("mousedown", function(e) {
            if (enableSetRadius) {
                dragStart = e.latlng;
                setCircle(e);
            }
        });

    } else {
        interestMarker.setLatLng(e.latlng);
    }
}

function beginSetMarker(e) {
    enableSetMarker = true;
}
function beginSetRadius(e) {
    enableSetRadius = true;
}

var map = L.map('map', {
        contextmenu: true,
        contextmenuWidth: 200,
        contextmenuItems: [
            {
                text: 'Set location of interest',
                callback: beginSetMarker
            },
            {
                text: 'Set radius of interest',
                callback: beginSetRadius
            },
        ],
        center: [38.0353437, -78.5064942],
        zoom: 16
});

map.on("mousemove", function(e) {
    if (dragStart != null && enableSetRadius) {
        let radius = getDistance([dragStart.lat, dragStart.lng], [e.latlng.lat, e.latlng.lng]);
        interestCircle.setRadius(radius);
    }
});

map.on("mouseup", function(e) {
    if (dragStart != null && enableSetRadius) {
        enableSetRadius = false;
        dragStart = null;
    }
});
map.on("mousedown", function(e) {
    if (enableSetMarker) {
        setMarker(e);
        if (interestCircle != null) {
            interestCircle.setLatLng(e.latlng);
        }
        enableSetMarker = false;
    }
});

map.on("contextmenu", function(e) {
    let coords = e.latlng;
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
