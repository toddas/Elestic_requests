import time
import requests
import json
import csv


# kintamieji



# elastiko requestu

custurl = "http://xxx.xxx.xxx:11000/subscription/agent/"


# funkc

def getcustid(agentid):




    rekvestas = requests.get(custurl+agentid)
    rekvestas1 = rekvestas.text
    custid = json.loads(rekvestas1)



    return custid['customerId']



def main():
    i = 0

    with open("lifetime.csv") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        agentids = []
        serials = []
        for row in readCSV:
            agentid = row[0]
            serial = row[1]

            agentids.append(agentid)
            serials.append(serial)


        for agent in agentids:

            i += 1
            custid = getcustid(agent)
            cus = str(custid)
            header = {'Content-Type': "application/json", 'Accept': 'application/json'}
            agentid = str(agent)
            serials[i] = str(serials[i])





            payload = "{\"custumerId\":\""+cus+"\",\n\"agentId\":\""+agentid+"\",\n\"lifetime\":\"true\",\n\"serial\":\""+serials[i]+"\"}"

            custurl = "http://1xxx.xxx.xxx:11000/manage/agent/"+agentid+"/activation"
            rekvestas = requests.request("POST", custurl, data=payload, headers=header)

            print(rekvestas)
            print(agentid)
            time.sleep(0.3)

time.sleep(5)


if __name__ == '__main__':
    main()




