### Intelligence measurement system project

#### Authors:
* Erkid Hoxholli (179040)
* Nandan Hegde (179042)

## AWS pipeline setup
* Setup SQS (simple queue service) and created a queue
* Setup DynamoDB instance
* Create lambda function that is triggered when we send a message (our data) in SQS
* The lambda function saves the data in the database
* Setup API gateway as a separate lambda function used to read the data and generate REST API endpoint
* In this lambda function we also do the calculation logic and grouping of the wifi routers (you can check the files upload for more info)
* We used Cloudwatch to look for logs or errors that we encountered while setting up the lambda service.

## Deployment
* We used netlify to deploy our static assets (js, html) which are used to make ajax call to get the API data as well as show the map and charts.
* CORS was activated in the API gateway to allow ajax calls from our deployed website.

### Generating map and chart
* The map shows the groups of routers in Tricity where the radius of each group is 3Km. We are using leaflet.js to show map and draw radius and markers.
![map](https://github.com/jwszol-classes/ims-2019-nanduhalasige/blob/master/map.PNG?raw=true)

* The graph shows in the X-axis the number of groups and in the Y-axis the number of wifi routers corresponding to each group. We used highchart js library
![chart](https://github.com/jwszol-classes/ims-2019-nanduhalasige/blob/master/chart.PNG?raw=true)

### API endpoint response
* We get the following data from the API gateway which we manipulate in Javascript to it feed into our graph and map.
![api-gateway-response](https://github.com/jwszol-classes/ims-2019-nanduhalasige/blob/master/api-call-response.PNG?raw=true)

### Sending our data message via SQS
![sqs-message](https://github.com/jwszol-classes/ims-2019-nanduhalasige/blob/master/sqsMessage.PNG?raw=true)


### Implementation of File upload from Postman.
* We can upload csv file from Postman with Content-Type is set to multipart/form-data. 
* New Lambda function is created as an API Gateway which will recieve the uploaded file content and we will be parsing the content and the content is sent to sqs queue using sqs.send_message() 
![File-upload](https://github.com/jwszol-classes/ims-2019-nanduhalasige/blob/master/fileupload.PNG?raw=true)
