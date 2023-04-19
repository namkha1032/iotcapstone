function getDateAgo(date, days) {
  let dateCopy = new Date(date);

  dateCopy.setDate(date.getDate() - days);
  return dateCopy;
}
let day0 = new Date();
let day1 = getDateAgo(day0, 1);
let day2 = getDateAgo(day0, 2);
let day3 = getDateAgo(day0, 3);
let day4 = getDateAgo(day0, 4);
let day5 = getDateAgo(day0, 5);
let day6 = getDateAgo(day0, 6);
let day7 = getDateAgo(day0, 7);
let day8 = getDateAgo(day0, 8);
let day9 = getDateAgo(day0, 9);
// tbl = document.getElementById("tbl")
// tbl.removeChild(tbl.firstElementChild);
let day = new Date();
day = day.toDateString();
var x = `<tr>
                <td>${day}</td>
                <td>30 <sup>o</sup>C</td>
                <td>namkha</td>
                <td>80%</td>
                <td>
                  <span class="badge bg-success">Good</span>
                </td>
              </tr>`;
for (let i = 0; i < 20; i++) {
  var div = document.createElement("template");
  div.innerHTML = x;
  let y = div.content.firstElementChild;
  document.getElementById("tbl").appendChild(y);
}

// import "./assets/extensions/simple-datatables/umd/simple-datatables.js";
// import "./assets/static/js/pages/simple-datatables.js";
