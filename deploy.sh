
if [ -f function.zip ]; then
	rm function.zip
fi
cd ./modules
zip -r9 ../function.zip .
cd ../nc_covid_response
zip -gr9 ../function.zip .
cd ..
aws lambda update-function-code --function-name nc-covid-send-sms --zip-file fileb://function.zip