$(document).ready(function(){
    new Vue({
        el: '#vue-users-app',
        data: {
            users: [],
            user: null,
            amount: 0,
            name: "",
            has_search_name: false,
            has_result: false
        },
        methods: {
            search_user: function(){
                console.log(search_name);
                if(search_name !== null && search_name !== undefined && search_name.value !== ''){
                    this.has_search_name = true;
                    this.pull_users();
                }
                else {
                this.has_search_name = false;
                }
            },
            pull_users: function(){
            console.log('pull fc');
            $.ajax({
                method: "GET",
                url: (
                    "/uzytkownicy-app?amount=" +
                    this.amount +
                    (this.has_search_name?"&name="+search_name.value:"")
                ),
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
            change_amount: function(){
                if(amount !== null && amount !== undefined){
                    this.amount = amount.value;
                }
                else {
                    this.amount = 0;
                }
                this.pull_users();
            }
        },
        computed: {
        },
        mounted: function(){
            console.log('uzytkownicy.js');
        }
    });
});