data_typebarchart = [{"key": "Deaths by Type", "values": [{"x": "Accidental", "y": 1639}, 
 {"x": "Homicide", "y": 35176}, {"x": "Suicide", "y": 63175}, {"x": "Undetermined", "y": 807}],
  "yAxis": "1"}];


nv.addGraph(function() {
var chart = nv.models.discreteBarChart();

chart.margin({top: 30, right: 60, bottom: 20, left: 60});

var datum = data_typebarchart;



      chart.yAxis
  .tickFormat(d3.format(',.0f'));








d3.select('#typebarchart svg')
.datum(datum)
.transition().duration(500)
.attr('width', 400)
.attr('height', 400)
.call(chart);


});