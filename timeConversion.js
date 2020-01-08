/**
 * Converts 12 hour time to 24 hour format.
 * @param {string} s the time in 12 hour format
 * @returns
 */
function timeConversion(s) {
  const time = s;

  if (time[8] === 'P' && time[1] !== '2')
    return Number(time.slice(0, 2)) + 12 + time.slice(2, 8);

  if (time[8] === 'P' && time.slice(0, 2) === '02')
    return Number(time.slice(0, 2)) + 12 + time.slice(2, 8);

  if (time[8] === 'A' && time[1] === '2') return '00' + time.slice(2, 8);

  return time.slice(0, 8);
}

console.log("TCL: timeConversion('07:05:45PM')", timeConversion('07:05:45PM'));
console.log("TCL: timeConversion('12:00:00AM')", timeConversion('12:00:00AM'));
console.log("TCL: timeConversion('12:00:00AM')", timeConversion('12:34:57PM'));
console.log("TCL: timeConversion('12:00:00AM')", timeConversion('12:34:57AM'));
console.log("TCL: timeConversion('12:45:54PM')", timeConversion('12:45:54PM'));
console.log("TCL: timeConversion('02:34:50PM')", timeConversion('02:34:50PM'));

function timeConversion2(s) {
  /*
   * Write your code here.
   */
  // grab a copy of the input 12-hour time
  const time = s;

  // if the time is in PM and not the twelfth hour
  if (time[8] === 'P' && time.slice(0, 2) !== '12') {
    // return the 24-hour format by adding twelve and stripping the PM
    return Number(time.slice(0, 2)) + 12 + time.slice(2, 8);
  }

  // if time is in AM and it is the twelfth hour
  if (time[8] === 'A' && time.slice(0, 2) === '12') {
    // set the hour to 00
    return '00' + time.slice(2, 8);
  }

  // otherwise, strip the AM 
  return time.slice(0, 8);
}

console.log(
  "TCL: timeConversion2('07:05:45PM')",
  timeConversion2('07:05:45PM'),
);
console.log(
  "TCL: timeConversion2('12:00:00AM')",
  timeConversion2('12:00:00AM'),
);
console.log(
  "TCL: timeConversion2('12:00:00AM')",
  timeConversion2('12:34:57PM'),
);
console.log(
  "TCL: timeConversion2('12:00:00AM')",
  timeConversion2('12:34:57AM'),
);
console.log(
  "TCL: timeConversion2('12:45:54PM')",
  timeConversion2('12:45:54PM'),
);
console.log(
  "TCL: timeConversion2('02:34:50PM')",
  timeConversion2('02:34:50PM'),
);
