new function () {
// >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

kukit.actionsGlobalRegistry.register("inlinejs-effect", function(oper) {
	oper.evaluateParameters(['code'], {'debug':false});

        var code = oper.parms.code;
        var debug = oper.parms.debug;
        var node = oper.node;
        try {
            eval(code);
            }
        catch(ex) {
                if (debug == '1') {
                    alert(ex.message);
                }
            }
});
kukit.commandsGlobalRegistry.registerFromAction('inlinejs-effect', 
                                                kukit.cr.makeSelectorCommand);



// <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
}();
