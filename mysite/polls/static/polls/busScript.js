function bussFunction() {

  var x = document.getElementById("myBusSearch").value;
  var r = new XMLHttpRequest();
  r.open("GET", "bus_search?value=" + x, true);
  // r.open("GET", "db_req?value=" + x, true);
  r.onreadystatechange = function() {
    if (r.readyState != 4 || r.status != 200) return;
    (r.responseText);
    // document.getElementById("demo").innerHTML = r.responseText;
    data = JSON.parse(r.responseText)
    nodes = []
    // nodes.push({
    //   "name": x,
    //   "value": 10,
    //   "text": "aspect"
    // });


    for (var key in data)
      if (data.hasOwnProperty(key)) {
        nodes.push({
          "name": data[key].nouns[0].name,
          // "name": key,
          "value": data[key].nouns[0].value,
          "text": data[key].text
        });
      }
    nodes.sort(function(a, b) {
      return (a.value) - (b.value);
    });
    
    tmp_nodes=[]
    for(i=nodes.length-1; i>0; i--){
       tmp_nodes.push(nodes[i])
    }
    nodes=[]
    nodes.push({
      "name": x,
      "value": 10,
      "text": "aspect"
    });
    for( i in tmp_nodes )
      if(tmp_nodes[i]!=undefined || tmp_nodes[i].value<0)
        nodes.push(tmp_nodes[i])


    links = []
    for (i = 1; i < nodes.length; i++)
      links.push({
        "source": i,
        "target": 0
      });

    json = {
      "nodes": nodes,
      "links": links
    };
    draw();
    // graph={"nodes":nodes,"links":links};
  };
  // alert(x);
  r.send({
    "value": x
  });
}

function draw() {
  var radius = d3.scale.sqrt()
        .range([3, 10]);
  var width = 500,
    height = 500


  //remove previous graph
  var elem = document.getElementById("viz");
  if(elem !==null){
    elem.parentNode.removeChild(elem);
  }
  

  var svg = d3.select("body").append("svg")
    .attr("id", 'viz')
    .attr("width", width)
    .attr("height", height);

  var force = d3.layout.force()
    .gravity(0.05)
    .distance(100)
    .charge(-100)
    .size([width, height]);
  force
    .nodes(json.nodes)
    .links(json.links)
    .start();
  // setTimeout(function(){ force.stop(); }, 3000);

  var link = svg.selectAll(".link")
    .data(json.links)
    .enter().append("line")
    .attr("class", "link");

  var node = svg.selectAll(".node")
    .data(json.nodes)
    .enter().append("g")
    .attr("class", "node")
    .call(force.drag);

  // node.append("image")
  //     .attr("xlink:href", "https://github.com/favicon.ico")
  //     .attr("x", -8)
  //     .attr("y", -8)
  //     .attr("width", 16)
  //     .attr("height", 16);

  node.append("circle")
    // .filter(function(d){
    //     for(i=0;i<json.nodes.length;i++)

  //                 if(d.atom==sel_circle.atom) return d;
  //                 if(d.is_topic && d.atom==sel_circle.sizes[i].name) return d;
  //                 if(d.topic==sel_circle.atom ) {
  //                     draw_entity(d);
  //                     return d; 
  //                 }
  //             } })
  .attr("r", function(d) {
      // for(i=0;i<json.nodes.length;i++){
      // if (d.value<0){
      return radius(1+Math.abs(d.value) * 2)
        // }
        // }
    })
    .style("fill", function(d) {
        if (d.value < 0) {
          return "#ff0000"
        } else return "#00ff00"
      })

      node.append("text")
      .attr("dx", 12)
      .attr("dy", ".35em")
      .attr("fill", "black")
      .text(function(d) {
        return d.name
      });

      node.on('click', function(d) {
              document.getElementById("demo").innerHTML = d.text;
              // alert('aaa')
            });
      force.on("tick", function() {link.attr("x1", function(d) {return d.source.x; })
          .attr("y1", function(d) {
            return d.source.y;
          })
          .attr("x2", function(d) {
            return d.target.x;
          })
          .attr("y2", function(d) {
            return d.target.y;
          });

        node.attr("transform", function(d) {
          return "translate(" + d.x + "," + d.y + ")";
        });
        // alert(d.)
        // setTimeout(function(){ force.stop(); }, 1500);
      });
    }