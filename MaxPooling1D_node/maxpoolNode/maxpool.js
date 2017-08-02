module.exports = function(RED) {
    function maxpooling1d_go(config) {
        RED.nodes.createNode(this,config);
	var node = this;
	this.on('maxpooling1d', function(msg) {
        node.send(msg);
        
	});
    }
    RED.nodes.registerType("MaxPooling1D",maxpooling1d_go);
};
