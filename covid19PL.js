const fetch = require('node-fetch');

fetch("https://api.nowywirus.pl/", { method: "GET" })
    .then(res => res.json())
    .then((json) => {
        console.log(`Ilość aktywnych koronawirusów wynosi ${json[0].cases}, przybyło nowych ${json[0].new_cases} koronawirusów w Polsce.`);
        console.log(`Nie żyje już ${json[0].deaths} osób, dzisiaj zmarło ${json[0].new_deaths}.`)
    });
