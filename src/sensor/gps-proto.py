import serial
import datetime
import pynmea2
import pandas as pd
# import geopandas as gpd

def gps_retrieve():
    ser = serial.Serial("/dev/serial0", baudrate=9600)
    ser.flushInput()
    ser.flushOutput()
    idx = 0

    nmea_data = b""

    # skip first line, since it could be incomplete
    ser.readline()

    while True:
        idx += 1
        nmea_sentence = ser.readline()
        nmea_data += nmea_sentence

        # if idx % 100 == 0:
        #     # print(f"idx: {idx}")
        #     # print(nmea_data)
            
        if idx % 100 == 0:

            # save to file after 2000 sentences added
            # filename = datetime.datetime.utcnow().strftime("./src/data/gps_data_%Y%m%d-%H%M%S.nmea")
            # f = open(filename, "ab")
            # f.write(nmea_data)
            # print(nmea_data)
            # f.close()
            
            nmea_data = b""
            gps_reader(nmea_data)




def gps_reader(nmea_data):
    # nmea_data = open("./src/data/gps_data_20220913-041532.nmea", "rb")

    coordinates_data = []
    err = False
    # for message_bytes in nmea_data.readlines():    
    try:
        message = nmea_data.decode("utf-8").replace("\n", "").replace("\r", "")
        parsed_message = pynmea2.parse(message)
    except:
        # skip invalid sentences
        # continue
        err = True

    cga_data = {}
    if(err == False):
        # process only GGA messages
        if parsed_message.sentence_type == "GGA":
            for attr in ["timestamp", "latitude", "longitude", "latitude", "horizontal_dil", "num_sats", "gps_qual"]:
                cga_data[attr] = getattr(parsed_message, attr)
            coordinates_data.append(cga_data)
            print(cga_data)
                
        # coordinates_data[0]

        # df = pd.DataFrame(coordinates_data)
        # gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.longitude, df.latitude, crs="EPSG:4326"))
        print(df)

def main():
    gps_retrieve()

if __name__ == "__main__":
    main()