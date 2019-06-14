function registrar(){
        var username = $('#username').val();
        var password = $('#password').val();
        var name = $('#Name').val();
        var fullname = $('#Fullname').val();
        var usuario = JSON.stringify({
                "username": username,
                "password": password,
                "name": name,
                "fullname":fullname
            });





        $.ajax({
            url:'/users',
            type:'POST',
            contentType: 'application/json',
            data : usuario,
            dataType:'json',
            success: function(response){


            },
            error: function(response){
                //alert(JSON.stringify(response));
            }
        });

        document.getElementById("username").value="";
        document.getElementById("password").value="";
        document.getElementById("Name").value="";
        document.getElementById("Fullname").value="";
}