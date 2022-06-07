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

/*This definitely could have been done with a href ?= in the html file like we did with the page numbers below */

function initiateFilters(){
    filterBoxes = document.getElementsByClassName("filterContent")
    
    for(i=0; i<filterBoxes.length; i+=1){
        filterBoxes[i].addEventListener('click', function(){
            window.location = ("http://localhost:8000/home/parts/" + this.textContent.trim())
        })
    }//for

    pageNumbers()
}

function pageNumbers(){
    url = window.location.href
    pageNumber = url.slice(-1);
    pageNumber = parseInt(pageNumber) - 1 
    console.log(pageNumber)

    numbers = document.getElementsByClassName("numbers")
    if(pageNumber > 0){ /*!= NaN does not work for some reason */
        console.log(numbers)
        numbers[pageNumber].style.backgroundColor ="rgb(235, 18, 18)"
    }//if
    else{
        numbers[0].style.backgroundColor ="rgb(235, 18, 18)" /*Ensures that the #1 page number is highlighted even though a page number hasnt been formally selected */
    }
    
}

initiate()