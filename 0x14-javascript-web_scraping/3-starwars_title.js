#!/usr/bin/node
const { get } = require('axios').default;
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

get(url)
  .then(({ data: { title } }) => console.log(title))
  .catch((err) => console.error(err));
