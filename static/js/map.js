var pressedKeys = {};
window.onkeyup = function(e) {
    pressedKeys[e.keyCode] = false;
}
window.onkeydown = function(e) {
    pressedKeys[e.keyCode] = true;
}

function getDistance(origin, destination) {
    // return distance in meters
    var lon1 = toRadian(origin[1]),
        lat1 = toRadian(origin[0]),
        lon2 = toRadian(destination[1]),
        lat2 = toRadian(destination[0]);

    var deltaLat = lat2 - lat1;
    var deltaLon = lon2 - lon1;

    var a = Math.pow(Math.sin(deltaLat / 2), 2) + Math.cos(lat1) * Math.cos(lat2) * Math.pow(Math.sin(deltaLon / 2), 2);
    var c = 2 * Math.asin(Math.sqrt(a));
    var EARTH_RADIUS = 6371;
    return c * EARTH_RADIUS * 1000;
}

function toRadian(degree) {
    return degree * Math.PI / 180;
}

function updateAPI() {
    let currentPos = searchMarker.getLatLng();
    let currentRadius = 0;
    if (searchCircle != null) {
        currentRadius = searchCircle.getRadius();
    }
    var data = {
        lat: currentPos.lat,
        lng: currentPos.lng,
        radius: (currentRadius / 1609).toFixed(2)
    };
    fetch("/marker/", {
        method: "POST",
        headers: {
            "X-CSRFToken": CSRF_TOKEN,
        },
        body: JSON.stringify(data)
    }).then(
        function(res) {
            return res.json();
        }
    ).then(
        function(data) {
            console.log(data);
        }
    );
}

var searchMarker = null;
var searchCircle = null;
var enableSetMarker = false;
var enableSetRadius = false;

var dragStart = null;

function setCircle(coords) {
    if (searchCircle == null) {
        searchCircle = new L.circle(coords, 0).addTo(map);

        searchCircle.on('mouseover', function() {
            if (enableSetRadius) {
                map.dragging.disable();
            }
        });
        searchCircle.on('mouseout', function() {
            map.dragging.enable();
        });
        searchCircle.on("mousedown", function(e) {
            dragStart = searchCircle.getLatLng();
        });
    } else {
        searchCircle.setLatLng(coords);
    }
}

function setMarker(coords) {
    if (searchMarker == null) {
        searchMarker = new L.Marker(coords).addTo(map);

        searchMarker.on('mouseover', function() {
            if (enableSetMarker) {
                map.dragging.disable();
            }
        });

        searchMarker.on('mouseout', function() {
            map.dragging.enable();
        });

        searchMarker.on('mouseup', function() {
            searchMarker.dragging.disable();
            updateAPI();
        });

        searchMarker.on("mousedown", function(e) {
            if (enableSetRadius) {
                dragStart = e.latlng;
                setCircle(e.latlng);
            }
        });

        searchMarker.on("drag", function(e) {
            setCircle(e.latlng);
        });

    } else {
        searchMarker.setLatLng(coords);
    }
}

function beginSetMarker(e) {
    enableSetMarker = true;
    if (searchMarker != null) {
        searchMarker.dragging.enable();
    }
}

function beginSetRadius(e) {
    enableSetRadius = true;
}

var map = L.map('map', {
    contextmenu: true,
    contextmenuWidth: 200,
    contextmenuItems: [{
            text: 'Set location of search',
            callback: beginSetMarker
        },
        {
            text: 'Set radius of search',
            callback: beginSetRadius
        },
    ],
    center: [38.0353437, -78.5064942],
    zoom: 16
});

map.on("mousemove", function(e) {
    if (dragStart != null && enableSetRadius) {
        let radius = getDistance([dragStart.lat, dragStart.lng], [e.latlng.lat, e.latlng.lng]);
        searchCircle.setRadius(radius);
    }
});

map.on("mouseup", function(e) {
    if (dragStart != null && enableSetRadius) {
        updateAPI();
        enableSetRadius = false;
        dragStart = null;
    }
});
map.on("mousedown", function(e) {
    if (enableSetMarker) {
        setMarker(e.latlng);
        if (searchCircle != null) {
            searchCircle.setLatLng(e.latlng);
        }
        enableSetMarker = false;
    }
});

map.on("contextmenu", function(e) {});

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

/*if (window.navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(setPosition);
}*/

function setPosition(position) {
    const latitude = position.coords.latitude;
    const longitude = position.coords.longitude;
    map.setView(L.latLng(latitude, longitude));
}

function setData(data) {
    console.log(data);
    if (data.lat != null && data.lng != null) {
        setMarker([data.lat, data.lng]);
        if (data.radius != null) {
            map.setView(L.latLng(data.lat, data.lng));
            setCircle(L.latLng(data.lat, data.lng))
            searchCircle.setRadius((data.radius * 1609).toFixed(2));
        }
    }
}

fetch('/marker/')
    .then((response) => {
        return response.json();
    })
    .then(data => setData(data));