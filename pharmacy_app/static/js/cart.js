$(document).ready(function(){
    new Vue({
        el: '#vue-shop-app',
        data: {
            products: undefined,
            categories: undefined,
            got_products: false,
            got_categories: false,
            products_to_show: undefined,
            prods_in_cart: 0,
            products_cost: 0,
            total_price: 0,
            delivery_cost: 0,
            order_result: null,
            delivery: null,
            cart_empty: true
        },
        methods: {
            getProducts: function(){
                $.ajax({
                    method: "GET",
                    url: "/api/products/",
                    async: true,
                    success: function(response){
                        this.products = response;
                        this.prepare_products();
                        this.got_products = true;
                    }.bind(this)
                });
            },
            getCategories: function(){
                $.ajax({
                    method: "GET",
                    url: "/api/categories/",
                    async: true,
                    success: function(response){
                        this.categories = response;
                        this.got_categories = true;
                    }.bind(this)
                });
            },
            post_order: function(data) {
                $.ajax({
                    method: "POST",
                    url: "/api/order/",
                    dataType: "json",
                    contentType: "application/json; charset=utf-8",
                    data: JSON.stringify({data}),
                    headers: {'X-CSRFToken': Cookies.get('csrftoken')},
                    async: false,
                    success: function(response){
                        this.order_result = response
                    }.bind(this),
                    error: function(jqXHR, status, error){
                        this.order_result = response;
                    }.bind(this)
                });
            },
            prepare_products: function(){
                this.products_to_show = [];
                this.products_cost = 0;
                var cart = this.get_cart_from_cookie();
                for(var i = 0; i < this.products.length; i++) {
                    var product = this.products[i];
                    var index = cart.indexOf(product.img_name);
                    if(index != -1) {
                        product.amount = cart[index+1];
                        this.products_to_show.push(product);
                        this.products_cost += product.price * product.amount;
                    }
                }
                this.set_total_price();
                this.cart_empty = (this.products_to_show.length == 0) ? true : false;
            },
            add_to_cart: function(product_name){
                this.add_product_to_cookie(product_name, 1);
                this.set_amount_of_prods_in_cart();
            },
            add_product_to_cookie(product_name, amount) {
                var cart = this.get_cart_from_cookie();
                var prod_index = cart.indexOf(product_name);
                if(cart.length < 2) {
                    cart = [product_name, amount];
                }
                else if(prod_index == -1) {
                    cart.push(product_name);
                    cart.push(amount);
                } else {
                    cart[prod_index + 1] = amount;
                }

                this.save_cart_to_cookie(cart);
            },
            get_cart_from_cookie: function() {
                var cookie = document.cookie;
                if(!cookie.includes('cart')){
                    cookie += '; cart=(); path=/; expires=Fri, 31 Dec 9999 23:59:59 GMT';
                }
                var index_of_cart = cookie.indexOf('cart=') + 6;
                var cart = '';
                var last_index = null;
                for(var i = index_of_cart; i < cookie.length; i++){
                    if(cookie[i] === ')') {
                        last_index = i;
                        break;
                    }
                    cart += cookie[i];
                }
                cart = cart.split(',');
                return cart;
            },
            save_cart_to_cookie: function(cart) {
                cart = cart.join(',');
                var cookie = 'cart=(' + cart + '); path=/; expires=Fri, 31 Dec 9999 23:59:59 GMT';
                document.cookie = cookie;
            },
            set_amount_of_prods_in_cart: function() {
                this.prods_in_cart = Math.floor(this.get_cart_from_cookie().length/2);
            },
            remove_item: function(product_name) {
                var cart = this.get_cart_from_cookie();
                var prod_index = cart.indexOf(product_name);
                if(prod_index != -1) {
                    cart.splice(prod_index, 2);
                }
                this.save_cart_to_cookie(cart);
                this.prepare_products();
            },
            change_amount: function(product_name) {
                var amount = document.getElementById(product_name).value;
                this.add_product_to_cookie(product_name, amount);
                this.prepare_products();
            },
            set_total_price: function() {
                this.delivery = document.getElementById('delivery-method').value;

                if(this.delivery.includes('Fedex')) {
                    this.delivery_cost = 12;
                } else if(this.delivery.includes('DHL')) {
                    this.delivery_cost = 10;
                } else if(this.delivery.includes('DPD')) {
                    this.delivery_cost = 9;
                }
                this.total_price = this.products_cost + this.delivery_cost;
            },
            order: function() {
                var name = document.getElementById('name');
                var surname = document.getElementById('surname');
                var city = document.getElementById('city');
                var address = document.getElementById('address');
                if(name.validity.valueMissing ||
                    surname.validity.valueMissing ||
                    city.validity.valueMissing ||
                    address.validity.valueMissing) {

                    alert('fill personal information fields');
                } else {
                    var cart = this.get_cart_from_cookie();
                    var data = {
                        name: name.value,
                        surname: surname.value,
                        city: city.value,
                        address: address.value,
                        products: cart,
                        delivery: this.delivery,
                        cost: this.total_price
                    }
                    this.post_order(data);
                    for(var i = 0; i < cart.length; i += 2) {
                        this.remove_item(cart[i]);
                    }
                    document.location = '/order_confirmation/' + this.order_result;
                }
            }
        },
        computed: {
        },
        mounted: function(){
            var $that = this;
            setTimeout(function(){
                $that.getProducts();
                $that.getCategories();
                $that.set_amount_of_prods_in_cart();
            }, 2000);
        }
    });
});