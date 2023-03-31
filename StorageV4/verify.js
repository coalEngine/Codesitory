function verify(){

    if(document.form.username.value == "Thiery" && document.form.password.value == "games") 
    {
        alert("Username and Passowrd are correct!");
        location = "http://www.SimpleGamesOnline.com";
    }
    else
    {
        alert("Username and Password are Incorrect!"); 
    }
}