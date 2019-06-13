/**
 * *Takes an array and returns the markdown format for it
 * *Should format multiline values
 * @param {*} arr
 * @returns {string}
 */
function markdownTables(arr) {
  let markdown = "";

  markdown += `|${arr[0].replace(/,/, "|")}|\n|`;

  for (const i of arr[0]) {
    if (i === ",") {
      markdown += "|";
      continue;
    }
    markdown += "-";
  }

  markdown += "|\n";

  for (let i = 1; i < arr.length; i++)
    markdown += `|${arr[i].replace(/,/, "|")}|\n`;

  return markdown.trim();
}

console.log(
  markdownTables([
    "name,email",
    "emily,emily@email.com",
    "mary,maryberry@gbbs.co.uk"
  ])
);
