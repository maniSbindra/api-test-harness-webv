#! /bin/sh

echo "Test Type: $TEST_TYPE"
echo "Mongodb Database: $MONGO_DB"
echo "Mongodb Collection: $MONGO_COLL"

# Import the data into mongodb
mongoimport --uri $MONGO_URI --drop --db $MONGO_DB --collection $MONGO_COLL   --file /testFiles/$TEST_TYPE/Data/BooksTestData.json --jsonArray --legacy 
# mongo --host $MONGO_URI < /command/index.js

# The following sleep prevents mongo import container from exiting before the webv tests have completed
# When executing API tests using docker-compose the container exiting will cause the web tests to abort
sleep 1800