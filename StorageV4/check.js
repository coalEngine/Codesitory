
function verify(){

    if(document.form.name.value == "Thiery" && document.form.lastName.value == "Jean Baptiste" && document.form.address.value == "Pine Bush" && document.form.city.value == "Middletown" && document.form.state.value == "New York" && document.form.Code.value == "12566" && document.form.email.value == "pb.thiery.jean.baptiste@pinebushschools.org") 
    {
        alert("Information is Correct!");
        location = "https://www.pinebushschools.org";
    }
    if(document.form.name.value == 0 || document.form.lastName.value == 0 || document.form.address.value == 0 || document.form.city.value == 0 || document.form.state.value == 0 || document.form.Code.value == 0 || document.form.email.value == 0) 
    {
        alert("Please complete each field")

    }
    else if(document.form.name.value != "Thiery" && document.form.lastName.value != "Jean Baptiste" && document.form.address.value != "Pine Bush" && document.form.city.value != "Middletown" && document.form.state.value != "New York" && document.form.Code.value != "12566" && document.form.email.value != "pb.thiery.jean.baptiste@pinebushschools.org")
    {
        alert("Information is Incorrect!"); 
    }
}