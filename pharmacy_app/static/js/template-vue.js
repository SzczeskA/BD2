$(document).ready(function(){
    new Vue({
        el: '#comments-container',
        data: {
        },
        methods: {
            getComments: function(){
                $.ajax({
                    method: "GET",
                    url: "/getComments?eventID=" + this.eventID,
                    async: true,
                    success: function(response){
                        if(response !== null && response.result === "ok"){
                            if(response.comments !== undefined){
                                this.comments = this.prepareComments(response.comments);
                            }
                        }
                    }.bind(this),
                    error: function(jqXHR, status, error){
                        this.noCommentsInfo = "Wystąpił błąd podczas pobierania wpisów!";
                    }.bind(this)
                });
                this.isGettingComments = false;
            },
            sendComment: function() {
                var text = $('.comment-text').val();
                if (text.length != 0) {
                    $.ajax({
                        method: "POST",
                        url: "/postComment",
                        dataType: "json",
                        contentType: "application/json; charset=utf-8",
                        data: this.getCommentData(text),
                        async: true,
                        //success: function(response){}.bind(this),
                        error: function(jqXHR, status, error){
                            this.noCommentsInfo = "Wystąpił błąd podczas wysyłania wpisu!";
                        }.bind(this)
                    });
                }
                this.getComments();
                this.inputToShow = undefined;
            },
        },
        computed: {
        },
        mounted: function(){
            var $that = this;
            setTimeout(function(){
                $that.getComments();
            }, 2000);
        }
    });
});