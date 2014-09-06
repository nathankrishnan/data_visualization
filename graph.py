# Graph

from collections import Counter

import csv
import matplotlib.pyplot as plt
import numpy.numarray as na

MY_FILE = "./data/sample_sfpd_incident_all.csv"

def parse(raw_file, delimeter):
	""" Parses a raw CSV file to a JSON-like object. """	
	
	# Open CSV file
	opened_file = open(raw_file)

	# Read CSV file
	csv_data = csv.reader(opened_file, delimiter=delimeter)

	# Setup an empty list
	parsed_data = []

	# Skip over the first line of the file for the headers
	fields = csv_data.next()
	
	# Iterate over each row of the csv file, zip together field -> value
	for row in csv_data:
		parsed_data.append(dict(zip(fields, row)))
	
	# Close CSV file
	opened_file.close()

	return parsed_data

def visualize_days():
    """Visualize data by day of week"""
    data_file = parse(MY_FILE, ",")
    # Returns a dict where it sums the total values for each key.
    # In this case, the keys are the DaysOfWeek, and the values are
    # a count of incidents.
    counter = Counter(item["DayOfWeek"] for item in data_file)

    # Separate out the counter to order it correctly when plotting.
    data_list = [
                  counter["Monday"],
                  counter["Tuesday"],
                  counter["Wednesday"],
                  counter["Thursday"],
                  counter["Friday"],
                  counter["Saturday"],
                  counter["Sunday"]
                ]
    day_tuple = tuple(["Mon", "Tues", "Wed", "Thurs", "Fri", "Sat", "Sun"])

    # Assign the data to a plot
    plt.plot(data_list)

    # Assign labels to the plot from day_list
    plt.xticks(range(len(day_tuple)), day_tuple)

    # Save the graph!
    plt.savefig("Days.png")

    # Close figure
    plt.clf()	

def main():
	visualize_days()


# Boilerplate code
if __name__ == "__main__":
    main()
