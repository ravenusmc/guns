data_educbarchart = [{"yAxis": "1", "values": [{"y": 21823, "x": "< High School"}, 
{"y": 42927, "x": "High School"}, {"y": 21680, "x": "Some College"}, 
{"y": 12946, "x": "Graduated College"}, {"y": 1369, "x": "Not Available"}], "key": "Serie 1"}];

            nv.addGraph(function() {
        var chart = nv.models.discreteBarChart();

        chart.margin({top: 30, right: 60, bottom: 20, left: 60});

        var datum = data_educbarchart;



                    chart.yAxis
                .tickFormat(d3.format(',.0f'));

            d3.select('#educbarchart svg')
            .datum(datum)
            .transition().duration(500)
            .attr('width', 800)
            .attr('height', 500)
            .call(chart);
        });