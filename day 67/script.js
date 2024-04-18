let dateTime = new Date();

let day = dateTime.getDay();
let year = dateTime.getFullYear();
let month = dateTime.getMonth();
let date = dateTime.getDate();
let hours = dateTime.getHours();

console.log(year)
console.log(month)
console.log(day)
console.log(date)
console.log(date + " / " + month + " / " + year)