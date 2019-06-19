/**
 * *Solves the rock, paper and scissors repetition game
 * @param {*} n
 * @returns
 */
function rockPaperScissors(n) {
  const keyWords = ['rock', 'paper', 'scissors'];
  const result = [];
  const turns = n;

  const generateCombinations = (turnsLeft, game) => {
    if (turnsLeft === 0) {
      result.push(game);
      return;
    }

    for (let i = 0; i < keyWords.length; i++) {
      const current = keyWords[i];
      generateCombinations(turnsLeft - 1, game.concat(current));
    }
  };

  generateCombinations(turns, []);
  return result;
}

console.log(rockPaperScissors(1));
console.log(rockPaperScissors(2));
console.log(rockPaperScissors(3));
