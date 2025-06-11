import { generate } from "./table.js";

// Get seed from URL query parameter
const urlParams = new URLSearchParams(window.location.search);
const seed = urlParams.get("seed") || "";

// Generate table data
const tableData = generate(seed, 50, 10);

// Render HTML table
function renderTable(data) {
  const table = document.createElement("table");
  data.forEach((row) => {
    const tr = document.createElement("tr");
    row.forEach((cell) => {
      const td = document.createElement("td");
      td.textContent = cell;
      tr.appendChild(td);
    });
    table.appendChild(tr);
  });
  return table;
}

// Insert table into #table element
document.getElementById("table").appendChild(renderTable(tableData));
