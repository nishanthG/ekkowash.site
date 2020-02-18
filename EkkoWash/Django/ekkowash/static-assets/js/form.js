'use strict';

(function ($) {

        $("#contact-form").on('submit',function(event) {
            event.preventDefault(); // to prevent default page reloading

         var obj = {
            "name" : $('#name').val(),
            "email" : $('#email').val(),
            "addon": $('#addon option:selected').text(),
            "addr": $('#addr').val(),
            "atime": $('#atime').val(),
            "ccode": $('#ccode').val(),
            "ctype": $('#ctype option:selected').text(),
            "date": $('#date').val(),
            "desc": $('#desc').val(),
            "landmark": $('#landmark').val(),
            "pnum": $('#phone').val(),
            "time": $('#time').val(),
            "city":$('#city').val(),
            "state":$('#state').val(),
            "pincode":$('#pincode').val()
        }
        
        console.log(JSON.stringify(obj))

        $.ajax({
            type:"POST",
            url: "http://127.0.0.1:5000/ekko/api/bookings",
            crossDomain: true,
            data : JSON.stringify(obj),
            success: function(data){
                $('#output').html('<p>successfully sent data.</p>');
                $('#contact-form')[0].reset(); // to reset form data
            }
        }).done(function(data){
            setTimeout(function () {
                alert("Form submitted successfully! We'll get back to you soon. Thank you.");
            }, 2000);
            //alert("Form submitted successfully! We'll get back to you soon. Thank you."); // This will be called after the ajax executed
        });

});

})(jQuery);