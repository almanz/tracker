"""
This class should implement the requirements highlighted in the document linked in the wo package.
"""
import json
# import lib for: json-->csv
class JobTracker:

    global d
    d = {}
    global id
    id = 0
    global rubrik
    rubrik = ["Company","didApply","Website","Job Title","appLink","Resume","Extras"]

    # def __init__(self,):
    #     d = dict()

    def addjob(self,lst):
        dict = {}
        id = 0
        for elem in lst:
            dict[rubrik[id]] = elem
            id += 1
        d["first"] = dict

    def lookup(self,param):
        return 0

    def export_to_csv(self):
        json.dump(d)
        return 0

    def to_json(self):
        with open('data.txt', 'w') as outfile:
            json.dump(d, outfile)

