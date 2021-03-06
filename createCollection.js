const data = [
  {
    id: 'dbe9ce84-3816-4086-99c1-24dae9ae2ee8',
    surveyId: 'a0ed0c14-3f16-40fb-b345-3e2013394038',
    questionId: 'c5e83dd5-7870-4848-9f81-fb4a66aa7c8c',
    comment: 'First response to first question',
    rating: null,
  },
  {
    id: '5f9c7d8d-66f5-4e06-a908-f6fa35952b06',
    surveyId: 'a0ed0c14-3f16-40fb-b345-3e2013394038',
    questionId: 'e794bbb9-81a4-49d0-b023-644b4bddce1f',
    comment: 'Second response to first question',
    rating: null,
  },
  {
    id: 'f3f81053-ef20-4b41-ab14-0324a49ee09b',
    surveyId: 'a0ed0c14-3f16-40fb-b345-3e2013394038',
    questionId: '5166a28a-2876-4173-bed8-2e3357c02d15',
    comment: 'Third response to first question',
    rating: null,
  },
  {
    id: '44136535-46bb-4cfc-bed8-daf818f800b8',
    surveyId: 'a0ed0c14-3f16-40fb-b345-3e2013394038',
    questionId: 'e794bbb9-81a4-49d0-b023-644b4bddce1f',
    comment: 'Second response to first question',
    rating: null,
  },
];

/**
 * Takes an array of object and creates a group based on the object.questionId
 * @param {object[]} arr
 * @returns {object}
 */
const createCollection = arr => {
  const group = {};

  arr.forEach(item => {
    id = item.questionId;

    if (group.hasOwnProperty(id)) {
      group[id].push(item.comment);
    } else {
      group[id] = [];
      group[id].push(item.comment);
    }
  });

  return group;
};

console.log('TCL: createCollection(data)', createCollection(data));
