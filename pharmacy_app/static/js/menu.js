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
            modalError: ''
        },
        methods: {
            checkLogin: function(){
                login = Cookies.get('login');
                if(login !== null && login !== undefined){
                    user_type = Cookies.get('user_type')
                    $.ajax({
                        method: "POST",
                        url: "/autoryzacja/" + user_type,
                        dataType: "json",
                        contentType: "application/json; charset=utf-8",
                        data: JSON.stringify({'user_login': login, 'user_token': Cookies.get('user_token')}),
                        headers: {'X-CSRFToken': Cookies.get('csrftoken')},
                        async: true,
                        success: function(response){
                            if(response.status === 'ok'){
                                this.is_logged_in = true;
                                this.username = login;
                            }
                        }.bind(this),
                        error: function(jqXHR, status, error){
                            this.noCommentsInfo = "Wystąpił błąd podczas wysyłania wpisu!";
                        }.bind(this)
                })};
            },
            logout: function() {
                $.ajax({
                    method: "POST",
                    url: "/rest-auth/logout/",
                    dataType: "json",
                    contentType: "application/json; charset=utf-8",
                    data: JSON.stringify({}),
                    headers: {'X-CSRFToken': Cookies.get('csrftoken')},
                    async: true,
                    success: function(response){
                        this.username = '';
                        this.is_logged_in = false;
                    }.bind(this),
                    error: function(jqXHR, status, error){
                        this.noCommentsInfo = "Wystąpił błąd podczas wysyłania wpisu!";
                    }.bind(this)
                });
            },
            login: function() {
                var username = $('#login-username').val()
                var password = $('#login-password').val()
                $.ajax({
                    method: "POST",
                    url: "/rest-auth/login/",
                    dataType: "json",
                    contentType: "application/json; charset=utf-8",
                    data: JSON.stringify({'username': username, 'password': password}),
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
            register: function() {
                var username = $('#register-username').val()
                var email = $('#register-email').val()
                var password = $('#register-password').val()
                var passwordRepeat = $('#register-password-repeat').val()
                $.ajax({
                    method: "POST",
                    url: "/rest-auth/registration/",
                    dataType: "json",
                    contentType: "application/json; charset=utf-8",
                    data: JSON.stringify({
                        'username': username,
                        'password1': password,
                        'password2': passwordRepeat,
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
            changePassword: function() {
                var password = $('#chpass-password').val()
                var passwordRepeat = $('#chpass-password-repeat').val()
                $.ajax({
                    method: "POST",
                    url: "/rest-auth/password/change/",
                    dataType: "json",
                    contentType: "application/json; charset=utf-8",
                    data: JSON.stringify({
                        'new_password1': password,
                        'new_password2': passwordRepeat,
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