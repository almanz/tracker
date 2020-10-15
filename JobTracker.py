"""
This class should implement the requirements highlighted in the document linked in the wo package.
"""
import json
import uuid as id

class JobTracker:

    global d
    d = {}
    global col
    col = ["Company", "didApply", "Website", "Job Title", "appLink", "Resume", "Extras"]


    def addjob(self,lst):
        print("addjob:")
        print("lst size: ",len(lst))
        for elem in lst:
            dic = {}
            # print("size of elem",elem)
            counter = 0
            for el in elem:
                # print("el in elem:",el)
                dic[col[counter]] = el
                counter += 1
            # print("dic is: ",dic)
            d[str(id.uuid1())] = dic
            # print("d is: ",d)

    # def lookup(self,param):
    #     return 0

    def to_file(self):
        with open('data.txt', 'w+') as outfile:
            json.dump(d, outfile)

