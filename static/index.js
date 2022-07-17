let xhr = new XMLHttpRequest();
xhr.responseType = "blob";
let process = {};
let fileImport = document.getElementById("file-import");
let preview = document.querySelector("#preview");
let download = document.getElementById("download");

let contrastSets = {scale: 0};
let brightSets = {const: 0};
let scaleSets = {
    xscale: 1,
    yscale: 1
};
let rotateSets = {angle: 0};
let transSets = {
    xtrans: 0,
    ytrans: 0
};
let smoshaSets = {
    level: 0
};
let pp1Sets = {angle: 0};
let pp2Sets = {
    top: 0,
    left: 0
};


function send_data(json) {
    let formData = new FormData();
    formData.append("settings", json);
    formData.append("image", fileImport.files[0]);
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            let imagesrc = URL.createObjectURL(this.response);
            console.log(this.response);
            preview.src = imagesrc;
            download.setAttribute("href", imagesrc);
        }
    }
    xhr.open("POST", "/image", true);
    xhr.send(formData);
}

fileImport.addEventListener("change", function(e) {
    if (!fileImport.files[0]) return;
    process = {};
    let formData = new FormData();
    formData.append("image", fileImport.files[0]);
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4 && xhr.status == 200) {
            let imagesrc = URL.createObjectURL(this.response);
            preview.src = imagesrc;
            download.setAttribute("href", imagesrc);
        }
    }
    xhr.open("POST", "/image", true);
    xhr.send(formData);
    preview.style.display = "inline-block";
});

document.getElementById("CSscale").addEventListener("change", function() {
    let value = parseFloat(this.value);
    if (!process.hasOwnProperty("contrastSets")) {
        contrastSets["scale"] = value;
        process["contrastSets"] = contrastSets;
    }
    else {
        process["contrastSets"]["scale"] = value;
    }
    let json = JSON.stringify(process);
    send_data(json);
});

document.getElementById("IBconst").addEventListener("change", function() {
    let value = parseFloat(this.value);
    if (!process.hasOwnProperty("brightSets")) {
        brightSets["const"] = value;
        process["brightSets"] = brightSets;
    }
    else {
        process["brightSets"]["const"] = value;
    }
    let json = JSON.stringify(process);
    send_data(json);
});

document.getElementById("negative").addEventListener("change", function() {
    if (this.checked) {
        process["negative"] = true;
    }
    else {
        process["negative"] = false;
    }
    let json = JSON.stringify(process);
    send_data(json);
});

for (let element of document.getElementsByClassName("scale")){
    element.addEventListener("change", function() {
        scaleSets["xscale"] = parseFloat(document.getElementById("xscale").value);
        scaleSets["yscale"] = parseFloat(document.getElementById("yscale").value);
        process["scaleSets"] = scaleSets;
        let json = JSON.stringify(process);
        send_data(json);
    });
}

document.getElementById("angleRotate").addEventListener("change", function() {
    rotateSets["angle"] = parseInt(this.value);
    process["rotateSets"] = rotateSets;
    let json = JSON.stringify(process);
    send_data(json);
});

for (let element of document.getElementsByClassName("translation")){
    element.addEventListener("change", function() {
        transSets["xtrans"] = parseInt(document.getElementById("xtrans").value);
        transSets["ytrans"] = parseInt(document.getElementById("ytrans").value);
        process["transSets"] = transSets;
        let json = JSON.stringify(process);
        send_data(json);
    });
}

document.getElementById("levelSS").addEventListener("change", function() {
    smoshaSets["level"] = parseFloat(this.value);
    process["smoshaSets"] = smoshaSets;
    let json = JSON.stringify(process);
    send_data(json);
});

document.getElementById("anglePP").addEventListener("change", function() {
    pp1Sets["angle"] = parseInt(this.value);
    process["pp1Sets"] = pp1Sets;
    let json = JSON.stringify(process);
    send_data(json);
});

for (let element of document.getElementsByClassName("PP2")){
    element.addEventListener("change", function() {
        pp2Sets["top"] = parseInt(document.getElementById("topPP2").value);
        pp2Sets["left"] = parseInt(document.getElementById("leftPP2").value);
        process["pp2Sets"] = pp2Sets;
        let json = JSON.stringify(process);
        send_data(json);
    });
}