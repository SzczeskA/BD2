$(document).ready(function(){
    new Vue({
        el: '#vue-dodawanie_aptekarzy-app',
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
            da_dodaj_apt: function(){
                if(!this.isText(da_login)){
                    alert("Wymagany jest login!");
                }
                else if(!this.isText(da_haslo)){
                    alert("Wymagane jest haslo!");
                }
                else if(!this.isText(da_poziom_d)){
                    alert("Wymagany jest poziom dostępu!");
                }

                console.log('sending request')
                    $.ajax({
                        method: "POST",
                        url: "/pracownicy/dodaj",
                        dataType: "json",
                        contentType: "application/json; charset=utf-8",
                        data: JSON.stringify({
                            'login': Cookies.get('login'),
                            'token': Cookies.get('token'),
                            'new_pass': da_haslo,
                            'new_login': da_login,
                            'new_level_h': da_poziom_d
                            }),
                        headers: {'X-CSRFToken': Cookies.get('csrftoken')},
                        async: true,
                        success: function(response){
                            alert(response.alert);
                            if(response.status === 'ok'){
                                da_login.value = "";
                                da_haslo.value = "";
                                da_dodaj_apt.value = "";
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
            console.log('dodaj-lek.js');
            //this.pobierz_leki();
        }
    });
});
