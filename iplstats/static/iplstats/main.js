function plot_matches_played(){
    Highcharts.chart('plot-container', {
        chart: {
            type: 'column'
        },
        title: {
            text: 'Matches Played Per Season'
        },
        xAxis: {
            categories: [
                {% for entry in data %}'{{ entry.season }}'{% if not forloop.last %}, {% endif %}{% endfor %}
            ]
        },
        series: [{
            name: 'Matches Played',
            data: [
                {% for entry in data %}{{ entry.id__count }}{% if not forloop.last %}, {% endif %}{% endfor %}
            ],
            color: 'skyblue'
        } ]
    });
}



// Highcharts.chart('container', {
//     chart: {
//       type: 'bar'
//     },
//     title: {
//       text: 'Stacked bar chart'
//     },
//     xAxis: {
//       categories: ['Apples', 'Oranges', 'Pears', 'Grapes', 'Bananas']
//     },
//     yAxis: {
//       min: 0,
//       title: {
//         text: 'Total fruit consumption'
//       }
//     },
//     legend: {
//       reversed: true
//     },
//     plotOptions: {
//       series: {
//         stacking: 'normal'
//       }
//     },
//     series: [{
//       name: 'John',
//       data: [5, 3, 4, 7, 2]
//     }, {
//       name: 'Jane',
//       data: [2, 2, 3, 2, 1]
//     }, {
//       name: 'Joe',
//       data: [3, 4, 4, 2, 5]
//     }]
//   });