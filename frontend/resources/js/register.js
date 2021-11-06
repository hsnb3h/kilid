
// $(document).ready(function() {
//     //form submit
//     $("register-form").submit(function(event){
//         var _email      = $('#email').val();
//         var _password   = $('#password').val();
//         $.post("http://localhost:3000/api/login",{
//             email:_email, password: _password
//         }).done(function(data){
//             $.cookie('token',data.token)
//         })
//     })
// });
 

$(document).ready(function () {
   $('#register').click(function(e) {


        var fullnameField = document.forms['register-form']['full_name'].value;
        var emailField = document.forms['register-form']['email'].value;
        var phoneField = document.forms['register-form']['phone_number'].value;
        var companyField = document.forms['register-form']['company_name'].value;
        var jobField = document.forms['register-form']['job_title'].value;
        var passField = document.forms['register-form']['password'].value;
        var fillTheForm = document.getElementById("fillform");
        
        

        var form = $(this.form);
        e.preventDefault();
        

        $.ajax({
            type: form.attr('method'),
            url: form.attr('action'),
            data: form.serialize(),
            success: function(data) {
                $(location).prop('href', 'http://127.0.0.1:5500/success.html')
                console.log(data)
            },
            error: function(data) {
                
                if ( fullnameField == null || fullnameField == '' || emailField == null || emailField == '' || phoneField == null || phoneField == "" || companyField == null || companyField == "" || jobField == null || jobField == "" || passField == null || passField == "") {
                    fillTheForm.innerHTML='لطفا فرم زیر را با دقت پر کنید'
                    
                } else {
                   console
                }
            }
        })
   })
});