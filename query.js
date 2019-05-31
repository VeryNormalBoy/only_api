var data_container = document.getElementById('data_table')
var open_detail = document.getElementById('add_button')
var filter_page = document.getElementById('filter')

function load_doc(){    // starting the load_doc function here

var myRequest = new XMLHttpRequest();           // creation of new XMLHttpRequest object with the name myRequest
myRequest.onreadystatechange = function(){      // creation of call back function

    if (this.readyState == 4 && this.status == 200){        // Checking the readyState

        var data = JSON.parse(this.responseText)            // Getting the response text and parse it to Json object
        renderHTML(data)                                    // rendering the HTML and pass data to it
//document.getElementById("data_table").innerHTML = this.responseText;

}
};
myRequest.open("GET","/display",true )
myRequest.send();
}

function renderHTML(dt){

    var data_string = "";           // creating the empty string and assign it to variable data_string

        for(i in dt.details){                         // Looping through the object
        data_string = data_string + '<tr><td><center> '+ dt.details[i].first_name +'</center></td><td><center>'+ dt.details[i].last_name +'</center></td><td><center>'
        + dt.details[i].age +'</center></td><td><center>'+ dt.details[i].phone +'</center></td></tr>'; // passing object properties to table rows

        }
        data_container.innerHTML = '<table border="1" width="500"><tr> <td><center>FirstName</center></td>'
                +'<td><center>Second name</center></td><td><center>Age</center></td><td><center>Phone</center></td></tr>'
                +data_string+'</table>';
}


      open_detail.onclick = function() {
        location.href = 'http://localhost:8080/add';

};

       filter_page.onclick = function(){

            location.href = 'http://localhost:8080/result';

       }
