function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 39.76777970380029, lng: -102.67985765608903},
        zoom: 5,
        mapId: '6876145de3a50763'
        });
    
    // Name
    // Lat, Long
    // Image URL
    //scaledSize width, height
    const colleges = [
        [
            "University of Texas at Austin",
            30.28722163515074,
            -97.7291850310966,
            "longhorn.jpg",
            38,
            31
        ],
        [
            "Rice University",
            29.71738476421553,
            -95.40175610042736,
            "rice.jpg",
            38,
            31
        ],
        [
            "Brown University",
            41.826963652875484,
            -71.40254820181998,
            "brown.jpg",
            38,
            31
        ],
        [
            "California Institute of Technology",
            34.13787958449847,
            -118.12527973102935,
            "caltech.jpg",
            38,
            31
        ],
        [
            "Carnigie Mellon University",
            40.4432353400532,
            -79.9428606309003,
            "cmu.jpg",
            38,
            31
        ],
        [
            "Columbia University",
            40.80747051326415,
            -73.96248687137893,
            "columbia.jpg",
            38,
            31
        ],
        [
            "Cornell University",
            42.45333835489112,
            -76.47336322716723,
            "cornell.jpg",
            38,
            31
        ],
        [
            "Dartmouth College",
            43.7044716031998,
            -72.28881151917287,
            "dartmouth.jpg",
            38,
            31
        ],
        [
            "Duke University",
            36.001460498731376,
            -78.93830370400238,
            "duke.jpg",
            38,
            31
        ],
        [
            "Georgia Institute of Technology",
            33.77568020690832, 
            -84.39631718870562,
            "gatech.jpg",
            38,
            31
        ],
        [
            "Harvard University",
            42.3770425075226,
            -71.1166386443518,
            "harvard.jpg",
            38,
            31
        ],
        [
            "Johns Hopkins University",
            39.32998426803128,
            -76.62080738062956,
            "johnshopkins.jpg",
            38,
            31
        ],
        [
            "Massachusetts Institute of Technology",
            42.36017818496631,
            -71.0950075799713,
            "mit.jpg",
            38,
            31
        ],
        [
            "Princeton University",
            40.34294389850641,
            -74.65486546325741,
            "princeton.jpg",
            38,
            31
        ],
        [
            "Purdue University",
            40.42332150380552,
            -86.92122678857028,
            "purdue.jpg",
            38,
            31
        ],
        [
            "Stanford University",
            37.428003806728285,
            -122.17064111398952,
            "stanford.jpg",
            38,
            31
        ],
        [
            "Texas A&M University",
            30.606581579292026,
            -96.35679768691742,
            "tamu.jpg",
            38,
            31
        ],
        [
            "Texas Tech University",
            33.58411730202425,
            -101.87814120161748,
            "txtech.jpg",
            38,
            31,
        ],
        [
            "University of California at Berkely",
            37.871899625806385,
            -122.25875567773659,
            "berkeley.jpg",
            38,
            31
        ],
        [
            "University of California at San Diego",
            32.88006038094516,
            -117.23428172308752,
            "ucsd.jpg",
            38,
            31
        ],
        [
            "University of California at Santa Barbara",
            34.41377700867955,
            -119.84906501937226,
            "ucsb.jpg",
            38,
            31
        ],
        [
            "University of Illinois at Urbana-Champagne",
            40.10173070406735,
            -88.22628173761909,
            "uiuc.jpg",
            38,
            31
        ],
        [
            "University of Maryland at College Park",
            38.986108155657234,
            -76.9435057520451,
            "umd.jpg",
            38,
            31
        ],
        [
            "University of Michigan at Ann Arbor",
            42.278003888447735,
            -83.73820264435412,
            "umich.jpg",
            38,
            31
        ],
        [
            "University of North Carolina at Chapel Hill",
            35.90475624033239,
            -79.04761819344438,
            "unc.jpg",
            38,
            31
        ],
        [
            "University of Pennsylvania",
            39.9522352284501,
            -75.19329953275468,
            "upenn.jpg",
            38,
            31
        ],
        [
            "University of Southern California",
            34.02220960422883,
            -118.28513845986623,
            "usc.jpg",
            38,
            31
        ],
        [
            "University of Texas at Dallas",
            32.985607486695265,
            -96.75141684520916,
            "utd.jpg",
            38,
            31
        ],
        [
            "University of Virginia",
            38.033119980966696,
            -78.50744887121373,
            "uva.jpg",
            38,
            31
        ],
        [
            "University of Washington-Seattle",
            47.6552772645618,
            -122.30365937674365,
            "washington.jpg",
            38,
            31
        ],
        [
            "University of Wisconsin at Madison",
            43.07652144803823,
            -89.41240167132656,
            "wisconsin.jpg",
            38,
            31
        ],
        [
            "Vanderbilt University",
            36.14483267573013,
            -86.80287491696127,
            "vanderbilt.jpg",
            38,
            31
        ],
        [
            "Washington University in St. Louis",
            38.64861351825395,
            -90.31058162540845,
            "washu.jpg",
            38,
            31
        ]
    ];

    for(let i = 0; i<colleges.length; i++){
        const currCollege = colleges[i];
        const marker = new google.maps.Marker({
            position: { lat: currCollege[1], lng: currCollege[2] },
            map,
            title: currCollege[0],
            icon: {
                url: currCollege[3],
                scaledSize: new google.maps.Size(currCollege[4], currCollege[5])
            },
            animation: google.maps.Animation.DROP
        });
    
        const infowindow = new google.maps.InfoWindow({
            content: currCollege[0],
          });
    
        marker.addListener("click", () => {
            infowindow.open(map, marker);
        });
    }

    
}

