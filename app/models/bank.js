var mongoose = require('mongoose');

module.exports = mongoose.model('bank', {
    ifsc: String,
    bank_id: String,
    branch: String,
    address: String,
    city: String,
    district: String,
    state: String,
    bank_name: String,
    createdDate: {
        type: Date,
        default: Date.now
    }
});



