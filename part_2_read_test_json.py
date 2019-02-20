import test_data
import json


#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json( json_data ):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()
    ### Begin Add Code Here ###
    #Loop through the json_data
        #Create a new Game object from the json_data by reading

    for game_data in json_data["Games"]:
        #  The loop steps through each element in the list (here the list is kids_data)
        #  and the variable kid_data represents the current element in the list
        #Make a new Kid
        game = test_data.Game()
        
        # Get the data from from the current kid in the kids_data list
        platform_json = game_data["Platform"]
        
        # game.platform.name = game_data["Name"]
        game.title = game_data["Title"]
        game.year = game_data["Year"]
        new_platform = test_data.Platform()
        new_platform.launch_year = platform_json["Year"]
        new_platform.name = platform_json["Name"]
        

        game_library.add_game(game)
        
        #Add that Game object to the game_library
    ### End Add Code Here ###

    return (game_library)

    
    


#Part 2
input_json_file = "data/test_data.json"

### Begin Add Code Here ###
#Open the file specified by input_json_file
with open("data/test_data.json","r") as reader:
#Use the json module to load the data from the file
    test_json = json.load(reader)
#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
test_data = make_game_library_from_json(test_json)
print(test_data)

#Print out the resulting GameLibrary data using print()

### End Add Code Here ###
