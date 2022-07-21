console.log("Hello world");
//camelCase please
let testVariable;
let age = 30;
let name = "Gines";
let id = null;
const sunColor = "Yellow";

let person = {
    name: "Comboni",
    age: 52
}

person.name;
person['name'];

let userSelection = "name";

person[userSelection];

let cities = ["khartoum", "yuba", "asmara"];
cities[3] = "madrid";
console.log[cities[0]];
console.log(cities.length);

function destroyCity (cities) {
    return cities.pop();
}

let citiesDestroyed = destroyCity(cities);
console.log(citiesDestroyed);

function createFullName (name, lastName) {
        return name + " " + lastName;
}
console.log(createFullName("Gines", "Sanchez"));

let identification = {
    firstName: "fName",
    lastName: "lName",
}
identification.firstName = "Gines";
identification.lastName ="Sanchez";

let yearOperations = {
    year: 2,
    getSecondsInYear() {
        return (this.year * 365 * 24 * 60);
    }
}

console.log(yearOperations.getSecondsInYear());

if (yearOperations.getSecondsInYear()> 100000) {
    console.log ("Too many time");
} else {
    console.log("We can do it");
}

yearOperations.getSecondsInYear() > 100000 ? console.log ("Too many time"): console.log("We can do it");
cities = ["khartoum", "yuba", "asmara"];
for (let i = 0; i < cities.length; i ++){
    console.log(cities[i]);
}
for (let city of cities) {
    console.log(city);
}



function changeText (id) {
    id.innerHTML = "Daniel Comboni is the best";
}
console.log("Here");
document.getElementById("morePhotos").addEventListener("click", getNextPhoto);
let currentPhoto = 1;
const path ="img_comboni"
const extension= ".jpg"
function getNextPhoto() {
    if (currentPhoto <3) {
        currentPhoto +=1;
    } else {
        currentPhoto = 1;
    }
    let source = path+String(currentPhoto)+extension;
    document.getElementById("comboniPhoto").src=source;
    console.log(source);
}