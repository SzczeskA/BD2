$(document).ready(function(){
    new Vue({
        el: '#vue-users-app',
        data: {
            users: [],
            user: null,
            amount: 10,
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
                    method: "POST",
                    url: "/uzytkownicy-app",
                    dataType: "json",
                    contentType: "application/json; charset=utf-8",
                    data: JSON.stringify({
                        'phrase': this.search_name,
                        'amount': this.amount,
                        'login': Cookies.get('login'),
                        'token': Cookies.get('token')
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
            delete_user(event){
                delete_login = event.currentTarget.id;
                console.log(event.currentTarget.id);
                $.ajax({
                        method: "POST",
                        url: "/uzytkownicy-app/usun",
                        dataType: "json",
                        contentType: "application/json; charset=utf-8",
                        data: JSON.stringify({
                            'login': Cookies.get('login'),
                            'token': Cookies.get('token'),
                            'delete_login': delete_login
                            }),
                        headers: {'X-CSRFToken': Cookies.get('csrftoken')},
                        async: true,
                        success: function(response)
                        {
                            alert('Usunięto użytkownika!');
                            this.pull_users();
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
            console.log('aptekarze.js');
        }
    });
});