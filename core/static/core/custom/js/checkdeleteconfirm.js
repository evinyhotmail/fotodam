
document.addEventListener('DOMContentLoaded', function () {
  const myform = document.getElementById("myCrudForm");

      document.addEventListener('click', event => {
        const element = event.target;
        if (element.className == "btn btn-outline-light btn-delete-confirm") {
            // with Submit(), is like the user clicked on submit option
            myform.submit();
        }
 
    })
});//end of addEventListener('DOMContentLoaded')

