$(document).ready(function(){
    new Vue({
        el: '#vue-menu-app',
        data: {
            is_logged_in: false,
            username: '',
            is_checking_authentication: true,
            showModalBg: false,
            showLoginModal: false,
            showRegisterModal: false,
            showPasswordChangeModal: false,
            modalError: '',
            user_token: ''
        },
        methods: {
            checkLogin: function(){
                console.log('check login');
                this.username = '';
                this.is_logged_in = false;
                this.is_checking_authentication = false;
                login = Cookies.get('login');
                console.log('login: ' + Cookies.get('login'));
                if(login !== null && login !== undefined){
                    var choice = Cookies.get('user_type')
                    console.log('sending request')
                    $.ajax({
                        method: "POST",
                        url: "/autoryzacja/" +choice,
                        dataType: "json",
                        contentType: "application/json; charset=utf-8",
                        data: JSON.stringify({
                            'user_login': login,
                            'user_token': this.user_token
                            }),
                        headers: {'X-CSRFToken': Cookies.get('csrftoken')},
                        async: true,
                        success: function(response){
                            if(response.status === 'ok'){
                                this.is_logged_in = true;
                                this.username = login;
                                this.is_checking_authentication = false;
                                console.log(this.username);
                            }
                        }.bind(this),
                        error: function(jqXHR, status, error){}.bind(this)
                })};
            },
            logout: function() {
                $.ajax({
                    method: "POST",
                    url: "/wylogowanie/" + choice,
                    dataType: "json",
                    contentType: "application/json; charset=utf-8",
                    data: JSON.stringify({'token': user, 'haslo': pass}),
                    headers: {'X-CSRFToken': Cookies.get('csrftoken')},
                    async: true,
                    success: function(response){
                        this.username = '';
                        this.is_logged_in = false;
                        console.log(this.username + " has logged out");
                    }.bind(this),
                    error: function(jqXHR, status, error){
                        this.noCommentsInfo = "Wystąpił błąd podczas wysyłania wpisu!";
                    }.bind(this)
                });
            },
            login: function() {
                var user = $('#login-username').val()
                var pass = $('#login-password').val()
                var Box = document.getElementById("login-acces");
                var choice;
                if (Box.checked == true){choice ="pracownik";} 
                else {choice= "klient";}
                $.ajax({
                    method: "POST",
                    url: "/logowanie/"+ choice,
                    dataType: "json",
                    contentType: "application/json; charset=utf-8",
                    data: JSON.stringify({'login': user, 'haslo': pass}),
                    headers: {'X-CSRFToken': Cookies.get('csrftoken')},
                    async: true,
                    success: function(response){
                        if(response.status === 'ok'){
                            console.log(this.username + " has logged in");
                            this.is_logged_in = true;
                            this.username = user;
                            Cookies.set('user_token', response.user_token);
                            Cookies.set('login', user);
                            Cookies.set('user_type', choice);
                            this.closeModals();
                            this.checkLogin();
                        }
                    }.bind(this),
                    error: function(jqXHR, status, error){
                        this.set_modal_error(jqXHR);
                    }.bind(this)
                });
                console.log(this.data);
            },
            register: function() {
                var choice = Cookies.get('user_type');
                var username = $('#register-username').val()
                var email = $('#register-email').val()
                var password = $('#register-password').val()
                var passwordRepeat = $('#register-password-repeat').val()
                $.ajax({
                    method: "POST",
                    url: "/rejestracja" + choice,
                    dataType: "json",
                    contentType: "application/json; charset=utf-8",
                    data: JSON.stringify({
                        'login': username,
                        'haslo': password,
                        'haslo2': passwordRepeat,
                        'email': email
                    }),
                    headers: {'X-CSRFToken': Cookies.get('csrftoken')},
                    async: true,
                    success: function(response){
                        this.closeModals();
                        this.checkLogin();
                    }.bind(this),
                    error: function(jqXHR, status, error){
                        this.set_modal_error(jqXHR);
                    }.bind(this)
                });
            },
           
            set_modal_error(jqXHR) {
                this.modalError = '';
                for (var key in jqXHR.responseJSON) {
                    if (Object.prototype.hasOwnProperty.call(jqXHR.responseJSON, key)) {
                        var val = jqXHR.responseJSON[key];
                        console.log(val);
                        console.log(key);
                        this.modalError = ((key !== 'non_field_errors' ? key + ': ' : ''))
                                            + val[0];
                    }
                }
            },
            startLoginModal: function() {
                this.showModalBg = true;
                this.showLoginModal = true;
            },
            startRegisterModal: function() {
                this.showModalBg = true;
                this.showRegisterModal = true;
            },
            startPasswordChangeModal: function() {
                this.showModalBg = true;
                this.showPasswordChangeModal = true;
            },
            closeModals: function() {
                this.showModalBg = false;
                this.showLoginModal = false;
                this.showRegisterModal = false;
                this.showPasswordChangeModal = false;
                this.modalError = '';
            }
        },
        computed: {
        },
        mounted: function(){
            var $that = this;
            setTimeout(function(){
                $that.checkLogin();
            }, 2000);
        }
    });
});
