console.log("Enter in javascript");

// Palette de couleurs utilisée par tous les graphiques
var colors = ["#1D507A", "#2F6999", "#66A0D1", "#8FC0E9", "#4682B4"];

d3.json('/api/yield/mean/cereals/wheat/time', display_nvd3_graph);

function display_nvd3_graph(data) {
      nv.addGraph(function() {

          var data_d3 = [{
              key: 'Mean yield',
              values: data
          }
          ]

          console.log(data_d3)
          var chart = nv.models.lineChart()
              .x(function(d) {
                  return d[0]
              })
              .y(function(d) {
                  return d[1]
              })
              // .yDomain([-5, 35])
              .height(270)
              .color(colors);

          chart.xAxis
              .showMaxMin(false)
              .axisLabel('Year')


          chart.yAxis //Chart y-axis settings
              .showMaxMin(false)
              .axisLabel('Yield (t/H)')
              .tickFormat(d3.format(',r'));

          d3.select('#yield svg')
            .datum(data_d3)
              .call(chart);

          nv.utils.windowResize(chart.update);

          return chart;
      });
}


console.log("End of javascript");



// nv.models.lineChart()
//   .margin({left: 100})  //Adjust chart margins to give the x-axis some breathing room.
//   .useInteractiveGuideline(true)  //We want nice looking tooltips and a guideline!
//   .transitionDuration(350)  //how fast do you want the lines to transition?
//   .showLegend(true)       //Show the legend, allowing users to turn on/off line series.
//   .showYAxis(true)        //Show the y-axis
//   .showXAxis(true)        //Show the x-axis
