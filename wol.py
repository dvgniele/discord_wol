import socket

def create_magic_packet(macaddress: str):
    if len(macaddress) == 17:
        sep = macaddress[2]
        macaddress = macaddress.replace(sep, "")
    elif len(macaddress) != 12:
        raise ValueError("Incorrect MAC address format")
    payload = "F" * 12 + macaddress * 16
    payload = bytes.fromhex(payload)
    return payload


def send_magik_packet(mac, ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            packet = create_magic_packet(mac)
            if len(packet) != 102:
                raise ValueError(
                    "Packet Byte Length Must be 102, instead, got {}".format(len(packet)))
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
            sock.sendto(packet, (ip, port))
    except socket.gaierror as e:
        print(e)
        print("Conection failed")
        return f"{e}\nConnection failed."
    except ValueError as e:
        print(e)
        return f"{e}"
    print("Sent magic packet.")
    return f"Sent magic packet!"
