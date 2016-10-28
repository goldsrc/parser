parser
============

Simple web service to parse and tag all the words in one sentence, The methods are based on nltk part-of-speech tagger.
Sentences are passed as POST requests and must be in text format.
the service returns an JSON String that includes each word and it's tag.

* Launching the service
```
python parser.py [--port 1234]
```

* Example call
```
curl --form sent="And now for something completely different" http://127.0.0.1:5000/parse
```

* Example Returned JSON
```
[
    {
        "And": "CC"
    },
    {
        "now": "RB"
    },
    {
        "for": "IN"
    },
    {
        "something": "NN"
    },
    {
        "completely": "RB"
    },
    {
        "different": "JJ"
    }
]
```
Here we see that and is CC, a coordinating conjunction; now and completely are RB, or adverbs; for is IN, a preposition; something is NN, a noun; and different is JJ, an adjective.
you can find explanation for each of these tag in [here](all_tags.txt)
