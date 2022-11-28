new Vue({
    el: '#app',
    vuetify: new Vuetify(),
    data: () => ({
      offsetTop: 0,
    }),
  
    methods: {
      onScroll (e) {
        this.offsetTop = e.target.scrollTop
      },
    },
  })