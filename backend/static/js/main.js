for (p in stations) {
    var toAppend = '<option>' + p + '</option>';
    var station = stations[p];
    $("#stationStart").append(toAppend);
    $("#stationEnd").append(toAppend);
}

var lineName = [];
for (line in lines) {
    lineName.push(Object.keys(lines[line]))
}
var cLine = 3;
var cStation = 0;
var cLineLen = lines[cLine][lineName[cLine]].length;
console.log("Now Start parse Line: " + lineName[cLine]);
console.log("Next station: " + lines[cLine][lineName[cLine]][cStation]);

function showStation(evt) {
    var e = evt.target;
    var dim = e.getBoundingClientRect();
    var x = evt.clientX;
    var y = evt.clientY;
    var cLineName = lineName[cLine][0];
    var cStationName = lines[cLine][cLineName][cStation];
    var obj = {
        "station": cStationName,
        "line": cLineName,
        "x": x,
        "y": y
    }
    console.log(obj);
    cStation += 1;
    console.log(cStation);
    // $.post("http://cs139.dcs.warwick.ac.uk/~apc/cs139/hackathon/save.php",
    //     obj,
    //     function(data) {
    //         console.log(data);
    //     });
    if (cStation < cLineLen) {
        console.log("Next station: " + lines[cLine][lineName[cLine]][cStation]);
    } else {
        cLine += 1;
        cStation = 0;
        cLineLen = lines[cLine][lineName[cLine]].length;
        if (cLine>7) {
            alert("Finished");
        } else {
            console.log("Now Start parse Line: " + lineName[cLine]);
            console.log("Next station: " + lines[cLine][lineName[cLine]][cStation]);
        }
    }
}
