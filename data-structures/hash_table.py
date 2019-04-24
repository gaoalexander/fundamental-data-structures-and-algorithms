#--------------------------------------------------------------
# MOST BASIC IMPLEMENTATION

# hash_table_1 = [[] for i in range(10)]

# def hashfunction(key, hash_table):
# 	return key % len(hash_table)

# def insert(hash_table, key, value):
# 	hash_value = hashfunction(key, hash_table)
# 	hash_table[hash_value].append(value)

# insert(hash_table_1, 24, "Test")
# insert(hash_table_1, 39, "Test1")
# print(hash_table_1[hashfunction(39, hash_table_1)])


#--------------------------------------------------------------
# MORE ROBUST IMPLEMENTATION

def hash(key, hash_table):
	return key % len(hash_table)

def insert(hash_table, key, value):
	hash_value = hash(key, hash_table)
	bucket = hash_table[hash_value]
	key_exists = False
	for i, (k,v) in enumerate(bucket):
		if key == k:
			key_exists = True
			break
	if key_exists:
		bucket[i] = key, value
	else:
		bucket.append((key,value))

def search(hash_table, key):
	hash_value = hash(key, hash_table)
	bucket = hash_table[hash_value]
	for i, (k,v) in enumerate(bucket):
		if key == k:
			return v
	return None

def delete(hash_table, key):
	hash_value = hash(key, hash_table)
	bucket = hash_table[hash_value]
	for i, (k,v) in enumerate(bucket):
		if key == k:
			del bucket[i]

def test_implementation():
	hash_table_1 = [[] for bucket in range(100)]
	insert(hash_table_1, 25, "hello")
	insert(hash_table_1, 125, "hello2")
	print(hash_table_1)
	result = search(hash_table_1, 15)
	print(result)
	delete(hash_table_1, 25)
	print(hash_table_1)

test_implementation()

# def search(hash_table, key):