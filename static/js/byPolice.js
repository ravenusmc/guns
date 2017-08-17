data_policebarchart=[{"values": [{"x": "Not police killed", "y": 99396}, 
{"x": "Police killed", "y": 1402}], "yAxis": "1", "key": "Serie 1"}];

            nv.addGraph(function() {
        var chart = nv.models.discreteBarChart();

        chart.margin({top: 30, right: 60, bottom: 20, left: 60});

        var datum = data_policebarchart;

                    chart.yAxis
                .tickFormat(d3.format(',.0f'));

            d3.select('#policebarchart svg')
            .datum(datum)
            .transition().duration(500)
            .attr('width', 800)
            .attr('height', 500)
            .call(chart);
});