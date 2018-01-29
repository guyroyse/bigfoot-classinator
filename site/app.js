var classinateUrl = 'https://ejitn71uqd.execute-api.us-east-1.amazonaws.com/prod/bigfootClassinator'

var app = new Vue({
    el: '#app',
    data: {
        report: '',
        classification: ''
    },
    methods: {
        classinate: function() {
            this.$http.post(classinateUrl, { reportText: this.report })
                .then(response => {
                    console.log("There was a response", response);
                    this.classification = response.body.reportClass;
                }, error => {
                    console.log("There was an error", error);
                });
        }
    }
});
