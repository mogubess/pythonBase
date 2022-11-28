new Vue({
    el: '#app',
    data:{
        message: 'HelloWorld',
        number: 3,
        ok: false
    },
    methods:{
        reverseMessage: function (){
            console.info("test")
            // console.info(this.message.split('').reverse().join())
            this.message = this.message.split('').reverse().join('')
            console.info(this.message)
        },
        sayHi: function (){
            return 'Hi'
        },
        sayHi2: function (){
            // this.message ='Hello VueJs'
            return 'Hi2';
        }

    }
})
