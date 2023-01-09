// function myFunction(){
//   var x = document.getElementById("id_73");
//   var y = document.getElementById("id_80");
//   var a = document.getElementById("id_70")
//   if (x.style.display == "none" && y.style.display == "none"){
//     x.style.display = "block";
//     y.style.display = "none";
//   }
//   else if(y.style.display = "none" && x.style.display == "block"){
//     y.style.display = "block";
//     a.style.display = "block";
//     x.style.display = "none";
//   }
//   else{
//     x.style.display = "block";
//     y.style.display = "none";
//     a.style.display = "none";
//   }
// }

// function myFunction1(){
//     var x = document.getElementById("id_74");
//     if (x.style.display === "none") {
//     x.style.display = "block";
//     }
//     else {
//     x.style.display = "none";
//     }
// }


function myFunction(x){
  if (x==0){
    document.getElementById("id_73").style.display = "block";
    document.getElementById("id_80").style.display = "none";
    document.getElementById("id_70").style.display = "none";
    if (document.getElementById("id_74")){
      document.getElementById("id_74").style.display = "none";
    }
  }
  else if (x==1){
    document.getElementById("id_80").style.display = "block";
    document.getElementById("id_70").style.display = "block";
    document.getElementById("id_73").style.display = "none";
    document.getElementById("input_70_0").checked = false;
  }
}

function myFunction1(x){
  if (x==0){
    document.getElementById("id_74").style.display = "block";
  }
  else if (x==1){
    document.getElementById("id_74").style.display = "none";
  }
}