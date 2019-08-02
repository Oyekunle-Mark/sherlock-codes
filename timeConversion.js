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
