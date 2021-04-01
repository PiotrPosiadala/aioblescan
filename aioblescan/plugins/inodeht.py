#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# def parse(packet):
#     peer = packet.retrieve("peer")
#     rssi = packet.retrieve("rssi")
#     svc_data = packet.retrieve("Service Data uuid")
#     adv_payload = packet.retrieve("Adv Payload")
#     if peer and rssi and svc_data and adv_payload:
#         mac = peer[0].val
#         uuid = svc_data[0].val
#         if b"\x18\x1a" == uuid:
#             mac_in_payload = ":".join("%02x" % x for x in adv_payload[0].val[:6])
#             if mac == mac_in_payload:
#                 return parse_payload(mac, rssi[0].val, adv_payload[0].val)

class iNodeHT(object):
    """Class defining the content of an iNodeHT sensor advertisement."""

    def decode(self, packet):
        # Look for iNodeHT sensor custom firmware advertisements
        result = parse(packet)
        return result
