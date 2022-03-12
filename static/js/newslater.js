// $(document).on('submit','#neslaterform', function(e){
//     e.preventDefault();
//     $.ajax({
//         type:'POST',
//         url: 'signup_to_newslater/',
//         data:{
//             useremail:$('#useremail').val()
//         },
//         success:function(){
//           alert("successfully added email")
//         }
//     })
// })
$(document).ready(function(){
    $('#neslaterform').submit(function(event){
      event.preventDefault()
      form = $("#neslaterform")
  
      $.ajax({
        'url':'/signup_to_newslater/',
        'type':'POST',
        data:{
                useremail:$('#useremail').val()
            },
        'dataType':'json',
        'success': function(data){
          alert(data['success'])
        },
      })// END of Ajax method
    //   $('#id_your_name').val('')
    //   $("#id_email").val('')
    }) // End of submit event
  
  })