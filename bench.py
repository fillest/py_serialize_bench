import gc
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




import cStringIO
n = 100000
rn = [None] * n
rn1 = [None] * int(0.2 / 0.005)


def test_list():
	buf = []

	t1 = _time()
	for _ in rn:

		del buf[:]
		for __ in rn1:
			d = "path/to/some_proj/some/module.py:" + str(_) + ":function_name"
			# print len(d) * 40
			buf.append(d)
		res = "".join(buf)
		# print len(res)
		# raise SystemExit()

	lat = _time() - t1
	print "list", lat

def test_concat():
	t1 = _time()
	for _ in rn:

		buf = ""
		for __ in rn1:
			d = "path/to/some_proj/some/module.py:" + str(_) + ":function_name"
			# print len(d) * 40
			buf += d
		# res = "".join(buf)
		# print len(res)
		# raise SystemExit()

	lat = _time() - t1
	print "concat", lat

def test_bytearray():
	buf = bytearray()

	t1 = _time()
	for _ in rn:
		
		del buf[:]
		for __ in rn1:
			d = "path/to/some_proj/some/module.py:" + str(_) + ":function_name"
			# print len(d) * 40
			buf.extend(d)
		# res = "".join(buf)
		# print len(res)
		# raise SystemExit()

	lat = _time() - t1
	print "bytearray", lat

def test_list_prealloc():
	buf = [None] * 45

	t1 = _time()
	for _ in rn:

		i = 0
		for __ in rn1:
			d = "path/to/some_proj/some/module.py:" + str(_) + ":function_name"
			buf[i] = d
			i += 1
		res = "".join(buf[:i])

	lat = _time() - t1
	print "list_prealloc", lat

import collections
def test_deque():
	buf = collections.deque()

	t1 = _time()
	for _ in rn:

		buf.clear()
		for __ in rn1:
			d = "path/to/some_proj/some/module.py:" + str(_) + ":function_name"
			# print len(d) * 40
			buf.append(d)
		res = "".join(buf)
		# print len(res)
		# raise SystemExit()

	lat = _time() - t1
	print "deque", lat

def test_cstringio ():
	buf = cStringIO.StringIO()

	t1 = _time()
	for _ in rn:

		for __ in rn1:
			d = "path/to/some_proj/some/module.py:" + str(_) + ":function_name"
			# print len(d) * 40
			buf.write(d)
		buf.truncate()
		res = buf.getvalue()
		# print len(res)
		# raise SystemExit()
		buf.seek(0)

	lat = _time() - t1
	print "cstringio", lat

def test_cstringiom ():
	buf = cStringIO.StringIO()

	t1 = _time()
	for _ in rn:

		for __ in rn1:
			buf.write("path/to/some_proj/some/module.py:")
			buf.write(str(_))
			buf.write(":function_name")
		buf.truncate()
		res = buf.getvalue()
		# print len(res)
		# raise SystemExit()
		buf.seek(0)

	lat = _time() - t1
	print "cstringio m", lat

def test_mem ():
	# a = " " * (1024 * 4)
	# a = bytearray(1024 * 400)
	# a = bytearray(51000000)
	a = bytearray(len("path/to/some_proj/some/module.py:" + str(n) + ":function_name") * 40)
	buf = memoryview(a)
	assert buf.readonly == False
	
	t1 = _time()
	for _ in rn:

		pos = 0
		for __ in rn1:
			d = "path/to/some_proj/some/module.py:" + str(_) + ":function_name"
			ld = len(d)
			buf[pos:(pos + ld)] = d
			pos += ld
		res = buf[:pos].tobytes()

	lat = _time() - t1
	print "memoryview", lat





n = 10000000
rn = [None] * n

def test_comp ():
	t = _time()
	a = "GET"
	b1 = "/some/path/whatever"
	b2 = "/some/path/whatever1"
	s1 = str(t) + "|" + a + '|' + b1
	s2 = str(t) + "|" + a + '|' + b2
	assert s1 != s2
	
	t1 = _time()
	for _ in rn:
		# s1 = str(t) + "|" + a + '|' + b1
		# s2 = str(t) + "|" + a + '|' + b2

		res = s1 == s2

	lat = _time() - t1
	print "test_comp", lat

def test_intern ():
	t = _time()
	a = "GET"
	b1 = "/some/path/whatever"
	b2 = "/some/path/whatever1"
	s1 = intern(str(t) + "|" + a + '|' + b1)
	s2 = intern(str(t) + "|" + a + '|' + b2)
	assert s1 is not s2
	
	t1 = _time()
	for _ in rn:
		# s1 = intern(str(t) + "|" + a + '|' + b1)
		# s2 = intern(str(t) + "|" + a + '|' + b2)

		res = s1 is s2
		# pass

	lat = _time() - t1
	print "test_intern", lat


# n = 1000000
# rn = [None] * n

# def test_comp ():
# 	t = _time()
# 	a = "GET"
# 	b1 = "/some/path/whatever"
# 	b2 = "/some/path/whatever1"
# 	s1 = str(t) + "|" + a + '|' + b1
# 	s2 = str(t) + "|" + a + '|' + b2
# 	assert s1 != s2

# 	z = dict(a = "GET", b =  "/some/path/whatever")
	
# 	t1 = _time()
# 	for _ in rn:
# 		res = str(t) + "|" + z['a'] + '|' + z['b']

# 	lat = _time() - t1
# 	print "test_comp", lat

# j = '|'.join
# def test_intern ():
# 	t = _time()
# 	a = "GET"
# 	b1 = "/some/path/whatever"
# 	b2 = "/some/path/whatever1"
# 	s1 = str(t) + "|" + a + '|' + b1
# 	s2 = str(t) + "|" + a + '|' + b2
# 	assert s1 != s2

# 	z = dict(a = "GET", b =  "/some/path/whatever")

# 	t1 = _time()
# 	for _ in rn:

# 		res = j((str(t), z['a'], z['b']))

# 	lat = _time() - t1
# 	print "test_intern", lat


def main ():
	# fs = (test_pickle, test_ujson, test_marshal)
	# fs = (
	# 		test_cstringio,
	# 		test_deque,
	# 		test_concat,
	# 		test_bytearray,
	# 		test_list,
	# 		test_list_prealloc,
	# 		# test_cstringiom,
	# 		test_mem)
	fs = (test_comp, test_intern)
	for f in fs:
		for _ in range(3):
			gc.collect()
			f()


if __name__ == '__main__':
	main()