module.exports = function(RED) {
    function conv_lstm_2d_go(config) {
        RED.nodes.createNode(this,config);
	var node = this;
	this.on('conv_lstm_2d', function(msg) {
        node.send(msg);
        
	});
    }
    RED.nodes.registerType("ConvLSTM2D_node",conv_lstm_2d_go);
};
