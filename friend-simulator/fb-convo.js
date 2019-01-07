const fs = require("fs");

const rawdata = fs.readFileSync("manny.json");
const data = JSON.parse(rawdata);

const messages = data.messages;
const separated = groupBy(messages, "sender_name");

const a = separated[Object.keys(separated)[0]];
const b = separated[Object.keys(separated)[1]];

// console.log(a.slice(0, 5));
console.log(groupByDay(a.slice(0, 50), "timestamp_ms"));

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
    date.setHours(0, 0, 0); // Without hr, min, ms
    // let msDate = date.getTime();
    let str = date.getFullYear() + "/" + date.getMonth() + "/" + date.getDate();
    // console.log(str);
    if (!acc[str]) {
      acc[str] = [];
    }
    acc[str].push(msg);
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
