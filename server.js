const express = require('express');
const app = require('express')();
const http = require('http').Server(app);
const io = require('socket.io')(http);
var path = require('path');

//const worker = require('./worker.js');
var  clustering  = require('./worker.js');

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/public/index.html');
//  res.sendFile(__dirname +'/public/style.css');
});



io.on('connection', (socket) => {
  socket.on('bounds_changed', (bbox,zoom,clusters) => {

    var clusters = clustering.clusteredMarkers(bbox,zoom);
    socket.emit('bounds_changed',bbox,zoom,clusters);
    
  });
  socket.on('getZoom', (feature,zoom,center) => {
    socket.emit('getZoom',feature,clustering.getClusterZoom(feature.properties.cluster_id),center);
  });
  socket.on('getChildren', (feature,children,center) => {
    socket.emit('getChildren',feature,clustering.getChildren(feature.properties.cluster_id),center);
  });
  
});

http.listen(8081, () => {
  console.log('listening on :8081');
});
//app.use(express.static("/public/"));
app.use(express.static(path.join(__dirname, '/public/')));




