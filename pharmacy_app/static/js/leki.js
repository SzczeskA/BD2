$(document).ready(function(){
    new Vue({
        el: '#vue-przegladanie-lekow-app',
        data: {
            leki: [],
            amount: 0,
            nazwa: "",
            has_nazwa: false
        },
        methods: {
            wyszukaj_leki: function(){
                console.log(search_name);
                if(search_name !== null && search_name !== undefined){
                    this.has_nazwa = true;
                    this.pobierz_leki();
                }
                else {
                this.has_nazwa = false;
                }
            },
            pobierz_leki: function(){
                $.ajax({
                    method: "POST",
                    url: "/leki-app",
                    dataType: "json",
                    contentType: "application/json; charset=utf-8",
                    data: JSON.stringify({
                        'phrase': this.search_name,
                        'amount': this.amount
                        }),
                    headers: {'X-CSRFToken': Cookies.get('csrftoken')},
                    async: true,
                    success: function(response){
                this.users = response.data;
                if(this.users !== null && this.users != undefined && this.users.length > 0)
                    this.has_result = true;
                else {
                    this.has_result = false;}
                console.log(users);
            }.bind(this)
            })
            },
            change_amount(){
                if(amount !== null && amount !== undefined){
                    this.amount = amount.value;
                }
                else {
                    this.amount = 0;
                }
                this.pull_users();
            },
            mounted: function(){
            console.log('leki.js');
            this.pobierz_leki();
        }                  }
            });
});
