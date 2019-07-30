function getMinimumDifference(a, b) {
  const resultArray = [];

  for (let i = 0; i < a.length; i++) {
    resultArray.push(determineAnagram(a[i], b[i]))
  }

  return resultArray;
}

const determineAnagram = (str1, str2) => {
  if (str1.length !== str2.length) return -1;
  if (str1 === str2) return 0;

  let count = 0;

  str1 = str1.split('').sort()
  str2 = str2.split('').sort()

  for (let i = 0; i < str1.length; i++) {
    if (str1[i] !== str2[i]) count++;
  }

  return count;
};

console.log(getMinimumDifference('his', 'sih'));
