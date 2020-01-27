$(document).ready(function(){
    new Vue({
        el: '#vue-usuwanie_aptek-app',
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
            ua_usun_apteke: function(){
                if(!this.isText(ua_adres)){
                    alert("Wymagany jest adres!");
                }
                else if(!this.isText(ua_nazwa)){
                    alert("Wymagana jest nazwa!");
                }

                //console.log('sending request')
                    $.ajax({
                        method: "POST",
                        url: "/apteki/usun",
                        dataType: "json",
                        contentType: "application/json; charset=utf-8",
                        data: JSON.stringify({
                            'login': Cookies.get('login'),
                            'token': Cookies.get('token'),
                            'ua_nazwa':  ua_nazwa.value,
                            'ua_adres':  ua_adres.value
                            }),
                        headers: {'X-CSRFToken': Cookies.get('csrftoken')},
                        async: true,
                        success: function(response){
                            alert(response.alert);
                            if(response.status === 'ok'){
                                ua_nazwa.value = "";
                                ua_adres.value = "";
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
            console.log('usun_apt.js');
            //this.pobierz_leki();
        }
    });
});
