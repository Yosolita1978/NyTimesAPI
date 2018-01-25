(function(){
    var width = 500;
    var height = 500;

    var svg = d3.select("#chart")
    .append("svg")
    .attr("height", height)
    .attr("width", width)
    .append("g")
    .attr("transform", "translate(100,400)")

    var simulation = d3.forceSimulation()
    .force("x", d3.forceX(width / 2).strength(0.05))
    .force("y", d3.forceY(height / 2).strength(0.05))

    d3.queue()
    .defer(d3.csv, "output_trump.csv")
    .await(ready)

    function ready(error, datapoints){

        var circles = svg.selectAll(".word")
        .data(datapoints)
        .enter().append("circles")
        .attr("class", "word")
        .attr("r", 100)
        .attr("fill", "red")
        
        simulation.nodes(datapoints)
        .on('tick', ticked)

        function ticked(){
            circles
            .attr("cx", d => d.x)
            .attr("cy", d => d.y)
        }
    }

})();