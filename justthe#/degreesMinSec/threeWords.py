import what3words
from os import environ

geocoder = what3words.Geocoder("339SOHLH") 
# what3words-api-key

autosuggest = geocoder.autosuggest('brilliant.convince.catch', \
    clip_to_country="UG", \
    focus=what3words.Coordinates(-0.617737, 30.656135), \
    n_results=1, \
)
#    48.856618, 2.3522411 ... focus
if 'error' in autosuggest: # An error has been returned from the API
    code = autosuggest['error']['code']
    message = autosuggest['error']['message']

    print (code, message)
else:
    # Obtains the one, and only result from the returned list of suggestions
    words = autosuggest['suggestions'][0]['words']
    print("Top 3 word address match: {}".format(words))

    # Use the `convert_to_coordinates` API to convert the returned 3 word address into coordinates
    convert_to_coordinates = geocoder.convert_to_coordinates(words)

    print("WGS84 Coordinates: {}, {}".format( \
        convert_to_coordinates['coordinates']['lat'], \
        convert_to_coordinates['coordinates']['lng']))
    print("Nearest Place: {}".format(convert_to_coordinates['nearestPlace']))