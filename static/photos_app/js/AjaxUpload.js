$(document).ready(function(){

        function getCookie(name) {
            var cookieValue = null;
            if (document.cookie && document.cookie != '') {
                var cookies = document.cookie.split(';');
                for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                 // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
            return cookieValue;
        }
    var csrftoken = getCookie('csrftoken');

        function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
        }

    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
        }

        $('#form').submit(function(e){
            e.preventDefault();
            //check if everything regarding field validation is ok
            //freeze until server return response

            //fill FormData with form fields
            //refactor this
            var data = new FormData($(this));
            data.append("photo", $("#id_photo")[0].files[0]);
            data.append("description",$("#id_description").val());
            data.append("city_part",$("#id_city_part").val());

            $.ajax({
                url:'/',
                type: 'POST',
                data: data,//$(this).serializeArray(),//new FormData($('form')),//.append("photo",$("#id_photo").get()),
                cache:false,
                processData: false,
                contentType: false, //"multipart/form-data",//false,//'application/x-www-form-urlencoded;charset=utf-8',//false ili ap ne menja nista
                beforeSend: function(xhr, settings) {
                    if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                     // Send the token to same-origin, relative URLs only.
                     // Send the token only if the method warrants CSRF protection
                     // Using the CSRFToken value acquired earlier
                        xhr.setRequestHeader("X-CSRFToken", csrftoken);
                }
                },
                success: function(data){
                    var parseData = $.parseJSON(data);
                    console.log(parseData.message);
                    alert(parseData.message);
                    //clear all fields
                    //unfreeze submit button
                }
            });

        });
    });

