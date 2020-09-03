import csv


def CSVtoLIST(file):
    dataList = []
    with open(file, newline='') as dataFile:
        csvReader = csv.reader(dataFile)
        next(csvReader, None)
        for line in csvReader:
            if line[0] == 'NA' or line[1] == 'NA':
                continue
            else:
                tempList = []
                tempList.insert(len(tempList), float(line[0]))
                tempList.insert(len(tempList), float(line[1]))
                tempList.insert(len(tempList), line[2])
                tempList.insert(len(tempList), line[3])
                tempList.insert(len(tempList), line[4])
                dataList.insert(len(dataList), tempList)
    return dataList


def priceData(file):
    listWithPrices = []
    with open(file, newline='') as dataFile:
        csvReader = csv.reader(dataFile)
        next(csvReader, None)
        for line in csvReader:
            if line[0] == 'NA' or line[1] == 'NA':
                continue
            else:
                tempList = []
                tempList.insert(len(tempList), float(line[0]))
                tempList.insert(len(tempList), float(line[1]))
                if line[2] == 'NA':
                    tempList.insert(len(tempList), float(-1))
                tempList.insert(len(tempList), line[3])
                tempList.insert(len(tempList), line[4])
                listWithPrices.insert(len(listWithPrices), tempList)
    return listWithPrices



