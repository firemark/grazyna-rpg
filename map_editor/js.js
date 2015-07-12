var map = {};

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
    document.querySelector('#menu h2').innerText = x + '×' + y;
}

function update_cell(x, y, z) {
    //todo
}