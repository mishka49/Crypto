console.log("hellow world")

const socket = new WebSocket('ws://' + window.location.host + '/ws/dashboard_slug/')

console.log(socket)

socket.onopen = function (e) {
    console.log('Server:' + e.data);
};

socket.onopen = function (e) {
    socket.send(JSON.stringify({
        'message': 'Hellow from client',
        'sender': 'test sender'
    }));
};

