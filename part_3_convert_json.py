import cc_dat_utils
import json


def make_level_library_from_json(json_data):

	level_library = cc_data.CCDataFile()
	for level_data in json_data["Levels"]:
		level = test_data.CCLevel()
		level_library.time = level_data["time"]
		level_library.level_number = level_data["level_number"]
		level_library.num_chips = level_data["num_chips"]
		level_library.optional_fields = level_data["optiona_fields"]
		level_library.upper_layer = level_data["upper_layer"]
		




	pfgd_test_data = cc_dat_utils.make_cc_data_from_dat("data/sehenry_cc1.json")
	cc_dat_utils.write_cc_data_to_dat(pfgd_test_data, "data/copy_of_sehenry_cc1.json")
	pfgd_test_data

#Part 3
#Load your custom JSON file
with open ("data/sehenry_cc1.json","r") as reader:
	test_json = json.load(reader)
#Convert JSON data to cc_data
cc_data = make_level_library_from_json(test_json)
#Save converted data to DAT file

print(pfgd_test_data)







print(make_level_library_from_json(test_json))