$(document).ready(function(){
    new Vue({
        el: '#vue-usuwanie-lekow-app',
        data: {
            leki: [],
            amount: 0,
            Nazwa: "",
            has_nazwa: false
        },
        methods: {
            wyszukaj_leki: function(){
                console.log(search_name);
                if(search_name !== null && search_name !== undefined){
                    this.has_nazwa = true;
                    //this.usun_leki();
                }
                else {
                this.has_nazwa = false;
                }
            },
            usun_leki: function(){
             console.log("sending delete request for "+ search_name);
            if(this.has_nazwa==true)
            {
                console.log("sending delete request for "+ search_name);
                $.ajax({
                    method: "POST",
                    url: "/leki/usun",
                    dataType: "json",
                    contentType: "application/json; charset=utf-8",
                    data: JSON.stringify({
                    'user_login': Cookies.get('login'),
                    'user_token': Cookies.get('user_token'),
                    'lek': search_name.value
                    }),
                    headers: {'X-CSRFToken': Cookies.get('csrftoken')},
                    async: true,
                    success: function(response){
                        if(response.status === 'ok'){

                        }
                    }.bind(this),

                });
                console.log(search_name.value);
            }

            },
            change_amount: function(){
                if(amount !== null && amount !== undefined){
                    this.amount = amount.value;
                }
                else {
                    this.amount = 0;
                }
                this.pobierz_leki();
            }
        },
        computed: {
        },
        mounted: function(){
            this.usun_leki();
        }
    });
});