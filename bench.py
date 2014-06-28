from time import time as _time
import cPickle as pickle
pickle_dumps = pickle.dumps
import ujson
ujson_dumps = ujson.dumps
import marshal
marshal_dumps = marshal.dumps


n = 1000000
rn = [None] * n


PPROTO = 2
data = (16769, 140174002231040, 'path/to/some_proj/some/module.py', 123, 'function_name')


def test_pickle ():
	t1 = _time()
	for _ in rn:

		result = pickle_dumps(data, PPROTO)

	lat = _time() - t1
	print "cPickle p2", lat, len(result)

def test_ujson ():
	t1 = _time()
	for _ in rn:

		result = ujson_dumps(data)

		# result = ujson_dumps(data, ensure_ascii = False)
	lat = _time() - t1
	print "ujson", lat, len(result)

def test_marshal ():
	t1 = _time()
	for _ in rn:

		result = marshal_dumps(data, PPROTO)

	lat = _time() - t1
	print "marshal p2", lat, len(result)


def main ():
	for f in (test_pickle, test_ujson, test_marshal):
		for _ in range(3):
			f()


if __name__ == '__main__':
	main()