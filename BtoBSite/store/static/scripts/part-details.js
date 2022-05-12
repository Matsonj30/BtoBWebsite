function displayAvailability(){
    console.log("HI")
    isAvailable = document.getElementsByClassName('isAvailableImg')
    for(i = 0; i<isAvailable.length; i+=1){
        console.log(isAvailable[i]);
        if(isAvailable[i].alt == "True"){ //If available, display check mark
            console.log("HI")
            isAvailable[i].src="/static/images/redX.png"
        }//if
        else{
            isAvailable[i].src="/static/images/greenCheck.png"

        }//else
    }//for


}
displayAvailability()