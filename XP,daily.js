// EXERCICE 1

// function displayNumbersDivisible() {
//     let somme = 0;
//     for (let i = 0; i <= 500; i++) {
//         if (i % 23 === 0){
//             console.log(i);
//             somme += i;
//         }
//     }
//     console.log('the sum is :', somme);
    
// }


// displayNumbersDivisible();


// function displayNumbersDivisible(divisor) {
//     let somme = 0;
//     for (let i = 0; i <= 500; i++) {
//         if (i % divisor === 0){
//             console.log(i);
//             somme += i;
//         }
//     }
//     console.log('the sum is :', somme);
    
// }

// displayNumbersDivisible(3)
// displayNumbersDivisible(45)





//EXERCICE 2

// const stock = { 
//     "banana": 6, 
//     "apple": 0,
//     "pear": 12,
//     "orange": 32,
//     "blueberry":1
// }  

// const prices = {    
//     "banana": 4, 
//     "apple": 2, 
//     "pear": 1,
//     "orange": 1.5,
//     "blueberry":10
// } 

// const shoppingList = ['banana', 'orange','apple'];

// function myBill() {
//     let total = 0;
//     for (let item of shoppingList) {
//         if (item in stock && stock[item] > 0) {
//             total += prices[item];
//             stock[item]--;
//         } else if (item in stock && stock[item] === 0) {
//             console.log(`Sorry, we don't have ${item} in stock`);
//         }
//     }
//     console.log("Total:", total);
// }

// myBill();
// console.log(stock);






// EXERCICE 3


// function changeEnough(itemPrice, amountOfChange){
//     let quarters = amountOfChange[0] * 0.25;
//     let dimes = amountOfChange[1] * 0.1;
//     let nickel = amountOfChange[2] * 0.05;
//     let penny = amountOfChange[3] * 0.01;

//     let somme = quarters + dimes + nickel + penny

//     if(itemPrice <= somme){
//         return true;
//     } else {
//         return false;
        
//     }
// }

// console.log(changeEnough(4.25, [25, 20, 5, 0]));
// console.log(changeEnough(14.11, [2,100,0,0]));







// //EXERCICE 4


// function hotelCost(nights){
//     let priceNight = 140;
//     // let nights;
    
//     // while( isNaN(nights) || nights === '' || nights === null){
//     //     nights = prompt('how many nights do you want to stay? ');
//     //     nights = Number(nights);
//      return nights * priceNight;
// }

// // console.log('your hotel price is:', hotelCost());

// function planeRideCost(destination){
//     // let destination;

//     // while(!destination || !isNaN(destination)){
//     //     destination = prompt('where do you want to go? ');

//       if(destination.toLowerCase() === 'london'){
//         return 183;
//     } else if (destination.toLowerCase() === 'paris'){
//         return 220;
//     } else {
//         return 300;
//     }
    
// }
// // console.log('your flight price is $'+ planeRideCost());


// function rentalCarCost(days){
//     let priceDay = 40;
//     // let days;
    

//     // while(isNaN(days) || days === '' || days === null){
//     //     days = prompt('how many days do you want to rent the car? ');
//     //     days = Number(days);
//     // }   
//         let total = days * priceDay;
//         if(days > 10){
//             total = total * 0.95;
//         }
        
//         return total;
        
// }

// // console.log('your rental car price is:', rentalCarCost());


// function totalVacationCost(){
//     let destination;
//     let nights;
//     let days;

//     while(!destination || !isNaN(destination)){
//         destination = prompt('where do you want to go? ');}
//     while( isNaN(nights) || nights === '' || nights === null){
//         nights = prompt('how many nights do you want to stay? ');
//         nights = Number(nights);}
//         while(isNaN(days) || days === '' || days === null){
//         days = prompt('how many days do you want to rent the car? ');
//         days = Number(days);
//         }   


//  let hotel = hotelCost(nights);
//  let flight = planeRideCost(destination);
//  let car = rentalCarCost(days);  
//  let totalCost = hotel + flight + car;

//  console.log(`hotel cost: $${hotel}, flight cost: $${flight}, car cost: $${car}`);
//  console.log(`Your total vacation cost is: $${totalCost}`);

//  return totalCost;

// }

// totalVacationCost();



// lines 162-174 it is the bonus






//EXERCICE 5


// const div = document.getElementsByTagName('div')
// console.log(div);

// const richard = document.querySelectorAll('li');
// richard[1].textContent = 'Richard';

// let ul = document.querySelectorAll('ul');
// let secondUl = ul[1];
// let li = secondUl.getElementsByTagName('li');
// secondUl.removeChild(li[1]);

// let miko = document.querySelectorAll('ul');
// for (let ul of miko){
//     ul.children[0].textContent = 'Michael'
// }


// let aa = document.querySelectorAll('ul');
// let i = 0;
// for( bb of aa){
//     bb.classList.add('student_list');
//     if ( i === 0){
//         bb.classList.add('university', 'attendance');
//     } i++;
// }


// const couleur = document.getElementById('container');
// couleur.style.backgroundColor = 'lightblue'
// couleur.style.padding = '10px'


// const hideDan = document.querySelectorAll('li');
// for( let dd of hideDan){
//     if(dd.textContent === 'Dan')
//     dd.style.display = 'none';
// }

// const bord = document.querySelectorAll('li');
// for(let bor of bord){
//    if(bor.textContent === 'Richard')
//     bor.style.border = '2px solid red';
// }


// const body = document.querySelector('body');
// body.style.fontSize = '20px'




