/**
 *  Your algorithm will iterate through the array parameter (arr). It will search each object in the array for a "manufacturer" property. 
 *  *It will compare the manufacturer property on the object to the string parameter (mfrStr). 
 *  *If it finds a match, it will push the results of invoking the callback function into a placeholder array.
 *  !Before you return the results you've put in your placeholder array, you'll want to check for one "edge case". 
 *  !If there were no matches and the placeholder array is empty, return a string stating that there were no matches 
 *  !(see the example below for the sentence to return).
 */

// Don't modify this array of objects
let arcadeGames = [
  {
    'id': 1,
    'title': 'Arkanoid',
    'year': 1986,
    'manufacturer': 'Taito',
    'genre': 'breakout',
    'max_players': 2,
    'url': 'https://en.wikipedia.org/wiki/Arkanoid',
  },
  {
    'id': 2,
    'title': 'Asteroids',
    'year': 1979,
    'manufacturer': 'Atari',
    'genre': 'multi-directional shooter',
    'max_players': 2,
    'url': 'https://en.wikipedia.org/wiki/Asteroids_(video_game)',
  },
  {
    'id': 3,
    'title': 'Defender',
    'year': 1981,
    'manufacturer': 'Williams',
    'genre': 'scrolling shooter',
    'max_players': 2,
    'url': 'https://en.wikipedia.org/wiki/Defender_(video_game)',
  },
  {
    'id': 4,
    'title': 'Rush\'n\'Attack',
    'year': 1985,
    'manufacturer': 'Konami',
    'genre': 'run and gun',
    'max_players': 2,
    'url': 'https://en.wikipedia.org/wiki/Rush%27n_Attack',
  },
  {
    'id': 5,
    'title': 'Sinistar',
    'year': 1982,
    'manufacturer': 'Williams',
    'genre': 'scrolling shooter',
    'max_players': 2,
    'url': 'https://en.wikipedia.org/wiki/Sinistar',
  },
  {
    'id': 6,
    'title': 'Skate or Die!',
    'year': 1988,
    'manufacturer': 'Electronic Arts',
    'genre': 'skateboarding',
    'max_players': 1,
    'url': 'https://en.wikipedia.org/wiki/Skate_or_Die!',
  },
];


  /**
   * @param {[]} arr
   * @param {number} index
   * @returns {string}
   */
  function titleMfrYearString (arr, index) {
    return `${arr[index].title} was made by ${arr[index].manufacturer} in ${arr[index].year}`;
  }
  
  /**
   ** whoMadeWhatWhen function
   ** takes in an array ref, a manufacturers string and a call back function pointer
   ** returns an array of format strings if the manufacturer exists in the array
   ** returns a single error format string if the manufacturer is not in the array
  **/
 
  function whoMadeWhatWhen(arr, mfrStr, cb) {
    // create empty array to store the results in
    let retval = [];

    // loop over the array items checking if the manufacturer is equal to the supplied manufacturer string
    for(let i = 0; i < arr.length; i++) {
        if(arr[i].manufacturer === mfrStr) {
            retval.push(cb(arr, i))
        }
    }
    // base case of manufacturer not found then return an error message
    if(retval.length === 0) {
        return `We don't have anything by ${mfrStr} in our inventory`
    }
    // if we have got any data in the array return the results of the callback
    return retval;
  }

  console.log(whoMadeWhatWhen(arcadeGames, 'Williams', titleMfrYearString));
  // --> [ 'Defender was made by Williams in 1981', 'Sinistar was made by Williams in 1982' ]