import csv
import xml.etree.ElementTree as ET

def read_excel_csv_file(file_name):
    """
    Given a CSV file, this reads the data into a nested list
    Args : a string corresponding to comma-separated CSV file
    Returns : a nested list consisting of the fields in the CSV file. Empty strings are set to 0, and irrelevant lines are deleted.
    """
    csv_table = []
    with open(file_name, newline='') as csv_file:       
        csv_reader = csv.reader(csv_file, delimiter=',')
        count = 0
        for row in csv_reader:
            if count == 1:
                count += 1
            else:
                count += 1
            csv_table.append(row)
    for item in csv_table:
        for index in range(len(item)):
            if item[index] == "":
                item[index] = 0
    del csv_table[0]
    del csv_table[len(csv_table) - 8:]
    return csv_table

def write_csv_file(csv_table, file_name):
    """
    Given a nested list (csv_table), this writes a CSV file
    Args : a nested list and string file name
    Returns : csv file with file_name as name
    """
    with open(file_name, 'w', newline = '') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter = ',', quoting = csv.QUOTE_MINIMAL)
        for line in csv_table:
            spamwriter.writerow(line)

def write_csv_dict(csv_dict, file_name):
    with open(file_name, 'w', newline = '') as csvfile:
        spamwriter = csv.writer(csvfile, delimiter = ',', quoting = csv.QUOTE_MINIMAL)
        spamwriter.writerows(csv_dict.items())

def read_dek_xml_file(file_name):
    """
    This function will read a .dek xml file into a nested list
    Args : a string corresponding to the DEK file
    Returns : a nested list
    """
    pass

def reconcile_files(excel, dek):
    """
    This function will update the CSV Excel file with the data from the DEK file
    Input: a string corresponding to a CSV file and a DEK file
    Returns : an updated CSV file
    """
    pass

def position_dict(table):
    """
    This creates a dictionary where the keys are cards and the values are my current position in them in dollars
    Args : a list of lists where each list is row in the csv file, corresponding to a card bought at a specific price point
    Returns : a dictionary where the keys are the names of cards and the values are the total amount currently invested in them
    """
    current_position = {}
    for item in table:
        if item[0] not in current_position:
            current_position[item[0]] = float(item[5])     
        else:
            current_position[item[0]] += float(item[5])
    for item in current_position:
        current_position[item] = round(current_position[item], 2)
    return current_position

def count_dict(table):
    """
    This creates a dictionary where the keys are cards and the values are the number of copies left
    Args : a list of lists where each list is row in the csv file, corresponding to a card bought at a specific price point
    Returns : a dictionary where the keys are the names of cards and the values are the number of copies left
    """
    card_count = {}
    for item in table:
        if item[0] not in card_count:
            card_count[item[0]] = int(item[3])
        else:
            card_count[item[0]] += int(item[3])
    return card_count

def profit_dict(table):
    """
    This creates a dictionary where the keys are cards and the values are my total profit on the card
    Args : a list of lists where each list is row in the csv file, corresponding to a card bought at a specific price point
    Returns : a dictionary where the keys are the names of cards and the values are the total profits made from the card
    """
    total_profit = {}
    for item in table:
        if item[0] not in total_profit:
            # print(item[9])
            total_profit[item[0]] = float(float(item[9]) + float(item[14]) + float(item[19]) + float(item[24]) + float(item[29]))  
        else:
            total_profit[item[0]] += float(float(item[9]) + float(item[14]) + float(item[19]) + float(item[24]) + float(item[29]))
    for item in total_profit:
        total_profit[item] = round(total_profit[item], 2)
    return total_profit

def complete_dict(position_d, profit_d, count_d):
    """
    This function creates a dictionary where the keys are card names and the values are a list of the current position, current profit, and current count.
    Args : dictionary mapping name to position, dictionary mapping name to profit, dictionary mapping name to count.
    Returns : dictionary mapping name to [position, profit, count].
    """
    complete_d = {}
    for item in position_d:
        if item not in complete_d:
            complete_d[item] = [position_d[item]]
    for item in profit_d:
        if item not in complete_d:
            complete_d[item] = [0, profit_d[item]]
        else:
            complete_d[item].append(profit_d[item])
    for item in count_d:
        if item not in complete_d:
            complete_d[item] = [0, 0, count_d[item]]
        else:
            complete_d[item].append(count_d[item])
    return complete_d

# write_csv_dict(complete_dict(position_dict(read_excel_csv_file("MTGcsv.csv")), count_dict(read_excel_csv_file("MTGcsv.csv")), profit_dict(read_excel_csv_file("MTGcsv.csv"))), "MTGdict.csv")

def total_profits(file):
    """
    This returns the total profit from a csv file
    Args : csv file name as string
    Returns : total profit rounded to the nearest cent
    """
    total = 0
    card_table = read_excel_csv_file(file)
    profit = profit_dict(card_table)
    for item in profit:
        total += profit[item]
    total = round(total, 2)
    return total


def card_info(file):
    """
    This returns the current position and profit for a given card
    Args : csv file name as string and card name as string
    Returns : string with position, profit, and copies left for the named card
    """
    print("\n\nUsing " + file + " for data")
    card = input("\n\nWhat card would you like info for? \n\n")
    card_table = read_excel_csv_file(file)
    profit = profit_dict(card_table)
    position = position_dict(card_table)
    count = count_dict(card_table)
    return print("\nCurrent position for " + card + " = $" + str(position[card]) + ", profit so far = $" + str(profit[card]) + ", number of copies left = " + str(count[card]))

# MTG_file = read_excel_csv_file("MTGcsv.csv")

# write_csv_file(MTG_file, "MTGnew.csv")