var map = {};

var selectedCell = null;
var selectedCors = null;



function init() {
    var node_map = document.getElementById('map');

    for(var i=0; i < 32; i++) {
        var node_tr = document.createElement('tr');
        for (var j = 0; j < 32; j++) {
            var node_td = document.createElement('td');
            node_td.className = i + '-' + j;
            node_td.dataset.x = j;
            node_td.dataset.y = i;
            node_td.onclick = click_cell;
            node_tr.appendChild(node_td);
        }
        node_map.appendChild(node_tr);
    }
    select_cell(0, 0);
}


function click_cell(){
    var x = this.dataset.x;
    var y = this.dataset.y;

    select_cell(x, y);
}

function select_cell(x, y, z) {
    update_cell();
    selectedCors = {x: x, y: y, z: z};
    selectedCell = map[x + '-' + y];
    if (selectedCell) {
        selectedCell = JSON.parse(JSON.stringify(selectedCell))  //clone
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
    var inputs = document.querySelectorAll('#menu input, #menu select');
    for (var i = 0; i < inputs.length; ++i) {
        var input = inputs[i];
        input.value = selectedCell[input.name];
    }
}

function update_cell() {
    if (!selectedCell)
        return;
    var inputs = document.querySelectorAll('#menu input, #menu select');
    for (var i = 0; i < inputs.length; ++i) {
        var input = inputs[i];
        selectedCell[input.name] = input.value;
    }
    if (selectedCell.tile_type == '---')
        return;
    map[selectedCors.x + '-' + selectedCors.y] = selectedCell;
}