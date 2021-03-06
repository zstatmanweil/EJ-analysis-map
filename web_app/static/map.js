mapboxgl.accessToken = 'pk.eyJ1IjoienN0YXRtYW53ZWlsIiwiYSI6ImNqbWY3b3V2cjAyMWUzcXBmNXRzdHNnOWEifQ.E-JUGH3ab30ya_NXealg_A';

// Set bounds
var bounds = [
    [-125.339515, 23.089636], // Southwest Coordinates
    [-62.346295, 50.046593] // Norteast Coordinates
];
// Initialize map
var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/light-v10',
    center: [-74.385210, 40.118365], // long, lat
    zoom: 7,
    //    maxBounds: bounds // Sets bounds as max
});

// Add Geocoder
map.addControl(new MapboxGeocoder({
    accessToken: mapboxgl.accessToken
}));
// Add navigation control
map.addControl(new mapboxgl.NavigationControl());
function mapReset() {
}
map.addControl(new mapboxgl.FullscreenControl());
map.on('load', function () {

    // Add lists for choropleth
    var vioColors = ['#FFEDA0', '#FEB24C', '#FC4E2A', '#BD0026', '#800026'];
    var demoColors = ['#d0c2d6', '#b69bc1', '#805591', '#501966', '#2a0738']; // update

    // All violations
    var vioBreaks = [5, 15, 35, 65, 128];
    // Health violations
    var healthVioBreaks = [1, 2, 4, 5, 10];
    // Percent below the poverty line (areal weighting) 
    var percPOCBreaks = [0.15, 0.28, 0.46, 0.69, 0.98];
    var percPOCBreaksDisplay = [15, 28, 46, 69, 98];
    // Percent below the poverty line (areal weighting)
    var percPovBreaks = [0.05, 0.08, 0.14, 0.24, 0.47];
    var percPovBreaksDisplay = [5, 8, 14, 24, 47];
    // Percent below the poverty line (county-level analysis)
    var percPOCBreaksCounty = [21, 32, 49, 59, 71];
    // Percent below the poverty line (county-level analysis)
    var percPovBreaksCounty = [5, 8, 11, 15, 17];

    mapReset();
    // Add NJ boundary source
    map.addSource("NJ", {
        type: "geojson",
        data: 'https://raw.githubusercontent.com/zstatmanweil/EJ-analysis-map/master/web_app/data/NJ_boundary.geojson'
    });
    // Add NJ boundary layer
    map.addLayer({
        'id': 'new_jersey',
        'type': 'line',
        'source': 'NJ',
        'layout': {},
        'paint': {
            'line-color': '#070705'
        }
    });
    // Add health violation data layer
    map.addLayer({
        'id': 'Health-based SDWA Violations',
        'type': 'fill',
        "source": {
            type: 'vector',
            url: 'mapbox://zstatmanweil.01gjua4s'
        },
        'layout': {
            'visibility': 'none'
        },
        "source-layer": "pws_aw",
        'paint': {
            'fill-color': {
                'property': 'health_violations',
                'stops': [
                    [healthVioBreaks[0], vioColors[0]],
                    [healthVioBreaks[1], vioColors[1]],
                    [healthVioBreaks[2], vioColors[2]],
                    [healthVioBreaks[3], vioColors[3]],
                    [healthVioBreaks[4], vioColors[4]],
                ]
            },
            'fill-opacity': 0.9,
            'fill-outline-color': '#6d6d51'
        }
    });
    // Add all violations
    map.addLayer({
        'id': 'Total SDWA Violations',
        'type': 'fill',
        "source": {
            type: 'vector',
            url: 'mapbox://zstatmanweil.01gjua4s'
        },
        'layout': {
            'visibility': 'none'
        },
        "source-layer": "pws_aw",
        'paint': {
            'fill-color': {
                'property': 'all_violations',
                'stops': [
                    [vioBreaks[0], vioColors[0]],
                    [vioBreaks[1], vioColors[1]],
                    [vioBreaks[2], vioColors[2]],
                    [vioBreaks[3], vioColors[3]],
                    [vioBreaks[4], vioColors[4]],
                ]
            },
            'fill-opacity': 0.9,
            'fill-outline-color': '#6d6d51'
        }
    });
    // Add percent below the poverty line (areal weighting)
    map.addLayer({
        'id': 'Percentage Below the Poverty Line (areal weighting)',
        'type': 'fill',
        "source": {
            type: 'vector',
            url: 'mapbox://zstatmanweil.01gjua4s'
        },
        'layout': {
            'visibility': 'none'
        },
        "source-layer": "pws_aw",
        'paint': {
            'fill-color': {
                'property': 'perc_pov',
                'stops': [
                    [percPovBreaks[0], demoColors[0]],
                    [percPovBreaks[1], demoColors[1]],
                    [percPovBreaks[2], demoColors[2]],
                    [percPovBreaks[3], demoColors[3]],
                    [percPovBreaks[4], demoColors[4]],
                ]
            },
            'fill-opacity': 0.9,
            'fill-outline-color': '#6d6d51'
        }
    });
    // Add percent POC (areal weighting)
    map.addLayer({
        'id': 'Percentage POC (areal weighting)',
        'type': 'fill',
        "source": {
            type: 'vector',
            url: 'mapbox://zstatmanweil.01gjua4s'
        },
        'layout': {
            'visibility': 'none'
        },
        "source-layer": "pws_aw",
        'paint': {
            'fill-color': {
                'property': 'perc_POC',
                'stops': [
                    [percPOCBreaks[0], demoColors[0]],
                    [percPOCBreaks[1], demoColors[1]],
                    [percPOCBreaks[2], demoColors[2]],
                    [percPOCBreaks[3], demoColors[3]],
                    [percPOCBreaks[4], demoColors[4]],
                ]
            },
            'fill-opacity': 0.9,
            'fill-outline-color': '#6d6d51'
        }
    });

    // Add percent below the poverty line (county-level analysis)
    map.addLayer({
        'id': 'Percentage Below the Poverty Line (county-level analysis)',
        'type': 'fill',
        "source": {
            type: 'vector',
            url: 'mapbox://zstatmanweil.8q8hf0qi'
        },
        'layout': {
            'visibility': 'none'
        },
        "source-layer": "pws_county",
        'paint': {
            'fill-color': {
                'property': 'perc_pov',
                'stops': [
                    [percPovBreaksCounty[0], demoColors[0]],
                    [percPovBreaksCounty[1], demoColors[1]],
                    [percPovBreaksCounty[2], demoColors[2]],
                    [percPovBreaksCounty[3], demoColors[3]],
                    [percPovBreaksCounty[4], demoColors[4]],
                ]
            },
            'fill-opacity': 0.9,
            'fill-outline-color': '#6d6d51'
        }
    });
    // Add percent POC (county-level analysis)
    map.addLayer({
        'id': 'Percentage POC (county-level analysis)',
        'type': 'fill',
        "source": {
            type: 'vector',
            url: 'mapbox://zstatmanweil.8q8hf0qi'
        },
        'layout': {
            'visibility': 'none'
        },
        "source-layer": "pws_county",
        'paint': {
            'fill-color': {
                'property': 'perc_POC',
                'stops': [
                    [percPOCBreaksCounty[0], demoColors[0]],
                    [percPOCBreaksCounty[1], demoColors[1]],
                    [percPOCBreaksCounty[2], demoColors[2]],
                    [percPOCBreaksCounty[3], demoColors[3]],
                    [percPOCBreaksCounty[4], demoColors[4]],
                ]
            },
            'fill-opacity': 0.9,
            'fill-outline-color': '#6d6d51'
        }
    });

    // Settig up for Toggling between layers
    var toggleableLayerIds = ['Total SDWA Violations',
        'Health-based SDWA Violations',
        'Percentage POC (areal weighting)',
        'Percentage Below the Poverty Line (areal weighting)',
        'Percentage POC (county-level analysis)',
        'Percentage Below the Poverty Line (county-level analysis)'];

    // Associated breaks = 
    var breakNames = [vioBreaks,
        healthVioBreaks,
        percPOCBreaksDisplay,
        percPovBreaksDisplay,
        percPOCBreaksCounty,
        percPovBreaksCounty
    ]
    // Toggle between layers
    for (var i = 0; i < toggleableLayerIds.length; i++) {
        var id = toggleableLayerIds[i];

        var link = document.createElement('a');
        link.href = '#';
        link.className = '';
        link.textContent = id;

        link.onclick = function (e) {
            var clickedLayer = this.textContent;
            e.preventDefault();
            e.stopPropagation();

            var visibility = map.getLayoutProperty(clickedLayer, 'visibility');

            if (visibility === 'visible') {
                map.setLayoutProperty(clickedLayer, 'visibility', 'none');
                this.className = '';
            } else {
                // Turn off other layers and turn on selected layer 
                var a = document.getElementById('menu').getElementsByTagName('a');
                for (var j = 0; j < a.length; j++) {
                    var elem = a[j];
                    elem.className = '';
                    map.setLayoutProperty(elem.textContent, 'visibility', 'none');
                }

                // Turn on selected layer
                map.setLayoutProperty(clickedLayer, 'visibility', 'visible')
                this.className = 'active';

                // Remove any existing legend prior to adding one
                $('.legend-key').remove();
                $("#legend").find('span').remove()

                // Add legend for selected layer
                // First select colors
                if (clickedLayer.includes('Vio')) {
                    var colors = vioColors;
                } else {
                    var colors = demoColors;
                }

                // Select breaks for legend
                var i = toggleableLayerIds.indexOf(clickedLayer);
                var breaks = breakNames[i];

                // Add legend
                var legend = document.getElementById('legend');
                var item = document.createElement('div');
                var key = document.createElement('span');
                key.className = 'map-overlay';

                var value = document.createElement('span');
                value.innerHTML = clickedLayer;
                item.appendChild(value);
                legend.appendChild(item);

                // Create Key 
                for (i = 0; i < breaks.length; i++) {
                    var layer = breaks[i];
                    var color = colors[i];
                    var item = document.createElement('div');
                    var key = document.createElement('span');
                    key.className = 'legend-key';
                    key.style.backgroundColor = color;

                    var value = document.createElement('span');
                    value.innerHTML = layer;
                    item.appendChild(key);
                    item.appendChild(value);
                    legend.appendChild(item);
                };

                // Add hover with information about public water system under mouse
                // Identify type of data being shown
                if (clickedLayer === 'Total SDWA Violations') {
                    var type = 'total SDWA violations';
                    var property = 'all_violations';
                } else if (clickedLayer === 'Health-based SDWA Violations') {
                    var type = 'health-based SDWA violations';
                    var property = 'health_violations';
                } else if (clickedLayer.includes('Pov')){
                    var type = '%';
                    var property = 'perc_pov';
                } else {
                    var type = '%';
                    var property = 'perc_POC';
                }

                map.on('mousemove', clickedLayer, function (e) {
                    var pws = map.queryRenderedFeatures(e.point, {
                        layers: [clickedLayer]
                    })

                    // Check if it is the areal weighting data because then percentages need to be multiplied by 100
                    if (clickedLayer.includes('(areal')) {
                        var pws_value = Math.floor(pws[0].properties[property]*100);
                    } else {
                        var pws_value = Math.floor(pws[0].properties[property]);
                    }

                    // Add pws value to overlay box
                    document.getElementById('pd').innerHTML = '<h5> PWS ID: ' + pws[0].properties.PWID + '</h5><p><em>' + pws_value + ' ' + type + '</em></p>';
                });
                map.on('mouseleave', clickedLayer, function (e) {
                    document.getElementById('pd').innerHTML = '<p>Hover over a water system</p>';
                });

            };
        };

        var layers = document.getElementById('menu');
        layers.appendChild(link);
    }

});