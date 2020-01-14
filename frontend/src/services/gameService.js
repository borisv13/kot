import config from "./config";

class GameService {
  static instance = null;
  callbacks = {};

  static getInstance() {
    if (!GameService.instance) {
      GameService.instance = new GameService();
    }
    return GameService.instance;
  }

  constructor() {
    this.socketRef = null;
  }

  // Format: [['COMMAND_TOKEN', 'COMMAND_OPTION', 'COMMAND_OPTIONS']]
  // payload example: [['cmd', 'init_player'], #]
  // payload example: [['cmd', 'refresh_player'], #]
  // payload example: [['cmd', 'store_replace_card', #]] where # indicates number of cards to return from deck
  // payload example: [['cmd', 'store_buy_card', #]] where # indicates cards id to purchase
  // payload example: [['cmd', 'chat_send'], #]

  connect(roomName) {
    const path = config.GAME_SOCKET_API_PATH + roomName + "/";
    this.socketRef = new WebSocket(path);

    this.socketRef.onopen = () => {
      console.log("WebSocket open");
    };

    this.socketRef.onmessage = e => {
      let data = e.data;
      this.socketNewMessage(data);
      console.log("Socket OnMessage: " + data);
    };

    this.socketRef.onerror = e => {
      console.log("Socket OnError: " + e.message);
    };

    this.socketRef.onclose = e => {
      console.log("Socket OnClosed, Reopening...");
      this.connect(roomName);
    };
  }

  socketNewMessage(data) {
    const parsedData = JSON.parse(data);
    const command = parsedData.command;
    const action = parsedData.action;
    if (Object.keys(this.callbacks).length === 0) {
      return;
    }

    if (command === "server_response") {
      this.callbacks[command](action);
    }
  }

  addCallbacks(serverResponseCallback) {
    this.callbacks["server_response"] = serverResponseCallback;
  }

  sendMessage(data) {
    try {
      this.socketRef.send(JSON.stringify({ ...data }));
    } catch (err) {
      console.log(err.message);
    }
  }

  state() {
    return this.socketRef.readyState;
  }

  waitForSocketConnection(callback) {
    const socket = this.socketRef;
    const recursion = this.waitForSocketConnection;
    setTimeout(function() {
      if (socket.readyState === 1) {
        console.log("Connection is made");
        if (callback != null) {
          callback();
        }
        return;
      } else {
        console.log("wait for connection...");
        recursion(callback);
      }
    }, 1); // wait 5 milisecond for the connection...
  }
}

const GameInstance = GameService.getInstance();

export default GameInstance;
