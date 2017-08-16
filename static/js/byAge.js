data_agebarchart = [{"values": [{"y": 509, "x": "0-10"}, {"y": 9418, "x": "11-20"}, 
{"y": 22466, "x": "21-30"}, {"y": 15993, "x": "31-40"}, {"y": 15258, "x": "41-50"}, 
{"y": 15856, "x": "51-60"}, {"y": 10104, "x": "61-70"}, {"y": 6485, "x": "71-80"}, 
{"y": 4077, "x": "81-90"}, {"y": 609, "x": "91-100"}], "yAxis": "1", "key": "Serie 1"}];


            nv.addGraph(function() {
        var chart = nv.models.discreteBarChart();

        chart.margin({top: 30, right: 60, bottom: 20, left: 60});

        var datum = data_agebarchart;

                    chart.yAxis
                .tickFormat(d3.format(',.0f'));

            d3.select('#Agebarchart svg')
            .datum(datum)
            .transition().duration(500)
            .attr('width', 800)
            .attr('height', 500)
            .call(chart);

    
        });