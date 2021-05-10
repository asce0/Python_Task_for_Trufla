import json
import xmltodict

def read_xml(filename):
    # read the xml file and convert it into dict
    with open(filename) as xml_file:
        data_dict = xmltodict.parse(xml_file.read())
        xml_file.close()

    return data_dict
    
def dict_to_json(data):
    # convert the dict  into a json string
    json_data = json.dumps(data)
    # write the json string into json file
    with open(r"C:\Users\ASCE\Desktop\GitRepo\Python_Task_for_Trufla\parsing_result\Xml_result\customer2.json", "w") as json_file:
        json_file.write(json_data)
        json_file.close()

