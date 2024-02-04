var ctx = document.getElementById('total-users').getContext('2d');
var data = {{ data_for_chart|safe }};

var userchart = new Chart(ctx, {
    type: 'line',
    data: {
        datasets: [{
            label: 'Total Users',
            data: data,
        }]
    },
    options: {
        // Customize chart options as needed
    }
});