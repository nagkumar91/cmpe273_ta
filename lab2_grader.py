import requests
import unittest


class LabTwoTest(unittest.TestCase):
	def setUp(self):
		self.ports = [3001,3002,3003,3004,3005]
		self.keys = ["1", "2", "3", "4", "5"]
		self.expected_values = {
			"1": "A",
			"2": "B",
			"3": "C",
			"4": "D",
			"5": "E",
			"6": "F"
		}
		self.output = []
		for port in self.ports:
			url = "http://localhost:%s/" % port
			for key in self.keys:
				go_server_url = "%s%s" % (url, key)
				r = requests.get(go_server_url)
				for k, v in r.json().iteritems():
					self.output.append({k:v})
		self.flattened_output = reduce(lambda row, dictionary: row.update(dictionary) or row, self.output, {})
		print self.flattened_output

	def test_if_output_has_all_keys_and_values(self):
		for key in self.keys:
			self.assertTrue(key in self.flattened_output)
			# key = str(key)
			self.assertEqual(self.flattened_output[key], self.expected_values[key])
