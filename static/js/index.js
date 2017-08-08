document.querySelector('#year_data').addEventListener('click', function(){

     let target = Number(document.querySelector('#a').value);
     
     if (target < 2012){
        alert('Please enter in a valid year!');
        location.reload();
     }else if (target > 2014){
        alert('Please enter in a valid year!');
        location.reload();
     }
});