#!/usr/bin/node
const { get } = require('axios').default;
const id = process.argv[2];
const baseUrl = `https://swapi-api.hbtn.io/api/films/${id}`;

get(baseUrl)
  .then(({ data: { characters } }) => {
    const requests = characters.map(character => get(character));
    Promise.all(requests)
      .then((data) => data.forEach(({ data: { name } }) => console.log(name)));
  })
  .catch((err) => console.error(err));
