#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from struct import unpack
import aioblescan as aios

INODEHT = 39824
INODEHT2 = 155


class iNodeHT(object):
    """
    Class defining the content of a iNode HT sensor advertisement
    """

    def __init__(self):
        self.f = open("inodeht.log", "a")

    def decode(self, packet):
        data = {}
        raw_data = packet.retrieve("Manufacturer Specific Data")
        # if raw_data:
        #     self.f.write("{}\n".format(str(raw_data[0].payload[0].val)))
        try:
            raw_data = raw_data[0].payload
            if raw_data:
                mfg_id = raw_data[0].val
                if mfg_id == INODEHT:
                    pckt = raw_data[1].val
                    self.f.write("{}\n".format(str(pckt)))
                    # data["model"] = unpack("<B", pckt[0:1])[0]
                    # data["batt_lvl"] = unpack("<B", pckt[1:2])[0]
                    # data["logging"] = unpack(">H", pckt[2:4])[0]
                    # data["interval"] = unpack(">H", pckt[4:6])[0]
                    data["temperature"] = ((unpack("<h", pckt[6:8])[0] * 175.72 * 4) / 65536 ) - 46.85
                    data["humidity"] = ((unpack("<h", pckt[8:10])[0] * 125 * 4) /65536) - 6
                    # data["pressure"] = unpack(">h", pckt[10:12])[0] / 10
        except:
            pass
        return data
        



    # def decode(self, packet):
    #     data = {}
    #     raw_data = packet.retrieve("Manufacturer Specific Data")
    #     # if raw_data:
    #     #     self.f.write("{}\n".format(str(raw_data[0].payload[0].val)))
    #     try:
    #         raw_data = raw_data[0].payload
    #         if raw_data:
    #             mfg_id = raw_data[0].val
    #             if mfg_id == INODEHT:
    #                 pckt = raw_data[1].val
    #                 self.f.write("{}\n".format(str(pckt)))
    #                 # data["version"] = unpack("<B", pckt[0:1])[0]
    #                 # data["batt_lvl"] = unpack("<B", pckt[1:2])[0]
    #                 # data["logging"] = unpack(">H", pckt[2:4])[0]
    #                 # data["interval"] = unpack(">H", pckt[4:6])[0]
    #                 data["temperature"] = ((unpack("<h", pckt[6:8])[0] * 175.72 * 4) / 65536 ) - 46.85
    #                 data["humidity"] = ((unpack("<h", pckt[8:10])[0] * 125 * 4) /65536) - 6
    #                 # data["pressure"] = unpack(">h", pckt[10:12])[0] / 10
    #     except:
    #         pass
    #     return data
        