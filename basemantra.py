
def test_object():
    try:
        # Creating the dictionary
        logger.info("test object")
        data = {
            "Title": "Sample Title",
            "Text": "This is a sample text."
        }
        logger.info(data)
        return(data)
    except Exception as e:
        logger.error("Error " + str(e))
        data
        # # To view the dictionary
        # print(data)

        # # If you want to convert the dictionary to a JSON string
        # import json
        # json_string = json.dumps(data)
        # print(json_string)



