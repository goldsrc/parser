parser
============

Simple web service, The methods are based on nltk. Models are passed as POST requests and must be in text format. and returns in text/json format

* Launching the service
```
python parser [--port 1234]
```

* Example call
```
curl --form sent="Something New" http://127.0.0.1:5000/parse
```
