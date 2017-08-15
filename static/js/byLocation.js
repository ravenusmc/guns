data_locationbarchart = [{"yAxis": "1", "key": "Serie 1", "values": [{"x": "Farm", "y": 470}, 
{"x": "Home", "y": 60486}, {"x": "Street", "y": 11151}, {"x": "Trade/service area", "y": 3439}, 
{"x": "Residential institution", "y": 203}, {"x": "Street", "y": 11151}, 
{"x": "Industrial/construction", "y": 248}]}];


            nv.addGraph(function() {
        var chart = nv.models.discreteBarChart();

        chart.margin({top: 30, right: 60, bottom: 20, left: 60});

        var datum = data_locationbarchart;



                    chart.yAxis
                .tickFormat(d3.format(',.0f'));

            d3.select('#locationbarchart svg')
            .datum(datum)
            .transition().duration(500)
            .attr('width', 900)
            .attr('height', 500)
            .call(chart);    
        });