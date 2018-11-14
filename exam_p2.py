import csv
def process_file(file_name):
    """
    Given a file name, returns a list of lists [name, gender, births]
    HINT: https://stackoverflow.com/a/35340988/941742

    :param file_name: a string
    :return: a list of lists, [[name1, gender1, births1], [name2, gender2, births2]...]

    Example:
    process_file('yob1880.txt')
        will return
    [["Mary","F",7065], ["Anna","F",2604],...]

    """
    with open(file_name, 'r') as f:
        reader = csv.reader(f)
        your_list = list(reader)
    return your_list


def total_births(year):
    """

    :param year: an integer, between 1880 and 2010
    :return: an integer, the total births of all the babies in that year
    """
    names = process_file('babynames/yob'+str(year)+'.txt')
    total = 0
    for name in names:
        total += float(name[2])
    return total



def proportion(name, gender, year):
    """

    :param name: a string, first name
    :param gender: a string, "F" or "M"
    :param year: an integer, between 1880 and 2010
    :return: a floating number, the proportion of babies with the given name to total births in given year
    """
    names = process_file('babynames/yob'+str(year)+'.txt')
    births = 0
    totalbirths = total_births(year)
    for listname in names:
        if listname[0] == name and listname[1] == gender:
            births = float(listname[2])
    return births/totalbirths

def highest_year(name, gender):
    """

    :param name: a string
    :param gender: a string, "F" or "M"
    :return: an integer, the year when the given name has the highest proportion over the years (among all the proportions of the same name in different years)
    """
    years = list(range(1880, 2011))
    high_year = 0
    highest_proportion = 0
    for year in years:
        if proportion(name, gender, year) > highest_proportion:
            high_year = year
            highest_proportion = proportion(name, gender, year)
    return high_year

def main():
    # print(process_file('babynames\yob1880.txt'))
    print(proportion('Sarah', 'F', 1981))
    print(highest_year('Sarah', 'F'))
    print(highest_year('Matthew', 'M'))
    # print(highest_year('Sarah', 'F'))


if __name__ == '__main__':
    main()
