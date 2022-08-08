from open_v2g_structs import *
import ctypes

class OpenV2GUtils:
    def writeStringToEXIString(string: str, exiString: (exi_string_character_t*100)):
        for i in range(len(string)):
            exiString[i] = exi_string_character_t(ord(string[i]))

        return len(string)

    def EXIStringToASCIIString(string: (exi_string_character_t*100), len: int):
        ascii_str = ""
        for i in range(len):
            ascii_str += f"{chr(string[i])}"

        return ascii_str

    def convert_to_array_type_bytes(val: int, size=dinSessionSetupReqType_EVCCID_BYTES_SIZE):
        # val is 8 bytes
        mask = 0xFF
        i = 0
        byte_array = []
        while i < size:
            byte_array.insert(0, (val & mask) >> 8*i)
            i += 1
            mask = mask << 8

        BYTES = (ctypes.c_uint8*size)(*byte_array)

        return BYTES

    def convert_to_array_type_characters(val: str, size=dinParameterType_Name_CHARACTERS_SIZE):
        array = []
        for i in range(len(val)):
            array.append(ord(val[i]))

        CHARACTERS = (exi_string_character_t*size)(*array)

        return CHARACTERS


    def convert_to_array_type_bytes_str(val: str, size=dinParameterType_Name_CHARACTERS_SIZE):
        array = []
        for i in range(len(val)):
            array.append(ord(val[i]))

        BYTES = (ctypes.c_uint8*size)(*array)

        return BYTES


    def convert_array_type_bytes_to_int(val: list[int]):
        value = 0

        for i in range(len(val)):
            value |= (val[i] << 8*(len(val)-i-1))

        return value


    def convert_array_type_characters_to_str(val: list[int]):
        str = ""

        for i in range(len(val)):
            if val[i] != 0:
                str += chr(val[i])

        return str