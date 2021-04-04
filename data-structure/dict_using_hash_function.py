class MyDict:
    def __init__(self):
        self.size = 8
        self.hashmap = [[] for _ in range(0, self.size)]
        self.length = 0

    def custom_hash(self, key):
        index_key = hash(key)%(self.size - 1)
        return index_key

    def insert_item(self, key, value):
        hash_key = self.custom_hash(key)
        key_exists = False

        bucket = self.hashmap[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            bucket[i] = (key, value)
        else:
            bucket.append((key, value))
        self.length += 1

    def get_item(self, key):
        hash_key = self.custom_hash(key)
        bucket = self.hashmap[hash_key]

        for kv in bucket:
            k,v = kv
            if key == k:
                return v
        raise KeyError("Key doesn't exist")

    def delete_item(self, key):
        hash_key = self.custom_hash(key)
        bucket = self.hashmap[hash_key]

        for i, kv in enumerate(bucket):
            k,v = kv
            if key == k:
                del bucket[i]
                self.length -= 1
                return True
        raise KeyError("Key doesn't exist")

    def __getitem__(self, key):
        return self.get_item(key)

    def __setitem__(self, key, value):
        return self.insert_item(key, value)

    def __delitem__(self, key):
        return self.delete_item(key)

    def __len__(self):
        return self.length



if __name__ == "__main__":
    d = MyDict()

    d["key1"]="value1"
    d["key2"]="value2"
    d["key3"]="value3"
    d["key4"]="value4"

    print(len(d))
    del d["key4"]
    print(len(d))