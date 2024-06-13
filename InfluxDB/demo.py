import influxdb_client
import random
import time
from influxdb_client.client.write_api import SYNCHRONOUS
bucket = 'TimeDataProject'
org = 'TECHstile'
token = "xSZb3jJZP8oHNsEjUKLOLNhEveJiNDfqkmhLuDgBTD6b2_XpWNvWX8QFzjz5P91BNiIyWEJf7QFGgj7-Cam4RQ=="
url = "http://localhost:8086"

client = influxdb_client.InfluxDBClient(
    url=url,
    token=token,
    org=org
)

print("connection Done!")

def writeData():
    write_api = client.write_api(write_options=SYNCHRONOUS)
    userInput = int(input("Give Temp:"))
    c = influxdb_client.Point("data1").tag("measured_in","Celsius").field("temperature", userInput)

    f = influxdb_client.Point("data1").tag("measured_in","Fahrenheit").field("temperature", userInput)
    # for point in data_points: 
    write_api.write(bucket=bucket, org=org, record=c)
    write_api.write(bucket=bucket, org=org, record=f)
    print('Data inserted Successfully')

def readData():
    query_api = client.query_api()
    query = f'from(bucket: "{bucket}") \
    |> range(start: -3h) \
    |> filter(fn: (r) => r._measurement == "data1" and r._field == "temperature")'
    result = query_api.query(org=org, query=query)
    # for table in result:
    #   for row in table.records:
    #     time=row.get_time()
    #     temperature =row.values["_value"]
    #     print(f'Time: {time}, temperature: {temperature}')
    keys = []
    values = []
    for table in result:
     for record in table.records:
        for key, value in record.values.items():
            keys.append(key)
            values.append(value)
    print("Keys:", keys)
    # print("Values:", values)
    
print('Select the query to perform')
print('1. Write Data')
print('2. Read Data')
choice = int(input('Write your Choice:'))

def randomData():
   for i in range(0,100000):
      data = int(random.uniform(5,100))
      write_api = client.write_api(write_options=SYNCHRONOUS)
      c = influxdb_client.Point("data1").tag("measured_in","Celsius").field("temperature", data)
      fahren = int((data*9)/5 + 32) 
      f = influxdb_client.Point("data1").tag("measured_in","Fahrenheit").field("temperature", fahren)
    # for point in data_points: 
      write_api.write(bucket=bucket, org=org, record=c)
      write_api.write(bucket=bucket, org=org, record=f)

      print("Inserted Successfully")
      time.sleep(1)

   print("data successs")

if choice ==1:
   writeData()
elif choice ==2:
   readData()
elif choice ==3:
   randomData()
else:
   print("Give correct input")