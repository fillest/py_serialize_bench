Bench some Python serialization methods on some specific data.

`timeit` is not used because it does the similar stuff and is not convenient.

```
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

Example output:
```
$ python bench.py 
cPickle p2 1.44136309624 82
cPickle p2 1.50603795052 82
cPickle p2 1.50947213173 82
ujson 1.01340603828 82
ujson 1.00318002701 82
ujson 1.01054382324 82
marshal p2 0.807271957397 79
marshal p2 0.801562070847 79
marshal p2 0.802716016769 79
```