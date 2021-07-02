const Supercluster = require('supercluster');
const GeoJSON = require('geojson');
var data = require('./cut2_6.json')


module.exports = {
    clusteredMarkers:  (box,czoom) => {
    try{
      let zoom = czoom;
      let index = new Supercluster({
          radius: 256,
          maxZoom: 18
       }).load(data);
       return  index.getClusters(box, zoom);
     
    }catch(err){
        if(err){
            return 'get clusters failed';
        }
    }
    },
    getClusterZoom:  (id) => {
        
        try{
          let index = new Supercluster({
              radius: 256,
              maxZoom: 18
           }).load(data);
           //console.log(index.getClusterExpansionZoom(id));
           return  index.getClusterExpansionZoom(id);
         
        }catch(err){
            if(err){
                return 'getcluster zoom failed';
            }
        }
    },
    getChildren:  (id) => {
        
        try{
          let index = new Supercluster({
              radius: 256,
              maxZoom: 18
           }).load(data);
           //console.log(index.getClusterExpansionZoom(id));
           return  index.getLeaves(id, limit = Infinity);
         
        }catch(err){
            if(err){
                return 'getcluster zoom failed';
            }
        }
    }
};
