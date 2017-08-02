var wordsList = [];

function init() {
  // Load the words from the dictionary text file to wordsList
  var wordsFile = "https://raw.githubusercontent.com/GirlsFirst/SIP-2017/master/Unit2_Applications/dictionary-attack/dictionary.txt?token=ADcVhZjRMd86ZdhPE2jVvIaJdQdzLA6Yks5YvvVSwA%3D%3D";
  $.get(wordsFile, function(data) {
    document.getElementById("btnSubmit").disabled = true;
    wordsList = data.split('\n');
    document.getElementById("btnSubmit").disabled = false;
  });
}

window.onload = init;

/* ADD YOUR CODE BELOW */

function checkPassword() {
  var pw = document.getElementById("pw").value;
  pw= getVariations(pw)
  var found = false;
  for(x = 0; x < wordsList.length; x++) {
  if (pw == wordsList[x]) {
    found = true;
  }
  }
  if(found==true) {
    document.getElementById("results").innerHTML="weak password"

  }else{
    document.getElementById("results").innerHTML="strong password"
}
}

function getVariations(pw){
  pw = pw.replace(/1/g,"i");
  pw = pw.replace(/2/g,"z");
  pw = pw.replace(/3/g,"e");
  pw = pw.replace(/4/g,"a");
  pw = pw.replace(/5/g,"s");
  pw = pw.replace(/6/g,"g");
  pw = pw.replace(/7/g,"t");
  pw = pw.replace(/8/g,"b");
  pw = pw.replace(/0/g,"o");
  return pw;

}
