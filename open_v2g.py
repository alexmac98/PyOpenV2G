import ctypes
from ctypes import *
import pathlib
from open_v2g_structs import *
from open_v2g_constants import *

class OpenV2G:
    def __init__(self):
        self.libname = pathlib.Path().absolute() / "open_v2g/build/libopenv2g.so"
        self.libopenv2g = ctypes.CDLL(self.libname)
        self.libopenv2g.connect()
    
    # ---------- appHandshake ---------- #
    # open_v2g/source/appHandshake/appHandEXIDatatypes.h
    def init_appHandEXIDocument(self, exiDoc: appHandEXIDocument):
        return self.libopenv2g.init_appHandEXIDocument(ctypes.byref(exiDoc))

    def init_appHandAppProtocolType(self, appHandAppProtocolType: appHandAppProtocolType):
        return self.libopenv2g.init_appHandAppProtocolType(ctypes.byref(appHandAppProtocolType))

    def init_appHandAnonType_supportedAppProtocolReq(self, appHandAnonType_supportedAppProtocolReq: appHandAnonType_supportedAppProtocolReq):
        return self.libopenv2g.init_appHandAnonType_supportedAppProtocolReq(ctypes.byref(appHandAnonType_supportedAppProtocolReq))

    def init_appHandAnonType_supportedAppProtocolRes(self, appHandAnonType_supportedAppProtocolRes: appHandAnonType_supportedAppProtocolRes):
        return self.libopenv2g.init_appHandAnonType_supportedAppProtocolRes(ctypes.byref(appHandAnonType_supportedAppProtocolRes))


    # open_v2g/source/appHandshake/appHandEXIDatatypesDecoder.h
    def decode_appHandExiDocument(self, stream: bitstream_t, exiDoc: appHandEXIDocument):
        return self.libopenv2g.decode_appHandExiDocument(ctypes.byref(stream), ctypes.byref(exiDoc))
    

    # open_v2g/source/appHandshake/appHandEXIDatatypesEncoder.h
    def encode_appHandExiDocument(self, stream: bitstream_t, exiDoc: appHandEXIDocument):
        return self.libopenv2g.encode_appHandExiDocument(ctypes.pointer(stream), ctypes.pointer(exiDoc))
    

    # ---------- codec ---------- #
    # open_v2g/source/codec/BitInputStream.h
    def readBits(self, stream: bitstream_t, num_bits: c_size_t, b: c_uint32):
        return self.libopenv2g.readBits(ctypes.pointer(stream), num_bits, ctypes.pointer(b))

    # open_v2g/source/codec/BitOutputStream.h
    def writeBits(self, stream: bitstream_t, nbits: c_size_t, bits: c_uint32):
        return self.libopenv2g.writeBits(ctypes.point(stream), nbits, bits)

    def flush(self, stream: bitstream_t):
        return self.libopenv2g.flush(ctypes.pointer(stream))
    
    # open_v2g/source/codec/ByteStream.h
    def readBytesFromFile(self, filename: c_char_p, data: c_uint8, size: c_size_t, pos: c_size_t):
        return self.libopenv2g.readBytesFromFile(ctypes.pointer(filename), ctypes.pointer(data), size, ctypes.pointer(pos))

    def writeBytesToFile(self, data: c_uint8, len: c_size_t, filename: c_char_p):
        return self.libopenv2g.writeBytesToFile(ctypes.pointer(data), len, filename)

    # open_v2g/source/codec/DecoderChannel.h
    def decode(self, stream: bitstream_t, b: c_uint8):
        return self.libopenv2g.decode(ctypes.pointer(stream), ctypes.pointer(b))

    def decodeBoolean(self, stream: bitstream_t, b: int):
        return self.libopenv2g.decodeBoolean(ctypes.pointer(stream), ctypes.pointer(b))

    def decodeNBitUnsignedInteger(self, stream: bitstream_t, bits: c_size_t, uint32: c_uint32):
        return self.libopenv2g.decodeNBitUnsignedInteger(ctypes.pointer(stream), bits, ctypes.pointer(uint32))

    def decodeUnsignedInteger(self, stream: bitstream_t, iv: exi_integer_t):
        return self.libopenv2g.decodeUnsignedInteger(ctypes.pointer(stream), ctypes.pointer(iv))

    def decodeUnsignedInteger16(self, stream: bitstream_t, uint16: c_uint16):
        return self.libopenv2g.decodeUnsignedInteger16(ctypes.pointer(stream), ctypes.pointer(uint16))

    def decodeUnsignedInteger32(self, stream: bitstream_t, uint32: c_uint32):
        return self.libopenv2g.decodeUnsignedInteger32(ctypes.pointer(stream), ctypes.pointer(uint32))

    def decodeUnsignedIntegerSizeT(self, stream: bitstream_t, sizeT: c_size_t):
        return self.libopenv2g.decodeUnsignedIntegerSizeT(ctypes.pointer(stream), ctypes.pointer(sizeT))

    def decodeUnsignedInteger64(self, stream: bitstream_t, uint64: c_uint64):
        return self.libopenv2g.decodeUnsignedInteger64(ctypes.pointer(stream), ctypes.pointer(uint64))

    def decodeInteger(self, stream: bitstream_t, iv: exi_integer_t):
        return self.libopenv2g.decodeInteger(ctypes.pointer(stream), ctypes.pointer(iv))

    def decodeInteger16(self, stream: bitstream_t, int16: c_int16):
        return self.libopenv2g.decodeInteger16(ctypes.pointer(stream), ctypes.pointer(int16))

    def decodeInteger32(self, stream: bitstream_t, int32: c_int32):
        return self.libopenv2g.decodeInteger32(ctypes.pointer(stream), ctypes.pointer(int32))

    def decodeInteger64(self, stream: bitstream_t, int64: c_int64):
        return self.libopenv2g.decodeInteger64(ctypes.pointer(stream), ctypes.pointer(int64))

    def decodeFloat(self, stream: bitstream_t, f: exi_float_me_t):
        return self.libopenv2g.decodeFloat(ctypes.pointer(stream), ctypes.pointer(f))

    def decodeDecimal(self, stream: bitstream_t, d: exi_decimal_t):
        return self.libopenv2g.decodeDecimal(ctypes.pointer(stream), ctypes.pointer(d))

    def decodeStringOnly(self, stream: bitstream_t, len: c_size_t, s: exi_string_t):
        return self.libopenv2g.decodeStringOnly(ctypes.pointer(stream), len,  ctypes.pointer(s))

    def decodeString(self, stream: bitstream_t, s: exi_string_t):
        return self.libopenv2g.decodeString(ctypes.pointer(stream), ctypes.pointer(s))

    def decodeStringValue(self, stream: bitstream_t, stringTable: exi_value_string_table_t, namespaceUriID: c_size_t, localNameID: c_size_t, s: exi_string_value_t):
        return self.libopenv2g.decodeStringValue(ctypes.pointer(stream), ctypes.pointer(stringTable), namespaceUriID, localNameID, ctypes.pointer(s))

    def decodeRCSStringValue(self, stream: bitstream_t, stringTable: exi_value_string_table_t, namespaceUriID: c_size_t, localNameID: c_size_t, rcs: exi_rcs_t, s: exi_string_value_t):
        return self.libopenv2g.decodeRCSStringValue(ctypes.pointer(stream), ctypes.pointer(stringTable), namespaceUriID, localNameID, ctypes.pointer(rcs), ctypes.pointer(s))

    def decodeCharacters(self, stream: bitstream_t, len: c_size_t, chars: exi_string_character_t, charsSize: c_size_t):
        return self.libopenv2g.decodeCharacters(ctypes.pointer(stream), len, ctypes.pointer(chars), charsSize)

    def decodeRCSCharacters(self, stream: bitstream_t, len: c_size_t, chars: exi_string_character_t, charsSize: c_size_t, rcsCodeLength: c_size_t, rcsSize: c_size_t,  rcsSet: list[exi_string_character_t]):
        return self.libopenv2g.decodeRCSCharacters(ctypes.pointer(stream), len, ctypes.pointer(chars), charsSize, rcsCodeLength, rcsSize, rcsSet)

    def decodeBinary(self, stream: bitstream_t, bytes: exi_bytes_t):
        return self.libopenv2g.decodeBinary(ctypes.pointer(stream), ctypes.pointer(bytes))

    def decodeBytes(self, stream: bitstream_t, len: c_size_t, data: c_uint8):
        return self.libopenv2g.decodeBytes(ctypes.pointer(stream), len, ctypes.pointer(data))

    def decodeDateTime(self, stream: bitstream_t, type: exi_datetime_type_t, datetime: exi_datetime_t):
        return self.libopenv2g.decodeDateTime(ctypes.pointer(stream), type, ctypes.pointer(datetime))


    # open_v2g/source/codec/EncoderChannel.h
    def encode(self, stream: bitstream_t, b: c_uint8):
        return self.libopenv2g.encode(ctypes.pointer(stream), b)

    def encodeBoolean(self, stream: bitstream_t, b: c_int):
        return self.libopenv2g.encodeBoolean(ctypes.pointer(stream), b)

    def encodeNBitUnsignedInteger(self, stream: bitstream_t, nbits: c_size_t, val: c_uint32):
        return self.libopenv2g.encodeNBitUnsignedInteger(ctypes.pointer(stream), nbits, val)

    def encodeUnsignedInteger(self, stream: bitstream_t, iv: exi_integer_t):
        return self.libopenv2g.encodeUnsignedInteger(ctypes.pointer(stream), ctypes.pointer(iv))

    def encodeUnsignedInteger16(self, stream: bitstream_t, n: c_uint16):
        return self.libopenv2g.encodeUnsignedInteger16(ctypes.pointer(stream), n)

    def encodeUnsignedInteger32(self, stream: bitstream_t, n: c_uint32):
        return self.libopenv2g.encodeUnsignedInteger32(ctypes.pointer(stream), n)

    def encodeUnsignedInteger64(self, stream: bitstream_t, n: c_uint64):
        return self.libopenv2g.encodeUnsignedInteger64(ctypes.pointer(stream), n)

    def encodeInteger(self, stream: bitstream_t, iv: exi_integer_t):
        return self.libopenv2g.encodeInteger(ctypes.pointer(stream), ctypes.pointer(iv))

    def encodeInteger16(self, stream: bitstream_t, n: c_int16):
        return self.libopenv2g.encodeInteger16(ctypes.pointer(stream), n)

    def encodeInteger32(self, stream: bitstream_t, n: c_int32):
        return self.libopenv2g.encodeInteger32(ctypes.pointer(stream), n)

    def encodeInteger64(self, stream: bitstream_t, n: c_int64):
        return self.libopenv2g.encodeInteger64(ctypes.pointer(stream), n)

    def encodeFloat(self, stream: bitstream_t, f: exi_float_me_t):
        return self.libopenv2g.encodeFloat(ctypes.pointer(stream), ctypes.pointer(f))

    def encodeDecimal(self, stream: bitstream_t, d: exi_decimal_t):
        return self.libopenv2g.encodeDecimal(ctypes.pointer(stream), ctypes.pointer(d))

    def encodeString(self, stream: bitstream_t, string: exi_string_t):
        return self.libopenv2g.encodeString(ctypes.pointer(stream), ctypes.pointer(string))

    def encodeStringValue(self, stream: bitstream_t, stringTable: exi_value_string_table_t, namespaceUriID: c_size_t, localNameID: c_size_t, string: exi_string_value_t):
        return self.libopenv2g.encodeStringValue(ctypes.pointer(stream), ctypes.pointer(stringTable), namespaceUriID, localNameID, ctypes.pointer(string))

    def encodeRCSStringValue(self, stream: bitstream_t, stringTable: exi_value_string_table_t, namespaceUriID: c_size_t, localNameID: c_size_t, rcs: exi_rcs_t, string: exi_string_value_t):
        return self.libopenv2g.encodeRCSStringValue(ctypes.pointer(stream), ctypes.pointer(stringTable), namespaceUriID, localNameID, ctypes.pointer(rcs), ctypes.pointer(string))

    def encodeCharacters(self, stream: bitstream_t, chars: exi_string_character_t, len: c_size_t):
        return self.libopenv2g.encodeCharacters(ctypes.pointer(stream), ctypes.pointer(chars), len)

    def encodeRCSCharacters(self, stream: bitstream_t, chars: exi_string_character_t, len: c_size_t, rcsCodeLength: c_size_t, rcsSize: c_size_t, rcsSet: list[exi_string_character_t]):
        return self.libopenv2g.encodeRCSCharacters(ctypes.pointer(stream), ctypes.pointer(chars), len, rcsCodeLength, rcsSize, ctypes.pointer(rcsSet))

    def encodeBinary(self, stream: bitstream_t, bytes: exi_bytes_t):
        return self.libopenv2g.encodeBinary(ctypes.pointer(stream), ctypes.pointer(bytes))

    def encodeBytes(self, stream: bitstream_t, data: c_uint8, len: c_size_t):
        return self.libopenv2g.encodeBytes(ctypes.pointer(stream), ctypes.pointer(data), len)

    def encodeDateTime(self, stream: bitstream_t, datetime: exi_datetime_t):
        return self.libopenv2g.encodeDateTime(ctypes.pointer(stream), ctypes.pointer(datetime))

    def encodeFinish(self, stream: bitstream_t):
        return self.libopenv2g.encodeFinish(ctypes.pointer(stream))

    # open_v2g/source/codec/EXIHeaderDecoder.h
    def readEXIHeader(self, stream: bitstream_t):
        return self.libopenv2g.readEXIHeader(ctypes.pointer(stream))

    # open_v2g/source/codec/EXIHeaderEncoder.h
    def writeEXIHeader(self, stream: bitstream_t):
        return self.libopenv2g.writeEXIHeader(ctypes.pointer(stream))

    # open_v2g/source/codec/MethodsBag.h
    def exiGetCodingLength(self, characteristics: c_size_t, codingLength: c_size_t):
        return self.libopenv2g.exiGetCodingLength(characteristics, ctypes.pointer(codingLength))

    def numberOf7BitBlocksToRepresent(self, n: c_uint32):
        return self.libopenv2g.numberOf7BitBlocksToRepresent(n)

    # ---------- din ---------- #
    # open_v2g/source/din/dinEXIDatatypes.h
    def init_dinEXIDocument(self, exiDoc: dinEXIDocument):
        return self.libopenv2g.init_dinEXIDocument(ctypes.byref(exiDoc))

    def init_dinEXIFragment(self, exiFrag: dinEXIFragment):
        return self.libopenv2g.init_dinEXIFragment(ctypes.pointer(exiFrag))

    def init_dinMeteringReceiptReqType(self, dinMeteringReceiptReqType: dinMeteringReceiptReqType):
        return self.libopenv2g.init_dinMeteringReceiptReqType(ctypes.pointer(dinMeteringReceiptReqType))

    def init_dinBodyType(self, dinBodyType: dinBodyType):
        return self.libopenv2g.init_dinBodyType(ctypes.pointer(dinBodyType))

    def init_dinSessionSetupReqType(self, dinSessionSetupReqType: dinSessionSetupReqType):
        return self.libopenv2g.init_dinSessionSetupReqType(ctypes.pointer(dinSessionSetupReqType))

    def init_dinPowerDeliveryResType(self, dinPowerDeliveryResType: dinPowerDeliveryResType):
        return self.libopenv2g.init_dinPowerDeliveryResType(ctypes.byref(dinPowerDeliveryResType))

    def init_dinServiceDetailResType(self, dinServiceDetailResType: dinServiceDetailResType):
        return self.libopenv2g.init_dinServiceDetailResType(ctypes.byref(dinServiceDetailResType))

    def init_dinWeldingDetectionResType(self, dinWeldingDetectionResType: dinWeldingDetectionResType):
        return self.libopenv2g.init_dinWeldingDetectionResType(ctypes.pointer(dinWeldingDetectionResType))

    def init_dinContractAuthenticationResType(self, dinContractAuthenticationResType: dinContractAuthenticationResType):
        return self.libopenv2g.init_dinContractAuthenticationResType(ctypes.pointer(dinContractAuthenticationResType))

    def init_dinCanonicalizationMethodType(self, dinCanonicalizationMethodType: dinCanonicalizationMethodType):
        return self.libopenv2g.init_dinCanonicalizationMethodType(ctypes.pointer(dinCanonicalizationMethodType))

    def init_dinSPKIDataType(self, dinSPKIDataType: dinSPKIDataType):
        return self.libopenv2g.init_dinSPKIDataType(ctypes.pointer(dinSPKIDataType))

    def init_dinListOfRootCertificateIDsType(self, dinListOfRootCertificateIDsType: dinListOfRootCertificateIDsType):
        return self.libopenv2g.init_dinListOfRootCertificateIDsType(ctypes.pointer(dinListOfRootCertificateIDsType))

    def init_dinSelectedServiceListType(self, dinSelectedServiceListType: dinSelectedServiceListType):
        return self.libopenv2g.init_dinSelectedServiceListType(ctypes.pointer(dinSelectedServiceListType))

    def init_dinCurrentDemandResType(self, dinCurrentDemandResType: dinCurrentDemandResType):
        return self.libopenv2g.init_dinCurrentDemandResType(ctypes.pointer(dinCurrentDemandResType))

    def init_dinTransformType(self, dinTransformType: dinTransformType):
        return self.libopenv2g.init_dinTransformType(ctypes.pointer(dinTransformType))

    def init_dinAC_EVChargeParameterType(self, dinAC_EVChargeParameterType: dinAC_EVChargeParameterType):
        return self.libopenv2g.init_dinAC_EVChargeParameterType(ctypes.pointer(dinAC_EVChargeParameterType))

    def init_dinX509DataType(self, dinX509DataType: dinX509DataType):
        return self.libopenv2g.init_dinX509DataType(ctypes.pointer(dinX509DataType))

    def init_dinChargingStatusResType(self, dinChargingStatusResType: dinChargingStatusResType):
        return self.libopenv2g.init_dinChargingStatusResType(ctypes.pointer(dinChargingStatusResType))

    def init_dinWeldingDetectionReqType(self, dinWeldingDetectionReqType: dinWeldingDetectionReqType):
        return self.libopenv2g.init_dinWeldingDetectionReqType(ctypes.pointer(dinWeldingDetectionReqType))

    def init_dinSignaturePropertiesType(self, dinSignaturePropertiesType: dinSignaturePropertiesType):
        return self.libopenv2g.init_dinSignaturePropertiesType(ctypes.pointer(dinSignaturePropertiesType))

    def init_dinContractAuthenticationReqType(self, dinContractAuthenticationReqType: dinContractAuthenticationReqType):
        return self.libopenv2g.init_dinContractAuthenticationReqType(ctypes.pointer(dinContractAuthenticationReqType))

    def init_dinDC_EVPowerDeliveryParameterType(self, dinDC_EVPowerDeliveryParameterType: dinDC_EVPowerDeliveryParameterType):
        return self.libopenv2g.init_dinDC_EVPowerDeliveryParameterType(ctypes.pointer(dinDC_EVPowerDeliveryParameterType))

    def init_dinEVSEChargeParameterType(self, dinEVSEChargeParameterType: dinEVSEChargeParameterType):
        return self.libopenv2g.init_dinEVSEChargeParameterType(ctypes.pointer(dinEVSEChargeParameterType))

    def init_dinCableCheckReqType(self, dinCableCheckReqType: dinCableCheckReqType):
        return self.libopenv2g.init_dinCableCheckReqType(ctypes.pointer(dinCableCheckReqType))

    def init_dinDC_EVChargeParameterType(self, dinDC_EVChargeParameterType: dinDC_EVChargeParameterType):
        return self.libopenv2g.init_dinDC_EVChargeParameterType(ctypes.pointer(dinDC_EVChargeParameterType))

    def init_dinSAScheduleListType(self, dinSAScheduleListType: dinSAScheduleListType):
        return self.libopenv2g.init_dinSAScheduleListType(ctypes.pointer(dinSAScheduleListType))

    def init_dinPMaxScheduleType(self, dinPMaxScheduleType: dinPMaxScheduleType):
        return self.libopenv2g.init_dinPMaxScheduleType(ctypes.pointer(dinPMaxScheduleType))

    def init_dinServicePaymentSelectionReqType(self, dinServicePaymentSelectionReqType: dinServicePaymentSelectionReqType):
        return self.libopenv2g.init_dinServicePaymentSelectionReqType(ctypes.pointer(dinServicePaymentSelectionReqType))

    def init_dinRelativeTimeIntervalType(self, dinRelativeTimeIntervalType: dinRelativeTimeIntervalType):
        return self.libopenv2g.init_dinRelativeTimeIntervalType(ctypes.pointer(dinRelativeTimeIntervalType))

    def init_dinEVStatusType(self, dinEVStatusType: dinEVStatusType):
        return self.libopenv2g.init_dinEVStatusType(ctypes.pointer(dinEVStatusType))

    def init_dinPreChargeResType(self, dinPreChargeResType: dinPreChargeResType):
        return self.libopenv2g.init_dinPreChargeResType(ctypes.pointer(dinPreChargeResType))

    def init_dinDC_EVSEChargeParameterType(self, dinDC_EVSEChargeParameterType: dinDC_EVSEChargeParameterType):
        return self.libopenv2g.init_dinDC_EVSEChargeParameterType(ctypes.pointer(dinDC_EVSEChargeParameterType))

    def init_dinPaymentDetailsResType(self, dinPaymentDetailsResType: dinPaymentDetailsResType):
        return self.libopenv2g.init_dinPaymentDetailsResType(ctypes.pointer(dinPaymentDetailsResType))

    def init_dinDSAKeyValueType(self, dinDSAKeyValueType: dinDSAKeyValueType):
        return self.libopenv2g.init_dinDSAKeyValueType(ctypes.pointer(dinDSAKeyValueType))

    def init_dinSASchedulesType(self, dinSASchedulesType: dinSASchedulesType):
        return self.libopenv2g.init_dinSASchedulesType(ctypes.pointer(dinSASchedulesType))

    def init_dinCertificateUpdateResType(self, dinCertificateUpdateResType: dinCertificateUpdateResType):
        return self.libopenv2g.init_dinCertificateUpdateResType(ctypes.pointer(dinCertificateUpdateResType))

    def init_dinEVChargeParameterType(self, dinEVChargeParameterType: dinEVChargeParameterType):
        return self.libopenv2g.init_dinEVChargeParameterType(ctypes.pointer(dinEVChargeParameterType))

    def init_dinMessageHeaderType(self, dinMessageHeaderType: dinMessageHeaderType):
        return self.libopenv2g.init_dinMessageHeaderType(ctypes.pointer(dinMessageHeaderType))

    def init_dinBodyBaseType(self, dinBodyBaseType: dinBodyBaseType):
        return self.libopenv2g.init_dinBodyBaseType(ctypes.pointer(dinBodyBaseType))

    def init_dinKeyValueType(self, dinKeyValueType: dinKeyValueType):
        return self.libopenv2g.init_dinKeyValueType(ctypes.pointer(dinKeyValueType))

    def init_dinIntervalType(self, dinIntervalType: dinIntervalType):
        return self.libopenv2g.init_dinIntervalType(ctypes.pointer(dinIntervalType))

    def init_dinChargeParameterDiscoveryResType(self, dinChargeParameterDiscoveryResType: dinChargeParameterDiscoveryResType):
        return self.libopenv2g.init_dinChargeParameterDiscoveryResType(ctypes.pointer(dinChargeParameterDiscoveryResType))

    def init_dinPowerDeliveryReqType(self, dinPowerDeliveryReqType: dinPowerDeliveryReqType):
        return self.libopenv2g.init_dinPowerDeliveryReqType(ctypes.pointer(dinPowerDeliveryReqType))

    def init_dinCertificateChainType(self, dinCertificateChainType: dinCertificateChainType):
        return self.libopenv2g.init_dinCertificateChainType(ctypes.pointer(dinCertificateChainType))

    def init_dinTransformsType(self, dinTransformsType: dinTransformsType):
        return self.libopenv2g.init_dinTransformsType(ctypes.pointer(dinTransformsType))

    def init_dinEntryType(self, dinEntryType: dinEntryType):
        return self.libopenv2g.init_dinEntryType(ctypes.pointer(dinEntryType))

    def init_dinSessionStopType(self, dinSessionStopType: dinSessionStopType):
        return self.libopenv2g.init_dinSessionStopType(ctypes.pointer(dinSessionStopType))

    def init_dinServiceDetailReqType(self, dinServiceDetailReqType: dinServiceDetailReqType):
        return self.libopenv2g.init_dinServiceDetailReqType(ctypes.pointer(dinServiceDetailReqType))

    def init_dinDigestMethodType(self, dinDigestMethodType: dinDigestMethodType):
        return self.libopenv2g.init_dinDigestMethodType(ctypes.pointer(dinDigestMethodType))

    def init_dinParameterType(self, dinParameterType: dinParameterType):
        return self.libopenv2g.init_dinParameterType(ctypes.pointer(dinParameterType))

    def init_dinChargingStatusReqType(self, dinChargingStatusReqType: dinChargingStatusReqType):
        return self.libopenv2g.init_dinChargingStatusReqType(ctypes.pointer(dinChargingStatusReqType))

    def init_dinSignatureMethodType(self, dinSignatureMethodType: dinSignatureMethodType):
        return self.libopenv2g.init_dinSignatureMethodType(ctypes.pointer(dinSignatureMethodType))

    def init_dinCertificateInstallationReqType(self, dinCertificateInstallationReqType: dinCertificateInstallationReqType):
        return self.libopenv2g.init_dinCertificateInstallationReqType(ctypes.pointer(dinCertificateInstallationReqType))

    def init_dinSalesTariffEntryType(self, dinSalesTariffEntryType: dinSalesTariffEntryType):
        return self.libopenv2g.init_dinSalesTariffEntryType(ctypes.pointer(dinSalesTariffEntryType))

    def init_dinServiceDiscoveryResType(self, dinServiceDiscoveryResType: dinServiceDiscoveryResType):
        return self.libopenv2g.init_dinServiceDiscoveryResType(ctypes.pointer(dinServiceDiscoveryResType))

    def init_dinParameterSetType(self, dinParameterSetType: dinParameterSetType):
        return self.libopenv2g.init_dinParameterSetType(ctypes.pointer(dinParameterSetType))

    def init_dinCurrentDemandReqType(self, dinCurrentDemandReqType: dinCurrentDemandReqType):
        return self.libopenv2g.init_dinCurrentDemandReqType(ctypes.pointer(dinCurrentDemandReqType))

    def init_dinPreChargeReqType(self, dinPreChargeReqType: dinPreChargeReqType):
        return self.libopenv2g.init_dinPreChargeReqType(ctypes.pointer(dinPreChargeReqType))

    def init_dinSignatureType(self, dinSignatureType: dinSignatureType):
        return self.libopenv2g.init_dinSignatureType(ctypes.pointer(dinSignatureType))

    def init_dinReferenceType(self, dinReferenceType: dinReferenceType):
        return self.libopenv2g.init_dinReferenceType(ctypes.pointer(dinReferenceType))

    def init_dinProfileEntryType(self, dinProfileEntryType: dinProfileEntryType):
        return self.libopenv2g.init_dinProfileEntryType(ctypes.pointer(dinProfileEntryType))

    def init_dinAnonType_V2G_Message(self, dinAnonType_V2G_Message: dinAnonType_V2G_Message):
        return self.libopenv2g.init_dinAnonType_V2G_Message(ctypes.pointer(dinAnonType_V2G_Message))

    def init_dinChargeParameterDiscoveryReqType(self, dinChargeParameterDiscoveryReqType: dinChargeParameterDiscoveryReqType):
        return self.libopenv2g.init_dinChargeParameterDiscoveryReqType(ctypes.pointer(dinChargeParameterDiscoveryReqType))

    def init_dinConsumptionCostType(self, dinConsumptionCostType: dinConsumptionCostType):
        return self.libopenv2g.init_dinConsumptionCostType(ctypes.pointer(dinConsumptionCostType))

    def init_dinRSAKeyValueType(self, dinRSAKeyValueType: dinRSAKeyValueType):
        return self.libopenv2g.init_dinRSAKeyValueType(ctypes.pointer(dinRSAKeyValueType))

    def init_dinServiceType(self, dinServiceType: dinServiceType):
        return self.libopenv2g.init_dinServiceType(ctypes.pointer(dinServiceType))

    def init_dinServiceTagListType(self, dinServiceTagListType: dinServiceTagListType):
        return self.libopenv2g.init_dinServiceTagListType(ctypes.pointer(dinServiceTagListType))

    def init_dinEVSEStatusType(self, dinEVSEStatusType: dinEVSEStatusType):
        return self.libopenv2g.init_dinEVSEStatusType(ctypes.pointer(dinEVSEStatusType))

    def init_dinSessionSetupResType(self, dinSessionSetupResType: dinSessionSetupResType):
        return self.libopenv2g.init_dinSessionSetupResType(ctypes.pointer(dinSessionSetupResType))

    def init_dinEVPowerDeliveryParameterType(self, dinEVPowerDeliveryParameterType: dinEVPowerDeliveryParameterType):
        return self.libopenv2g.init_dinEVPowerDeliveryParameterType(ctypes.pointer(dinEVPowerDeliveryParameterType))

    def init_dinX509IssuerSerialType(self, dinX509IssuerSerialType: dinX509IssuerSerialType):
        return self.libopenv2g.init_dinX509IssuerSerialType(ctypes.pointer(dinX509IssuerSerialType))

    def init_dinSelectedServiceType(self, dinSelectedServiceType: dinSelectedServiceType):
        return self.libopenv2g.init_dinSelectedServiceType(ctypes.pointer(dinSelectedServiceType))

    def init_dinMeteringReceiptResType(self, dinMeteringReceiptResType: dinMeteringReceiptResType):
        return self.libopenv2g.init_dinMeteringReceiptResType(ctypes.pointer(dinMeteringReceiptResType))

    def init_dinDC_EVStatusType(self, dinDC_EVStatusType: dinDC_EVStatusType):
        return self.libopenv2g.init_dinDC_EVStatusType(ctypes.pointer(dinDC_EVStatusType))

    def init_dinPhysicalValueType(self, dinPhysicalValueType: dinPhysicalValueType):
        return self.libopenv2g.init_dinPhysicalValueType(ctypes.pointer(dinPhysicalValueType))

    def init_dinManifestType(self, dinManifestType: dinManifestType):
        return self.libopenv2g.init_dinManifestType(ctypes.pointer(dinManifestType))

    def init_dinPMaxScheduleEntryType(self, dinPMaxScheduleEntryType: dinPMaxScheduleEntryType):
        return self.libopenv2g.init_dinPMaxScheduleEntryType(ctypes.pointer(dinPMaxScheduleEntryType))

    def init_dinServiceParameterListType(self, dinServiceParameterListType: dinServiceParameterListType):
        return self.libopenv2g.init_dinServiceParameterListType(ctypes.pointer(dinServiceParameterListType))

    def init_dinSignatureValueType(self, dinSignatureValueType: dinSignatureValueType):
        return self.libopenv2g.init_dinSignatureValueType(ctypes.pointer(dinSignatureValueType))

    def init_dinPaymentOptionsType(self, dinPaymentOptionsType: dinPaymentOptionsType):
        return self.libopenv2g.init_dinPaymentOptionsType(ctypes.pointer(dinPaymentOptionsType))

    def init_dinServiceTagType(self, dinServiceTagType: dinServiceTagType):
        return self.libopenv2g.init_dinServiceTagType(ctypes.pointer(dinServiceTagType))

    def init_dinAC_EVSEStatusType(self, dinAC_EVSEStatusType: dinAC_EVSEStatusType):
        return self.libopenv2g.init_dinAC_EVSEStatusType(ctypes.byref(dinAC_EVSEStatusType))

    def init_dinCertificateUpdateReqType(self, dinCertificateUpdateReqType: dinCertificateUpdateReqType):
        return self.libopenv2g.init_dinCertificateUpdateReqType(ctypes.pointer(dinCertificateUpdateReqType))

    def init_dinServicePaymentSelectionResType(self, dinServicePaymentSelectionResType: dinServicePaymentSelectionResType):
        return self.libopenv2g.init_dinServicePaymentSelectionResType(ctypes.pointer(dinServicePaymentSelectionResType))

    def init_dinSAScheduleTupleType(self, dinSAScheduleTupleType: dinSAScheduleTupleType):
        return self.libopenv2g.init_dinSAScheduleTupleType(ctypes.pointer(dinSAScheduleTupleType))

    def init_dinChargingProfileType(self, dinChargingProfileType: dinChargingProfileType):
        return self.libopenv2g.init_dinChargingProfileType(ctypes.pointer(dinChargingProfileType))

    def init_dinServiceDiscoveryReqType(self, dinServiceDiscoveryReqType: dinServiceDiscoveryReqType):
        return self.libopenv2g.init_dinServiceDiscoveryReqType(ctypes.pointer(dinServiceDiscoveryReqType))

    def init_dinAC_EVSEChargeParameterType(self, dinAC_EVSEChargeParameterType: dinAC_EVSEChargeParameterType):
        return self.libopenv2g.init_dinAC_EVSEChargeParameterType(ctypes.pointer(dinAC_EVSEChargeParameterType))

    def init_dinKeyInfoType(self, dinKeyInfoType: dinKeyInfoType):
        return self.libopenv2g.init_dinKeyInfoType(ctypes.pointer(dinKeyInfoType))

    def init_dinPaymentDetailsReqType(self, dinPaymentDetailsReqType: dinPaymentDetailsReqType):
        return self.libopenv2g.init_dinPaymentDetailsReqType(ctypes.pointer(dinPaymentDetailsReqType))

    def init_dinCableCheckResType(self, dinCableCheckResType: dinCableCheckResType):
        return self.libopenv2g.init_dinCableCheckResType(ctypes.pointer(dinCableCheckResType))

    def init_dinObjectType(self, dinObjectType: dinObjectType):
        return self.libopenv2g.init_dinObjectType(ctypes.pointer(dinObjectType))

    def init_dinSessionStopResType(self, dinSessionStopResType: dinSessionStopResType):
        return self.libopenv2g.init_dinSessionStopResType(ctypes.pointer(dinSessionStopResType))

    def init_dinSignedInfoType(self, dinSignedInfoType: dinSignedInfoType):
        return self.libopenv2g.init_dinSignedInfoType(ctypes.pointer(dinSignedInfoType))

    def init_dinSalesTariffType(self, dinSalesTariffType: dinSalesTariffType):
        return self.libopenv2g.init_dinSalesTariffType(ctypes.pointer(dinSalesTariffType))

    def init_dinCostType(self, dinCostType: dinCostType):
        return self.libopenv2g.init_dinCostType(ctypes.pointer(dinCostType))

    def init_dinServiceChargeType(self, dinServiceChargeType: dinServiceChargeType):
        return self.libopenv2g.init_dinServiceChargeType(ctypes.pointer(dinServiceChargeType))

    def init_dinDC_EVSEStatusType(self, dinDC_EVSEStatusType: dinDC_EVSEStatusType):
        return self.libopenv2g.init_dinDC_EVSEStatusType(ctypes.byref(dinDC_EVSEStatusType))

    def init_dinRetrievalMethodType(self, dinRetrievalMethodType: dinRetrievalMethodType):
        return self.libopenv2g.init_dinRetrievalMethodType(ctypes.pointer(dinRetrievalMethodType))

    def init_dinNotificationType(self, dinNotificationType: dinNotificationType):
        return self.libopenv2g.init_dinNotificationType(ctypes.pointer(dinNotificationType))

    def init_dinPGPDataType(self, dinPGPDataType: dinPGPDataType):
        return self.libopenv2g.init_dinPGPDataType(ctypes.pointer(dinPGPDataType))

    def init_dinCertificateInstallationResType(self, dinCertificateInstallationResType: dinCertificateInstallationResType):
        return self.libopenv2g.init_dinCertificateInstallationResType(ctypes.pointer(dinCertificateInstallationResType))

    def init_dinSignaturePropertyType(self, dinSignaturePropertyType: dinSignaturePropertyType):
        return self.libopenv2g.init_dinSignaturePropertyType(ctypes.pointer(dinSignaturePropertyType))

    def init_dinMeterInfoType(self, dinMeterInfoType: dinMeterInfoType):
        return self.libopenv2g.init_dinMeterInfoType(ctypes.pointer(dinMeterInfoType))

    def init_dinSubCertificatesType(self, dinSubCertificatesType: dinSubCertificatesType):
        return self.libopenv2g.init_dinSubCertificatesType(ctypes.pointer(dinSubCertificatesType))

    # open_v2g/source/din/dinEXIDataTypesDecoder.h
    def decode_dinExiDocument(self, stream: bitstream_t, exiDoc: dinEXIDocument):
        return self.libopenv2g.decode_dinExiDocument(ctypes.pointer(stream), ctypes.pointer(exiDoc))

    def decode_dinExiFragment(self, stream: bitstream_t, exiFrag: dinEXIFragment):
        return self.libopenv2g.decode_dinExiFragment(ctypes.pointer(stream), ctypes.pointer(exiFrag))

    # open_v2g/source/din/dinEXIDataTypesEncoder.h
    def encode_dinExiDocument(self, stream: bitstream_t, exiDoc: dinEXIDocument):
        return self.libopenv2g.encode_dinExiDocument(ctypes.byref(stream), ctypes.byref(exiDoc))

    def encode_dinExiFragment(self, stream: bitstream_t, exiFrag: dinEXIFragment):
        return self.libopenv2g.encode_dinExiFragment(ctypes.pointer(stream), ctypes.pointer(exiFrag))

    # ---------- iso1 ---------- #
    # open_v2g/source/iso1/iso1EXIDataTypes.h
    def init_iso1EXIDocument(self, exiDoc: iso1EXIDocument):
        return self.libopenv2g.init_iso1EXIDocument(ctypes.pointer(exiDoc))

    def init_iso1EXIFragment(self, exiFrag: iso1EXIFragment):
        return self.libopenv2g.init_iso1EXIFragment(ctypes.pointer(exiFrag))

    def init_iso1EXISchemaInformedElementFragmentGrammar(self, exiFrag: iso1EXISchemaInformedElementFragmentGrammar):
        return self.libopenv2g.init_iso1EXISchemaInformedElementFragmentGrammar(ctypes.pointer(exiFrag))

    def init_iso1MessageHeaderType(self, iso1MessageHeaderType: iso1MessageHeaderType):
        return self.libopenv2g.init_iso1MessageHeaderType(ctypes.pointer(iso1MessageHeaderType))

    def init_iso1SignatureType(self, iso1SignatureType: iso1SignatureType):
        return self.libopenv2g.init_iso1SignatureType(ctypes.pointer(iso1SignatureType))

    def init_iso1PowerDeliveryReqType(self, iso1PowerDeliveryReqType: iso1PowerDeliveryReqType):
        return self.libopenv2g.init_iso1PowerDeliveryReqType(ctypes.pointer(iso1PowerDeliveryReqType))

    def init_iso1ParameterType(self, iso1ParameterType: iso1ParameterType):
        return self.libopenv2g.init_iso1ParameterType(ctypes.pointer(iso1ParameterType))

    def init_iso1CertificateInstallationReqType(self, iso1CertificateInstallationReqType: iso1CertificateInstallationReqType):
        return self.libopenv2g.init_iso1CertificateInstallationReqType(ctypes.pointer(iso1CertificateInstallationReqType))

    def init_iso1SessionSetupResType(self, iso1SessionSetupResType: iso1SessionSetupResType):
        return self.libopenv2g.init_iso1SessionSetupResType(ctypes.pointer(iso1SessionSetupResType))

    def init_iso1EVChargeParameterType(self, iso1EVChargeParameterType: iso1EVChargeParameterType):
        return self.libopenv2g.init_iso1EVChargeParameterType(ctypes.pointer(iso1EVChargeParameterType))

    def init_iso1DiffieHellmanPublickeyType(self, iso1DiffieHellmanPublickeyType: iso1DiffieHellmanPublickeyType):
        return self.libopenv2g.init_iso1DiffieHellmanPublickeyType(ctypes.pointer(iso1DiffieHellmanPublickeyType))

    def init_iso1ServiceDiscoveryResType(self, iso1ServiceDiscoveryResType: iso1ServiceDiscoveryResType):
        return self.libopenv2g.init_iso1ServiceDiscoveryResType(ctypes.pointer(iso1ServiceDiscoveryResType))

    def init_iso1ServiceParameterListType(self, iso1ServiceParameterListType: iso1ServiceParameterListType):
        return self.libopenv2g.init_iso1ServiceParameterListType(ctypes.pointer(iso1ServiceParameterListType))

    def init_iso1CertificateChainType(self, iso1CertificateChainType: iso1CertificateChainType):
        return self.libopenv2g.init_iso1CertificateChainType(ctypes.pointer(iso1CertificateChainType))

    def init_iso1SASchedulesType(self, iso1SASchedulesType: iso1SASchedulesType):
        return self.libopenv2g.init_iso1SASchedulesType(ctypes.pointer(iso1SASchedulesType))

    def init_iso1DC_EVSEStatusType(self, iso1DC_EVSEStatusType: iso1DC_EVSEStatusType):
        return self.libopenv2g.init_iso1DC_EVSEStatusType(ctypes.pointer(iso1DC_EVSEStatusType))

    def init_iso1PreChargeResType(self, iso1PreChargeResType: iso1PreChargeResType):
        return self.libopenv2g.init_iso1PreChargeResType(ctypes.pointer(iso1PreChargeResType))

    def init_iso1ParameterSetType(self, iso1ParameterSetType: iso1ParameterSetType):
        return self.libopenv2g.init_iso1ParameterSetType(ctypes.pointer(iso1ParameterSetType))

    def init_iso1ServiceDetailReqType(self, iso1ServiceDetailReqType: iso1ServiceDetailReqType):
        return self.libopenv2g.init_iso1ServiceDetailReqType(ctypes.pointer(iso1ServiceDetailReqType))

    def init_iso1RelativeTimeIntervalType(self, iso1RelativeTimeIntervalType: iso1RelativeTimeIntervalType):
        return self.libopenv2g.init_iso1RelativeTimeIntervalType(ctypes.pointer(iso1RelativeTimeIntervalType))

    def init_iso1SignedInfoType(self, iso1SignedInfoType: iso1SignedInfoType):
        return self.libopenv2g.init_iso1SignedInfoType(ctypes.pointer(iso1SignedInfoType))

    def init_iso1EMAIDType(self, iso1EMAIDType: iso1EMAIDType):
        return self.libopenv2g.init_iso1EMAIDType(ctypes.pointer(iso1EMAIDType))

    def init_iso1EVStatusType(self, iso1EVStatusType: iso1EVStatusType):
        return self.libopenv2g.init_iso1EVStatusType(ctypes.pointer(iso1EVStatusType))

    def init_iso1ServiceListType(self, iso1ServiceListType: iso1ServiceListType):
        return self.libopenv2g.init_iso1ServiceListType(ctypes.pointer(iso1ServiceListType))

    def init_iso1EVSEChargeParameterType(self, iso1EVSEChargeParameterType: iso1EVSEChargeParameterType):
        return self.libopenv2g.init_iso1EVSEChargeParameterType(ctypes.pointer(iso1EVSEChargeParameterType))

    def init_iso1EVPowerDeliveryParameterType(self, iso1EVPowerDeliveryParameterType: iso1EVPowerDeliveryParameterType):
        return self.libopenv2g.init_iso1EVPowerDeliveryParameterType(ctypes.pointer(iso1EVPowerDeliveryParameterType))

    def init_iso1ProfileEntryType(self, iso1ProfileEntryType: iso1ProfileEntryType):
        return self.libopenv2g.init_iso1ProfileEntryType(ctypes.pointer(iso1ProfileEntryType))

    def init_iso1AuthorizationReqType(self, iso1AuthorizationReqType: iso1AuthorizationReqType):
        return self.libopenv2g.init_iso1AuthorizationReqType(ctypes.pointer(iso1AuthorizationReqType))

    def init_iso1MeterInfoType(self, iso1MeterInfoType: iso1MeterInfoType):
        return self.libopenv2g.init_iso1MeterInfoType(ctypes.pointer(iso1MeterInfoType))

    def init_iso1ManifestType(self, iso1ManifestType: iso1ManifestType):
        return self.libopenv2g.init_iso1ManifestType(ctypes.pointer(iso1ManifestType))

    def init_iso1ChargeParameterDiscoveryResType(self, iso1ChargeParameterDiscoveryResType: iso1ChargeParameterDiscoveryResType):
        return self.libopenv2g.init_iso1ChargeParameterDiscoveryResType(ctypes.pointer(iso1ChargeParameterDiscoveryResType))

    def init_iso1PowerDeliveryResType(self, iso1PowerDeliveryResType: iso1PowerDeliveryResType):
        return self.libopenv2g.init_iso1PowerDeliveryResType(ctypes.pointer(iso1PowerDeliveryResType))

    def init_iso1DC_EVChargeParameterType(self, iso1DC_EVChargeParameterType: iso1DC_EVChargeParameterType):
        return self.libopenv2g.init_iso1DC_EVChargeParameterType(ctypes.pointer(iso1DC_EVChargeParameterType))

    def init_iso1ConsumptionCostType(self, iso1ConsumptionCostType: iso1ConsumptionCostType):
        return self.libopenv2g.init_iso1ConsumptionCostType(ctypes.pointer(iso1ConsumptionCostType))

    def init_iso1PMaxScheduleType(self, iso1PMaxScheduleType: iso1PMaxScheduleType):
        return self.libopenv2g.init_iso1PMaxScheduleType(ctypes.pointer(iso1PMaxScheduleType))

    def init_iso1PaymentOptionListType(self, iso1PaymentOptionListType: iso1PaymentOptionListType):
        return self.libopenv2g.init_iso1PaymentOptionListType(ctypes.pointer(iso1PaymentOptionListType))

    def init_iso1ObjectType(self, iso1ObjectType: iso1ObjectType):
        return self.libopenv2g.init_iso1ObjectType(ctypes.pointer(iso1ObjectType))

    def init_iso1PhysicalValueType(self, iso1PhysicalValueType: iso1PhysicalValueType):
        return self.libopenv2g.init_iso1PhysicalValueType(ctypes.pointer(iso1PhysicalValueType))

    def init_iso1RSAKeyValueType(self, iso1RSAKeyValueType: iso1RSAKeyValueType):
        return self.libopenv2g.init_iso1RSAKeyValueType(ctypes.pointer(iso1RSAKeyValueType))

    def init_iso1SessionStopResType(self, iso1SessionStopResType: iso1SessionStopResType):
        return self.libopenv2g.init_iso1SessionStopResType(ctypes.pointer(iso1SessionStopResType))

    def init_iso1CertificateUpdateReqType(self, iso1CertificateUpdateReqType: iso1CertificateUpdateReqType):
        return self.libopenv2g.init_iso1CertificateUpdateReqType(ctypes.pointer(iso1CertificateUpdateReqType))

    def init_iso1SignatureValueType(self, iso1SignatureValueType: iso1SignatureValueType):
        return self.libopenv2g.init_iso1SignatureValueType(ctypes.pointer(iso1SignatureValueType))

    def init_iso1PaymentDetailsReqType(self, iso1PaymentDetailsReqType: iso1PaymentDetailsReqType):
        return self.libopenv2g.init_iso1PaymentDetailsReqType(ctypes.pointer(iso1PaymentDetailsReqType))

    def init_iso1AuthorizationResType(self, iso1AuthorizationResType: iso1AuthorizationResType):
        return self.libopenv2g.init_iso1AuthorizationResType(ctypes.pointer(iso1AuthorizationResType))

    def init_iso1DC_EVSEChargeParameterType(self, iso1DC_EVSEChargeParameterType: iso1DC_EVSEChargeParameterType):
        return self.libopenv2g.init_iso1DC_EVSEChargeParameterType(ctypes.pointer(iso1DC_EVSEChargeParameterType))

    def init_iso1SubCertificatesType(self, iso1SubCertificatesType: iso1SubCertificatesType):
        return self.libopenv2g.init_iso1SubCertificatesType(ctypes.pointer(iso1SubCertificatesType))

    def init_iso1ChargingStatusResType(self, iso1ChargingStatusResType: iso1ChargingStatusResType):
        return self.libopenv2g.init_iso1ChargingStatusResType(ctypes.pointer(iso1ChargingStatusResType))

    def init_iso1DSAKeyValueType(self, iso1DSAKeyValueType: iso1DSAKeyValueType):
        return self.libopenv2g.init_iso1DSAKeyValueType(ctypes.pointer(iso1DSAKeyValueType))

    def init_iso1ListOfRootCertificateIDsType(self, iso1ListOfRootCertificateIDsType: iso1ListOfRootCertificateIDsType):
        return self.libopenv2g.init_iso1ListOfRootCertificateIDsType(ctypes.pointer(iso1ListOfRootCertificateIDsType))

    def init_iso1ChargeServiceType(self, iso1ChargeServiceType: iso1ChargeServiceType):
        return self.libopenv2g.init_iso1ChargeServiceType(ctypes.pointer(iso1ChargeServiceType))

    def init_iso1IntervalType(self, iso1IntervalType: iso1IntervalType):
        return self.libopenv2g.init_iso1IntervalType(ctypes.pointer(iso1IntervalType))

    def init_iso1MeteringReceiptReqType(self, iso1MeteringReceiptReqType: iso1MeteringReceiptReqType):
        return self.libopenv2g.init_iso1MeteringReceiptReqType(ctypes.pointer(iso1MeteringReceiptReqType))

    def init_iso1ServiceDetailResType(self, iso1ServiceDetailResType: iso1ServiceDetailResType):
        return self.libopenv2g.init_iso1ServiceDetailResType(ctypes.pointer(iso1ServiceDetailResType))

    def init_iso1KeyValueType(self, iso1KeyValueType: iso1KeyValueType):
        return self.libopenv2g.init_iso1KeyValueType(ctypes.pointer(iso1KeyValueType))

    def init_iso1SelectedServiceListType(self, iso1SelectedServiceListType: iso1SelectedServiceListType):
        return self.libopenv2g.init_iso1SelectedServiceListType(ctypes.pointer(iso1SelectedServiceListType))

    def init_iso1CableCheckResType(self, iso1CableCheckResType: iso1CableCheckResType):
        return self.libopenv2g.init_iso1CableCheckResType(ctypes.pointer(iso1CableCheckResType))

    def init_iso1X509IssuerSerialType(self, iso1X509IssuerSerialType: iso1X509IssuerSerialType):
        return self.libopenv2g.init_iso1X509IssuerSerialType(ctypes.pointer(iso1X509IssuerSerialType))

    def init_iso1KeyInfoType(self, iso1KeyInfoType: iso1KeyInfoType):
        return self.libopenv2g.init_iso1KeyInfoType(ctypes.pointer(iso1KeyInfoType))

    def init_iso1TransformsType(self, iso1TransformsType: iso1TransformsType):
        return self.libopenv2g.init_iso1TransformsType(ctypes.pointer(iso1TransformsType))

    def init_iso1ChargeParameterDiscoveryReqType(self, iso1ChargeParameterDiscoveryReqType: iso1ChargeParameterDiscoveryReqType):
        return self.libopenv2g.init_iso1ChargeParameterDiscoveryReqType(ctypes.pointer(iso1ChargeParameterDiscoveryReqType))

    def init_iso1PreChargeReqType(self, iso1PreChargeReqType: iso1PreChargeReqType):
        return self.libopenv2g.init_iso1PreChargeReqType(ctypes.pointer(iso1PreChargeReqType))

    def init_iso1EVSEStatusType(self, iso1EVSEStatusType: iso1EVSEStatusType):
        return self.libopenv2g.init_iso1EVSEStatusType(ctypes.pointer(iso1EVSEStatusType))

    def init_iso1SignatureMethodType(self, iso1SignatureMethodType: iso1SignatureMethodType):
        return self.libopenv2g.init_iso1SignatureMethodType(ctypes.pointer(iso1SignatureMethodType))

    def init_iso1X509DataType(self, iso1X509DataType: iso1X509DataType):
        return self.libopenv2g.init_iso1X509DataType(ctypes.pointer(iso1X509DataType))

    def init_iso1NotificationType(self, iso1NotificationType: iso1NotificationType):
        return self.libopenv2g.init_iso1NotificationType(ctypes.pointer(iso1NotificationType))

    def init_iso1SAScheduleListType(self, iso1SAScheduleListType: iso1SAScheduleListType):
        return self.libopenv2g.init_iso1SAScheduleListType(ctypes.pointer(iso1SAScheduleListType))

    def init_iso1BodyType(self, iso1BodyType: iso1BodyType):
        return self.libopenv2g.init_iso1BodyType(ctypes.pointer(iso1BodyType))

    def init_iso1ChargingProfileType(self, iso1ChargingProfileType: iso1ChargingProfileType):
        return self.libopenv2g.init_iso1ChargingProfileType(ctypes.pointer(iso1ChargingProfileType))

    def init_iso1TransformType(self, iso1TransformType: iso1TransformType):
        return self.libopenv2g.init_iso1TransformType(ctypes.pointer(iso1TransformType))

    def init_iso1SAScheduleTupleType(self, iso1SAScheduleTupleType: iso1SAScheduleTupleType):
        return self.libopenv2g.init_iso1SAScheduleTupleType(ctypes.pointer(iso1SAScheduleTupleType))

    def init_iso1AC_EVChargeParameterType(self, iso1AC_EVChargeParameterType: iso1AC_EVChargeParameterType):
        return self.libopenv2g.init_iso1AC_EVChargeParameterType(ctypes.pointer(iso1AC_EVChargeParameterType))

    def init_iso1AnonType_V2G_Message(self, iso1AnonType_V2G_Message: iso1AnonType_V2G_Message):
        return self.libopenv2g.init_iso1AnonType_V2G_Message(ctypes.pointer(iso1AnonType_V2G_Message))

    def init_iso1PaymentDetailsResType(self, iso1PaymentDetailsResType: iso1PaymentDetailsResType):
        return self.libopenv2g.init_iso1PaymentDetailsResType(ctypes.pointer(iso1PaymentDetailsResType))

    def init_iso1ContractSignatureEncryptedPrivateKeyType(self, iso1ContractSignatureEncryptedPrivateKeyType: iso1ContractSignatureEncryptedPrivateKeyType):
        return self.libopenv2g.init_iso1ContractSignatureEncryptedPrivateKeyType(ctypes.pointer(iso1ContractSignatureEncryptedPrivateKeyType))

    def init_iso1PMaxScheduleEntryType(self, iso1PMaxScheduleEntryType: iso1PMaxScheduleEntryType):
        return self.libopenv2g.init_iso1PMaxScheduleEntryType(ctypes.pointer(iso1PMaxScheduleEntryType))

    def init_iso1SPKIDataType(self, iso1SPKIDataType: iso1SPKIDataType):
        return self.libopenv2g.init_iso1SPKIDataType(ctypes.pointer(iso1SPKIDataType))

    def init_iso1MeteringReceiptResType(self, iso1MeteringReceiptResType: iso1MeteringReceiptResType):
        return self.libopenv2g.init_iso1MeteringReceiptResType(ctypes.pointer(iso1MeteringReceiptResType))

    def init_iso1SessionStopReqType(self, iso1SessionStopReqType: iso1SessionStopReqType):
        return self.libopenv2g.init_iso1SessionStopReqType(ctypes.pointer(iso1SessionStopReqType))

    def init_iso1WeldingDetectionResType(self, iso1WeldingDetectionResType: iso1WeldingDetectionResType):
        return self.libopenv2g.init_iso1WeldingDetectionResType(ctypes.pointer(iso1WeldingDetectionResType))

    def init_iso1ReferenceType(self, iso1ReferenceType: iso1ReferenceType):
        return self.libopenv2g.init_iso1ReferenceType(ctypes.pointer(iso1ReferenceType))

    def init_iso1CurrentDemandReqType(self, iso1CurrentDemandReqType: iso1CurrentDemandReqType):
        return self.libopenv2g.init_iso1CurrentDemandReqType(ctypes.pointer(iso1CurrentDemandReqType))

    def init_iso1SalesTariffEntryType(self, iso1SalesTariffEntryType: iso1SalesTariffEntryType):
        return self.libopenv2g.init_iso1SalesTariffEntryType(ctypes.pointer(iso1SalesTariffEntryType))

    def init_iso1EntryType(self, iso1EntryType: iso1EntryType):
        return self.libopenv2g.init_iso1EntryType(ctypes.pointer(iso1EntryType))

    def init_iso1SessionSetupReqType(self, iso1SessionSetupReqType: iso1SessionSetupReqType):
        return self.libopenv2g.init_iso1SessionSetupReqType(ctypes.pointer(iso1SessionSetupReqType))

    def init_iso1CostType(self, iso1CostType: iso1CostType):
        return self.libopenv2g.init_iso1CostType(ctypes.pointer(iso1CostType))

    def init_iso1DC_EVPowerDeliveryParameterType(self, iso1DC_EVPowerDeliveryParameterType: iso1DC_EVPowerDeliveryParameterType):
        return self.libopenv2g.init_iso1DC_EVPowerDeliveryParameterType(ctypes.pointer(iso1DC_EVPowerDeliveryParameterType))

    def init_iso1RetrievalMethodType(self, iso1RetrievalMethodType: iso1RetrievalMethodType):
        return self.libopenv2g.init_iso1RetrievalMethodType(ctypes.pointer(iso1RetrievalMethodType))

    def init_iso1CertificateUpdateResType(self, iso1CertificateUpdateResType: iso1CertificateUpdateResType):
        return self.libopenv2g.init_iso1CertificateUpdateResType(ctypes.pointer(iso1CertificateUpdateResType))

    def init_iso1CertificateInstallationResType(self, iso1CertificateInstallationResType: iso1CertificateInstallationResType):
        return self.libopenv2g.init_iso1CertificateInstallationResType(ctypes.pointer(iso1CertificateInstallationResType))

    def init_iso1CanonicalizationMethodType(self, iso1CanonicalizationMethodType: iso1CanonicalizationMethodType):
        return self.libopenv2g.init_iso1CanonicalizationMethodType(ctypes.pointer(iso1CanonicalizationMethodType))

    def init_iso1WeldingDetectionReqType(self, iso1WeldingDetectionReqType: iso1WeldingDetectionReqType):
        return self.libopenv2g.init_iso1WeldingDetectionReqType(ctypes.pointer(iso1WeldingDetectionReqType))

    def init_iso1DC_EVStatusType(self, iso1DC_EVStatusType: iso1DC_EVStatusType):
        return self.libopenv2g.init_iso1DC_EVStatusType(ctypes.pointer(iso1DC_EVStatusType))

    def init_iso1CurrentDemandResType(self, iso1CurrentDemandResType: iso1CurrentDemandResType):
        return self.libopenv2g.init_iso1CurrentDemandResType(ctypes.pointer(iso1CurrentDemandResType))

    def init_iso1ServiceType(self, iso1ServiceType: iso1ServiceType):
        return self.libopenv2g.init_iso1ServiceType(ctypes.pointer(iso1ServiceType))

    def init_iso1ServiceDiscoveryReqType(self, iso1ServiceDiscoveryReqType: iso1ServiceDiscoveryReqType):
        return self.libopenv2g.init_iso1ServiceDiscoveryReqType(ctypes.pointer(iso1ServiceDiscoveryReqType))

    def init_iso1AC_EVSEChargeParameterType(self, iso1AC_EVSEChargeParameterType: iso1AC_EVSEChargeParameterType):
        return self.libopenv2g.init_iso1AC_EVSEChargeParameterType(ctypes.pointer(iso1AC_EVSEChargeParameterType))

    def init_iso1CableCheckReqType(self, iso1CableCheckReqType: iso1CableCheckReqType):
        return self.libopenv2g.init_iso1CableCheckReqType(ctypes.pointer(iso1CableCheckReqType))

    def init_iso1SelectedServiceType(self, iso1SelectedServiceType: iso1SelectedServiceType):
        return self.libopenv2g.init_iso1SelectedServiceType(ctypes.pointer(iso1SelectedServiceType))

    def init_iso1AC_EVSEStatusType(self, iso1AC_EVSEStatusType: iso1AC_EVSEStatusType):
        return self.libopenv2g.init_iso1AC_EVSEStatusType(ctypes.pointer(iso1AC_EVSEStatusType))

    def init_iso1SalesTariffType(self, iso1SalesTariffType: iso1SalesTariffType):
        return self.libopenv2g.init_iso1SalesTariffType(ctypes.pointer(iso1SalesTariffType))

    def init_iso1PaymentServiceSelectionReqType(self, iso1PaymentServiceSelectionReqType: iso1PaymentServiceSelectionReqType):
        return self.libopenv2g.init_iso1PaymentServiceSelectionReqType(ctypes.pointer(iso1PaymentServiceSelectionReqType))

    def init_iso1SignaturePropertiesType(self, iso1SignaturePropertiesType: iso1SignaturePropertiesType):
        return self.libopenv2g.init_iso1SignaturePropertiesType(ctypes.pointer(iso1SignaturePropertiesType))

    def init_iso1BodyBaseType(self, iso1BodyBaseType: iso1BodyBaseType):
        return self.libopenv2g.init_iso1BodyBaseType(ctypes.pointer(iso1BodyBaseType))

    def init_iso1SupportedEnergyTransferModeType(self, iso1SupportedEnergyTransferModeType: iso1SupportedEnergyTransferModeType):
        return self.libopenv2g.init_iso1SupportedEnergyTransferModeType(ctypes.pointer(iso1SupportedEnergyTransferModeType))

    def init_iso1ChargingStatusReqType(self, iso1ChargingStatusReqType: iso1ChargingStatusReqType):
        return self.libopenv2g.init_iso1ChargingStatusReqType(ctypes.pointer(iso1ChargingStatusReqType))

    def init_iso1PaymentServiceSelectionResType(self, iso1PaymentServiceSelectionResType: iso1PaymentServiceSelectionResType):
        return self.libopenv2g.init_iso1PaymentServiceSelectionResType(ctypes.pointer(iso1PaymentServiceSelectionResType))

    def init_iso1DigestMethodType(self, iso1DigestMethodType: iso1DigestMethodType):
        return self.libopenv2g.init_iso1DigestMethodType(ctypes.pointer(iso1DigestMethodType))

    def init_iso1SignaturePropertyType(self, iso1SignaturePropertyType: iso1SignaturePropertyType):
        return self.libopenv2g.init_iso1SignaturePropertyType(ctypes.pointer(iso1SignaturePropertyType))

    def init_iso1PGPDataType(self, iso1PGPDataType: iso1PGPDataType):
        return self.libopenv2g.init_iso1PGPDataType(ctypes.pointer(iso1PGPDataType))


    # open_v2g/source/iso1/iso1EXIDatatypesDecoder.h
    def decode_iso1ExiDocument(self, stream: bitstream_t, exiDoc: iso1EXIDocument):
        return self.libopenv2g.decode_iso1ExiDocument(ctypes.pointer(stream), ctypes.pointer(exiDoc))

    def decode_iso1ExiFragment(self, stream: bitstream_t, exiFrag: iso1EXIFragment):
        return self.libopenv2g.decode_iso1ExiFragment(ctypes.pointer(stream), ctypes.pointer(exiFrag))

    # open_v2g/source/iso1/iso1EXIDatatypesEncoder.h
    def encode_iso1ExiDocument(self, stream: bitstream_t, exiDoc: iso1EXIDocument):
        return self.libopenv2g.encode_iso1ExiDocument(ctypes.pointer(stream), ctypes.pointer(exiDoc))

    def encode_iso1ExiFragment(self, stream: bitstream_t, exiFrag: iso1EXIFragment):
        return self.libopenv2g.encode_iso1ExiFragment(ctypes.pointer(stream), ctypes.pointer(exiFrag))


    # ---------- iso2 ---------- #
    # open_v2g/source/iso2/iso2EXIDataTypes.h    
    def init_iso2EXIDocument(self, exiDoc: iso2EXIDocument):
        return self.libopenv2g.init_iso2EXIDocument(ctypes.pointer(exiDoc))

    def init_iso2EXIFragment(self, exiFrag: iso2EXIFragment):
        return self.libopenv2g.init_iso2EXIFragment(ctypes.pointer(exiFrag))

    def init_iso2RetrievalMethodType(self, iso2RetrievalMethodType: iso2RetrievalMethodType):
        return self.libopenv2g.init_iso2RetrievalMethodType(ctypes.pointer(iso2RetrievalMethodType))

    def init_iso2AuthorizationResType(self, iso2AuthorizationResType: iso2AuthorizationResType):
        return self.libopenv2g.init_iso2AuthorizationResType(ctypes.pointer(iso2AuthorizationResType))

    def init_iso2MV_EVSEFinePositioningSetupParametersType(self, iso2MV_EVSEFinePositioningSetupParametersType: iso2MV_EVSEFinePositioningSetupParametersType):
        return self.libopenv2g.init_iso2MV_EVSEFinePositioningSetupParametersType(ctypes.pointer(iso2MV_EVSEFinePositioningSetupParametersType))

    def init_iso2X509DataType(self, iso2X509DataType: iso2X509DataType):
        return self.libopenv2g.init_iso2X509DataType(ctypes.pointer(iso2X509DataType))

    def init_iso2RSAKeyValueType(self, iso2RSAKeyValueType: iso2RSAKeyValueType):
        return self.libopenv2g.init_iso2RSAKeyValueType(ctypes.pointer(iso2RSAKeyValueType))

    def init_iso2DC_BidirectionalControlResType(self, iso2DC_BidirectionalControlResType: iso2DC_BidirectionalControlResType):
        return self.libopenv2g.init_iso2DC_BidirectionalControlResType(ctypes.pointer(iso2DC_BidirectionalControlResType))

    def init_iso2CostType(self, iso2CostType: iso2CostType):
        return self.libopenv2g.init_iso2CostType(ctypes.pointer(iso2CostType))

    def init_iso2ChargingStatusResType(self, iso2ChargingStatusResType: iso2ChargingStatusResType):
        return self.libopenv2g.init_iso2ChargingStatusResType(ctypes.pointer(iso2ChargingStatusResType))

    def init_iso2MeterInfoType(self, iso2MeterInfoType: iso2MeterInfoType):
        return self.libopenv2g.init_iso2MeterInfoType(ctypes.pointer(iso2MeterInfoType))

    def init_iso2AC_EVChargeParameterType(self, iso2AC_EVChargeParameterType: iso2AC_EVChargeParameterType):
        return self.libopenv2g.init_iso2AC_EVChargeParameterType(ctypes.pointer(iso2AC_EVChargeParameterType))

    def init_iso2AC_EVSEBidirectionalParameterType(self, iso2AC_EVSEBidirectionalParameterType: iso2AC_EVSEBidirectionalParameterType):
        return self.libopenv2g.init_iso2AC_EVSEBidirectionalParameterType(ctypes.pointer(iso2AC_EVSEBidirectionalParameterType))

    def init_iso2VehicleCheckOutResType(self, iso2VehicleCheckOutResType: iso2VehicleCheckOutResType):
        return self.libopenv2g.init_iso2VehicleCheckOutResType(ctypes.pointer(iso2VehicleCheckOutResType))

    def init_iso2MagneticVectorListType(self, iso2MagneticVectorListType: iso2MagneticVectorListType):
        return self.libopenv2g.init_iso2MagneticVectorListType(ctypes.pointer(iso2MagneticVectorListType))

    def init_iso2CableCheckResType(self, iso2CableCheckResType: iso2CableCheckResType):
        return self.libopenv2g.init_iso2CableCheckResType(ctypes.pointer(iso2CableCheckResType))

    def init_iso2ServiceDiscoveryReqType(self, iso2ServiceDiscoveryReqType: iso2ServiceDiscoveryReqType):
        return self.libopenv2g.init_iso2ServiceDiscoveryReqType(ctypes.pointer(iso2ServiceDiscoveryReqType))

    def init_iso2ServiceType(self, iso2ServiceType: iso2ServiceType):
        return self.libopenv2g.init_iso2ServiceType(ctypes.pointer(iso2ServiceType))

    def init_iso2ServiceParameterListType(self, iso2ServiceParameterListType: iso2ServiceParameterListType):
        return self.libopenv2g.init_iso2ServiceParameterListType(ctypes.pointer(iso2ServiceParameterListType))

    def init_iso2PMaxScheduleType(self, iso2PMaxScheduleType: iso2PMaxScheduleType):
        return self.libopenv2g.init_iso2PMaxScheduleType(ctypes.pointer(iso2PMaxScheduleType))

    def init_iso2SignaturePropertiesType(self, iso2SignaturePropertiesType: iso2SignaturePropertiesType):
        return self.libopenv2g.init_iso2SignaturePropertiesType(ctypes.pointer(iso2SignaturePropertiesType))

    def init_iso2PMaxScheduleEntryType(self, iso2PMaxScheduleEntryType: iso2PMaxScheduleEntryType):
        return self.libopenv2g.init_iso2PMaxScheduleEntryType(ctypes.pointer(iso2PMaxScheduleEntryType))

    def init_iso2SignatureType(self, iso2SignatureType: iso2SignatureType):
        return self.libopenv2g.init_iso2SignatureType(ctypes.pointer(iso2SignatureType))

    def init_iso2VehicleCheckInReqType(self, iso2VehicleCheckInReqType: iso2VehicleCheckInReqType):
        return self.libopenv2g.init_iso2VehicleCheckInReqType(ctypes.pointer(iso2VehicleCheckInReqType))

    def init_iso2ConnectChargingDeviceResType(self, iso2ConnectChargingDeviceResType: iso2ConnectChargingDeviceResType):
        return self.libopenv2g.init_iso2ConnectChargingDeviceResType(ctypes.pointer(iso2ConnectChargingDeviceResType))

    def init_iso2WeldingDetectionResType(self, iso2WeldingDetectionResType: iso2WeldingDetectionResType):
        return self.libopenv2g.init_iso2WeldingDetectionResType(ctypes.pointer(iso2WeldingDetectionResType))

    def init_iso2SessionStopResType(self, iso2SessionStopResType: iso2SessionStopResType):
        return self.libopenv2g.init_iso2SessionStopResType(ctypes.pointer(iso2SessionStopResType))

    def init_iso2VehicleCheckInResType(self, iso2VehicleCheckInResType: iso2VehicleCheckInResType):
        return self.libopenv2g.init_iso2VehicleCheckInResType(ctypes.pointer(iso2VehicleCheckInResType))

    def init_iso2ServiceListType(self, iso2ServiceListType: iso2ServiceListType):
        return self.libopenv2g.init_iso2ServiceListType(ctypes.pointer(iso2ServiceListType))

    def init_iso2CertificateUpdateResType(self, iso2CertificateUpdateResType: iso2CertificateUpdateResType):
        return self.libopenv2g.init_iso2CertificateUpdateResType(ctypes.pointer(iso2CertificateUpdateResType))

    def init_iso2FinePositioningSetupResType(self, iso2FinePositioningSetupResType: iso2FinePositioningSetupResType):
        return self.libopenv2g.init_iso2FinePositioningSetupResType(ctypes.pointer(iso2FinePositioningSetupResType))

    def init_iso2AC_EVBidirectionalParameterType(self, iso2AC_EVBidirectionalParameterType: iso2AC_EVBidirectionalParameterType):
        return self.libopenv2g.init_iso2AC_EVBidirectionalParameterType(ctypes.pointer(iso2AC_EVBidirectionalParameterType))

    def init_iso2DC_BidirectionalControlReqType(self, iso2DC_BidirectionalControlReqType: iso2DC_BidirectionalControlReqType):
        return self.libopenv2g.init_iso2DC_BidirectionalControlReqType(ctypes.pointer(iso2DC_BidirectionalControlReqType))

    def init_iso2CertificateUpdateReqType(self, iso2CertificateUpdateReqType: iso2CertificateUpdateReqType):
        return self.libopenv2g.init_iso2CertificateUpdateReqType(ctypes.pointer(iso2CertificateUpdateReqType))

    def init_iso2ConsumptionCostType(self, iso2ConsumptionCostType: iso2ConsumptionCostType):
        return self.libopenv2g.init_iso2ConsumptionCostType(ctypes.pointer(iso2ConsumptionCostType))

    def init_iso2SAScheduleListType(self, iso2SAScheduleListType: iso2SAScheduleListType):
        return self.libopenv2g.init_iso2SAScheduleListType(ctypes.pointer(iso2SAScheduleListType))

    def init_iso2MagneticVectorSetupType(self, iso2MagneticVectorSetupType: iso2MagneticVectorSetupType):
        return self.libopenv2g.init_iso2MagneticVectorSetupType(ctypes.pointer(iso2MagneticVectorSetupType))

    def init_iso2LFA_EVSEFinePositioningSetupParametersType(self, iso2LFA_EVSEFinePositioningSetupParametersType: iso2LFA_EVSEFinePositioningSetupParametersType):
        return self.libopenv2g.init_iso2LFA_EVSEFinePositioningSetupParametersType(ctypes.pointer(iso2LFA_EVSEFinePositioningSetupParametersType))

    def init_iso2PaymentOptionListType(self, iso2PaymentOptionListType: iso2PaymentOptionListType):
        return self.libopenv2g.init_iso2PaymentOptionListType(ctypes.pointer(iso2PaymentOptionListType))

    def init_iso2LFA_EVSEFinePositioningParametersType(self, iso2LFA_EVSEFinePositioningParametersType: iso2LFA_EVSEFinePositioningParametersType):
        return self.libopenv2g.init_iso2LFA_EVSEFinePositioningParametersType(ctypes.pointer(iso2LFA_EVSEFinePositioningParametersType))

    def init_iso2RelativeTimeIntervalType(self, iso2RelativeTimeIntervalType: iso2RelativeTimeIntervalType):
        return self.libopenv2g.init_iso2RelativeTimeIntervalType(ctypes.pointer(iso2RelativeTimeIntervalType))

    def init_iso2EVFinePositioningParametersType(self, iso2EVFinePositioningParametersType: iso2EVFinePositioningParametersType):
        return self.libopenv2g.init_iso2EVFinePositioningParametersType(ctypes.pointer(iso2EVFinePositioningParametersType))

    def init_iso2AlignmentCheckReqType(self, iso2AlignmentCheckReqType: iso2AlignmentCheckReqType):
        return self.libopenv2g.init_iso2AlignmentCheckReqType(ctypes.pointer(iso2AlignmentCheckReqType))

    def init_iso2CertificateInstallationReqType(self, iso2CertificateInstallationReqType: iso2CertificateInstallationReqType):
        return self.libopenv2g.init_iso2CertificateInstallationReqType(ctypes.pointer(iso2CertificateInstallationReqType))

    def init_iso2TransformsType(self, iso2TransformsType: iso2TransformsType):
        return self.libopenv2g.init_iso2TransformsType(ctypes.pointer(iso2TransformsType))

    def init_iso2ObjectType(self, iso2ObjectType: iso2ObjectType):
        return self.libopenv2g.init_iso2ObjectType(ctypes.pointer(iso2ObjectType))

    def init_iso2SensorOrderListType(self, iso2SensorOrderListType: iso2SensorOrderListType):
        return self.libopenv2g.init_iso2SensorOrderListType(ctypes.pointer(iso2SensorOrderListType))

    def init_iso2ChargeParameterDiscoveryReqType(self, iso2ChargeParameterDiscoveryReqType: iso2ChargeParameterDiscoveryReqType):
        return self.libopenv2g.init_iso2ChargeParameterDiscoveryReqType(ctypes.pointer(iso2ChargeParameterDiscoveryReqType))

    def init_iso2ParameterType(self, iso2ParameterType: iso2ParameterType):
        return self.libopenv2g.init_iso2ParameterType(ctypes.pointer(iso2ParameterType))

    def init_iso2SessionStopReqType(self, iso2SessionStopReqType: iso2SessionStopReqType):
        return self.libopenv2g.init_iso2SessionStopReqType(ctypes.pointer(iso2SessionStopReqType))

    def init_iso2SensorMeasurementsType(self, iso2SensorMeasurementsType: iso2SensorMeasurementsType):
        return self.libopenv2g.init_iso2SensorMeasurementsType(ctypes.pointer(iso2SensorMeasurementsType))

    def init_iso2DC_EVSEChargeParameterType(self, iso2DC_EVSEChargeParameterType: iso2DC_EVSEChargeParameterType):
        return self.libopenv2g.init_iso2DC_EVSEChargeParameterType(ctypes.pointer(iso2DC_EVSEChargeParameterType))

    def init_iso2SensorPackageListType(self, iso2SensorPackageListType: iso2SensorPackageListType):
        return self.libopenv2g.init_iso2SensorPackageListType(ctypes.pointer(iso2SensorPackageListType))

    def init_iso2MeasurementDataListType(self, iso2MeasurementDataListType: iso2MeasurementDataListType):
        return self.libopenv2g.init_iso2MeasurementDataListType(ctypes.pointer(iso2MeasurementDataListType))

    def init_iso2CertificateChainType(self, iso2CertificateChainType: iso2CertificateChainType):
        return self.libopenv2g.init_iso2CertificateChainType(ctypes.pointer(iso2CertificateChainType))

    def init_iso2SignaturePropertyType(self, iso2SignaturePropertyType: iso2SignaturePropertyType):
        return self.libopenv2g.init_iso2SignaturePropertyType(ctypes.pointer(iso2SignaturePropertyType))

    def init_iso2TransformType(self, iso2TransformType: iso2TransformType):
        return self.libopenv2g.init_iso2TransformType(ctypes.pointer(iso2TransformType))

    def init_iso2EMAIDType(self, iso2EMAIDType: iso2EMAIDType):
        return self.libopenv2g.init_iso2EMAIDType(ctypes.pointer(iso2EMAIDType))

    def init_iso2DSAKeyValueType(self, iso2DSAKeyValueType: iso2DSAKeyValueType):
        return self.libopenv2g.init_iso2DSAKeyValueType(ctypes.pointer(iso2DSAKeyValueType))

    def init_iso2EntryType(self, iso2EntryType: iso2EntryType):
        return self.libopenv2g.init_iso2EntryType(ctypes.pointer(iso2EntryType))

    def init_iso2MessageHeaderType(self, iso2MessageHeaderType: iso2MessageHeaderType):
        return self.libopenv2g.init_iso2MessageHeaderType(ctypes.pointer(iso2MessageHeaderType))

    def init_iso2WPT_EVChargeParameterType(self, iso2WPT_EVChargeParameterType: iso2WPT_EVChargeParameterType):
        return self.libopenv2g.init_iso2WPT_EVChargeParameterType(ctypes.pointer(iso2WPT_EVChargeParameterType))

    def init_iso2DisconnectChargingDeviceReqType(self, iso2DisconnectChargingDeviceReqType: iso2DisconnectChargingDeviceReqType):
        return self.libopenv2g.init_iso2DisconnectChargingDeviceReqType(ctypes.pointer(iso2DisconnectChargingDeviceReqType))

    def init_iso2ChargeLoopReqType(self, iso2ChargeLoopReqType: iso2ChargeLoopReqType):
        return self.libopenv2g.init_iso2ChargeLoopReqType(ctypes.pointer(iso2ChargeLoopReqType))

    def init_iso2V2GRequestType(self, iso2V2GRequestType: iso2V2GRequestType):
        return self.libopenv2g.init_iso2V2GRequestType(ctypes.pointer(iso2V2GRequestType))

    def init_iso2MeteringReceiptResType(self, iso2MeteringReceiptResType: iso2MeteringReceiptResType):
        return self.libopenv2g.init_iso2MeteringReceiptResType(ctypes.pointer(iso2MeteringReceiptResType))

    def init_iso2SessionSetupResType(self, iso2SessionSetupResType: iso2SessionSetupResType):
        return self.libopenv2g.init_iso2SessionSetupResType(ctypes.pointer(iso2SessionSetupResType))

    def init_iso2AC_BidirectionalControlReqType(self, iso2AC_BidirectionalControlReqType: iso2AC_BidirectionalControlReqType):
        return self.libopenv2g.init_iso2AC_BidirectionalControlReqType(ctypes.pointer(iso2AC_BidirectionalControlReqType))

    def init_iso2MV_EVSEFinePositioningParametersType(self, iso2MV_EVSEFinePositioningParametersType: iso2MV_EVSEFinePositioningParametersType):
        return self.libopenv2g.init_iso2MV_EVSEFinePositioningParametersType(ctypes.pointer(iso2MV_EVSEFinePositioningParametersType))

    def init_iso2ReferenceType(self, iso2ReferenceType: iso2ReferenceType):
        return self.libopenv2g.init_iso2ReferenceType(ctypes.pointer(iso2ReferenceType))

    def init_iso2EVSEEnergyTransferParameterType(self, iso2EVSEEnergyTransferParameterType: iso2EVSEEnergyTransferParameterType):
        return self.libopenv2g.init_iso2EVSEEnergyTransferParameterType(ctypes.pointer(iso2EVSEEnergyTransferParameterType))

    def init_iso2MeteringReceiptReqType(self, iso2MeteringReceiptReqType: iso2MeteringReceiptReqType):
        return self.libopenv2g.init_iso2MeteringReceiptReqType(ctypes.pointer(iso2MeteringReceiptReqType))

    def init_iso2KeyValueType(self, iso2KeyValueType: iso2KeyValueType):
        return self.libopenv2g.init_iso2KeyValueType(ctypes.pointer(iso2KeyValueType))

    def init_iso2SensorListType(self, iso2SensorListType: iso2SensorListType):
        return self.libopenv2g.init_iso2SensorListType(ctypes.pointer(iso2SensorListType))

    def init_iso2CurrentDemandReqType(self, iso2CurrentDemandReqType: iso2CurrentDemandReqType):
        return self.libopenv2g.init_iso2CurrentDemandReqType(ctypes.pointer(iso2CurrentDemandReqType))

    def init_iso2FinePositioningSetupReqType(self, iso2FinePositioningSetupReqType: iso2FinePositioningSetupReqType):
        return self.libopenv2g.init_iso2FinePositioningSetupReqType(ctypes.pointer(iso2FinePositioningSetupReqType))

    def init_iso2LFA_EVFinePositioningSetupParametersType(self, iso2LFA_EVFinePositioningSetupParametersType: iso2LFA_EVFinePositioningSetupParametersType):
        return self.libopenv2g.init_iso2LFA_EVFinePositioningSetupParametersType(ctypes.pointer(iso2LFA_EVFinePositioningSetupParametersType))

    def init_iso2SAScheduleTupleType(self, iso2SAScheduleTupleType: iso2SAScheduleTupleType):
        return self.libopenv2g.init_iso2SAScheduleTupleType(ctypes.pointer(iso2SAScheduleTupleType))

    def init_iso2WPT_EVSEChargeParameterType(self, iso2WPT_EVSEChargeParameterType: iso2WPT_EVSEChargeParameterType):
        return self.libopenv2g.init_iso2WPT_EVSEChargeParameterType(ctypes.pointer(iso2WPT_EVSEChargeParameterType))

    def init_iso2FinePositioningResType(self, iso2FinePositioningResType: iso2FinePositioningResType):
        return self.libopenv2g.init_iso2FinePositioningResType(ctypes.pointer(iso2FinePositioningResType))

    def init_iso2BodyBaseType(self, iso2BodyBaseType: iso2BodyBaseType):
        return self.libopenv2g.init_iso2BodyBaseType(ctypes.pointer(iso2BodyBaseType))

    def init_iso2ServiceDetailResType(self, iso2ServiceDetailResType: iso2ServiceDetailResType):
        return self.libopenv2g.init_iso2ServiceDetailResType(ctypes.pointer(iso2ServiceDetailResType))

    def init_iso2PowerDeliveryReqType(self, iso2PowerDeliveryReqType: iso2PowerDeliveryReqType):
        return self.libopenv2g.init_iso2PowerDeliveryReqType(ctypes.pointer(iso2PowerDeliveryReqType))

    def init_iso2PairingResType(self, iso2PairingResType: iso2PairingResType):
        return self.libopenv2g.init_iso2PairingResType(ctypes.pointer(iso2PairingResType))

    def init_iso2AuthorizationReqType(self, iso2AuthorizationReqType: iso2AuthorizationReqType):
        return self.libopenv2g.init_iso2AuthorizationReqType(ctypes.pointer(iso2AuthorizationReqType))

    def init_iso2ParameterSetType(self, iso2ParameterSetType: iso2ParameterSetType):
        return self.libopenv2g.init_iso2ParameterSetType(ctypes.pointer(iso2ParameterSetType))

    def init_iso2SPKIDataType(self, iso2SPKIDataType: iso2SPKIDataType):
        return self.libopenv2g.init_iso2SPKIDataType(ctypes.pointer(iso2SPKIDataType))

    def init_iso2PaymentDetailsResType(self, iso2PaymentDetailsResType: iso2PaymentDetailsResType):
        return self.libopenv2g.init_iso2PaymentDetailsResType(ctypes.pointer(iso2PaymentDetailsResType))

    def init_iso2SignatureMethodType(self, iso2SignatureMethodType: iso2SignatureMethodType):
        return self.libopenv2g.init_iso2SignatureMethodType(ctypes.pointer(iso2SignatureMethodType))

    def init_iso2AC_BidirectionalControlResType(self, iso2AC_BidirectionalControlResType: iso2AC_BidirectionalControlResType):
        return self.libopenv2g.init_iso2AC_BidirectionalControlResType(ctypes.pointer(iso2AC_BidirectionalControlResType))

    def init_iso2VehicleCheckOutReqType(self, iso2VehicleCheckOutReqType: iso2VehicleCheckOutReqType):
        return self.libopenv2g.init_iso2VehicleCheckOutReqType(ctypes.pointer(iso2VehicleCheckOutReqType))

    def init_iso2WeldingDetectionReqType(self, iso2WeldingDetectionReqType: iso2WeldingDetectionReqType):
        return self.libopenv2g.init_iso2WeldingDetectionReqType(ctypes.pointer(iso2WeldingDetectionReqType))

    def init_iso2AlignmentCheckResType(self, iso2AlignmentCheckResType: iso2AlignmentCheckResType):
        return self.libopenv2g.init_iso2AlignmentCheckResType(ctypes.pointer(iso2AlignmentCheckResType))

    def init_iso2PowerDemandReqType(self, iso2PowerDemandReqType: iso2PowerDemandReqType):
        return self.libopenv2g.init_iso2PowerDemandReqType(ctypes.pointer(iso2PowerDemandReqType))

    def init_iso2MinimumPMaxRequestType(self, iso2MinimumPMaxRequestType: iso2MinimumPMaxRequestType):
        return self.libopenv2g.init_iso2MinimumPMaxRequestType(ctypes.pointer(iso2MinimumPMaxRequestType))

    def init_iso2DisconnectChargingDeviceResType(self, iso2DisconnectChargingDeviceResType: iso2DisconnectChargingDeviceResType):
        return self.libopenv2g.init_iso2DisconnectChargingDeviceResType(ctypes.pointer(iso2DisconnectChargingDeviceResType))

    def init_iso2SessionSetupReqType(self, iso2SessionSetupReqType: iso2SessionSetupReqType):
        return self.libopenv2g.init_iso2SessionSetupReqType(ctypes.pointer(iso2SessionSetupReqType))

    def init_iso2PaymentDetailsReqType(self, iso2PaymentDetailsReqType: iso2PaymentDetailsReqType):
        return self.libopenv2g.init_iso2PaymentDetailsReqType(ctypes.pointer(iso2PaymentDetailsReqType))

    def init_iso2Generic_EVFinePositioningParametersType(self, iso2Generic_EVFinePositioningParametersType: iso2Generic_EVFinePositioningParametersType):
        return self.libopenv2g.init_iso2Generic_EVFinePositioningParametersType(ctypes.pointer(iso2Generic_EVFinePositioningParametersType))

    def init_iso2ConnectChargingDeviceReqType(self, iso2ConnectChargingDeviceReqType: iso2ConnectChargingDeviceReqType):
        return self.libopenv2g.init_iso2ConnectChargingDeviceReqType(ctypes.pointer(iso2ConnectChargingDeviceReqType))

    def init_iso2AC_EVSEChargeParameterType(self, iso2AC_EVSEChargeParameterType: iso2AC_EVSEChargeParameterType):
        return self.libopenv2g.init_iso2AC_EVSEChargeParameterType(ctypes.pointer(iso2AC_EVSEChargeParameterType))

    def init_iso2SalesTariffEntryType(self, iso2SalesTariffEntryType: iso2SalesTariffEntryType):
        return self.libopenv2g.init_iso2SalesTariffEntryType(ctypes.pointer(iso2SalesTariffEntryType))

    def init_iso2DC_EVSEBidirectionalParameterType(self, iso2DC_EVSEBidirectionalParameterType: iso2DC_EVSEBidirectionalParameterType):
        return self.libopenv2g.init_iso2DC_EVSEBidirectionalParameterType(ctypes.pointer(iso2DC_EVSEBidirectionalParameterType))

    def init_iso2CanonicalizationMethodType(self, iso2CanonicalizationMethodType: iso2CanonicalizationMethodType):
        return self.libopenv2g.init_iso2CanonicalizationMethodType(ctypes.pointer(iso2CanonicalizationMethodType))

    def init_iso2DisplayParametersType(self, iso2DisplayParametersType: iso2DisplayParametersType):
        return self.libopenv2g.init_iso2DisplayParametersType(ctypes.pointer(iso2DisplayParametersType))

    def init_iso2DC_EVBidirectionalParameterType(self, iso2DC_EVBidirectionalParameterType: iso2DC_EVBidirectionalParameterType):
        return self.libopenv2g.init_iso2DC_EVBidirectionalParameterType(ctypes.pointer(iso2DC_EVBidirectionalParameterType))

    def init_iso2PaymentServiceSelectionReqType(self, iso2PaymentServiceSelectionReqType: iso2PaymentServiceSelectionReqType):
        return self.libopenv2g.init_iso2PaymentServiceSelectionReqType(ctypes.pointer(iso2PaymentServiceSelectionReqType))

    def init_iso2MagneticVectorType(self, iso2MagneticVectorType: iso2MagneticVectorType):
        return self.libopenv2g.init_iso2MagneticVectorType(ctypes.pointer(iso2MagneticVectorType))

    def init_iso2PhysicalValueType(self, iso2PhysicalValueType: iso2PhysicalValueType):
        return self.libopenv2g.init_iso2PhysicalValueType(ctypes.pointer(iso2PhysicalValueType))

    def init_iso2SystemStatusReqType(self, iso2SystemStatusReqType: iso2SystemStatusReqType):
        return self.libopenv2g.init_iso2SystemStatusReqType(ctypes.pointer(iso2SystemStatusReqType))

    def init_iso2SystemStatusResType(self, iso2SystemStatusResType: iso2SystemStatusResType):
        return self.libopenv2g.init_iso2SystemStatusResType(ctypes.pointer(iso2SystemStatusResType))

    def init_iso2EVSEFinePositioningSetupParametersType(self, iso2EVSEFinePositioningSetupParametersType: iso2EVSEFinePositioningSetupParametersType):
        return self.libopenv2g.init_iso2EVSEFinePositioningSetupParametersType(ctypes.pointer(iso2EVSEFinePositioningSetupParametersType))

    def init_iso2V2GResponseType(self, iso2V2GResponseType: iso2V2GResponseType):
        return self.libopenv2g.init_iso2V2GResponseType(ctypes.pointer(iso2V2GResponseType))

    def init_iso2BodyType(self, iso2BodyType: iso2BodyType):
        return self.libopenv2g.init_iso2BodyType(ctypes.pointer(iso2BodyType))

    def init_iso2PreChargeResType(self, iso2PreChargeResType: iso2PreChargeResType):
        return self.libopenv2g.init_iso2PreChargeResType(ctypes.pointer(iso2PreChargeResType))

    def init_iso2EVSEFinePositioningParametersType(self, iso2EVSEFinePositioningParametersType: iso2EVSEFinePositioningParametersType):
        return self.libopenv2g.init_iso2EVSEFinePositioningParametersType(ctypes.pointer(iso2EVSEFinePositioningParametersType))

    def init_iso2PaymentServiceSelectionResType(self, iso2PaymentServiceSelectionResType: iso2PaymentServiceSelectionResType):
        return self.libopenv2g.init_iso2PaymentServiceSelectionResType(ctypes.pointer(iso2PaymentServiceSelectionResType))

    def init_iso2DigestMethodType(self, iso2DigestMethodType: iso2DigestMethodType):
        return self.libopenv2g.init_iso2DigestMethodType(ctypes.pointer(iso2DigestMethodType))

    def init_iso2TargetPositionType(self, iso2TargetPositionType: iso2TargetPositionType):
        return self.libopenv2g.init_iso2TargetPositionType(ctypes.pointer(iso2TargetPositionType))

    def init_iso2LFA_EVFinePositioningParametersType(self, iso2LFA_EVFinePositioningParametersType: iso2LFA_EVFinePositioningParametersType):
        return self.libopenv2g.init_iso2LFA_EVFinePositioningParametersType(ctypes.pointer(iso2LFA_EVFinePositioningParametersType))

    def init_iso2DC_EVChargeParameterType(self, iso2DC_EVChargeParameterType: iso2DC_EVChargeParameterType):
        return self.libopenv2g.init_iso2DC_EVChargeParameterType(ctypes.pointer(iso2DC_EVChargeParameterType))

    def init_iso2ServiceDetailReqType(self, iso2ServiceDetailReqType: iso2ServiceDetailReqType):
        return self.libopenv2g.init_iso2ServiceDetailReqType(ctypes.pointer(iso2ServiceDetailReqType))

    def init_iso2PreChargeReqType(self, iso2PreChargeReqType: iso2PreChargeReqType):
        return self.libopenv2g.init_iso2PreChargeReqType(ctypes.pointer(iso2PreChargeReqType))

    def init_iso2ManifestType(self, iso2ManifestType: iso2ManifestType):
        return self.libopenv2g.init_iso2ManifestType(ctypes.pointer(iso2ManifestType))

    def init_iso2AnonType_V2G_Message(self, iso2AnonType_V2G_Message: iso2AnonType_V2G_Message):
        return self.libopenv2g.init_iso2AnonType_V2G_Message(ctypes.pointer(iso2AnonType_V2G_Message))

    def init_iso2SelectedServiceListType(self, iso2SelectedServiceListType: iso2SelectedServiceListType):
        return self.libopenv2g.init_iso2SelectedServiceListType(ctypes.pointer(iso2SelectedServiceListType))

    def init_iso2Generic_EVSEFinePositioningParametersType(self, iso2Generic_EVSEFinePositioningParametersType: iso2Generic_EVSEFinePositioningParametersType):
        return self.libopenv2g.init_iso2Generic_EVSEFinePositioningParametersType(ctypes.pointer(iso2Generic_EVSEFinePositioningParametersType))

    def init_iso2CartesianCoordinatesType(self, iso2CartesianCoordinatesType: iso2CartesianCoordinatesType):
        return self.libopenv2g.init_iso2CartesianCoordinatesType(ctypes.pointer(iso2CartesianCoordinatesType))

    def init_iso2KeyInfoType(self, iso2KeyInfoType: iso2KeyInfoType):
        return self.libopenv2g.init_iso2KeyInfoType(ctypes.pointer(iso2KeyInfoType))

    def init_iso2SubCertificatesType(self, iso2SubCertificatesType: iso2SubCertificatesType):
        return self.libopenv2g.init_iso2SubCertificatesType(ctypes.pointer(iso2SubCertificatesType))

    def init_iso2ListOfRootCertificateIDsType(self, iso2ListOfRootCertificateIDsType: iso2ListOfRootCertificateIDsType):
        return self.libopenv2g.init_iso2ListOfRootCertificateIDsType(ctypes.pointer(iso2ListOfRootCertificateIDsType))

    def init_iso2EVEnergyTransferParameterType(self, iso2EVEnergyTransferParameterType: iso2EVEnergyTransferParameterType):
        return self.libopenv2g.init_iso2EVEnergyTransferParameterType(ctypes.pointer(iso2EVEnergyTransferParameterType))

    def init_iso2ContractSignatureEncryptedPrivateKeyType(self, iso2ContractSignatureEncryptedPrivateKeyType: iso2ContractSignatureEncryptedPrivateKeyType):
        return self.libopenv2g.init_iso2ContractSignatureEncryptedPrivateKeyType(ctypes.pointer(iso2ContractSignatureEncryptedPrivateKeyType))

    def init_iso2MagneticVectorSetupListType(self, iso2MagneticVectorSetupListType: iso2MagneticVectorSetupListType):
        return self.libopenv2g.init_iso2MagneticVectorSetupListType(ctypes.pointer(iso2MagneticVectorSetupListType))

    def init_iso2PairingReqType(self, iso2PairingReqType: iso2PairingReqType):
        return self.libopenv2g.init_iso2PairingReqType(ctypes.pointer(iso2PairingReqType))

    def init_iso2CurrentDemandResType(self, iso2CurrentDemandResType: iso2CurrentDemandResType):
        return self.libopenv2g.init_iso2CurrentDemandResType(ctypes.pointer(iso2CurrentDemandResType))

    def init_iso2X509IssuerSerialType(self, iso2X509IssuerSerialType: iso2X509IssuerSerialType):
        return self.libopenv2g.init_iso2X509IssuerSerialType(ctypes.pointer(iso2X509IssuerSerialType))

    def init_iso2ChargingStatusReqType(self, iso2ChargingStatusReqType: iso2ChargingStatusReqType):
        return self.libopenv2g.init_iso2ChargingStatusReqType(ctypes.pointer(iso2ChargingStatusReqType))

    def init_iso2CertificateInstallationResType(self, iso2CertificateInstallationResType: iso2CertificateInstallationResType):
        return self.libopenv2g.init_iso2CertificateInstallationResType(ctypes.pointer(iso2CertificateInstallationResType))

    def init_iso2SensorPackageType(self, iso2SensorPackageType: iso2SensorPackageType):
        return self.libopenv2g.init_iso2SensorPackageType(ctypes.pointer(iso2SensorPackageType))

    def init_iso2PGPDataType(self, iso2PGPDataType: iso2PGPDataType):
        return self.libopenv2g.init_iso2PGPDataType(ctypes.pointer(iso2PGPDataType))

    def init_iso2ServiceDiscoveryResType(self, iso2ServiceDiscoveryResType: iso2ServiceDiscoveryResType):
        return self.libopenv2g.init_iso2ServiceDiscoveryResType(ctypes.pointer(iso2ServiceDiscoveryResType))

    def init_iso2ServiceIDListType(self, iso2ServiceIDListType: iso2ServiceIDListType):
        return self.libopenv2g.init_iso2ServiceIDListType(ctypes.pointer(iso2ServiceIDListType))

    def init_iso2EVFinePositioningSetupParametersType(self, iso2EVFinePositioningSetupParametersType: iso2EVFinePositioningSetupParametersType):
        return self.libopenv2g.init_iso2EVFinePositioningSetupParametersType(ctypes.pointer(iso2EVFinePositioningSetupParametersType))

    def init_iso2ChargeParameterDiscoveryResType(self, iso2ChargeParameterDiscoveryResType: iso2ChargeParameterDiscoveryResType):
        return self.libopenv2g.init_iso2ChargeParameterDiscoveryResType(ctypes.pointer(iso2ChargeParameterDiscoveryResType))

    def init_iso2PowerDemandResType(self, iso2PowerDemandResType: iso2PowerDemandResType):
        return self.libopenv2g.init_iso2PowerDemandResType(ctypes.pointer(iso2PowerDemandResType))

    def init_iso2ChargingProfileType(self, iso2ChargingProfileType: iso2ChargingProfileType):
        return self.libopenv2g.init_iso2ChargingProfileType(ctypes.pointer(iso2ChargingProfileType))

    def init_iso2FinePositioningReqType(self, iso2FinePositioningReqType: iso2FinePositioningReqType):
        return self.libopenv2g.init_iso2FinePositioningReqType(ctypes.pointer(iso2FinePositioningReqType))

    def init_iso2SalesTariffType(self, iso2SalesTariffType: iso2SalesTariffType):
        return self.libopenv2g.init_iso2SalesTariffType(ctypes.pointer(iso2SalesTariffType))

    def init_iso2SensorType(self, iso2SensorType: iso2SensorType):
        return self.libopenv2g.init_iso2SensorType(ctypes.pointer(iso2SensorType))

    def init_iso2SignatureValueType(self, iso2SignatureValueType: iso2SignatureValueType):
        return self.libopenv2g.init_iso2SignatureValueType(ctypes.pointer(iso2SignatureValueType))

    def init_iso2SignedInfoType(self, iso2SignedInfoType: iso2SignedInfoType):
        return self.libopenv2g.init_iso2SignedInfoType(ctypes.pointer(iso2SignedInfoType))

    def init_iso2PowerDeliveryResType(self, iso2PowerDeliveryResType: iso2PowerDeliveryResType):
        return self.libopenv2g.init_iso2PowerDeliveryResType(ctypes.pointer(iso2PowerDeliveryResType))

    def init_iso2CableCheckReqType(self, iso2CableCheckReqType: iso2CableCheckReqType):
        return self.libopenv2g.init_iso2CableCheckReqType(ctypes.pointer(iso2CableCheckReqType))

    def init_iso2SelectedServiceType(self, iso2SelectedServiceType: iso2SelectedServiceType):
        return self.libopenv2g.init_iso2SelectedServiceType(ctypes.pointer(iso2SelectedServiceType))

    def init_iso2DiffieHellmanPublickeyType(self, iso2DiffieHellmanPublickeyType: iso2DiffieHellmanPublickeyType):
        return self.libopenv2g.init_iso2DiffieHellmanPublickeyType(ctypes.pointer(iso2DiffieHellmanPublickeyType))

    def init_iso2EVSEStatusType(self, iso2EVSEStatusType: iso2EVSEStatusType):
        return self.libopenv2g.init_iso2EVSEStatusType(ctypes.pointer(iso2EVSEStatusType))

    # open_v2g/source/iso2/iso2EXIDatatypesDecoder.h    
    def decode_iso2ExiDocument(self, stream: bitstream_t, exiDoc: iso2EXIDocument):
        return self.libopenv2g.decode_iso2ExiDocument(ctypes.pointer(stream), ctypes.pointer(exiDoc))

    def decode_iso2ExiFragment(self, stream: bitstream_t, exiFrag: iso2EXIFragment):
        return self.libopenv2g.decode_iso2ExiFragment(ctypes.pointer(stream), ctypes.pointer(exiFrag))

    # open_v2g/source/iso2/iso2EXIDatatypesEncoder.h    
    def encode_iso2ExiDocument(self, stream: bitstream_t, exiDoc: iso2EXIDocument):
        return self.libopenv2g.encode_iso2ExiDocument(ctypes.pointer(stream), ctypes.pointer(exiDoc))

    def encode_iso2ExiFragment(self, stream: bitstream_t, exiFrag: iso2EXIFragment):
        return self.libopenv2g.encode_iso2ExiFragment(ctypes.pointer(stream), ctypes.pointer(exiFrag))

    # ---------- transport ---------- #
    # open_v2g/source/transpot/v2gtp.h
    def write_v2gtpHeader(self, outStream: POINTER(c_uint8), outStreamLength: c_uint32, payloadType: c_uint16):
        return self.libopenv2g.write_v2gtpHeader(outStream, outStreamLength, payloadType)

    def read_v2gtpHeader(self, inStream: POINTER(c_uint8), payloadLength: POINTER(c_uint32)):
        return self.libopenv2g.read_v2gtpHeader(inStream, payloadLength)

    # ---------- xmldsig ---------- #
    # open_v2g/source/xmldsig/xmldsigEXIDatatypes.h
    def init_xmldsigEXIDocument(self, exiDoc: xmldsigEXIDocument):
        return self.libopenv2g.init_xmldsigEXIDocument(ctypes.pointer(exiDoc))
        
    def init_xmldsigEXIFragment(self, exiFrag: xmldsigEXIFragment):
        return self.libopenv2g.init_xmldsigEXIFragment(ctypes.pointer(exiFrag))
        
    def init_xmldsigCanonicalizationMethodType(self, xmldsigCanonicalizationMethodType: xmldsigCanonicalizationMethodType):
        return self.libopenv2g.init_xmldsigCanonicalizationMethodType(ctypes.pointer(xmldsigCanonicalizationMethodType))
        
    def init_xmldsigManifestType(self, xmldsigManifestType: xmldsigManifestType):
        return self.libopenv2g.init_xmldsigManifestType(ctypes.pointer(xmldsigManifestType))
        
    def init_xmldsigObjectType(self, xmldsigObjectType: xmldsigObjectType):
        return self.libopenv2g.init_xmldsigObjectType(ctypes.pointer(xmldsigObjectType))
        
    def init_xmldsigTransformType(self, xmldsigTransformType: xmldsigTransformType):
        return self.libopenv2g.init_xmldsigTransformType(ctypes.pointer(xmldsigTransformType))
        
    def init_xmldsigSignatureMethodType(self, xmldsigSignatureMethodType: xmldsigSignatureMethodType):
        return self.libopenv2g.init_xmldsigSignatureMethodType(ctypes.pointer(xmldsigSignatureMethodType))
        
    def init_xmldsigDigestMethodType(self, xmldsigDigestMethodType: xmldsigDigestMethodType):
        return self.libopenv2g.init_xmldsigDigestMethodType(ctypes.pointer(xmldsigDigestMethodType))
        
    def init_xmldsigRetrievalMethodType(self, xmldsigRetrievalMethodType: xmldsigRetrievalMethodType):
        return self.libopenv2g.init_xmldsigRetrievalMethodType(ctypes.pointer(xmldsigRetrievalMethodType))
        
    def init_xmldsigSignatureValueType(self, xmldsigSignatureValueType: xmldsigSignatureValueType):
        return self.libopenv2g.init_xmldsigSignatureValueType(ctypes.pointer(xmldsigSignatureValueType))
        
    def init_xmldsigX509IssuerSerialType(self, xmldsigX509IssuerSerialType: xmldsigX509IssuerSerialType):
        return self.libopenv2g.init_xmldsigX509IssuerSerialType(ctypes.pointer(xmldsigX509IssuerSerialType))
        
    def init_xmldsigSignedInfoType(self, xmldsigSignedInfoType: xmldsigSignedInfoType):
        return self.libopenv2g.init_xmldsigSignedInfoType(ctypes.pointer(xmldsigSignedInfoType))
        
    def init_xmldsigSignaturePropertiesType(self, xmldsigSignaturePropertiesType: xmldsigSignaturePropertiesType):
        return self.libopenv2g.init_xmldsigSignaturePropertiesType(ctypes.pointer(xmldsigSignaturePropertiesType))
        
    def init_xmldsigSignaturePropertyType(self, xmldsigSignaturePropertyType: xmldsigSignaturePropertyType):
        return self.libopenv2g.init_xmldsigSignaturePropertyType(ctypes.pointer(xmldsigSignaturePropertyType))
        
    def init_xmldsigKeyValueType(self, xmldsigKeyValueType: xmldsigKeyValueType):
        return self.libopenv2g.init_xmldsigKeyValueType(ctypes.pointer(xmldsigKeyValueType))
        
    def init_xmldsigRSAKeyValueType(self, xmldsigRSAKeyValueType: xmldsigRSAKeyValueType):
        return self.libopenv2g.init_xmldsigRSAKeyValueType(ctypes.pointer(xmldsigRSAKeyValueType))
        
    def init_xmldsigPGPDataType(self, xmldsigPGPDataType: xmldsigPGPDataType):
        return self.libopenv2g.init_xmldsigPGPDataType(ctypes.pointer(xmldsigPGPDataType))
        
    def init_xmldsigTransformsType(self, xmldsigTransformsType: xmldsigTransformsType):
        return self.libopenv2g.init_xmldsigTransformsType(ctypes.pointer(xmldsigTransformsType))
        
    def init_xmldsigX509DataType(self, xmldsigX509DataType: xmldsigX509DataType):
        return self.libopenv2g.init_xmldsigX509DataType(ctypes.pointer(xmldsigX509DataType))
        
    def init_xmldsigSignatureType(self, xmldsigSignatureType: xmldsigSignatureType):
        return self.libopenv2g.init_xmldsigSignatureType(ctypes.pointer(xmldsigSignatureType))
        
    def init_xmldsigDSAKeyValueType(self, xmldsigDSAKeyValueType: xmldsigDSAKeyValueType):
        return self.libopenv2g.init_xmldsigDSAKeyValueType(ctypes.pointer(xmldsigDSAKeyValueType))
        
    def init_xmldsigReferenceType(self, xmldsigReferenceType: xmldsigReferenceType):
        return self.libopenv2g.init_xmldsigReferenceType(ctypes.pointer(xmldsigReferenceType))
        
    def init_xmldsigSPKIDataType(self, xmldsigSPKIDataType: xmldsigSPKIDataType):
        return self.libopenv2g.init_xmldsigSPKIDataType(ctypes.pointer(xmldsigSPKIDataType))
        
    def init_xmldsigKeyInfoType(self, xmldsigKeyInfoType: xmldsigKeyInfoType):
        return self.libopenv2g.init_xmldsigKeyInfoType(ctypes.pointer(xmldsigKeyInfoType))
        
    # open_v2g/source/xmldsig/xmldsigEXIDatatypesDecoder.h
    def decode_xmldsigExiDocument(self, stream: bitstream_t, exiDoc: xmldsigEXIDocument):
        return self.libopenv2g.decode_xmldsigExiDocument(ctypes.pointer(stream), ctypes.pointer(exiDoc))

    def decode_xmldsigExiFragment(self, stream: bitstream_t, exiFrag: xmldsigEXIFragment):
        return self.libopenv2g.decode_xmldsigExiFragment(ctypes.pointer(stream), ctypes.pointer(exiFrag))

    # open_v2g/source/xmldsig/xmldsigEXIDatatypesEncoder.h
    def encode_xmldsigExiDocument(self, stream: bitstream_t, exiDoc: xmldsigEXIDocument):
        return self.libopenv2g.encode_xmldsigExiDocument(ctypes.pointer(stream), ctypes.pointer(exiDoc))

    def encode_xmldsigExiFragment(self, stream: bitstream_t, exiFrag: xmldsigEXIFragment):
        return self.libopenv2g.encode_xmldsigExiFragment(ctypes.pointer(stream), ctypes.pointer(exiFrag))


    # open_v2g/source/test/main_example.c
    def main_example(self):
        return self.libopenv2g.main_example()