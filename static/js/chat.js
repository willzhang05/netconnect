function scrollToBottom() {
    let objDiv = document.getElementById("chat-messages");
    objDiv.scrollTop = objDiv.scrollHeight;
}

scrollToBottom();

const roomName = JSON.parse(document.getElementById('json-roomname').textContent);
const userName = JSON.parse(document.getElementById('json-username').textContent);
let wsURI = '';
if (window.location.protocol == 'https:') {
    wsURI += 'wss://' + window.location.host + '/ws/' + roomName + '/'
} else {
    wsURI += 'ws://' + window.location.host + '/ws/' + roomName + '/'
}
const chatSocket = new WebSocket(wsURI);

chatSocket.onmessage = function(e) {
    console.log('onmessage');

    const data = JSON.parse(e.data);

    if (data.message) {
        document.querySelector('#chat-messages').innerHTML += ('<b>' + data.username + '</b>: ' + data.message + '<br>');
    }

    scrollToBottom();
};

chatSocket.onclose = function(e) {
    console.log('The socket close unexpectadly');
};

document.querySelector('#chat-message-submit').onclick = function(e) {
    const messageInputDom = document.querySelector('#chat-message-input');
    const message = messageInputDom.value;

    chatSocket.send(JSON.stringify({
        'message': message,
        'username': userName,
        'room': roomName
    }));

    messageInputDom.value = '';
};
