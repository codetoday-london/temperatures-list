# We have a list with all the daily mean temperatures since 1772, in ºC
# We need to write a few functions to look at some of the stats from these
# data
#
# Note: the data are being loaded from an external Python data file using the
# pickle package. This is one way of storing data on disk to use across
# different Python scripts/programs or for the same script/program
# to save the output for the next time it runs
# You will need to have the file called `temperatures_list` in the same folder as this
# script for this to work.
# You can download it from the following link: https://github.com/codetoday-london/temperatures-list.git

import pickle

temperatures = pickle.load(open("temperatures_list", 'rb'))

# temperatures is a list of float

def find_n_days_below(input_temp, input_data):
    '''
    Finds the number number of days below (or equal to) input_temp from
    the temperatures in input_data. Returns both number of days
    and percentage

    :param input_temp: desired input temperature (int or float)
    :param input_data: list containing all the daily mean temperature data

    :return int with number of days:
    :return float with percentage:

    '''

    for temperature in input_data:
        if temperature <= input_temp:
            n_days = n_days + 1

    percent = n_days / len(temperatures) * 100


print(f"The number of days below or equal to {desired_temp}ºC (mean temperature) since 1772 is {number_of_days}. That is {percentage:0.1f}% of all days.")
