const classinateUrl = 'https://rccptdhzsa.execute-api.us-east-1.amazonaws.com/prod/bigfootClassinator';

const classMessages = {
    'class a': "You saw bigfoot! That's a Class A sighting.",
    'class b': "You found some evidence of bigfoot like a footprint! That's a Class B sighting.",
    'class c': "Someone told you about seeing bigfoot! That's a Class C sighting"
};

const waitMessage = "Analyzing your sighting...";
const errorMessage = "There was an error processing your classination.";

var app = new Vue({
    el: '#app',
    data: {
        report: '',
        classination: ''
    },
    methods: {
        classinate: function() {
            this.classination = waitMessage;
            axios.post(classinateUrl, { reportText: this.report })
                .then(response => {
                    var reportClass = response.data.reportClass;
                    this.classination = classMessages[reportClass];
                })
                .catch(error => {
                    console.log(error);
                    this.classination = errorMessage;
                });
        }
    }
});
