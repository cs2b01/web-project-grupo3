var currentUserId = 0;

var currentClickedId = 0;

function usuario(){
        $.ajax({
            url:'/current',
            type:'GET',
            contentType: 'application/json',
            dataType:'json',
            success: function(response){
                //alert(JSON.stringify(response));
                $('#cu_username').html(response['username'])
                var name = response['name']+" "+response['fullname'];
                currentUserId = response['id'];
                allcompras();
                allproductos();
            },
            error: function(response){
                alert("Ingrese primero");
                location.href= "/static/login.html";

            }
        });

    }

     function allcompras(){
        $.ajax({
            url:'/compras',
            type:'GET',
            contentType: 'application/json',
            dataType:'json',
            success: function(response){
                //alert(JSON.stringify(response));
                var i = 0;
                $.each(response, function(){
                    if( (response[i]['usercomprador_id']) == currentUserId){
                    f = '<div class="alert alert-secondary" role="alert"  >';
                    f = f + response[i]['producto']['nombre'];
                    f = f + '</div>';
                    i = i+1;
                    $('#allcompras').append(f);}
                    else {
                        i=i+1;
                    }
                });
            },
            error: function(response){
                alert(JSON.stringify(response));
            }
        });
    }
        function allproductos(){
        $.ajax({
            url:'/productos',
            type:'GET',
            contentType: 'application/json',
            dataType:'json',
            success: function(response){
                //alert(JSON.stringify(response));
                var i = 0;
                $.each(response, function(){
                    if( (response[i]['cantidad']) != 0){
                    f = '<div class="alert alert-secondary" role="alert"  onclick=comprar('+currentUserId+','+response[i].id+') >';
                    f = f + response[i]['nombre'];
                    f = f + '<br/>'
                    f = f + 'Precio: '
                    f = f + response[i]['precio'];
                    f = f + '<br/>'
                    f = f + 'Cantidad: '
                    f = f + response[i]['cantidad'];
                    f = f + '</div>';
                    i = i+1;
                    $('#allproductos').append(f);
                    }
                    else {
                    i = i+1;
                    }
                });
            },
            error: function(response){
                alert(JSON.stringify(response));
            }
        });
    }

function comprar(current, producto_id){
        //alert(user_from_id);
        //alert(user_to_id);
        currentClickedId = producto_id;
        var data = JSON.stringify({
                "usercomprador_id": currentUserId,
                "producto_id": currentClickedId,
                "satisfaccion": 8
            });
        $.ajax({
            url:'/compra',
            type:'POST',
            contentType: 'application/json',
            data : data,
            dataType:'json',
           success: function(response){
                location.href= "/static/catalogo.html"
            },
            error: function(response){
                location.href= "/static/catalogo.html"
            }
        });
}

function pagar(){
       alert("Gracias por su compra. \n Nos pondremos en Contacto para la entrega.");
       location.href="/static/index.html"
}