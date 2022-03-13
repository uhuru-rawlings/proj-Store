const showModels = (clicked_id) =>{
    document.getElementsByClassName(clicked_id)[0].style.display = "block";
}

const hideratings = () =>{
    document.getElementById("retinmgsform").style.display = "none";
}
const showratings = (clicked_ids) =>{
    document.getElementById("retinmgsform").style.display = "block";
    document.getElementById("retedpost").value = clicked_ids;
}