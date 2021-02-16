document.addEventListener('DOMContentLoaded', function(){
    document.querySelector('.convert-form').addEventListener('submit', event => convert_ticket());
    


});
function convert_ticket(){
    //event.preventDefault();
    const id = document.querySelector('#ticket-number').value;
    console.log(id);
    var s = document.getElementById('selected-solver');
    var strUser = s.options[s.selectedIndex].value;
    console.log(strUser);
    var status = document.getElementById('select-status');
    var strStatus = status.options[status.selectedIndex].text;
    console.log(strStatus);
    //Get the current url.
    const url = window.location.href;
    console.log(url);
    const data = {'id': id, 'it_user': strUser, 'status': strStatus}
    //make ajax request with server
    fetch(`${url}/convert_ticket`, {
        method: 'PUT',
        headers: {
            'Content-TYPE': 'application/json',
        },
        body: JSON.stringify(data), 
    })
    .then(res => res.json())
    .then(result => {
        console.log(result);
    })
    alert(`ticket converted to ${strUser} successfully`);
    
}
/*document.addEventListener('DOMContentLoaded', function(){
    
    document.querySelectorAll('.row-ticket').forEach(function(tr){
        if(tr.children[4].textContent==='unaccomplished'){
            tr.style.color='#f05337';
        
        }else{
            tr.style.color='#0ec414';
        } 
    })
    const url = window.location.href;
    console.log(url);
    document.querySelector('#submit').addEventListener('click', () => load_ticket());

function load_ticket(){
    const ticket_number = document.querySelector('#ticket-number').value;
    console.log(ticket_number);
    };
});

    /*const url = window.location.href;
    console.log(url);
    const form = document.querySelector('convert-form');
    document.querySelectorAll('.row-ticket').forEach(function(tr){
        if(tr.children[4].textContent==='unaccomplished'){
            tr.style.color='#f05337';
        
        }else{
            tr.style.color='#0ec414';
        } 
    })

    form.onsubmit = function(){
        const ticket_number = document.querySelector('#ticket-number').value;
        var select_user = document.querySelector('#selected-solver').selectedIndex;
        const it_user = document.querySelector('#it-user')[select_user].value;
        var select_status = document.querySelector('#select-status').selectedIndex;
        const accomplishment = document.querySelector('.accomplishment')[select_status].value;
        //create json data  and make it ready to be converted.
        const data = {'id': ticket_number, 'it_user': it_user, 'accomplishment': accomplishment}
        //const url = window.location.href;
        //send json data
        fetch(`${url}/convert_ticket`,{
            method: 'PUT',
            headers: {
                'Content-TYPE': 'application/json',
            },
            body: JSON.stringify(data),
        })
        .then(res => res.json())
        .then(result => {
            console.log(result);
        })

    
    }; */