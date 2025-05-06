// exercice 1

const people = ["Greg", "Mary", "Devon", "James"];

people.shift()
console.log(people)

people[people.indexOf('James')] = 'Jason'
console.log(people)

people.push('Fellucci')
console.log(people)

console.log(people.indexOf("Mary"));

let sliced_people = people.slice(1,3)
console.log(sliced_people)


console.log(people.indexOf('Foo'))
//  it print -1 because 'Foo' doesnt existe in people


const last = people[people.length - 1];
console.log("Last element of the array is :", last);


for (let i = 0; i < people.length; i++) {
    console.log(people[i]);
  }



  for (let i = 0; i < people.length; i++) {
    console.log(people[i]);
    if (people[i] === "Devon") {
      break;
    }
  }





//    exercice 2

let colors = ['orange', 'blue', 'red', 'purple', 'yellow']
let favcolor = colors[1]
let fav2color = colors[2]
let fav3color = colors[4]
let fav4color = colors[0]
let fav5color = colors[0]

console.log('my favorit color is', favcolor)





// exercice 3

// const prompt = require('prompt-sync')();

// let input = prompt('Enter a number: ');
// let number = Number(input);

// while (isNaN(number) || number < 10) {
//   console.log('This number is too small or it is not a number');
//   input = prompt('Enter another number: ');
//   number = Number(input);
// }

// console.log('Congrats! The number is great:', number);






// exercice 4

const building = {
  numberOfFloors: 4,
  numberOfAptByFloor: {
      firstFloor: 3,
      secondFloor: 4,
      thirdFloor: 9,
      fourthFloor: 2,
  },
  nameOfTenants: ["Sarah", "Dan", "David"],
  numberOfRoomsAndRent:  {
      Sarah: [3, 990],
      Dan:  [4, 1000],
      David: [1, 500],
  },
}

console.log(building.numberOfFloors)

console.log(building.numberOfAptByFloor.firstFloor,building.numberOfAptByFloor.thirdFloor)

const secondTenant = building.nameOfTenants[1];
const rooms = building.numberOfRoomsAndRent[secondTenant][0];
console.log('the seconde tenant is:', secondTenant);
console.log('he has', rooms, 'in his apartment');



const first = building.nameOfTenants[0];
const firstPrice = building.numberOfRoomsAndRent[first][1];

const second = building.nameOfTenants[1];
const secondPrice = building.numberOfRoomsAndRent[second][1];

const third = building.nameOfTenants[2];
const thirdPrice = building.numberOfRoomsAndRent[third][1];

if (firstPrice + thirdPrice < secondPrice) {
  building.numberOfRoomsAndRent[second][1] = 1200;
  console.log('the rent of', second, 'changed to 1200$');
} else {console.log('no need to change', second, 'rent');
}







// exercice 5

let family = {dad: 'Lionel',
  mom: 'Veronique',
son1: 'Uriel',
son2: 'Michael',
daughter: 'Elsa'
};

for (let i in family) {
  console.log(i);
}
for (let i in family) { 
  console.log(family[i]);
}






// exercice 6

const details = {
  my: 'name',
  is: 'Rudolf',
  the: 'reindeer'
}

console.log('my name is', details.is, 'the', details.the)






// exercice 7

const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
let secretName = []

for (let i = 0; i < names.length; i++){
  secretName.push(names[i][0]);
}
secretName.sort();
const companyName =secretName.join('');
console.log('the name of the company is', companyName)











// exercice stars

for (let i = 1; i <= 6; i++) {
  console.log("* ".repeat(i));
}


for (let i = 1; i <= 6; i++) {
  let line = "";
  for (let j = 1; j <= i; j++) {
    line += "* ";
  }
  console.log(line);
}
