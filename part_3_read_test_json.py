import cc_dat_utils
import json
import cc_data


def make_cc_level_from_json(level_data):
    # level_library = cc_data.CCDataFile()
    new_level = cc_data.CCLevel()
    new_level.level_number = level_data["level_number"]
    new_level.num_chips = level_data["num_chips"]
    new_level.upper_layer = level_data["upper_layer"]
    new_level.time = level_data["time"]
    for field_json in level_data["optional_fields"]:
        new_field = None

        print("field_json: " + str(field_json))
        if field_json["id"] == "Hint":
            new_field = cc_data.CCMapHintField(field_json["hint_data"])
            new_level.add_field(new_field)
        if field_json["id"] == "Password":
            new_field = cc_data.CCEncodedPasswordField(field_json["Password_data"])
            new_level.add_field(new_field)
        if field_json["id"] == "title":
            new_field = cc_data.CCMapTitleField(field_json["title_data"])
            new_level.add_field(new_field)
        elif field_json["id"] == "monsters":
            monster_coords = []
            for monster_json in field_json["monster_data"]:
                monster_coords.append(cc_data.CCCoordinate(monster_json[0], monster_json[1]))
            new_field = cc_data.CCMonsterMovementField(monster_coords)
            new_level.add_field(new_field)
    return new_level


# Part 3
# Load your custom JSON file
with open("data/sehenry_cc_level_data.json", "r") as reader:
    test_json = json.load(reader)
# Convert JSON data to cc_data
new_level_library = cc_data.CCDataFile()
for level_json in test_json["Levels"]:
    new_level = make_cc_level_from_json(level_json)
    new_level_library.add_level(new_level)
print(new_level_library)

# cc_level_data = make_cc_level_from_json(test_json)

# Save converted data to DAT file
cc_dat_utils.write_cc_data_to_dat(new_level_library, "data/sehenry_cc_level_data.dat")

# # print(pfgd_test_data)
# print(cc_level_data)
