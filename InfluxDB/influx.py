from influxdb import InfluxDBClient
import influxdb_client
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
# result = client.query('SELECT * FROM "TimeDataProject"."autogen"."data1"')
# result.raw
# get_result = results.get_points(fiels:)
write_api = client.write_api(write_options=SYNCHRONOUS)

# p = influxdb_client.Point("data1").field("temperature", 28)
# data_points = [
#     {"measurement":"data1","fields":{"temperature":29}},
#     {"measurement":"data1","fields":{"temperature":30}},
#     {"measurement":"data1","fields":{"temperature":45}},
#     {"measurement":"data1","fields":{"temperature":40}},
#     {"measurement":"data1","fields":{"temperature":74}},
#     {"measurement":"data1","fields":{"temperature":56}},
#     {"measurement":"data1","fields":{"temperature":89}},
#     {"measurement":"data1","fields":{"temperature":100}},
#     {"measurement":"data1","fields":{"temperature":39}},
#     {"measurement":"data1","fields":{"temperature":73}},
#     {"measurement":"data1","fields":{"temperature":12}},
#     {"measurement":"data1","fields":{"temperature":100}}
# ]

# for point in data_points:
#     write_api.write(bucket=bucket, org=org, record=point)


# write_api.write(bucket=bucket, org=org, record=data_points)
query_api = client.query_api()
# query = 'SELECT * FROM "TimeDataProject"."autogen"."data1"'

query = f'from(bucket: "{bucket}") \
    |> range(start: -1h) \
    |> filter(fn: (r) => r._measurement == "data1" and r._field == "temperature")'

# from(bucket: "TimeDataProject")
#   |> range(start: v.timeRangeStart)
#   |> filter(fn: (r) => r._measurement == "data1" and r._field == "temperature")

result = query_api.query(org=org, query=query)
for table in result:
    for row in table.records:
        time=row.get_time()
        temperature =row.values["_value"]
        print(f'Time: {time}, temperature: {temperature}')
print("connection done!")