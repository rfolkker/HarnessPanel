from unittest import TestCase
import unittest
import json
import requests

class PremiereTest(TestCase):
    def __init__(self, *args, **kwargs):
        super(PremiereTest, self).__init__(*args, **kwargs)
        result = requests.get('http://localhost:3200/ExportDom')
        f = open("result.json", "w")
        f.write(result.text)
        f.close()
        

    def dict_compare(self, d1, d2):
        d1_keys = set(d1.keys())
        d2_keys = set(d2.keys())
        intersect_keys = d1_keys.intersection(d2_keys)
        added = d1_keys - d2_keys
        removed = d2_keys - d1_keys
        modified = {o : (d1[o], d2[o]) for o in intersect_keys if d1[o] != d2[o]}
        same = set(o for o in intersect_keys if d1[o] == d2[o])
        return added, removed, modified, same
    
    def test_all_dom(self):
        data = ""
        compare = ""
        with open('result.json') as json_file:  
            data = json.load(json_file)
        result = requests.get('http://localhost:3200/ExportDom');
        self.assertEqual(result.status_code, 200)
        compare = json.loads(result.text)
        self.assertDictEqual(data, compare)

    def test_invalid_dom(self):
        data = ""
        compare = ""
        with open('result.json') as json_file:  
            data = json.load(json_file)
        ## Modify data to ensure invalid test
        data['InvalidValue'] = False
        result = requests.get('http://localhost:3200/ExportDom');
        self.assertEqual(result.status_code, 200)
        compare = json.loads(result.text)
        added, removed, modified, same = self.dict_compare(data,compare)
        self.assertEqual(len(added), 1)
        
if __name__ == '__main__':
    unittest.main()