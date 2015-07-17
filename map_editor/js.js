var map = {};

var selectedCell = null;
var selectedCors = null;

var mapColors = {
    '---': '',
    forest: '#5E8C31',
    dungeon: '#253529',
    area: '#926F5B',
    hell: '#CA3435',
    market: '#F2C649',
    town: '#A9B2C3',
    hospital: '#2887C8',
    respawn: '#6CDAE7'
};

function init() {
    updateMap();
    var monTypeNode = document.getElementById('mon_type');
    var monTypesNode = document.getElementById('mon_types');
    for(var i=1; i <= 3; i++){
        var newNode = monTypeNode.cloneNode(true);
        newNode.name = 'mon_type' + i;
        newNode.id = null;
        monTypesNode.appendChild(newNode);
    }
    monTypesNode.removeChild(monTypeNode);

}

function updateMap() {
    var node_map = document.getElementById('map');
    node_map.innerHTML = '';

    for(var y = 0; y < 32; y++) {
        var node_tr = document.createElement('tr');
        for (var x = 0; x < 32; x++) {
            var node_td = document.createElement('td');
            node_td.id = 'cell-' + x + '-' + y;
            node_td.dataset.x = x;
            node_td.dataset.y = y;
            var color = mapColors[(map[x + '-' + y] || {}).tile_type];
            node_td.style.backgroundColor = color;
            node_td.onclick = click_cell;
            node_tr.appendChild(node_td);
        }
        node_map.appendChild(node_tr);
    }
    select_cell(15, 15);
}


function click_cell(){
    var x = this.dataset.x;
    var y = this.dataset.y;

    select_cell(x, y);
}

function select_cell(x, y, z) {
    if (selectedCell) {
        var key = selectedCors.x + '-' + selectedCors.y;
        document.querySelector('#cell-' + key).innerText = '';
    }

    update_cell();
    document.querySelector('#cell-' + x + "-" + y).innerText = '×';
    selectedCors = {x: x, y: y, z: z};
    selectedCell = map[x + '-' + y];
    if (selectedCell) {
        selectedCell = JSON.parse(JSON.stringify(selectedCell)); //clone
    } else {
        selectedCell = {
            tile_type: '---',
            name: '',
            mon_types: '',
            portal: '',
            stairs: false
        };
    }

    document.querySelector('#menu h2').innerText = x + '×' + y;
    document.querySelector('#cell-' + x + "-" + y).innerText = '⚫';
    var inputs = document.querySelectorAll('#fields input, #fields select');
    for (var i = 0; i < inputs.length; ++i) {
        var input = inputs[i];
        input.value = selectedCell[input.name];
    }
}

function update_cell() {
    if (!selectedCell)
        return;
    var inputs = document.querySelectorAll('#fields input, #fields select');
    for (var i = 0; i < inputs.length; ++i) {
        var input = inputs[i];
        selectedCell[input.name] = input.value;
    }
    var key = selectedCors.x + '-' + selectedCors.y;
    var cellNode = document.querySelector('#cell-' + key);
    cellNode.style.backgroundColor = mapColors[selectedCell.tile_type];
    if (selectedCell.tile_type == '---') {
        if (map[key] != undefined)
            delete map[key];
    } else {
        map[key] = selectedCell;
    }
}

function save_map(e) {
    update_cell();
    var node = e.target;
    var content = JSON.stringify(map);
    var blob = new Blob([content], {type:'application/json'});

    if (window.URL) {
        node.href = window.URL.createObjectURL(blob);
    } else if (window.webkitURL) {
        node.href = window.webkitURL.createObjectURL(blob);
    } else {
        alert('srsly, update browser');
        return false;
    }
    node.download = 'map.json';
    return true;
}

function load_map(e) {
	var fileReader = new FileReader();
	fileReader.onload = function(ee) {
        map = JSON.parse(ee.target.result);
		updateMap();
	};
    var node = e.target;
	fileReader.readAsText(node.files[0], "UTF-8");
    return true;
}