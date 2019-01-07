const fs = require("fs");

const rawdata = fs.readFileSync("manny.json");
const data = JSON.parse(rawdata);

const messages = data.messages;
const separated = groupBy(messages, "sender_name");

const a = separated[Object.keys(separated)[0]]; // person 1
const b = separated[Object.keys(separated)[1]]; // person 2

// console.log(a.slice(0, 5));
const days = groupByDay(messages, "timestamp_ms");

console.log(Object.keys(days).length);

// {
//   "sender_name": "Erick",
//   "timestamp_ms": 1440381009905,
//   "content": "Yo digo que si",
//   "type": "Generic"
// }

// Inspiration - https://i.redd.it/23v9czqdj6i01.jpg

// utils
function groupBy(array, property) {
  return array.reduce((acc, obj) => {
    let key = obj[property];
    if (!acc[key]) {
      acc[key] = [];
    }
    acc[key].push(obj);
    return acc;
  }, {});
}

function groupByDay(array, property) {
  return array.reduce((acc, msg) => {
    let date = new Date(msg[property]);
    date.setHours(0, 0, 0, 0); // Without hr, min, ms
    let msDate = date.getTime();
    if (!acc[msDate]) {
      acc[msDate] = [];
    }
    acc[msDate].push(msg);
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
