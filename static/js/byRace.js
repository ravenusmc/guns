data_racebarchart=[{"yAxis": "1", "key": "Serie 1", "values": [{"y": 66237, "x": "White"}, 
{"y": 23296, "x": "Black"}, {"y": 1326, "x": "Asian/Pacific Islander"}, {"y": 917, "x": "Native American"}, 
{"y": 9022, "x": "Hispanic"}]}];


            nv.addGraph(function() {
        var chart = nv.models.discreteBarChart();

        chart.margin({top: 30, right: 60, bottom: 20, left: 60});

        var datum = data_racebarchart;

                    chart.yAxis
                .tickFormat(d3.format(',.0f'));

            d3.select('#racebarchart svg')
            .datum(datum)
            .transition().duration(500)
            .attr('width', 800)
            .attr('height', 500)
            .call(chart);

    
        });