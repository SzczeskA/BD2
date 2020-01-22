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
                method: "GET",
                url: (
                    "/dupa?ilosc=" +
                    this.amount +
                    (this.has_nazwa?"&nazwa="+search_name.value:"")
                ),
                async: true,
                success: function(response){
                    this.leki = response.data;
                }.bind(this)
                })
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
            this.pobierz_leki();
        }
    });
});