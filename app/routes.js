var bank = require('./models/bank');
var response_config_success = {
    "status" : "ok",
    "message" : "",
    "data" : []
}

var result_limit = 10;

exports.index_page = function(req, res, next) {
    res.sendFile(__dirname + '/view/index.html')

}

exports.get_bank = function(req, res, next) {
    bank.distinct('bank_name',function(error, results){
        if(!error){
            response_config_success.data = results;
            response_config_success.message = "Found";
            res.status(200).json(response_config_success)
        } else {
            response_config_success.data = [];
            response_config_success.message = "No Data Found";
            res.status(200).json(response_config_success)
        }
    });
    
};

exports.get_bank_cities = function(req, res, next) {
    var city_name = req.body.city_name;
    var city_name_regex = new RegExp('^'+city_name);
    bank.distinct('city',{'city': city_name_regex}, function(error, results) {
        if(!error){
            results.splice(result_limit)
            response_config_success.message = "Top 10 City"
            response_config_success.data = results;
            res.send(response_config_success);
        } else {
            response_config_success.data = [];
            response_config_success.message = "No Data Found";
            res.status(200).json(response_config_success)
        }
    });

};

exports.all_branches = function(req, res, next) {

    var city_name = req.body.city_name;
    var bank_name = req.body.bank_name;
    bank.find({'city': city_name, 'bank_name' : bank_name}, function(error, results) {
        if(!error){
            response_config_success.message = "Branch List"
            response_config_success.data = results;
            res.send(response_config_success);
        } else {
            response_config_success.data = [];
            response_config_success.message = "No Data Found";
            res.status(200).json(response_config_success)
        }
    });
};
