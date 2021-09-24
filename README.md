# RESTful-web-service-using-Python-and-the-Flask-microframework
In this course project, I implemented a RESTful web service using Python and the Flask microframework.
Central to the concept of RESTful web services is the notion of resources. Resources are
represented by URIs. The clients send requests to these URIs using the methods defined by the
HTTP protocol, and possibly as a result of that the state of the affected resource changes. Therefore,
we need to select the resources that will be exposed by this service.
The key/value resource will use HTTP methods as follows:

<p align = "center">
  <img src = "https://github.com/mandanaGh/RESTful-web-service-using-Python-and-the-Flask-microframework/blob/main/images/RESTful_web_ervice.jpg" width = 700>
  </p>


I implemented a simple web application, in a file called app.py. The client of
our web service will be asking the service to add and retrieve key/value pairs, so clearly we need to
have a way to store key/value pairs. The obvious way to do that is to build a small database, but for
simplicity, I stored key/value pairs in a memory structure, which is nothing more than a plain and
simple array of dictionaries. Each entry in the array has the fields as defined below. This will only
work when the web server that runs our application is a single process and single threaded.
We can define a key/value pair as having the following fields (Json format):
```
keyValue_db=[{
'key': name,
'value': value,
'version': version
}]
```

After starting the web service (by running app.py), the client can use resources as follow:
```
./client set key1 value1
./client get key1
./client history key1
```
