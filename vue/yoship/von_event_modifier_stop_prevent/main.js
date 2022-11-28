new Vue({
    el: '#app',
    data:{
        number: 0,
        x:0,
        y:0,
        a:0,
        b:0,
    },
    methods:{
        countUp: function() { this.number+=1 } ,
        changeMousePosition: function(event,divideNumver){
            this.x = event.clientX/divideNumver;
            this.y = event.clientY/divideNumver;
        },
        changeMousePosition2: function(event){
            this.a = event.clientX;
            this.b = event.clientY;
        },
        noEvent: function(event){
            console.log(event);
            event.stopPropagation();
        },
        noEvent2: function(event){
            console.log(event);
        },
    }
})
