# MTGFinance

## Introduction

This program takes as input a CSV file, with basic comma separation, reads it, and then creates new lists or dictionaries based on the file that simplify the data. It can also write these new lists and dictionaries to a new CSV file.

The point of the program is to take a large CSV file produced by excel and both extract useful data from it and reduce its complexity by filtering out irrelevant entities and collapsing others into single measures. The CSV file it takes as input is included in the git. Most cards in the CSV file have multiple rows associated with them, and one of the functions of the program is to collapse these into a single row and add up the relevant values, creating dictionaries where the key is the card name and the value is either the desired value (e.g. current position, total profit so far, number of copies in inventory), or a list of these values.

## Future plans

In the future, the program will be able to parse a .DEK file produced by the Magic Online client and reconcile it with the inventory in the CSV file, updating the CSV file to reflect the values found in the .DEK file.

The program will also add in other information about the cards, such as their rarity, so as to perform data analyses across multiple dimensions.

## Known issues

The current output of some of the functions returns as strings rather than lists.
