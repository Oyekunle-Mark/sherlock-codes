/**
 * *returns true if the string argument is palindrome
 * @param {String} word
 * @returns {Boolean}
 */
function isPalindrome(word) {
  if (
    word
      .split('')
      .reverse()
      .join('') === word
  )
    return true;

  return false;
}
