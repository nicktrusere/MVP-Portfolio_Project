This a Mobile Network Site Performance Tracker

To handle data transfer and monitor 
network performance -> Mobile Cellphone Towers/Sites.  A radio access network (RAN) connects individual devices to other parts of a network through radio connections. It is a major component of modern telecommunications with different generations of mobile networking evolving from 1G through 5G.

This project aims to model data from a fake database(Back-End) to be manipulated by a user(Front-End) - connected via an Restful-API.

Installations and set - up - Done.

-Flask
-SQLAlchemy -- ORM - similar to Sqlite/Mongoese - Mongo DB
-Marshmellow - Serialization and Deserialization passing through Schema. 
-Postman - Requests to API  for data - testing API using HTTP - methods CRUD.

Minimum Viable Product (MVP) Specification
The MVP of the "RAN Mobile Network Site Performance Tracker" project consists of the following features:

1. Display basic Site Information that includes:
Site_Type_Model  eg Huaweii/Nokia
Site_Name 
Number of Panels/Cells on Site 
Range - Network Coverage Distance  (m/km) 
Emergency Battery Device_Power Supply 
Alarms on Site:
GPS  Coordinates of Site

2. Network Elements- Dashboard to show
Network Speed available on the site 5G/4G- LTE/3G/GSM,  Network Un_Availablity displayed as a % and Rate of 2 % unavailability as benchmark..
Call_traffic  per Sec and Data Traffic displayed as volume per second handled by the site
SMS_traffic per Sec and Dropped Calls Rate i.e the number of calls dropped by siteper volume per minute. 
Call Set Up and Call Success Rate i.e calls that connect first time

3. Create a Backend Data Storage (Static and Dynamic) - databases.
4. Create and Implement An  API to fetch the data.
3.  Implement error handling to display clear messages for invalid user input or API errors.
4.       Ensure responsive design for various devices to provide a consistent user experience.
5.       User page with log-in details
6.    Store  user profile in database with rights and user authentication are outside the current scope.
Architecture:
The architecture involves a Flask web application that serves as the backend. The frontend interacts with the user and requests data from the backend. The backend communicates with the API  to fetch user data and then responds to frontend requests with the fetched data. The data flow diagram below provides more illustration of this architecture.

Only a few of the mention attributes will be implemented and others added on as project develops. 
