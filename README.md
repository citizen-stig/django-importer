# django-importer

Django-importer allows import data from different data-sources.

For make it work, you need to setup appropriate parsers and importer for your model.

Parser class handles matching of raw data to your model fields.
Retriever class reads data from given source
Importer class run import procedure, which includes:
    - Retrieve data using Retriever class
    - Pass this data to Parser class
    - Create model from data, returned by parser.
    
    
For examples see simple django app. All stuff is placed in app "events" in "tasks" module