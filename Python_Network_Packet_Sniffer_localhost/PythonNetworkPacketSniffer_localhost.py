import socket
import struct

#unpack ethernet frame
def ethernet_frame(data):
    dest_mac, src_mac, proto = struct.unpack('! 6s 6s H', data[:14])
    return get_mac_addr(dest_mac), get_mac_addr(src_mac), socket.htons(proto), data[14:]

#return properly formatted MAC address
def get_mac_addr(bytes_addr):
    bytes_str = map('{:02x}'.format, bytes_addr)
    return ':'.join(bytes_str).upper()

#unpacks IPv4 Packet
def ipv4_packet(data):
    version_header_length = data[0]
    version = version_header_length >> 4
    header_length = (version_header_length & 15) * 4
    ttl, proto, src, target = struct.unpack('! 8x B B 2x 4s 4s', data[:20])
    return version, header_length, ttl, proto, ipv4(src), ipv4(target), data[header_length:]

#return properly formatted IPv4 address
def ipv4(addr):
    return '.'.join(map(str, addr))

#unpack ICMP packet
def icmp_packet(data):
    icmp_type, code, checksum = struct.unpack('! B B H', data[:4])
    return icmp_type, code, checksum, data[4:]

#unpack TCP packet
def tcp_packet(data):
    (src_port, dest_port, sequence, acknowledgement, offset_reserved_flags) = struct.unpack('! H H L L H', data[:14])
    offset = (offset_reserved_flags >> 12) * 4
    flag_urg = (offset_reserved_flags & 32) >> 5
    flag_ack = (offset_reserved_flags & 16) >> 4
    flag_psh = (offset_reserved_flags & 8) >> 3
    flag_rst = (offset_reserved_flags & 4) >> 2
    flag_syn = (offset_reserved_flags & 2) >> 1
    flag_fin = offset_reserved_flags & 1
    return src_port, dest_port, sequence, acknowledgement, flag_urg, flag_ack, flag_psh, flag_rst, flag_syn, flag_fin, data[offset:]

#unpack UDP packet
def udp_packet(data):
    src_port, dest_port, length = struct.unpack('! H H 2x H', data[:8])
    return src_port , dest_port, length, data[8:]
    
def main():

    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    counter_packets = {'icmp':0, 'tcp':0, 'udp':0, 'other':0}
    counter_bytes = {'icmp':0, 'tcp':0, 'udp':0, 'other':0}

    try:
        while True:
            raw_data, addr = conn.recvfrom(65536)
            dest_mac, src_mac, eth_proto, data = ethernet_frame(raw_data)
            packet_length = len(raw_data)

            if eth_proto == 8: #ipv4
                (version, header_length, ttl, proto, src, target, data) = ipv4_packet(data)
                if src == '127.0.0.1' or target == '127.0.0.1':
                    print('IPv4 Packet: ')
                    print('Version: {}, Header Length: {}, TTL: {}'.format(version, header_length, ttl))
                    print('Protocol: {}, Source: {}, Target: {}'.format(proto, src, target))

                    if proto == 1: #icmp
                        icmp_type, code, checksum, data = icmp_packet(data)
                        print('ICMP Packet: ')
                        print('Type: {}, Code: {}, Checksum: {}'.format(icmp_type, code, checksum))
                        print('Data: {}'.format(data))
                        counter_packets['icmp'] += 1
                        counter_bytes['icmp'] += packet_length
                
                    elif proto == 6: #tcp
                        src_port, dest_port, sequence, acknowledgement, flag_urg, flag_ack, flag_psh, flag_rst, flag_syn, flag_fin, data = tcp_packet(data)     
                        print('TCP Packet: ')
                        print('Source port: {}, Destination Port: {}'.format(src_port, dest_port))
                        print('Sequence: {}, Acknoledgement: {}'.format(sequence, acknowledgement))
                        print('Flags: ')
                        print('URG: {}, ACK: {}, PSH: {}, RST: {}, SYN: {}, FIN {}'.format(flag_urg, flag_ack, flag_psh, flag_rst, flag_syn, flag_fin))
                        print('Data: {}'.format(data))
                        counter_packets['tcp'] += 1
                        counter_bytes['tcp'] += packet_length

                    elif proto == 17: #udp
                        src_port , dest_port, length, data = udp_packet(data)
                        print('UDP Packet: ')
                        print('Source port: {}, Destination Port: {}, Length: {}'.format(src_port, dest_port, length))
                        print('Data: {}'.format(data))
                        counter_packets['udp'] += 1
                        counter_bytes['udp'] += packet_length

                    else: #other
                        print('Data: {}'.format(data))
                        counter_packets['other'] += 1
                        counter_bytes['other'] += packet_length

    except KeyboardInterrupt:
        print(f'\n\nPackets Count: {counter_packets}')
        print(f'Bytes Count: {counter_bytes}')
    finally:
        print('\n\nFinish!')

main()