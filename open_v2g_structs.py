
from open_v2g_constants import *
from ctypes import *


def ArrayType_factory(ctype: Structure, ctype_name: str, size: int):
	class ArrayType(Structure):

		_fields_=[

			(ctype_name, ctype*size),

			(ctype_name+"Len", c_uint16)

		]
	return ArrayType

class iso2RSAKeyValueType(Structure):
	_fields_=[
		("Modulus", ArrayType_factory(c_uint8, "bytes", iso2RSAKeyValueType_Modulus_BYTES_SIZE)),

		("Exponent", ArrayType_factory(c_uint8, "bytes", iso2RSAKeyValueType_Exponent_BYTES_SIZE)),
	]


class iso2MeterInfoType(Structure):
	_fields_=[
		("MeterReadingCharged", c_uint64),

		("MeterReadingCharged_isUsed", c_uint, 1),

		("MeterReadingDischarged", c_uint64),

		("MeterReadingDischarged_isUsed", c_uint, 1),

		("SigMeterReading_isUsed", c_uint, 1),

		("MeterStatus", c_int16),

		("MeterStatus_isUsed", c_uint, 1),

		("TMeter", c_int64),

		("TMeter_isUsed", c_uint, 1),

		("MeterID", ArrayType_factory(c_uint32, "characters", iso2MeterInfoType_MeterID_CHARACTERS_SIZE)),

		("SigMeterReading", ArrayType_factory(c_uint8, "bytes", iso2MeterInfoType_SigMeterReading_BYTES_SIZE)),
	]


class iso2ServiceType(Structure):
	_fields_=[
		("ServiceID", c_uint16),

		("FreeService", c_int),
	]


class iso2ServiceListType(Structure):
	_fields_=[
		("array", (iso2ServiceType*iso2ServiceListType_Service_ARRAY_SIZE)),
	]


class iso2MagneticVectorSetupType(Structure):
	_fields_=[
		("FrequencyChannel", c_uint32),

		("GAID", ArrayType_factory(c_uint32, "characters", iso2MagneticVectorSetupType_GAID_CHARACTERS_SIZE)),
	]


class iso2RelativeTimeIntervalType(Structure):
	_fields_=[
		("start", c_uint32),

		("duration", c_uint32),

		("duration_isUsed", c_uint, 1),
	]


class iso2EVFinePositioningParametersType(Structure):
	_fields_=[
		("noContent", c_int),
	]


class iso2ObjectType(Structure):
	_fields_=[
		("Id_isUsed", c_uint, 1),

		("MimeType_isUsed", c_uint, 1),

		("Encoding_isUsed", c_uint, 1),

		("ANY_isUsed", c_uint, 1),

		("Id", ArrayType_factory(c_uint32, "characters", iso2ObjectType_Id_CHARACTERS_SIZE)),

		("MimeType", ArrayType_factory(c_uint32, "characters", iso2ObjectType_MimeType_CHARACTERS_SIZE)),

		("Encoding", ArrayType_factory(c_uint32, "characters", iso2ObjectType_Encoding_CHARACTERS_SIZE)),

		("ANY", ArrayType_factory(c_uint32, "characters", iso2ObjectType_ANY_CHARACTERS_SIZE)),
	]


class iso2SensorOrderListType(Structure):
	_fields_=[
		("SensorPosition", ArrayType_factory(c_uint8, "array", iso2SensorOrderListType_SensorPosition_ARRAY_SIZE)),
	]


class iso2MeasurementDataListType(Structure):
	_fields_=[
		("MeasurementData", ArrayType_factory(c_uint16, "array", iso2MeasurementDataListType_MeasurementData_ARRAY_SIZE)),
	]


class iso2SignaturePropertyType(Structure):
	_fields_=[
		("Id_isUsed", c_uint, 1),

		("ANY_isUsed", c_uint, 1),

		("Target", ArrayType_factory(c_uint32, "characters", iso2SignaturePropertyType_Target_CHARACTERS_SIZE)),

		("Id", ArrayType_factory(c_uint32, "characters", iso2SignaturePropertyType_Id_CHARACTERS_SIZE)),

		("ANY", ArrayType_factory(c_uint32, "characters", iso2SignaturePropertyType_ANY_CHARACTERS_SIZE)),
	]


class iso2TransformType(Structure):
	_fields_=[
		("ANY_isUsed", c_uint, 1),

		("Algorithm", ArrayType_factory(c_uint32, "characters", iso2TransformType_Algorithm_CHARACTERS_SIZE)),

		("ANY", ArrayType_factory(c_uint32, "characters", iso2TransformType_ANY_CHARACTERS_SIZE)),

		("XPath", ArrayType_factory(ArrayType_factory(c_uint32, "characters", iso2TransformType_XPath_CHARACTERS_SIZE), "array", iso2TransformType_XPath_ARRAY_SIZE)),
	]


class iso2EMAIDType(Structure):
	_fields_=[
		("Id", ArrayType_factory(c_uint32, "characters", iso2EMAIDType_Id_CHARACTERS_SIZE)),

		("CONTENT", ArrayType_factory(c_uint32, "characters", iso2EMAIDType_CONTENT_CHARACTERS_SIZE)),
	]


class iso2DSAKeyValueType(Structure):
	_fields_=[
		("P_isUsed", c_uint, 1),

		("Q_isUsed", c_uint, 1),

		("G_isUsed", c_uint, 1),

		("J_isUsed", c_uint, 1),

		("Seed_isUsed", c_uint, 1),

		("PgenCounter_isUsed", c_uint, 1),

		("P", ArrayType_factory(c_uint8, "bytes", iso2DSAKeyValueType_P_BYTES_SIZE)),

		("Q", ArrayType_factory(c_uint8, "bytes", iso2DSAKeyValueType_Q_BYTES_SIZE)),

		("G", ArrayType_factory(c_uint8, "bytes", iso2DSAKeyValueType_G_BYTES_SIZE)),

		("Y", ArrayType_factory(c_uint8, "bytes", iso2DSAKeyValueType_Y_BYTES_SIZE)),

		("J", ArrayType_factory(c_uint8, "bytes", iso2DSAKeyValueType_J_BYTES_SIZE)),

		("Seed", ArrayType_factory(c_uint8, "bytes", iso2DSAKeyValueType_Seed_BYTES_SIZE)),

		("PgenCounter", ArrayType_factory(c_uint8, "bytes", iso2DSAKeyValueType_PgenCounter_BYTES_SIZE)),
	]


class iso2EntryType(Structure):
	_fields_=[
		("RelativeTimeInterval", iso2RelativeTimeIntervalType),
	]


class iso2V2GRequestType(Structure):
	_fields_=[
		("noContent", c_int),
	]


class iso2EVSEEnergyTransferParameterType(Structure):
	_fields_=[
		("noContent", c_int),
	]


class iso2MeteringReceiptReqType(Structure):
	_fields_=[
		("SAScheduleTupleID", c_uint8),

		("SAScheduleTupleID_isUsed", c_uint, 1),

		("MeterInfo", iso2MeterInfoType),

		("Id", ArrayType_factory(c_uint32, "characters", iso2MeteringReceiptReqType_Id_CHARACTERS_SIZE)),

		("SessionID", ArrayType_factory(c_uint8, "bytes", iso2MeteringReceiptReqType_SessionID_BYTES_SIZE)),
	]


class iso2KeyValueType(Structure):
	_fields_=[
		("DSAKeyValue", iso2DSAKeyValueType),

		("DSAKeyValue_isUsed", c_uint, 1),

		("RSAKeyValue", iso2RSAKeyValueType),

		("RSAKeyValue_isUsed", c_uint, 1),

		("ANY_isUsed", c_uint, 1),

		("ANY", ArrayType_factory(c_uint32, "characters", iso2KeyValueType_ANY_CHARACTERS_SIZE)),
	]


class iso2BodyBaseType(Structure):
	_fields_=[
		("noContent", c_int),
	]


class iso2AuthorizationReqType(Structure):
	_fields_=[
		("Id_isUsed", c_uint, 1),

		("GenChallenge_isUsed", c_uint, 1),

		("Id", ArrayType_factory(c_uint32, "characters", iso2AuthorizationReqType_Id_CHARACTERS_SIZE)),

		("GenChallenge", ArrayType_factory(c_uint8, "bytes", iso2AuthorizationReqType_GenChallenge_BYTES_SIZE)),
	]


class iso2SPKIDataType(Structure):
	_fields_=[
		("ANY_isUsed", c_uint, 1),

		("ANY", ArrayType_factory(c_uint32, "characters", iso2SPKIDataType_ANY_CHARACTERS_SIZE)),

		("SPKISexp", ArrayType_factory(ArrayType_factory(c_uint8, "bytes", iso2SPKIDataType_SPKISexp_BYTES_SIZE), "array", iso2SPKIDataType_SPKISexp_ARRAY_SIZE)),
	]


class iso2SignatureMethodType(Structure):
	_fields_=[
		("HMACOutputLength", c_int64),

		("HMACOutputLength_isUsed", c_uint, 1),

		("ANY_isUsed", c_uint, 1),

		("Algorithm", ArrayType_factory(c_uint32, "characters", iso2SignatureMethodType_Algorithm_CHARACTERS_SIZE)),

		("ANY", ArrayType_factory(c_uint32, "characters", iso2SignatureMethodType_ANY_CHARACTERS_SIZE)),
	]


class iso2WeldingDetectionReqType(Structure):
	_fields_=[
		("noContent", c_int),
	]


class iso2SessionSetupReqType(Structure):
	_fields_=[
		("EVCCID", ArrayType_factory(c_uint8, "bytes", iso2SessionSetupReqType_EVCCID_BYTES_SIZE)),
	]


class iso2CanonicalizationMethodType(Structure):
	_fields_=[
		("ANY_isUsed", c_uint, 1),

		("Algorithm", ArrayType_factory(c_uint32, "characters", iso2CanonicalizationMethodType_Algorithm_CHARACTERS_SIZE)),

		("ANY", ArrayType_factory(c_uint32, "characters", iso2CanonicalizationMethodType_ANY_CHARACTERS_SIZE)),
	]


class iso2PhysicalValueType(Structure):
	_fields_=[
		("Exponent", c_int8),

		("Value", c_int16),
	]


class iso2SystemStatusReqType(Structure):
	_fields_=[
		("OperationMode", c_uint),

		("EVMechanicalChargingDeviceStatus", c_uint),
	]


class iso2EVSEFinePositioningSetupParametersType(Structure):
	_fields_=[
		("noContent", c_int),
	]


class iso2EVSEFinePositioningParametersType(Structure):
	_fields_=[
		("noContent", c_int),
	]


class iso2DigestMethodType(Structure):
	_fields_=[
		("ANY_isUsed", c_uint, 1),

		("Algorithm", ArrayType_factory(c_uint32, "characters", iso2DigestMethodType_Algorithm_CHARACTERS_SIZE)),

		("ANY", ArrayType_factory(c_uint32, "characters", iso2DigestMethodType_ANY_CHARACTERS_SIZE)),
	]


class iso2TargetPositionType(Structure):
	_fields_=[
		("TargetOffsetX", c_uint16),

		("TargetOffsetY", c_uint16),
	]


class iso2DC_EVChargeParameterType(Structure):
	_fields_=[
		("DepartureTime", c_uint32),

		("EVMaximumChargePower", iso2PhysicalValueType),

		("EVMaximumChargePower_isUsed", c_uint, 1),

		("EVMinimumChargePower", iso2PhysicalValueType),

		("EVMinimumChargePower_isUsed", c_uint, 1),

		("EVMaximumChargeCurrent", iso2PhysicalValueType),

		("EVMinimumChargeCurrent", iso2PhysicalValueType),

		("EVMaximumVoltage", iso2PhysicalValueType),

		("EVTargetEnergyRequest", iso2PhysicalValueType),

		("EVTargetEnergyRequest_isUsed", c_uint, 1),

		("EVMaximumEnergyRequest", iso2PhysicalValueType),

		("EVMaximumEnergyRequest_isUsed", c_uint, 1),

		("EVMinimumEnergyRequest", iso2PhysicalValueType),

		("EVMinimumEnergyRequest_isUsed", c_uint, 1),

		("CurrentSOC", c_int8),

		("CurrentSOC_isUsed", c_uint, 1),

		("TargetSOC", c_int8),

		("TargetSOC_isUsed", c_uint, 1),

		("BulkSOC", c_int8),

		("BulkSOC_isUsed", c_uint, 1),
	]


class iso2ServiceDetailReqType(Structure):
	_fields_=[
		("ServiceID", c_uint16),
	]


class iso2PreChargeReqType(Structure):
	_fields_=[
		("EVTargetVoltage", iso2PhysicalValueType),

		("EVTargetCurrent", iso2PhysicalValueType),
	]


class iso2CartesianCoordinatesType(Structure):
	_fields_=[
		("XCoordinate", c_int16),

		("YCoordinate", c_int16),

		("ZCoordinate", c_int16),
	]


class iso2SubCertificatesType(Structure):
	_fields_=[
		("Certificate", ArrayType_factory(ArrayType_factory(c_uint8, "bytes", iso2SubCertificatesType_Certificate_BYTES_SIZE), "array", iso2SubCertificatesType_Certificate_ARRAY_SIZE)),
	]


class iso2EVEnergyTransferParameterType(Structure):
	_fields_=[
		("DepartureTime", c_uint32),
	]


class iso2ContractSignatureEncryptedPrivateKeyType(Structure):
	_fields_=[
		("Id", ArrayType_factory(c_uint32, "characters", iso2ContractSignatureEncryptedPrivateKeyType_Id_CHARACTERS_SIZE)),

		("CONTENT", ArrayType_factory(c_uint8, "bytes", iso2ContractSignatureEncryptedPrivateKeyType_CONTENT_BYTES_SIZE)),
	]


class iso2MagneticVectorSetupListType(Structure):
	_fields_=[
		("array", (iso2MagneticVectorSetupType*iso2MagneticVectorSetupListType_MagneticVectorSetup_ARRAY_SIZE)),
	]


class iso2X509IssuerSerialType(Structure):
	_fields_=[
		("X509SerialNumber", c_int64),

		("X509IssuerName", ArrayType_factory(c_uint32, "characters", iso2X509IssuerSerialType_X509IssuerName_CHARACTERS_SIZE)),
	]


class iso2PGPDataType(Structure):
	_fields_=[
		("PGPKeyID_isUsed", c_uint, 1),

		("PGPKeyPacket_isUsed", c_uint, 1),

		("ANY_isUsed", c_uint, 1),

		("PGPKeyID", ArrayType_factory(c_uint8, "bytes", iso2PGPDataType_PGPKeyID_BYTES_SIZE)),

		("PGPKeyPacket", ArrayType_factory(c_uint8, "bytes", iso2PGPDataType_PGPKeyPacket_BYTES_SIZE)),

		("ANY", ArrayType_factory(c_uint32, "characters", iso2PGPDataType_ANY_CHARACTERS_SIZE)),
	]


class iso2ServiceIDListType(Structure):
	_fields_=[
		("ServiceID", ArrayType_factory(c_uint16, "array", iso2ServiceIDListType_ServiceID_ARRAY_SIZE)),
	]


class iso2EVFinePositioningSetupParametersType(Structure):
	_fields_=[
		("noContent", c_int),
	]


class iso2SensorType(Structure):
	_fields_=[
		("SensorID", c_uint8),

		("SensorPosition", iso2CartesianCoordinatesType),

		("SensorOrientation", iso2CartesianCoordinatesType),
	]


class iso2SignatureValueType(Structure):
	_fields_=[
		("Id_isUsed", c_uint, 1),

		("Id", ArrayType_factory(c_uint32, "characters", iso2SignatureValueType_Id_CHARACTERS_SIZE)),

		("CONTENT", ArrayType_factory(c_uint8, "bytes", iso2SignatureValueType_CONTENT_BYTES_SIZE)),
	]


class iso2CableCheckReqType(Structure):
	_fields_=[
		("noContent", c_int),
	]


class iso2SelectedServiceType(Structure):
	_fields_=[
		("ServiceID", c_uint16),

		("ParameterSetID", c_uint16),
	]


class iso2DiffieHellmanPublickeyType(Structure):
	_fields_=[
		("Id", ArrayType_factory(c_uint32, "characters", iso2DiffieHellmanPublickeyType_Id_CHARACTERS_SIZE)),

		("CONTENT", ArrayType_factory(c_uint8, "bytes", iso2DiffieHellmanPublickeyType_CONTENT_BYTES_SIZE)),
	]


class iso2EVSEStatusType(Structure):
	_fields_=[
		("NotificationMaxDelay", c_uint16),

		("EVSENotification", c_uint),
	]


class iso2AuthorizationResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),

		("EVSEStatus", iso2EVSEStatusType),

		("EVSEStatus_isUsed", c_uint, 1),

		("EVSEProcessing", c_uint),
	]


class iso2MV_EVSEFinePositioningSetupParametersType(Structure):
	_fields_=[
		("FrequencyChannel", c_uint32),

		("FrequencyChannel_isUsed", c_uint, 1),

		("MagneticVectorSetupList", iso2MagneticVectorSetupListType),

		("MagneticVectorSetupList_isUsed", c_uint, 1),
	]


class iso2X509DataType(Structure):
	_fields_=[
		("ANY_isUsed", c_uint, 1),

		("array", (iso2X509IssuerSerialType*iso2X509DataType_X509IssuerSerial_ARRAY_SIZE)),

		("ANY", ArrayType_factory(c_uint32, "characters", iso2X509DataType_ANY_CHARACTERS_SIZE)),

		("X509SKI", ArrayType_factory(ArrayType_factory(c_uint8, "bytes", iso2X509DataType_X509SKI_BYTES_SIZE), "array", iso2X509DataType_X509SKI_ARRAY_SIZE)),

		("X509SubjectName", ArrayType_factory(ArrayType_factory(c_uint32, "characters", iso2X509DataType_X509SubjectName_CHARACTERS_SIZE), "array", iso2X509DataType_X509SubjectName_ARRAY_SIZE)),

		("X509Certificate", ArrayType_factory(ArrayType_factory(c_uint8, "bytes", iso2X509DataType_X509Certificate_BYTES_SIZE), "array", iso2X509DataType_X509Certificate_ARRAY_SIZE)),

		("X509CRL", ArrayType_factory(ArrayType_factory(c_uint8, "bytes", iso2X509DataType_X509CRL_BYTES_SIZE), "array", iso2X509DataType_X509CRL_ARRAY_SIZE)),
	]


class iso2DC_BidirectionalControlResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),

		("EVSEStatus", iso2EVSEStatusType),

		("EVSEStatus_isUsed", c_uint, 1),

		("EVSEPresentCurrent", iso2PhysicalValueType),

		("EVSEPresentVoltage", iso2PhysicalValueType),

		("EVSEPowerLimitAchieved", c_int),

		("EVSECurrentLimitAchieved", c_int),

		("EVSEVoltageLimitAchieved", c_int),

		("EVSEMaximumChargePower", iso2PhysicalValueType),

		("EVSEMaximumChargePower_isUsed", c_uint, 1),

		("EVSEMaximumDischargePower", iso2PhysicalValueType),

		("EVSEMaximumDischargePower_isUsed", c_uint, 1),

		("EVSEMaximumChargeCurrent", iso2PhysicalValueType),

		("EVSEMaximumChargeCurrent_isUsed", c_uint, 1),

		("EVSEMaximumDischargeCurrent", iso2PhysicalValueType),

		("EVSEMaximumDischargeCurrent_isUsed", c_uint, 1),

		("EVSEMaximumVoltage", iso2PhysicalValueType),

		("EVSEMaximumVoltage_isUsed", c_uint, 1),

		("EVSEMinimumVoltage", iso2PhysicalValueType),

		("EVSEMinimumVoltage_isUsed", c_uint, 1),

		("SAScheduleTupleID", c_uint8),

		("SAScheduleTupleID_isUsed", c_uint, 1),

		("MeterInfo", iso2MeterInfoType),

		("MeterInfo_isUsed", c_uint, 1),

		("ReceiptRequired", c_int),

		("ReceiptRequired_isUsed", c_uint, 1),

		("EVSEID", ArrayType_factory(c_uint32, "characters", iso2DC_BidirectionalControlResType_EVSEID_CHARACTERS_SIZE)),
	]


class iso2CostType(Structure):
	_fields_=[
		("costKind", c_uint),

		("amount", iso2PhysicalValueType),
	]


class iso2ChargingStatusResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),

		("EVSEStatus", iso2EVSEStatusType),

		("EVSEStatus_isUsed", c_uint, 1),

		("SAScheduleTupleID", c_uint8),

		("SAScheduleTupleID_isUsed", c_uint, 1),

		("MeterInfo", iso2MeterInfoType),

		("MeterInfo_isUsed", c_uint, 1),

		("ReceiptRequired", c_int),

		("ReceiptRequired_isUsed", c_uint, 1),

		("EVSETargetPower", iso2PhysicalValueType),

		("EVSETargetPower_isUsed", c_uint, 1),

		("EVSEID", ArrayType_factory(c_uint32, "characters", iso2ChargingStatusResType_EVSEID_CHARACTERS_SIZE)),
	]


class iso2AC_EVChargeParameterType(Structure):
	_fields_=[
		("DepartureTime", c_uint32),

		("EVMaximumChargePower", iso2PhysicalValueType),

		("EVMaximumChargeCurrent", iso2PhysicalValueType),

		("EVMinimumChargeCurrent", iso2PhysicalValueType),

		("EVTargetEnergyRequest", iso2PhysicalValueType),

		("EVTargetEnergyRequest_isUsed", c_uint, 1),

		("EVMaximumEnergyRequest", iso2PhysicalValueType),

		("EVMaximumEnergyRequest_isUsed", c_uint, 1),

		("EVMinimumEnergyRequest", iso2PhysicalValueType),

		("EVMinimumEnergyRequest_isUsed", c_uint, 1),

		("EVMaximumVoltage", iso2PhysicalValueType),
	]


class iso2AC_EVSEBidirectionalParameterType(Structure):
	_fields_=[
		("EVSEMaximumChargeCurrent", iso2PhysicalValueType),

		("EVSENominalVoltage", iso2PhysicalValueType),

		("EVSENominalFrequency", iso2PhysicalValueType),

		("EVSEMaximumDischargeCurrent", iso2PhysicalValueType),
	]


class iso2VehicleCheckOutResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),

		("EVSEStatus", iso2EVSEStatusType),

		("EVSEStatus_isUsed", c_uint, 1),

		("EVSECheckOutStatus", c_uint),
	]


class iso2CableCheckResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),

		("EVSEStatus", iso2EVSEStatusType),

		("EVSEStatus_isUsed", c_uint, 1),

		("EVSEProcessing", c_uint),
	]


class iso2ServiceDiscoveryReqType(Structure):
	_fields_=[
		("SupportedServiceIDs", iso2ServiceIDListType),

		("SupportedServiceIDs_isUsed", c_uint, 1),
	]


class iso2SignaturePropertiesType(Structure):
	_fields_=[
		("Id_isUsed", c_uint, 1),

		("Id", ArrayType_factory(c_uint32, "characters", iso2SignaturePropertiesType_Id_CHARACTERS_SIZE)),

		("array", (iso2SignaturePropertyType*iso2SignaturePropertiesType_SignatureProperty_ARRAY_SIZE)),
	]


class iso2PMaxScheduleEntryType(Structure):
	_fields_=[
		("RelativeTimeInterval", iso2RelativeTimeIntervalType),

		("array", (iso2PhysicalValueType*iso2PMaxScheduleEntryType_PMax_ARRAY_SIZE)),
	]


class iso2VehicleCheckInReqType(Structure):
	_fields_=[
		("EVCheckInStatus", c_uint),

		("ParkingMethod", c_uint),

		("ParkingMethod_isUsed", c_uint, 1),
	]


class iso2ConnectChargingDeviceResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),

		("EVSEStatus", iso2EVSEStatusType),

		("EVSEStatus_isUsed", c_uint, 1),

		("EVSEProcessing", c_uint),

		("EVSEElectricalChargingDeviceStatus", c_uint),

		("EVSEMechanicalChargingDeviceStatus", c_uint),
	]


class iso2WeldingDetectionResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),

		("EVSEStatus", iso2EVSEStatusType),

		("EVSEStatus_isUsed", c_uint, 1),

		("EVSEPresentVoltage", iso2PhysicalValueType),
	]


class iso2SessionStopResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),

		("EVSEStatus", iso2EVSEStatusType),

		("EVSEStatus_isUsed", c_uint, 1),
	]


class iso2VehicleCheckInResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),

		("EVSEStatus", iso2EVSEStatusType),

		("EVSEStatus_isUsed", c_uint, 1),

		("VehicleSpace", c_uint16),

		("TargetOffset", iso2TargetPositionType),

		("TargetOffset_isUsed", c_uint, 1),
	]


class iso2AC_EVBidirectionalParameterType(Structure):
	_fields_=[
		("DepartureTime", c_uint32),

		("EVMaximumChargePower", iso2PhysicalValueType),

		("EVMaximumChargeCurrent", iso2PhysicalValueType),

		("EVMinimumChargeCurrent", iso2PhysicalValueType),

		("EVTargetEnergyRequest", iso2PhysicalValueType),

		("EVTargetEnergyRequest_isUsed", c_uint, 1),

		("EVMaximumEnergyRequest", iso2PhysicalValueType),

		("EVMaximumEnergyRequest_isUsed", c_uint, 1),

		("EVMinimumEnergyRequest", iso2PhysicalValueType),

		("EVMinimumEnergyRequest_isUsed", c_uint, 1),

		("EVMaximumVoltage", iso2PhysicalValueType),

		("EVMaximumDischargePower", iso2PhysicalValueType),

		("EVMaximumDischargeCurrent", iso2PhysicalValueType),

		("EVMinimumDischargeCurrent", iso2PhysicalValueType),
	]


class iso2ConsumptionCostType(Structure):
	_fields_=[
		("startValue", iso2PhysicalValueType),

		("array", (iso2CostType*iso2ConsumptionCostType_Cost_ARRAY_SIZE)),
	]


class iso2PaymentOptionListType(Structure):
	_fields_=[
		("PaymentOption", ArrayType_factory(c_uint32, "array", iso2PaymentOptionListType_PaymentOption_ARRAY_SIZE)),
	]


class iso2TransformsType(Structure):
	_fields_=[
		("array", (iso2TransformType*iso2TransformsType_Transform_ARRAY_SIZE)),
	]


class iso2ParameterType(Structure):
	_fields_=[
		("boolValue", c_int),

		("boolValue_isUsed", c_uint, 1),

		("byteValue", c_int8),

		("byteValue_isUsed", c_uint, 1),

		("shortValue", c_int16),

		("shortValue_isUsed", c_uint, 1),

		("intValue", c_int32),

		("intValue_isUsed", c_uint, 1),

		("physicalValue", iso2PhysicalValueType),

		("physicalValue_isUsed", c_uint, 1),

		("stringValue_isUsed", c_uint, 1),

		("Name", ArrayType_factory(c_uint32, "characters", iso2ParameterType_Name_CHARACTERS_SIZE)),

		("stringValue", ArrayType_factory(c_uint32, "characters", iso2ParameterType_stringValue_CHARACTERS_SIZE)),
	]


class iso2SessionStopReqType(Structure):
	_fields_=[
		("ChargingSession", c_uint),
	]


class iso2SensorMeasurementsType(Structure):
	_fields_=[
		("SensorID", c_uint8),

		("EffectiveRadiatedPower", c_int8),

		("MeasurementDataList", iso2MeasurementDataListType),
	]


class iso2DC_EVSEChargeParameterType(Structure):
	_fields_=[
		("EVSEMaximumChargePower", iso2PhysicalValueType),

		("EVSEMaximumChargeCurrent", iso2PhysicalValueType),

		("EVSEMinimumChargeCurrent", iso2PhysicalValueType),

		("EVSEMaximumVoltage", iso2PhysicalValueType),

		("EVSEMinimumVoltage", iso2PhysicalValueType),

		("EVSECurrentRegulationTolerance", iso2PhysicalValueType),

		("EVSECurrentRegulationTolerance_isUsed", c_uint, 1),

		("EVSEPeakCurrentRipple", iso2PhysicalValueType),

		("EVSEEnergyToBeDelivered", iso2PhysicalValueType),

		("EVSEEnergyToBeDelivered_isUsed", c_uint, 1),
	]


class iso2CertificateChainType(Structure):
	_fields_=[
		("Id_isUsed", c_uint, 1),

		("SubCertificates", iso2SubCertificatesType),

		("SubCertificates_isUsed", c_uint, 1),

		("Id", ArrayType_factory(c_uint32, "characters", iso2CertificateChainType_Id_CHARACTERS_SIZE)),

		("Certificate", ArrayType_factory(c_uint8, "bytes", iso2CertificateChainType_Certificate_BYTES_SIZE)),
	]


class iso2WPT_EVChargeParameterType(Structure):
	_fields_=[
		("DepartureTime", c_uint32),

		("EVMaximumPower", iso2PhysicalValueType),

		("EVMinimumPower", iso2PhysicalValueType),

		("EVTargetEnergyRequest", iso2PhysicalValueType),

		("EVTargetEnergyRequest_isUsed", c_uint, 1),

		("EVMaximumEnergyRequest", iso2PhysicalValueType),

		("EVMaximumEnergyRequest_isUsed", c_uint, 1),

		("EVMinimumEnergyRequest", iso2PhysicalValueType),

		("EVMinimumEnergyRequest_isUsed", c_uint, 1),
	]


class iso2DisconnectChargingDeviceReqType(Structure):
	_fields_=[
		("EVElectricalChargingDeviceStatus", c_uint),

		("EVMechanicalChargingDeviceStatus", c_uint),
	]


class iso2MeteringReceiptResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),

		("EVSEStatus", iso2EVSEStatusType),

		("EVSEStatus_isUsed", c_uint, 1),
	]


class iso2SessionSetupResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),

		("EVSEStatus", iso2EVSEStatusType),

		("EVSEStatus_isUsed", c_uint, 1),

		("EVSETimeStamp", c_int64),

		("EVSETimeStamp_isUsed", c_uint, 1),

		("EVSEID", ArrayType_factory(c_uint32, "characters", iso2SessionSetupResType_EVSEID_CHARACTERS_SIZE)),
	]


class iso2ReferenceType(Structure):
	_fields_=[
		("Id_isUsed", c_uint, 1),

		("URI_isUsed", c_uint, 1),

		("Type_isUsed", c_uint, 1),

		("Transforms", iso2TransformsType),

		("Transforms_isUsed", c_uint, 1),

		("DigestMethod", iso2DigestMethodType),

		("Id", ArrayType_factory(c_uint32, "characters", iso2ReferenceType_Id_CHARACTERS_SIZE)),

		("URI", ArrayType_factory(c_uint32, "characters", iso2ReferenceType_URI_CHARACTERS_SIZE)),

		("Type", ArrayType_factory(c_uint32, "characters", iso2ReferenceType_Type_CHARACTERS_SIZE)),

		("DigestValue", ArrayType_factory(c_uint8, "bytes", iso2ReferenceType_DigestValue_BYTES_SIZE)),
	]


class iso2SensorListType(Structure):
	_fields_=[
		("array", (iso2SensorType*iso2SensorListType_Sensor_ARRAY_SIZE)),
	]


class iso2LFA_EVFinePositioningSetupParametersType(Structure):
	_fields_=[
		("NumberOfSensors", c_uint8),

		("SensorList", iso2SensorListType),

		("SensorOrder", iso2SensorOrderListType),

		("SignalPulseDuration", c_uint8),

		("SignalSeparationTime", c_uint8),

		("PackageSeparationTime", c_uint8),

		("AlignmentOffset", c_uint16),
	]


class iso2WPT_EVSEChargeParameterType(Structure):
	_fields_=[
		("EVSEMaximumPower", iso2PhysicalValueType),

		("EVSEMinimumPower", iso2PhysicalValueType),
	]


class iso2ParameterSetType(Structure):
	_fields_=[
		("ParameterSetID", c_uint16),

		("array", (iso2ParameterType*iso2ParameterSetType_Parameter_ARRAY_SIZE)),
	]


class iso2PaymentDetailsResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),

		("EVSEStatus", iso2EVSEStatusType),

		("EVSEStatus_isUsed", c_uint, 1),

		("EVSETimeStamp", c_int64),

		("GenChallenge", ArrayType_factory(c_uint8, "bytes", iso2PaymentDetailsResType_GenChallenge_BYTES_SIZE)),
	]


class iso2AC_BidirectionalControlResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),

		("EVSEStatus", iso2EVSEStatusType),

		("EVSEStatus_isUsed", c_uint, 1),

		("EVSEProcessing", c_uint),

		("EVSETargetPower", iso2PhysicalValueType),

		("EVSETargetReactivePower", iso2PhysicalValueType),

		("SAScheduleTupleID", c_uint8),

		("SAScheduleTupleID_isUsed", c_uint, 1),

		("MeterInfo", iso2MeterInfoType),

		("MeterInfo_isUsed", c_uint, 1),

		("ReceiptRequired", c_int),

		("ReceiptRequired_isUsed", c_uint, 1),

		("EVSEID", ArrayType_factory(c_uint32, "characters", iso2AC_BidirectionalControlResType_EVSEID_CHARACTERS_SIZE)),
	]


class iso2VehicleCheckOutReqType(Structure):
	_fields_=[
		("EVCheckOutStatus", c_uint),

		("CheckOutTime", c_uint64),
	]


class iso2AlignmentCheckResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),

		("EVSEStatus", iso2EVSEStatusType),

		("EVSEStatus_isUsed", c_uint, 1),

		("EVSEProcessing", c_uint),

		("AlignmentCheckParameters", iso2ParameterSetType),

		("AlignmentCheckParameters_isUsed", c_uint, 1),
	]


class iso2MinimumPMaxRequestType(Structure):
	_fields_=[
		("array", (iso2PMaxScheduleEntryType*iso2MinimumPMaxRequestType_MinimumPMaxScheduleEntry_ARRAY_SIZE)),
	]


class iso2DisconnectChargingDeviceResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),

		("EVSEStatus", iso2EVSEStatusType),

		("EVSEStatus_isUsed", c_uint, 1),

		("EVSEProcessing", c_uint),

		("EVSEElectricalChargingDeviceStatus", c_uint),

		("EVSEMechanicalChargingDeviceStatus", c_uint),
	]


class iso2PaymentDetailsReqType(Structure):
	_fields_=[
		("ContractSignatureCertChain", iso2CertificateChainType),

		("eMAID", ArrayType_factory(c_uint32, "characters", iso2PaymentDetailsReqType_eMAID_CHARACTERS_SIZE)),
	]


class iso2Generic_EVFinePositioningParametersType(Structure):
	_fields_=[
		("GenericParameters", iso2ParameterSetType),
	]


class iso2ConnectChargingDeviceReqType(Structure):
	_fields_=[
		("EVElectricalChargingDeviceStatus", c_uint),

		("EVMechanicalChargingDeviceStatus", c_uint),
	]


class iso2AC_EVSEChargeParameterType(Structure):
	_fields_=[
		("EVSEMaximumChargeCurrent", iso2PhysicalValueType),

		("EVSENominalVoltage", iso2PhysicalValueType),

		("EVSENominalFrequency", iso2PhysicalValueType),
	]


class iso2SalesTariffEntryType(Structure):
	_fields_=[
		("RelativeTimeInterval", iso2RelativeTimeIntervalType),

		("EPriceLevel", c_uint8),

		("EPriceLevel_isUsed", c_uint, 1),

		("array", (iso2ConsumptionCostType*iso2SalesTariffEntryType_ConsumptionCost_ARRAY_SIZE)),
	]


class iso2DC_EVSEBidirectionalParameterType(Structure):
	_fields_=[
		("EVSEMaximumChargePower", iso2PhysicalValueType),

		("EVSEMaximumChargeCurrent", iso2PhysicalValueType),

		("EVSEMinimumChargeCurrent", iso2PhysicalValueType),

		("EVSEMaximumVoltage", iso2PhysicalValueType),

		("EVSEMinimumVoltage", iso2PhysicalValueType),

		("EVSECurrentRegulationTolerance", iso2PhysicalValueType),

		("EVSECurrentRegulationTolerance_isUsed", c_uint, 1),

		("EVSEPeakCurrentRipple", iso2PhysicalValueType),

		("EVSEEnergyToBeDelivered", iso2PhysicalValueType),

		("EVSEEnergyToBeDelivered_isUsed", c_uint, 1),

		("EVSEMaximumDischargePower", iso2PhysicalValueType),

		("EVSEMaximumDischargeCurrent", iso2PhysicalValueType),

		("EVSEMinimumDischargeCurrent", iso2PhysicalValueType),
	]


class iso2DisplayParametersType(Structure):
	_fields_=[
		("CurrentRange", c_uint16),

		("CurrentRange_isUsed", c_uint, 1),

		("CurrentSOC", c_int8),

		("CurrentSOC_isUsed", c_uint, 1),

		("TargetSOC", c_int8),

		("TargetSOC_isUsed", c_uint, 1),

		("BulkSOC", c_int8),

		("BulkSOC_isUsed", c_uint, 1),

		("MinimumSOC", c_int8),

		("MinimumSOC_isUsed", c_uint, 1),

		("ChargingPerformance", iso2PhysicalValueType),

		("ChargingPerformance_isUsed", c_uint, 1),

		("RemainingTimeToTargetSOC", c_int8),

		("RemainingTimeToTargetSOC_isUsed", c_uint, 1),

		("RemainingTimeToBulkSOC", c_int8),

		("RemainingTimeToBulkSOC_isUsed", c_uint, 1),

		("RemainingTimeToMinimumSOC", c_int8),

		("RemainingTimeToMinimumSOC_isUsed", c_uint, 1),

		("ChargingComplete", c_int),

		("ChargingComplete_isUsed", c_uint, 1),

		("BulkChargingComplete", c_int),

		("BulkChargingComplete_isUsed", c_uint, 1),

		("InletHot", c_int),

		("InletHot_isUsed", c_uint, 1),
	]


class iso2DC_EVBidirectionalParameterType(Structure):
	_fields_=[
		("DepartureTime", c_uint32),

		("EVMaximumChargePower", iso2PhysicalValueType),

		("EVMaximumChargePower_isUsed", c_uint, 1),

		("EVMinimumChargePower", iso2PhysicalValueType),

		("EVMinimumChargePower_isUsed", c_uint, 1),

		("EVMaximumChargeCurrent", iso2PhysicalValueType),

		("EVMinimumChargeCurrent", iso2PhysicalValueType),

		("EVMaximumVoltage", iso2PhysicalValueType),

		("EVTargetEnergyRequest", iso2PhysicalValueType),

		("EVTargetEnergyRequest_isUsed", c_uint, 1),

		("EVMaximumEnergyRequest", iso2PhysicalValueType),

		("EVMaximumEnergyRequest_isUsed", c_uint, 1),

		("EVMinimumEnergyRequest", iso2PhysicalValueType),

		("EVMinimumEnergyRequest_isUsed", c_uint, 1),

		("CurrentSOC", c_int8),

		("CurrentSOC_isUsed", c_uint, 1),

		("TargetSOC", c_int8),

		("TargetSOC_isUsed", c_uint, 1),

		("BulkSOC", c_int8),

		("BulkSOC_isUsed", c_uint, 1),

		("EVMaximumDischargePower", iso2PhysicalValueType),

		("EVMaximumDischargePower_isUsed", c_uint, 1),

		("EVMinimumDischargePower", iso2PhysicalValueType),

		("EVMinimumDischargePower_isUsed", c_uint, 1),

		("EVMaximumDischargeCurrent", iso2PhysicalValueType),

		("EVMinimumDischargeCurrent", iso2PhysicalValueType),

		("EVMinimumVoltage", iso2PhysicalValueType),

		("MinimumSOC", c_int8),

		("MinimumSOC_isUsed", c_uint, 1),
	]


class iso2MagneticVectorType(Structure):
	_fields_=[
		("Distance", c_uint16),

		("AngleGAtoVA", iso2PhysicalValueType),

		("RotationVAtoGA", iso2PhysicalValueType),

		("FODStatus", c_uint),

		("GAID", ArrayType_factory(c_uint32, "characters", iso2MagneticVectorType_GAID_CHARACTERS_SIZE)),
	]


class iso2SystemStatusResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),

		("EVSEStatus", iso2EVSEStatusType),

		("EVSEStatus_isUsed", c_uint, 1),

		("OperationMode", c_uint),

		("EVSEMechanicalChargingDeviceStatus", c_uint),
	]


class iso2V2GResponseType(Structure):
	_fields_=[
		("ResponseCode", c_uint),

		("EVSEStatus", iso2EVSEStatusType),

		("EVSEStatus_isUsed", c_uint, 1),
	]


class iso2PreChargeResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),

		("EVSEStatus", iso2EVSEStatusType),

		("EVSEStatus_isUsed", c_uint, 1),

		("EVSEPresentVoltage", iso2PhysicalValueType),
	]


class iso2PaymentServiceSelectionResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),

		("EVSEStatus", iso2EVSEStatusType),

		("EVSEStatus_isUsed", c_uint, 1),
	]


class iso2ManifestType(Structure):
	_fields_=[
		("Id_isUsed", c_uint, 1),

		("Id", ArrayType_factory(c_uint32, "characters", iso2ManifestType_Id_CHARACTERS_SIZE)),

		("array", (iso2ReferenceType*iso2ManifestType_Reference_ARRAY_SIZE)),
	]


class iso2SelectedServiceListType(Structure):
	_fields_=[
		("array", (iso2SelectedServiceType*iso2SelectedServiceListType_SelectedService_ARRAY_SIZE)),
	]


class iso2Generic_EVSEFinePositioningParametersType(Structure):
	_fields_=[
		("GenericParameters", iso2ParameterSetType),
	]


class iso2ListOfRootCertificateIDsType(Structure):
	_fields_=[
		("array", (iso2X509IssuerSerialType*iso2ListOfRootCertificateIDsType_RootCertificateID_ARRAY_SIZE)),
	]


class iso2PairingReqType(Structure):
	_fields_=[
		("EVProcessing", c_uint),

		("PairingParameters", iso2ParameterSetType),

		("PairingParameters_isUsed", c_uint, 1),
	]


class iso2CurrentDemandResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),

		("EVSEStatus", iso2EVSEStatusType),

		("EVSEStatus_isUsed", c_uint, 1),

		("EVSEPresentCurrent", iso2PhysicalValueType),

		("EVSEPresentVoltage", iso2PhysicalValueType),

		("EVSEPowerLimitAchieved", c_int),

		("EVSECurrentLimitAchieved", c_int),

		("EVSEVoltageLimitAchieved", c_int),

		("EVSEMaximumPower", iso2PhysicalValueType),

		("EVSEMaximumPower_isUsed", c_uint, 1),

		("EVSEMaximumCurrent", iso2PhysicalValueType),

		("EVSEMaximumCurrent_isUsed", c_uint, 1),

		("EVSEMaximumVoltage", iso2PhysicalValueType),

		("EVSEMaximumVoltage_isUsed", c_uint, 1),

		("SAScheduleTupleID", c_uint8),

		("SAScheduleTupleID_isUsed", c_uint, 1),

		("MeterInfo", iso2MeterInfoType),

		("MeterInfo_isUsed", c_uint, 1),

		("ReceiptRequired", c_int),

		("ReceiptRequired_isUsed", c_uint, 1),

		("EVSEID", ArrayType_factory(c_uint32, "characters", iso2CurrentDemandResType_EVSEID_CHARACTERS_SIZE)),
	]


class iso2ChargingStatusReqType(Structure):
	_fields_=[
		("EVTargetEnergyRequest", iso2PhysicalValueType),

		("EVMaximumEnergyRequest", iso2PhysicalValueType),

		("EVMaximumEnergyRequest_isUsed", c_uint, 1),

		("EVMinimumEnergyRequest", iso2PhysicalValueType),

		("EVMinimumEnergyRequest_isUsed", c_uint, 1),

		("DisplayParameters", iso2DisplayParametersType),

		("DisplayParameters_isUsed", c_uint, 1),

		("EVMaximumChargePower", iso2PhysicalValueType),

		("EVMaximumChargePower_isUsed", c_uint, 1),

		("EVMaximumChargeCurrent", iso2PhysicalValueType),

		("EVMaximumChargeCurrent_isUsed", c_uint, 1),

		("EVMinimumChargeCurrent", iso2PhysicalValueType),

		("EVMinimumChargeCurrent_isUsed", c_uint, 1),
	]


class iso2CertificateInstallationResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),

		("EVSEStatus", iso2EVSEStatusType),

		("EVSEStatus_isUsed", c_uint, 1),

		("SAProvisioningCertificateChain", iso2CertificateChainType),

		("ContractSignatureCertChain", iso2CertificateChainType),

		("ContractSignatureEncryptedPrivateKey", iso2ContractSignatureEncryptedPrivateKeyType),

		("DHpublickey", iso2DiffieHellmanPublickeyType),

		("eMAID", iso2EMAIDType),
	]


class iso2SensorPackageType(Structure):
	_fields_=[
		("PackageIndex", c_uint32),

		("array", (iso2SensorMeasurementsType*iso2SensorPackageType_SensorMeasurements_ARRAY_SIZE)),
	]


class iso2ServiceDiscoveryResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),

		("EVSEStatus", iso2EVSEStatusType),

		("EVSEStatus_isUsed", c_uint, 1),

		("PaymentOptionList", iso2PaymentOptionListType),

		("EnergyTransferServiceList", iso2ServiceListType),

		("VASList", iso2ServiceListType),

		("VASList_isUsed", c_uint, 1),
	]


class iso2PowerDemandResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),

		("EVSEStatus", iso2EVSEStatusType),

		("EVSEStatus_isUsed", c_uint, 1),

		("EVSEOutputPower", iso2PhysicalValueType),

		("SAScheduleTupleID", c_uint8),

		("SAScheduleTupleID_isUsed", c_uint, 1),

		("MeterInfo", iso2MeterInfoType),

		("MeterInfo_isUsed", c_uint, 1),

		("ReceiptRequired", c_int),

		("ReceiptRequired_isUsed", c_uint, 1),

		("PowerDemandParameters", iso2ParameterSetType),

		("PowerDemandParameters_isUsed", c_uint, 1),

		("EVSEID", ArrayType_factory(c_uint32, "characters", iso2PowerDemandResType_EVSEID_CHARACTERS_SIZE)),
	]


class iso2ChargingProfileType(Structure):
	_fields_=[
		("array", (iso2PMaxScheduleEntryType*iso2ChargingProfileType_ProfileEntry_ARRAY_SIZE)),
	]


class iso2SalesTariffType(Structure):
	_fields_=[
		("SalesTariffID", c_uint8),

		("SalesTariffDescription_isUsed", c_uint, 1),

		("NumEPriceLevels", c_uint8),

		("NumEPriceLevels_isUsed", c_uint, 1),

		("Id", ArrayType_factory(c_uint32, "characters", iso2SalesTariffType_Id_CHARACTERS_SIZE)),

		("SalesTariffDescription", ArrayType_factory(c_uint32, "characters", iso2SalesTariffType_SalesTariffDescription_CHARACTERS_SIZE)),

		("array", (iso2SalesTariffEntryType*iso2SalesTariffType_SalesTariffEntry_ARRAY_SIZE)),
	]


class iso2SignedInfoType(Structure):
	_fields_=[
		("Id_isUsed", c_uint, 1),

		("CanonicalizationMethod", iso2CanonicalizationMethodType),

		("SignatureMethod", iso2SignatureMethodType),

		("Id", ArrayType_factory(c_uint32, "characters", iso2SignedInfoType_Id_CHARACTERS_SIZE)),

		("array", (iso2ReferenceType*iso2SignedInfoType_Reference_ARRAY_SIZE)),
	]


class iso2PowerDeliveryResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),

		("EVSEStatus", iso2EVSEStatusType),

		("EVSEStatus_isUsed", c_uint, 1),

		("EVSEProcessing", c_uint),
	]


class iso2RetrievalMethodType(Structure):
	_fields_=[
		("URI_isUsed", c_uint, 1),

		("Type_isUsed", c_uint, 1),

		("Transforms", iso2TransformsType),

		("Transforms_isUsed", c_uint, 1),

		("URI", ArrayType_factory(c_uint32, "characters", iso2RetrievalMethodType_URI_CHARACTERS_SIZE)),

		("Type", ArrayType_factory(c_uint32, "characters", iso2RetrievalMethodType_Type_CHARACTERS_SIZE)),
	]


class iso2MagneticVectorListType(Structure):
	_fields_=[
		("array", (iso2MagneticVectorType*iso2MagneticVectorListType_MagneticVector_ARRAY_SIZE)),
	]


class iso2ServiceParameterListType(Structure):
	_fields_=[
		("array", (iso2ParameterSetType*iso2ServiceParameterListType_ParameterSet_ARRAY_SIZE)),
	]


class iso2PMaxScheduleType(Structure):
	_fields_=[
		("array", (iso2PMaxScheduleEntryType*iso2PMaxScheduleType_PMaxScheduleEntry_ARRAY_SIZE)),
	]


class iso2CertificateUpdateResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),

		("EVSEStatus", iso2EVSEStatusType),

		("EVSEStatus_isUsed", c_uint, 1),

		("SAProvisioningCertificateChain", iso2CertificateChainType),

		("ContractSignatureCertChain", iso2CertificateChainType),

		("ContractSignatureEncryptedPrivateKey", iso2ContractSignatureEncryptedPrivateKeyType),

		("DHpublickey", iso2DiffieHellmanPublickeyType),

		("eMAID", iso2EMAIDType),

		("RetryCounter", c_int16),

		("RetryCounter_isUsed", c_uint, 1),
	]


class iso2DC_BidirectionalControlReqType(Structure):
	_fields_=[
		("EVTargetEnergyRequest", iso2PhysicalValueType),

		("EVMaximumEnergyRequest", iso2PhysicalValueType),

		("EVMaximumEnergyRequest_isUsed", c_uint, 1),

		("EVMinimumEnergyRequest", iso2PhysicalValueType),

		("EVMinimumEnergyRequest_isUsed", c_uint, 1),

		("DisplayParameters", iso2DisplayParametersType),

		("DisplayParameters_isUsed", c_uint, 1),

		("EVTargetCurrent", iso2PhysicalValueType),

		("EVTargetVoltage", iso2PhysicalValueType),

		("EVMaximumVoltage", iso2PhysicalValueType),

		("EVMinimumVoltage", iso2PhysicalValueType),

		("EVMaximumChargeCurrent", iso2PhysicalValueType),

		("EVMaximumDischargeCurrent", iso2PhysicalValueType),

		("EVMaximumDischargeCurrent_isUsed", c_uint, 1),

		("EVMaximumChargePower", iso2PhysicalValueType),

		("EVMaximumChargePower_isUsed", c_uint, 1),

		("EVMaximumDischargePower", iso2PhysicalValueType),

		("EVMaximumDischargePower_isUsed", c_uint, 1),
	]


class iso2CertificateUpdateReqType(Structure):
	_fields_=[
		("ContractSignatureCertChain", iso2CertificateChainType),

		("ListOfRootCertificateIDs", iso2ListOfRootCertificateIDsType),

		("Id", ArrayType_factory(c_uint32, "characters", iso2CertificateUpdateReqType_Id_CHARACTERS_SIZE)),

		("eMAID", ArrayType_factory(c_uint32, "characters", iso2CertificateUpdateReqType_eMAID_CHARACTERS_SIZE)),
	]


class iso2LFA_EVSEFinePositioningSetupParametersType(Structure):
	_fields_=[
		("NumberOfSensors", c_uint8),

		("SensorList", iso2SensorListType),

		("SensorOrder", iso2SensorOrderListType),

		("SignalPulseDuration", c_uint8),

		("SignalSeparationTime", c_uint8),

		("PackageSeparationTime", c_uint8),

		("AlignmentOffset", c_uint16),

		("SignalFrequency", c_uint16),
	]


class iso2AlignmentCheckReqType(Structure):
	_fields_=[
		("EVProcessing", c_uint),

		("AlignmentCheckParameters", iso2ParameterSetType),

		("AlignmentCheckParameters_isUsed", c_uint, 1),
	]


class iso2CertificateInstallationReqType(Structure):
	_fields_=[
		("ListOfRootCertificateIDs", iso2ListOfRootCertificateIDsType),

		("Id", ArrayType_factory(c_uint32, "characters", iso2CertificateInstallationReqType_Id_CHARACTERS_SIZE)),

		("OEMProvisioningCert", ArrayType_factory(c_uint8, "bytes", iso2CertificateInstallationReqType_OEMProvisioningCert_BYTES_SIZE)),
	]


class iso2ChargeParameterDiscoveryReqType(Structure):
	_fields_=[
		("MaxSupportingPoints", c_uint16),

		("MaxSupportingPoints_isUsed", c_uint, 1),

		("EVEnergyTransferParameter", iso2EVEnergyTransferParameterType),

		("EVEnergyTransferParameter_isUsed", c_uint, 1),

		("AC_EVChargeParameter", iso2AC_EVChargeParameterType),

		("AC_EVChargeParameter_isUsed", c_uint, 1),

		("AC_EVBidirectionalParameter", iso2AC_EVBidirectionalParameterType),

		("AC_EVBidirectionalParameter_isUsed", c_uint, 1),

		("DC_EVChargeParameter", iso2DC_EVChargeParameterType),

		("DC_EVChargeParameter_isUsed", c_uint, 1),

		("DC_EVBidirectionalParameter", iso2DC_EVBidirectionalParameterType),

		("DC_EVBidirectionalParameter_isUsed", c_uint, 1),

		("WPT_EVChargeParameter", iso2WPT_EVChargeParameterType),

		("WPT_EVChargeParameter_isUsed", c_uint, 1),

		("MinimumPMaxRequest", iso2MinimumPMaxRequestType),

		("MinimumPMaxRequest_isUsed", c_uint, 1),
	]


class iso2SensorPackageListType(Structure):
	_fields_=[
		("array", (iso2SensorPackageType*iso2SensorPackageListType_SensorPackage_ARRAY_SIZE)),
	]


class iso2ChargeLoopReqType(Structure):
	_fields_=[
		("EVTargetEnergyRequest", iso2PhysicalValueType),

		("EVMaximumEnergyRequest", iso2PhysicalValueType),

		("EVMaximumEnergyRequest_isUsed", c_uint, 1),

		("EVMinimumEnergyRequest", iso2PhysicalValueType),

		("EVMinimumEnergyRequest_isUsed", c_uint, 1),

		("DisplayParameters", iso2DisplayParametersType),

		("DisplayParameters_isUsed", c_uint, 1),
	]


class iso2AC_BidirectionalControlReqType(Structure):
	_fields_=[
		("EVTargetEnergyRequest", iso2PhysicalValueType),

		("EVMaximumEnergyRequest", iso2PhysicalValueType),

		("EVMaximumEnergyRequest_isUsed", c_uint, 1),

		("EVMinimumEnergyRequest", iso2PhysicalValueType),

		("EVMinimumEnergyRequest_isUsed", c_uint, 1),

		("DisplayParameters", iso2DisplayParametersType),

		("DisplayParameters_isUsed", c_uint, 1),

		("EVOperation", c_uint),

		("EVOperation_isUsed", c_uint, 1),

		("EVMaximumChargePower", iso2PhysicalValueType),

		("EVMaximumDischargePower", iso2PhysicalValueType),

		("EVMaximumDischargePower_isUsed", c_uint, 1),

		("EVMaximumChargeCurrent", iso2PhysicalValueType),

		("EVMaximumDischargeCurrent", iso2PhysicalValueType),

		("EVMaximumDischargeCurrent_isUsed", c_uint, 1),

		("EVMinimumChargeCurrent", iso2PhysicalValueType),

		("EVMinimumDischargeCurrent", iso2PhysicalValueType),

		("EVMinimumDischargeCurrent_isUsed", c_uint, 1),

		("EVPresentActivePower", iso2PhysicalValueType),

		("EVPresentReactivePower", iso2PhysicalValueType),
	]


class iso2MV_EVSEFinePositioningParametersType(Structure):
	_fields_=[
		("MagneticVectorList", iso2MagneticVectorListType),
	]


class iso2CurrentDemandReqType(Structure):
	_fields_=[
		("EVTargetEnergyRequest", iso2PhysicalValueType),

		("EVMaximumEnergyRequest", iso2PhysicalValueType),

		("EVMaximumEnergyRequest_isUsed", c_uint, 1),

		("EVMinimumEnergyRequest", iso2PhysicalValueType),

		("EVMinimumEnergyRequest_isUsed", c_uint, 1),

		("DisplayParameters", iso2DisplayParametersType),

		("DisplayParameters_isUsed", c_uint, 1),

		("EVTargetCurrent", iso2PhysicalValueType),

		("EVTargetVoltage", iso2PhysicalValueType),

		("EVMaximumCurrent", iso2PhysicalValueType),

		("EVMaximumCurrent_isUsed", c_uint, 1),

		("EVMaximumPower", iso2PhysicalValueType),

		("EVMaximumPower_isUsed", c_uint, 1),

		("EVMaximumVoltage", iso2PhysicalValueType),

		("EVMaximumVoltage_isUsed", c_uint, 1),
	]


class iso2FinePositioningSetupReqType(Structure):
	_fields_=[
		("EVFinePositioningSetupParameters", iso2EVFinePositioningSetupParametersType),

		("LFA_EVFinePositioningSetupParameters", iso2LFA_EVFinePositioningSetupParametersType),
	]


class iso2SAScheduleTupleType(Structure):
	_fields_=[
		("SAScheduleTupleID", c_uint8),

		("PMaxSchedule", iso2PMaxScheduleType),

		("PMaxDischargeSchedule", iso2PMaxScheduleType),

		("PMaxDischargeSchedule_isUsed", c_uint, 1),

		("SalesTariff", iso2SalesTariffType),

		("SalesTariff_isUsed", c_uint, 1),

		("BuyBackTariff", iso2SalesTariffType),

		("BuyBackTariff_isUsed", c_uint, 1),
	]


class iso2ServiceDetailResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),

		("EVSEStatus", iso2EVSEStatusType),

		("EVSEStatus_isUsed", c_uint, 1),

		("ServiceID", c_uint16),

		("ServiceParameterList", iso2ServiceParameterListType),

		("ServiceParameterList_isUsed", c_uint, 1),
	]


class iso2PowerDeliveryReqType(Structure):
	_fields_=[
		("ChargeProgress", c_uint),

		("EVOperation", c_uint),

		("EVOperation_isUsed", c_uint, 1),

		("SAScheduleTupleID", c_uint8),

		("SAScheduleTupleID_isUsed", c_uint, 1),

		("ChargingProfile", iso2ChargingProfileType),

		("ChargingProfile_isUsed", c_uint, 1),
	]


class iso2PairingResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),

		("EVSEStatus", iso2EVSEStatusType),

		("EVSEStatus_isUsed", c_uint, 1),

		("EVSEProcessing", c_uint),

		("PairingParameters", iso2ParameterSetType),

		("PairingParameters_isUsed", c_uint, 1),
	]


class iso2PowerDemandReqType(Structure):
	_fields_=[
		("EVTargetEnergyRequest", iso2PhysicalValueType),

		("EVMaximumEnergyRequest", iso2PhysicalValueType),

		("EVMaximumEnergyRequest_isUsed", c_uint, 1),

		("EVMinimumEnergyRequest", iso2PhysicalValueType),

		("EVMinimumEnergyRequest_isUsed", c_uint, 1),

		("DisplayParameters", iso2DisplayParametersType),

		("DisplayParameters_isUsed", c_uint, 1),

		("EVTargetPower", iso2PhysicalValueType),

		("EVInputPower", iso2PhysicalValueType),

		("PowerDemandParameters", iso2ParameterSetType),

		("PowerDemandParameters_isUsed", c_uint, 1),
	]


class iso2PaymentServiceSelectionReqType(Structure):
	_fields_=[
		("SelectedPaymentOption", c_uint),

		("SelectedEnergyTransferService", iso2SelectedServiceType),

		("SelectedVASList", iso2SelectedServiceListType),

		("SelectedVASList_isUsed", c_uint, 1),
	]


class iso2LFA_EVFinePositioningParametersType(Structure):
	_fields_=[
		("NumberOfSignalPackages", c_uint8),

		("SensorPackageList", iso2SensorPackageListType),
	]


class iso2KeyInfoType(Structure):
	_fields_=[
		("Id_isUsed", c_uint, 1),

		("ANY_isUsed", c_uint, 1),

		("Id", ArrayType_factory(c_uint32, "characters", iso2KeyInfoType_Id_CHARACTERS_SIZE)),

		("array", (iso2KeyValueType*iso2KeyInfoType_KeyValue_ARRAY_SIZE)),

		("array", (iso2RetrievalMethodType*iso2KeyInfoType_RetrievalMethod_ARRAY_SIZE)),

		("array", (iso2X509DataType*iso2KeyInfoType_X509Data_ARRAY_SIZE)),

		("array", (iso2PGPDataType*iso2KeyInfoType_PGPData_ARRAY_SIZE)),

		("array", (iso2SPKIDataType*iso2KeyInfoType_SPKIData_ARRAY_SIZE)),

		("ANY", ArrayType_factory(c_uint32, "characters", iso2KeyInfoType_ANY_CHARACTERS_SIZE)),

		("KeyName", ArrayType_factory(ArrayType_factory(c_uint32, "characters", iso2KeyInfoType_KeyName_CHARACTERS_SIZE), "array", iso2KeyInfoType_KeyName_ARRAY_SIZE)),

		("MgmtData", ArrayType_factory(ArrayType_factory(c_uint32, "characters", iso2KeyInfoType_MgmtData_CHARACTERS_SIZE), "array", iso2KeyInfoType_MgmtData_ARRAY_SIZE)),
	]


class iso2FinePositioningReqType(Structure):
	_fields_=[
		("EVProcessing", c_uint),

		("EVFinePositioningParameters", iso2EVFinePositioningParametersType),

		("EVFinePositioningParameters_isUsed", c_uint, 1),

		("Generic_EVFinePositioningParameters", iso2Generic_EVFinePositioningParametersType),

		("Generic_EVFinePositioningParameters_isUsed", c_uint, 1),

		("LFA_EVFinePositioningParameters", iso2LFA_EVFinePositioningParametersType),

		("LFA_EVFinePositioningParameters_isUsed", c_uint, 1),
	]


class iso2SignatureType(Structure):
	_fields_=[
		("Id_isUsed", c_uint, 1),

		("SignedInfo", iso2SignedInfoType),

		("SignatureValue", iso2SignatureValueType),

		("KeyInfo", iso2KeyInfoType),

		("KeyInfo_isUsed", c_uint, 1),

		("Id", ArrayType_factory(c_uint32, "characters", iso2SignatureType_Id_CHARACTERS_SIZE)),

		("array", (iso2ObjectType*iso2SignatureType_Object_ARRAY_SIZE)),
	]


class iso2FinePositioningSetupResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),

		("EVSEStatus", iso2EVSEStatusType),

		("EVSEStatus_isUsed", c_uint, 1),

		("EVSEFinePositioningSetupParameters", iso2EVSEFinePositioningSetupParametersType),

		("EVSEFinePositioningSetupParameters_isUsed", c_uint, 1),

		("LFA_EVSEFinePositioningSetupParameters", iso2LFA_EVSEFinePositioningSetupParametersType),

		("LFA_EVSEFinePositioningSetupParameters_isUsed", c_uint, 1),

		("MV_EVSEFinePositioningSetupParameters", iso2MV_EVSEFinePositioningSetupParametersType),

		("MV_EVSEFinePositioningSetupParameters_isUsed", c_uint, 1),
	]


class iso2SAScheduleListType(Structure):
	_fields_=[
		("array", (iso2SAScheduleTupleType*iso2SAScheduleListType_SAScheduleTuple_ARRAY_SIZE)),
	]


class iso2LFA_EVSEFinePositioningParametersType(Structure):
	_fields_=[
		("NumberOfSignalPackages", c_uint8),

		("SensorPackageList", iso2SensorPackageListType),
	]


class iso2MessageHeaderType(Structure):
	_fields_=[
		("Signature", iso2SignatureType),

		("Signature_isUsed", c_uint, 1),

		("SessionID", ArrayType_factory(c_uint8, "bytes", iso2MessageHeaderType_SessionID_BYTES_SIZE)),
	]


class iso2FinePositioningResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),

		("EVSEStatus", iso2EVSEStatusType),

		("EVSEStatus_isUsed", c_uint, 1),

		("EVSEProcessing", c_uint),

		("EVSEFinePositioningParameters", iso2EVSEFinePositioningParametersType),

		("EVSEFinePositioningParameters_isUsed", c_uint, 1),

		("Generic_EVSEFinePositioningParameters", iso2Generic_EVSEFinePositioningParametersType),

		("Generic_EVSEFinePositioningParameters_isUsed", c_uint, 1),

		("LFA_EVSEFinePositioningParameters", iso2LFA_EVSEFinePositioningParametersType),

		("LFA_EVSEFinePositioningParameters_isUsed", c_uint, 1),

		("MV_EVSEFinePositioningParameters", iso2MV_EVSEFinePositioningParametersType),

		("MV_EVSEFinePositioningParameters_isUsed", c_uint, 1),
	]


class iso2ChargeParameterDiscoveryResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),

		("EVSEStatus", iso2EVSEStatusType),

		("EVSEStatus_isUsed", c_uint, 1),

		("EVSEProcessing", c_uint),

		("SAScheduleList", iso2SAScheduleListType),

		("SAScheduleList_isUsed", c_uint, 1),

		("EVSEEnergyTransferParameter", iso2EVSEEnergyTransferParameterType),

		("EVSEEnergyTransferParameter_isUsed", c_uint, 1),

		("AC_EVSEChargeParameter", iso2AC_EVSEChargeParameterType),

		("AC_EVSEChargeParameter_isUsed", c_uint, 1),

		("AC_EVSEBidirectionalParameter", iso2AC_EVSEBidirectionalParameterType),

		("AC_EVSEBidirectionalParameter_isUsed", c_uint, 1),

		("DC_EVSEChargeParameter", iso2DC_EVSEChargeParameterType),

		("DC_EVSEChargeParameter_isUsed", c_uint, 1),

		("DC_EVSEBidirectionalParameter", iso2DC_EVSEBidirectionalParameterType),

		("DC_EVSEBidirectionalParameter_isUsed", c_uint, 1),

		("WPT_EVSEChargeParameter", iso2WPT_EVSEChargeParameterType),

		("WPT_EVSEChargeParameter_isUsed", c_uint, 1),
	]


class iso2BodyType(Structure):
	_fields_=[
		("BodyElement", iso2BodyBaseType),

		("V2GRequest", iso2BodyBaseType),

		("DisconnectChargingDeviceReq", iso2DisconnectChargingDeviceReqType),

		("ConnectChargingDeviceReq", iso2ConnectChargingDeviceReqType),

		("SystemStatusReq", iso2SystemStatusReqType),

		("DC_BidirectionalControlReq", iso2DC_BidirectionalControlReqType),

		("AC_BidirectionalControlReq", iso2AC_BidirectionalControlReqType),

		("VehicleCheckOutReq", iso2VehicleCheckOutReqType),

		("VehicleCheckInReq", iso2VehicleCheckInReqType),

		("PowerDemandReq", iso2PowerDemandReqType),

		("PairingReq", iso2PairingReqType),

		("AlignmentCheckReq", iso2AlignmentCheckReqType),

		("FinePositioningReq", iso2FinePositioningReqType),

		("FinePositioningSetupReq", iso2FinePositioningSetupReqType),

		("WeldingDetectionReq", iso2WeldingDetectionReqType),

		("CurrentDemandReq", iso2CurrentDemandReqType),

		("PreChargeReq", iso2PreChargeReqType),

		("CableCheckReq", iso2CableCheckReqType),

		("ChargingStatusReq", iso2ChargingStatusReqType),

		("CertificateInstallationReq", iso2CertificateInstallationReqType),

		("CertificateUpdateReq", iso2CertificateUpdateReqType),

		("SessionStopReq", iso2SessionStopReqType),

		("MeteringReceiptReq", iso2MeteringReceiptReqType),

		("PowerDeliveryReq", iso2PowerDeliveryReqType),

		("ChargeParameterDiscoveryReq", iso2ChargeParameterDiscoveryReqType),

		("AuthorizationReq", iso2AuthorizationReqType),

		("PaymentDetailsReq", iso2PaymentDetailsReqType),

		("PaymentServiceSelectionReq", iso2PaymentServiceSelectionReqType),

		("ServiceDetailReq", iso2ServiceDetailReqType),

		("ServiceDiscoveryReq", iso2ServiceDiscoveryReqType),

		("SessionSetupReq", iso2SessionSetupReqType),

		("V2GResponse", iso2V2GResponseType),

		("DisconnectChargingDeviceRes", iso2DisconnectChargingDeviceResType),

		("ConnectChargingDeviceRes", iso2ConnectChargingDeviceResType),

		("SystemStatusRes", iso2SystemStatusResType),

		("DC_BidirectionalControlRes", iso2DC_BidirectionalControlResType),

		("AC_BidirectionalControlRes", iso2AC_BidirectionalControlResType),

		("VehicleCheckOutRes", iso2VehicleCheckOutResType),

		("VehicleCheckInRes", iso2VehicleCheckInResType),

		("PowerDemandRes", iso2PowerDemandResType),

		("PairingRes", iso2PairingResType),

		("AlignmentCheckRes", iso2AlignmentCheckResType),

		("FinePositioningRes", iso2FinePositioningResType),

		("FinePositioningSetupRes", iso2FinePositioningSetupResType),

		("WeldingDetectionRes", iso2WeldingDetectionResType),

		("CurrentDemandRes", iso2CurrentDemandResType),

		("PreChargeRes", iso2PreChargeResType),

		("CableCheckRes", iso2CableCheckResType),

		("ChargingStatusRes", iso2ChargingStatusResType),

		("CertificateInstallationRes", iso2CertificateInstallationResType),

		("CertificateUpdateRes", iso2CertificateUpdateResType),

		("SessionStopRes", iso2SessionStopResType),

		("MeteringReceiptRes", iso2MeteringReceiptResType),

		("PowerDeliveryRes", iso2PowerDeliveryResType),

		("ChargeParameterDiscoveryRes", iso2ChargeParameterDiscoveryResType),

		("AuthorizationRes", iso2AuthorizationResType),

		("PaymentDetailsRes", iso2PaymentDetailsResType),

		("PaymentServiceSelectionRes", iso2PaymentServiceSelectionResType),

		("ServiceDetailRes", iso2ServiceDetailResType),

		("ServiceDiscoveryRes", iso2ServiceDiscoveryResType),

		("SessionSetupRes", iso2SessionSetupResType),
	]


class iso2AnonType_V2G_Message(Structure):
	_fields_=[
		("Header", iso2MessageHeaderType),

		("Body", iso2BodyType),
	]


class iso2EXIDocument(Structure):
	_fields_=[
		("V2G_Message", iso2AnonType_V2G_Message),

		("ServiceDiscoveryReq", iso2ServiceDiscoveryReqType),

		("ServiceDiscoveryRes", iso2ServiceDiscoveryResType),

		("FinePositioningReq", iso2FinePositioningReqType),

		("FinePositioningRes", iso2FinePositioningResType),

		("DisconnectChargingDeviceReq", iso2DisconnectChargingDeviceReqType),

		("DisconnectChargingDeviceRes", iso2DisconnectChargingDeviceResType),

		("PowerDemandReq", iso2PowerDemandReqType),

		("MeteringReceiptReq", iso2MeteringReceiptReqType),

		("PaymentDetailsReq", iso2PaymentDetailsReqType),

		("PowerDemandRes", iso2PowerDemandResType),

		("MeteringReceiptRes", iso2MeteringReceiptResType),

		("PaymentDetailsRes", iso2PaymentDetailsResType),

		("SessionSetupReq", iso2SessionSetupReqType),

		("SessionSetupRes", iso2SessionSetupResType),

		("CableCheckReq", iso2CableCheckReqType),

		("CableCheckRes", iso2CableCheckResType),

		("CertificateInstallationReq", iso2CertificateInstallationReqType),

		("CertificateInstallationRes", iso2CertificateInstallationResType),

		("SystemStatusReq", iso2SystemStatusReqType),

		("SystemStatusRes", iso2SystemStatusResType),

		("PairingReq", iso2PairingReqType),

		("WeldingDetectionReq", iso2WeldingDetectionReqType),

		("ConnectChargingDeviceReq", iso2ConnectChargingDeviceReqType),

		("PairingRes", iso2PairingResType),

		("WeldingDetectionRes", iso2WeldingDetectionResType),

		("ConnectChargingDeviceRes", iso2ConnectChargingDeviceResType),

		("CertificateUpdateReq", iso2CertificateUpdateReqType),

		("CertificateUpdateRes", iso2CertificateUpdateResType),

		("PaymentServiceSelectionReq", iso2PaymentServiceSelectionReqType),

		("PowerDeliveryReq", iso2PowerDeliveryReqType),

		("PaymentServiceSelectionRes", iso2PaymentServiceSelectionResType),

		("PowerDeliveryRes", iso2PowerDeliveryResType),

		("ChargingStatusReq", iso2ChargingStatusReqType),

		("ChargingStatusRes", iso2ChargingStatusResType),

		("BodyElement", iso2BodyBaseType),

		("AC_BidirectionalControlReq", iso2AC_BidirectionalControlReqType),

		("AC_BidirectionalControlRes", iso2AC_BidirectionalControlResType),

		("VehicleCheckInReq", iso2VehicleCheckInReqType),

		("CurrentDemandReq", iso2CurrentDemandReqType),

		("VehicleCheckInRes", iso2VehicleCheckInResType),

		("PreChargeReq", iso2PreChargeReqType),

		("CurrentDemandRes", iso2CurrentDemandResType),

		("PreChargeRes", iso2PreChargeResType),

		("AlignmentCheckReq", iso2AlignmentCheckReqType),

		("V2GRequest", iso2BodyBaseType),

		("SessionStopReq", iso2SessionStopReqType),

		("AuthorizationReq", iso2AuthorizationReqType),

		("AlignmentCheckRes", iso2AlignmentCheckResType),

		("SessionStopRes", iso2SessionStopResType),

		("AuthorizationRes", iso2AuthorizationResType),

		("VehicleCheckOutReq", iso2VehicleCheckOutReqType),

		("ChargeParameterDiscoveryReq", iso2ChargeParameterDiscoveryReqType),

		("VehicleCheckOutRes", iso2VehicleCheckOutResType),

		("ChargeParameterDiscoveryRes", iso2ChargeParameterDiscoveryResType),

		("V2GResponse", iso2V2GResponseType),

		("FinePositioningSetupReq", iso2FinePositioningSetupReqType),

		("FinePositioningSetupRes", iso2FinePositioningSetupResType),

		("ServiceDetailReq", iso2ServiceDetailReqType),

		("DC_BidirectionalControlReq", iso2DC_BidirectionalControlReqType),

		("ServiceDetailRes", iso2ServiceDetailResType),

		("DC_BidirectionalControlRes", iso2DC_BidirectionalControlResType),

		("LFA_EVFinePositioningSetupParameters", iso2LFA_EVFinePositioningSetupParametersType),

		("MV_EVSEFinePositioningParameters", iso2MV_EVSEFinePositioningParametersType),

		("RelativeTimeInterval", iso2RelativeTimeIntervalType),

		("SalesTariffEntry", iso2SalesTariffEntryType),

		("LFA_EVSEFinePositioningSetupParameters", iso2LFA_EVSEFinePositioningSetupParametersType),

		("AC_EVChargeParameter", iso2AC_EVChargeParameterType),

		("MV_EVSEFinePositioningSetupParameters", iso2MV_EVSEFinePositioningSetupParametersType),

		("EVEnergyTransferParameter", iso2EVEnergyTransferParameterType),

		("DC_EVSEBidirectionalParameter", iso2DC_EVSEBidirectionalParameterType),

		("SAScheduleList", iso2SAScheduleListType),

		("EVSEFinePositioningSetupParameters", iso2EVSEFinePositioningSetupParametersType),

		("Generic_EVSEFinePositioningParameters", iso2Generic_EVSEFinePositioningParametersType),

		("DC_EVChargeParameter", iso2DC_EVChargeParameterType),

		("DC_EVSEChargeParameter", iso2DC_EVSEChargeParameterType),

		("LFA_EVFinePositioningParameters", iso2LFA_EVFinePositioningParametersType),

		("EVFinePositioningSetupParameters", iso2EVFinePositioningSetupParametersType),

		("AC_EVSEBidirectionalParameter", iso2AC_EVSEBidirectionalParameterType),

		("EVFinePositioningParameters", iso2EVFinePositioningParametersType),

		("WPT_EVChargeParameter", iso2WPT_EVChargeParameterType),

		("LFA_EVSEFinePositioningParameters", iso2LFA_EVSEFinePositioningParametersType),

		("EVSEEnergyTransferParameter", iso2EVSEEnergyTransferParameterType),

		("AC_EVBidirectionalParameter", iso2AC_EVBidirectionalParameterType),

		("EVSEFinePositioningParameters", iso2EVSEFinePositioningParametersType),

		("WPT_EVSEChargeParameter", iso2WPT_EVSEChargeParameterType),

		("AC_EVSEChargeParameter", iso2AC_EVSEChargeParameterType),

		("PMaxScheduleEntry", iso2PMaxScheduleEntryType),

		("Generic_EVFinePositioningParameters", iso2Generic_EVFinePositioningParametersType),

		("DC_EVBidirectionalParameter", iso2DC_EVBidirectionalParameterType),

		("SignatureProperty", iso2SignaturePropertyType),

		("DSAKeyValue", iso2DSAKeyValueType),

		("SignatureProperties", iso2SignaturePropertiesType),

		("KeyValue", iso2KeyValueType),

		("Transforms", iso2TransformsType),

		("DigestMethod", iso2DigestMethodType),

		("Signature", iso2SignatureType),

		("RetrievalMethod", iso2RetrievalMethodType),

		("Manifest", iso2ManifestType),

		("Reference", iso2ReferenceType),

		("CanonicalizationMethod", iso2CanonicalizationMethodType),

		("RSAKeyValue", iso2RSAKeyValueType),

		("Transform", iso2TransformType),

		("PGPData", iso2PGPDataType),

		("SignatureMethod", iso2SignatureMethodType),

		("KeyInfo", iso2KeyInfoType),

		("SPKIData", iso2SPKIDataType),

		("X509Data", iso2X509DataType),

		("SignatureValue", iso2SignatureValueType),

		("SignedInfo", iso2SignedInfoType),

		("Object", iso2ObjectType),

		("MgmtData", ArrayType_factory(c_uint32, "characters", EXIDocument_MgmtData_CHARACTERS_SIZE)),

		("KeyName", ArrayType_factory(c_uint32, "characters", EXIDocument_KeyName_CHARACTERS_SIZE)),

		("DigestValue", ArrayType_factory(c_uint8, "bytes", EXIDocument_DigestValue_BYTES_SIZE)),
	]


class iso2EXIFragment(Structure):
	_fields_=[
		("EVMaximumVoltage", iso2PhysicalValueType),

		("FrequencyChannel", c_uint32),

		("EVProcessing", c_uint),

		("BulkChargingComplete", c_int),

		("ParkingMethod", c_uint),

		("SAScheduleTupleID", c_uint8),

		("Distance", c_uint16),

		("ParameterSet", iso2ParameterSetType),

		("EVMinimumDischargeCurrent", iso2PhysicalValueType),

		("SignalSeparationTime", c_uint8),

		("EVSEEnergyTransferParameter", iso2EVSEEnergyTransferParameterType),

		("EVSEMaximumVoltage", iso2PhysicalValueType),

		("DC_EVSEBidirectionalParameter", iso2DC_EVSEBidirectionalParameterType),

		("ChargingSession", c_uint),

		("SubCertificates", iso2SubCertificatesType),

		("RetrievalMethod", iso2RetrievalMethodType),

		("MagneticVectorSetupList", iso2MagneticVectorSetupListType),

		("PairingParameters", iso2ParameterSetType),

		("EVSEMinimumPower", iso2PhysicalValueType),

		("AC_BidirectionalControlReq", iso2AC_BidirectionalControlReqType),

		("Cost", iso2CostType),

		("AC_BidirectionalControlRes", iso2AC_BidirectionalControlResType),

		("BuyBackTariff", iso2SalesTariffType),

		("XCoordinate", c_int16),

		("EVSECheckOutStatus", c_uint),

		("RetryCounter", c_int16),

		("EVSEMaximumDischargeCurrent", iso2PhysicalValueType),

		("Sensor", iso2SensorType),

		("MeterReadingCharged", c_uint64),

		("HMACOutputLength", c_int64),

		("V2GResponse", iso2V2GResponseType),

		("EVMinimumVoltage", iso2PhysicalValueType),

		("EVMinimumEnergyRequest", iso2PhysicalValueType),

		("RelativeTimeInterval", iso2RelativeTimeIntervalType),

		("WPT_EVChargeParameter", iso2WPT_EVChargeParameterType),

		("SAScheduleTuple", iso2SAScheduleTupleType),

		("ServiceID", c_uint16),

		("AngleGAtoVA", iso2PhysicalValueType),

		("boolValue", c_int),

		("EVMaximumDischargeCurrent", iso2PhysicalValueType),

		("NotificationMaxDelay", c_uint16),

		("EVSEMaximumDischargePower", iso2PhysicalValueType),

		("PGPData", iso2PGPDataType),

		("EVSEMaximumChargePower", iso2PhysicalValueType),

		("EVSEEnergyToBeDelivered", iso2PhysicalValueType),

		("EVMaximumPower", iso2PhysicalValueType),

		("EVMaximumCurrent", iso2PhysicalValueType),

		("RSAKeyValue", iso2RSAKeyValueType),

		("EVSENominalVoltage", iso2PhysicalValueType),

		("MagneticVector", iso2MagneticVectorType),

		("Signature", iso2SignatureType),

		("EVElectricalChargingDeviceStatus", c_uint),

		("EVSEProcessing", c_uint),

		("FODStatus", c_uint),

		("PowerDeliveryRes", iso2PowerDeliveryResType),

		("SessionStopRes", iso2SessionStopResType),

		("WPT_EVSEChargeParameter", iso2WPT_EVSEChargeParameterType),

		("ResponseCode", c_uint),

		("EVTargetEnergyRequest", iso2PhysicalValueType),

		("FinePositioningSetupReq", iso2FinePositioningSetupReqType),

		("EVSEPresentCurrent", iso2PhysicalValueType),

		("FinePositioningSetupRes", iso2FinePositioningSetupResType),

		("ProfileEntry", iso2PMaxScheduleEntryType),

		("SAProvisioningCertificateChain", iso2CertificateChainType),

		("PowerDeliveryReq", iso2PowerDeliveryReqType),

		("SessionStopReq", iso2SessionStopReqType),

		("ReceiptRequired", c_int),

		("ChargingProfile", iso2ChargingProfileType),

		("MaxSupportingPoints", c_uint16),

		("start", c_uint32),

		("EVMinimumChargePower", iso2PhysicalValueType),

		("amount", iso2PhysicalValueType),

		("PreChargeReq", iso2PreChargeReqType),

		("PackageIndex", c_uint32),

		("PreChargeRes", iso2PreChargeResType),

		("ContractSignatureCertChain", iso2CertificateChainType),

		("MV_EVSEFinePositioningSetupParameters", iso2MV_EVSEFinePositioningSetupParametersType),

		("EVSEMinimumDischargeCurrent", iso2PhysicalValueType),

		("EVMaximumChargeCurrent", iso2PhysicalValueType),

		("AlignmentOffset", c_uint16),

		("RemainingTimeToTargetSOC", c_int8),

		("SensorMeasurements", iso2SensorMeasurementsType),

		("SalesTariff", iso2SalesTariffType),

		("EVSEMaximumPower", iso2PhysicalValueType),

		("TargetOffset", iso2TargetPositionType),

		("PowerDemandParameters", iso2ParameterSetType),

		("DisconnectChargingDeviceReq", iso2DisconnectChargingDeviceReqType),

		("DisconnectChargingDeviceRes", iso2DisconnectChargingDeviceResType),

		("DSAKeyValue", iso2DSAKeyValueType),

		("SalesTariffEntry", iso2SalesTariffEntryType),

		("CertificateInstallationRes", iso2CertificateInstallationResType),

		("CanonicalizationMethod", iso2CanonicalizationMethodType),

		("Generic_EVFinePositioningParameters", iso2Generic_EVFinePositioningParametersType),

		("EVSEMinimumVoltage", iso2PhysicalValueType),

		("SystemStatusRes", iso2SystemStatusResType),

		("EVSEOutputPower", iso2PhysicalValueType),

		("SignedInfo", iso2SignedInfoType),

		("EVMinimumChargeCurrent", iso2PhysicalValueType),

		("costKind", c_uint),

		("SystemStatusReq", iso2SystemStatusReqType),

		("CableCheckReq", iso2CableCheckReqType),

		("NumEPriceLevels", c_uint8),

		("EVSEVoltageLimitAchieved", c_int),

		("PackageSeparationTime", c_uint8),

		("CableCheckRes", iso2CableCheckResType),

		("EVCheckInStatus", c_uint),

		("PMaxDischargeSchedule", iso2PMaxScheduleType),

		("EVMinimumPower", iso2PhysicalValueType),

		("ChargingPerformance", iso2PhysicalValueType),

		("AlignmentCheckReq", iso2AlignmentCheckReqType),

		("EVMechanicalChargingDeviceStatus", c_uint),

		("VehicleSpace", c_uint16),

		("AlignmentCheckRes", iso2AlignmentCheckResType),

		("EVMinimumDischargePower", iso2PhysicalValueType),

		("RemainingTimeToMinimumSOC", c_int8),

		("AuthorizationRes", iso2AuthorizationResType),

		("CertificateInstallationReq", iso2CertificateInstallationReqType),

		("PaymentDetailsReq", iso2PaymentDetailsReqType),

		("PaymentDetailsRes", iso2PaymentDetailsResType),

		("AuthorizationReq", iso2AuthorizationReqType),

		("EVTargetCurrent", iso2PhysicalValueType),

		("SessionSetupReq", iso2SessionSetupReqType),

		("SessionSetupRes", iso2SessionSetupResType),

		("EVSENominalFrequency", iso2PhysicalValueType),

		("Header", iso2MessageHeaderType),

		("NumberOfSensors", c_uint8),

		("EVSETimeStamp", c_int64),

		("MeterStatus", c_int16),

		("MV_EVSEFinePositioningParameters", iso2MV_EVSEFinePositioningParametersType),

		("ChargeProgress", c_uint),

		("PMaxSchedule", iso2PMaxScheduleType),

		("duration", c_uint32),

		("RemainingTimeToBulkSOC", c_int8),

		("SensorOrientation", iso2CartesianCoordinatesType),

		("EVSEMaximumChargeCurrent", iso2PhysicalValueType),

		("LFA_EVSEFinePositioningParameters", iso2LFA_EVSEFinePositioningParametersType),

		("VehicleCheckInRes", iso2VehicleCheckInResType),

		("PMaxScheduleEntry", iso2PMaxScheduleEntryType),

		("SAScheduleList", iso2SAScheduleListType),

		("PaymentOptionList", iso2PaymentOptionListType),

		("ContractSignatureEncryptedPrivateKey", iso2ContractSignatureEncryptedPrivateKeyType),

		("VehicleCheckInReq", iso2VehicleCheckInReqType),

		("CheckOutTime", c_uint64),

		("CurrentSOC", c_int8),

		("ZCoordinate", c_int16),

		("MeasurementData", c_uint16),

		("PairingRes", iso2PairingResType),

		("EVSEMaximumCurrent", iso2PhysicalValueType),

		("LFA_EVFinePositioningParameters", iso2LFA_EVFinePositioningParametersType),

		("AlignmentCheckParameters", iso2ParameterSetType),

		("EffectiveRadiatedPower", c_int8),

		("PairingReq", iso2PairingReqType),

		("Value", c_int16),

		("byteValue", c_int8),

		("CurrentDemandReq", iso2CurrentDemandReqType),

		("Generic_EVSEFinePositioningParameters", iso2Generic_EVSEFinePositioningParametersType),

		("CurrentDemandRes", iso2CurrentDemandResType),

		("AC_EVBidirectionalParameter", iso2AC_EVBidirectionalParameterType),

		("SelectedEnergyTransferService", iso2SelectedServiceType),

		("startValue", iso2PhysicalValueType),

		("SelectedVASList", iso2SelectedServiceListType),

		("ChargeParameterDiscoveryReq", iso2ChargeParameterDiscoveryReqType),

		("ChargeParameterDiscoveryRes", iso2ChargeParameterDiscoveryResType),

		("TargetSOC", c_int8),

		("EVSEStatus", iso2EVSEStatusType),

		("EVSEMinimumChargeCurrent", iso2PhysicalValueType),

		("EVSEElectricalChargingDeviceStatus", c_uint),

		("X509SerialNumber", c_int64),

		("PaymentOption", c_uint),

		("Transforms", iso2TransformsType),

		("EVSEPeakCurrentRipple", iso2PhysicalValueType),

		("ConsumptionCost", iso2ConsumptionCostType),

		("EVSEFinePositioningSetupParameters", iso2EVSEFinePositioningSetupParametersType),

		("EPriceLevel", c_uint8),

		("X509IssuerSerial", iso2X509IssuerSerialType),

		("SPKIData", iso2SPKIDataType),

		("MagneticVectorList", iso2MagneticVectorListType),

		("EVSEFinePositioningParameters", iso2EVSEFinePositioningParametersType),

		("EVTargetPower", iso2PhysicalValueType),

		("SensorPackageList", iso2SensorPackageListType),

		("DepartureTime", c_uint32),

		("InletHot", c_int),

		("EVPresentActivePower", iso2PhysicalValueType),

		("X509Data", iso2X509DataType),

		("YCoordinate", c_int16),

		("KeyValue", iso2KeyValueType),

		("DisplayParameters", iso2DisplayParametersType),

		("EVSEPowerLimitAchieved", c_int),

		("Body", iso2BodyType),

		("DC_EVChargeParameter", iso2DC_EVChargeParameterType),

		("Service", iso2ServiceType),

		("SignatureProperty", iso2SignaturePropertyType),

		("LFA_EVFinePositioningSetupParameters", iso2LFA_EVFinePositioningSetupParametersType),

		("MinimumPMaxRequest", iso2MinimumPMaxRequestType),

		("FinePositioningReq", iso2FinePositioningReqType),

		("EnergyTransferServiceList", iso2ServiceListType),

		("FinePositioningRes", iso2FinePositioningResType),

		("AC_EVSEBidirectionalParameter", iso2AC_EVSEBidirectionalParameterType),

		("FreeService", c_int),

		("AC_EVSEChargeParameter", iso2AC_EVSEChargeParameterType),

		("SensorID", c_uint8),

		("EVSECurrentRegulationTolerance", iso2PhysicalValueType),

		("EVSEMechanicalChargingDeviceStatus", c_uint),

		("EVEnergyTransferParameter", iso2EVEnergyTransferParameterType),

		("SignalPulseDuration", c_uint8),

		("shortValue", c_int16),

		("Manifest", iso2ManifestType),

		("DC_EVSEChargeParameter", iso2DC_EVSEChargeParameterType),

		("MeteringReceiptReq", iso2MeteringReceiptReqType),

		("MeteringReceiptRes", iso2MeteringReceiptResType),

		("ServiceDiscoveryReq", iso2ServiceDiscoveryReqType),

		("SalesTariffID", c_uint8),

		("ServiceDiscoveryRes", iso2ServiceDiscoveryResType),

		("MagneticVectorSetup", iso2MagneticVectorSetupType),

		("DigestMethod", iso2DigestMethodType),

		("MeterReadingDischarged", c_uint64),

		("MeasurementDataList", iso2MeasurementDataListType),

		("SignatureProperties", iso2SignaturePropertiesType),

		("SensorPosition", iso2CartesianCoordinatesType),

		("LFA_EVSEFinePositioningSetupParameters", iso2LFA_EVSEFinePositioningSetupParametersType),

		("eMAID", iso2EMAIDType),

		("SensorPackage", iso2SensorPackageType),

		("EVCheckOutStatus", c_uint),

		("RootCertificateID", iso2X509IssuerSerialType),

		("DC_BidirectionalControlReq", iso2DC_BidirectionalControlReqType),

		("EVSEPresentVoltage", iso2PhysicalValueType),

		("DC_BidirectionalControlRes", iso2DC_BidirectionalControlResType),

		("VASList", iso2ServiceListType),

		("MeterInfo", iso2MeterInfoType),

		("EVSETargetReactivePower", iso2PhysicalValueType),

		("ChargingStatusReq", iso2ChargingStatusReqType),

		("GenericParameters", iso2ParameterSetType),

		("ChargingStatusRes", iso2ChargingStatusResType),

		("EVMaximumChargePower", iso2PhysicalValueType),

		("BulkSOC", c_int8),

		("NumberOfSignalPackages", c_uint8),

		("ParameterSetID", c_uint16),

		("PMax", iso2PhysicalValueType),

		("EVMaximumEnergyRequest", iso2PhysicalValueType),

		("EVOperation", c_uint),

		("CertificateUpdateRes", iso2CertificateUpdateResType),

		("ChargingComplete", c_int),

		("ListOfRootCertificateIDs", iso2ListOfRootCertificateIDsType),

		("RotationVAtoGA", iso2PhysicalValueType),

		("EVTargetVoltage", iso2PhysicalValueType),

		("CertificateUpdateReq", iso2CertificateUpdateReqType),

		("ConnectChargingDeviceRes", iso2ConnectChargingDeviceResType),

		("DHpublickey", iso2DiffieHellmanPublickeyType),

		("ServiceParameterList", iso2ServiceParameterListType),

		("SignatureValue", iso2SignatureValueType),

		("physicalValue", iso2PhysicalValueType),

		("OperationMode", c_uint),

		("EVSECurrentLimitAchieved", c_int),

		("ServiceDetailReq", iso2ServiceDetailReqType),

		("ServiceDetailRes", iso2ServiceDetailResType),

		("intValue", c_int32),

		("EVMaximumDischargePower", iso2PhysicalValueType),

		("MinimumSOC", c_int8),

		("SelectedPaymentOption", c_uint),

		("V2G_Message", iso2AnonType_V2G_Message),

		("TMeter", c_int64),

		("SensorOrder", iso2SensorOrderListType),

		("SupportedServiceIDs", iso2ServiceIDListType),

		("EVFinePositioningParameters", iso2EVFinePositioningParametersType),

		("SensorList", iso2SensorListType),

		("KeyInfo", iso2KeyInfoType),

		("ConnectChargingDeviceReq", iso2ConnectChargingDeviceReqType),

		("AC_EVChargeParameter", iso2AC_EVChargeParameterType),

		("Parameter", iso2ParameterType),

		("WeldingDetectionRes", iso2WeldingDetectionResType),

		("SignalFrequency", c_uint16),

		("EVSETargetPower", iso2PhysicalValueType),

		("DC_EVBidirectionalParameter", iso2DC_EVBidirectionalParameterType),

		("SignatureMethod", iso2SignatureMethodType),

		("WeldingDetectionReq", iso2WeldingDetectionReqType),

		("SelectedService", iso2SelectedServiceType),

		("EVInputPower", iso2PhysicalValueType),

		("VehicleCheckOutReq", iso2VehicleCheckOutReqType),

		("PowerDemandReq", iso2PowerDemandReqType),

		("VehicleCheckOutRes", iso2VehicleCheckOutResType),

		("CurrentRange", c_uint16),

		("EVPresentReactivePower", iso2PhysicalValueType),

		("V2GRequest", iso2BodyBaseType),

		("Reference", iso2ReferenceType),

		("BodyElement", iso2BodyBaseType),

		("MinimumPMaxScheduleEntry", iso2PMaxScheduleEntryType),

		("EVFinePositioningSetupParameters", iso2EVFinePositioningSetupParametersType),

		("EVSENotification", c_uint),

		("PaymentServiceSelectionReq", iso2PaymentServiceSelectionReqType),

		("PaymentServiceSelectionRes", iso2PaymentServiceSelectionResType),

		("Transform", iso2TransformType),

		("Object", iso2ObjectType),

		("TargetOffsetY", c_uint16),

		("PowerDemandRes", iso2PowerDemandResType),

		("TargetOffsetX", c_uint16),

		("stringValue", ArrayType_factory(c_uint32, "characters", EXIFragment_stringValue_CHARACTERS_SIZE)),

		("PgenCounter", ArrayType_factory(c_uint8, "bytes", EXIFragment_PgenCounter_BYTES_SIZE)),

		("SalesTariffDescription", ArrayType_factory(c_uint32, "characters", EXIFragment_SalesTariffDescription_CHARACTERS_SIZE)),

		("SessionID", ArrayType_factory(c_uint8, "bytes", EXIFragment_SessionID_BYTES_SIZE)),

		("XPath", ArrayType_factory(c_uint32, "characters", EXIFragment_XPath_CHARACTERS_SIZE)),

		("MgmtData", ArrayType_factory(c_uint32, "characters", EXIFragment_MgmtData_CHARACTERS_SIZE)),

		("OEMProvisioningCert", ArrayType_factory(c_uint8, "bytes", EXIFragment_OEMProvisioningCert_BYTES_SIZE)),

		("P", ArrayType_factory(c_uint8, "bytes", EXIFragment_P_BYTES_SIZE)),

		("Q", ArrayType_factory(c_uint8, "bytes", EXIFragment_Q_BYTES_SIZE)),

		("X509SubjectName", ArrayType_factory(c_uint32, "characters", EXIFragment_X509SubjectName_CHARACTERS_SIZE)),

		("G", ArrayType_factory(c_uint8, "bytes", EXIFragment_G_BYTES_SIZE)),

		("J", ArrayType_factory(c_uint8, "bytes", EXIFragment_J_BYTES_SIZE)),

		("Y", ArrayType_factory(c_uint8, "bytes", EXIFragment_Y_BYTES_SIZE)),

		("DigestValue", ArrayType_factory(c_uint8, "bytes", EXIFragment_DigestValue_BYTES_SIZE)),

		("EVCCID", ArrayType_factory(c_uint8, "bytes", EXIFragment_EVCCID_BYTES_SIZE)),

		("PGPKeyID", ArrayType_factory(c_uint8, "bytes", EXIFragment_PGPKeyID_BYTES_SIZE)),

		("KeyName", ArrayType_factory(c_uint32, "characters", EXIFragment_KeyName_CHARACTERS_SIZE)),

		("X509SKI", ArrayType_factory(c_uint8, "bytes", EXIFragment_X509SKI_BYTES_SIZE)),

		("Certificate", ArrayType_factory(c_uint8, "bytes", EXIFragment_Certificate_BYTES_SIZE)),

		("Modulus", ArrayType_factory(c_uint8, "bytes", EXIFragment_Modulus_BYTES_SIZE)),

		("SigMeterReading", ArrayType_factory(c_uint8, "bytes", EXIFragment_SigMeterReading_BYTES_SIZE)),

		("Exponent", ArrayType_factory(c_uint8, "bytes", EXIFragment_Exponent_BYTES_SIZE)),

		("PGPKeyPacket", ArrayType_factory(c_uint8, "bytes", EXIFragment_PGPKeyPacket_BYTES_SIZE)),

		("Seed", ArrayType_factory(c_uint8, "bytes", EXIFragment_Seed_BYTES_SIZE)),

		("MeterID", ArrayType_factory(c_uint32, "characters", EXIFragment_MeterID_CHARACTERS_SIZE)),

		("X509CRL", ArrayType_factory(c_uint8, "bytes", EXIFragment_X509CRL_BYTES_SIZE)),

		("SPKISexp", ArrayType_factory(c_uint8, "bytes", EXIFragment_SPKISexp_BYTES_SIZE)),

		("X509Certificate", ArrayType_factory(c_uint8, "bytes", EXIFragment_X509Certificate_BYTES_SIZE)),

		("EVSEID", ArrayType_factory(c_uint32, "characters", EXIFragment_EVSEID_CHARACTERS_SIZE)),

		("GenChallenge", ArrayType_factory(c_uint8, "bytes", EXIFragment_GenChallenge_BYTES_SIZE)),

		("GAID", ArrayType_factory(c_uint32, "characters", EXIFragment_GAID_CHARACTERS_SIZE)),

		("X509IssuerName", ArrayType_factory(c_uint32, "characters", EXIFragment_X509IssuerName_CHARACTERS_SIZE)),
	]


class xmldsigCanonicalizationMethodType(Structure):
	_fields_=[
		("ANY_isUsed", c_uint, 1),

		("Algorithm", ArrayType_factory(c_uint32, "characters", xmldsigCanonicalizationMethodType_Algorithm_CHARACTERS_SIZE)),

		("ANY", ArrayType_factory(c_uint32, "characters", xmldsigCanonicalizationMethodType_ANY_CHARACTERS_SIZE)),
	]


class xmldsigObjectType(Structure):
	_fields_=[
		("Id_isUsed", c_uint, 1),

		("MimeType_isUsed", c_uint, 1),

		("Encoding_isUsed", c_uint, 1),

		("ANY_isUsed", c_uint, 1),

		("Id", ArrayType_factory(c_uint32, "characters", xmldsigObjectType_Id_CHARACTERS_SIZE)),

		("MimeType", ArrayType_factory(c_uint32, "characters", xmldsigObjectType_MimeType_CHARACTERS_SIZE)),

		("Encoding", ArrayType_factory(c_uint32, "characters", xmldsigObjectType_Encoding_CHARACTERS_SIZE)),

		("ANY", ArrayType_factory(c_uint32, "characters", xmldsigObjectType_ANY_CHARACTERS_SIZE)),
	]


class xmldsigTransformType(Structure):
	_fields_=[
		("ANY_isUsed", c_uint, 1),

		("Algorithm", ArrayType_factory(c_uint32, "characters", xmldsigTransformType_Algorithm_CHARACTERS_SIZE)),

		("ANY", ArrayType_factory(c_uint32, "characters", xmldsigTransformType_ANY_CHARACTERS_SIZE)),

		("XPath", ArrayType_factory(ArrayType_factory(c_uint32, "characters", xmldsigTransformType_XPath_CHARACTERS_SIZE), "array", xmldsigTransformType_XPath_ARRAY_SIZE)),
	]


class xmldsigSignatureMethodType(Structure):
	_fields_=[
		("HMACOutputLength", c_int64),

		("HMACOutputLength_isUsed", c_uint, 1),

		("ANY_isUsed", c_uint, 1),

		("Algorithm", ArrayType_factory(c_uint32, "characters", xmldsigSignatureMethodType_Algorithm_CHARACTERS_SIZE)),

		("ANY", ArrayType_factory(c_uint32, "characters", xmldsigSignatureMethodType_ANY_CHARACTERS_SIZE)),
	]


class xmldsigDigestMethodType(Structure):
	_fields_=[
		("ANY_isUsed", c_uint, 1),

		("Algorithm", ArrayType_factory(c_uint32, "characters", xmldsigDigestMethodType_Algorithm_CHARACTERS_SIZE)),

		("ANY", ArrayType_factory(c_uint32, "characters", xmldsigDigestMethodType_ANY_CHARACTERS_SIZE)),
	]


class xmldsigSignatureValueType(Structure):
	_fields_=[
		("Id_isUsed", c_uint, 1),

		("Id", ArrayType_factory(c_uint32, "characters", xmldsigSignatureValueType_Id_CHARACTERS_SIZE)),

		("CONTENT", ArrayType_factory(c_uint8, "bytes", xmldsigSignatureValueType_CONTENT_BYTES_SIZE)),
	]


class xmldsigX509IssuerSerialType(Structure):
	_fields_=[
		("X509SerialNumber", c_int64),

		("X509IssuerName", ArrayType_factory(c_uint32, "characters", xmldsigX509IssuerSerialType_X509IssuerName_CHARACTERS_SIZE)),
	]


class xmldsigSignaturePropertyType(Structure):
	_fields_=[
		("Id_isUsed", c_uint, 1),

		("ANY_isUsed", c_uint, 1),

		("Target", ArrayType_factory(c_uint32, "characters", xmldsigSignaturePropertyType_Target_CHARACTERS_SIZE)),

		("Id", ArrayType_factory(c_uint32, "characters", xmldsigSignaturePropertyType_Id_CHARACTERS_SIZE)),

		("ANY", ArrayType_factory(c_uint32, "characters", xmldsigSignaturePropertyType_ANY_CHARACTERS_SIZE)),
	]


class xmldsigRSAKeyValueType(Structure):
	_fields_=[
		("Modulus", ArrayType_factory(c_uint8, "bytes", xmldsigRSAKeyValueType_Modulus_BYTES_SIZE)),

		("Exponent", ArrayType_factory(c_uint8, "bytes", xmldsigRSAKeyValueType_Exponent_BYTES_SIZE)),
	]


class xmldsigPGPDataType(Structure):
	_fields_=[
		("PGPKeyID_isUsed", c_uint, 1),

		("PGPKeyPacket_isUsed", c_uint, 1),

		("ANY_isUsed", c_uint, 1),

		("PGPKeyID", ArrayType_factory(c_uint8, "bytes", xmldsigPGPDataType_PGPKeyID_BYTES_SIZE)),

		("PGPKeyPacket", ArrayType_factory(c_uint8, "bytes", xmldsigPGPDataType_PGPKeyPacket_BYTES_SIZE)),

		("ANY", ArrayType_factory(c_uint32, "characters", xmldsigPGPDataType_ANY_CHARACTERS_SIZE)),
	]


class xmldsigTransformsType(Structure):
	_fields_=[
		("array", (xmldsigTransformType*xmldsigTransformsType_Transform_ARRAY_SIZE)),
	]


class xmldsigX509DataType(Structure):
	_fields_=[
		("ANY_isUsed", c_uint, 1),

		("array", (xmldsigX509IssuerSerialType*xmldsigX509DataType_X509IssuerSerial_ARRAY_SIZE)),

		("ANY", ArrayType_factory(c_uint32, "characters", xmldsigX509DataType_ANY_CHARACTERS_SIZE)),

		("X509SKI", ArrayType_factory(ArrayType_factory(c_uint8, "bytes", xmldsigX509DataType_X509SKI_BYTES_SIZE), "array", xmldsigX509DataType_X509SKI_ARRAY_SIZE)),

		("X509SubjectName", ArrayType_factory(ArrayType_factory(c_uint32, "characters", xmldsigX509DataType_X509SubjectName_CHARACTERS_SIZE), "array", xmldsigX509DataType_X509SubjectName_ARRAY_SIZE)),

		("X509Certificate", ArrayType_factory(ArrayType_factory(c_uint8, "bytes", xmldsigX509DataType_X509Certificate_BYTES_SIZE), "array", xmldsigX509DataType_X509Certificate_ARRAY_SIZE)),

		("X509CRL", ArrayType_factory(ArrayType_factory(c_uint8, "bytes", xmldsigX509DataType_X509CRL_BYTES_SIZE), "array", xmldsigX509DataType_X509CRL_ARRAY_SIZE)),
	]


class xmldsigDSAKeyValueType(Structure):
	_fields_=[
		("P_isUsed", c_uint, 1),

		("Q_isUsed", c_uint, 1),

		("G_isUsed", c_uint, 1),

		("J_isUsed", c_uint, 1),

		("Seed_isUsed", c_uint, 1),

		("PgenCounter_isUsed", c_uint, 1),

		("P", ArrayType_factory(c_uint8, "bytes", xmldsigDSAKeyValueType_P_BYTES_SIZE)),

		("Q", ArrayType_factory(c_uint8, "bytes", xmldsigDSAKeyValueType_Q_BYTES_SIZE)),

		("G", ArrayType_factory(c_uint8, "bytes", xmldsigDSAKeyValueType_G_BYTES_SIZE)),

		("Y", ArrayType_factory(c_uint8, "bytes", xmldsigDSAKeyValueType_Y_BYTES_SIZE)),

		("J", ArrayType_factory(c_uint8, "bytes", xmldsigDSAKeyValueType_J_BYTES_SIZE)),

		("Seed", ArrayType_factory(c_uint8, "bytes", xmldsigDSAKeyValueType_Seed_BYTES_SIZE)),

		("PgenCounter", ArrayType_factory(c_uint8, "bytes", xmldsigDSAKeyValueType_PgenCounter_BYTES_SIZE)),
	]


class xmldsigReferenceType(Structure):
	_fields_=[
		("Id_isUsed", c_uint, 1),

		("URI_isUsed", c_uint, 1),

		("Type_isUsed", c_uint, 1),

		("Transforms", xmldsigTransformsType),

		("Transforms_isUsed", c_uint, 1),

		("DigestMethod", xmldsigDigestMethodType),

		("Id", ArrayType_factory(c_uint32, "characters", xmldsigReferenceType_Id_CHARACTERS_SIZE)),

		("URI", ArrayType_factory(c_uint32, "characters", xmldsigReferenceType_URI_CHARACTERS_SIZE)),

		("Type", ArrayType_factory(c_uint32, "characters", xmldsigReferenceType_Type_CHARACTERS_SIZE)),

		("DigestValue", ArrayType_factory(c_uint8, "bytes", xmldsigReferenceType_DigestValue_BYTES_SIZE)),
	]


class xmldsigSPKIDataType(Structure):
	_fields_=[
		("ANY_isUsed", c_uint, 1),

		("ANY", ArrayType_factory(c_uint32, "characters", xmldsigSPKIDataType_ANY_CHARACTERS_SIZE)),

		("SPKISexp", ArrayType_factory(ArrayType_factory(c_uint8, "bytes", xmldsigSPKIDataType_SPKISexp_BYTES_SIZE), "array", xmldsigSPKIDataType_SPKISexp_ARRAY_SIZE)),
	]


class xmldsigManifestType(Structure):
	_fields_=[
		("Id_isUsed", c_uint, 1),

		("Id", ArrayType_factory(c_uint32, "characters", xmldsigManifestType_Id_CHARACTERS_SIZE)),

		("array", (xmldsigReferenceType*xmldsigManifestType_Reference_ARRAY_SIZE)),
	]


class xmldsigRetrievalMethodType(Structure):
	_fields_=[
		("URI_isUsed", c_uint, 1),

		("Type_isUsed", c_uint, 1),

		("Transforms", xmldsigTransformsType),

		("Transforms_isUsed", c_uint, 1),

		("URI", ArrayType_factory(c_uint32, "characters", xmldsigRetrievalMethodType_URI_CHARACTERS_SIZE)),

		("Type", ArrayType_factory(c_uint32, "characters", xmldsigRetrievalMethodType_Type_CHARACTERS_SIZE)),
	]


class xmldsigSignedInfoType(Structure):
	_fields_=[
		("Id_isUsed", c_uint, 1),

		("CanonicalizationMethod", xmldsigCanonicalizationMethodType),

		("SignatureMethod", xmldsigSignatureMethodType),

		("Id", ArrayType_factory(c_uint32, "characters", xmldsigSignedInfoType_Id_CHARACTERS_SIZE)),

		("array", (xmldsigReferenceType*xmldsigSignedInfoType_Reference_ARRAY_SIZE)),
	]


class xmldsigSignaturePropertiesType(Structure):
	_fields_=[
		("Id_isUsed", c_uint, 1),

		("Id", ArrayType_factory(c_uint32, "characters", xmldsigSignaturePropertiesType_Id_CHARACTERS_SIZE)),

		("array", (xmldsigSignaturePropertyType*xmldsigSignaturePropertiesType_SignatureProperty_ARRAY_SIZE)),
	]


class xmldsigKeyValueType(Structure):
	_fields_=[
		("DSAKeyValue", xmldsigDSAKeyValueType),

		("DSAKeyValue_isUsed", c_uint, 1),

		("RSAKeyValue", xmldsigRSAKeyValueType),

		("RSAKeyValue_isUsed", c_uint, 1),

		("ANY_isUsed", c_uint, 1),

		("ANY", ArrayType_factory(c_uint32, "characters", xmldsigKeyValueType_ANY_CHARACTERS_SIZE)),
	]


class xmldsigKeyInfoType(Structure):
	_fields_=[
		("Id_isUsed", c_uint, 1),

		("ANY_isUsed", c_uint, 1),

		("Id", ArrayType_factory(c_uint32, "characters", xmldsigKeyInfoType_Id_CHARACTERS_SIZE)),

		("array", (xmldsigKeyValueType*xmldsigKeyInfoType_KeyValue_ARRAY_SIZE)),

		("array", (xmldsigRetrievalMethodType*xmldsigKeyInfoType_RetrievalMethod_ARRAY_SIZE)),

		("array", (xmldsigX509DataType*xmldsigKeyInfoType_X509Data_ARRAY_SIZE)),

		("array", (xmldsigPGPDataType*xmldsigKeyInfoType_PGPData_ARRAY_SIZE)),

		("array", (xmldsigSPKIDataType*xmldsigKeyInfoType_SPKIData_ARRAY_SIZE)),

		("ANY", ArrayType_factory(c_uint32, "characters", xmldsigKeyInfoType_ANY_CHARACTERS_SIZE)),

		("KeyName", ArrayType_factory(ArrayType_factory(c_uint32, "characters", xmldsigKeyInfoType_KeyName_CHARACTERS_SIZE), "array", xmldsigKeyInfoType_KeyName_ARRAY_SIZE)),

		("MgmtData", ArrayType_factory(ArrayType_factory(c_uint32, "characters", xmldsigKeyInfoType_MgmtData_CHARACTERS_SIZE), "array", xmldsigKeyInfoType_MgmtData_ARRAY_SIZE)),
	]


class xmldsigSignatureType(Structure):
	_fields_=[
		("Id_isUsed", c_uint, 1),

		("SignedInfo", xmldsigSignedInfoType),

		("SignatureValue", xmldsigSignatureValueType),

		("KeyInfo", xmldsigKeyInfoType),

		("KeyInfo_isUsed", c_uint, 1),

		("Id", ArrayType_factory(c_uint32, "characters", xmldsigSignatureType_Id_CHARACTERS_SIZE)),

		("array", (xmldsigObjectType*xmldsigSignatureType_Object_ARRAY_SIZE)),
	]


class xmldsigEXIDocument(Structure):
	_fields_=[
		("SignatureProperty", xmldsigSignaturePropertyType),

		("DSAKeyValue", xmldsigDSAKeyValueType),

		("SignatureProperties", xmldsigSignaturePropertiesType),

		("KeyValue", xmldsigKeyValueType),

		("Transforms", xmldsigTransformsType),

		("DigestMethod", xmldsigDigestMethodType),

		("Signature", xmldsigSignatureType),

		("RetrievalMethod", xmldsigRetrievalMethodType),

		("Manifest", xmldsigManifestType),

		("Reference", xmldsigReferenceType),

		("CanonicalizationMethod", xmldsigCanonicalizationMethodType),

		("RSAKeyValue", xmldsigRSAKeyValueType),

		("Transform", xmldsigTransformType),

		("PGPData", xmldsigPGPDataType),

		("SignatureMethod", xmldsigSignatureMethodType),

		("KeyInfo", xmldsigKeyInfoType),

		("SPKIData", xmldsigSPKIDataType),

		("X509Data", xmldsigX509DataType),

		("SignatureValue", xmldsigSignatureValueType),

		("SignedInfo", xmldsigSignedInfoType),

		("Object", xmldsigObjectType),

		("MgmtData", ArrayType_factory(c_uint32, "characters", EXIDocument_MgmtData_CHARACTERS_SIZE)),

		("KeyName", ArrayType_factory(c_uint32, "characters", EXIDocument_KeyName_CHARACTERS_SIZE)),

		("DigestValue", ArrayType_factory(c_uint8, "bytes", EXIDocument_DigestValue_BYTES_SIZE)),
	]


class xmldsigEXIFragment(Structure):
	_fields_=[
		("DigestValue", ArrayType_factory(c_uint8, "bytes", EXIFragment_DigestValue_BYTES_SIZE)),

		("X509Data", xmldsigX509DataType),

		("KeyValue", xmldsigKeyValueType),

		("DigestMethod", xmldsigDigestMethodType),

		("Transforms", xmldsigTransformsType),

		("Reference", xmldsigReferenceType),

		("SignatureProperties", xmldsigSignaturePropertiesType),

		("PGPData", xmldsigPGPDataType),

		("DSAKeyValue", xmldsigDSAKeyValueType),

		("SignatureValue", xmldsigSignatureValueType),

		("KeyInfo", xmldsigKeyInfoType),

		("SignatureProperty", xmldsigSignaturePropertyType),

		("HMACOutputLength", c_int64),

		("Manifest", xmldsigManifestType),

		("CanonicalizationMethod", xmldsigCanonicalizationMethodType),

		("RSAKeyValue", xmldsigRSAKeyValueType),

		("X509IssuerSerial", xmldsigX509IssuerSerialType),

		("SPKIData", xmldsigSPKIDataType),

		("SignedInfo", xmldsigSignedInfoType),

		("Transform", xmldsigTransformType),

		("Object", xmldsigObjectType),

		("X509SerialNumber", c_int64),

		("RetrievalMethod", xmldsigRetrievalMethodType),

		("Signature", xmldsigSignatureType),

		("SignatureMethod", xmldsigSignatureMethodType),

		("DigestValue", ArrayType_factory(c_uint8, "bytes", EXIFragment_DigestValue_BYTES_SIZE)),

		("SPKISexp", ArrayType_factory(c_uint8, "bytes", EXIFragment_SPKISexp_BYTES_SIZE)),

		("KeyName", ArrayType_factory(c_uint32, "characters", EXIFragment_KeyName_CHARACTERS_SIZE)),

		("X509IssuerName", ArrayType_factory(c_uint32, "characters", EXIFragment_X509IssuerName_CHARACTERS_SIZE)),

		("MgmtData", ArrayType_factory(c_uint32, "characters", EXIFragment_MgmtData_CHARACTERS_SIZE)),

		("PGPKeyID", ArrayType_factory(c_uint8, "bytes", EXIFragment_PGPKeyID_BYTES_SIZE)),

		("PGPKeyPacket", ArrayType_factory(c_uint8, "bytes", EXIFragment_PGPKeyPacket_BYTES_SIZE)),

		("Exponent", ArrayType_factory(c_uint8, "bytes", EXIFragment_Exponent_BYTES_SIZE)),

		("P", ArrayType_factory(c_uint8, "bytes", EXIFragment_P_BYTES_SIZE)),

		("Q", ArrayType_factory(c_uint8, "bytes", EXIFragment_Q_BYTES_SIZE)),

		("Seed", ArrayType_factory(c_uint8, "bytes", EXIFragment_Seed_BYTES_SIZE)),

		("X509SubjectName", ArrayType_factory(c_uint32, "characters", EXIFragment_X509SubjectName_CHARACTERS_SIZE)),

		("X509Certificate", ArrayType_factory(c_uint8, "bytes", EXIFragment_X509Certificate_BYTES_SIZE)),

		("G", ArrayType_factory(c_uint8, "bytes", EXIFragment_G_BYTES_SIZE)),

		("J", ArrayType_factory(c_uint8, "bytes", EXIFragment_J_BYTES_SIZE)),

		("X509SKI", ArrayType_factory(c_uint8, "bytes", EXIFragment_X509SKI_BYTES_SIZE)),

		("XPath", ArrayType_factory(c_uint32, "characters", EXIFragment_XPath_CHARACTERS_SIZE)),

		("Modulus", ArrayType_factory(c_uint8, "bytes", EXIFragment_Modulus_BYTES_SIZE)),

		("X509CRL", ArrayType_factory(c_uint8, "bytes", EXIFragment_X509CRL_BYTES_SIZE)),

		("Y", ArrayType_factory(c_uint8, "bytes", EXIFragment_Y_BYTES_SIZE)),

		("PgenCounter", ArrayType_factory(c_uint8, "bytes", EXIFragment_PgenCounter_BYTES_SIZE)),
	]


class bitstream_t(Structure):
	_fields_=[
		("size", c_size_t),

		("data", POINTER(c_uint8)),

		("pos", POINTER(c_size_t)),

		("file", c_uint32),

		("buffer", c_uint8),

		("capacity", c_uint8),
	]

class exi_string_t(Structure):
	_fields_=[
		("size", c_size_t),
		("characters", c_char_p),
		("len", c_size_t)
	]

class exi_string_value_t(Structure):
	_fields_=[
		("type", c_uint32),

		("miss", exi_string_t),

		("localID", c_size_t),

		("globalID", c_size_t),
	]


class exi_rcs_t(Structure):
	_fields_=[
		("size", c_size_t),

		("characters", POINTER(c_uint32)),

		("codingLength", c_uint8),
	]


class exi_bytes_t(Structure):
	_fields_=[
		("size", c_size_t),

		("data", POINTER(c_uint8)),

		("len", c_size_t),
	]

class exi_integer_val_union_t(Union):
	_fields_=[
		("int8", c_int8),

		("int16", c_int16),

		("int32", c_int32),

		("int64", c_int64),

		("uint8", c_uint8),

		("uint16", c_uint16),

		("uint32", c_uint32),

		("uint64", c_uint64),

	]

class exi_integer_t(Structure):
	_fields_=[
		("type", c_uint32),

		("val", exi_integer_val_union_t)
	]


class exi_float_me_t(Structure):
	_fields_=[
		("mantissa", c_int64),

		("exponent", c_int16),

	]


class exi_decimal_t(Structure):
	_fields_=[
		("negative", c_int),

		("integral", exi_integer_t),

		("reverseFraction", exi_integer_t),
	]


class exi_datetime_t(Structure):
	_fields_=[
		("type", c_uint32),

		("year", c_int32),

		("monthDay", c_uint32),

		("time", c_uint32),

		("presenceFractionalSecs", c_int),

		("fractionalSecs", c_uint32),

		("presenceTimezone", c_int),

		("timezone", c_uint32),
	]


class exi_list_t(Structure):
	_fields_=[
		("type", c_uint32),

		("len", c_size_t),

		("datetimeType", c_uint32),
	]


class exi_eqname_t(Structure):
	_fields_=[
		("namespaceURI", c_size_t),

		("localPart", c_size_t),
	]


class exi_name_entry_t(Structure):
	_fields_=[
		("type", c_uint32),

		("id", c_size_t),

		("str", exi_string_t),
	]


class exi_qname_t(Structure):
	_fields_=[
		("uri", exi_name_entry_t),

		("localName", exi_name_entry_t),
	]


class exi_name_table_prepopulated_t(Structure):
	_fields_=[
		("len", c_size_t),

		("localNames", POINTER(c_size_t)),
	]


class exi_uri_partition_t(Structure):
	_fields_=[
		("uri", POINTER(c_char)),

		("uriID", c_size_t),
	]


class exi_localname_partition_t(Structure):
	_fields_=[
		("localName", POINTER(c_char)),

		("localNameID", c_size_t),

		("uriID", c_size_t),
	]

class exi_name_partition_entry_t(Structure):
	_fields_=[
		("uriPartition", exi_uri_partition_t), 
		
		("localNamePartition", exi_localname_partition_t)
	]

class exi_name_partition_t(Structure):
	_fields_=[
		("entry", exi_name_partition_entry_t),

		("namePartitionType", c_uint32),
	]


class exi_name_table_runtime_t(Structure):
	_fields_=[
		("namePartitionEntries", exi_name_partition_t * EXI_MAXIMUM_NUMBER_OF_NAME_PARTITION_ENTRIES),

		("addedUriEntries", c_size_t),

		("addedLocalNameEntries", c_size_t),

	]


class exi_runtime_element_t(Structure):
	_fields_=[
		("namespaceUriID", c_size_t),

		("localNameID", c_size_t),

		("numberOfProductions", c_size_t),

		("hasXsiType", c_int),

		("hasEE", c_int ),
	]


class exi_value_string_table_entry_t(Structure):
	_fields_=[
		("namespaceUriID", c_size_t),

		("localNameID", c_size_t),

		("localValueID", c_size_t),

		("str", exi_string_t),
	]


class exi_value_string_table_t(Structure):
	_fields_=[
		("size", c_size_t),

		("strs", POINTER(exi_value_string_table_entry_t)),

		("len", c_size_t),
	]


class exi_state_t(Structure):
	_fields_=[
		("grammarStack", (c_int16 * EXI_ELEMENT_STACK_SIZE)),

		("elementStack", (exi_eqname_t * EXI_ELEMENT_STACK_SIZE)),

		("stackIndex", c_size_t),

		("eventCode", c_uint32),

		("nameTablePrepopulated", POINTER(exi_name_table_prepopulated_t)),

		("nameTableRuntime", POINTER(exi_name_table_runtime_t)),

		("nextQNameID", c_size_t),

		("stringTable", POINTER(exi_value_string_table_t)),

		("numberOfRuntimeGrammars", c_size_t),

		("runtimeGrammars", (exi_runtime_element_t * MAX_NUMBER_OF_RUNTIME_ELEMENTS * 2)),
	]


class exi_value_t(Structure):
	_fields_=[
		("type", c_uint32),

		("boolean", c_int),

		("enumeration", c_uint32),

		("integer", exi_integer_t),

		("binary", exi_bytes_t),

		("str", exi_string_value_t),

		("float_me", exi_float_me_t),

		("decimal", exi_decimal_t),

		("datetime", exi_datetime_t),

		("list", exi_list_t),

		("eqname", exi_eqname_t),
	]


class iso1EVChargeParameterType(Structure):
	_fields_=[
		("DepartureTime", c_uint32),

		("DepartureTime_isUsed", c_uint, 1),
	]


class iso1DiffieHellmanPublickeyType(Structure):
	id_type = ArrayType_factory(c_uint32, "characters", iso1DiffieHellmanPublickeyType_Id_CHARACTERS_SIZE)
	content_type = ArrayType_factory(c_uint8, "bytes", iso1DiffieHellmanPublickeyType_CONTENT_BYTES_SIZE)
	
	_fields_=[
		("Id", id_type),

		("CONTENT", content_type),
	]


class iso1SASchedulesType(Structure):
	_fields_=[
		("noContent", c_int),
	]


class iso1ServiceDetailReqType(Structure):
	_fields_=[
		("ServiceID", c_uint16),
	]


class iso1RelativeTimeIntervalType(Structure):
	_fields_=[
		("start", c_uint32),

		("duration", c_uint32),

		("duration_isUsed", c_uint, 1),
	]


class iso1EMAIDType(Structure):
	id_type = ArrayType_factory(c_uint32, "characters", iso1EMAIDType_Id_CHARACTERS_SIZE)
	content_type = ArrayType_factory(c_uint32, "characters", iso1EMAIDType_CONTENT_CHARACTERS_SIZE)

	_fields_=[
		("Id", id_type),

		("CONTENT", content_type),
	]


class iso1EVStatusType(Structure):
	_fields_=[
		("noContent", c_int),
	]


class iso1EVSEChargeParameterType(Structure):
	_fields_=[
		("noContent", c_int),
	]


class iso1EVPowerDeliveryParameterType(Structure):
	_fields_=[
		("noContent", c_int),
	]


class iso1AuthorizationReqType(Structure):
	id_type = ArrayType_factory(c_uint32, "characters", iso1AuthorizationReqType_Id_CHARACTERS_SIZE)
	gen_challenge_type = ArrayType_factory(c_uint8, "bytes", iso1AuthorizationReqType_GenChallenge_BYTES_SIZE)

	_fields_=[
		("Id", id_type),

		("Id_isUsed", c_uint8, 1),

		("GenChallenge", gen_challenge_type),

		("GenChallenge_isUsed", c_uint8, 1),

	]


class iso1MeterInfoType(Structure):
	meter_id_type = ArrayType_factory(c_uint32, "characters", iso1MeterInfoType_MeterID_CHARACTERS_SIZE)
	sig_meter_reading_type = ArrayType_factory(c_uint8, "bytes", iso1MeterInfoType_SigMeterReading_BYTES_SIZE)

	_fields_=[
		("MeterID", meter_id_type),

		("MeterReading", c_uint64),

		("MeterReading_isUsed", c_uint8, 1),

		("SigMeterReading", sig_meter_reading_type),

		("SigMeterReading_isUsed", c_uint8, 1),

		("MeterStatus", c_int16),

		("MeterStatus_isUsed", c_uint8, 1),

		("TMeter", c_int64),

		("TMeter_isUsed", c_uint8, 1),

	]


class iso1ObjectType(Structure):
	id_type = ArrayType_factory(c_uint32, "characters", iso1ObjectType_Id_CHARACTERS_SIZE)
	mime_type_type = ArrayType_factory(c_uint32, "characters", iso1ObjectType_MimeType_CHARACTERS_SIZE)
	encoding_type = ArrayType_factory(c_uint32, "characters", iso1ObjectType_Encoding_CHARACTERS_SIZE)
	any_type = ArrayType_factory(c_uint32, "characters", iso1ObjectType_ANY_CHARACTERS_SIZE)

	_fields_=[
		("Id", id_type),

		("Id_isUsed", c_uint8, 1),

		("MimeType", mime_type_type),

		("MimeType_isUsed", c_uint8, 1),

		("Encoding", encoding_type),

		("Encoding_isUsed", c_uint8, 1),

		("ANY", any_type),

		("ANY_isUsed", c_uint8, 1),
	]


class iso1RSAKeyValueType(Structure):
	modulus_type = ArrayType_factory(c_uint8, "bytes", iso1RSAKeyValueType_Modulus_BYTES_SIZE)
	exponent_type = ArrayType_factory(c_uint8, "bytes", iso1RSAKeyValueType_Exponent_BYTES_SIZE)

	_fields_=[
		("Modulus", modulus_type),

		("Exponent", exponent_type),
	]


class iso1SessionStopResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),
	]


class iso1SignatureValueType(Structure):
	id_type = ArrayType_factory(c_uint32, "characters", iso1SignatureValueType_Id_CHARACTERS_SIZE)
	content_type = ArrayType_factory(c_uint8, "bytes", iso1SignatureValueType_CONTENT_BYTES_SIZE)

	_fields_=[
		("Id", id_type),

		("Id_isUsed", c_uint, 1),

		("CONTENT", content_type),
	]


class iso1SubCertificatesType(Structure):
	certificate_type = ArrayType_factory(ArrayType_factory(c_uint8, "bytes", iso1SubCertificatesType_Certificate_BYTES_SIZE), "array", iso1SubCertificatesType_Certificate_ARRAY_SIZE)

	_fields_=[
		("Certificate", certificate_type),
	]


class iso1DSAKeyValueType(Structure):
	p_type = ArrayType_factory(c_uint8, "bytes", iso1DSAKeyValueType_P_BYTES_SIZE)
	q_type = ArrayType_factory(c_uint8, "bytes", iso1DSAKeyValueType_Q_BYTES_SIZE)
	g_type = ArrayType_factory(c_uint8, "bytes", iso1DSAKeyValueType_G_BYTES_SIZE)
	y_type = ArrayType_factory(c_uint8, "bytes", iso1DSAKeyValueType_Y_BYTES_SIZE)
	j_type = ArrayType_factory(c_uint8, "bytes", iso1DSAKeyValueType_J_BYTES_SIZE)
	seed_type = ArrayType_factory(c_uint8, "bytes", iso1DSAKeyValueType_Seed_BYTES_SIZE)
	pgen_counter_type = ArrayType_factory(c_uint8, "bytes", iso1DSAKeyValueType_PgenCounter_BYTES_SIZE)

	_fields_=[
		("P", p_type),

		("P_isUsed", c_uint8, 1),

		("Q", q_type),

		("Q_isUsed", c_uint8, 1),

		("G", g_type),

		("G_isUsed", c_uint8, 1),

		("Y", y_type),

		("J", j_type),

		("J_isUsed", c_uint8, 1),

		("Seed", seed_type),

		("Seed_isUsed", c_uint8, 1),

		("PgenCounter", pgen_counter_type),

		("PgenCounter_isUsed", c_uint8, 1),
	]


class iso1IntervalType(Structure):
	_fields_=[
		("noContent", c_int),
	]


class iso1MeteringReceiptReqType(Structure):
	session_id_type = ArrayType_factory(c_uint8, "bytes", iso1MeteringReceiptReqType_SessionID_BYTES_SIZE)
	id_type = ArrayType_factory(c_uint32, "characters", iso1MeteringReceiptReqType_Id_CHARACTERS_SIZE)

	_fields_=[
		("Id", id_type),

		("Id_isUsed", c_uint8, 1),

		("SessionID", session_id_type),

		("SAScheduleTupleID", c_uint8),

		("SAScheduleTupleID_isUsed", c_uint8, 1),

		("MeterInfo", iso1MeterInfoType),
	]


class iso1KeyValueType(Structure):
	any_type = ArrayType_factory(c_uint32, "characters", iso1KeyValueType_ANY_CHARACTERS_SIZE)

	_fields_=[
		("DSAKeyValue", iso1DSAKeyValueType),

		("DSAKeyValue_isUsed", c_uint8, 1),

		("RSAKeyValue", iso1RSAKeyValueType),

		("RSAKeyValue_isUsed", c_uint8, 1),

		("ANY", any_type),

		("ANY_isUsed", c_uint8, 1),

	]


class iso1X509IssuerSerialType(Structure):
	x509_issuer_name_type = ArrayType_factory(c_uint32, "characters", iso1X509IssuerSerialType_X509IssuerName_CHARACTERS_SIZE)
	
	_fields_=[
		("X509IssuerName", x509_issuer_name_type),

		("X509SerialNumber", c_int64),

	]


class iso1EVSEStatusType(Structure):
	_fields_=[
		("NotificationMaxDelay", c_uint16),

		("EVSENotification", c_uint),
	]


class iso1SignatureMethodType(Structure):
	algorithm_type = ArrayType_factory(c_uint32, "characters", iso1SignatureMethodType_Algorithm_CHARACTERS_SIZE)
	any_type = ArrayType_factory(c_uint32, "characters", iso1SignatureMethodType_ANY_CHARACTERS_SIZE)

	_fields_=[
		("Algorithm", algorithm_type),

		("HMACOutputLength", c_int64),

		("HMACOutputLength_isUsed", c_uint8, 1),

		("ANY", any_type),

		("ANY_isUsed", c_uint8, 1),
	]


class iso1X509DataType(Structure):
	x509_issuer_serial_type = ArrayType_factory(iso1X509IssuerSerialType, "array", iso1X509DataType_X509IssuerSerial_ARRAY_SIZE)
	x509_ski_type = ArrayType_factory(ArrayType_factory(c_uint8, "bytes", iso1X509DataType_X509SKI_BYTES_SIZE), "array", dinX509DataType_X509SKI_ARRAY_SIZE)
	x509_subject_name_type = ArrayType_factory(ArrayType_factory(c_uint32, "characters", iso1X509DataType_X509SubjectName_CHARACTERS_SIZE), "array", dinX509DataType_X509SubjectName_ARRAY_SIZE)
	x509_certificate_type = ArrayType_factory(ArrayType_factory(c_uint8, "bytes", iso1X509DataType_X509Certificate_BYTES_SIZE), "array", dinX509DataType_X509Certificate_ARRAY_SIZE)
	x509_crl_type = ArrayType_factory(ArrayType_factory(c_uint8, "bytes", iso1X509DataType_X509CRL_BYTES_SIZE), "array", dinX509DataType_X509CRL_ARRAY_SIZE)
	any_type = ArrayType_factory(c_uint32, "characters", iso1X509DataType_ANY_CHARACTERS_SIZE)

	_fields_=[
		
		("X509IssuerSerial", x509_issuer_serial_type),

		("X509SKI", x509_ski_type),

		("X509SubjectName", x509_subject_name_type),

		("X509Certificate", x509_certificate_type),

		("X509CRL", x509_crl_type),

		("ANY", any_type),

		("ANY_isUsed", c_uint, 1),
	]


class iso1NotificationType(Structure):
	fault_msg_type = ArrayType_factory(c_uint32, "characters", iso1NotificationType_FaultMsg_CHARACTERS_SIZE)

	_fields_=[
		("FaultCode", c_uint),

		("FaultMsg", fault_msg_type),

		("FaultMsg_isUsed", c_uint, 1),
	]


class iso1TransformType(Structure):
	algorithm_type = ArrayType_factory(c_uint32, "characters", iso1TransformType_Algorithm_CHARACTERS_SIZE)
	any_type = ArrayType_factory(c_uint32, "characters", iso1TransformType_ANY_CHARACTERS_SIZE)
	xpath_type = ArrayType_factory(ArrayType_factory(c_uint32, "characters", iso1TransformType_XPath_CHARACTERS_SIZE), "array", dinTransformType_XPath_ARRAY_SIZE)

	_fields_=[
		("Algorithm", algorithm_type),

		("ANY", any_type),

		("ANY_isUsed", c_uint, 1),

		("XPath", xpath_type),
	]


class iso1PaymentDetailsResType(Structure):
	gen_challenge_type = ArrayType_factory(c_ubyte, "bytes", iso1PaymentDetailsResType_GenChallenge_BYTES_SIZE)

	_fields_=[
		("ResponseCode", c_uint),

		("GenChallenge", gen_challenge_type),

		("EVSETimeStamp", c_int64),
	]


class iso1ContractSignatureEncryptedPrivateKeyType(Structure):
	id_type = ArrayType_factory(c_uint32, "characters", iso1ContractSignatureEncryptedPrivateKeyType_Id_CHARACTERS_SIZE)
	content_type = ArrayType_factory(c_uint8, "bytes", iso1ContractSignatureEncryptedPrivateKeyType_CONTENT_BYTES_SIZE)

	_fields_=[
		("Id", id_type),

		("CONTENT", content_type),
	]


class iso1SPKIDataType(Structure):
	any_type = ArrayType_factory(c_uint32, "characters", iso1SPKIDataType_ANY_CHARACTERS_SIZE)
	spki_exp_type = ArrayType_factory(ArrayType_factory(c_uint8, "bytes", iso1SPKIDataType_SPKISexp_BYTES_SIZE), "array", dinSPKIDataType_SPKISexp_ARRAY_SIZE)

	_fields_=[
		("SPKISexp", spki_exp_type),

		("ANY", any_type),

		("ANY_isUsed", c_uint, 1),
	]


class iso1SessionStopReqType(Structure):
	_fields_=[
		("ChargingSession", c_uint),
	]


class iso1EntryType(Structure):
	_fields_=[
		("TimeInterval", iso1IntervalType),

		("RelativeTimeInterval", iso1RelativeTimeIntervalType),

		("TimeInterval_isUsed", c_uint, 1),

		("RelativeTimeInterval_isUsed", c_uint, 1),

	]


class iso1SessionSetupReqType(Structure):
	evccid_type = ArrayType_factory(c_uint8, "bytes", iso1SessionSetupReqType_EVCCID_BYTES_SIZE)

	_fields_=[
		("EVCCID", evccid_type),
	]


class iso1CanonicalizationMethodType(Structure):
	algorithm_type = ArrayType_factory(c_uint32, "characters", iso1CanonicalizationMethodType_Algorithm_CHARACTERS_SIZE)
	any_type = ArrayType_factory(c_uint32, "characters", iso1CanonicalizationMethodType_ANY_CHARACTERS_SIZE)

	_fields_=[
		("Algorithm", algorithm_type),

		("ANY", any_type),

		("ANY_isUsed", c_uint, 1),
	]


class iso1DC_EVStatusType(Structure):
	_fields_=[
		("EVReady", c_int),

		("EVErrorCode", c_uint),

		("EVRESSSOC", c_int8),
	]


class iso1ServiceType(Structure):
	service_name_type = ArrayType_factory(c_uint32, "characters", iso1ServiceType_ServiceName_CHARACTERS_SIZE)
	service_scope_type = ArrayType_factory(c_uint32, "characters", iso1ServiceType_ServiceScope_CHARACTERS_SIZE)

	_fields_=[
		("ServiceID", c_uint16),

		("ServiceName", service_name_type),

		("ServiceName_isUsed", c_uint, 1),

		("ServiceCategory", c_uint),

		("ServiceScope", service_scope_type),

		("ServiceScope_isUsed", c_uint, 1),

		("FreeService", c_int),
	]


class iso1ServiceDiscoveryReqType(Structure):
	service_scope_type = ArrayType_factory(c_uint32, "characters", iso1ServiceDiscoveryReqType_ServiceScope_CHARACTERS_SIZE)

	_fields_=[
		("ServiceScope", service_scope_type),

		("ServiceScope_isUsed", c_uint, 1),

		("ServiceCategory", c_uint),

		("ServiceCategory_isUsed", c_uint, 1),
	]


class iso1CableCheckReqType(Structure):
	_fields_=[
		("DC_EVStatus", iso1DC_EVStatusType),
	]


class iso1SelectedServiceType(Structure):
	_fields_=[
		("ServiceID", c_uint16),

		("ParameterSetID", c_int16),

		("ParameterSetID_isUsed", c_uint, 1),
	]


class iso1AC_EVSEStatusType(Structure):
	_fields_=[
		("NotificationMaxDelay", c_uint16),

		("EVSENotification", c_uint),

		("RCD", c_int),
	]


class iso1BodyBaseType(Structure):
	_fields_=[
		("noContent", c_int),
	]


class iso1SupportedEnergyTransferModeType(Structure):
	energy_transfer_mode_type = ArrayType_factory(c_uint32, "array", iso1SupportedEnergyTransferModeType_EnergyTransferMode_ARRAY_SIZE)

	_fields_=[
		("EnergyTransferMode", energy_transfer_mode_type),
	]


class iso1ChargingStatusReqType(Structure):
	_fields_=[
		("noContent", c_int),
	]


class iso1PaymentServiceSelectionResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),
	]


class iso1DigestMethodType(Structure):
	algorithm_type = ArrayType_factory(c_uint32, "characters", iso1DigestMethodType_Algorithm_CHARACTERS_SIZE)
	any_type = ArrayType_factory(c_uint32, "characters", iso1DigestMethodType_ANY_CHARACTERS_SIZE)

	_fields_=[
		("Algorithm", algorithm_type),

		("ANY", any_type),

		("ANY_isUsed", c_uint, 1),
	]


class iso1SignaturePropertyType(Structure):
	target_type = ArrayType_factory(c_uint32, "characters", iso1SignaturePropertyType_Target_CHARACTERS_SIZE)
	id_type = ArrayType_factory(c_uint32, "characters", iso1SignaturePropertyType_Id_CHARACTERS_SIZE)
	any_type = ArrayType_factory(c_uint32, "characters", iso1SignaturePropertyType_ANY_CHARACTERS_SIZE) 

	_fields_=[
		("Target", target_type),

		("Id", id_type),

		("Id_isUsed", c_uint, 1),

		("ANY", any_type),

		("ANY_isUsed", c_uint, 1),
	]


class iso1PGPDataType(Structure):
	pgp_key_id_type = ArrayType_factory(c_uint8, "bytes", iso1PGPDataType_PGPKeyID_BYTES_SIZE)
	pgp_key_packet_type = ArrayType_factory(c_uint8, "bytes", iso1PGPDataType_PGPKeyPacket_BYTES_SIZE)
	any_type = ArrayType_factory(c_uint32, "characters", iso1PGPDataType_ANY_CHARACTERS_SIZE)

	_fields_=[
		("PGPKeyID", pgp_key_id_type),

		("PGPKeyID_isUsed", c_uint8, 1),

		("PGPKeyPacket", pgp_key_packet_type),

		("PGPKeyPacket_isUsed", c_uint8, 1),

		("ANY", any_type),

		("ANY_isUsed", c_uint8, 1),
	]


class iso1SessionSetupResType(Structure):
	evse_id_type = ArrayType_factory(c_uint32, "characters", iso1SessionSetupResType_EVSEID_CHARACTERS_SIZE)

	_fields_=[
		("ResponseCode", c_uint),

		("EVSEID", evse_id_type),

		("EVSETimeStamp", c_int64),

		("EVSETimeStamp_isUsed", c_uint, 1),

	]


class iso1CertificateChainType(Structure):
	id_type = ArrayType_factory(c_uint32, "characters", iso1CertificateChainType_Id_CHARACTERS_SIZE)
	certificate_type = ArrayType_factory(c_uint8, "bytes", iso1CertificateChainType_Certificate_BYTES_SIZE)

	_fields_=[
		("Id", id_type),

		("Id_isUsed", c_uint8, 1),

		("Certificate", certificate_type),

		("SubCertificates", iso1SubCertificatesType),

		("SubCertificates_isUsed", c_uint8, 1),
	]


class iso1DC_EVSEStatusType(Structure):
	_fields_=[
		("NotificationMaxDelay", c_uint16),

		("EVSENotification", c_uint),

		("EVSEIsolationStatus", c_uint),

		("EVSEIsolationStatus_isUsed", c_uint, 1),

		("EVSEStatusCode", c_uint),
	]


class iso1ServiceListType(Structure):
	service_type = ArrayType_factory(iso1ServiceType, "array", iso1ServiceListType_Service_ARRAY_SIZE)

	_fields_=[
		("Service", service_type),
	]


class iso1PowerDeliveryResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),

		("EVSEStatus", iso1EVSEStatusType),

		("EVSEStatus_isUsed", c_uint, 1),

		("AC_EVSEStatus", iso1AC_EVSEStatusType),

		("AC_EVSEStatus_isUsed", c_uint, 1),

		("DC_EVSEStatus", iso1DC_EVSEStatusType),

		("DC_EVSEStatus_isUsed", c_uint, 1),
	]


class iso1PaymentOptionListType(Structure):
	payment_option_type = ArrayType_factory(c_uint32, "array", iso1PaymentOptionListType_PaymentOption_ARRAY_SIZE)

	_fields_=[
		("PaymentOption", payment_option_type),
	]


class iso1PhysicalValueType(Structure):
	_fields_=[
		("Multiplier", c_int8),

		("Unit", c_uint),

		("Value", c_int16),
	]


class iso1PaymentDetailsReqType(Structure):
	emaid_type = ArrayType_factory(c_uint32, "characters", iso1PaymentDetailsReqType_eMAID_CHARACTERS_SIZE)

	_fields_=[
		("eMAID", emaid_type),

		("ContractSignatureCertChain", iso1CertificateChainType),
	]


class iso1AuthorizationResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),

		("EVSEProcessing", c_uint),
	]


class iso1DC_EVSEChargeParameterType(Structure):
	_fields_=[
		("DC_EVSEStatus", iso1DC_EVSEStatusType),

		("EVSEMaximumCurrentLimit", iso1PhysicalValueType),

		("EVSEMaximumPowerLimit", iso1PhysicalValueType),

		("EVSEMaximumVoltageLimit", iso1PhysicalValueType),

		("EVSEMinimumCurrentLimit", iso1PhysicalValueType),

		("EVSEMinimumVoltageLimit", iso1PhysicalValueType),

		("EVSECurrentRegulationTolerance", iso1PhysicalValueType),

		("EVSECurrentRegulationTolerance_isUsed", c_uint, 1),

		("EVSEPeakCurrentRipple", iso1PhysicalValueType),

		("EVSEEnergyToBeDelivered", iso1PhysicalValueType),

		("EVSEEnergyToBeDelivered_isUsed", c_uint, 1),
	]


class iso1ChargingStatusResType(Structure):
	evse_id_type = ArrayType_factory(c_uint32, "characters", iso1ChargingStatusResType_EVSEID_CHARACTERS_SIZE)
	
	_fields_=[
		("ResponseCode", c_uint),

		("EVSEID", evse_id_type),

		("SAScheduleTupleID", c_uint8),

		("EVSEMaxCurrent", iso1PhysicalValueType),

		("EVSEMaxCurrent_isUsed", c_uint, 1),

		("MeterInfo", iso1MeterInfoType),

		("MeterInfo_isUsed", c_uint, 1),

		("ReceiptRequired", c_int),

		("ReceiptRequired_isUsed", c_uint, 1),

		("AC_EVSEStatus", iso1AC_EVSEStatusType),
	]


class iso1ListOfRootCertificateIDsType(Structure):
	root_certificate_id_type = ArrayType_factory(iso1X509IssuerSerialType, "array", iso1ListOfRootCertificateIDsType_RootCertificateID_ARRAY_SIZE)

	_fields_=[
		("RootCertificateID", root_certificate_id_type),
	]


class iso1ChargeServiceType(Structure):
	service_scope_type = ArrayType_factory(c_uint32, "characters", iso1ChargeServiceType_ServiceScope_CHARACTERS_SIZE)
	service_name_type = ArrayType_factory(c_uint32, "characters", iso1ChargeServiceType_ServiceName_CHARACTERS_SIZE)

	_fields_=[
		("ServiceID", c_uint16),

		("ServiceName", service_name_type),

		("ServiceName_isUsed", c_uint, 1),

		("ServiceCategory", c_uint),

		("ServiceScope", service_scope_type),

		("ServiceScope_isUsed", c_uint, 1),

		("FreeService", c_int),

		("SupportedEnergyTransferMode", iso1SupportedEnergyTransferModeType),
	]


class iso1SelectedServiceListType(Structure):
	selected_service_type = ArrayType_factory(iso1SelectedServiceType, "array", iso1SelectedServiceListType_SelectedService_ARRAY_SIZE)

	_fields_=[
		("SelectedService", selected_service_type),
	]


class iso1CableCheckResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),

		("DC_EVSEStatus", iso1DC_EVSEStatusType),

		("EVSEProcessing", c_uint),
	]


class iso1TransformsType(Structure):
	transform_type = ArrayType_factory(iso1TransformType, "array", iso1TransformsType_Transform_ARRAY_SIZE)
	
	_fields_=[
		("Transform", transform_type),
	]


class iso1PreChargeReqType(Structure):
	_fields_=[
		("DC_EVStatus", iso1DC_EVStatusType),

		("EVTargetVoltage", iso1PhysicalValueType),

		("EVTargetCurrent", iso1PhysicalValueType),
	]


class iso1AC_EVChargeParameterType(Structure):
	_fields_=[
		("DepartureTime", c_uint32),

		("DepartureTime_isUsed", c_uint, 1),

		("EAmount", iso1PhysicalValueType),

		("EVMaxVoltage", iso1PhysicalValueType),

		("EVMaxCurrent", iso1PhysicalValueType),

		("EVMinCurrent", iso1PhysicalValueType),
	]


class iso1PMaxScheduleEntryType(Structure):
	_fields_=[
		("TimeInterval", iso1IntervalType),

		("TimeInterval_isUsed", c_uint, 1),

		("RelativeTimeInterval", iso1RelativeTimeIntervalType),

		("RelativeTimeInterval_isUsed", c_uint, 1),

		("PMax", iso1PhysicalValueType),
	]


class iso1MeteringReceiptResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),

		("EVSEStatus", iso1EVSEStatusType),

		("EVSEStatus_isUsed", c_uint, 1),

		("AC_EVSEStatus", iso1AC_EVSEStatusType),

		("AC_EVSEStatus_isUsed", c_uint, 1),

		("DC_EVSEStatus", iso1DC_EVSEStatusType),

		("DC_EVSEStatus_isUsed", c_uint, 1),
	]


class iso1WeldingDetectionResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),

		("DC_EVSEStatus", iso1DC_EVSEStatusType),

		("EVSEPresentVoltage", iso1PhysicalValueType),
	]


class iso1ReferenceType(Structure):
	id_type = ArrayType_factory(c_uint32, "characters", iso1ReferenceType_Id_CHARACTERS_SIZE)
	uri_type = ArrayType_factory(c_uint32, "characters", iso1ReferenceType_URI_CHARACTERS_SIZE)
	type_type = ArrayType_factory(c_uint32, "characters", iso1ReferenceType_Type_CHARACTERS_SIZE)
	digest_value_type = ArrayType_factory(c_uint8, "bytes", iso1ReferenceType_DigestValue_BYTES_SIZE)

	_fields_=[
		("Id", id_type),

		("Id_isUsed", c_uint, 1),

		("URI", uri_type),

		("URI_isUsed", c_uint, 1),

		("Type", type_type),

		("Type_isUsed", c_uint, 1),

		("Transforms", iso1TransformsType),

		("Transforms_isUsed", c_uint, 1),

		("DigestMethod", iso1DigestMethodType),

		("DigestValue", digest_value_type),
	]


class iso1CurrentDemandReqType(Structure):
	_fields_=[
		("DC_EVStatus", iso1DC_EVStatusType),

		("EVTargetCurrent", iso1PhysicalValueType),

		("EVMaximumVoltageLimit", iso1PhysicalValueType),

		("EVMaximumVoltageLimit_isUsed", c_uint, 1),

		("EVMaximumCurrentLimit", iso1PhysicalValueType),

		("EVMaximumCurrentLimit_isUsed", c_uint, 1),

		("EVMaximumPowerLimit", iso1PhysicalValueType),

		("EVMaximumPowerLimit_isUsed", c_uint, 1),

		("BulkChargingComplete", c_int),

		("BulkChargingComplete_isUsed", c_uint, 1),

		("ChargingComplete", c_int),

		("RemainingTimeToFullSoC", iso1PhysicalValueType),

		("RemainingTimeToFullSoC_isUsed", c_uint, 1),

		("RemainingTimeToBulkSoC", iso1PhysicalValueType),

		("RemainingTimeToBulkSoC_isUsed", c_uint, 1),

		("EVTargetVoltage", iso1PhysicalValueType),
	]


class iso1CostType(Structure):
	_fields_=[
		("costKind", c_uint),

		("amount", c_uint32),

		("amountMultiplier", c_int8),

		("amountMultiplier_isUsed", c_uint8, 1),
	]


class iso1DC_EVPowerDeliveryParameterType(Structure):
	_fields_=[
		("DC_EVStatus", iso1DC_EVStatusType),

		("BulkChargingComplete", c_int),

		("BulkChargingComplete_isUsed", c_uint, 1),

		("ChargingComplete", c_int),
	]


class iso1RetrievalMethodType(Structure):
	uri_type = ArrayType_factory(c_uint32, "characters", iso1RetrievalMethodType_URI_CHARACTERS_SIZE)
	type_type = ArrayType_factory(c_uint32, "characters", iso1RetrievalMethodType_Type_CHARACTERS_SIZE)

	_fields_=[
		("URI", uri_type),

		("URI_isUsed", c_uint, 1),

		("Type", type_type),

		("Type_isUsed", c_uint, 1),

		("Transforms", iso1TransformsType),

		("Transforms_isUsed", c_uint, 1),


	]


class iso1CertificateUpdateResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),

		("SAProvisioningCertificateChain", iso1CertificateChainType),

		("ContractSignatureCertChain", iso1CertificateChainType),

		("ContractSignatureEncryptedPrivateKey", iso1ContractSignatureEncryptedPrivateKeyType),

		("DHpublickey", iso1DiffieHellmanPublickeyType),

		("eMAID", iso1EMAIDType),

		("RetryCounter", c_int16),

		("RetryCounter_isUsed", c_uint8, 1),
	]


class iso1CertificateInstallationResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),

		("SAProvisioningCertificateChain", iso1CertificateChainType),

		("ContractSignatureCertChain", iso1CertificateChainType),

		("ContractSignatureEncryptedPrivateKey", iso1ContractSignatureEncryptedPrivateKeyType),

		("DHpublickey", iso1DiffieHellmanPublickeyType),

		("eMAID", iso1EMAIDType),
	]


class iso1WeldingDetectionReqType(Structure):
	_fields_=[
		("DC_EVStatus", iso1DC_EVStatusType),
	]


class iso1CurrentDemandResType(Structure):
	evse_id_type = ArrayType_factory(c_uint32, "characters", iso1CurrentDemandResType_EVSEID_CHARACTERS_SIZE)

	_fields_=[
		("ResponseCode", c_uint),

		("DC_EVSEStatus", iso1DC_EVSEStatusType),

		("EVSEPresentVoltage", iso1PhysicalValueType),

		("EVSEPresentCurrent", iso1PhysicalValueType),

		("EVSECurrentLimitAchieved", c_int),

		("EVSEVoltageLimitAchieved", c_int),

		("EVSEPowerLimitAchieved", c_int),

		("EVSEMaximumVoltageLimit", iso1PhysicalValueType),

		("EVSEMaximumVoltageLimit_isUsed", c_uint, 1),

		("EVSEMaximumCurrentLimit", iso1PhysicalValueType),

		("EVSEMaximumCurrentLimit_isUsed", c_uint, 1),

		("EVSEMaximumPowerLimit", iso1PhysicalValueType),

		("EVSEMaximumPowerLimit_isUsed", c_uint, 1),

		("EVSEID", evse_id_type),

		("SAScheduleTupleID", c_uint8),

		("MeterInfo", iso1MeterInfoType),

		("MeterInfo_isUsed", c_uint, 1),

		("ReceiptRequired", c_int),

		("ReceiptRequired_isUsed", c_uint, 1),

	]


class iso1AC_EVSEChargeParameterType(Structure):
	_fields_=[
		("AC_EVSEStatus", iso1AC_EVSEStatusType),

		("EVSENominalVoltage", iso1PhysicalValueType),

		("EVSEMaxCurrent", iso1PhysicalValueType),
	]


class iso1PaymentServiceSelectionReqType(Structure):
	_fields_=[
		("SelectedPaymentOption", c_uint),

		("SelectedServiceList", iso1SelectedServiceListType),
	]


class iso1SignaturePropertiesType(Structure):
	id_type = ArrayType_factory(c_uint32, "characters", iso1SignaturePropertiesType_Id_CHARACTERS_SIZE)
	signature_property_type = ArrayType_factory(iso1SignaturePropertyType, "array", iso1SignaturePropertiesType_SignatureProperty_ARRAY_SIZE)

	_fields_=[
		("Id", id_type),

		("Id_isUsed", c_uint, 1),

		("SignatureProperty", signature_property_type),
	]


class iso1ParameterType(Structure):
	string_value_type = ArrayType_factory(c_uint32, "characters", iso1ParameterType_stringValue_CHARACTERS_SIZE)
	name_type = ArrayType_factory(c_uint32, "characters", iso1ParameterType_Name_CHARACTERS_SIZE)

	_fields_=[
		("Name", name_type),

		("boolValue", c_int),

		("boolValue_isUsed", c_uint8, 1),

		("byteValue", c_int8),

		("byteValue_isUsed", c_uint8, 1),

		("shortValue", c_int16),

		("shortValue_isUsed", c_uint8, 1),

		("intValue", c_int32),

		("intValue_isUsed", c_uint8, 1),

		("physicalValue", iso1PhysicalValueType),

		("physicalValue_isUsed", c_uint8, 1),

		("stringValue", string_value_type),

		("stringValue_isUsed", c_uint8, 1),
	]


class iso1CertificateInstallationReqType(Structure):
	id_type = ArrayType_factory(c_uint32, "characters", iso1CertificateInstallationReqType_Id_CHARACTERS_SIZE)
	oem_provisioning_cert_type = ArrayType_factory(c_uint8, "bytes", iso1CertificateInstallationReqType_OEMProvisioningCert_BYTES_SIZE)
	
	_fields_=[
		("Id", id_type),

		("OEMProvisioningCert", oem_provisioning_cert_type),

		("ListOfRootCertificateIDs", iso1ListOfRootCertificateIDsType),


	]


class iso1ServiceDiscoveryResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),

		("PaymentOptionList", iso1PaymentOptionListType),

		("ChargeService", iso1ChargeServiceType),

		("ServiceList", iso1ServiceListType),

		("ServiceList_isUsed", c_uint, 1),
	]


class iso1PreChargeResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),

		("DC_EVSEStatus", iso1DC_EVSEStatusType),

		("EVSEPresentVoltage", iso1PhysicalValueType),
	]


class iso1ParameterSetType(Structure):
	parameter_type = ArrayType_factory(iso1ParameterType, "array", iso1ParameterSetType_Parameter_ARRAY_SIZE)

	_fields_=[
		("ParameterSetID", c_int16),

		("Parameter", parameter_type),
	]


class iso1SignedInfoType(Structure):
	id_type = ArrayType_factory(c_uint32, "characters", iso1SignedInfoType_Id_CHARACTERS_SIZE)
	reference_type = ArrayType_factory(iso1ReferenceType, "array", iso1SignedInfoType_Reference_ARRAY_SIZE)

	_fields_=[
		("Id", id_type),

		("Id_isUsed", c_uint, 1),

		("CanonicalizationMethod", iso1CanonicalizationMethodType),

		("SignatureMethod", iso1SignatureMethodType),

		("Reference", reference_type),
	]


class iso1ProfileEntryType(Structure):
	_fields_=[
		("ChargingProfileEntryStart", c_uint32),

		("ChargingProfileEntryMaxPower", iso1PhysicalValueType),

		("ChargingProfileEntryMaxNumberOfPhasesInUse", c_int8),

		("ChargingProfileEntryMaxNumberOfPhasesInUse_isUsed", c_uint8, 1),
	]


class iso1ManifestType(Structure):
	id_type = ArrayType_factory(c_uint32, "characters", iso1ManifestType_Id_CHARACTERS_SIZE)
	reference_type = ArrayType_factory(iso1ReferenceType, "array", iso1ManifestType_Reference_ARRAY_SIZE)

	_fields_=[
		("Id", id_type),

		("Id_isUsed", c_uint, 1),

		("Reference", reference_type),
	]


class iso1DC_EVChargeParameterType(Structure):
	_fields_=[
		("DepartureTime", c_uint32),

		("DepartureTime_isUsed", c_uint8, 1),

		("DC_EVStatus", iso1DC_EVStatusType),

		("EVMaximumCurrentLimit", iso1PhysicalValueType),

		("EVMaximumPowerLimit", iso1PhysicalValueType),

		("EVMaximumPowerLimit_isUsed", c_uint8, 1),

		("EVMaximumVoltageLimit", iso1PhysicalValueType),

		("EVEnergyCapacity", iso1PhysicalValueType),

		("EVEnergyCapacity_isUsed", c_uint8, 1),

		("EVEnergyRequest", iso1PhysicalValueType),

		("EVEnergyRequest_isUsed", c_uint8, 1),

		("FullSOC", c_int8),

		("FullSOC_isUsed", c_uint8, 1),

		("BulkSOC", c_int8),

		("BulkSOC_isUsed", c_uint8, 1),
	]


class iso1ConsumptionCostType(Structure):
	cost_type = ArrayType_factory(iso1CostType, "array", iso1ConsumptionCostType_Cost_ARRAY_SIZE)

	_fields_=[
		("startValue", iso1PhysicalValueType),

		("Cost", cost_type),
	]


class iso1PMaxScheduleType(Structure):
	pmax_schedule_entry_type = ArrayType_factory(iso1PMaxScheduleEntryType, "array", iso1PMaxScheduleType_PMaxScheduleEntry_ARRAY_SIZE)

	_fields_=[
		("PMaxScheduleEntry", pmax_schedule_entry_type),
	]


class iso1CertificateUpdateReqType(Structure):
	id_type = ArrayType_factory(c_uint32, "characters", iso1CertificateUpdateReqType_Id_CHARACTERS_SIZE)
	emaid_type = ArrayType_factory(c_uint32, "characters", iso1CertificateUpdateReqType_eMAID_CHARACTERS_SIZE)

	_fields_=[
		("Id", id_type),

		("ContractSignatureCertChain", iso1CertificateChainType),

		("eMAID", emaid_type),

		("ListOfRootCertificateIDs", iso1ListOfRootCertificateIDsType),
	]


class iso1KeyInfoType(Structure):
	id_type = ArrayType_factory(c_uint32, "characters", iso1KeyInfoType_Id_CHARACTERS_SIZE)
	key_name_type = ArrayType_factory(ArrayType_factory(c_uint32, "characters", iso1KeyInfoType_KeyName_CHARACTERS_SIZE), "array", iso1KeyInfoType_KeyName_ARRAY_SIZE)
	key_value_type = ArrayType_factory(iso1KeyValueType, "array", iso1KeyInfoType_KeyValue_ARRAY_SIZE)
	retrieval_method_type = ArrayType_factory(iso1RetrievalMethodType, "array", iso1KeyInfoType_RetrievalMethod_ARRAY_SIZE)
	x509_data_type = ArrayType_factory(iso1X509DataType, "array", iso1KeyInfoType_X509Data_ARRAY_SIZE)
	pgp_data_type = ArrayType_factory(iso1PGPDataType, "array", iso1KeyInfoType_PGPData_ARRAY_SIZE)
	spki_data_type = ArrayType_factory(iso1SPKIDataType, "array", iso1KeyInfoType_SPKIData_ARRAY_SIZE)
	mgmt_data_type = ArrayType_factory(ArrayType_factory(c_uint32, "characters", iso1KeyInfoType_MgmtData_CHARACTERS_SIZE), "array", iso1KeyInfoType_MgmtData_ARRAY_SIZE)
	any_type = ArrayType_factory(c_uint32, "characters", iso1KeyInfoType_ANY_CHARACTERS_SIZE)

	_fields_=[
		("Id", id_type),

		("Id_isUsed", c_uint, 1),

		("KeyName", key_name_type),

		("KeyValue", key_value_type),

		("RetrievalMethod", retrieval_method_type),

		("X509Data", x509_data_type),

		("PGPData", pgp_data_type),

		("SPKIData", spki_data_type),

		("MgmtData", mgmt_data_type),

		("ANY", any_type),

		("ANY_isUsed", c_uint, 1),
	]


class iso1ChargeParameterDiscoveryReqType(Structure):
	_fields_=[
		("MaxEntriesSAScheduleTuple", c_uint16),

		("MaxEntriesSAScheduleTuple_isUsed", c_uint8, 1),

		("RequestedEnergyTransferMode", c_uint),

		("EVChargeParameter", iso1EVChargeParameterType),

		("EVChargeParameter_isUsed", c_uint8, 1),

		("AC_EVChargeParameter", iso1AC_EVChargeParameterType),

		("AC_EVChargeParameter_isUsed", c_uint8, 1),

		("DC_EVChargeParameter", iso1DC_EVChargeParameterType),

		("DC_EVChargeParameter_isUsed", c_uint8, 1),
	]


class iso1ChargingProfileType(Structure):
	profile_entry_type = ArrayType_factory(iso1ProfileEntryType, "array", iso1ChargingProfileType_ProfileEntry_ARRAY_SIZE)

	_fields_=[
		("ProfileEntry", profile_entry_type),
	]


class iso1SalesTariffEntryType(Structure):
	consumption_cost_type = ArrayType_factory(iso1ConsumptionCostType, "array", iso1SalesTariffEntryType_ConsumptionCost_ARRAY_SIZE)

	_fields_=[
		("TimeInterval", iso1IntervalType),

		("TimeInterval_isUsed", c_uint8, 1),

		("RelativeTimeInterval", iso1RelativeTimeIntervalType),

		("RelativeTimeInterval_isUsed", c_uint8, 1),

		("EPriceLevel", c_uint8),

		("EPriceLevel_isUsed", c_uint8, 1),

		("ConsumptionCost", consumption_cost_type),
	]


class iso1SalesTariffType(Structure):
	id_type = ArrayType_factory(c_uint32, "characters", iso1SalesTariffType_Id_CHARACTERS_SIZE)
	sales_tariff_description_type = ArrayType_factory(c_uint32, "characters", iso1SalesTariffType_SalesTariffDescription_CHARACTERS_SIZE)
	sales_tariff_entry_type = ArrayType_factory(iso1SalesTariffEntryType, "array", iso1SalesTariffType_SalesTariffEntry_ARRAY_SIZE)

	_fields_=[
		("Id", id_type),

		("Id_isUsed", c_uint8, 1),

		("SalesTariffID", c_uint8),

		("SalesTariffDescription", sales_tariff_description_type),

		("SalesTariffDescription_isUsed", c_uint8, 1),

		("NumEPriceLevels", c_uint8),

		("NumEPriceLevels_isUsed", c_uint8, 1),

		("SalesTariffEntry", sales_tariff_entry_type),
	]


class iso1SignatureType(Structure):
	id_type = ArrayType_factory(c_uint32, "characters", iso1SignatureType_Id_CHARACTERS_SIZE)
	object_type = ArrayType_factory(iso1ObjectType, "array", iso1SignatureType_Object_ARRAY_SIZE)

	_fields_=[
		("Id", id_type),

		("Id_isUsed", c_uint, 1),

		("SignedInfo", iso1SignedInfoType),

		("SignatureValue", iso1SignatureValueType),

		("KeyInfo", iso1KeyInfoType),

		("KeyInfo_isUsed", c_uint, 1),

		("Object", object_type),
	]


class iso1PowerDeliveryReqType(Structure):
	_fields_=[
		("ChargeProgress", c_uint),

		("SAScheduleTupleID", c_uint8),

		("ChargingProfile", iso1ChargingProfileType),

		("ChargingProfile_isUsed", c_uint, 1),

		("EVPowerDeliveryParameter", iso1EVPowerDeliveryParameterType),

		("EVPowerDeliveryParameter_isUsed", c_uint, 1),

		("DC_EVPowerDeliveryParameter", iso1DC_EVPowerDeliveryParameterType),

		("DC_EVPowerDeliveryParameter_isUsed", c_uint, 1),
	]


class iso1ServiceParameterListType(Structure):
	parameter_set_type = ArrayType_factory(iso1ParameterSetType, "array", iso1ServiceParameterListType_ParameterSet_ARRAY_SIZE)

	_fields_=[
		("ParameterSet", parameter_set_type),
	]


class iso1ServiceDetailResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),

		("ServiceID", c_uint16),

		("ServiceParameterList", iso1ServiceParameterListType),

		("ServiceParameterList_isUsed", c_uint, 1),
	]


class iso1SAScheduleTupleType(Structure):
	_fields_=[
		("SAScheduleTupleID", c_uint8),

		("PMaxSchedule", iso1PMaxScheduleType),

		("SalesTariff", iso1SalesTariffType),

		("SalesTariff_isUsed", c_uint, 1),
	]


class iso1MessageHeaderType(Structure):
	session_id_type = ArrayType_factory(c_uint8, "bytes", iso1MessageHeaderType_SessionID_BYTES_SIZE)

	_fields_=[
		("SessionID", session_id_type),

		("Notification", iso1NotificationType),

		("Notification_isUsed", c_uint, 1),

		("Signature", iso1SignatureType),

		("Signature_isUsed", c_uint, 1),
	]


class iso1SAScheduleListType(Structure):
	sa_schedule_tuple_type = ArrayType_factory(iso1SAScheduleTupleType, "array", iso1SAScheduleListType_SAScheduleTuple_ARRAY_SIZE)

	_fields_=[
		("SAScheduleTuple", sa_schedule_tuple_type),
	]


class iso1ChargeParameterDiscoveryResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),

		("EVSEProcessing", c_uint),

		("SASchedules", iso1SASchedulesType),

		("SASchedules_isUsed", c_uint, 1),

		("SAScheduleList", iso1SAScheduleListType),

		("SAScheduleList_isUsed", c_uint, 1),

		("EVSEChargeParameter", iso1EVSEChargeParameterType),

		("EVSEChargeParameter_isUsed", c_uint, 1),

		("AC_EVSEChargeParameter", iso1AC_EVSEChargeParameterType),

		("AC_EVSEChargeParameter_isUsed", c_uint, 1),

		("DC_EVSEChargeParameter", iso1DC_EVSEChargeParameterType),

		("DC_EVSEChargeParameter_isUsed", c_uint, 1),
	]


class iso1BodyType(Structure):
	_fields_=[
		("BodyElement", iso1BodyBaseType),

		("SessionSetupReq", iso1SessionSetupReqType),

		("SessionSetupRes", iso1SessionSetupResType),

		("ServiceDiscoveryReq", iso1ServiceDiscoveryReqType),

		("ServiceDiscoveryRes", iso1ServiceDiscoveryResType),

		("ServiceDetailReq", iso1ServiceDetailReqType),

		("ServiceDetailRes", iso1ServiceDetailResType),

		("PaymentServiceSelectionReq", iso1PaymentServiceSelectionReqType),

		("PaymentServiceSelectionRes", iso1PaymentServiceSelectionResType),

		("PaymentDetailsReq", iso1PaymentDetailsReqType),

		("PaymentDetailsRes", iso1PaymentDetailsResType),

		("AuthorizationReq", iso1AuthorizationReqType),

		("AuthorizationRes", iso1AuthorizationResType),

		("ChargeParameterDiscoveryReq", iso1ChargeParameterDiscoveryReqType),

		("ChargeParameterDiscoveryRes", iso1ChargeParameterDiscoveryResType),

		("PowerDeliveryReq", iso1PowerDeliveryReqType),

		("PowerDeliveryRes", iso1PowerDeliveryResType),

		("MeteringReceiptReq", iso1MeteringReceiptReqType),

		("MeteringReceiptRes", iso1MeteringReceiptResType),

		("SessionStopReq", iso1SessionStopReqType),

		("SessionStopRes", iso1SessionStopResType),

		("CertificateUpdateReq", iso1CertificateUpdateReqType),

		("CertificateUpdateRes", iso1CertificateUpdateResType),

		("CertificateInstallationReq", iso1CertificateInstallationReqType),

		("CertificateInstallationRes", iso1CertificateInstallationResType),

		("ChargingStatusReq", iso1ChargingStatusReqType),

		("ChargingStatusRes", iso1ChargingStatusResType),

		("CableCheckReq", iso1CableCheckReqType),

		("CableCheckRes", iso1CableCheckResType),

		("PreChargeReq", iso1PreChargeReqType),

		("PreChargeRes", iso1PreChargeResType),

		("CurrentDemandReq", iso1CurrentDemandReqType),

		("CurrentDemandRes", iso1CurrentDemandResType),

		("WeldingDetectionReq", iso1WeldingDetectionReqType),

		("WeldingDetectionRes", iso1WeldingDetectionResType),

		("BodyElement_isUsed", c_uint8, 1),
		
		("SessionSetupReq_isUsed", c_uint8, 1),
		
		("SessionSetupRes_isUsed", c_uint8, 1),
		
		("ServiceDiscoveryReq_isUsed", c_uint8, 1),
		
		("ServiceDiscoveryRes_isUsed", c_uint8, 1),
		
		("ServiceDetailReq_isUsed", c_uint8, 1),
		
		("ServiceDetailRes_isUsed", c_uint8, 1),
		
		("PaymentServiceSelectionReq_isUsed", c_uint8, 1),
		
		("PaymentServiceSelectionRes_isUsed", c_uint8, 1),
		
		("PaymentDetailsReq_isUsed", c_uint8, 1),
		
		("PaymentDetailsRes_isUsed", c_uint8, 1),
		
		("AuthorizationReq_isUsed", c_uint8, 1),
		
		("AuthorizationRes_isUsed", c_uint8, 1),
		
		("ChargeParameterDiscoveryReq_isUsed", c_uint8, 1),
		
		("ChargeParameterDiscoveryRes_isUsed", c_uint8, 1),
		
		("PowerDeliveryReq_isUsed", c_uint8, 1),
		
		("PowerDeliveryRes_isUsed", c_uint8, 1),
		
		("MeteringReceiptReq_isUsed", c_uint8, 1),
		
		("MeteringReceiptRes_isUsed", c_uint8, 1),
		
		("SessionStopReq_isUsed", c_uint8, 1),
		
		("SessionStopRes_isUsed", c_uint8, 1),
		
		("CertificateUpdateReq_isUsed", c_uint8, 1),
		
		("CertificateUpdateRes_isUsed", c_uint8, 1),
		
		("CertificateInstallationReq_isUsed", c_uint8, 1),
		
		("CertificateInstallationRes_isUsed", c_uint8, 1),
		
		("ChargingStatusReq_isUsed", c_uint8, 1),
		
		("ChargingStatusRes_isUsed", c_uint8, 1),
		
		("CableCheckReq_isUsed", c_uint8, 1),
		
		("CableCheckRes_isUsed", c_uint8, 1),
		
		("PreChargeReq_isUsed", c_uint8, 1),
		
		("PreChargeRes_isUsed", c_uint8, 1),
		
		("CurrentDemandReq_isUsed", c_uint8, 1),
		
		("CurrentDemandRes_isUsed", c_uint8, 1),
		
		("WeldingDetectionReq_isUsed", c_uint8, 1),
		
		("WeldingDetectionRes_isUsed", c_uint8, 1),
		
	]


class iso1AnonType_V2G_Message(Structure):
	_fields_=[
		("Header", iso1MessageHeaderType),

		("Body", iso1BodyType),
	]


class iso1EXIDocument(Structure):
	mgmt_data_type = ArrayType_factory(c_uint32, "characters", EXIDocument_MgmtData_CHARACTERS_SIZE)
	key_name_type = ArrayType_factory(c_uint32, "characters", EXIDocument_KeyName_CHARACTERS_SIZE)
	digest_value_type = ArrayType_factory(c_uint8, "bytes", EXIDocument_DigestValue_BYTES_SIZE)

	_fields_=[
		("V2G_Message", iso1AnonType_V2G_Message),

		("ServiceDiscoveryReq", iso1ServiceDiscoveryReqType),

		("ServiceDiscoveryRes", iso1ServiceDiscoveryResType),

		("MeteringReceiptReq", iso1MeteringReceiptReqType),

		("PaymentDetailsReq", iso1PaymentDetailsReqType),

		("MeteringReceiptRes", iso1MeteringReceiptResType),

		("PaymentDetailsRes", iso1PaymentDetailsResType),

		("SessionSetupReq", iso1SessionSetupReqType),

		("SessionSetupRes", iso1SessionSetupResType),

		("CableCheckReq", iso1CableCheckReqType),

		("CableCheckRes", iso1CableCheckResType),

		("CertificateInstallationReq", iso1CertificateInstallationReqType),

		("CertificateInstallationRes", iso1CertificateInstallationResType),

		("WeldingDetectionReq", iso1WeldingDetectionReqType),

		("WeldingDetectionRes", iso1WeldingDetectionResType),

		("CertificateUpdateReq", iso1CertificateUpdateReqType),

		("CertificateUpdateRes", iso1CertificateUpdateResType),

		("PaymentServiceSelectionReq", iso1PaymentServiceSelectionReqType),

		("PowerDeliveryReq", iso1PowerDeliveryReqType),

		("PaymentServiceSelectionRes", iso1PaymentServiceSelectionResType),

		("PowerDeliveryRes", iso1PowerDeliveryResType),

		("ChargingStatusReq", iso1ChargingStatusReqType),

		("ChargingStatusRes", iso1ChargingStatusResType),

		("BodyElement", iso1BodyBaseType),

		("CurrentDemandReq", iso1CurrentDemandReqType),

		("PreChargeReq", iso1PreChargeReqType),

		("CurrentDemandRes", iso1CurrentDemandResType),

		("PreChargeRes", iso1PreChargeResType),

		("SessionStopReq", iso1SessionStopReqType),

		("AuthorizationReq", iso1AuthorizationReqType),

		("SessionStopRes", iso1SessionStopResType),

		("AuthorizationRes", iso1AuthorizationResType),

		("ChargeParameterDiscoveryReq", iso1ChargeParameterDiscoveryReqType),

		("ChargeParameterDiscoveryRes", iso1ChargeParameterDiscoveryResType),

		("ServiceDetailReq", iso1ServiceDetailReqType),

		("ServiceDetailRes", iso1ServiceDetailResType),

		("DC_EVSEStatus", iso1DC_EVSEStatusType),

		("RelativeTimeInterval", iso1RelativeTimeIntervalType),

		("SalesTariffEntry", iso1SalesTariffEntryType),

		("DC_EVPowerDeliveryParameter", iso1DC_EVPowerDeliveryParameterType),

		("SASchedules", iso1SASchedulesType),

		("AC_EVChargeParameter", iso1AC_EVChargeParameterType),

		("SAScheduleList", iso1SAScheduleListType),

		("DC_EVStatus", iso1DC_EVStatusType),

		("EVStatus", iso1EVStatusType),

		("DC_EVChargeParameter", iso1DC_EVChargeParameterType),

		("DC_EVSEChargeParameter", iso1DC_EVSEChargeParameterType),

		("EVSEStatus", iso1EVSEStatusType),

		("TimeInterval", iso1IntervalType),

		("EVPowerDeliveryParameter", iso1EVPowerDeliveryParameterType),

		("EVSEChargeParameter", iso1EVSEChargeParameterType),

		("AC_EVSEStatus", iso1AC_EVSEStatusType),

		("Entry", iso1EntryType),

		("AC_EVSEChargeParameter", iso1AC_EVSEChargeParameterType),

		("PMaxScheduleEntry", iso1PMaxScheduleEntryType),

		("EVChargeParameter", iso1EVChargeParameterType),

		("SignatureProperty", iso1SignaturePropertyType),

		("DSAKeyValue", iso1DSAKeyValueType),

		("SignatureProperties", iso1SignaturePropertiesType),

		("KeyValue", iso1KeyValueType),

		("Transforms", iso1TransformsType),

		("DigestMethod", iso1DigestMethodType),

		("Signature", iso1SignatureType),

		("RetrievalMethod", iso1RetrievalMethodType),

		("Manifest", iso1ManifestType),

		("Reference", iso1ReferenceType),

		("CanonicalizationMethod", iso1CanonicalizationMethodType),

		("RSAKeyValue", iso1RSAKeyValueType),

		("Transform", iso1TransformType),

		("PGPData", iso1PGPDataType),

		("MgmtData", mgmt_data_type),

		("SignatureMethod", iso1SignatureMethodType),

		("KeyInfo", iso1KeyInfoType),

		("SPKIData", iso1SPKIDataType),

		("X509Data", iso1X509DataType),

		("SignatureValue", iso1SignatureValueType),

		("KeyName", key_name_type),

		("DigestValue", digest_value_type),

		("SignedInfo", iso1SignedInfoType),

		("Object", iso1ObjectType),

		("V2G_Message_isUsed", c_uint8, 1),

		("ServiceDiscoveryReq_isUsed", c_uint8, 1),

		("ServiceDiscoveryRes_isUsed", c_uint8, 1),

		("MeteringReceiptReq_isUsed", c_uint8, 1),

		("PaymentDetailsReq_isUsed", c_uint8, 1),

		("MeteringReceiptRes_isUsed", c_uint8, 1),

		("PaymentDetailsRes_isUsed", c_uint8, 1),

		("SessionSetupReq_isUsed", c_uint8, 1),

		("SessionSetupRes_isUsed", c_uint8, 1),

		("CableCheckReq_isUsed", c_uint8, 1),

		("CableCheckRes_isUsed", c_uint8, 1),

		("CertificateInstallationReq_isUsed", c_uint8, 1),

		("CertificateInstallationRes_isUsed", c_uint8, 1),

		("WeldingDetectionReq_isUsed", c_uint8, 1),

		("WeldingDetectionRes_isUsed", c_uint8, 1),

		("CertificateUpdateReq_isUsed", c_uint8, 1),

		("CertificateUpdateRes_isUsed", c_uint8, 1),

		("PaymentServiceSelectionReq_isUsed", c_uint8, 1),

		("PowerDeliveryReq_isUsed", c_uint8, 1),

		("PaymentServiceSelectionRes_isUsed", c_uint8, 1),

		("PowerDeliveryRes_isUsed", c_uint8, 1),

		("ChargingStatusReq_isUsed", c_uint8, 1),

		("ChargingStatusRes_isUsed", c_uint8, 1),

		("BodyElement_isUsed", c_uint8, 1),

		("CurrentDemandReq_isUsed", c_uint8, 1),

		("PreChargeReq_isUsed", c_uint8, 1),

		("CurrentDemandRes_isUsed", c_uint8, 1),

		("PreChargeRes_isUsed", c_uint8, 1),

		("SessionStopReq_isUsed", c_uint8, 1),

		("AuthorizationReq_isUsed", c_uint8, 1),

		("SessionStopRes_isUsed", c_uint8, 1),

		("AuthorizationRes_isUsed", c_uint8, 1),

		("ChargeParameterDiscoveryReq_isUsed", c_uint8, 1),

		("ChargeParameterDiscoveryRes_isUsed", c_uint8, 1),

		("ServiceDetailReq_isUsed", c_uint8, 1),

		("ServiceDetailRes_isUsed", c_uint8, 1),

		("DC_EVSEStatus_isUsed", c_uint8, 1),

		("RelativeTimeInterval_isUsed", c_uint8, 1),

		("SalesTariffEntry_isUsed", c_uint8, 1),

		("DC_EVPowerDeliveryParameter_isUsed", c_uint8, 1),

		("SASchedules_isUsed", c_uint8, 1),

		("AC_EVChargeParameter_isUsed", c_uint8, 1),

		("SAScheduleList_isUsed", c_uint8, 1),

		("DC_EVStatus_isUsed", c_uint8, 1),

		("EVStatus_isUsed", c_uint8, 1),

		("DC_EVChargeParameter_isUsed", c_uint8, 1),

		("DC_EVSEChargeParameter_isUsed", c_uint8, 1),

		("EVSEStatus_isUsed", c_uint8, 1),

		("TimeInterval_isUsed", c_uint8, 1),

		("EVPowerDeliveryParameter_isUsed", c_uint8, 1),

		("EVSEChargeParameter_isUsed", c_uint8, 1),

		("AC_EVSEStatus_isUsed", c_uint8, 1),

		("Entry_isUsed", c_uint8, 1),

		("AC_EVSEChargeParameter_isUsed", c_uint8, 1),

		("PMaxScheduleEntry_isUsed", c_uint8, 1),

		("EVChargeParameter_isUsed", c_uint8, 1),

		("SignatureProperty_isUsed", c_uint8, 1),

		("DSAKeyValue_isUsed", c_uint8, 1),

		("SignatureProperties_isUsed", c_uint8, 1),

		("KeyValue_isUsed", c_uint8, 1),

		("Transforms_isUsed", c_uint8, 1),

		("DigestMethod_isUsed", c_uint8, 1),

		("Signature_isUsed", c_uint8, 1),

		("RetrievalMethod_isUsed", c_uint8, 1),

		("Manifest_isUsed", c_uint8, 1),

		("Reference_isUsed", c_uint8, 1),

		("CanonicalizationMethod_isUsed", c_uint8, 1),

		("RSAKeyValue_isUsed", c_uint8, 1),

		("Transform_isUsed", c_uint8, 1),

		("PGPData_isUsed", c_uint8, 1),

		("MgmtData_isUsed", c_uint8, 1),

		("SignatureMethod_isUsed", c_uint8, 1),

		("KeyInfo_isUsed", c_uint8, 1),

		("SPKIData_isUsed", c_uint8, 1),

		("X509Data_isUsed", c_uint8, 1),

		("SignatureValue_isUsed", c_uint8, 1),

		("KeyName_isUsed", c_uint8, 1),

		("DigestValue_isUsed", c_uint8, 1),

		("SignedInfo_isUsed", c_uint8, 1),

		("Object_isUsed", c_uint8, 1),

		("_warning_", c_int),
	]


class iso1EXISchemaInformedElementFragmentGrammar(Structure):
	id_type = ArrayType_factory(c_uint32, "characters", exiElementFrag_Id_CHARACTERS_SIZE)
	characters_generic_type = ArrayType_factory(c_uint32, "characters", exiElementFrag_CHARACTERS_GENERIC_CHARACTERS_SIZE)
	
	_fields_=[
		("Id_isUsed", c_uint, 1),

		("Id", id_type),

		("CHARACTERS_GENERIC_isUsed", c_uint, 1),

		("CHARACTERS_GENERIC", characters_generic_type),

		("_warning_", c_int),


	]


class iso1EXIFragment(Structure):
	_fields_=[
		("ChargingComplete", c_int),

		("EVMaxVoltage", iso1PhysicalValueType),

		("ServiceID", c_uint16),

		("EVRESSSOC", c_int8),

		("MeterReading", c_uint64),

		("physicalValue", iso1PhysicalValueType),

		("TimeInterval", iso1IntervalType),

		("AC_EVSEStatus", iso1AC_EVSEStatusType),

		("EVMaxCurrent", iso1PhysicalValueType),

		("ChargingProfileEntryStart", c_uint32),

		("EVSEMaxCurrent", iso1PhysicalValueType),

		("costKind", c_uint),

		("EAmount", iso1PhysicalValueType),

		("EnergyTransferMode", c_uint),

		("X509SerialNumber", c_int64),

		("NumEPriceLevels", c_uint8),

		("RetrievalMethod", iso1RetrievalMethodType),

		("PMax", iso1PhysicalValueType),

		("ParameterSetID", c_int16),

		("BulkSOC", c_int8),

		("EVSEMinimumCurrentLimit", iso1PhysicalValueType),

		("EVSEPowerLimitAchieved", c_int),

		("SalesTariffEntry", iso1SalesTariffEntryType),

		("Transforms", iso1TransformsType),

		("EVSEProcessing", c_uint),

		("EVSEIsolationStatus", c_uint),

		("BulkChargingComplete", c_int),

		("SAScheduleTupleID", c_uint8),

		("FaultCode", c_uint),

		("RootCertificateID", iso1X509IssuerSerialType),

		("HMACOutputLength", c_int64),

		("X509IssuerSerial", iso1X509IssuerSerialType),

		("byteValue", c_int8),

		("SPKIData", iso1SPKIDataType),

		("SAScheduleList", iso1SAScheduleListType),

		("EVMaximumPowerLimit", iso1PhysicalValueType),

		("DC_EVSEStatus", iso1DC_EVSEStatusType),

		("RetryCounter", c_int16),

		("EVSEMaximumCurrentLimit", iso1PhysicalValueType),

		("SalesTariff", iso1SalesTariffType),

		("X509Data", iso1X509DataType),

		("EVSECurrentRegulationTolerance", iso1PhysicalValueType),

		("KeyValue", iso1KeyValueType),

		("V2G_Message", iso1AnonType_V2G_Message),

		("EVSEMinimumVoltageLimit", iso1PhysicalValueType),

		("ResponseCode", c_uint),

		("ProfileEntry", iso1ProfileEntryType),

		("start", c_uint32),

		("EVErrorCode", c_uint),

		("EVChargeParameter", iso1EVChargeParameterType),

		("ContractSignatureCertChain", iso1CertificateChainType),

		("EVSEPresentCurrent", iso1PhysicalValueType),

		("PGPData", iso1PGPDataType),

		("EVMinCurrent", iso1PhysicalValueType),

		("FullSOC", c_int8),

		("amount", c_uint32),

		("DC_EVSEChargeParameter", iso1DC_EVSEChargeParameterType),

		("Entry", iso1EntryType),

		("SessionStopRes", iso1SessionStopResType),

		("shortValue", c_int16),

		("SAProvisioningCertificateChain", iso1CertificateChainType),

		("PowerDeliveryReq", iso1PowerDeliveryReqType),

		("PowerDeliveryRes", iso1PowerDeliveryResType),

		("SessionStopReq", iso1SessionStopReqType),

		("SignatureProperty", iso1SignaturePropertyType),

		("Header", iso1MessageHeaderType),

		("RSAKeyValue", iso1RSAKeyValueType),

		("FreeService", c_int),

		("EVSENominalVoltage", iso1PhysicalValueType),

		("MeteringReceiptRes", iso1MeteringReceiptResType),

		("ServiceDiscoveryReq", iso1ServiceDiscoveryReqType),

		("MeteringReceiptReq", iso1MeteringReceiptReqType),

		("PreChargeRes", iso1PreChargeResType),

		("EVEnergyCapacity", iso1PhysicalValueType),

		("Signature", iso1SignatureType),

		("AC_EVSEChargeParameter", iso1AC_EVSEChargeParameterType),

		("ServiceDiscoveryRes", iso1ServiceDiscoveryResType),

		("PreChargeReq", iso1PreChargeReqType),

		("NotificationMaxDelay", c_uint16),

		("CableCheckReq", iso1CableCheckReqType),

		("EVSEVoltageLimitAchieved", c_int),

		("boolValue", c_int),

		("DC_EVChargeParameter", iso1DC_EVChargeParameterType),

		("ChargingStatusReq", iso1ChargingStatusReqType),

		("CableCheckRes", iso1CableCheckResType),

		("MeterInfo", iso1MeterInfoType),

		("EVSEEnergyToBeDelivered", iso1PhysicalValueType),

		("EVSEStatus", iso1EVSEStatusType),

		("Service", iso1ServiceType),

		("Manifest", iso1ManifestType),

		("EVMaximumVoltageLimit", iso1PhysicalValueType),

		("intValue", c_int32),

		("ChargingProfile", iso1ChargingProfileType),

		("ReceiptRequired", c_int),

		("MeterStatus", c_int16),

		("DC_EVStatus", iso1DC_EVStatusType),

		("ChargingStatusRes", iso1ChargingStatusResType),

		("ServiceCategory", c_uint),

		("Notification", iso1NotificationType),

		("EVSEPresentVoltage", iso1PhysicalValueType),

		("EVSEMaximumPowerLimit", iso1PhysicalValueType),

		("EVSETimeStamp", c_int64),

		("Cost", iso1CostType),

		("EVSEPeakCurrentRipple", iso1PhysicalValueType),

		("ConsumptionCost", iso1ConsumptionCostType),

		("DigestMethod", iso1DigestMethodType),

		("SessionSetupRes", iso1SessionSetupResType),

		("EVSECurrentLimitAchieved", c_int),

		("ServiceDetailReq", iso1ServiceDetailReqType),

		("EVSEMaximumVoltageLimit", iso1PhysicalValueType),

		("ServiceDetailRes", iso1ServiceDetailResType),

		("SignatureProperties", iso1SignaturePropertiesType),

		("EPriceLevel", c_uint8),

		("EVTargetCurrent", iso1PhysicalValueType),

		("RemainingTimeToBulkSoC", iso1PhysicalValueType),

		("SessionSetupReq", iso1SessionSetupReqType),

		("Multiplier", c_int8),

		("CertificateUpdateRes", iso1CertificateUpdateResType),

		("EVTargetVoltage", iso1PhysicalValueType),

		("DSAKeyValue", iso1DSAKeyValueType),

		("CertificateUpdateReq", iso1CertificateUpdateReqType),

		("EVMaximumCurrentLimit", iso1PhysicalValueType),

		("CanonicalizationMethod", iso1CanonicalizationMethodType),

		("CertificateInstallationReq", iso1CertificateInstallationReqType),

		("CertificateInstallationRes", iso1CertificateInstallationResType),

		("EVStatus", iso1EVStatusType),

		("SupportedEnergyTransferMode", iso1SupportedEnergyTransferModeType),

		("SignedInfo", iso1SignedInfoType),

		("eMAID", iso1EXISchemaInformedElementFragmentGrammar),

		("MaxEntriesSAScheduleTuple", c_uint16),

		("PaymentOption", c_uint),

		("SubCertificates", iso1SubCertificatesType),

		("PaymentDetailsReq", iso1PaymentDetailsReqType),

		("AuthorizationReq", iso1AuthorizationReqType),

		("PaymentDetailsRes", iso1PaymentDetailsResType),

		("AuthorizationRes", iso1AuthorizationResType),

		("EVSEStatusCode", c_uint),

		("PaymentOptionList", iso1PaymentOptionListType),

		("SelectedServiceList", iso1SelectedServiceListType),

		("ContractSignatureEncryptedPrivateKey", iso1ContractSignatureEncryptedPrivateKeyType),

		("WeldingDetectionReq", iso1WeldingDetectionReqType),

		("WeldingDetectionRes", iso1WeldingDetectionResType),

		("ChargeProgress", c_uint),

		("SelectedPaymentOption", c_uint),

		("ParameterSet", iso1ParameterSetType),

		("EVSEChargeParameter", iso1EVSEChargeParameterType),

		("SignatureValue", iso1SignatureValueType),

		("SASchedules", iso1SASchedulesType),

		("SalesTariffID", c_uint8),

		("DHpublickey", iso1DiffieHellmanPublickeyType),

		("ServiceParameterList", iso1ServiceParameterListType),

		("ListOfRootCertificateIDs", iso1ListOfRootCertificateIDsType),

		("ChargeService", iso1ChargeServiceType),

		("amountMultiplier", c_int8),

		("RCD", c_int),

		("startValue", iso1PhysicalValueType),

		("CurrentDemandReq", iso1CurrentDemandReqType),

		("DC_EVPowerDeliveryParameter", iso1DC_EVPowerDeliveryParameterType),

		("Body", iso1BodyType),

		("EVSENotification", c_uint),

		("Value", c_int16),

		("KeyInfo", iso1KeyInfoType),

		("AC_EVChargeParameter", iso1AC_EVChargeParameterType),

		("PMaxScheduleEntry", iso1PMaxScheduleEntryType),

		("Parameter", iso1ParameterType),

		("SelectedService", iso1SelectedServiceType),

		("PaymentServiceSelectionReq", iso1PaymentServiceSelectionReqType),

		("PaymentServiceSelectionRes", iso1PaymentServiceSelectionResType),

		("CurrentDemandRes", iso1CurrentDemandResType),

		("EVReady", c_int),

		("SignatureMethod", iso1SignatureMethodType),

		("PMaxSchedule", iso1PMaxScheduleType),

		("Unit", c_uint),

		("Reference", iso1ReferenceType),

		("ChargingProfileEntryMaxNumberOfPhasesInUse", c_int8),

		("EVPowerDeliveryParameter", iso1EVPowerDeliveryParameterType),

		("ChargingProfileEntryMaxPower", iso1PhysicalValueType),

		("ChargeParameterDiscoveryReq", iso1ChargeParameterDiscoveryReqType),

		("duration", c_uint32),

		("TMeter", c_int64),

		("ChargeParameterDiscoveryRes", iso1ChargeParameterDiscoveryResType),

		("ServiceList", iso1ServiceListType),

		("SAScheduleTuple", iso1SAScheduleTupleType),

		("BodyElement", iso1BodyBaseType),

		("RemainingTimeToFullSoC", iso1PhysicalValueType),

		("RelativeTimeInterval", iso1RelativeTimeIntervalType),

		("Transform", iso1TransformType),

		("DepartureTime", c_uint32),

		("Object", iso1ObjectType),

		("EVEnergyRequest", iso1PhysicalValueType),

		("ChargingSession", c_uint),

		("RequestedEnergyTransferMode", c_uint),

		("Exponent", ArrayType_factory(c_uint8, "bytes", EXIFragment_Exponent_BYTES_SIZE)),

		("PgenCounter", ArrayType_factory(c_uint8, "bytes", EXIFragment_PgenCounter_BYTES_SIZE)),

		("SessionID", ArrayType_factory(c_uint8, "bytes", EXIFragment_SessionID_BYTES_SIZE)),

		("PGPKeyPacket", ArrayType_factory(c_uint8, "bytes", EXIFragment_PGPKeyPacket_BYTES_SIZE)),

		("Seed", ArrayType_factory(c_uint8, "bytes", EXIFragment_Seed_BYTES_SIZE)),

		("XPath", ArrayType_factory(c_uint32, "characters", EXIFragment_XPath_CHARACTERS_SIZE)),

		("OEMProvisioningCert", ArrayType_factory(c_uint8, "bytes", EXIFragment_OEMProvisioningCert_BYTES_SIZE)),

		("SalesTariffDescription", ArrayType_factory(c_uint32, "characters", EXIFragment_SalesTariffDescription_CHARACTERS_SIZE)),

		("EVCCID", ArrayType_factory(c_uint8, "bytes", EXIFragment_EVCCID_BYTES_SIZE)),

		("MgmtData", ArrayType_factory(c_uint32, "characters", EXIFragment_MgmtData_CHARACTERS_SIZE)),

		("P", ArrayType_factory(c_uint8, "bytes", EXIFragment_P_BYTES_SIZE)),

		("Q", ArrayType_factory(c_uint8, "bytes", EXIFragment_Q_BYTES_SIZE)),

		("X509SubjectName", ArrayType_factory(c_uint32, "characters", EXIFragment_X509SubjectName_CHARACTERS_SIZE)),

		("G", ArrayType_factory(c_uint8, "bytes", EXIFragment_G_BYTES_SIZE)),

		("J", ArrayType_factory(c_uint8, "bytes", EXIFragment_J_BYTES_SIZE)),

		("ServiceScope", ArrayType_factory(c_uint32, "characters", EXIFragment_ServiceScope_CHARACTERS_SIZE)),

		("ServiceName", ArrayType_factory(c_uint32, "characters", EXIFragment_ServiceName_CHARACTERS_SIZE)),

		("X509CRL", ArrayType_factory(c_uint8, "bytes", EXIFragment_X509CRL_BYTES_SIZE)),

		("Y", ArrayType_factory(c_uint8, "bytes", EXIFragment_Y_BYTES_SIZE)),

		("DigestValue", ArrayType_factory(c_uint8, "bytes", EXIFragment_DigestValue_BYTES_SIZE)),

		("SPKISexp", ArrayType_factory(c_uint8, "bytes", EXIFragment_SPKISexp_BYTES_SIZE)),

		("stringValue", ArrayType_factory(c_uint32, "characters", EXIFragment_stringValue_CHARACTERS_SIZE)),

		("PGPKeyID", ArrayType_factory(c_uint8, "bytes", EXIFragment_PGPKeyID_BYTES_SIZE)),

		("X509Certificate", ArrayType_factory(c_uint8, "bytes", EXIFragment_X509Certificate_BYTES_SIZE)),

		("FaultMsg", ArrayType_factory(c_uint32, "characters", EXIFragment_FaultMsg_CHARACTERS_SIZE)),

		("EVSEID", ArrayType_factory(c_uint32, "characters", EXIFragment_EVSEID_CHARACTERS_SIZE)),

		("SigMeterReading", ArrayType_factory(c_uint8, "bytes", EXIFragment_SigMeterReading_BYTES_SIZE)),

		("MeterID", ArrayType_factory(c_uint32, "characters", EXIFragment_MeterID_CHARACTERS_SIZE)),

		("KeyName", ArrayType_factory(c_uint32, "characters", EXIFragment_KeyName_CHARACTERS_SIZE)),

		("GenChallenge", ArrayType_factory(c_uint8, "bytes", EXIFragment_GenChallenge_BYTES_SIZE)),

		("X509SKI", ArrayType_factory(c_uint8, "bytes", EXIFragment_X509SKI_BYTES_SIZE)),

		("Certificate", ArrayType_factory(c_uint8, "bytes", EXIFragment_Certificate_BYTES_SIZE)),

		("X509IssuerName", ArrayType_factory(c_uint32, "characters", EXIFragment_X509IssuerName_CHARACTERS_SIZE)),

		("Modulus", ArrayType_factory(c_uint8, "bytes", EXIFragment_Modulus_BYTES_SIZE)),
	]


class appHandAppProtocolType(Structure):
	protocol_namespace_type = ArrayType_factory(c_uint32, "characters", appHandAppProtocolType_ProtocolNamespace_CHARACTERS_SIZE)

	_fields_=[
		("ProtocolNamespace", protocol_namespace_type),

		("VersionNumberMajor", c_uint32),

		("VersionNumberMinor", c_uint32),

		("SchemaID", c_uint8),

		("Priority", c_uint8),
		
	]

class appHandAnonType_supportedAppProtocolRes(Structure):
	_fields_=[
		("ResponseCode", c_uint),

		("SchemaID", c_uint, 8),

		("SchemaID_isUsed", c_uint, 1),
	]


class appHandAnonType_supportedAppProtocolReq(Structure):
	app_protocol_type = ArrayType_factory(appHandAppProtocolType, "array", appHandAnonType_supportedAppProtocolReq_AppProtocol_ARRAY_SIZE)

	_fields_=[
		("AppProtocol", app_protocol_type),
	]

class appHandEXIDocument(Structure):
	_fields_=[
		("supportedAppProtocolReq", appHandAnonType_supportedAppProtocolReq),

		("supportedAppProtocolRes", appHandAnonType_supportedAppProtocolRes),

		("supportedAppProtocolReq_isUsed", c_uint, 1),

		("supportedAppProtocolRes_isUsed", c_uint, 1),

		("_warning_", c_int),
	]


class dinSessionSetupReqType(Structure):
	evccid_type = ArrayType_factory(c_uint8, "bytes", dinSessionSetupReqType_EVCCID_BYTES_SIZE)

	_fields_=[
		("EVCCID", evccid_type),
	]


class dinCanonicalizationMethodType(Structure):
	algorithm_type = ArrayType_factory(c_uint32, "characters", dinCanonicalizationMethodType_Algorithm_CHARACTERS_SIZE)
	any_type = ArrayType_factory(c_uint32, "characters", dinCanonicalizationMethodType_ANY_CHARACTERS_SIZE)

	_fields_=[
		("Algorithm", algorithm_type),

		("ANY", any_type),

		("ANY_isUsed", c_uint, 1),
	]


class dinSPKIDataType(Structure):
	any_type = ArrayType_factory(c_uint32, "characters", dinSPKIDataType_ANY_CHARACTERS_SIZE)
	spki_exp_type = ArrayType_factory(ArrayType_factory(c_uint8, "bytes", dinSPKIDataType_SPKISexp_BYTES_SIZE), "array", dinSPKIDataType_SPKISexp_ARRAY_SIZE)

	_fields_=[
		("SPKISexp", spki_exp_type),

		("ANY", any_type),

		("ANY_isUsed", c_uint, 1),
	]


class dinListOfRootCertificateIDsType(Structure):
	root_certificate_id_type = ArrayType_factory(ArrayType_factory(c_uint32, "characters", dinListOfRootCertificateIDsType_RootCertificateID_CHARACTERS_SIZE), "array", dinListOfRootCertificateIDsType_RootCertificateID_ARRAY_SIZE)

	_fields_=[
		("RootCertificateID", ArrayType_factory(ArrayType_factory(c_uint32, "characters", dinListOfRootCertificateIDsType_RootCertificateID_CHARACTERS_SIZE), "array", dinListOfRootCertificateIDsType_RootCertificateID_ARRAY_SIZE)),
	]


class dinTransformType(Structure):
	algorithm_type = ArrayType_factory(c_uint32, "characters", dinTransformType_Algorithm_CHARACTERS_SIZE)
	any_type = ArrayType_factory(c_uint32, "characters", dinTransformType_ANY_CHARACTERS_SIZE)
	xpath_type = ArrayType_factory(ArrayType_factory(c_uint32, "characters", dinTransformType_XPath_CHARACTERS_SIZE), "array", dinTransformType_XPath_ARRAY_SIZE)

	_fields_=[
		("Algorithm", algorithm_type),

		("ANY", any_type),

		("ANY_isUsed", c_uint, 1),

		("XPath", xpath_type),
	]


class dinContractAuthenticationReqType(Structure):
	id_type = ArrayType_factory(c_uint32, "characters", dinContractAuthenticationReqType_Id_CHARACTERS_SIZE)
	gen_challenge_type = ArrayType_factory(c_uint32, "characters", dinContractAuthenticationReqType_GenChallenge_CHARACTERS_SIZE)

	_fields_=[
		("Id", id_type),

		("Id_isUsed", c_uint, 1),

		("GenChallenge", gen_challenge_type),

		("GenChallenge_isUsed", c_uint, 1),
	]


class dinEVSEChargeParameterType(Structure):
	_fields_=[
		("noContent", c_int),
	]


class dinRelativeTimeIntervalType(Structure):
	_fields_=[
		("start", c_uint32),

		("duration", c_uint32),

		("duration_isUsed", c_uint, 1),
	]


class dinEVStatusType(Structure):
	_fields_=[
		("noContent", c_int),
	]


class dinDSAKeyValueType(Structure):
	_fields_=[
		("P", ArrayType_factory(c_uint8, "bytes", dinDSAKeyValueType_P_BYTES_SIZE)),

		("P_isUsed", c_uint8, 1),

		("Q", ArrayType_factory(c_uint8, "bytes", dinDSAKeyValueType_Q_BYTES_SIZE)),

		("Q_isUsed", c_uint8, 1),

		("G", ArrayType_factory(c_uint8, "bytes", dinDSAKeyValueType_G_BYTES_SIZE)),

		("G_isUsed", c_uint8, 1),

		("Y", ArrayType_factory(c_uint8, "bytes", dinDSAKeyValueType_Y_BYTES_SIZE)),

		("J", ArrayType_factory(c_uint8, "bytes", dinDSAKeyValueType_J_BYTES_SIZE)),

		("J_isUsed", c_uint8, 1),

		("Seed", ArrayType_factory(c_uint8, "bytes", dinDSAKeyValueType_Seed_BYTES_SIZE)),

		("Seed_isUsed", c_uint8, 1),

		("PgenCounter", ArrayType_factory(c_uint8, "bytes", dinDSAKeyValueType_PgenCounter_BYTES_SIZE)),

		("PgenCounter_isUsed", c_uint8, 1),

	]


class dinSASchedulesType(Structure):
	_fields_=[
		("noContent", c_int),
	]


class dinEVChargeParameterType(Structure):
	_fields_=[
		("noContent", c_int),
	]


class dinBodyBaseType(Structure):
	_fields_=[
		("noContent", c_int),
	]


class dinIntervalType(Structure):
	_fields_=[
		("noContent", c_int),
	]


class dinTransformsType(Structure):
	transform_type = ArrayType_factory(dinTransformType, "array", dinTransformsType_Transform_ARRAY_SIZE)

	_fields_=[
		("Transform", transform_type),
	]


class dinEntryType(Structure):
	_fields_=[
		("TimeInterval", dinIntervalType),

		("RelativeTimeInterval", dinRelativeTimeIntervalType),

		("TimeInterval_isUsed", c_uint, 1),

		("RelativeTimeInterval_isUsed", c_uint, 1),

	]


class dinSessionStopType(Structure):
	_fields_=[
		("noContent", c_int),
	]


class dinServiceDetailReqType(Structure):
	_fields_=[
		("ServiceID", c_uint16),
	]


class dinDigestMethodType(Structure):
	algorithm_type = ArrayType_factory(c_uint32, "characters", dinDigestMethodType_Algorithm_CHARACTERS_SIZE)
	any_type = ArrayType_factory(c_uint32, "characters", dinDigestMethodType_ANY_CHARACTERS_SIZE)

	_fields_=[
		("Algorithm", algorithm_type),

		("ANY", any_type),

		("ANY_isUsed", c_uint, 1),
	]


class dinChargingStatusReqType(Structure):
	_fields_=[
		("noContent", c_int),
	]


class dinSignatureMethodType(Structure):
	algorithm_type = ArrayType_factory(c_uint32, "characters", dinSignatureMethodType_Algorithm_CHARACTERS_SIZE)
	any_type = ArrayType_factory(c_uint32, "characters", dinSignatureMethodType_ANY_CHARACTERS_SIZE)

	_fields_=[
		("Algorithm", algorithm_type),

		("HMACOutputLength", c_int64),

		("HMACOutputLength_isUsed", c_uint8, 1),

		("ANY", any_type),

		("ANY_isUsed", c_uint8, 1),
	]


class dinCertificateInstallationReqType(Structure):
	id_type = ArrayType_factory(c_uint32, "characters", dinCertificateInstallationReqType_Id_CHARACTERS_SIZE)
	oemp_provision_cert_type = ArrayType_factory(c_uint8, "bytes", dinCertificateInstallationReqType_OEMProvisioningCert_BYTES_SIZE)
	dh_params_type = ArrayType_factory(c_uint8, "bytes", dinCertificateInstallationReqType_DHParams_BYTES_SIZE)

	_fields_=[
		("Id", id_type),

		("Id_isUsed", c_uint8, 1),

		("OEMProvisioningCert", oemp_provision_cert_type),

		("ListOfRootCertificateIDs", dinListOfRootCertificateIDsType),

		("DHParams", dh_params_type),
	]


class dinReferenceType(Structure):
	id_type = ArrayType_factory(c_uint32, "characters", dinReferenceType_Id_CHARACTERS_SIZE)
	uri_type = ArrayType_factory(c_uint32, "characters", dinReferenceType_URI_CHARACTERS_SIZE)
	type_type = ArrayType_factory(c_uint32, "characters", dinReferenceType_Type_CHARACTERS_SIZE)
	digest_value_type = ArrayType_factory(c_uint8, "bytes", dinReferenceType_DigestValue_BYTES_SIZE)

	_fields_=[
		("Id", id_type),

		("Id_isUsed", c_uint, 1),

		("URI", uri_type),

		("URI_isUsed", c_uint, 1),

		("Type", type_type),

		("Type_isUsed", c_uint, 1),

		("Transforms", dinTransformsType),

		("Transforms_isUsed", c_uint, 1),

		("DigestMethod", dinDigestMethodType),

		("DigestValue", digest_value_type),
	]


class dinProfileEntryType(Structure):
	_fields_=[
		("ChargingProfileEntryStart", c_uint32),

		("ChargingProfileEntryMaxPower", c_int16),
	]


class dinRSAKeyValueType(Structure):
	modulus_type = ArrayType_factory(c_uint8, "bytes", dinRSAKeyValueType_Modulus_BYTES_SIZE)
	exponent_type = ArrayType_factory(c_uint8, "bytes", dinRSAKeyValueType_Exponent_BYTES_SIZE)

	_fields_=[
		("Modulus", modulus_type),

		("Exponent", exponent_type),
	]


class dinEVSEStatusType(Structure):
	_fields_=[
		("noContent", c_int),
	]


class dinEVPowerDeliveryParameterType(Structure):
	_fields_=[
		("noContent", c_int),
	]


class dinX509IssuerSerialType(Structure):
	x509_issuer_name_type = ArrayType_factory(c_uint32, "characters", dinX509IssuerSerialType_X509IssuerName_CHARACTERS_SIZE)

	_fields_=[
		("X509IssuerName", x509_issuer_name_type),

		("X509SerialNumber", c_int64),

	]


class dinSelectedServiceType(Structure):
	_fields_=[
		("ServiceID", c_uint16),

		("ParameterSetID", c_int16),

		("ParameterSetID_isUsed", c_uint, 1),
	]


class dinDC_EVStatusType(Structure):
	_fields_=[
		("EVReady", c_int),

		("EVCabinConditioning", c_int),

		("EVCabinConditioning_isUsed", c_uint, 1),

		("EVRESSConditioning", c_int),

		("EVRESSConditioning_isUsed", c_uint, 1),

		("EVErrorCode", c_uint),

		("EVRESSSOC", c_int8),
	]


class dinPhysicalValueType(Structure):
	_fields_=[
		("Multiplier", c_int8), # size = 1
 
		("Unit", c_uint), # size = 4

		("Unit_isUsed", c_uint8, 1), # 1 

		("Value", c_int16), # size = 2
	]


class dinManifestType(Structure):
	id_type = ArrayType_factory(c_uint32, "characters", dinManifestType_Id_CHARACTERS_SIZE)
	reference_type = ArrayType_factory(dinReferenceType, "array", dinManifestType_Reference_ARRAY_SIZE)

	_fields_=[
		("Id", id_type),

		("Id_isUsed", c_uint, 1),

		("Reference", reference_type),
	]


class dinPMaxScheduleEntryType(Structure):
	_fields_=[
		("TimeInterval", dinIntervalType),

		("TimeInterval_isUsed", c_uint8, 1),

		("RelativeTimeInterval", dinRelativeTimeIntervalType),

		("RelativeTimeInterval_isUsed", c_uint8, 1),

		("PMax", c_int16),
	]


class dinSignatureValueType(Structure):
	id_type = ArrayType_factory(c_uint32, "characters", dinSignatureValueType_Id_CHARACTERS_SIZE)
	content_type = ArrayType_factory(c_uint8, "bytes", dinSignatureValueType_CONTENT_BYTES_SIZE)

	_fields_=[
		("Id", id_type),

		("Id_isUsed", c_uint, 1),

		("CONTENT", content_type),
	]


class dinPaymentOptionsType(Structure):
	_fields_=[
		("PaymentOption", ArrayType_factory(c_uint32, "array", dinPaymentOptionsType_PaymentOption_ARRAY_SIZE)),
	]


class dinServiceTagType(Structure):
	service_name_type = ArrayType_factory(c_uint32, "characters", dinServiceTagType_ServiceName_CHARACTERS_SIZE)
	service_scope_type = ArrayType_factory(c_uint32, "characters", dinServiceTagType_ServiceScope_CHARACTERS_SIZE)

	_fields_=[
		("ServiceID", c_uint16),

		("ServiceName", service_name_type),

		("ServiceName_isUsed", c_uint, 1),

		("ServiceCategory", c_uint),

		("ServiceScope", service_scope_type),

		("ServiceScope_isUsed", c_uint, 1),

	]


class dinAC_EVSEStatusType(Structure):
	_fields_=[
		("PowerSwitchClosed", c_int),

		("RCD", c_int),

		("NotificationMaxDelay", c_uint32),

		("EVSENotification", c_uint),
	]


class dinChargingProfileType(Structure):
	profile_entry_type = ArrayType_factory(dinProfileEntryType, "array", dinChargingProfileType_ProfileEntry_ARRAY_SIZE)

	_fields_=[
		("SAScheduleTupleID", c_int16),

		("ProfileEntry", profile_entry_type),
	]


class dinServiceDiscoveryReqType(Structure):
	service_scope_type = ArrayType_factory(c_uint32, "characters", dinServiceDiscoveryReqType_ServiceScope_CHARACTERS_SIZE)

	_fields_=[
		("ServiceScope", service_scope_type),

		("ServiceScope_isUsed", c_uint, 1),

		("ServiceCategory", c_uint),

		("ServiceCategory_isUsed", c_uint, 1),

	]


class dinAC_EVSEChargeParameterType(Structure):
	_fields_=[
		("AC_EVSEStatus", dinAC_EVSEStatusType),

		("EVSEMaxVoltage", dinPhysicalValueType),

		("EVSEMaxCurrent", dinPhysicalValueType),

		("EVSEMinCurrent", dinPhysicalValueType),
	]


class dinObjectType(Structure):
	id_type = ArrayType_factory(c_uint32, "characters", dinObjectType_Id_CHARACTERS_SIZE)
	mime_type_type = ArrayType_factory(c_uint32, "characters", dinObjectType_MimeType_CHARACTERS_SIZE)
	encoding_type = ArrayType_factory(c_uint32, "characters", dinObjectType_Encoding_CHARACTERS_SIZE)
	any_type = ArrayType_factory(c_uint32, "characters", dinObjectType_ANY_CHARACTERS_SIZE)

	_fields_=[
		("Id", id_type),

		("Id_isUsed", c_uint, 1),

		("MimeType", mime_type_type),

		("MimeType_isUsed", c_uint, 1),

		("Encoding", encoding_type),

		("Encoding_isUsed", c_uint, 1),

		("ANY", any_type),

		("ANY_isUsed", c_uint, 1),
	]


class dinSessionStopResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),
	]


class dinSignedInfoType(Structure):
	id_type = ArrayType_factory(c_uint32, "characters", dinSignedInfoType_Id_CHARACTERS_SIZE)
	reference_type = ArrayType_factory(dinReferenceType, "array", dinSignedInfoType_Reference_ARRAY_SIZE)

	_fields_=[
		("Id", id_type),

		("Id_isUsed", c_uint, 1),

		("CanonicalizationMethod", dinCanonicalizationMethodType),

		("SignatureMethod", dinSignatureMethodType),

		("Reference", reference_type),
	]


class dinCostType(Structure):
	_fields_=[
		("costKind", c_uint),

		("amount", c_uint32),

		("amountMultiplier", c_int8),

		("amountMultiplier_isUsed", c_uint8, 1),
	]


class dinServiceChargeType(Structure):
	_fields_=[
		("ServiceTag", dinServiceTagType),

		("FreeService", c_int),

		("EnergyTransferType", c_uint),
	]


class dinDC_EVSEStatusType(Structure):
	_fields_=[
		("EVSEIsolationStatus", c_uint),

		("EVSEIsolationStatus_isUsed", c_uint, 1),

		("EVSEStatusCode", c_uint),

		("NotificationMaxDelay", c_uint32),

		("EVSENotification", c_uint),
	]


class dinRetrievalMethodType(Structure):
	uri_type = ArrayType_factory(c_uint32, "characters", dinRetrievalMethodType_URI_CHARACTERS_SIZE)
	type_type = ArrayType_factory(c_uint32, "characters", dinRetrievalMethodType_Type_CHARACTERS_SIZE)

	_fields_=[
		("URI", uri_type),

		("URI_isUsed", c_uint, 1),

		("Type", type_type),

		("Type_isUsed", c_uint, 1),

		("Transforms", dinTransformsType),

		("Transforms_isUsed", c_uint, 1),
	]


class dinNotificationType(Structure):
	fault_msg_type = ArrayType_factory(c_uint32, "characters", dinNotificationType_FaultMsg_CHARACTERS_SIZE)

	_fields_=[
		("FaultCode", c_uint),

		("FaultMsg", fault_msg_type),

		("FaultMsg_isUsed", c_uint, 1),
	]


class dinPGPDataType(Structure):
	pgp_key_id_type = ArrayType_factory(c_uint8, "bytes", dinPGPDataType_PGPKeyID_BYTES_SIZE)
	pgp_key_packet_type = ArrayType_factory(c_uint8, "bytes", dinPGPDataType_PGPKeyPacket_BYTES_SIZE)
	any_type = ArrayType_factory(c_uint32, "characters", dinPGPDataType_ANY_CHARACTERS_SIZE)

	_fields_=[
		("PGPKeyID", pgp_key_id_type),

		("PGPKeyID_isUsed", c_uint8, 1),

		("PGPKeyPacket", pgp_key_packet_type),

		("PGPKeyPacket_isUsed", c_uint8, 1),

		("ANY", any_type),

		("ANY_isUsed", c_uint8, 1),
	]


class dinSignaturePropertyType(Structure):
	target_type = ArrayType_factory(c_uint32, "characters", dinSignaturePropertyType_Target_CHARACTERS_SIZE)
	id_type = ArrayType_factory(c_uint32, "characters", dinSignaturePropertyType_Id_CHARACTERS_SIZE)
	any_type = ArrayType_factory(c_uint32, "characters", dinSignaturePropertyType_ANY_CHARACTERS_SIZE) 

	_fields_=[
		("Target", target_type),

		("Id", id_type),

		("Id_isUsed", c_uint, 1),

		("ANY", any_type),

		("ANY_isUsed", c_uint, 1),
	]


class dinMeterInfoType(Structure):
	meter_id_type = ArrayType_factory(c_uint32, "characters", dinMeterInfoType_MeterID_CHARACTERS_SIZE)
	sig_meter_reading_type = ArrayType_factory(c_uint8, "bytes", dinMeterInfoType_SigMeterReading_BYTES_SIZE)

	_fields_=[
		("MeterID", meter_id_type),

		("MeterReading", dinPhysicalValueType),

		("MeterReading_isUsed", c_uint16, 1),

		("SigMeterReading", sig_meter_reading_type),

		("SigMeterReading_isUsed", c_uint16, 1),

		("MeterStatus", c_int16),

		("MeterStatus_isUsed", c_uint, 1),

		("TMeter", c_int64),

		("TMeter_isUsed", c_uint, 1),

	]


class dinSubCertificatesType(Structure):
	certificate_type = ArrayType_factory(ArrayType_factory(c_uint8, "bytes", dinSubCertificatesType_Certificate_BYTES_SIZE), "array", dinSubCertificatesType_Certificate_ARRAY_SIZE)

	_fields_=[
		("Certificate", certificate_type),
	]


class dinMeteringReceiptReqType(Structure):
	id_type = ArrayType_factory(c_uint32, "characters", dinMeteringReceiptReqType_Id_CHARACTERS_SIZE)
	session_id_type = ArrayType_factory(c_uint8, "bytes", dinMeteringReceiptReqType_SessionID_BYTES_SIZE)

	_fields_=[
		("Id", id_type),

		("Id_isUsed", c_uint8, 1),

		("SessionID", session_id_type),

		("SAScheduleTupleID", c_int16),

		("SAScheduleTupleID_isUsed", c_uint8, 1),

		("MeterInfo", dinMeterInfoType),


	]


class dinPowerDeliveryResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),

		("EVSEStatus", dinEVSEStatusType),

		("EVSEStatus_isUsed", c_uint, 1),

		("AC_EVSEStatus", dinAC_EVSEStatusType),

		("AC_EVSEStatus_isUsed", c_uint, 1),

		("DC_EVSEStatus", dinDC_EVSEStatusType),

		("DC_EVSEStatus_isUsed", c_uint, 1),
	]


class dinWeldingDetectionResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),

		("DC_EVSEStatus", dinDC_EVSEStatusType),

		("EVSEPresentVoltage", dinPhysicalValueType),
	]


class dinContractAuthenticationResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),

		("EVSEProcessing", c_uint),
	]


class dinSelectedServiceListType(Structure):
	selected_service_type = ArrayType_factory(dinSelectedServiceType, "array", dinSelectedServiceListType_SelectedService_ARRAY_SIZE)

	_fields_=[
		("SelectedService", selected_service_type),
	]


class dinCurrentDemandResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),

		("DC_EVSEStatus", dinDC_EVSEStatusType),

		("EVSEPresentVoltage", dinPhysicalValueType),

		("EVSEPresentCurrent", dinPhysicalValueType),

		("EVSECurrentLimitAchieved", c_int),

		("EVSEVoltageLimitAchieved", c_int),

		("EVSEPowerLimitAchieved", c_int),

		("EVSEMaximumVoltageLimit", dinPhysicalValueType),

		("EVSEMaximumVoltageLimit_isUsed", c_uint, 1),

		("EVSEMaximumCurrentLimit", dinPhysicalValueType),

		("EVSEMaximumCurrentLimit_isUsed", c_uint, 1),

		("EVSEMaximumPowerLimit", dinPhysicalValueType),

		("EVSEMaximumPowerLimit_isUsed", c_uint, 1),
	]


class dinAC_EVChargeParameterType(Structure):
	_fields_=[
		("DepartureTime", c_uint32),

		("EAmount", dinPhysicalValueType),

		("EVMaxVoltage", dinPhysicalValueType),

		("EVMaxCurrent", dinPhysicalValueType),

		("EVMinCurrent", dinPhysicalValueType),
	]


class dinX509DataType(Structure):
	x509_issuer_serial_type = ArrayType_factory(dinX509IssuerSerialType, "array", dinX509DataType_X509IssuerSerial_ARRAY_SIZE)
	x509_ski_type = ArrayType_factory(ArrayType_factory(c_uint8, "bytes", dinX509DataType_X509SKI_BYTES_SIZE), "array", dinX509DataType_X509SKI_ARRAY_SIZE)
	x509_subject_name_type = ArrayType_factory(ArrayType_factory(c_uint32, "characters", dinX509DataType_X509SubjectName_CHARACTERS_SIZE), "array", dinX509DataType_X509SubjectName_ARRAY_SIZE)
	x509_certificate_type = ArrayType_factory(ArrayType_factory(c_uint8, "bytes", dinX509DataType_X509Certificate_BYTES_SIZE), "array", dinX509DataType_X509Certificate_ARRAY_SIZE)
	x509_crl_type = ArrayType_factory(ArrayType_factory(c_uint8, "bytes", dinX509DataType_X509CRL_BYTES_SIZE), "array", dinX509DataType_X509CRL_ARRAY_SIZE)
	any_type = ArrayType_factory(c_uint32, "characters", dinX509DataType_ANY_CHARACTERS_SIZE)

	_fields_=[
		
		("X509IssuerSerial", x509_issuer_serial_type),

		("X509SKI", x509_ski_type),

		("X509SubjectName", x509_subject_name_type),

		("X509Certificate", x509_certificate_type),

		("X509CRL", x509_crl_type),

		("ANY", any_type),

		("ANY_isUsed", c_uint, 1),
	]


class dinChargingStatusResType(Structure):
	evse_id_type = ArrayType_factory(c_uint8, "bytes", dinChargingStatusResType_EVSEID_BYTES_SIZE)

	_fields_=[
		("ResponseCode", c_uint),

		("EVSEID", evse_id_type),

		("SAScheduleTupleID", c_int16),

		("EVSEMaxCurrent", dinPhysicalValueType),

		("EVSEMaxCurrent_isUsed", c_uint, 1),

		("MeterInfo", dinMeterInfoType),

		("MeterInfo_isUsed", c_uint, 1),

		("ReceiptRequired", c_int),

		("AC_EVSEStatus", dinAC_EVSEStatusType),

	]


class dinWeldingDetectionReqType(Structure):
	_fields_=[
		("DC_EVStatus", dinDC_EVStatusType),
	]


class dinSignaturePropertiesType(Structure):
	id_type = ArrayType_factory(c_uint32, "characters", dinSignaturePropertiesType_Id_CHARACTERS_SIZE)
	signature_property_type = ArrayType_factory(dinSignaturePropertyType, "array", dinSignaturePropertiesType_SignatureProperty_ARRAY_SIZE)

	_fields_=[
		("Id", id_type),

		("Id_isUsed", c_uint, 1),

		("SignatureProperty", signature_property_type),
	]


class dinDC_EVPowerDeliveryParameterType(Structure):
	_fields_=[
		("DC_EVStatus", dinDC_EVStatusType),

		("BulkChargingComplete", c_int),

		("BulkChargingComplete_isUsed", c_uint, 1),

		("ChargingComplete", c_int),
	]


class dinCableCheckReqType(Structure):
	_fields_=[
		("DC_EVStatus", dinDC_EVStatusType),
	]


class dinDC_EVChargeParameterType(Structure):
	_fields_=[
		("DC_EVStatus", dinDC_EVStatusType),

		("EVMaximumCurrentLimit", dinPhysicalValueType),

		("EVMaximumPowerLimit", dinPhysicalValueType),

		("EVMaximumPowerLimit_isUsed", c_uint8, 1),

		("EVMaximumVoltageLimit", dinPhysicalValueType),

		("EVEnergyCapacity", dinPhysicalValueType),

		("EVEnergyCapacity_isUsed", c_uint8, 1),

		("EVEnergyRequest", dinPhysicalValueType),

		("EVEnergyRequest_isUsed", c_uint8, 1),

		("FullSOC", c_int8),

		("FullSOC_isUsed", c_uint8, 1),

		("BulkSOC", c_int8),

		("BulkSOC_isUsed", c_uint8, 1),
	]


class dinPMaxScheduleType(Structure):
	pmax_schedule_entry_type = ArrayType_factory(dinPMaxScheduleEntryType, "array", dinPMaxScheduleType_PMaxScheduleEntry_ARRAY_SIZE)

	_fields_=[
		("PMaxScheduleID", c_int16),

		("PMaxScheduleEntry", pmax_schedule_entry_type),
	]


class dinServicePaymentSelectionReqType(Structure):
	_fields_=[
		("SelectedPaymentOption", c_uint),

		("SelectedServiceList", dinSelectedServiceListType),
	]


class dinPreChargeResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),

		("DC_EVSEStatus", dinDC_EVSEStatusType),

		("EVSEPresentVoltage", dinPhysicalValueType),
	]


class dinDC_EVSEChargeParameterType(Structure):
	_fields_=[
		("DC_EVSEStatus", dinDC_EVSEStatusType),

		("EVSEMaximumCurrentLimit", dinPhysicalValueType),

		("EVSEMaximumPowerLimit", dinPhysicalValueType),

		("EVSEMaximumPowerLimit_isUsed", c_uint, 1),

		("EVSEMaximumVoltageLimit", dinPhysicalValueType),

		("EVSEMinimumCurrentLimit", dinPhysicalValueType),

		("EVSEMinimumVoltageLimit", dinPhysicalValueType),

		("EVSECurrentRegulationTolerance", dinPhysicalValueType),

		("EVSECurrentRegulationTolerance_isUsed", c_uint, 1),

		("EVSEPeakCurrentRipple", dinPhysicalValueType),

		("EVSEEnergyToBeDelivered", dinPhysicalValueType),

		("EVSEEnergyToBeDelivered_isUsed", c_uint, 1),
	]


class dinPaymentDetailsResType(Structure):
	gen_challenge_type = ArrayType_factory(c_uint32, "characters", dinPaymentDetailsResType_GenChallenge_CHARACTERS_SIZE)

	_fields_=[
		("ResponseCode", c_uint),

		("GenChallenge", gen_challenge_type),

		("DateTimeNow", c_int64),
	]


class dinKeyValueType(Structure):
	any_type = ArrayType_factory(c_uint32, "characters", dinKeyValueType_ANY_CHARACTERS_SIZE)

	_fields_=[
		("DSAKeyValue", dinDSAKeyValueType),

		("DSAKeyValue_isUsed", c_uint8, 1),

		("RSAKeyValue", dinRSAKeyValueType),

		("RSAKeyValue_isUsed", c_uint8, 1),

		("ANY", any_type),

		("ANY_isUsed", c_uint8, 1),

	]


class dinPowerDeliveryReqType(Structure):
	_fields_=[
		("ReadyToChargeState", c_int),

		("ChargingProfile", dinChargingProfileType),

		("ChargingProfile_isUsed", c_uint, 1),

		("EVPowerDeliveryParameter", dinEVPowerDeliveryParameterType),

		("EVPowerDeliveryParameter_isUsed", c_uint, 1),

		("DC_EVPowerDeliveryParameter", dinDC_EVPowerDeliveryParameterType),

		("DC_EVPowerDeliveryParameter_isUsed", c_uint, 1),
	]


class dinCertificateChainType(Structure):
	certificate_type = ArrayType_factory(c_uint8, "bytes", dinCertificateChainType_Certificate_BYTES_SIZE)

	_fields_=[
		("Certificate", certificate_type),

		("SubCertificates", dinSubCertificatesType),

		("SubCertificates_isUsed", c_uint8, 1),

	]


class dinParameterType(Structure):
	name_type = ArrayType_factory(c_uint32, "characters", dinParameterType_Name_CHARACTERS_SIZE)
	string_value_type = ArrayType_factory(c_uint32, "characters", dinParameterType_stringValue_CHARACTERS_SIZE)

	_fields_=[
		("Name", name_type),

		("ValueType", c_uint),

		("boolValue", c_int),

		("boolValue_isUsed", c_uint8, 1),

		("byteValue", c_int8),

		("byteValue_isUsed", c_uint8, 1),

		("shortValue", c_int16),

		("shortValue_isUsed", c_uint8, 1),

		("intValue", c_int32),

		("intValue_isUsed", c_uint8, 1),

		("physicalValue", dinPhysicalValueType),

		("physicalValue_isUsed", c_uint8, 1),

		("stringValue", string_value_type),

		("stringValue_isUsed", c_uint8, 1),
	]


class dinParameterSetType(Structure):
	parameter_type = ArrayType_factory(dinParameterType, "array", dinParameterSetType_Parameter_ARRAY_SIZE)

	_fields_=[
		("ParameterSetID", c_int16),

		("Parameter", parameter_type),
	]


class dinCurrentDemandReqType(Structure):
	_fields_=[
		("DC_EVStatus", dinDC_EVStatusType),

		("EVTargetCurrent", dinPhysicalValueType),

		("EVMaximumVoltageLimit", dinPhysicalValueType),

		("EVMaximumVoltageLimit_isUsed", c_uint, 1),

		("EVMaximumCurrentLimit", dinPhysicalValueType),

		("EVMaximumCurrentLimit_isUsed", c_uint, 1),

		("EVMaximumPowerLimit", dinPhysicalValueType),

		("EVMaximumPowerLimit_isUsed", c_uint, 1),

		("BulkChargingComplete", c_int),

		("BulkChargingComplete_isUsed", c_uint, 1),

		("ChargingComplete", c_int),

		("RemainingTimeToFullSoC", dinPhysicalValueType),

		("RemainingTimeToFullSoC_isUsed", c_uint, 1),

		("RemainingTimeToBulkSoC", dinPhysicalValueType),

		("RemainingTimeToBulkSoC_isUsed", c_uint, 1),

		("EVTargetVoltage", dinPhysicalValueType),
	]


class dinPreChargeReqType(Structure):
	_fields_=[
		("DC_EVStatus", dinDC_EVStatusType),

		("EVTargetVoltage", dinPhysicalValueType),

		("EVTargetCurrent", dinPhysicalValueType),
	]


class dinChargeParameterDiscoveryReqType(Structure):
	_fields_=[
		("EVRequestedEnergyTransferType", c_uint),

		("EVChargeParameter", dinEVChargeParameterType),

		("EVChargeParameter_isUsed", c_uint, 1),

		("AC_EVChargeParameter", dinAC_EVChargeParameterType),

		("AC_EVChargeParameter_isUsed", c_uint, 1),

		("DC_EVChargeParameter", dinDC_EVChargeParameterType),

		("DC_EVChargeParameter_isUsed", c_uint, 1),
	]


class dinConsumptionCostType(Structure):
	cost_type = ArrayType_factory(dinCostType, "array", dinConsumptionCostType_Cost_ARRAY_SIZE)

	_fields_=[
		("startValue", c_uint32),

		("Cost", cost_type),
	]


class dinServiceType(Structure):
	_fields_=[
		("ServiceTag", dinServiceTagType),

		("FreeService", c_int),
	]


class dinServiceTagListType(Structure):
	service_type = ArrayType_factory(dinServiceType, "array", dinServiceTagListType_Service_ARRAY_SIZE)

	_fields_=[
		("Service", service_type),
	]


class dinSessionSetupResType(Structure):
	evse_id_type = ArrayType_factory(c_uint8, "bytes", dinSessionSetupResType_EVSEID_BYTES_SIZE)

	_fields_=[
		("ResponseCode", c_uint),

		("EVSEID", evse_id_type),

		("DateTimeNow", c_int64),

		("DateTimeNow_isUsed", c_uint, 1),
	]


class dinMeteringReceiptResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),

		("AC_EVSEStatus", dinAC_EVSEStatusType),
	]


class dinServiceParameterListType(Structure):
	parameter_set_type = ArrayType_factory(dinParameterSetType, "array", dinServiceParameterListType_ParameterSet_ARRAY_SIZE)

	_fields_=[
		("ParameterSet", parameter_set_type),
	]


class dinCertificateUpdateReqType(Structure):
	id_type = ArrayType_factory(c_uint32, "characters", dinCertificateUpdateReqType_Id_CHARACTERS_SIZE)
	contract_id_type = ArrayType_factory(c_uint32, "characters", dinCertificateUpdateReqType_ContractID_CHARACTERS_SIZE)
	dh_params_type = ArrayType_factory(c_uint8, "bytes", dinCertificateUpdateReqType_DHParams_BYTES_SIZE)

	_fields_=[
		("Id", id_type),

		("Id_isUsed", c_uint, 1),

		("ContractSignatureCertChain", dinCertificateChainType),

		("ContractID", contract_id_type),

		("ListOfRootCertificateIDs", dinListOfRootCertificateIDsType),

		("DHParams", dh_params_type),
	]


class dinServicePaymentSelectionResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),
	]


class dinKeyInfoType(Structure):
	id_type = ArrayType_factory(c_uint32, "characters", dinKeyInfoType_Id_CHARACTERS_SIZE)
	key_name_type = ArrayType_factory(ArrayType_factory(c_uint32, "characters", dinKeyInfoType_KeyName_CHARACTERS_SIZE), "array", dinKeyInfoType_KeyName_ARRAY_SIZE)
	key_value_type = ArrayType_factory(dinKeyValueType, "array", dinKeyInfoType_KeyValue_ARRAY_SIZE)
	retrieval_method_type = ArrayType_factory(dinRetrievalMethodType, "array", dinKeyInfoType_RetrievalMethod_ARRAY_SIZE)
	x509_data_type = ArrayType_factory(dinX509DataType, "array", dinKeyInfoType_X509Data_ARRAY_SIZE)
	pgp_data_type = ArrayType_factory(dinPGPDataType, "array", dinKeyInfoType_PGPData_ARRAY_SIZE)
	spki_data_type = ArrayType_factory(dinSPKIDataType, "array", dinKeyInfoType_SPKIData_ARRAY_SIZE)
	mgmt_data_type = ArrayType_factory(ArrayType_factory(c_uint32, "characters", dinKeyInfoType_MgmtData_CHARACTERS_SIZE), "array", dinKeyInfoType_MgmtData_ARRAY_SIZE)
	any_type = ArrayType_factory(c_uint32, "characters", dinKeyInfoType_ANY_CHARACTERS_SIZE)

	_fields_=[
		("Id", id_type),

		("Id_isUsed", c_uint, 1),

		("KeyName", key_name_type),

		("KeyValue", key_value_type),

		("RetrievalMethod", retrieval_method_type),

		("X509Data", x509_data_type),

		("PGPData", pgp_data_type),

		("SPKIData", spki_data_type),

		("MgmtData", mgmt_data_type),

		("ANY", any_type),

		("ANY_isUsed", c_uint, 1),
	]


class dinPaymentDetailsReqType(Structure):
	contract_id_type = ArrayType_factory(c_uint32, "characters", dinPaymentDetailsReqType_ContractID_CHARACTERS_SIZE)

	_fields_=[
		("ContractID", contract_id_type),

		("ContractSignatureCertChain", dinCertificateChainType),
	]


class dinCableCheckResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),

		("DC_EVSEStatus", dinDC_EVSEStatusType),

		("EVSEProcessing", c_uint),
	]


class dinCertificateInstallationResType(Structure):
	id_type = ArrayType_factory(c_uint32, "characters", dinCertificateInstallationResType_Id_CHARACTERS_SIZE)
	contract_signature_encrypted_private_key_type = ArrayType_factory(c_uint8, "bytes", dinCertificateInstallationResType_ContractSignatureEncryptedPrivateKey_BYTES_SIZE)
	dh_params_type = ArrayType_factory(c_uint8, "bytes", dinCertificateInstallationResType_DHParams_BYTES_SIZE)
	contract_id_type = ArrayType_factory(c_uint32, "characters", dinCertificateInstallationResType_ContractID_CHARACTERS_SIZE)

	_fields_=[
		("Id", id_type),

		("ResponseCode", c_uint),

		("ContractSignatureCertChain", dinCertificateChainType),

		("ContractSignatureEncryptedPrivateKey", contract_signature_encrypted_private_key_type),

		("DHParams", dh_params_type),

		("ContractID", contract_id_type),
	]


class dinServiceDetailResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),

		("ServiceID", c_uint16),

		("ServiceParameterList", dinServiceParameterListType),

		("ServiceParameterList_isUsed", c_uint, 1),
	]


class dinCertificateUpdateResType(Structure):
	contract_id_type = ArrayType_factory(c_uint32, "characters", dinCertificateUpdateResType_ContractID_CHARACTERS_SIZE)
	dh_params_type = ArrayType_factory(c_uint8, "bytes", dinCertificateUpdateResType_DHParams_BYTES_SIZE)
	contract_signature_encrypted_private_key_type = ArrayType_factory(c_uint8, "bytes", dinCertificateUpdateResType_ContractSignatureEncryptedPrivateKey_BYTES_SIZE)
	id_type = ArrayType_factory(c_uint32, "characters", dinCertificateUpdateResType_Id_CHARACTERS_SIZE)

	_fields_=[
		("Id", id_type),

		("ResponseCode", c_uint),

		("ContractSignatureCertChain", dinCertificateChainType),

		("ContractSignatureEncryptedPrivateKey", contract_signature_encrypted_private_key_type),
		
		("DHParams", dh_params_type),

		("ContractID", contract_id_type),

		("RetryCounter", c_int16),
	]


class dinSalesTariffEntryType(Structure):
	consumption_cost_type = ArrayType_factory(dinConsumptionCostType, "array", dinSalesTariffEntryType_ConsumptionCost_ARRAY_SIZE)

	_fields_=[
		("TimeInterval", dinIntervalType),

		("TimeInterval_isUsed", c_uint8, 1),

		("RelativeTimeInterval", dinRelativeTimeIntervalType),

		("RelativeTimeInterval_isUsed", c_uint8, 1),

		("EPriceLevel", c_uint8),

		("ConsumptionCost", consumption_cost_type),
	]


class dinServiceDiscoveryResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),

		("PaymentOptions", dinPaymentOptionsType),

		("ChargeService", dinServiceChargeType),

		("ServiceList", dinServiceTagListType),

		("ServiceList_isUsed", c_uint, 1),
	]


class dinSignatureType(Structure):
	id_type = ArrayType_factory(c_uint32, "characters", dinSignatureType_Id_CHARACTERS_SIZE)
	object_type = ArrayType_factory(dinObjectType, "array", dinSignatureType_Object_ARRAY_SIZE)

	_fields_=[
		("Id", id_type),

		("Id_isUsed", c_uint, 1),

		("SignedInfo", dinSignedInfoType),

		("SignatureValue", dinSignatureValueType),

		("KeyInfo", dinKeyInfoType),

		("KeyInfo_isUsed", c_uint, 1),

		("Object", object_type),
	]


class dinSalesTariffType(Structure):
	id_type = ArrayType_factory(c_uint32, "characters", dinSalesTariffType_Id_CHARACTERS_SIZE)
	sales_tariff_description_type = ArrayType_factory(c_uint32, "characters", dinSalesTariffType_SalesTariffDescription_CHARACTERS_SIZE)
	sales_tariff_entry_type  = ArrayType_factory(dinSalesTariffEntryType, "array", dinSalesTariffType_SalesTariffEntry_ARRAY_SIZE)

	_fields_=[
		("Id", id_type),

		("SalesTariffID", c_int16),

		("SalesTariffDescription", sales_tariff_description_type),

		("SalesTariffDescription_isUsed", c_uint8, 1),

		("NumEPriceLevels", c_uint8),

		("SalesTariffEntry", sales_tariff_entry_type),
	]


class dinMessageHeaderType(Structure):
	session_id_type = ArrayType_factory(c_uint8, "bytes", dinMessageHeaderType_SessionID_BYTES_SIZE)

	_fields_=[
		("SessionID", session_id_type),

		("Notification", dinNotificationType),

		("Notification_isUsed", c_uint, 1),

		("Signature", dinSignatureType),

		("Signature_isUsed", c_uint, 1),

	]


class dinSAScheduleTupleType(Structure):
	_fields_=[
		("SAScheduleTupleID", c_int16),

		("PMaxSchedule", dinPMaxScheduleType),

		("SalesTariff", dinSalesTariffType),

		("SalesTariff_isUsed", c_uint, 1),
	]


class dinSAScheduleListType(Structure):
	sa_schedule_tuple_type = ArrayType_factory(dinSAScheduleTupleType, "array", dinSAScheduleListType_SAScheduleTuple_ARRAY_SIZE)

	_fields_=[
		("SAScheduleTuple", sa_schedule_tuple_type),
	]


class dinChargeParameterDiscoveryResType(Structure):
	_fields_=[
		("ResponseCode", c_uint),

		("EVSEProcessing", c_uint),

		("SASchedules", dinSASchedulesType),

		("SASchedules_isUsed", c_uint, 1),

		("SAScheduleList", dinSAScheduleListType),

		("SAScheduleList_isUsed", c_uint, 1),

		("EVSEChargeParameter", dinEVSEChargeParameterType),

		("EVSEChargeParameter_isUsed", c_uint, 1),

		("AC_EVSEChargeParameter", dinAC_EVSEChargeParameterType),

		("AC_EVSEChargeParameter_isUsed", c_uint, 1),

		("DC_EVSEChargeParameter", dinDC_EVSEChargeParameterType),

		("DC_EVSEChargeParameter_isUsed", c_uint, 1),
	]


class dinBodyType(Structure):
	_fields_=[
		("BodyElement", dinBodyBaseType),

		("SessionSetupReq", dinSessionSetupReqType),

		("SessionSetupRes", dinSessionSetupResType),

		("ServiceDiscoveryReq", dinServiceDiscoveryReqType),

		("ServiceDiscoveryRes", dinServiceDiscoveryResType),

		("ServiceDetailReq", dinServiceDetailReqType),

		("ServiceDetailRes", dinServiceDetailResType),

		("ServicePaymentSelectionReq", dinServicePaymentSelectionReqType),

		("ServicePaymentSelectionRes", dinServicePaymentSelectionResType),

		("PaymentDetailsReq", dinPaymentDetailsReqType),

		("PaymentDetailsRes", dinPaymentDetailsResType),

		("ContractAuthenticationReq", dinContractAuthenticationReqType),

		("ContractAuthenticationRes", dinContractAuthenticationResType),

		("ChargeParameterDiscoveryReq", dinChargeParameterDiscoveryReqType),

		("ChargeParameterDiscoveryRes", dinChargeParameterDiscoveryResType),

		("PowerDeliveryReq", dinPowerDeliveryReqType),

		("PowerDeliveryRes", dinPowerDeliveryResType),

		("ChargingStatusReq", dinChargingStatusReqType),

		("ChargingStatusRes", dinChargingStatusResType),

		("MeteringReceiptReq", dinMeteringReceiptReqType),

		("MeteringReceiptRes", dinMeteringReceiptResType),

		("SessionStopReq", dinSessionStopType),

		("SessionStopRes", dinSessionStopResType),

		("CertificateUpdateReq", dinCertificateUpdateReqType),

		("CertificateUpdateRes", dinCertificateUpdateResType),

		("CertificateInstallationReq", dinCertificateInstallationReqType),

		("CertificateInstallationRes", dinCertificateInstallationResType),

		("CableCheckReq", dinCableCheckReqType),

		("CableCheckRes", dinCableCheckResType),

		("PreChargeReq", dinPreChargeReqType),

		("PreChargeRes", dinPreChargeResType),

		("CurrentDemandReq", dinCurrentDemandReqType),

		("CurrentDemandRes", dinCurrentDemandResType),

		("WeldingDetectionReq", dinWeldingDetectionReqType),

		("WeldingDetectionRes", dinWeldingDetectionResType),

		("BodyElement_isUsed", c_uint, 1),
		
		("SessionSetupReq_isUsed", c_uint, 1),
		
		("SessionSetupRes_isUsed", c_uint, 1),
		
		("ServiceDiscoveryReq_isUsed", c_uint, 1),
		
		("ServiceDiscoveryRes_isUsed", c_uint, 1),
		
		("ServiceDetailReq_isUsed", c_uint, 1),
		
		("ServiceDetailRes_isUsed", c_uint, 1),
		
		("ServicePaymentSelectionReq_isUsed", c_uint, 1),
		
		("ServicePaymentSelectionRes_isUsed", c_uint, 1),
		
		("PaymentDetailsReq_isUsed", c_uint, 1),
		
		("PaymentDetailsRes_isUsed", c_uint, 1),
		
		("ContractAuthenticationReq_isUsed", c_uint, 1),
		
		("ContractAuthenticationRes_isUsed", c_uint, 1),
		
		("ChargeParameterDiscoveryReq_isUsed", c_uint, 1),
		
		("ChargeParameterDiscoveryRes_isUsed", c_uint, 1),
		
		("PowerDeliveryReq_isUsed", c_uint, 1),
		
		("PowerDeliveryRes_isUsed", c_uint, 1),
		
		("ChargingStatusReq_isUsed", c_uint, 1),
		
		("ChargingStatusRes_isUsed", c_uint, 1),
		
		("MeteringReceiptReq_isUsed", c_uint, 1),
		
		("MeteringReceiptRes_isUsed", c_uint, 1),
		
		("SessionStopReq_isUsed", c_uint, 1),
		
		("SessionStopRes_isUsed", c_uint, 1),
		
		("CertificateUpdateReq_isUsed", c_uint, 1),
		
		("CertificateUpdateRes_isUsed", c_uint, 1),
		
		("CertificateInstallationReq_isUsed", c_uint, 1),
		
		("CertificateInstallationRes_isUsed", c_uint, 1),
		
		("CableCheckReq_isUsed", c_uint, 1),
		
		("CableCheckRes_isUsed", c_uint, 1),
		
		("PreChargeReq_isUsed", c_uint, 1),
		
		("PreChargeRes_isUsed", c_uint, 1),
		
		("CurrentDemandReq_isUsed", c_uint, 1),
		
		("CurrentDemandRes_isUsed", c_uint, 1),
		
		("WeldingDetectionReq_isUsed", c_uint, 1),
		
		("WeldingDetectionRes_isUsed", c_uint, 1),
		
	]


class dinAnonType_V2G_Message(Structure):
	_fields_=[
		("Header", dinMessageHeaderType),

		("Body", dinBodyType),
	]


class dinEXIDocument(Structure):
	_fields_=[
		("BodyElement", dinBodyBaseType),

		("V2G_Message", dinAnonType_V2G_Message),

		("SignatureProperty", dinSignaturePropertyType),

		("DSAKeyValue", dinDSAKeyValueType),

		("SignatureProperties", dinSignaturePropertiesType),

		("KeyValue", dinKeyValueType),

		("Transforms", dinTransformsType),

		("DigestMethod", dinDigestMethodType),

		("Signature", dinSignatureType),

		("RetrievalMethod", dinRetrievalMethodType),

		("Manifest", dinManifestType),

		("Reference", dinReferenceType),

		("CanonicalizationMethod", dinCanonicalizationMethodType),

		("RSAKeyValue", dinRSAKeyValueType),

		("Transform", dinTransformType),

		("PGPData", dinPGPDataType),

		("MgmtData", ArrayType_factory(c_uint32, "characters", EXIDocument_MgmtData_CHARACTERS_SIZE)),

		("SignatureMethod", dinSignatureMethodType),

		("KeyInfo", dinKeyInfoType),

		("SPKIData", dinSPKIDataType),

		("X509Data", dinX509DataType),

		("SignatureValue", dinSignatureValueType),

		("KeyName", ArrayType_factory(c_uint32, "characters", EXIDocument_KeyName_CHARACTERS_SIZE)),

		("DigestValue", ArrayType_factory(c_uint8, "bytes", EXIDocument_DigestValue_BYTES_SIZE)),

		("SignedInfo", dinSignedInfoType),

		("Object", dinObjectType),

		("DC_EVSEStatus", dinDC_EVSEStatusType),

		("RelativeTimeInterval", dinRelativeTimeIntervalType),

		("SalesTariffEntry", dinSalesTariffEntryType),

		("DC_EVPowerDeliveryParameter", dinDC_EVPowerDeliveryParameterType),

		("SASchedules", dinSASchedulesType),

		("AC_EVChargeParameter", dinAC_EVChargeParameterType),

		("SAScheduleList", dinSAScheduleListType),

		("DC_EVStatus", dinDC_EVStatusType),

		("ServiceCharge", dinServiceChargeType),

		("EVStatus", dinEVStatusType),

		("DC_EVChargeParameter", dinDC_EVChargeParameterType),

		("DC_EVSEChargeParameter", dinDC_EVSEChargeParameterType),

		("EVSEStatus", dinEVSEStatusType),

		("TimeInterval", dinIntervalType),

		("EVPowerDeliveryParameter", dinEVPowerDeliveryParameterType),

		("EVSEChargeParameter", dinEVSEChargeParameterType),

		("AC_EVSEStatus", dinAC_EVSEStatusType),

		("Entry", dinEntryType),

		("AC_EVSEChargeParameter", dinAC_EVSEChargeParameterType),

		("PMaxScheduleEntry", dinPMaxScheduleEntryType),

		("EVChargeParameter", dinEVChargeParameterType),

		("ServiceDiscoveryReq", dinServiceDiscoveryReqType),

		("ServiceDiscoveryRes", dinServiceDiscoveryResType),

		("MeteringReceiptReq", dinMeteringReceiptReqType),

		("PaymentDetailsReq", dinPaymentDetailsReqType),

		("MeteringReceiptRes", dinMeteringReceiptResType),

		("PaymentDetailsRes", dinPaymentDetailsResType),

		("SessionSetupReq", dinSessionSetupReqType),

		("SessionSetupRes", dinSessionSetupResType),

		("CableCheckReq", dinCableCheckReqType),

		("CableCheckRes", dinCableCheckResType),

		("ContractAuthenticationReq", dinContractAuthenticationReqType),

		("CertificateInstallationReq", dinCertificateInstallationReqType),

		("ContractAuthenticationRes", dinContractAuthenticationResType),

		("CertificateInstallationRes", dinCertificateInstallationResType),

		("WeldingDetectionReq", dinWeldingDetectionReqType),

		("WeldingDetectionRes", dinWeldingDetectionResType),

		("CertificateUpdateReq", dinCertificateUpdateReqType),

		("CertificateUpdateRes", dinCertificateUpdateResType),

		("PowerDeliveryReq", dinPowerDeliveryReqType),

		("PowerDeliveryRes", dinPowerDeliveryResType),

		("ChargingStatusReq", dinChargingStatusReqType),

		("ChargingStatusRes", dinChargingStatusResType),

		("CurrentDemandReq", dinCurrentDemandReqType),

		("PreChargeReq", dinPreChargeReqType),

		("CurrentDemandRes", dinCurrentDemandResType),

		("PreChargeRes", dinPreChargeResType),

		("ServicePaymentSelectionReq", dinServicePaymentSelectionReqType),

		("SessionStopReq", dinSessionStopType),

		("ServicePaymentSelectionRes", dinServicePaymentSelectionResType),

		("SessionStopRes", dinSessionStopResType),

		("ChargeParameterDiscoveryReq", dinChargeParameterDiscoveryReqType),

		("ChargeParameterDiscoveryRes", dinChargeParameterDiscoveryResType),

		("ServiceDetailReq", dinServiceDetailReqType),

		("ServiceDetailRes", dinServiceDetailResType),

		("BodyElement_isUsed", c_uint, 1),

		("V2G_Message_isUsed", c_uint, 1),

		("SignatureProperty_isUsed", c_uint, 1),

		("DSAKeyValue_isUsed", c_uint, 1),

		("SignatureProperties_isUsed", c_uint, 1),

		("KeyValue_isUsed", c_uint, 1),

		("Transforms_isUsed", c_uint, 1),

		("DigestMethod_isUsed", c_uint, 1),

		("Signature_isUsed", c_uint, 1),

		("RetrievalMethod_isUsed", c_uint, 1),

		("Manifest_isUsed", c_uint, 1),

		("Reference_isUsed", c_uint, 1),

		("CanonicalizationMethod_isUsed", c_uint, 1),

		("RSAKeyValue_isUsed", c_uint, 1),

		("Transform_isUsed", c_uint, 1),

		("PGPData_isUsed", c_uint, 1),

		("MgmtData_isUsed", c_uint, 1),

		("SignatureMethod_isUsed", c_uint, 1),

		("KeyInfo_isUsed", c_uint, 1),

		("SPKIData_isUsed", c_uint, 1),

		("X509Data_isUsed", c_uint, 1),

		("SignatureValue_isUsed", c_uint, 1),

		("KeyName_isUsed", c_uint, 1),

		("DigestValue_isUsed", c_uint, 1),

		("SignedInfo_isUsed", c_uint, 1),

		("Object_isUsed", c_uint, 1),

		("DC_EVSEStatus_isUsed", c_uint, 1),

		("RelativeTimeInterval_isUsed", c_uint, 1),

		("SalesTariffEntry_isUsed", c_uint, 1),

		("DC_EVPowerDeliveryParameter_isUsed", c_uint, 1),

		("SASchedules_isUsed", c_uint, 1),

		("AC_EVChargeParameter_isUsed", c_uint, 1),

		("SAScheduleList_isUsed", c_uint, 1),

		("DC_EVStatus_isUsed", c_uint, 1),

		("ServiceCharge_isUsed", c_uint, 1),

		("EVStatus_isUsed", c_uint, 1),

		("DC_EVChargeParameter_isUsed", c_uint, 1),

		("DC_EVSEChargeParameter_isUsed", c_uint, 1),

		("EVSEStatus_isUsed", c_uint, 1),

		("TimeInterval_isUsed", c_uint, 1),

		("EVPowerDeliveryParameter_isUsed", c_uint, 1),

		("EVSEChargeParameter_isUsed", c_uint, 1),

		("AC_EVSEStatus_isUsed", c_uint, 1),

		("Entry_isUsed", c_uint, 1),

		("AC_EVSEChargeParameter_isUsed", c_uint, 1),

		("PMaxScheduleEntry_isUsed", c_uint, 1),

		("EVChargeParameter_isUsed", c_uint, 1),

		("ServiceDiscoveryReq_isUsed", c_uint, 1),

		("ServiceDiscoveryRes_isUsed", c_uint, 1),

		("MeteringReceiptReq_isUsed", c_uint, 1),

		("PaymentDetailsReq_isUsed", c_uint, 1),

		("MeteringReceiptRes_isUsed", c_uint, 1),

		("PaymentDetailsRes_isUsed", c_uint, 1),

		("SessionSetupReq_isUsed", c_uint, 1),

		("SessionSetupRes_isUsed", c_uint, 1),

		("CableCheckReq_isUsed", c_uint, 1),

		("CableCheckRes_isUsed", c_uint, 1),

		("ContractAuthenticationReq_isUsed", c_uint, 1),

		("CertificateInstallationReq_isUsed", c_uint, 1),

		("ContractAuthenticationRes_isUsed", c_uint, 1),

		("CertificateInstallationRes_isUsed", c_uint, 1),

		("WeldingDetectionReq_isUsed", c_uint, 1),

		("WeldingDetectionRes_isUsed", c_uint, 1),

		("CertificateUpdateReq_isUsed", c_uint, 1),

		("CertificateUpdateRes_isUsed", c_uint, 1),

		("PowerDeliveryReq_isUsed", c_uint, 1),

		("PowerDeliveryRes_isUsed", c_uint, 1),

		("ChargingStatusReq_isUsed", c_uint, 1),

		("ChargingStatusRes_isUsed", c_uint, 1),

		("CurrentDemandReq_isUsed", c_uint, 1),

		("PreChargeReq_isUsed", c_uint, 1),

		("CurrentDemandRes_isUsed", c_uint, 1),

		("PreChargeRes_isUsed", c_uint, 1),

		("ServicePaymentSelectionReq_isUsed", c_uint, 1),

		("SessionStopReq_isUsed", c_uint, 1),

		("ServicePaymentSelectionRes_isUsed", c_uint, 1),

		("SessionStopRes_isUsed", c_uint, 1),

		("ChargeParameterDiscoveryReq_isUsed", c_uint, 1),

		("ChargeParameterDiscoveryRes_isUsed", c_uint, 1),

		("ServiceDetailReq_isUsed", c_uint, 1),

		("ServiceDetailRes_isUsed", c_uint, 1),

		("_warning_", c_int),

	]


class dinEXIFragment(Structure):
	_fields_=[
		("Unit", c_uint),

		("EVSEMaximumCurrentLimit", dinPhysicalValueType),

		("EVPowerDeliveryParameter", dinEVPowerDeliveryParameterType),

		("ChargingProfileEntryMaxPower", c_int16),

		("TMeter", c_int64),

		("EVSEPowerLimitAchieved", c_int),

		("duration", c_uint32),

		("EVMaximumCurrentLimit", dinPhysicalValueType),

		("Parameter", dinParameterType),

		("EVSEProcessing", c_uint),

		("AC_EVChargeParameter", dinAC_EVChargeParameterType),

		("PMaxScheduleEntry", dinPMaxScheduleEntryType),

		("EVSEMaximumVoltageLimit", dinPhysicalValueType),

		("SelectedService", dinSelectedServiceType),

		("EVSEMaximumPowerLimit", dinPhysicalValueType),

		("EVReady", c_int),

		("X509SerialNumber", c_int64),

		("RetrievalMethod", dinRetrievalMethodType),

		("RetryCounter", c_int16),

		("DC_EVSEStatus", dinDC_EVSEStatusType),

		("MeteringReceiptReq", dinMeteringReceiptReqType),

		("ReadyToChargeState", c_int),

		("Multiplier", c_int8),

		("EPriceLevel", c_uint8),

		("ServiceDiscoveryReq", dinServiceDiscoveryReqType),

		("Transforms", dinTransformsType),

		("MeteringReceiptRes", dinMeteringReceiptResType),

		("PreChargeReq", dinPreChargeReqType),

		("ServiceDiscoveryRes", dinServiceDiscoveryResType),

		("ResponseCode", c_uint),

		("ContractAuthenticationReq", dinContractAuthenticationReqType),

		("ContractSignatureCertChain", dinCertificateChainType),

		("ContractAuthenticationRes", dinContractAuthenticationResType),

		("HMACOutputLength", c_int64),

		("BulkChargingComplete", c_int),

		("DC_EVStatus", dinDC_EVStatusType),

		("SAScheduleTuple", dinSAScheduleTupleType),

		("DepartureTime", c_uint32),

		("X509IssuerSerial", dinX509IssuerSerialType),

		("SAScheduleTupleID", c_int16),

		("SPKIData", dinSPKIDataType),

		("RelativeTimeInterval", dinRelativeTimeIntervalType),

		("EVEnergyRequest", dinPhysicalValueType),

		("PreChargeRes", dinPreChargeResType),

		("PMaxSchedule", dinPMaxScheduleType),

		("ServiceCharge", dinServiceChargeType),

		("ChargingStatusReq", dinChargingStatusReqType),

		("X509Data", dinX509DataType),

		("SalesTariffEntry", dinSalesTariffEntryType),

		("KeyValue", dinKeyValueType),

		("ChargingStatusRes", dinChargingStatusResType),

		("V2G_Message", dinAnonType_V2G_Message),

		("ServicePaymentSelectionReq", dinServicePaymentSelectionReqType),

		("EVSEIsolationStatus", c_uint),

		("ServicePaymentSelectionRes", dinServicePaymentSelectionResType),

		("EVSEPresentVoltage", dinPhysicalValueType),

		("BodyElement", dinBodyBaseType),

		("PGPData", dinPGPDataType),

		("FaultCode", c_uint),

		("CableCheckReq", dinCableCheckReqType),

		("EVSEVoltageLimitAchieved", c_int),

		("EVRESSConditioning", c_int),

		("MeterInfo", dinMeterInfoType),

		("CableCheckRes", dinCableCheckResType),

		("ChargingProfileEntryStart", c_uint32),

		("SignatureProperty", dinSignaturePropertyType),

		("EVMaxCurrent", dinPhysicalValueType),

		("RSAKeyValue", dinRSAKeyValueType),

		("costKind", c_uint),

		("EAmount", dinPhysicalValueType),

		("EVSEPresentCurrent", dinPhysicalValueType),

		("PowerDeliveryRes", dinPowerDeliveryResType),

		("NumEPriceLevels", c_uint8),

		("SessionStopRes", dinSessionStopResType),

		("PowerDeliveryReq", dinPowerDeliveryReqType),

		("SessionStopReq", dinSessionStopType),

		("BulkSOC", c_int8),

		("PMax", c_int16),

		("ParameterSetID", c_int16),

		("Signature", dinSignatureType),

		("EVMaxVoltage", dinPhysicalValueType),

		("ReceiptRequired", c_int),

		("ChargingComplete", c_int),

		("ChargingProfile", dinChargingProfileType),

		("PaymentOptions", dinPaymentOptionsType),

		("SessionSetupRes", dinSessionSetupResType),

		("ServiceDetailRes", dinServiceDetailResType),

		("DC_EVPowerDeliveryParameter", dinDC_EVPowerDeliveryParameterType),

		("PaymentDetailsRes", dinPaymentDetailsResType),

		("PaymentDetailsReq", dinPaymentDetailsReqType),

		("Value", c_int16),

		("EVSENotification", c_uint),

		("EVTargetCurrent", dinPhysicalValueType),

		("RemainingTimeToBulkSoC", dinPhysicalValueType),

		("SessionSetupReq", dinSessionSetupReqType),

		("EVSECurrentLimitAchieved", c_int),

		("ServiceDetailReq", dinServiceDetailReqType),

		("byteValue", c_int8),

		("EVMaximumPowerLimit", dinPhysicalValueType),

		("PowerSwitchClosed", c_int),

		("Manifest", dinManifestType),

		("SAScheduleList", dinSAScheduleListType),

		("CertificateInstallationRes", dinCertificateInstallationResType),

		("CertificateInstallationReq", dinCertificateInstallationReqType),

		("SalesTariff", dinSalesTariffType),

		("Header", dinMessageHeaderType),

		("EVSEMinimumCurrentLimit", dinPhysicalValueType),

		("DC_EVChargeParameter", dinDC_EVChargeParameterType),

		("DigestMethod", dinDigestMethodType),

		("ChargeService", dinServiceChargeType),

		("EVSEEnergyToBeDelivered", dinPhysicalValueType),

		("SignatureProperties", dinSignaturePropertiesType),

		("EVSEMaxCurrent", dinPhysicalValueType),

		("EVSEStatus", dinEVSEStatusType),

		("Service", dinServiceType),

		("DSAKeyValue", dinDSAKeyValueType),

		("EnergyTransferType", c_uint),

		("WeldingDetectionRes", dinWeldingDetectionResType),

		("FreeService", c_int),

		("SelectedServiceList", dinSelectedServiceListType),

		("WeldingDetectionReq", dinWeldingDetectionReqType),

		("EVTargetVoltage", dinPhysicalValueType),

		("CanonicalizationMethod", dinCanonicalizationMethodType),

		("CertificateUpdateRes", dinCertificateUpdateResType),

		("CertificateUpdateReq", dinCertificateUpdateReqType),

		("EVSEMaxVoltage", dinPhysicalValueType),

		("SignedInfo", dinSignedInfoType),

		("AC_EVSEChargeParameter", dinAC_EVSEChargeParameterType),

		("EVEnergyCapacity", dinPhysicalValueType),

		("ServiceID", c_uint16),

		("EVSECurrentRegulationTolerance", dinPhysicalValueType),

		("ServiceParameterList", dinServiceParameterListType),

		("ListOfRootCertificateIDs", dinListOfRootCertificateIDsType),

		("ProfileEntry", dinProfileEntryType),

		("EVSEMinimumVoltageLimit", dinPhysicalValueType),

		("CurrentDemandRes", dinCurrentDemandResType),

		("EVRESSSOC", c_int8),

		("MeterReading", dinPhysicalValueType),

		("CurrentDemandReq", dinCurrentDemandReqType),

		("physicalValue", dinPhysicalValueType),

		("TimeInterval", dinIntervalType),

		("AC_EVSEStatus", dinAC_EVSEStatusType),

		("EVMaximumVoltageLimit", dinPhysicalValueType),

		("SignatureValue", dinSignatureValueType),

		("DateTimeNow", c_int64),

		("ServiceTag", dinServiceTagType),

		("intValue", c_int32),

		("SelectedPaymentOption", c_uint),

		("EVCabinConditioning", c_int),

		("MeterStatus", c_int16),

		("EVRequestedEnergyTransferType", c_uint),

		("ServiceCategory", c_uint),

		("NotificationMaxDelay", c_uint32),

		("boolValue", c_int),

		("EVSEStatusCode", c_uint),

		("ParameterSet", dinParameterSetType),

		("EVSEChargeParameter", dinEVSEChargeParameterType),

		("Body", dinBodyType),

		("SASchedules", dinSASchedulesType),

		("KeyInfo", dinKeyInfoType),

		("PMaxScheduleID", c_int16),

		("RemainingTimeToFullSoC", dinPhysicalValueType),

		("EVStatus", dinEVStatusType),

		("SubCertificates", dinSubCertificatesType),

		("PaymentOption", c_uint),

		("ServiceList", dinServiceTagListType),

		("Cost", dinCostType),

		("SignatureMethod", dinSignatureMethodType),

		("EVSEMinCurrent", dinPhysicalValueType),

		("ConsumptionCost", dinConsumptionCostType),

		("EVSEPeakCurrentRipple", dinPhysicalValueType),

		("EVErrorCode", c_uint),

		("EVChargeParameter", dinEVChargeParameterType),

		("start", c_uint32),

		("Reference", dinReferenceType),

		("EVMinCurrent", dinPhysicalValueType),

		("FullSOC", c_int8),

		("amount", c_uint32),

		("shortValue", c_int16),

		("DC_EVSEChargeParameter", dinDC_EVSEChargeParameterType),

		("Entry", dinEntryType),

		("SalesTariffID", c_int16),

		("ChargeParameterDiscoveryReq", dinChargeParameterDiscoveryReqType),

		("amountMultiplier", c_int8),

		("ChargeParameterDiscoveryRes", dinChargeParameterDiscoveryResType),

		("Transform", dinTransformType),

		("Object", dinObjectType),

		("RCD", c_int),

		("Notification", dinNotificationType),

		("startValue", c_uint32),

		("Certificate", ArrayType_factory(c_uint8, "bytes", EXIFragment_Certificate_BYTES_SIZE)),

		("stringValue", ArrayType_factory(c_uint32, "characters", EXIFragment_stringValue_CHARACTERS_SIZE)),

		("OEMProvisioningCert", ArrayType_factory(c_uint8, "bytes", EXIFragment_OEMProvisioningCert_BYTES_SIZE)),

		("Exponent", ArrayType_factory(c_uint8, "bytes", EXIFragment_Exponent_BYTES_SIZE)),

		("SessionID", ArrayType_factory(c_uint8, "bytes", EXIFragment_SessionID_BYTES_SIZE)),

		("PgenCounter", ArrayType_factory(c_uint8, "bytes", EXIFragment_PgenCounter_BYTES_SIZE)),

		("EVCCID", ArrayType_factory(c_uint8, "bytes", EXIFragment_EVCCID_BYTES_SIZE)),

		("RootCertificateID", ArrayType_factory(c_uint32, "characters", EXIFragment_RootCertificateID_CHARACTERS_SIZE)),

		("PGPKeyPacket", ArrayType_factory(c_uint8, "bytes", EXIFragment_PGPKeyPacket_BYTES_SIZE)),

		("Seed", ArrayType_factory(c_uint8, "bytes", EXIFragment_Seed_BYTES_SIZE)),

		("XPath", ArrayType_factory(c_uint32, "characters", EXIFragment_XPath_CHARACTERS_SIZE)),

		("ContractID", ArrayType_factory(c_uint32, "characters", EXIFragment_ContractID_CHARACTERS_SIZE)),

		("MgmtData", ArrayType_factory(c_uint32, "characters", EXIFragment_MgmtData_CHARACTERS_SIZE)),

		("P", ArrayType_factory(c_uint8, "bytes", EXIFragment_P_BYTES_SIZE)),

		("Q", ArrayType_factory(c_uint8, "bytes", EXIFragment_Q_BYTES_SIZE)),

		("X509SubjectName", ArrayType_factory(c_uint32, "characters", EXIFragment_X509SubjectName_CHARACTERS_SIZE)),

		("G", ArrayType_factory(c_uint8, "bytes", EXIFragment_G_BYTES_SIZE)),

		("J", ArrayType_factory(c_uint8, "bytes", EXIFragment_J_BYTES_SIZE)),

		("X509CRL", ArrayType_factory(c_uint8, "bytes", EXIFragment_X509CRL_BYTES_SIZE)),

		("Y", ArrayType_factory(c_uint8, "bytes", EXIFragment_Y_BYTES_SIZE)),

		("DigestValue", ArrayType_factory(c_uint8, "bytes", EXIFragment_DigestValue_BYTES_SIZE)),

		("ContractSignatureEncryptedPrivateKey", ArrayType_factory(c_uint8, "bytes", EXIFragment_ContractSignatureEncryptedPrivateKey_BYTES_SIZE)),

		("SPKISexp", ArrayType_factory(c_uint8, "bytes", EXIFragment_SPKISexp_BYTES_SIZE)),

		("DHParams", ArrayType_factory(c_uint8, "bytes", EXIFragment_DHParams_BYTES_SIZE)),

		("PGPKeyID", ArrayType_factory(c_uint8, "bytes", EXIFragment_PGPKeyID_BYTES_SIZE)),

		("X509Certificate", ArrayType_factory(c_uint8, "bytes", EXIFragment_X509Certificate_BYTES_SIZE)),

		("ServiceName", ArrayType_factory(c_uint32, "characters", EXIFragment_ServiceName_CHARACTERS_SIZE)),

		("EVSEID", ArrayType_factory(c_uint8, "bytes", EXIFragment_EVSEID_BYTES_SIZE)),

		("ServiceScope", ArrayType_factory(c_uint32, "characters", EXIFragment_ServiceScope_CHARACTERS_SIZE)),

		("GenChallenge", ArrayType_factory(c_uint32, "characters", EXIFragment_GenChallenge_CHARACTERS_SIZE)),

		("SalesTariffDescription", ArrayType_factory(c_uint32, "characters", EXIFragment_SalesTariffDescription_CHARACTERS_SIZE)),

		("FaultMsg", ArrayType_factory(c_uint32, "characters", EXIFragment_FaultMsg_CHARACTERS_SIZE)),

		("KeyName", ArrayType_factory(c_uint32, "characters", EXIFragment_KeyName_CHARACTERS_SIZE)),

		("SigMeterReading", ArrayType_factory(c_uint8, "bytes", EXIFragment_SigMeterReading_BYTES_SIZE)),

		("X509SKI", ArrayType_factory(c_uint8, "bytes", EXIFragment_X509SKI_BYTES_SIZE)),

		("X509IssuerName", ArrayType_factory(c_uint32, "characters", EXIFragment_X509IssuerName_CHARACTERS_SIZE)),

		("MeterID", ArrayType_factory(c_uint32, "characters", EXIFragment_MeterID_CHARACTERS_SIZE)),

		("Modulus", ArrayType_factory(c_uint8, "bytes", EXIFragment_Modulus_BYTES_SIZE)),
	]


