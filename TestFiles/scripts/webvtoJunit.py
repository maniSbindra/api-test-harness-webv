#!/usr/bin/env python3
'''
Utility to convert from webv output to JUnit format
'''

import sys
import json


def get_test_case_details(json_data):
    test_cases = ""
    test_suite_time = 0.0   
    test_case_count = 0
    failure_count = 0

    for test_case_json in json_data:
        test_case_name = str(test_case_json["tag"]) + ": " + str(test_case_json["verb"]) + ": " + encode_special_characters(str(test_case_json["path"]) )
        test_case_count += 1
        test_case_status = "passed"
        test_case_time = 0.0
        failed = test_case_json["failed"]
            
        if bool(failed) == True:
            err_blob = encode_special_characters(test_case_json["errors"])
            err_blob += "\nServer:" + encode_special_characters(test_case_json["server"])
            err_blob += "\nPath:" + encode_special_characters(test_case_json["path"])
            test_case_status = "failed"
            failure_count += 1

        test_case_time += float(test_case_json["duration"]) / 1000
        test_case = "<testcase "
        test_case += "classname=\"" + test_case_name + "\" "
        test_case += "name=\"" + test_case_name + "\" "
        test_case += "time=\"" + str(test_case_time) + "\">"
        if test_case_status == "passed":
            test_case += "<system-out>" 
            test_case += "</system-out>\n"
        else:
            test_case += "<failure message=\"" + err_blob + "\">"
            test_case += "</failure>\n"
        test_case += "</testcase>\n"

        test_cases += test_case
        test_suite_time += test_case_time
    return (test_cases, test_case_count, failure_count, test_suite_time)

def get_test_suite(test_cases_xml, test_case_count, failure_count, test_suite_time):
    test_suite = "<testsuite "
    test_suite += "failures=\"" + str(failure_count) + "\" "
    test_suite += "name=\"Webv to JUnit\" "
    test_suite += "skipped=\"0\" "
    test_suite += "tests=\"" + str(test_case_count) + "\" "
    test_suite += "time=\"" + str(test_suite_time) + "\">\n"
    for test_case in test_cases_xml:
        test_suite += test_case
    test_suite += "</testsuite>"

    return test_suite

def encode_special_characters(input_string):
    output_string = str(input_string).replace("&","&amp;")
    output_string = output_string.replace("\"","&quot;")
    output_string = output_string.replace("<","&lt;")
    output_string = output_string.replace(">","&gt;")
    return output_string


def main():
    '''
    Main func
    '''
    if len(sys.argv) < 2 or not sys.argv[1].endswith(".json"):
        print("JSON file path not found or incorrect:")
        sys.exit()
    if len(sys.argv) < 3 or not sys.argv[2].endswith(".xml"):
        print("XML file path incorrect")
        sys.exit()

    with open(sys.argv[1], "r") as json_file:
        print("Opening file " + sys.argv[1] + " in read-only mode")
        json_data = json.load(json_file)

    header = "<?xml version=\"1.0\" encoding=\"UTF-8\" standalone=\"no\"?>\n"

    # Get the XML, and aggregate details for test cases
    (test_cases, test_case_count, failure_count, test_case_total_time) = get_test_case_details(json_data)

    # Get the XML for test suite with embedded test cases
    test_suite = get_test_suite(test_cases, test_case_count, failure_count, test_case_total_time)
   
    with open(sys.argv[2], "w") as junit_file:
        print("Writing to file " + sys.argv[2] + "...")
        junit_file.write(header)
        junit_file.write(test_suite)

        print("webv report written in JUnit format...")


if __name__ == "__main__":
    main()