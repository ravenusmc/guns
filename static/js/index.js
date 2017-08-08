//This is the ajax request to get the number of murders by year.
$(document).ready(function(){
  $('#by_year_form').bind('submit', function(event){
    event.preventDefault();
    $.ajax({
      data: {
        a: $('#a').val()
      },
      type: 'POST',
      url: '/by_year',
      success: function(data){
        $('#result').text(data.result).show();
      }
    });
  });
});


//This code will get the user input for the number of gun deaths by year and validate it. 
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

//This is the ajax request to get the number of gun deaths by type.
$(document).ready(function(){
  $('#by_type_form').bind('submit', function(event){
    event.preventDefault();
    $.ajax({
      data: {
        b: $('#b').val()
      },
      type: 'POST',
      url: '/by_type',
      success: function(data){
        $('#result_death_type').text(data.result).show();
      }
    });
  });
});

//This is validation code for the gun deaths by type code.
document.querySelector('#type_data').addEventListener('click', function(){

  let target = document.querySelector('#b').value;

  console.log(target);
  //debugger;
  if (target != 'Homicide' || target != 'homicide') {
    alert('That is not the correct input!');
    alert('Please enter in either: Accidental, Homicide, Suicide, Undetermined');
    location.reload();
  } else {
    alert('equal')
  }
  // if ( target != 'Homicide' || target != 'homicide' || target != 'Accidental' || target != 'accidental'
  //   || target != 'Suicide' || target != 'suicide' || target != 'Undetermined' 
  //   || target != 'undetermined'){
  //   alert('That is not the correct input!');
  //   alert('Please enter in either: Accidental, Homicide, Suicide, Undetermined');
  //   location.reload();
  // } else {
  //   alert('yay');
  // }

})








































