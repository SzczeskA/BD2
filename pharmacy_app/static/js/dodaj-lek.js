$(document).ready(function(){
    new Vue({
        el: '#vue-przegladanie-lekow-app',
        data: {""
        },
        methods: {
            dl_dodaj_lek: function(){
                if(!this.isText(dl_nazwa)){
                    alert("Wymagana jest nazwa!");
                }
                else if(!this.isText(dl_substancja)){
                    alert("Wymagana jest nazwa substancji!");
                }
                else if(!this.isText(dl_dawka)){
                    alert("Wymagane jest podanie dawki!");
                }
                else if(!this.isText(dl_ilosc)){
                    alert("Wymagana jest ilość!");
                }
                else if(!this.isText(dl_kraj)){
                    alert("Wymagane jest podanie kraju produkcji!");
                }
                console.log('sending request')
                    $.ajax({
                        method: "POST",
                        url: "/app/dodaj-lek",
                        dataType: "json",
                        contentType: "application/json; charset=utf-8",
                        data: JSON.stringify({
                            'user_login': login,
                            'user_token': this.user_token,
                            'nazwa': dl_nazwa,
                            'substancja': dl_substancja,
                            'dawka': dl_dawka,
                            'ilosc':dl_ilosc,
                            'kraj':dl_kraj
                            }),
                        headers: {'X-CSRFToken': Cookies.get('csrftoken')},
                        async: true,
                        success: function(response){
                            if(response.status === 'ok'){
                                alert("Pomyślnie dodano lek");
                                dl_nazwa.value = "";
                                dl_substancja.value = "";
                                dl_dawka.value = "";
                                dl_ilosc.value = "";
                                dl_kraj.value = "";
                            }
                        }.bind(this),
                        error: function(jqXHR, status, error){}.bind(this)
                }

            },
            isText: function(text) {
                if(text === null || text === undefined)
                    return false;
                return text.trim().length;
            }
        },
        computed: {
        },
        mounted: function(){
            this.pobierz_leki();
        }
    });
});
