document.addEventListener('DOMContentLoaded', function(){
    const url = window.location.href;
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

    
    };
});