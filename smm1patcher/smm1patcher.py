import sys, struct, binascii
from binascii import hexlify, unhexlify

def float_to_hex(f):
    return hex(struct.unpack('<I', struct.pack('<f', f))[0])

main_binary = sys.argv[1]

def change_animation_speed(speed_float):
    global main
    with open(main_binary,'rb') as smm1binary:
            smm1data = smm1binary.read()
            smm1data = bytearray(smm1data)
            speed_float = hex(struct.unpack('<I', struct.pack('<f', speed_float))[0])
            speed_float = bytes.fromhex(str(speed_float).replace("0x",""))
            smm1data[0x8300:0x8304] = speed_float
            with open(main_binary,'wb') as smm1binary:
                smm1binary.write(smm1data)
                print('Successfully Patched ' + str(speed_float) + ' to 0x8300!')

def change_play_mode_entity_sizes(size_float):
    global main
    with open(main_binary,'rb') as smm1binary:
            smm1data = smm1binary.read()
            smm1data = bytearray(smm1data)
            size_float = hex(struct.unpack('<I', struct.pack('<f', size_float))[0])
            size_float = bytes.fromhex(str(size_float).replace("0x",""))
            smm1data[0xFBCC:0x0FBD0] = size_float
            with open(main_binary,'wb') as smm1binary:
                smm1binary.write(smm1data)
                print('Successfully Patched ' + str(size_float) + ' to 0xFBCC!')

def change_reset_rocket_speed(speed_float):
    global main
    with open(main_binary,'rb') as smm1binary:
            smm1data = smm1binary.read()
            smm1data = bytearray(smm1data)
            speed_float = hex(struct.unpack('<I', struct.pack('<f', speed_float))[0])
            speed_float = bytes.fromhex(str(speed_float).replace("0x",""))
            smm1data[0x77B8:0x77BC] = speed_float
            with open(main_binary,'wb') as smm1binary:
                smm1binary.write(smm1data)
                print('Successfully Patched ' + str(speed_float) + ' to 0x77B8!')

def change_course_height(course_height):
    global main
    with open(main_binary,'rb') as smm1binary:
            smm1data = smm1binary.read()
            smm1data = bytearray(smm1data)
            course_height = hex(struct.unpack('<I', struct.pack('<f', course_height))[0])
            course_height = bytes.fromhex(str(course_height).replace("0x",""))
            smm1data[0x20A80:0x20A84] = course_height
            with open(main_binary,'wb') as smm1binary:
                smm1binary.write(smm1data)
                print('Successfully Patched ' + str(course_height) + ' to 0x20A80!')

def change_camera_zoom(camera_zoom):
    global main
    with open(main_binary,'rb') as smm1binary:
            smm1data = smm1binary.read()
            smm1data = bytearray(smm1data)
            camera_zoom = hex(struct.unpack('<I', struct.pack('<f', camera_zoom))[0])
            camera_zoom = bytes.fromhex(str(camera_zoom).replace("0x",""))
            smm1data[0xDA974:0xDA978] = camera_zoom
            with open(main_binary,'wb') as smm1binary:
                smm1binary.write(smm1data)
                print('Successfully Patched ' + str(camera_zoom) + ' to 0xDA974!')
                with open(main_binary,'rb') as smm1binary:
                        smm1data = smm1binary.read()
                        smm1data = bytearray(smm1data)
                        smm1data[0x583830:0x583834] = b'\x7c\x03\x18\x00'
                        with open(main_binary,'wb') as smm1binary:
                            smm1binary.write(smm1data)
