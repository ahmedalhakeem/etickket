document.addEventListener('DOMContentLoaded', function(){
    //document.querySelector('.ticket-details').style.display = 'none';
    //console.log(sender);
    document.querySelector('.compose-ticket').onsubmit = function(){
        const title = document.querySelector('.title').value;
        const description = document.querySelector('.ticket-details').value;
        const sender = document.querySelector('.user-id').id;
        

        fetch(`/tickets`,{
            method: 'POST',
            body: JSON.stringify({
                title: title,
                description: description,
                sender: sender
            })
        })
        .then(response => response.json())
        .then(result => {
            if(result.success === true){
                console.log(result)
            }
            
        })
        .catch(err => console.log(err))
    };
});
        /*fetch(`/tickets?title=${title}&description=${description}&sender=${sender}`)
        .then(response => response.json())
        .then(result => {
            console.log(result)
        })*/
 