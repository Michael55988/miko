const solarSystem = [
    { name: "Mercury", moons: 0, color: "#a9a9a9" },
    { name: "Venus", moons: 0, color: "#ffcc00" },
    { name: "Earth", moons: 1, color: "#0077be" },
    { name: "Mars", moons: 2, color: "#b22222" },
    { name: "Jupiter", moons: 79, color: "#f5deb3" },
    { name: "Saturn", moons: 82, color: "#d2b48c" },
    { name: "Uranus", moons: 27, color: "#66cdaa" },
    { name: "Neptune", moons: 14, color: "#4169e1" },
  ];

  const section = document.querySelector('.listPlanets');

for(let i = 0; i < solarSystem.length; i++){
    // creat div element
    const planetDiv = document.createElement('div')
    planetDiv.classList.add('planet');
    planetDiv.style.backgroundColor = solarSystem[i].color;
    planetDiv.textContent = solarSystem[i].name;

    section.appendChild(planetDiv)

    // add the moon

    let left = 0
    for(let j = 0; j<solarSystem[i].moons; j++){
        const moonsDiv = document.createElement('div')
        moonsDiv.classList.add('moon');
        moonsDiv.style.left = left + 'px'
        moonsDiv.style.backgroundColor = getRandomColor()
        left += 15
        planetDiv.appendChild(moonsDiv)
    }
}


function getRandomColor(){
    let letters = '0123456789ABCDEF'
    let color = '#';
    for(let i = 0; i < 6; i++){
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;

}