function initiate(){
    isAvailable = document.getElementsByClassName('isAvailableImg');
    for(i = 0; i<isAvailable.length; i+=1){
        if(isAvailable[i].alt == "True"){ //If available, display check mark
            isAvailable[i].src="/static/images/greenCheck.png";
        }//if
        else{
            isAvailable[i].src="/static/images/redX.png";

        }//else
    }//for
    initiateFilters()

}
/* Adds an event lsitener to each filter checkbox, will then redirect to proper django
query that filters by the content checked off */
function initiateFilters(){
    filterBoxes = document.getElementsByClassName("filterContent")
    for(i=1; i<filterBoxes.length; i+=1){
        filterBoxes[i].addEventListener('click', function(){
            document.location.href = "parts/" + this.textContent.trim()
        })
    }//for
}


initiate()