import parsers.csv_parser
import parsers.xml_parser
import sys



print("Done!!")
if sys.argv[1] == 'xml':
    data = parsers.xml_parser.read_xml(sys.argv[2])
    parsers.xml_parser.dict_to_json(data)

elif sys.argv[1] == 'csv':
    parsers.csv_parser.merge_csv(sys.argv[2], sys.argv[3])
    parsers.csv_parser.generate_json()

