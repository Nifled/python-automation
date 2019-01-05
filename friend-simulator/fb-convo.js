const fs = require("fs");

const rawdata = fs.readFileSync("dania.json");
const data = JSON.parse(rawdata);

const messages = data.messages;
const separated = groupBy(messages, "sender_name");

const a = separated[Object.keys(separated)[0]];
const b = separated[Object.keys(separated)[1]];

console.log(a.slice(0, 1));
console.log(getTotalWords(a, "content"));

// {
//   "sender_name": "Erick",
//   "timestamp_ms": 1440381009905,
//   "content": "Yo digo que si",
//   "type": "Generic"
// }

// Inspiration - https://i.redd.it/23v9czqdj6i01.jpg

// utils
function groupBy(objectArray, property) {
  return objectArray.reduce((acc, obj) => {
    let key = obj[property];
    if (!acc[key]) {
      acc[key] = [];
    }
    acc[key].push(obj);
    return acc;
  }, {});
}

function getTotalWords(array, property) {
  return array.reduce((acc, msg) => {
    if (!msg.hasOwnProperty(property)) return acc;
    let words = msg[property].split(" ");
    return acc + words.length;
  }, 0);
}
