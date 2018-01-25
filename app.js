d3.select("div")
.insert("h2")
.text("The most commons words in the headlines about Mexico")
.attr("class", "test")
.style("color", '#673ab7')
.style("text-align", "center")


d3.select("div")
.insert("svg")
.attr("class", "bubbles")
.attr("width", 200)
.attr("height", 200)
.style("display", "block")
.style("margin", "0 auto")


var dataset;
    d3.csv('output_trump.csv', function(error, data) {
      if (error) {
          console.error('Error getting or parsing the data.');
          throw error;
      } else{
        dataset = data;
      }
      var chart = bubbleChart().width(600).height(400);
      d3.select('.test').data(dataset).call(chart);
    });

function bubbleChart() {
    var width = 960,
        height = 960,
        maxRadius = 6,
        columnForColors = "Word",
        columnForRadius = "frequency";

    function chart(selection) {
        var data = selection.enter().data();
        var div = selection,
            svg = div.selectAll('svg');
        svg.attr('width', width).attr('height', height);

        var tooltip = selection
            .append("div")
            .style("position", "absolute")
            .style("visibility", "hidden")
            .style("color", "white")
            .style("padding", "8px")
            .style("background-color", "#626D71")
            .style("border-radius", "6px")
            .style("text-align", "center")
            .style("font-family", "monospace")
            .style("width", "400px")
            .text("");


        var simulation = d3.forceSimulation(dataset)
            .force("charge", d3.forceManyBody().strength([-50]))
            .force("x", d3.forceX())
            .force("y", d3.forceY())
            .on("tick", ticked);

        function ticked(e) {
            node.attr("cx", function(d) {
                    return d.x;
                })
                .attr("cy", function(d) {
                    return d.y;
                });
        }

        var colorCircles = d3.scaleOrdinal(d3.schemeCategory10);
        var scaleRadius = d3.scaleLinear().domain([d3.min(dataset, function(d) {
            return +d[columnForRadius];
        }), d3.max(dataset, function(d) {
            return +d[columnForRadius];
        })]).range([5, 18])

        var node = svg.selectAll("circle")
            .data(dataset)
            .enter()
            .append("circle")
            .attr('r', function(d) {
                return scaleRadius(d[columnForRadius])
            })
            .style("fill", function(d) {
                return colorCircles(d[columnForColors])
            })
            .attr('transform', 'translate(' + [width / 2, height / 2] + ')')
            .on("mouseover", function(d) {
                tooltip.html(d[columnForColors] + "<br>" + d[columnForRadius] + " mentions");
                return tooltip.style("visibility", "visible");
            })
            .on("mousemove", function() {
                return tooltip.style("top", (d3.event.pageY - 10) + "px").style("left", (d3.event.pageX + 10) + "px");
            })
            .on("mouseout", function() {
                return tooltip.style("visibility", "hidden");
            });
    }

    chart.width = function(value) {
        if (!arguments.length) {
            return width;
        }
        width = value;
        return chart;
    };

    chart.height = function(value) {
        if (!arguments.length) {
            return height;
        }
        height = value;
        return chart;
    };


    chart.columnForColors = function(value) {
        if (!arguments.columnForColors) {
            return columnForColors;
        }
        columnForColors = value;
        return chart;
    };

    chart.columnForRadius = function(value) {
        if (!arguments.columnForRadius) {
            return columnForRadius;
        }
        columnForRadius = value;
        return chart;
    };

    return chart;
}
