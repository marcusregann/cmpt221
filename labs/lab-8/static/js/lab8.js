/****************************************************************************************************************/
/* In-Class Exercises                                                                                           */
/****************************************************************************************************************/
/* 1. create an array called "fruits" and assign the values "Strawberry", "Raspberry", and "Apple" to it         */
let fruits=[];
fruits=["Strawberry", "Raspberry", "Apple"];
console.log(fruits)
/* 2. add two more fruits to the "fruits" array using the correct array method                                   */
fruits.push("Pear", "Kiwi")
console.log(fruits)
/* 3. sort the fruits array alphabetically using the correct array method                                        */
console.log(fruits.sort());

/* 4. create a function called printFruit that prints each item in the fruits array to the console              */
/*    and call the printFruit function                                                                          */
function printFruits(){
    for (let index in fruits){
        console.log(fruits[index]);
    }
}
printFruits()
/* 5. create a fruit class that has three properties: name, color, and season and one method: printFruit()      */
/*    that prints all three properties of the fruit to the console. Then, create 3 fruit objects and print      */
/*    them using the printFruit() method*/
class fruit {
    constructor(name, color, season){
        this.name=name,
        this.color=color,
        this.season=season;
    }   
    printfruit(){
        /*Another way to do it:
        ------>console.log("Fruit Name: "+ this.name + "Fruit Color: " + this.color + "Season: " + this.season)
        */
        return "Fruit Name: " + this.name +", Fruit Color: " + this.color +", Season: "+ this.season;
    }    
}
const apple=new fruit("Apple", "Red", "Fall");
console.log(apple.printfruit());
const pear=new fruit("Pear", "Green", "Fall");
console.log(pear.printfruit());
const Kiwi=new fruit("Kiwi", "Green", "Spring");
console.log(Kiwi.printfruit());




/****************************************************************************************************************/
/* In-Class Lab                                                                                                 */
/****************************************************************************************************************/
/* 1. Write a function that asks the user if they want to say hi. If the user selects "Okay" (true), then       */
/*    display a welcome message. If the user selects "Cancel" (false), then display a different message         */
function areYouSure() {
    let text="Do you want to say hi?"
    if(confirm(text) === true ){
        text="Welcome to Lab 8!";
    } else{
        text = "Rude!";
    }
    document.getElementById("welcome").innerHTML = text;
}

/* 2. Write a function to change 3 styles on the webpage                                                        */
function changeStyle() {
    document.getElementById("welcome").style.fontFamily = "Impact,Charcoal,sans-serif";
    document.getElementById("button1").innerHTML = "Awesome Sauce!"
    document.getElementById("button2").style.color = "green"
}
