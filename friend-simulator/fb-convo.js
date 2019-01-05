const fs = require("fs");

const rawdata = fs.readFileSync("dania.json");
const data = JSON.parse(rawdata);

const messages = data.messages;

const a = messages.filter(x => x.sender_name === "Erick Delfin");
const b = messages.filter(x => x.sender_name === "Dania Alejandra Navarro");

console.log(a.length, "erick");
console.log(b.length, "dania");

// {
//   "sender_name": "Erick",
//   "timestamp_ms": 1440381009905,
//   "content": "Yo digo que si",
//   "type": "Generic"
// }

// Inspiration - https://i.redd.it/23v9czqdj6i01.jpg

