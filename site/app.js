var classinateUrl = 'https://ejitn71uqd.execute-api.us-east-1.amazonaws.com/prod/bigfootClassinator'

var classMap = {
    'class a': "You saw bigfoot! That's a Class A sighting.",
    'class b': "You found some evidence of bigfoot like a footprint or something! That's a Class B sighting.",
    'class c': "Someone told you about seeing bigfoot! That's a Class C sighting"
}

var app = new Vue({
    el: '#app',
    data: {
        report: '',
    },
    methods: {
        classinate: function() {
            this.$http.post(classinateUrl, { reportText: this.report })
                .then(response => {
                    var reportClass = response.body.reportClass;
                    window.alert(classMap[reportClass]);
                }, error => {
                    console.log("There was an error", error);
                });
        }
    }
});
