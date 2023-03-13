let age = 0
let msg = ""

console.log("Button clicked")
document.getElementById("confirm_btn").onclick=function(){
    
}
age = document.getElementById("age").innerHTML.valueOf
if(age <= 18){
    msg = "You are not allowed"
    document.getElementById("get_in").innerHTML.msg
}else{
    msg = "Welcome to the club"
    document.getElementById("get_in").innerHTML.msg
}




function validateAge(){
    var age = document.getElementById("age-input").value;
        if(age > 18) {
        msg = "You are legible";
        console.log("yes")
        } else {
        msg = "Chill kidogo";
        console.log("no")
    }
    document.getElementById("age").innerHTML = msg;

   } 
  
   