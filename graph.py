# Graph

from collections import Counter
from parse import parse

import csv
import matplotlib.pyplot as plt
import numpy.numarray as na

MY_FILE = "./data/sample_sfpd_incident_all.csv"

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
