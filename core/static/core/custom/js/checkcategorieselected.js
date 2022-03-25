document.addEventListener('DOMContentLoaded', function () {
    // Get the Bbtn used to save the form
    const btn = document.getElementById('submit_save');

    // get all input type checkbox:
    const checkboxes = document.querySelectorAll('input[type="checkbox"]');

    // I used it when the DOM is load in order to enable the btn
    // in this way when I modifing the form this is alreaduy to save
    //the form

   
   validcheck(checkboxes,btn);


    document.addEventListener('click', event => {
        const element = event.target;
        if (element.className == "category-check") {
               validcheck(checkboxes,btn);
        }
        

    })
});//end of addEventListener('DOMContentLoaded')

function validcheck(mycheckboxes,btn){
    for(var i=0,l=mycheckboxes.length;i<l;i++)
    {
        if(mycheckboxes[i].checked)
        {
            btn.disabled = false;
            break;
        }else{
             btn.disabled = true;
        }
    }
    return  

}