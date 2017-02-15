# Node Nextmail Coding  App

A Node app built with MongoDB and Angular. For demonstration purposes and a tutorial.

Node provides the RESTful API. Angular provides the frontend and accesses the API. MongoDB stores like a hoarder.

## Requirements

- [Node and npm](http://nodejs.org)
- MongoDB: Make sure you have your own local or remote MongoDB database URI configured in `config/database.js`

## Installation

1. Install the application: `npm install`
2. Go to public folder and do: `bower install`
3. Place your own MongoDB URI in `config/database.js`
4. Start the server: `node server.js`
5. View in browser at `http://localhost:3000`

## DB details
1. Database Name - indian_banks
2. collection name - bank
3. Schema - 
```
{
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
}
```

## Adding data to mongodb
1. Download csv from - https://raw.githubusercontent.com/nishantshobhit/indian_banks/master/bank_branches.csv
2. Run python add_data/add_Data.py
3. If libraries fail - contact rajanpriye03@gmail.com

## Implementation Details
1. For fetching all banks, mongoDb 'disticnt' function is used.
2. For fetcing city details - 
    * For every typed `string`, it will fetch top 10 city based on Regex
    * Future implementation solr can be used for very fash search result
    * Response for fetching city from query varies 10 - 100 milli second.
    * Based on selected Bank and City all the branches will be fetched.
    * Screen Shot for responses ![alt Bank Detail](https://github.com/priyaRanjan1/Bank/blob/master/screenshot/bank_name.png), ![alt City Detail](https://github.com/priyaRanjan1/Bank/blob/master/screenshot/city_name.png)



