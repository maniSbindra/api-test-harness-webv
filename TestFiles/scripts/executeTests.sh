#! /bin/sh

echo "Service test endpoint: =$TEST_SVC_ENDPOINT"
echo "Test Type: $TEST_TYPE"

# Wait for test data to get loaded before executing the webv tests
date
echo "sleeping ..."
sleep $TEST_DATA_LOAD_DELAY
echo "waking up...."
date
cd /testFiles/$TEST_TYPE/TestCases

# Execute the webv tests
dotnet "/app/webvalidate.dll" --server $TEST_SVC_ENDPOINT --files BooksTestCases.json --verbose-errors --verbose --json-log --max-errors 200
