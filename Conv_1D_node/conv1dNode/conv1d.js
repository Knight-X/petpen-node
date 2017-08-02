module.exports = function(RED) {
    function convolutional1d_go(config) {
        RED.nodes.createNode(this,config);
	var node = this;
	this.on('convolutional1d', function(msg) {
        node.send(msg);
        
	});
    }
    RED.nodes.registerType("Conv_1D_node",convolutional1d_go);
};
