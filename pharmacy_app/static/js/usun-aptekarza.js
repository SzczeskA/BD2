$(document).ready(function(){
    new Vue({
        el: '#vue-usuwanie_aptekarzy-app',
        data: {
        },
        methods: {
            trim: function(x){
                return x.replace(/^\s+|\s+$/gm,'');
            },
            isText: function(text) {
                if(text === null || text === undefined)
                    return false;
                b = (this.trim(text.value)).length;
                return b;
            },
            ua_usun_apt: function(){
                if(!this.isText(da_login)){
                    alert("Wymagany jest login!");
                }

                console.log('sending request')
                    $.ajax({
                        method: "POST",
                        url: "/pracownicy/usun",
                        dataType: "json",
                        contentType: "application/json; charset=utf-8",
                        data: JSON.stringify({
                            'login': Cookies.get('login'),
                            'token': Cookies.get('token'),
                            'remove_user': ua_login,
                            }),
                        headers: {'X-CSRFToken': Cookies.get('csrftoken')},
                        async: true,
                        success: function(response){
                            alert(response.alert);
                            if(response.status === 'ok'){
                                da_login.value = "";
                            }
                        }.bind(this),
                        error: function(jqXHR, status, error){}.bind(this)
                })

            },
            isText: function(text) {
                if(text === null || text === undefined)
                    return false;
                //return text.trim().length;
                return true;
            }
        },
        computed: {
        },
        mounted: function(){
            console.log('usun-aptekarza.js');
            //this.pobierz_leki();
        }
    });
});
