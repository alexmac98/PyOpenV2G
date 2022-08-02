import ctypes
from typing import Any

from pyrsistent import l
import open_v2g_structs as OV2GStructs
import open_v2g_constants as OV2GConstants 
from open_v2g_utils import OpenV2GUtils
from open_v2g_constants import *

class OpenV2GStructDeclarator:
    def appHandAppProtocolType( ProtocolNamespace: str="", 
                                VersionNumberMajor: int=0, 
                                VersionNumberMinor: int=0, 
                                SchemaID: int=0, 
                                Priority: int=0):
        converted_protocol_namespace = OpenV2GUtils.convert_to_array_type_characters(val=ProtocolNamespace, size=appHandAppProtocolType_ProtocolNamespace_CHARACTERS_SIZE)
        struct = OV2GStructs.appHandAppProtocolType()
        struct.ProtocolNamespace.characters = converted_protocol_namespace
        struct.ProtocolNamespace.charactersLen = len(ProtocolNamespace)
        struct.VersionNumberMajor = VersionNumberMajor
        struct.VersionNumberMinor = VersionNumberMinor
        struct.SchemaID = SchemaID
        struct.Priority = Priority
        return struct

    def appHandAnonType_supportedAppProtocolRes(ResponseCode: int=0, 
                                                SchemaID: int=0, 
                                                SchemaID_isUsed: int=0):
        struct = OV2GStructs.appHandAnonType_supportedAppProtocolRes()
        struct.ResponseCode = ResponseCode
        struct.SchemaID = SchemaID
        struct.SchemaID_isUsed = SchemaID_isUsed
        return struct

    def appHandAnonType_supportedAppProtocolReq(AppProtocol: list[OV2GStructs.appHandAppProtocolType]=[]):
        struct = OV2GStructs.appHandAnonType_supportedAppProtocolReq()
        for i in range(len(AppProtocol)):
            struct.AppProtocol.array[i] = AppProtocol[i]
        struct.AppProtocol.arrayLen = len(AppProtocol)
        return struct

    def appHandEXIDocument( supportedAppProtocolReq: OV2GStructs.appHandAnonType_supportedAppProtocolReq=appHandAnonType_supportedAppProtocolReq(), 
                            supportedAppProtocolRes: OV2GStructs.appHandAnonType_supportedAppProtocolRes=appHandAnonType_supportedAppProtocolRes(), 
                            supportedAppProtocolReq_isUsed: int=0, 
                            supportedAppProtocolRes_isUsed: int=0, 
                            _warning_: int=0):
        struct = OV2GStructs.appHandEXIDocument()
        struct.supportedAppProtocolReq = supportedAppProtocolReq
        struct.supportedAppProtocolRes = supportedAppProtocolRes
        struct.supportedAppProtocolReq_isUsed = supportedAppProtocolReq_isUsed
        struct.supportedAppProtocolRes_isUsed = supportedAppProtocolRes_isUsed
        struct._warning_ = _warning_
        return struct

    def bitstream_t(size: ctypes.c_size_t, 
                    data: (ctypes.c_ubyte*256), 
                    pos: ctypes.c_size_t, 
                    buffer: ctypes.c_uint8, 
                    capacity: ctypes.c_uint8):
        struct = OV2GStructs.bitstream_t()
        struct.size = size
        struct.data = ctypes.cast(data, ctypes.POINTER(ctypes.c_ubyte))
        struct.pos = ctypes.pointer(pos)
        struct.buffer = buffer
        struct.capacity = capacity
        return struct


    def dinSessionSetupReqType( EVCCID: int=0):
        struct = OV2GStructs.dinSessionSetupReqType()
        struct.EVCCID.bytes = OpenV2GUtils.convert_to_array_type_bytes(EVCCID)
        struct.EVCCID.bytesLen = dinSessionSetupReqType_EVCCID_BYTES_SIZE
        return struct

    def dinEVSEStatusType(noContent=0):
        struct = OV2GStructs.dinEVSEStatusType()
        struct.noContent = noContent
        return struct
        
    def dinAC_EVSEStatusType(   PowerSwitchClosed: int=0, 
                                RCD: int=0, 
                                NotificationMaxDelay: int=0, 
                                EVSENotification: int=0):
        struct = OV2GStructs.dinAC_EVSEStatusType()
        struct.PowerSwitchClosed = PowerSwitchClosed
        struct.RCD = RCD 
        struct.NotificationMaxDelay = NotificationMaxDelay
        struct.EVSENotification = EVSENotification
        return struct
        
    def dinDC_EVSEStatusType(   EVSEIsolationStatus: int=0, 
                                EVSEIsolationStatus_isUsed: int=0, 
                                EVSEStatusCode: int=0,
                                NotificationMaxDelay: int=0, 
                                EVSENotification: int=0):
        struct = OV2GStructs.dinDC_EVSEStatusType()
        struct.EVSEIsolationStatus = EVSEIsolationStatus
        struct.EVSEIsolationStatus_isUsed = EVSEIsolationStatus_isUsed
        struct.EVSEStatusCode = EVSEStatusCode
        struct.NotificationMaxDelay = NotificationMaxDelay
        struct.EVSENotification = EVSENotification
        return struct

    def dinPowerDeliveryResType(ResponseCode: int=0, 
                                EVSEStatus: OV2GStructs.dinEVSEStatusType=dinEVSEStatusType(), 
                                EVSEStatus_isUsed: int=0, 
                                AC_EVSEStatus: OV2GStructs.dinAC_EVSEStatusType=dinAC_EVSEStatusType(), 
                                AC_EVSEStatus_isUsed: int=0, 
                                DC_EVSEStatus: OV2GStructs.dinDC_EVSEStatusType=dinDC_EVSEStatusType(), 
                                DC_EVSEStatus_isUsed: int=0):
        struct = OV2GStructs.dinPowerDeliveryResType()
        struct.ResponseCode = ResponseCode
        struct.EVSEStatus = EVSEStatus
        struct.EVSEStatus_isUsed = EVSEStatus_isUsed
        struct.AC_EVSEStatus = AC_EVSEStatus
        struct.AC_EVSEStatus_isUsed = AC_EVSEStatus_isUsed
        struct.DC_EVSEStatus = DC_EVSEStatus
        struct.DC_EVSEStatus_isUsed = DC_EVSEStatus_isUsed
        return struct  

    def dinPhysicalValueType(   Multiplier: int=0, 
                                Unit: int=0, 
                                Unit_isUsed: int=0, 
                                Value: int=0):
        struct = OV2GStructs.dinPhysicalValueType()
        struct.Multiplier = Multiplier
        struct.Unit = Unit
        struct.Unit_isUsed = Unit_isUsed
        struct.Value = Value
        return struct

    def dinParameterType(   Name: str="", 
                            ValueType: int=0, 
                            boolValue: int=0, 
                            boolValue_isUsed: int=0, 
                            byteValue: int=0, 
                            byteValue_isUsed: int=0, 
                            shortValue: int=0, 
                            shortValue_isUsed: int=0, 
                            intValue: int=0, 
                            intValue_isUsed: int=0, 
                            physicalValue: OV2GStructs.dinPhysicalValueType=dinPhysicalValueType(), 
                            physicalValue_isUsed: int=0, 
                            stringValue: str="", 
                            stringValue_isUsed: int=0):

        converted_name = OpenV2GUtils.convert_to_array_type_characters(val=Name)
        converted_string_value = OpenV2GUtils.convert_to_array_type_characters(val=stringValue)
        struct = OV2GStructs.dinParameterType()
        struct.Name.characters = converted_name
        struct.Name.charactersLen = len(Name)
        struct.ValueType = ValueType
        struct.boolValue = boolValue
        struct.boolValue_isUsed = boolValue_isUsed
        struct.byteValue = byteValue
        struct.byteValue_isUsed = byteValue_isUsed
        struct.shortValue = shortValue
        struct.shortValue_isUsed = shortValue_isUsed
        struct.intValue = intValue
        struct.intValue_isUsed = intValue_isUsed
        struct.physicalValue = physicalValue
        struct.physicalValue_isUsed = physicalValue_isUsed
        struct.stringValue.characters = converted_string_value
        struct.stringValue.charactersLen = len(stringValue)
        struct.stringValue_isUsed = stringValue_isUsed
        return struct

    def dinParameterSetType(ParameterSetID: int=0, 
                            Parameter: list[OV2GStructs.dinParameterType]=[]):
        converted_array = (OV2GStructs.dinParameterType*dinParameterSetType_Parameter_ARRAY_SIZE)(*Parameter)
        struct = OV2GStructs.dinParameterSetType()
        struct.ParameterSetID = ParameterSetID
        struct.Parameter.array = converted_array
        struct.Parameter.arrayLen = len(Parameter)
        return struct


    def dinServiceParameterListType(ParameterSet: list[OV2GStructs.dinParameterSetType]=[]):
        converted_array = (OV2GStructs.dinParameterSetType*dinServiceParameterListType_ParameterSet_ARRAY_SIZE)(*ParameterSet)
        struct = OV2GStructs.dinServiceParameterListType()
        struct.ParameterSet.array = converted_array
        struct.ParameterSet.arrayLen = len(ParameterSet)
        return struct


    def dinServiceDetailResType(ResponseCode: int=0, 
                                ServiceID: int=0, 
                                ServiceParameterList: OV2GStructs.dinServiceParameterListType=dinServiceParameterListType(), 
                                ServiceParameterList_isUsed: int=0):
        struct = OV2GStructs.dinServiceDetailResType()
        struct.ResponseCode = ResponseCode
        struct.ServiceID = ServiceID
        struct.ServiceParameterList = ServiceParameterList
        struct.ServiceParameterList_isUsed = ServiceParameterList_isUsed
        return struct

    
    def dinWeldingDetectionResType( ResponseCode: int=0, 
                                    DC_EVSEStatus: OV2GStructs.dinDC_EVSEStatusType=dinDC_EVSEStatusType(), 
                                    EVSEPresentVoltage: OV2GStructs.dinPhysicalValueType=dinPhysicalValueType()):
        struct = OV2GStructs.dinWeldingDetectionResType()
        struct.ResponseCode = ResponseCode
        struct.DC_EVSEStatus = DC_EVSEStatus
        struct.EVSEPresentVoltage = EVSEPresentVoltage
        return struct


    def dinContractAuthenticationResType(   ResponseCode: int=0, 
                                            EVSEProcessing: int=0):
        struct = OV2GStructs.dinContractAuthenticationResType()
        struct.ResponseCode = ResponseCode
        struct.EVSEProcessing = EVSEProcessing
        return struct

    
    def dinCanonicalizationMethodType(  Algorithm: str="", 
                                        ANY: str="", 
                                        ANY_isUsed: int=0):
        converted_algorithm = OpenV2GUtils.convert_to_array_type_characters(val=Algorithm, size=dinCanonicalizationMethodType_Algorithm_CHARACTERS_SIZE)
        converted_any = OpenV2GUtils.convert_to_array_type_characters(val=ANY, size=dinCanonicalizationMethodType_ANY_CHARACTERS_SIZE)
        struct = OV2GStructs.dinCanonicalizationMethodType()
        struct.Algorithm.characters = converted_algorithm
        struct.Algorithm.charactersLen = len(Algorithm)
        struct.ANY.characters = converted_any
        struct.ANY.charactersLen = len(ANY)
        struct.ANY_isUsed = ANY_isUsed
        return struct


    def dinSPKIDataType(SPKISexp: int=0, 
                        ANY: str="", 
                        ANY_isUsed: int=0):
        converted_any = OpenV2GUtils.convert_to_array_type_characters(val=ANY, size=dinSPKIDataType_ANY_CHARACTERS_SIZE)
        converted_spki_exp = OpenV2GUtils.convert_to_array_type_bytes(val=SPKISexp, size=dinSPKIDataType_SPKISexp_BYTES_SIZE)
        struct = OV2GStructs.dinSPKIDataType()
        struct.SPKISexp.array[0].bytes =  converted_spki_exp
        struct.SPKISexp.array[0].bytesLen = dinSPKIDataType_SPKISexp_BYTES_SIZE
        struct.SPKISexp.arrayLen = dinSPKIDataType_SPKISexp_ARRAY_SIZE
        struct.ANY.characters = converted_any
        struct.ANY.charactersLen = len(ANY)
        struct.ANY_isUsed = ANY_isUsed
        return struct        

    
    def dinListOfRootCertificateIDsType(RootCertificateID: list[str]=[]):
        struct = OV2GStructs.dinListOfRootCertificateIDsType()

        for i in range(len(RootCertificateID)):
            converted_characters = OpenV2GUtils.convert_to_array_type_characters(val=RootCertificateID[i], size=dinListOfRootCertificateIDsType_RootCertificateID_CHARACTERS_SIZE)
            struct.RootCertificateID.array[i].characters = converted_characters
            struct.RootCertificateID.array[i].charactersLen = len(RootCertificateID[i])
        
        struct.RootCertificateID.arrayLen = len(RootCertificateID)        
        return struct


    def dinSelectedServiceType( ServiceID: int=0, 
                                ParameterSetID: int=0, 
                                ParameterSetID_isUsed: int=0):
        struct = OV2GStructs.dinSelectedServiceType()
        struct.ServiceID = ServiceID
        struct.ParameterSetID = ParameterSetID
        struct.ParameterSetID_isUsed = ParameterSetID_isUsed
        return struct


    def dinSelectedServiceListType(SelectedService: list[OV2GStructs.dinSelectedServiceType]=[]):
        struct = OV2GStructs.dinSelectedServiceListType()
        for i in range(len(SelectedService)):
            struct.SelectedService.array[i] = SelectedService[i]
        struct.SelectedService.arrayLen = len(SelectedService)
        return struct


    def dinCurrentDemandResType(ResponseCode: int=0, 
                                DC_EVSEStatus: OV2GStructs.dinDC_EVSEStatusType=dinDC_EVSEStatusType(),
                                EVSEPresentVoltage: OV2GStructs.dinPhysicalValueType=dinPhysicalValueType(),
                                EVSEPresentCurrent: OV2GStructs.dinPhysicalValueType=dinPhysicalValueType(),
                                EVSECurrentLimitAchieved: int=0,
                                EVSEVoltageLimitAchieved: int=0,
                                EVSEPowerLimitAchieved: int=0,
                                EVSEMaximumVoltageLimit: OV2GStructs.dinPhysicalValueType=dinPhysicalValueType(),
                                EVSEMaximumVoltageLimit_isUsed: int=0,
                                EVSEMaximumCurrentLimit: OV2GStructs.dinPhysicalValueType=dinPhysicalValueType(),
                                EVSEMaximumCurrentLimit_isUsed: int=0,
                                EVSEMaximumPowerLimit: OV2GStructs.dinPhysicalValueType=dinPhysicalValueType(),
                                EVSEMaximumPowerLimit_isUsed: int=0):

        struct = OV2GStructs.dinCurrentDemandResType()
        struct.ResponseCode = ResponseCode
        struct.DC_EVSEStatus = DC_EVSEStatus
        struct.EVSEPresentVoltage = EVSEPresentVoltage
        struct.EVSEPresentCurrent = EVSEPresentCurrent
        struct.EVSECurrentLimitAchieved = EVSECurrentLimitAchieved
        struct.EVSEVoltageLimitAchieved = EVSEVoltageLimitAchieved
        struct.EVSEPowerLimitAchieved = EVSEPowerLimitAchieved
        struct.EVSEMaximumVoltageLimit = EVSEMaximumVoltageLimit
        struct.EVSEMaximumVoltageLimit_isUsed = EVSEMaximumVoltageLimit_isUsed
        struct.EVSEMaximumCurrentLimit = EVSEMaximumCurrentLimit
        struct.EVSEMaximumCurrentLimit_isUsed = EVSEMaximumCurrentLimit_isUsed
        struct.EVSEMaximumPowerLimit = EVSEMaximumPowerLimit
        struct.EVSEMaximumPowerLimit_isUsed = EVSEMaximumPowerLimit_isUsed
        return struct


    def dinTransformType(   Algorithm: str="", 
                            ANY: str="", 
                            ANY_isUsed: int=0, 
                            XPath: str=""):
        converted_algorithm = OpenV2GUtils.convert_to_array_type_characters(val=Algorithm, size=dinTransformType_Algorithm_CHARACTERS_SIZE)
        converted_any = OpenV2GUtils.convert_to_array_type_characters(val=ANY, size=dinTransformType_ANY_CHARACTERS_SIZE)
        converted_xpath = OpenV2GUtils.convert_to_array_type_characters(val=XPath, size=dinTransformType_XPath_CHARACTERS_SIZE)
        struct = OV2GStructs.dinTransformType()
        struct.Algorithm.characters = converted_algorithm
        struct.Algorithm.charactersLen = len(Algorithm)
        struct.ANY.characters = converted_any
        struct.ANY.charactersLen = len(ANY)
        struct.ANY_isUsed = ANY_isUsed
        struct.XPath.array[0].characters = converted_xpath
        struct.XPath.array[0].charactersLen = len(XPath)
        struct.XPath.arrayLen = dinTransformType_XPath_ARRAY_SIZE
        return struct


    def dinAC_EVChargeParameterType(DepartureTime: int=0, 
                                    EAmount: OV2GStructs.dinPhysicalValueType=dinPhysicalValueType(),
                                    EVMaxVoltage: OV2GStructs.dinPhysicalValueType=dinPhysicalValueType(),
                                    EVMaxCurrent: OV2GStructs.dinPhysicalValueType=dinPhysicalValueType(),
                                    EVMinCurrent: OV2GStructs.dinPhysicalValueType=dinPhysicalValueType()):

        struct = OV2GStructs.dinAC_EVChargeParameterType()                                        
        struct.DepartureTime = DepartureTime
        struct.EAmount = EAmount
        struct.EVMaxVoltage = EVMaxVoltage
        struct.EVMaxCurrent = EVMaxCurrent
        struct.EVMinCurrent = EVMinCurrent
        return struct


    def dinX509IssuerSerialType(X509IssuerName: str="", 
                                X509SerialNumber: int=0):
        converted_x509_issuer_name = OpenV2GUtils.convert_to_array_type_characters(val=X509IssuerName, size=dinX509IssuerSerialType_X509IssuerName_CHARACTERS_SIZE)
        struct = OV2GStructs.dinX509IssuerSerialType()
        struct.X509IssuerName.characters = converted_x509_issuer_name
        struct.X509IssuerName.charactersLen = len(X509IssuerName)
        struct.X509SerialNumber = X509SerialNumber
        return struct


    def dinX509DataType(X509IssuerSerial: list[OV2GStructs.dinX509IssuerSerialType]=[dinX509IssuerSerialType()], 
                        X509SKI: int=0, 
                        X509SubjectName: str="", 
                        X509Certificate: int=0,
                        X509CRL: int=0,
                        ANY: str="",
                        ANY_isUsed: int=0):

        converted_any = OpenV2GUtils.convert_to_array_type_characters(val=ANY, size=dinX509DataType_ANY_CHARACTERS_SIZE)
        converted_x509_subject_name = OpenV2GUtils.convert_to_array_type_characters(val=X509SubjectName, size=dinX509DataType_X509SubjectName_CHARACTERS_SIZE)
        converted_x509_ski = OpenV2GUtils.convert_to_array_type_bytes(val=X509SKI, size=dinX509DataType_X509SKI_BYTES_SIZE)
        converted_x509_certificate = OpenV2GUtils.convert_to_array_type_bytes(val=X509Certificate, size=dinX509DataType_X509Certificate_BYTES_SIZE)
        converted_x509_crl = OpenV2GUtils.convert_to_array_type_bytes(val=X509CRL, size=dinX509DataType_X509CRL_BYTES_SIZE)
        struct = OV2GStructs.dinX509DataType()
        struct.X509IssuerSerial.array[0] = X509IssuerSerial[0]
        struct.X509IssuerSerial.arrayLen = dinX509DataType_X509IssuerSerial_ARRAY_SIZE
        struct.X509SKI.array[0].bytes = converted_x509_ski
        struct.X509SKI.array[0].bytesLen = dinX509DataType_X509SKI_BYTES_SIZE
        struct.X509SKI.arrayLen = dinX509DataType_X509SKI_ARRAY_SIZE
        struct.X509SubjectName.array[0].characters = converted_x509_subject_name
        struct.X509SubjectName.array[0].charactersLen = len(X509SubjectName)
        struct.X509SubjectName.arrayLen = dinX509DataType_X509SubjectName_ARRAY_SIZE
        struct.X509Certificate.array[0].bytes = converted_x509_certificate
        struct.X509Certificate.array[0].bytesLen = dinX509DataType_X509Certificate_BYTES_SIZE
        struct.X509Certificate.arrayLen = dinX509DataType_X509Certificate_ARRAY_SIZE
        struct.X509CRL.array[0].bytes = converted_x509_crl
        struct.X509CRL.array[0].bytesLen = dinX509DataType_X509CRL_BYTES_SIZE
        struct.X509CRL.arrayLen = dinX509DataType_X509CRL_ARRAY_SIZE
        struct.ANY.characters = converted_any
        struct.ANY.charactersLen = len(ANY)
        struct.ANY_isUsed = ANY_isUsed
        return struct

    def dinMeterInfoType(   MeterID: str="",
                            MeterReading: OV2GStructs.dinPhysicalValueType=dinPhysicalValueType(),
                            MeterReading_isUsed: int=0,
                            SigMeterReading: int=0,
                            SigMeterReading_isUsed: int=0,
                            MeterStatus: int=0,
                            MeterStatus_isUsed: int=0,
                            TMeter: int=0,
                            TMeter_isUsed: int=0):
        
        converted_meter_id = OpenV2GUtils.convert_to_array_type_characters(val=MeterID, size=dinMeterInfoType_MeterID_CHARACTERS_SIZE)
        converted_sig_meter_reading = OpenV2GUtils.convert_to_array_type_bytes(val=SigMeterReading, size=dinMeterInfoType_SigMeterReading_BYTES_SIZE)
        struct = OV2GStructs.dinMeterInfoType()
        struct.MeterID.characters = converted_meter_id
        struct.MeterID.charactersLen = len(MeterID)
        struct.MeterReading = MeterReading
        struct.MeterReading_isUsed = MeterReading_isUsed
        struct.SigMeterReading.bytes = converted_sig_meter_reading
        struct.SigMeterReading.bytesLen = dinMeterInfoType_SigMeterReading_BYTES_SIZE
        struct.SigMeterReading_isUsed = SigMeterReading_isUsed
        struct.MeterStatus = MeterStatus
        struct.MeterStatus_isUsed = MeterStatus_isUsed
        struct.TMeter = TMeter
        struct.TMeter_isUsed = TMeter_isUsed
        return struct
        

    def dinChargingStatusResType(   ResponseCode: int=0,
                                    EVSEID: int=0,
                                    SAScheduleTupleID: int=0,
                                    EVSEMaxCurrent: OV2GStructs.dinPhysicalValueType=dinPhysicalValueType(),
                                    EVSEMaxCurrent_isUsed: int=0,
                                    MeterInfo: OV2GStructs.dinMeterInfoType=dinMeterInfoType(),
                                    MeterInfo_isUsed: int=0,
                                    ReceiptRequired: int=0,
                                    AC_EVSEStatus: OV2GStructs.dinAC_EVSEStatusType=dinAC_EVSEStatusType()):

        converted_evse_id = OpenV2GUtils.convert_to_array_type_bytes(val=EVSEID, size=dinChargingStatusResType_EVSEID_BYTES_SIZE)
        struct = OV2GStructs.dinChargingStatusResType()
        struct.ResponseCode = ResponseCode
        struct.EVSEID.bytes = converted_evse_id
        struct.EVSEID.bytesLen = dinChargingStatusResType_EVSEID_BYTES_SIZE
        struct.SAScheduleTupleID = SAScheduleTupleID
        struct.EVSEMaxCurrent = EVSEMaxCurrent
        struct.EVSEMaxCurrent_isUsed = EVSEMaxCurrent_isUsed
        struct.MeterInfo = MeterInfo
        struct.MeterInfo_isUsed = MeterInfo_isUsed
        struct.ReceiptRequired = ReceiptRequired
        struct.AC_EVSEStatus = AC_EVSEStatus
        return struct


    def dinDC_EVStatusType( EVReady: int=0, 
                            EVCabinConditioning: int=0, 
                            EVCabinConditioning_isUsed: int=0,
                            EVRESSConditioning: int=0,
                            EVRESSConditioning_isUsed: int=0,
                            EVErrorCode: int=0,
                            EVRESSSOC: int=0):
        struct = OV2GStructs.dinDC_EVStatusType()
        struct.EVReady = EVReady 
        struct.EVCabinConditioning = EVCabinConditioning 
        struct.EVCabinConditioning_isUsed = EVCabinConditioning_isUsed
        struct.EVRESSConditioning = EVRESSConditioning
        struct.EVRESSConditioning_isUsed = EVRESSConditioning_isUsed
        struct.EVErrorCode = EVErrorCode
        struct.EVRESSSOC = EVRESSSOC        
        return struct
    
    def dinWeldingDetectionReqType(DC_EVStatus: OV2GStructs.dinDC_EVStatusType=dinDC_EVStatusType()):
        struct = OV2GStructs.dinWeldingDetectionReqType()
        struct.DC_EVStatus = DC_EVStatus
        return struct


    def dinSignaturePropertyType(   Target: str="", 
                                    Id: str="", 
                                    Id_isUsed: int=0, 
                                    ANY: str="", 
                                    ANY_isUsed: int=0):
        converted_type = OpenV2GUtils.convert_to_array_type_characters(val=Target, size=dinSignaturePropertyType_Target_CHARACTERS_SIZE)
        converted_id = OpenV2GUtils.convert_to_array_type_characters(val=Id, size=dinSignaturePropertyType_Id_CHARACTERS_SIZE)
        converted_any = OpenV2GUtils.convert_to_array_type_characters(val=ANY, size=dinSignaturePropertyType_ANY_CHARACTERS_SIZE)
        struct = OV2GStructs.dinSignaturePropertyType()
        struct.Target.characters = converted_type
        struct.Target.charactersLen = len(Target)
        struct.Id.characters = converted_id
        struct.Id.charactersLen = len(Id)
        struct.Id_isUsed = Id_isUsed
        struct.ANY.characters = converted_any
        struct.ANY.charactersLen = len(ANY)
        struct.ANY_isUsed = ANY_isUsed
        return struct
    

    def dinSignaturePropertiesType( Id: str="", 
                                    Id_isUsed: int=0, 
                                    SignatureProperty: list[OV2GStructs.dinSignaturePropertyType]=[dinSignaturePropertyType()]):
        converted_id = OpenV2GUtils.convert_to_array_type_characters(val=Id, size=dinSignaturePropertiesType_Id_CHARACTERS_SIZE)
        struct = OV2GStructs.dinSignaturePropertiesType()
        struct.Id.characters = converted_id
        struct.Id.charactersLen = len(Id)
        struct.Id_isUsed = Id_isUsed
        struct.SignatureProperty.array[0] = SignatureProperty[0]
        struct.SignatureProperty.arrayLen = dinSignaturePropertiesType_SignatureProperty_ARRAY_SIZE
        return struct


    def dinContractAuthenticationReqType(   Id: str="", 
                                            Id_isUsed: int=0, 
                                            GenChallenge: str="", 
                                            GenChallenge_isUsed: int=0):
        converted_id = OpenV2GUtils.convert_to_array_type_characters(val=Id, size=dinContractAuthenticationReqType_Id_CHARACTERS_SIZE)
        converted_gen_challenge = OpenV2GUtils.convert_to_array_type_characters(val=GenChallenge, size=dinContractAuthenticationReqType_GenChallenge_CHARACTERS_SIZE)
        struct = OV2GStructs.dinContractAuthenticationReqType()
        struct.Id.characters = converted_id
        struct.Id.charactersLen = len(Id)
        struct.Id_isUsed = Id_isUsed
        struct.GenChallenge.characters = converted_gen_challenge
        struct.GenChallenge.charactersLen = len(GenChallenge)
        struct.GenChallenge_isUsed = GenChallenge_isUsed
        return struct


    def dinDC_EVPowerDeliveryParameterType( DC_EVStatus: OV2GStructs.dinDC_EVStatusType=dinDC_EVStatusType(),
                                            BulkChargingComplete: int=0,
                                            BulkChargingComplete_isUsed: int=0,
                                            ChargingComplete: int=0):

        struct = OV2GStructs.dinDC_EVPowerDeliveryParameterType()
        struct.DC_EVStatus = DC_EVStatus
        struct.BulkChargingComplete = BulkChargingComplete
        struct.BulkChargingComplete_isUsed = BulkChargingComplete_isUsed
        struct.ChargingComplete = ChargingComplete
        return struct


    def dinEVSEChargeParameterType(noContent: int=0):
        struct = OV2GStructs.dinEVSEChargeParameterType()
        struct.noContent = noContent
        return struct


    def dinCableCheckReqType(DC_EVStatus: OV2GStructs.dinDC_EVStatusType=dinDC_EVStatusType()):
        struct = OV2GStructs.dinCableCheckReqType()
        struct.DC_EVStatus = DC_EVStatus
        return struct

    
    def dinDC_EVChargeParameterType(DC_EVStatus: OV2GStructs.dinDC_EVStatusType=dinDC_EVStatusType(),
                                    EVMaximumCurrentLimit: OV2GStructs.dinPhysicalValueType=dinPhysicalValueType(),
                                    EVMaximumPowerLimit: OV2GStructs.dinPhysicalValueType=dinPhysicalValueType(),
                                    EVMaximumPowerLimit_isUsed: int=0,
                                    EVMaximumVoltageLimit: OV2GStructs.dinPhysicalValueType=dinPhysicalValueType(),
                                    EVEnergyCapacity: OV2GStructs.dinPhysicalValueType=dinPhysicalValueType(),
                                    EVEnergyCapacity_isUsed: int=0,
                                    EVEnergyRequest: OV2GStructs.dinPhysicalValueType=dinPhysicalValueType(),
                                    EVEnergyRequest_isUsed: int=0,
                                    FullSOC: int=0,
                                    FullSOC_isUsed: int=0,
                                    BulkSOC: int=0,
                                    BulkSOC_isUsed: int=0):

        struct = OV2GStructs.dinDC_EVChargeParameterType()
        struct.DC_EVStatus = DC_EVStatus
        struct.EVMaximumCurrentLimit = EVMaximumCurrentLimit
        struct.EVMaximumPowerLimit = EVMaximumPowerLimit
        struct.EVMaximumPowerLimit_isUsed = EVMaximumPowerLimit_isUsed
        struct.EVMaximumVoltageLimit = EVMaximumVoltageLimit
        struct.EVEnergyCapacity = EVEnergyCapacity
        struct.EVEnergyCapacity_isUsed = EVEnergyCapacity_isUsed
        struct.EVEnergyRequest = EVEnergyRequest
        struct.EVEnergyRequest_isUsed = EVEnergyRequest_isUsed
        struct.FullSOC = FullSOC
        struct.FullSOC_isUsed = FullSOC_isUsed
        struct.BulkSOC = BulkSOC
        struct.BulkSOC_isUsed = BulkSOC_isUsed
        return struct

    
    def dinRelativeTimeIntervalType(start: int=0, 
                                    duration: int=0, 
                                    duration_isUsed: int=0):
        struct = OV2GStructs.dinRelativeTimeIntervalType()
        struct.start = start
        struct.duration = duration
        struct.duration_isUsed = duration_isUsed
        return struct


    def dinIntervalType(noContent: int=0):
        struct = OV2GStructs.dinIntervalType()
        struct.noContent = noContent
        return struct


    def dinPMaxScheduleEntryType(   TimeInterval: OV2GStructs.dinIntervalType=dinIntervalType(),
                                    TimeInterval_isUsed: int=0,
                                    RelativeTimeInterval: OV2GStructs.dinRelativeTimeIntervalType=dinRelativeTimeIntervalType(),
                                    RelativeTimeInterval_isUsed: int=0,
                                    PMax: int=0):
        struct = OV2GStructs.dinPMaxScheduleEntryType()
        struct.TimeInterval = TimeInterval
        struct.TimeInterval_isUsed = TimeInterval_isUsed
        struct.RelativeTimeInterval = RelativeTimeInterval
        struct.RelativeTimeInterval_isUsed = RelativeTimeInterval_isUsed
        struct.PMax = PMax
        return struct


    def dinPMaxScheduleType(    PMaxScheduleID: int=0,
                                PMaxScheduleEntry: list[OV2GStructs.dinPMaxScheduleEntryType]=[]):
        struct = OV2GStructs.dinPMaxScheduleType()
        struct.PMaxScheduleID = PMaxScheduleID
        for i in range(len(PMaxScheduleEntry)):
            struct.PMaxScheduleEntry.array[i] = PMaxScheduleEntry[i]
        struct.PMaxScheduleEntry.arrayLen = len(PMaxScheduleEntry)
        return struct


    def dinCostType(costKind: int=0,
                    amount: int=0,
                    amountMultiplier: int=0,
                    amountMultiplier_isUsed: int=0):
        struct = OV2GStructs.dinCostType()
        struct.costKind = costKind
        struct.amount = amount
        struct.amountMultiplier = amountMultiplier
        struct.amountMultiplier_isUsed = amountMultiplier_isUsed
        return struct


    def dinConsumptionCostType( startValue: int=0,
                                Cost: list[OV2GStructs.dinCostType]=[]):
        struct = OV2GStructs.dinConsumptionCostType()
        struct.startValue = startValue
        for i in range(len(Cost)):
            struct.Cost.array[i] = Cost[i]
        struct.Cost.arrayLen = len(Cost)
        return struct 


    def dinSalesTariffEntryType(TimeInterval: OV2GStructs.dinIntervalType=dinIntervalType(),
                                TimeInteraval_isUsed: int=0,
                                RelativeTimeInterval: OV2GStructs.dinRelativeTimeIntervalType=dinRelativeTimeIntervalType(),
                                RelativeTimeInteraval_isUsed: int=0,
                                EPriceLevel: int=0,
                                ConsumptionCost: list[OV2GStructs.dinConsumptionCostType]=[]):
        struct = OV2GStructs.dinSalesTariffEntryType()
        struct.TimeInterval = TimeInterval
        struct.TimeInteraval_isUsed = TimeInteraval_isUsed
        struct.RelativeTimeInterval = RelativeTimeInterval
        struct.RelativeTimeInteraval_isUsed = RelativeTimeInteraval_isUsed
        struct.EPriceLevel = EPriceLevel
        for i in range(len(ConsumptionCost)):
            struct.ConsumptionCost.array[i] = ConsumptionCost[i]
        struct.ConsumptionCost.arrayLen = len(ConsumptionCost)
        return struct


    def dinSalesTariffType( Id: str="",
                            SalesTariffID: int=0,
                            SalesTariffDescription: str="",
                            SalesTariffDescription_isUsed: int=0,
                            NumEPriceLevels: int=0,
                            SalesTariffEntry: list[OV2GStructs.dinSalesTariffEntryType]=[]):
        converted_id = OpenV2GUtils.convert_to_array_type_characters(val=Id, size=dinSalesTariffType_Id_CHARACTERS_SIZE)
        converted_sales_tariff_description = OpenV2GUtils.convert_to_array_type_characters(val=SalesTariffDescription, size=dinSalesTariffType_SalesTariffDescription_CHARACTERS_SIZE)
        struct = OV2GStructs.dinSalesTariffType()
        struct.Id.characters = converted_id
        struct.Id.charactersLen = len(Id)
        struct.SalesTariffID = SalesTariffID
        struct.SalesTariffDescription.characters = converted_sales_tariff_description
        struct.SalesTariffDescription.charactersLen = len(SalesTariffDescription)
        struct.SalesTariffDescription_isUsed = SalesTariffDescription_isUsed
        struct.NumEPriceLevels = NumEPriceLevels
        for i in range(len(SalesTariffEntry)):
            struct.SalesTariffEntry.array[i] = SalesTariffEntry[i]
        struct.SalesTariffEntry.arrayLen = len(SalesTariffEntry)
        return struct

    
    def dinSAScheduleTupleType( SAScheduleTupleID: int=0,
                                PMaxSchedule: OV2GStructs.dinPMaxScheduleType=dinPMaxScheduleType(),
                                SalesTariff: OV2GStructs.dinSalesTariffType=dinSalesTariffType(),
                                SalesTariff_isUsed: int=0):
        struct = OV2GStructs.dinSAScheduleTupleType()
        struct.SAScheduleTupleID = SAScheduleTupleID
        struct.PMaxSchedule = PMaxSchedule
        struct.SalesTariff = SalesTariff
        struct.SalesTariff_isUsed = SalesTariff_isUsed
        return struct
    

    def dinSAScheduleListType(SAScheduleTuple: list[OV2GStructs.dinSAScheduleTupleType]=[]):
        struct = OV2GStructs.dinSAScheduleListType()
        for i in range(len(SAScheduleTuple)):
            struct.SAScheduleTuple.array[i] = SAScheduleTuple[i]
        struct.SAScheduleTuple.arrayLen = len(SAScheduleTuple)
        return struct        


    def dinServicePaymentSelectionReqType(  SelectedPaymentOption: int=0,
                                            SelectedServiceList: OV2GStructs.dinSelectedServiceListType=dinSelectedServiceListType()):
        struct = OV2GStructs.dinServicePaymentSelectionReqType()
        struct.SelectedPaymentOption = SelectedPaymentOption
        struct.SelectedServiceList = SelectedServiceList
        return struct 


    def dinEVStatusType(noContent: int=0):
        struct = OV2GStructs.dinEVStatusType()
        struct.noContent = noContent
        return struct


    def dinPreChargeResType(ResponseCode: int=0,
                            DC_EVSEStatus: OV2GStructs.dinDC_EVSEStatusType=dinDC_EVSEStatusType(),
                            EVSEPresentVoltage: OV2GStructs.dinPhysicalValueType=dinPhysicalValueType()):

        struct = OV2GStructs.dinPreChargeResType()
        struct.ResponseCode = ResponseCode
        struct.DC_EVSEStatus = DC_EVSEStatus
        struct.EVSEPresentVoltage = EVSEPresentVoltage
        return struct

    
    def dinDC_EVSEChargeParameterType(  DC_EVSEStatus: OV2GStructs.dinDC_EVSEStatusType=dinDC_EVSEStatusType(),
                                        EVSEMaximumCurrentLimit: OV2GStructs.dinPhysicalValueType=dinPhysicalValueType(),
                                        EVSEMaximumPowerLimit: OV2GStructs.dinPhysicalValueType=dinPhysicalValueType(),
                                        EVSEMaximumPowerLimit_isUsed: int=0,
                                        EVSEMaximumVoltageLimit: OV2GStructs.dinPhysicalValueType=dinPhysicalValueType(),
                                        EVSEMinimumCurrentLimit: OV2GStructs.dinPhysicalValueType=dinPhysicalValueType(),
                                        EVSEMinimumVoltageLimit: OV2GStructs.dinPhysicalValueType=dinPhysicalValueType(),
                                        EVSECurrentRegulationTolerance: OV2GStructs.dinPhysicalValueType=dinPhysicalValueType(),
                                        EVSECurrentRegulationTolerance_isUsed: int=0,
                                        EVSEPeakCurrentRipple: OV2GStructs.dinPhysicalValueType=dinPhysicalValueType(),
                                        EVSEEnergyToBeDelivered: OV2GStructs.dinPhysicalValueType=dinPhysicalValueType(),
                                        EVSEEnergyToBeDelivered_isUsed: int=0):

        struct = OV2GStructs.dinDC_EVSEChargeParameterType()
        struct.DC_EVSEStatus = DC_EVSEStatus
        struct.EVSEMaximumCurrentLimit = EVSEMaximumCurrentLimit
        struct.EVSEMaximumPowerLimit = EVSEMaximumPowerLimit
        struct.EVSEMaximumPowerLimit_isUsed = EVSEMaximumPowerLimit_isUsed
        struct.EVSEMaximumVoltageLimit = EVSEMaximumVoltageLimit
        struct.EVSEMinimumCurrentLimit = EVSEMinimumCurrentLimit
        struct.EVSEMinimumVoltageLimit = EVSEMinimumVoltageLimit
        struct.EVSECurrentRegulationTolerance = EVSECurrentRegulationTolerance
        struct.EVSECurrentRegulationTolerance_isUsed = EVSECurrentRegulationTolerance_isUsed
        struct.EVSEPeakCurrentRipple = EVSEPeakCurrentRipple
        struct.EVSEEnergyToBeDelivered = EVSEEnergyToBeDelivered
        struct.EVSEEnergyToBeDelivered_isUsed = EVSEEnergyToBeDelivered_isUsed
        return struct


    def dinPaymentDetailsResType(   ResponseCode: int=0,
                                    GenChallenge: str="",
                                    DateTimeNow: int=0):
        converted_gen_challenge = OpenV2GUtils.convert_to_array_type_characters(val=GenChallenge, size=dinPaymentDetailsResType_GenChallenge_CHARACTERS_SIZE)
        struct = OV2GStructs.dinPaymentDetailsResType()
        struct.ResponseCode = ResponseCode
        struct.GenChallenge.characters = converted_gen_challenge
        struct.GenChallenge.charactersLen = len(GenChallenge)
        struct.DateTimeNow = DateTimeNow
        return struct 


    def dinDSAKeyValueType( P: int=0,
                            P_isUsed: int=0,
                            Q: int=0,
                            Q_isUsed: int=0,
                            G: int=0,
                            G_isUsed: int=0,
                            Y: int=0,
                            J: int=0,
                            J_isUsed: int=0,
                            Seed: int=0,
                            Seed_isUsed: int=0,
                            PgenCounter: int=0,
                            PgenCounter_isUsed: int=0):

        converted_p = OpenV2GUtils.convert_to_array_type_bytes(val=P, size=dinDSAKeyValueType_P_BYTES_SIZE)
        converted_q = OpenV2GUtils.convert_to_array_type_bytes(val=Q, size=dinDSAKeyValueType_Q_BYTES_SIZE)
        converted_g = OpenV2GUtils.convert_to_array_type_bytes(val=G, size=dinDSAKeyValueType_G_BYTES_SIZE)
        converted_y = OpenV2GUtils.convert_to_array_type_bytes(val=Y, size=dinDSAKeyValueType_Y_BYTES_SIZE)
        converted_j = OpenV2GUtils.convert_to_array_type_bytes(val=J, size=dinDSAKeyValueType_J_BYTES_SIZE)
        converted_seed = OpenV2GUtils.convert_to_array_type_bytes(val=Seed, size=dinDSAKeyValueType_Seed_BYTES_SIZE)
        converted_pgen_counter = OpenV2GUtils.convert_to_array_type_bytes(val=PgenCounter, size=dinDSAKeyValueType_PgenCounter_BYTES_SIZE)

        struct = OV2GStructs.dinDSAKeyValueType()
        struct.P.bytes = converted_p
        struct.P.bytesLen = dinDSAKeyValueType_P_BYTES_SIZE
        struct.P_isUsed = P_isUsed

        struct.Q.bytes = converted_q
        struct.Q.bytesLen = dinDSAKeyValueType_Q_BYTES_SIZE
        struct.Q_isUsed = Q_isUsed

        struct.G.bytes = converted_g
        struct.G.bytesLen = dinDSAKeyValueType_G_BYTES_SIZE
        struct.G_isUsed = G_isUsed

        struct.Y.bytes = converted_y
        struct.Y.bytesLen = dinDSAKeyValueType_Y_BYTES_SIZE

        struct.J.bytes = converted_j
        struct.J.bytesLen = dinDSAKeyValueType_J_BYTES_SIZE
        struct.J_isUsed = J_isUsed

        struct.Seed.bytes = converted_seed
        struct.Seed.bytesLen = dinDSAKeyValueType_Seed_BYTES_SIZE
        struct.Seed_isUsed = Seed_isUsed

        struct.PgenCounter.bytes = converted_pgen_counter
        struct.PgenCounter.bytesLen = dinDSAKeyValueType_PgenCounter_BYTES_SIZE
        struct.PgenCounter_isUsed = PgenCounter_isUsed

        return struct


    def dinSASchedulesType(noContent: int=0):
        struct = OV2GStructs.dinSASchedulesType()
        struct.noContent = noContent
        return struct 

    
    def dinEVChargeParameterType(noContent: int=0):
        struct = OV2GStructs.dinEVChargeParameterType()
        struct.noContent = noContent
        return struct 


    def dinBodyBaseType(noContent: int=0):
        struct = OV2GStructs.dinBodyBaseType()
        struct.noContent = noContent
        return struct 


    def dinSubCertificatesType(Certificate: list[str]=[]):
        struct = OV2GStructs.dinSubCertificatesType()
        for i in range(len(Certificate)):
            converted_certificate = OpenV2GUtils.convert_to_array_type_bytes_str(val=Certificate[i], size=dinSubCertificatesType_Certificate_BYTES_SIZE)
            struct.Certificate.array[i].bytes = converted_certificate
            struct.Certificate.array[i].bytesLen = len(Certificate[i])
        struct.Certificate.arrayLen = len(Certificate)
        return struct



    def dinCertificateChainType(Certificate: str="",
                                SubCertificates: OV2GStructs.dinSubCertificatesType=dinSubCertificatesType(),
                                SubCertificates_isUsed: int=0):

        converted_certificate = OpenV2GUtils.convert_to_array_type_bytes_str(val=Certificate, size=dinCertificateChainType_Certificate_BYTES_SIZE)
        struct = OV2GStructs.dinCertificateChainType()
        struct.Certificate.bytes = converted_certificate
        struct.Certificate.bytesLen = len(Certificate)
        struct.SubCertificates = SubCertificates
        struct.SubCertificates_isUsed = SubCertificates_isUsed
        return struct

    def dinCertificateUpdateResType(Id: str="",
                                    ResponseCode: int=0,
                                    ContractSignatureCertChain: OV2GStructs.dinCertificateChainType=dinCertificateChainType(),
                                    ContractSignatureEncryptedPrivateKey: str="",
                                    DHParams: str="",
                                    ContractID: str="",
                                    RetryCounter: int=0):
        converted_id = OpenV2GUtils.convert_to_array_type_characters(val=Id, size=dinCertificateUpdateResType_Id_CHARACTERS_SIZE)
        converted_contract_signature_encrypted_private_key = OpenV2GUtils.convert_to_array_type_bytes_str(val=ContractSignatureEncryptedPrivateKey, size=dinCertificateUpdateResType_ContractSignatureEncryptedPrivateKey_BYTES_SIZE)
        converted_dh_params = OpenV2GUtils.convert_to_array_type_bytes_str(val=DHParams, size=dinCertificateUpdateResType_DHParams_BYTES_SIZE)
        converted_contract_id = OpenV2GUtils.convert_to_array_type_characters(val=ContractID, size=dinCertificateUpdateResType_ContractID_CHARACTERS_SIZE)
        struct = OV2GStructs.dinCertificateUpdateResType()
        struct.Id.characters = converted_id
        struct.Id.charactersLen = len(Id)
        struct.ResponseCode = ResponseCode
        struct.ContractSignatureCertChain = ContractSignatureCertChain
        struct.ContractSignatureEncryptedPrivateKey.bytes = converted_contract_signature_encrypted_private_key
        struct.ContractSignatureEncryptedPrivateKey.bytesLen = len(ContractSignatureEncryptedPrivateKey)
        struct.DHParams.bytes = converted_dh_params
        struct.DHParams.bytesLen = len(DHParams)
        struct.ContractID.characters = converted_contract_id
        struct.ContractID.charactersLen = len(ContractID)
        struct.RetryCounter = RetryCounter
        return struct
    

    def dinNotificationType(FaultCode: int=0,
                            FaultMsg: str="",
                            FaultMsg_isUsed: int=0):
        converted_fault_msg = OpenV2GUtils.convert_to_array_type_characters(val=FaultMsg, size=dinNotificationType_FaultMsg_CHARACTERS_SIZE)
        struct = OV2GStructs.dinNotificationType()
        struct.FaultCode = FaultCode
        struct.FaultMsg.characters = converted_fault_msg
        struct.FaultMsg.charactersLen = len(FaultMsg)
        struct.FaultMsg_isUsed = FaultMsg_isUsed
        return struct


    def dinSignatureMethodType( Algorithm: str="",
                                HMACOutputLength: int=0,
                                HMACOutputLength_isUsed: int=0,
                                ANY: str="",
                                ANY_isUsed: int=0):
        converted_algorithm = OpenV2GUtils.convert_to_array_type_characters(val=Algorithm, size=dinSignatureMethodType_Algorithm_CHARACTERS_SIZE)    
        converted_any = OpenV2GUtils.convert_to_array_type_characters(val=ANY, size=dinSignatureMethodType_ANY_CHARACTERS_SIZE)
        struct = OV2GStructs.dinSignatureMethodType()
        struct.Algorithm.characters = converted_algorithm
        struct.Algorithm.charactersLen = len(Algorithm)
        struct.HMACOutputLength = HMACOutputLength
        struct.HMACOutputLength_isUsed = HMACOutputLength_isUsed
        struct.ANY.characters = converted_any
        struct.ANY.charactersLen = len(ANY)
        struct.ANY_isUsed = ANY_isUsed
        return struct

    def dinTransformsType(Transform: list[OV2GStructs.dinTransformType]=[]):
        struct = OV2GStructs.dinTransformsType()
        for i in range(len(Transform)):
            struct.Transform.array[i] = Transform[i]
        struct.Transform.arrayLen = len(Transform)
        return struct

    def dinDigestMethodType(Algorithm: str="",
                            ANY: str="",
                            ANY_isUsed: int=0):

        converted_algorithm = OpenV2GUtils.convert_to_array_type_characters(val=Algorithm, size=dinDigestMethodType_Algorithm_CHARACTERS_SIZE)
        converted_any = OpenV2GUtils.convert_to_array_type_characters(val=ANY, size=dinDigestMethodType_ANY_CHARACTERS_SIZE)
        struct = OV2GStructs.dinDigestMethodType()
        struct.Algorithm.characters = converted_algorithm
        struct.Algorithm.charactersLen = len(Algorithm)
        struct.ANY.characters = converted_any
        struct.ANY.charactersLen = len(ANY)
        struct.ANY_isUsed = ANY_isUsed
        return struct

    def dinReferenceType(   Id: str="",
                            Id_isUsed: int=0,
                            URI: str="",
                            URI_isUsed: int=0,
                            Type: str="",
                            Type_isUsed: int=0,
                            Transforms: OV2GStructs.dinTransformsType=dinTransformsType(),
                            Transforms_isUsed: int=0,
                            DigestMethod: OV2GStructs.dinDigestMethodType=dinDigestMethodType(),
                            DigestValue: str=""):

        converted_id = OpenV2GUtils.convert_to_array_type_characters(val=Id, size=dinReferenceType_Id_CHARACTERS_SIZE)
        converted_uri = OpenV2GUtils.convert_to_array_type_characters(val=URI, size=dinReferenceType_URI_CHARACTERS_SIZE)
        converted_type = OpenV2GUtils.convert_to_array_type_characters(val=Type, size=dinReferenceType_Type_CHARACTERS_SIZE)
        converted_digest_value = OpenV2GUtils.convert_to_array_type_bytes_str(val=DigestValue, size=dinReferenceType_DigestValue_BYTES_SIZE)
        struct = OV2GStructs.dinReferenceType()
        struct.Id.characters = converted_id
        struct.Id.charactersLen = len(Id)
        struct.Id_isUsed = Id_isUsed
        struct.URI.characters = converted_uri
        struct.URI.charactersLen = len(URI)
        struct.URI_isUsed = URI_isUsed
        struct.Type.characters = converted_type
        struct.Type.charactersLen = len(Type)
        struct.Type_isUsed = Type_isUsed
        struct.Transforms = Transforms
        struct.Transforms_isUsed = Transforms_isUsed
        struct.DigestMethod = DigestMethod
        struct.DigestValue.bytes = converted_digest_value
        struct.DigestValue.bytesLen = len(DigestValue)
        return struct


    def dinSignedInfoType(  Id: str="",
                            Id_isUsed: int=0,
                            CanonicalizationMethod: OV2GStructs.dinCanonicalizationMethodType=dinCanonicalizationMethodType(),
                            SignatureMethod: OV2GStructs.dinSignatureMethodType=dinSignatureMethodType(),
                            Reference: list[OV2GStructs.dinReferenceType]=[]):
        converted_id = OpenV2GUtils.convert_to_array_type_characters(val=Id, size=dinSignedInfoType_Id_CHARACTERS_SIZE)
        struct = OV2GStructs.dinSignedInfoType()
        struct.Id.characters = converted_id
        struct.Id.charactersLen = len(Id)
        struct.Id_isUsed = Id_isUsed
        struct.CanonicalizationMethod = CanonicalizationMethod
        struct.SignatureMethod = SignatureMethod
        for i in range(len(Reference)):
            struct.Reference.array[i] = Reference[i]
        struct.Reference.arrayLen = len(Reference)
        return struct


    def dinSignatureValueType(  Id: str="",
                                Id_isUsed: int=0,
                                CONTENT: str=""):
        converted_id = OpenV2GUtils.convert_to_array_type_characters(val=Id, size=dinSignatureValueType_Id_CHARACTERS_SIZE)
        converted_content = OpenV2GUtils.convert_to_array_type_bytes_str(val=CONTENT, size=dinSignatureValueType_CONTENT_BYTES_SIZE)
        struct = OV2GStructs.dinSignatureValueType()
        struct.Id.characters = converted_id
        struct.Id.charactersLen = len(Id)
        struct.Id_isUsed = Id_isUsed
        struct.CONTENT.bytes = converted_content
        struct.CONTENT.bytesLen = len(CONTENT)
        return struct

    def dinRSAKeyValueType( Modulus: int=0,
                            Exponent: int=0):
        converted_modulus = OpenV2GUtils.convert_to_array_type_bytes(val=Modulus, size=dinRSAKeyValueType_Modulus_BYTES_SIZE)
        converted_exponent = OpenV2GUtils.convert_to_array_type_bytes(val=Exponent, size=dinRSAKeyValueType_Exponent_BYTES_SIZE)
        struct = OV2GStructs.dinRSAKeyValueType()
        struct.Modulus.bytes = converted_modulus
        struct.Modulus.bytesLen = dinRSAKeyValueType_Modulus_BYTES_SIZE
        struct.Exponent.bytes = converted_exponent
        struct.Exponent.bytesLen = dinRSAKeyValueType_Exponent_BYTES_SIZE
        return struct
        

    def dinKeyValueType(DSAKeyValue: OV2GStructs.dinDSAKeyValueType=dinDSAKeyValueType(),
                        DSAKeyValue_isUsed: int=0,
                        RSAKeyValue: OV2GStructs.dinRSAKeyValueType=dinRSAKeyValueType(),
                        RSAKeyValue_isUsed: int=0,
                        ANY: str="",
                        ANY_isUsed: int=0):
        converted_any = OpenV2GUtils.convert_to_array_type_characters(val=ANY, size=dinKeyValueType_ANY_CHARACTERS_SIZE)
        struct = OV2GStructs.dinKeyValueType()
        struct.DSAKeyValue = DSAKeyValue
        struct.DSAKeyValue_isUsed = DSAKeyValue_isUsed
        struct.RSAKeyValue = RSAKeyValue
        struct.RSAKeyValue_isUsed = RSAKeyValue_isUsed
        struct.ANY.characters = converted_any
        struct.ANY.charactersLen = len(ANY)
        struct.ANY_isUsed = ANY_isUsed
        return struct

    
    def dinRetrievalMethodType( URI: str="",
                                URI_isUsed: int=0,
                                Type: str="",
                                Type_isUsed: int=0,
                                Transforms: OV2GStructs.dinTransformsType=dinTransformsType(),
                                Transforms_isUsed: int=0):
        converted_uri = OpenV2GUtils.convert_to_array_type_characters(val=URI, size=dinRetrievalMethodType_URI_CHARACTERS_SIZE)
        converted_type = OpenV2GUtils.convert_to_array_type_characters(val=Type, size=dinRetrievalMethodType_Type_CHARACTERS_SIZE)
        struct = OV2GStructs.dinRetrievalMethodType()
        struct.URI.characters = converted_uri
        struct.URI.charactersLen = len(URI)
        struct.URI_isUsed = URI_isUsed
        struct.Type.characters = converted_type
        struct.Type.charactersLen = len(Type)
        struct.Type_isUsed = Type_isUsed
        struct.Transforms = Transforms
        struct.Transforms_isUsed = Transforms_isUsed
        return struct
    

    def dinPGPDataType( PGPKeyID: str="",
                        PGPKeyID_isUsed: int=0,
                        PGPKeyPacket: str="",
                        PGPKeyPacket_isUsed: int=0,
                        ANY: str="",
                        ANY_isUsed: int=0):
        converted_pgp_key_id = OpenV2GUtils.convert_to_array_type_bytes_str(val=PGPKeyID, size=dinPGPDataType_PGPKeyID_BYTES_SIZE)
        converted_pgp_key_packet = OpenV2GUtils.convert_to_array_type_bytes_str(val=PGPKeyPacket, size=dinPGPDataType_PGPKeyPacket_BYTES_SIZE)
        converted_any = OpenV2GUtils.convert_to_array_type_characters(val=ANY, size=dinPGPDataType_ANY_CHARACTERS_SIZE)
        struct = OV2GStructs.dinPGPDataType()
        struct.PGPKeyID.bytes = converted_pgp_key_id
        struct.PGPKeyID.bytesLen = dinPGPDataType_PGPKeyID_BYTES_SIZE
        struct.PGPKeyID_isUsed = PGPKeyID_isUsed
        struct.PGPKeyPacket.bytes = converted_pgp_key_packet
        struct.PGPKeyPacket.bytesLen = dinPGPDataType_PGPKeyPacket_BYTES_SIZE
        struct.PGPKeyPacket_isUsed = PGPKeyPacket_isUsed
        struct.ANY.characters = converted_any
        struct.ANY.charactersLen = len(ANY)
        struct.ANY_isUsed = ANY_isUsed
        return struct


    def dinKeyInfoType( Id: str="",
                        Id_isUsed: int=0,
                        KeyName: list[str]=[""], 
                        KeyValue: list[OV2GStructs.dinKeyValueType]=[dinKeyValueType()],
                        RetrievalMethod: list[OV2GStructs.dinRetrievalMethodType]=[dinRetrievalMethodType()],
                        X509Data: list[OV2GStructs.dinX509DataType]=[dinX509DataType()],
                        PGPData: list[OV2GStructs.dinPGPDataType]=[dinPGPDataType()],
                        SPKIData: list[OV2GStructs.dinSPKIDataType]=[dinSPKIDataType()],
                        MgmtData: list[str]=[""],
                        ANY: str="",
                        ANY_isUsed: int=0):
        
        converted_id = OpenV2GUtils.convert_to_array_type_characters(val=Id, size=dinKeyInfoType_Id_CHARACTERS_SIZE)
        converted_key_name = OpenV2GUtils.convert_to_array_type_characters(val=KeyName[0], size=dinKeyInfoType_KeyName_CHARACTERS_SIZE)
        converted_mgmt_data = OpenV2GUtils.convert_to_array_type_characters(val=MgmtData[0], size=dinKeyInfoType_MgmtData_CHARACTERS_SIZE)
        converted_any = OpenV2GUtils.convert_to_array_type_characters(val=ANY, size=dinKeyInfoType_ANY_CHARACTERS_SIZE)
        
        struct = OV2GStructs.dinKeyInfoType()
        struct.Id.characters = converted_id
        struct.Id.charactersLen = len(Id)
        struct.Id_isUsed = Id_isUsed

        struct.KeyName.array[0].characters = converted_key_name
        struct.KeyName.array[0].charactersLen = len(Id)
        struct.KeyName.arrayLen = dinKeyInfoType_KeyName_ARRAY_SIZE

        struct.KeyValue.array[0] = KeyValue[0]
        struct.KeyValue.arrayLen = dinKeyInfoType_KeyValue_ARRAY_SIZE

        struct.RetrievalMethod.array[0] = RetrievalMethod[0]
        struct.RetrievalMethod.arrayLen = dinKeyInfoType_RetrievalMethod_ARRAY_SIZE

        struct.X509Data.array[0] = X509Data[0]
        struct.X509Data.arrayLen = dinKeyInfoType_X509Data_ARRAY_SIZE

        struct.PGPData.array[0] = PGPData[0]
        struct.PGPData.arrayLen = dinKeyInfoType_PGPData_ARRAY_SIZE

        struct.SPKIData.array[0] = SPKIData[0]
        struct.SPKIData.arrayLen = dinKeyInfoType_SPKIData_ARRAY_SIZE

        struct.MgmtData.array[0].characters = converted_mgmt_data
        struct.MgmtData.array[0].charactersLen = len(MgmtData)
        struct.MgmtData.arrayLen = dinKeyInfoType_MgmtData_ARRAY_SIZE

        struct.ANY.characters = converted_any
        struct.ANY.charactersLen = len(ANY)
        struct.ANY_isUsed = ANY_isUsed

        return struct

    def dinObjectType(  Id: str="",
                        Id_isUsed: int=0,
                        MimeType: str="",
                        MimeType_isUsed: int=0,
                        Encoding: str="",
                        Encoding_isUsed: int=0,
                        ANY: str="",
                        ANY_isUsed: int=0):
        converted_id = OpenV2GUtils.convert_to_array_type_characters(val=Id, size=dinObjectType_Id_CHARACTERS_SIZE)
        converted_mime_type = OpenV2GUtils.convert_to_array_type_characters(val=MimeType, size=dinObjectType_MimeType_CHARACTERS_SIZE)
        converted_encoding = OpenV2GUtils.convert_to_array_type_characters(val=Encoding, size=dinObjectType_Encoding_CHARACTERS_SIZE)
        converted_any = OpenV2GUtils.convert_to_array_type_characters(val=ANY, size=dinObjectType_ANY_CHARACTERS_SIZE)
        struct = OV2GStructs.dinObjectType()
        struct.Id.characters = converted_id
        struct.Id.charactersLen = len(Id)
        struct.Id_isUsed = Id_isUsed
        struct.MimeType.characters = converted_mime_type
        struct.MimeType.charactersLen = len(MimeType)
        struct.MimeType_isUsed = MimeType_isUsed
        struct.Encoding.characters = converted_encoding
        struct.Encoding.charactersLen = len(Encoding)
        struct.Encoding_isUsed = Encoding_isUsed
        struct.ANY.characters = converted_any
        struct.ANY.charactersLen = len(ANY)
        struct.ANY_isUsed = ANY_isUsed
        return struct


    def dinSignatureType(   Id: str="", 
                            Id_isUsed: int=0,
                            SignedInfo: OV2GStructs.dinSignedInfoType=dinSignedInfoType(),
                            SignatureValue: OV2GStructs.dinSignatureValueType=dinSignatureValueType(),
                            KeyInfo: OV2GStructs.dinKeyInfoType=dinKeyInfoType(),
                            KeyInfo_isUsed: int=0,
                            Object: list[OV2GStructs.dinObjectType]=[dinObjectType()]):
        converted_id = OpenV2GUtils.convert_to_array_type_characters(val=Id, size=dinSignatureType_Id_CHARACTERS_SIZE)
        struct = OV2GStructs.dinSignatureType()
        struct.Id.characters = converted_id
        struct.Id.charactersLen = len(Id)
        struct.Id_isUsed = Id_isUsed
        struct.SignedInfo = SignedInfo
        struct.SignatureValue = SignatureValue
        struct.KeyInfo = KeyInfo
        struct.KeyInfo_isUsed = KeyInfo_isUsed
        struct.Object.array[0] = Object[0]
        struct.Object.arrayLen = dinSignatureType_Object_ARRAY_SIZE
        return struct

    def dinMessageHeaderType(   SessionID: int=0, 
                                Notification: OV2GStructs.dinNotificationType=dinNotificationType(),
                                Notification_isUsed: int=0,
                                Signature: OV2GStructs.dinSignatureType=dinSignatureType(),
                                Signature_isUsed: int=0):

        converted_session_id = OpenV2GUtils.convert_to_array_type_bytes(val=SessionID, size=dinMessageHeaderType_SessionID_BYTES_SIZE)
        struct = OV2GStructs.dinMessageHeaderType()
        struct.SessionID.bytes = converted_session_id
        struct.SessionID.bytesLen = dinMessageHeaderType_SessionID_BYTES_SIZE
        struct.Notification = Notification
        struct.Notification_isUsed = Notification_isUsed
        struct.Signature = Signature
        struct.Signature_isUsed = Signature_isUsed
        return struct


    def dinAC_EVSEChargeParameterType(  AC_EVSEStatus: OV2GStructs.dinAC_EVSEStatusType=dinAC_EVSEStatusType(),
                                        EVSEMaxVoltage: OV2GStructs.dinPhysicalValueType=dinPhysicalValueType(),
                                        EVSEMaxCurrent: OV2GStructs.dinPhysicalValueType=dinPhysicalValueType(),
                                        EVSEMinCurrent: OV2GStructs.dinPhysicalValueType=dinPhysicalValueType()):
        struct = OV2GStructs.dinAC_EVSEChargeParameterType()
        struct.AC_EVSEStatus = AC_EVSEStatus
        struct.EVSEMaxVoltage = EVSEMaxVoltage
        struct.EVSEMaxCurrent = EVSEMaxCurrent
        struct.EVSEMinCurrent = EVSEMinCurrent
        return struct
        

    def dinChargeParameterDiscoveryResType( ResponseCode: int=0,
                                            EVSEProcessingType: int=0,
                                            SASchedules: OV2GStructs.dinSASchedulesType=dinSASchedulesType(),
                                            SASchedules_isUsed: int=0,
                                            SAScheduleList: OV2GStructs.dinSAScheduleListType=dinSAScheduleListType(),
                                            SAScheduleList_isUsed: int=0,
                                            EVSEChargeParameter: OV2GStructs.dinEVSEChargeParameterType=dinEVSEChargeParameterType(),
                                            EVSEChargeParameter_isUsed: int=0,
                                            AC_EVSEChargeParameter: OV2GStructs.dinAC_EVSEChargeParameterType=dinAC_EVSEChargeParameterType(),
                                            AC_EVSEChargeParameter_isUsed: int=0,
                                            DC_EVSEChargeParameter: OV2GStructs.dinDC_EVSEChargeParameterType=dinDC_EVSEChargeParameterType(),
                                            DC_EVSEChargeParameter_isUsed: int=0):
        struct = OV2GStructs.dinChargeParameterDiscoveryResType()
        struct.ResponseCode = ResponseCode
        struct.EVSEProcessingType = EVSEProcessingType
        struct.SASchedules = SASchedules
        struct.SASchedules_isUsed = SASchedules_isUsed
        struct.SAScheduleList = SAScheduleList
        struct.SAScheduleList_isUsed = SAScheduleList_isUsed
        struct.EVSEChargeParameter = EVSEChargeParameter
        struct.EVSEChargeParameter_isUsed = EVSEChargeParameter_isUsed
        struct.AC_EVSEChargeParameter = AC_EVSEChargeParameter
        struct.AC_EVSEChargeParameter_isUsed = AC_EVSEChargeParameter_isUsed
        struct.DC_EVSEChargeParameter = DC_EVSEChargeParameter
        struct.DC_EVSEChargeParameter_isUsed = DC_EVSEChargeParameter_isUsed
        return struct


    def dinProfileEntryType(ChargingProfileEntryStart: int=0,
                            ChargingProfileEntryMaxPower: int=0):
        struct = OV2GStructs.dinProfileEntryType()
        struct.ChargingProfileEntryStart = ChargingProfileEntryStart        
        struct.ChargingProfileEntryMaxPower = ChargingProfileEntryMaxPower
        return struct


    def dinChargingProfileType( SAScheduleTupleID: int=0,
                                ProfileEntry: list[OV2GStructs.dinProfileEntryType]=[]):
        struct = OV2GStructs.dinChargingProfileType()
        struct.SAScheduleTupleID = SAScheduleTupleID
        for i in range(len(ProfileEntry)):
            struct.ProfileEntry.array[i] = ProfileEntry[i]
        struct.ProfileEntry.arrayLen = len(ProfileEntry)
        return struct 

    def dinEVPowerDeliveryParameterType(noContent: int=0):
        struct = OV2GStructs.dinEVPowerDeliveryParameterType()
        struct.noContent = noContent
        return struct

    def dinPowerDeliveryReqType(ReadyToChargeState: int=0,
                                ChargingProfile: OV2GStructs.dinChargingProfileType=dinChargingProfileType(),
                                ChargingProfile_isUsed: int=0,
                                EVPowerDeliveryParameter: OV2GStructs.dinEVPowerDeliveryParameterType=dinEVPowerDeliveryParameterType(),
                                EVPowerDeliveryParameter_isUsed: int=0,
                                DC_EVPowerDeliveryParameter: OV2GStructs.dinDC_EVPowerDeliveryParameterType=dinDC_EVPowerDeliveryParameterType(),
                                DC_EVPowerDeliveryParameter_isUsed: int=0):

        struct = OV2GStructs.dinPowerDeliveryReqType()
        struct.ReadyToChargeState = ReadyToChargeState
        struct.ChargingProfile = ChargingProfile
        struct.ChargingProfile_isUsed = ChargingProfile_isUsed
        struct.EVPowerDeliveryParameter = EVPowerDeliveryParameter
        struct.EVPowerDeliveryParameter_isUsed = EVPowerDeliveryParameter_isUsed
        struct.DC_EVPowerDeliveryParameter = DC_EVPowerDeliveryParameter
        struct.DC_EVPowerDeliveryParameter_isUsed = DC_EVPowerDeliveryParameter_isUsed
        return struct


    def dinEntryType(   TimeInterval: OV2GStructs.dinIntervalType=dinIntervalType(),
                        RelativeTimeInterval: OV2GStructs.dinRelativeTimeIntervalType=dinRelativeTimeIntervalType(),
                        TimeInterval_isUsed: int=0,
                        RelativeTimeInterval_isUsed: int=0):
        
        struct = OV2GStructs.dinEntryType()
        struct.TimeInterval = TimeInterval
        struct.RelativeTimeInterval = RelativeTimeInterval
        struct.TimeInterval_isUsed = TimeInterval_isUsed
        struct.RelativeTimeInterval_isUsed = RelativeTimeInterval_isUsed
        return struct
        

    def dinSessionStopType(noContent: int=0):
        struct = OV2GStructs.dinSessionStopType()
        struct.noContent = noContent
        return struct
    

    def dinServiceDetailReqType(ServiceID: int=0):
        struct = OV2GStructs.dinServiceDetailReqType()
        struct.ServiceID = ServiceID
        return struct
        

    def dinChargingStatusReqType(noContent: int=0):
        struct = OV2GStructs.dinChargingStatusReqType()
        struct.noContent = noContent
        return struct


    def dinCertificateInstallationReqType(  Id: str="",
                                            Id_isUsed: int=0,
                                            OEMProvisioningCert: str="",
                                            ListOfRootCertificateIDs: OV2GStructs.dinListOfRootCertificateIDsType=dinListOfRootCertificateIDsType(),
                                            DHParams: str=""):
        
        converted_id = OpenV2GUtils.convert_to_array_type_characters(val=Id, size=dinCertificateInstallationReqType_Id_CHARACTERS_SIZE)
        converted_oemp_profision_cert = OpenV2GUtils.convert_to_array_type_bytes_str(val=OEMProvisioningCert, size=dinCertificateInstallationReqType_OEMProvisioningCert_BYTES_SIZE)
        converted_dh_params = OpenV2GUtils.convert_to_array_type_bytes_str(val=DHParams, size=dinCertificateInstallationReqType_DHParams_BYTES_SIZE)
        struct = OV2GStructs.dinCertificateInstallationReqType()
        struct.Id.characters = converted_id
        struct.Id.charactersLen = len(Id)
        struct.Id_isUsed = Id_isUsed
        struct.OEMProvisioningCert.bytes = converted_oemp_profision_cert
        struct.OEMProvisioningCert.bytesLen = dinCertificateInstallationReqType_OEMProvisioningCert_BYTES_SIZE
        struct.ListOfRootCertificateIDs = ListOfRootCertificateIDs
        struct.DHParams.bytes = converted_dh_params
        struct.DHParams.bytesLen = dinCertificateInstallationReqType_DHParams_BYTES_SIZE
        return struct
        

    def dinPaymentOptionsType(  PaymentOption: list[int]=[]):
        struct = OV2GStructs.dinPaymentOptionsType()
        for i in range(len(PaymentOption)):
            struct.PaymentOption.array[i] = PaymentOption[i]
        struct.PaymentOption.arrayLen = len(PaymentOption)
        return struct 


    def dinServiceTagType(  ServiceID: int=0,
                            ServiceName: str="",
                            ServiceName_isUsed: int=0,
                            ServiceCategory: int=0,
                            ServiceScope: str="",
                            ServiceScope_isUsed: int=0):
        converted_service_name = OpenV2GUtils.convert_to_array_type_characters(val=ServiceName, size=dinServiceTagType_ServiceName_CHARACTERS_SIZE)
        converted_service_scope = OpenV2GUtils.convert_to_array_type_characters(val=ServiceScope, size=dinServiceTagType_ServiceScope_CHARACTERS_SIZE)
        struct = OV2GStructs.dinServiceTagType()
        struct.ServiceID = ServiceID
        struct.ServiceName.characters = converted_service_name
        struct.ServiceName.charactersLen = len(ServiceName)
        struct.ServiceName_isUsed = ServiceName_isUsed
        struct.ServiceCategory= ServiceCategory
        struct.ServiceScope.characters = converted_service_scope
        struct.ServiceScope.charactersLen = len(ServiceScope)
        struct.ServiceScope_isUsed = ServiceScope_isUsed
        return struct 

    def dinServiceChargeType(   ServiceTag: OV2GStructs.dinServiceTagType=dinServiceTagType(),
                                FreeService: int=0,
                                EnergyTransferType: int=0):
        struct = OV2GStructs.dinServiceChargeType()
        struct.ServiceTag = ServiceTag
        struct.FreeService = FreeService
        struct.EnergyTransferType = EnergyTransferType
        return struct 


    def dinServiceType( ServiceTag: OV2GStructs.dinServiceTagType=dinServiceTagType(),
                        FreeService: int=0):
        struct = OV2GStructs.dinServiceType()
        struct.ServiceTag = ServiceTag
        struct.FreeService = FreeService
        return struct
        

    def dinServiceTagListType(Service: list[OV2GStructs.dinServiceType]=[]):
        struct = OV2GStructs.dinServiceTagListType()
        for i in range(len(Service)):
            struct.Service.array[i] = Service[i]
        struct.Service.arrayLen = len(Service)
        return struct


    def dinServiceDiscoveryResType( ResponseCode: int=0,
                                    PaymentOptions: OV2GStructs.dinPaymentOptionsType=dinPaymentOptionsType(),
                                    ChargeService: OV2GStructs.dinServiceChargeType=dinServiceChargeType(),
                                    ServiceList: OV2GStructs.dinServiceTagListType=dinServiceTagListType(),
                                    ServiceList_isUsed: int=0):
        struct = OV2GStructs.dinServiceDiscoveryResType()
        struct.ResponseCode = ResponseCode
        struct.PaymentOptions = PaymentOptions
        struct.ChargeService = ChargeService
        struct.ServiceList = ServiceList
        struct.ServiceList_isUsed = ServiceList_isUsed
        return struct


    def dinCurrentDemandReqType(DC_EVStatus: OV2GStructs.dinDC_EVStatusType=dinDC_EVStatusType(),
                                EVTargetCurrent: OV2GStructs.dinPhysicalValueType=dinPhysicalValueType(),
                                EVMaximumVoltageLimit: OV2GStructs.dinPhysicalValueType=dinPhysicalValueType(),
                                EVMaximumVoltageLimit_isUsed: int=0,
                                EVMaximumCurrentLimit: OV2GStructs.dinPhysicalValueType=dinPhysicalValueType(),
                                EVMaximumCurrentLimit_isUsed:int=0,
                                EVMaximumPowerimit: OV2GStructs.dinPhysicalValueType=dinPhysicalValueType(),
                                EVMaximumPowerLimit_isUsed:int=0,
                                BulkChargingComplete: int=0,
                                BulkChargingComplete_isUsed: int=0,
                                ChargingComplete: int=0,
                                RemainingTimeToFullSoC: OV2GStructs.dinPhysicalValueType=dinPhysicalValueType(),
                                RemainingTimeToFullSoC_isUsed:int=0,
                                RemainingTimeToBulkSoC: OV2GStructs.dinPhysicalValueType=dinPhysicalValueType(),
                                RemainingTimeToBulkSoC_isUsed:int=0,
                                EVTargetVoltage: OV2GStructs.dinPhysicalValueType=dinPhysicalValueType()):

        struct = OV2GStructs.dinCurrentDemandReqType()
        struct.DC_EVStatus = DC_EVStatus
        struct.EVTargetCurrent = EVTargetCurrent
        struct.EVMaximumVoltageLimit = EVMaximumVoltageLimit
        struct.EVMaximumVoltageLimit_isUsed = EVMaximumVoltageLimit_isUsed
        struct.EVMaximumCurrentLimit = EVMaximumCurrentLimit
        struct.EVMaximumCurrentLimit_isUsed = EVMaximumCurrentLimit_isUsed
        struct.EVMaximumPowerimit = EVMaximumPowerimit
        struct.EVMaximumPowerLimit_isUsed = EVMaximumPowerLimit_isUsed
        struct.BulkChargingComplete = BulkChargingComplete
        struct.BulkChargingComplete_isUsed = BulkChargingComplete_isUsed
        struct.ChargingComplete = ChargingComplete
        struct.RemainingTimeToFullSoC = RemainingTimeToFullSoC
        struct.RemainingTimeToFullSoC_isUsed = RemainingTimeToFullSoC_isUsed
        struct.RemainingTimeToBulkSoC = RemainingTimeToBulkSoC
        struct.RemainingTimeToBulkSoC_isUsed = RemainingTimeToBulkSoC_isUsed
        struct.EVTargetVoltage = EVTargetVoltage
        return struct


    def dinPreChargeReqType(DC_EVStatus: OV2GStructs.dinDC_EVStatusType=dinDC_EVStatusType(),
                            EVTargetVoltage: OV2GStructs.dinPhysicalValueType=dinPhysicalValueType(),
                            EVTargetCurrent: OV2GStructs.dinPhysicalValueType=dinPhysicalValueType()):
        struct = OV2GStructs.dinPreChargeReqType()
        struct.DC_EVStatus = DC_EVStatus
        struct.EVTargetVoltage = EVTargetVoltage
        struct.EVTargetCurrent = EVTargetCurrent
        return struct


    # TODO: TEST FROM HERE!
    def dinSessionSetupResType( ResponseCode: int=0,
                                EVSEID: int=0,
                                DateTimeNow: int=0,
                                DateTimeNow_isUsed: int=0):

        converted_evse_id = OpenV2GUtils.convert_to_array_type_bytes(val=EVSEID, size=dinSessionSetupResType_EVSEID_BYTES_SIZE)
        struct = OV2GStructs.dinSessionSetupResType()
        struct.ResponseCode = ResponseCode
        struct.EVSEID.bytes = converted_evse_id
        struct.EVSEID.bytesLen = dinSessionSetupResType_EVSEID_BYTES_SIZE
        struct.DateTimeNow = DateTimeNow
        struct.DateTimeNow_isUsed = DateTimeNow_isUsed
        return struct

    def dinServiceDiscoveryReqType( ServiceScope: str="",
                                    ServiceScope_isUsed: int=0,
                                    ServiceCategory: int=0,
                                    ServiceCategory_isUsed: int=0):
        converted_service_scope = OpenV2GUtils.convert_to_array_type_characters(val=ServiceScope, size=dinServiceDiscoveryReqType_ServiceScope_CHARACTERS_SIZE)
        struct = OV2GStructs.dinServiceDiscoveryReqType()
        struct.ServiceScope.characters = converted_service_scope
        struct.ServiceScope.charactersLen = len(ServiceScope)
        struct.ServiceScope_isUsed = ServiceScope_isUsed
        struct.ServiceCategory = ServiceCategory
        struct.ServiceCategory_isUsed = ServiceCategory_isUsed
        return struct 

    def dinServicePaymentSelectionResType(  ResponseCode: int=0):
        struct = OV2GStructs.dinServicePaymentSelectionResType()
        struct.ResponseCode = ResponseCode
        return struct 

    def dinPaymentDetailsReqType(   ContractID: str="",
                                    ContractSignatureCertChain: OV2GStructs.dinCertificateChainType=dinCertificateChainType()):
        converted_contract_id = OpenV2GUtils.convert_to_array_type_characters(val=ContractID, size=dinPaymentDetailsReqType_ContractID_CHARACTERS_SIZE)
        struct = OV2GStructs.dinPaymentDetailsReqType()
        struct.ContractID.characters = converted_contract_id
        struct.ContractID.charactersLen = len(ContractID)
        struct.ContractSignatureCertChain = ContractSignatureCertChain
        return struct

    def dinChargeParameterDiscoveryReqType( EVRequestedEnergyTransferType: int=0,
                                            EVChargeParameter: OV2GStructs.dinEVChargeParameterType=dinEVChargeParameterType(),
                                            EVChargeParameter_isUsed: int=0,
                                            AC_EVChargeParameter: OV2GStructs.dinAC_EVChargeParameterType=dinAC_EVChargeParameterType(),
                                            AC_EVChargeParameter_isUsed: int=0,
                                            DC_EVChargeParameter: OV2GStructs.dinDC_EVChargeParameterType=dinDC_EVChargeParameterType(),
                                            DC_EVChargeParameter_isUsed: int=0):
        struct = OV2GStructs.dinChargeParameterDiscoveryReqType()
        struct.EVRequestedEnergyTransferType = EVRequestedEnergyTransferType
        struct.EVChargeParameter = EVChargeParameter
        struct.EVChargeParameter_isUsed = EVChargeParameter_isUsed
        struct.AC_EVChargeParameter = AC_EVChargeParameter
        struct.AC_EVChargeParameter_isUsed = AC_EVChargeParameter_isUsed
        struct.DC_EVChargeParameter = DC_EVChargeParameter
        struct.DC_EVChargeParameter_isUsed = DC_EVChargeParameter_isUsed
        return struct 

    def dinMeteringReceiptReqType(  Id: str="",
                                    Id_isUsed: int=0,
                                    SessionID: int=0,
                                    SAScheduleTupleID: int=0,
                                    SAScheduleTupleID_isUsed: int=0,
                                    MeterInfo: OV2GStructs.dinMeterInfoType=dinMeterInfoType()):
        converted_id = OpenV2GUtils.convert_to_array_type_characters(val=Id, size=dinMeteringReceiptReqType_Id_CHARACTERS_SIZE)
        converted_session_id = OpenV2GUtils.convert_to_array_type_bytes(val=SessionID, size=dinMeteringReceiptReqType_SessionID_BYTES_SIZE)
        struct = OV2GStructs.dinMeteringReceiptReqType()
        struct.Id.characters = converted_id
        struct.Id.charactersLen = len(Id)
        struct.Id_isUsed = Id_isUsed
        struct.SessionID.bytes = converted_session_id
        struct.SessionID.bytesLen = dinMeteringReceiptReqType_SessionID_BYTES_SIZE
        struct.SAScheduleTupleID = SAScheduleTupleID
        struct.SAScheduleTupleID_isUsed = SAScheduleTupleID_isUsed
        struct.MeterInfo = MeterInfo
        return struct 

    def dinMeteringReceiptResType(  ResponseCode: int=0,
                                    AC_EVSEStatus: OV2GStructs.dinAC_EVSEStatusType=dinAC_EVSEStatusType()):
        struct = OV2GStructs.dinMeteringReceiptResType()
        struct.ResponseCode = ResponseCode
        struct.AC_EVSEStatus = AC_EVSEStatus
        return struct 

    def dinSessionStopResType(  ResponseCode: int=0):
        struct = OV2GStructs.dinSessionStopResType()
        struct.ResponseCode = ResponseCode
        return struct 

    def dinCertificateUpdateReqType(Id: str="",
                                    Id_isUsed: int=0,
                                    ContractSignatureCertChain: OV2GStructs.dinCertificateChainType=dinCertificateChainType(),
                                    ContractID: str="",
                                    ListOfRootCertificateIDs: OV2GStructs.dinListOfRootCertificateIDsType=dinListOfRootCertificateIDsType(),
                                    DHParams: str=""):
        converted_id = OpenV2GUtils.convert_to_array_type_characters(val=Id, size=dinCertificateUpdateReqType_Id_CHARACTERS_SIZE)
        converted_contract_id = OpenV2GUtils.convert_to_array_type_characters(val=ContractID, size=dinCertificateUpdateReqType_ContractID_CHARACTERS_SIZE)
        converted_dh_params = OpenV2GUtils.convert_to_array_type_bytes_str(val=DHParams, size=dinCertificateUpdateReqType_DHParams_BYTES_SIZE)
        struct = OV2GStructs.dinCertificateUpdateReqType()
        struct.Id.characters = converted_id
        struct.Id.charactersLen = len(Id)
        struct.Id_isUsed = Id_isUsed
        struct.ContractSignatureCertChain = ContractSignatureCertChain
        struct.ContractID.characters = converted_contract_id
        struct.ContractID.charactersLen = len(ContractID)
        struct.ListOfRootCertificateIDs = ListOfRootCertificateIDs
        struct.DHParams.bytes = converted_dh_params
        struct.DHParams.bytesLen = dinCertificateUpdateReqType_DHParams_BYTES_SIZE
        return struct

    def dinCertificateInstallationResType(  Id: str="",
                                            ResponseCode: int=0,
                                            ContractSignatureCertChain: OV2GStructs.dinCertificateChainType=dinCertificateChainType(),
                                            ContractSignatureEncryptedPrivateKey: str="",
                                            DHParams: str="",
                                            ContractID: str=""):
        converted_id = OpenV2GUtils.convert_to_array_type_characters(val=Id, size=dinCertificateInstallationResType_Id_CHARACTERS_SIZE)
        converted_contract_signature_encrypted_private_key = OpenV2GUtils.convert_to_array_type_bytes_str(val=ContractSignatureEncryptedPrivateKey, size=dinCertificateInstallationResType_ContractSignatureEncryptedPrivateKey_BYTES_SIZE)
        converted_dh_params = OpenV2GUtils.convert_to_array_type_bytes_str(val=DHParams, size=dinCertificateInstallationResType_DHParams_BYTES_SIZE)
        converted_contract_id = OpenV2GUtils.convert_to_array_type_characters(val=ContractID, size=dinCertificateInstallationResType_ContractID_CHARACTERS_SIZE)
        struct = OV2GStructs.dinCertificateInstallationResType()
        struct.Id.characters = converted_id
        struct.Id.charactersLen = len(Id)
        struct.ResponseCode = ResponseCode
        struct.ContractSignatureCertChain = ContractSignatureCertChain
        struct.ContractSignatureEncryptedPrivateKey.bytes = converted_contract_signature_encrypted_private_key
        struct.ContractSignatureEncryptedPrivateKey.bytesLen = dinCertificateInstallationResType_ContractSignatureEncryptedPrivateKey_BYTES_SIZE
        struct.DHParams.bytes = converted_dh_params
        struct.DHParams.bytesLen = dinCertificateInstallationResType_DHParams_BYTES_SIZE
        struct.ContractID.characters = converted_contract_id
        struct.ContractID.charactersLen = len(ContractID)
        return struct

    def dinCableCheckResType(   ResponseCode: int=0,
                                DC_EVSEStatus: OV2GStructs.dinDC_EVSEStatusType=dinDC_EVSEStatusType(),
                                EVSEProcessing: int=0):
        struct = OV2GStructs.dinCableCheckResType()
        struct.ResponseCode = ResponseCode
        struct.DC_EVSEStatus = DC_EVSEStatus
        struct.EVSEProcessing = EVSEProcessing
        return struct 

    def dinBodyType(BodyElement: OV2GStructs.dinBodyBaseType=dinBodyBaseType(),
                    SessionSetupReq: OV2GStructs.dinSessionSetupReqType=dinSessionSetupReqType(),
                    SessionSetupRes: OV2GStructs.dinSessionSetupResType=dinSessionSetupResType(),
                    ServiceDiscoveryReq: OV2GStructs.dinServiceDiscoveryReqType=dinServiceDiscoveryReqType(),
                    ServiceDiscoveryRes: OV2GStructs.dinServiceDiscoveryResType=dinServiceDiscoveryResType(),
                    ServiceDetailReq: OV2GStructs.dinServiceDetailReqType=dinServiceDetailReqType(),
                    ServiceDetailRes: OV2GStructs.dinServiceDetailResType=dinServiceDetailResType(),
                    ServicePaymentSelectionReq: OV2GStructs.dinServicePaymentSelectionReqType=dinServicePaymentSelectionReqType(),
                    ServicePaymentSelectionRes: OV2GStructs.dinServicePaymentSelectionResType=dinServicePaymentSelectionResType(),
                    PaymentDetailsReq: OV2GStructs.dinPaymentDetailsReqType=dinPaymentDetailsReqType(),
                    PaymentDetailsRes: OV2GStructs.dinPaymentDetailsResType=dinPaymentDetailsResType(),
                    ContractAuthenticationReq: OV2GStructs.dinContractAuthenticationReqType=dinContractAuthenticationReqType(),
                    ContractAuthenticationRes: OV2GStructs.dinContractAuthenticationResType=dinContractAuthenticationResType(),
                    ChargeParameterDiscoveryReq: OV2GStructs.dinChargeParameterDiscoveryReqType=dinChargeParameterDiscoveryReqType(),
                    ChargeParameterDiscoveryRes: OV2GStructs.dinChargeParameterDiscoveryResType=dinChargeParameterDiscoveryResType(),
                    PowerDeliveryReq: OV2GStructs.dinPowerDeliveryReqType=dinPowerDeliveryReqType(),
                    PowerDeliveryRes: OV2GStructs.dinPowerDeliveryResType=dinPowerDeliveryResType(),
                    ChargingStatusReq: OV2GStructs.dinChargingStatusReqType=dinChargingStatusReqType(),
                    ChargingStatusRes: OV2GStructs.dinChargingStatusResType=dinChargingStatusResType(),
                    MeteringReceiptReq: OV2GStructs.dinMeteringReceiptReqType=dinMeteringReceiptReqType(),
                    MeteringReceiptRes: OV2GStructs.dinMeteringReceiptResType=dinMeteringReceiptResType(),
                    SessionStopReq: OV2GStructs.dinSessionStopType=dinSessionStopType(),
                    SessionStopRes: OV2GStructs.dinSessionStopResType=dinSessionStopResType(),
                    CertificateUpdateReq: OV2GStructs.dinCertificateUpdateReqType=dinCertificateUpdateReqType(),
                    CertificateUpdateRes: OV2GStructs.dinCertificateUpdateResType=dinCertificateUpdateResType(),
                    CertificateInstallationReq: OV2GStructs.dinCertificateInstallationReqType=dinCertificateInstallationReqType(),
                    CertificateInstallationRes: OV2GStructs.dinCertificateInstallationResType=dinCertificateInstallationResType(),
                    CableCheckReq: OV2GStructs.dinCableCheckReqType=dinCableCheckReqType(),
                    CableCheckRes: OV2GStructs.dinCableCheckResType=dinCableCheckResType(),
                    PreChargeReq: OV2GStructs.dinPreChargeReqType=dinPreChargeReqType(),
                    PreChargeRes: OV2GStructs.dinPreChargeResType=dinPreChargeResType(),
                    CurrentDemandReq: OV2GStructs.dinCurrentDemandReqType=dinCurrentDemandReqType(),
                    CurrentDemandRes: OV2GStructs.dinCurrentDemandResType=dinCurrentDemandResType(),
                    WeldingDetectionReq: OV2GStructs.dinWeldingDetectionReqType=dinWeldingDetectionReqType(),
                    WeldingDetectionRes: OV2GStructs.dinWeldingDetectionResType=dinWeldingDetectionResType(),
                    BodyElement_isUsed: int=0,
                    SessionSetupReq_isUsed: int=0,
                    SessionSetupRes_isUsed: int=0,
                    ServiceDiscoveryReq_isUsed: int=0,
                    ServiceDiscoveryRes_isUsed: int=0,
                    ServiceDetailReq_isUsed: int=0,
                    ServiceDetailRes_isUsed: int=0,
                    ServicePaymentSelectionReq_isUsed: int=0,
                    ServicePaymentSelectionRes_isUsed: int=0,
                    PaymentDetailsReq_isUsed: int=0,
                    PaymentDetailsRes_isUsed: int=0,
                    ContractAuthenticationReq_isUsed: int=0,
                    ContractAuthenticationRes_isUsed: int=0,
                    ChargeParameterDiscoveryReq_isUsed: int=0,
                    ChargeParameterDiscoveryRes_isUsed: int=0,
                    PowerDeliveryReq_isUsed: int=0,
                    PowerDeliveryRes_isUsed: int=0,
                    ChargingStatusReq_isUsed: int=0,
                    ChargingStatusRes_isUsed: int=0,
                    MeteringReceiptReq_isUsed: int=0,
                    MeteringReceiptRes_isUsed: int=0,
                    SessionStopReq_isUsed: int=0,
                    SessionStopRes_isUsed: int=0,
                    CertificateUpdateReq_isUsed: int=0,
                    CertificateUpdateRes_isUsed: int=0,
                    CertificateInstallationReq_isUsed: int=0,
                    CertificateInstallationRes_isUsed: int=0,
                    CableCheckReq_isUsed: int=0,
                    CableCheckRes_isUsed: int=0,
                    PreChargeReq_isUsed: int=0,
                    PreChargeRes_isUsed: int=0,
                    CurrentDemandReq_isUsed: int=0,
                    CurrentDemandRes_isUsed: int=0,
                    WeldingDetectionReq_isUsed: int=0,
                    WeldingDetectionRes_isUsed: int=0):

        struct = OV2GStructs.dinBodyType()
        struct.BodyElement = BodyElement
        struct.SessionSetupReq = SessionSetupReq
        struct.SessionSetupRes = SessionSetupRes
        struct.ServiceDiscoveryReq = ServiceDiscoveryReq
        struct.ServiceDiscoveryRes = ServiceDiscoveryRes
        struct.ServiceDetailReq = ServiceDetailReq
        struct.ServiceDetailRes = ServiceDetailRes
        struct.ServicePaymentSelectionReq = ServicePaymentSelectionReq
        struct.ServicePaymentSelectionRes = ServicePaymentSelectionRes
        struct.PaymentDetailsReq = PaymentDetailsReq
        struct.PaymentDetailsRes = PaymentDetailsRes
        struct.ContractAuthenticationReq = ContractAuthenticationReq
        struct.ContractAuthenticationRes = ContractAuthenticationRes
        struct.ChargeParameterDiscoveryReq = ChargeParameterDiscoveryReq
        struct.ChargeParameterDiscoveryRes = ChargeParameterDiscoveryRes
        struct.PowerDeliveryReq = PowerDeliveryReq
        struct.PowerDeliveryRes = PowerDeliveryRes
        struct.ChargingStatusReq = ChargingStatusReq
        struct.ChargingStatusRes = ChargingStatusRes
        struct.MeteringReceiptReq = MeteringReceiptReq
        struct.MeteringReceiptRes = MeteringReceiptRes
        struct.SessionStopReq = SessionStopReq
        struct.SessionStopRes = SessionStopRes
        struct.CertificateUpdateReq = CertificateUpdateReq
        struct.CertificateUpdateRes = CertificateUpdateRes
        struct.CertificateInstallationReq = CertificateInstallationReq
        struct.CertificateInstallationRes = CertificateInstallationRes
        struct.CableCheckReq = CableCheckReq
        struct.CableCheckRes = CableCheckRes
        struct.PreChargeReq = PreChargeReq
        struct.PreChargeRes = PreChargeRes
        struct.CurrentDemandReq = CurrentDemandReq
        struct.CurrentDemandRes = CurrentDemandRes
        struct.WeldingDetectionReq = WeldingDetectionReq
        struct.WeldingDetectionRes = WeldingDetectionRes
        struct.BodyElement_isUsed = BodyElement_isUsed
        struct.SessionSetupReq_isUsed = SessionSetupReq_isUsed
        struct.SessionSetupRes_isUsed = SessionSetupRes_isUsed
        struct.ServiceDiscoveryReq_isUsed = ServiceDiscoveryReq_isUsed
        struct.ServiceDiscoveryRes_isUsed = ServiceDiscoveryRes_isUsed
        struct.ServiceDetailReq_isUsed = ServiceDetailReq_isUsed
        struct.ServiceDetailRes_isUsed = ServiceDetailRes_isUsed
        struct.ServicePaymentSelectionReq_isUsed = ServicePaymentSelectionReq_isUsed
        struct.ServicePaymentSelectionRes_isUsed = ServicePaymentSelectionRes_isUsed
        struct.PaymentDetailsReq_isUsed = PaymentDetailsReq_isUsed
        struct.PaymentDetailsRes_isUsed = PaymentDetailsRes_isUsed
        struct.ContractAuthenticationReq_isUsed = ContractAuthenticationReq_isUsed
        struct.ContractAuthenticationRes_isUsed = ContractAuthenticationRes_isUsed
        struct.ChargeParameterDiscoveryReq_isUsed = ChargeParameterDiscoveryReq_isUsed
        struct.ChargeParameterDiscoveryRes_isUsed = ChargeParameterDiscoveryRes_isUsed
        struct.PowerDeliveryReq_isUsed = PowerDeliveryReq_isUsed
        struct.PowerDeliveryRes_isUsed = PowerDeliveryRes_isUsed
        struct.ChargingStatusReq_isUsed = ChargingStatusReq_isUsed
        struct.ChargingStatusRes_isUsed = ChargingStatusRes_isUsed
        struct.MeteringReceiptReq_isUsed = MeteringReceiptReq_isUsed
        struct.MeteringReceiptRes_isUsed = MeteringReceiptRes_isUsed
        struct.SessionStopReq_isUsed = SessionStopReq_isUsed
        struct.SessionStopRes_isUsed = SessionStopRes_isUsed
        struct.CertificateUpdateReq_isUsed = CertificateUpdateReq_isUsed
        struct.CertificateUpdateRes_isUsed = CertificateUpdateRes_isUsed
        struct.CertificateInstallationReq_isUsed = CertificateInstallationReq_isUsed
        struct.CertificateInstallationRes_isUsed = CertificateInstallationRes_isUsed
        struct.CableCheckReq_isUsed = CableCheckReq_isUsed
        struct.CableCheckRes_isUsed = CableCheckRes_isUsed
        struct.PreChargeReq_isUsed = PreChargeReq_isUsed
        struct.PreChargeRes_isUsed = PreChargeRes_isUsed
        struct.CurrentDemandReq_isUsed = CurrentDemandReq_isUsed
        struct.CurrentDemandRes_isUsed = CurrentDemandRes_isUsed
        struct.WeldingDetectionReq_isUsed = WeldingDetectionReq_isUsed
        struct.WeldingDetectionRes_isUsed = WeldingDetectionRes_isUsed
        return struct


    def dinAnonType_V2G_Message(Header: OV2GStructs.dinMessageHeaderType=dinMessageHeaderType(),
                                Body: OV2GStructs.dinBodyType=dinBodyType()):
        struct = OV2GStructs.dinAnonType_V2G_Message()
        struct.Header = Header
        struct.Body = Body
        return struct

    def dinManifestType(Id: str="",
                        Id_isUsed: int=0,
                        Reference: list[OV2GStructs.dinReferenceType]=[dinReferenceType()]):
        converted_id = OpenV2GUtils.convert_to_array_type_characters(val=Id, size=dinManifestType_Id_CHARACTERS_SIZE)
        struct = OV2GStructs.dinManifestType()
        struct.Id.characters = converted_id
        struct.Id.charactersLen = len(Id)
        struct.Id_isUsed = Id_isUsed
        struct.Reference.array[0] = Reference[0]
        struct.Reference.arrayLen = dinManifestType_Reference_ARRAY_SIZE
        return struct


    def dinEXIDocument( BodyElement: OV2GStructs.dinBodyBaseType=dinBodyBaseType(),
                        V2G_Message: OV2GStructs.dinAnonType_V2G_Message=dinAnonType_V2G_Message(),
                        SignatureProperty: OV2GStructs.dinSignaturePropertyType=dinSignaturePropertyType(),
                        DSAKeyValue: OV2GStructs.dinDSAKeyValueType=dinDSAKeyValueType(),
                        SignatureProperties: OV2GStructs.dinSignaturePropertiesType=dinSignaturePropertiesType(),
                        KeyValue: OV2GStructs.dinKeyValueType=dinKeyValueType(),
                        Transforms: OV2GStructs.dinTransformsType=dinTransformsType(),
                        DigestMethod: OV2GStructs.dinDigestMethodType=dinDigestMethodType(),
                        Signature: OV2GStructs.dinSignatureType=dinSignatureType(),
                        RetrievalMethod: OV2GStructs.dinRetrievalMethodType=dinRetrievalMethodType(),
                        Manifest: OV2GStructs.dinManifestType=dinManifestType(),
                        Reference: OV2GStructs.dinReferenceType=dinReferenceType(),
                        CanonicalizationMethod: OV2GStructs.dinCanonicalizationMethodType=dinCanonicalizationMethodType(),
                        RSAKeyValue: OV2GStructs.dinRSAKeyValueType=dinRSAKeyValueType(),
                        Transform: OV2GStructs.dinTransformType=dinTransformType(),
                        PGPData: OV2GStructs.dinPGPDataType=dinPGPDataType(),
                        MgmtData: str="",
                        SignatureMethod: OV2GStructs.dinSignatureMethodType=dinSignatureMethodType(),
                        KeyInfo: OV2GStructs.dinKeyInfoType=dinKeyInfoType(),
                        SPKIData: OV2GStructs.dinSPKIDataType=dinSPKIDataType(),
                        X509Data: OV2GStructs.dinX509DataType=dinX509DataType(),
                        SignatureValue: OV2GStructs.dinSignatureValueType=dinSignatureValueType(),
                        KeyName: str="",
                        DigestValue: str="",
                        SignedInfo: OV2GStructs.dinSignedInfoType=dinSignedInfoType(),
                        Object: OV2GStructs.dinObjectType=dinObjectType(),
                        DC_EVSEStatus: OV2GStructs.dinDC_EVSEStatusType=dinDC_EVSEStatusType(),
                        RelativeTimeInterval: OV2GStructs.dinRelativeTimeIntervalType=dinRelativeTimeIntervalType(),
                        SalesTariffEntry: OV2GStructs.dinSalesTariffEntryType=dinSalesTariffEntryType(),
                        DC_EVPowerDeliveryParameter: OV2GStructs.dinDC_EVPowerDeliveryParameterType=dinDC_EVPowerDeliveryParameterType(),
                        SASchedules: OV2GStructs.dinSASchedulesType=dinSASchedulesType(),
                        AC_EVChargeParameter: OV2GStructs.dinAC_EVChargeParameterType=dinAC_EVChargeParameterType(),
                        SAScheduleList: OV2GStructs.dinSAScheduleListType=dinSAScheduleListType(),
                        DC_EVStatus: OV2GStructs.dinDC_EVStatusType=dinDC_EVStatusType(),
                        ServiceCharge: OV2GStructs.dinServiceChargeType=dinServiceChargeType(),
                        EVStatus: OV2GStructs.dinEVStatusType=dinEVStatusType(),
                        DC_EVChargeParameter: OV2GStructs.dinDC_EVChargeParameterType=dinDC_EVChargeParameterType(),
                        DC_EVSEChargeParameter: OV2GStructs.dinDC_EVSEChargeParameterType=dinDC_EVSEChargeParameterType(),
                        EVSEStatus: OV2GStructs.dinEVSEStatusType=dinEVSEStatusType(),
                        TimeInterval: OV2GStructs.dinIntervalType=dinIntervalType(),
                        EVPowerDeliveryParameter: OV2GStructs.dinEVPowerDeliveryParameterType=dinEVPowerDeliveryParameterType(),
                        EVSEChargeParameter: OV2GStructs.dinEVSEChargeParameterType=dinEVSEChargeParameterType(),
                        AC_EVSEStatus: OV2GStructs.dinAC_EVSEStatusType=dinAC_EVSEStatusType(),
                        Entry: OV2GStructs.dinEntryType=dinEntryType(),
                        AC_EVSEChargeParameter: OV2GStructs.dinAC_EVSEChargeParameterType=dinAC_EVSEChargeParameterType(),
                        PMaxScheduleEntry: OV2GStructs.dinPMaxScheduleEntryType=dinPMaxScheduleEntryType(),
                        EVChargeParameter: OV2GStructs.dinEVChargeParameterType=dinEVChargeParameterType(),
                        ServiceDiscoveryReq: OV2GStructs.dinServiceDiscoveryReqType=dinServiceDiscoveryReqType(),
                        ServiceDiscoveryRes: OV2GStructs.dinServiceDiscoveryResType=dinServiceDiscoveryResType(),
                        MeteringReceiptReq: OV2GStructs.dinMeteringReceiptReqType=dinMeteringReceiptReqType(),
                        PaymentDetailsReq: OV2GStructs.dinPaymentDetailsReqType=dinPaymentDetailsReqType(),
                        MeteringReceiptRes: OV2GStructs.dinMeteringReceiptResType=dinMeteringReceiptResType(),
                        PaymentDetailsRes: OV2GStructs.dinPaymentDetailsResType=dinPaymentDetailsResType(),
                        SessionSetupReq: OV2GStructs.dinSessionSetupReqType=dinSessionSetupReqType(),
                        SessionSetupRes: OV2GStructs.dinSessionSetupResType=dinSessionSetupResType(),
                        CableCheckReq: OV2GStructs.dinCableCheckReqType=dinCableCheckReqType(),
                        CableCheckRes: OV2GStructs.dinCableCheckResType=dinCableCheckResType(),
                        ContractAuthenticationReq: OV2GStructs.dinContractAuthenticationReqType=dinContractAuthenticationReqType(),
                        CertificateInstallationReq: OV2GStructs.dinCertificateInstallationReqType=dinCertificateInstallationReqType(),
                        ContractAuthenticationRes: OV2GStructs.dinContractAuthenticationResType=dinContractAuthenticationResType(),
                        CertificateInstallationRes: OV2GStructs.dinCertificateInstallationResType=dinCertificateInstallationResType(),
                        WeldingDetectionReq: OV2GStructs.dinWeldingDetectionReqType=dinWeldingDetectionReqType(),
                        WeldingDetectionRes: OV2GStructs.dinWeldingDetectionResType=dinWeldingDetectionResType(),
                        CertificateUpdateReq: OV2GStructs.dinCertificateUpdateReqType=dinCertificateUpdateReqType(),
                        CertificateUpdateRes: OV2GStructs.dinCertificateUpdateResType=dinCertificateUpdateResType(),
                        PowerDeliveryReq: OV2GStructs.dinPowerDeliveryReqType=dinPowerDeliveryReqType(),
                        PowerDeliveryRes: OV2GStructs.dinPowerDeliveryResType=dinPowerDeliveryResType(),
                        ChargingStatusReq: OV2GStructs.dinChargingStatusReqType=dinChargingStatusReqType(),
                        ChargingStatusRes: OV2GStructs.dinChargingStatusResType=dinChargingStatusResType(),
                        CurrentDemandReq: OV2GStructs.dinCurrentDemandReqType=dinCurrentDemandReqType(),
                        PreChargeReq: OV2GStructs.dinPreChargeReqType=dinPreChargeReqType(),
                        CurrentDemandRes: OV2GStructs.dinCurrentDemandResType=dinCurrentDemandResType(),
                        PreChargeRes: OV2GStructs.dinPreChargeResType=dinPreChargeResType(),
                        ServicePaymentSelectionReq: OV2GStructs.dinServicePaymentSelectionReqType=dinServicePaymentSelectionReqType(),
                        SessionStopReq: OV2GStructs.dinSessionStopType=dinSessionStopType(),
                        ServicePaymentSelectionRes: OV2GStructs.dinServicePaymentSelectionResType=dinServicePaymentSelectionResType(),
                        SessionStopRes: OV2GStructs.dinSessionStopResType=dinSessionStopResType(),
                        ChargeParameterDiscoveryReq: OV2GStructs.dinChargeParameterDiscoveryReqType=dinChargeParameterDiscoveryReqType(),
                        ChargeParameterDiscoveryRes: OV2GStructs.dinChargeParameterDiscoveryResType=dinChargeParameterDiscoveryResType(),
                        ServiceDetailReq: OV2GStructs.dinServiceDetailReqType=dinServiceDetailReqType(),
                        ServiceDetailRes: OV2GStructs.dinServiceDetailResType=dinServiceDetailResType(),
                        BodyElement_isUsed: int=0,
                        V2G_Message_isUsed: int=0,
                        SignatureProperty_isUsed: int=0,
                        DSAKeyValue_isUsed: int=0,
                        SignatureProperties_isUsed: int=0,
                        KeyValue_isUsed: int=0,
                        Transforms_isUsed: int=0,
                        DigestMethod_isUsed: int=0,
                        Signature_isUsed: int=0,
                        RetrievalMethod_isUsed: int=0,
                        Manifest_isUsed: int=0,
                        Reference_isUsed: int=0,
                        CanonicalizationMethod_isUsed: int=0,
                        RSAKeyValue_isUsed: int=0,
                        Transform_isUsed: int=0,
                        PGPData_isUsed: int=0,
                        MgmtData_isUsed: int=0,
                        SignatureMethod_isUsed: int=0,
                        KeyInfo_isUsed: int=0,
                        SPKIData_isUsed: int=0,
                        X509Data_isUsed: int=0,
                        SignatureValue_isUsed: int=0,
                        KeyName_isUsed: int=0,
                        DigestValue_isUsed: int=0,
                        SignedInfo_isUsed: int=0,
                        Object_isUsed: int=0,
                        DC_EVSEStatus_isUsed: int=0,
                        RelativeTimeInterval_isUsed: int=0,
                        SalesTariffEntry_isUsed: int=0,
                        DC_EVPowerDeliveryParameter_isUsed: int=0,
                        SASchedules_isUsed: int=0,
                        AC_EVChargeParameter_isUsed: int=0,
                        SAScheduleList_isUsed: int=0,
                        DC_EVStatus_isUsed: int=0,
                        ServiceCharge_isUsed: int=0,
                        EVStatus_isUsed: int=0,
                        DC_EVChargeParameter_isUsed: int=0,
                        DC_EVSEChargeParameter_isUsed: int=0,
                        EVSEStatus_isUsed: int=0,
                        TimeInterval_isUsed: int=0,
                        EVPowerDeliveryParameter_isUsed: int=0,
                        EVSEChargeParameter_isUsed: int=0,
                        AC_EVSEStatus_isUsed: int=0,
                        Entry_isUsed: int=0,
                        AC_EVSEChargeParameter_isUsed: int=0,
                        PMaxScheduleEntry_isUsed: int=0,
                        EVChargeParameter_isUsed: int=0,
                        ServiceDiscoveryReq_isUsed: int=0,
                        ServiceDiscoveryRes_isUsed: int=0,
                        MeteringReceiptReq_isUsed: int=0,
                        PaymentDetailsReq_isUsed: int=0,
                        MeteringReceiptRes_isUsed: int=0,
                        PaymentDetailsRes_isUsed: int=0,
                        SessionSetupReq_isUsed: int=0,
                        SessionSetupRes_isUsed: int=0,
                        CableCheckReq_isUsed: int=0,
                        CableCheckRes_isUsed: int=0,
                        ContractAuthenticationReq_isUsed: int=0,
                        CertificateInstallationReq_isUsed: int=0,
                        ContractAuthenticationRes_isUsed: int=0,
                        CertificateInstallationRes_isUsed: int=0,
                        WeldingDetectionReq_isUsed: int=0,
                        WeldingDetectionRes_isUsed: int=0,
                        CertificateUpdateReq_isUsed: int=0,
                        CertificateUpdateRes_isUsed: int=0,
                        PowerDeliveryReq_isUsed: int=0,
                        PowerDeliveryRes_isUsed: int=0,
                        ChargingStatusReq_isUsed: int=0,
                        ChargingStatusRes_isUsed: int=0,
                        CurrentDemandReq_isUsed: int=0,
                        PreChargeReq_isUsed: int=0,
                        CurrentDemandRes_isUsed: int=0,
                        PreChargeRes_isUsed: int=0,
                        ServicePaymentSelectionReq_isUsed: int=0,
                        SessionStopReq_isUsed: int=0,
                        ServicePaymentSelectionRes_isUsed: int=0,
                        SessionStopRes_isUsed: int=0,
                        ChargeParameterDiscoveryReq_isUsed: int=0,
                        ChargeParameterDiscoveryRes_isUsed: int=0,
                        ServiceDetailReq_isUsed: int=0,
                        ServiceDetailRes_isUsed: int=0,
                        _warning_: int=0):

        converted_mgmt_data = OpenV2GUtils.convert_to_array_type_characters(val=MgmtData, size=dinKeyInfoType_MgmtData_CHARACTERS_SIZE)
        converted_key_name = OpenV2GUtils.convert_to_array_type_characters(val=KeyName, size=dinKeyInfoType_KeyName_CHARACTERS_SIZE)
        converted_digest_value = OpenV2GUtils.convert_to_array_type_bytes_str(val=DigestValue, size=dinReferenceType_DigestValue_BYTES_SIZE)
        struct = OV2GStructs.dinEXIDocument()
        struct.BodyElement = BodyElement
        struct.V2G_Message = V2G_Message
        struct.SignatureProperty = SignatureProperty
        struct.DSAKeyValue = DSAKeyValue
        struct.SignatureProperties = SignatureProperties
        struct.KeyValue = KeyValue
        struct.Transforms = Transforms
        struct.DigestMethod = DigestMethod
        struct.Signature = Signature
        struct.RetrievalMethod = RetrievalMethod
        struct.Manifest = Manifest
        struct.Reference = Reference
        struct.CanonicalizationMethod = CanonicalizationMethod
        struct.RSAKeyValue = RSAKeyValue
        struct.Transform = Transform
        struct.PGPData = PGPData
        struct.MgmtData.characters = converted_mgmt_data
        struct.MgmtData.charactersLen = len(MgmtData)
        struct.SignatureMethod = SignatureMethod
        struct.KeyInfo = KeyInfo
        struct.SPKIData = SPKIData
        struct.X509Data = X509Data
        struct.SignatureValue = SignatureValue
        struct.KeyName.characters = converted_key_name
        struct.KeyName.charactersLen = len(KeyName)
        struct.DigestValue.bytes = converted_digest_value
        struct.DigestValue.bytesLen = EXIDocument_DigestValue_BYTES_SIZE
        struct.SignedInfo = SignedInfo
        struct.Object = Object
        struct.DC_EVSEStatus = DC_EVSEStatus
        struct.RelativeTimeInterval = RelativeTimeInterval
        struct.SalesTariffEntry = SalesTariffEntry
        struct.DC_EVPowerDeliveryParameter = DC_EVPowerDeliveryParameter
        struct.SASchedules = SASchedules
        struct.AC_EVChargeParameter = AC_EVChargeParameter
        struct.SAScheduleList = SAScheduleList
        struct.DC_EVStatus = DC_EVStatus
        struct.ServiceCharge = ServiceCharge
        struct.EVStatus = EVStatus
        struct.DC_EVChargeParameter = DC_EVChargeParameter
        struct.DC_EVSEChargeParameter = DC_EVSEChargeParameter
        struct.EVSEStatus = EVSEStatus
        struct.TimeInterval = TimeInterval
        struct.EVPowerDeliveryParameter = EVPowerDeliveryParameter
        struct.EVSEChargeParameter = EVSEChargeParameter
        struct.AC_EVSEStatus = AC_EVSEStatus
        struct.Entry = Entry
        struct.AC_EVSEChargeParameter = AC_EVSEChargeParameter
        struct.PMaxScheduleEntry = PMaxScheduleEntry
        struct.EVChargeParameter = EVChargeParameter
        struct.ServiceDiscoveryReq = ServiceDiscoveryReq
        struct.ServiceDiscoveryRes = ServiceDiscoveryRes
        struct.MeteringReceiptReq = MeteringReceiptReq
        struct.PaymentDetailsReq = PaymentDetailsReq
        struct.MeteringReceiptRes = MeteringReceiptRes
        struct.PaymentDetailsRes = PaymentDetailsRes
        struct.SessionSetupReq = SessionSetupReq
        struct.SessionSetupRes = SessionSetupRes
        struct.CableCheckReq = CableCheckReq
        struct.CableCheckRes = CableCheckRes
        struct.ContractAuthenticationReq = ContractAuthenticationReq
        struct.CertificateInstallationReq = CertificateInstallationReq
        struct.ContractAuthenticationRes = ContractAuthenticationRes
        struct.CertificateInstallationRes = CertificateInstallationRes
        struct.WeldingDetectionReq = WeldingDetectionReq
        struct.WeldingDetectionRes = WeldingDetectionRes
        struct.CertificateUpdateReq = CertificateUpdateReq
        struct.CertificateUpdateRes = CertificateUpdateRes
        struct.PowerDeliveryReq = PowerDeliveryReq
        struct.PowerDeliveryRes = PowerDeliveryRes
        struct.ChargingStatusReq = ChargingStatusReq
        struct.ChargingStatusRes = ChargingStatusRes
        struct.CurrentDemandReq = CurrentDemandReq
        struct.PreChargeReq = PreChargeReq
        struct.CurrentDemandRes = CurrentDemandRes
        struct.PreChargeRes = PreChargeRes
        struct.ServicePaymentSelectionReq = ServicePaymentSelectionReq
        struct.SessionStopReq = SessionStopReq
        struct.ServicePaymentSelectionRes = ServicePaymentSelectionRes
        struct.SessionStopRes = SessionStopRes
        struct.ChargeParameterDiscoveryReq = ChargeParameterDiscoveryReq
        struct.ChargeParameterDiscoveryRes = ChargeParameterDiscoveryRes
        struct.ServiceDetailReq = ServiceDetailReq
        struct.ServiceDetailRes = ServiceDetailRes
        struct.BodyElement_isUsed = BodyElement_isUsed
        struct.V2G_Message_isUsed = V2G_Message_isUsed
        struct.SignatureProperty_isUsed = SignatureProperty_isUsed
        struct.DSAKeyValue_isUsed = DSAKeyValue_isUsed
        struct.SignatureProperties_isUsed = SignatureProperties_isUsed
        struct.KeyValue_isUsed = KeyValue_isUsed
        struct.Transforms_isUsed = Transforms_isUsed
        struct.DigestMethod_isUsed = DigestMethod_isUsed
        struct.Signature_isUsed = Signature_isUsed
        struct.RetrievalMethod_isUsed = RetrievalMethod_isUsed
        struct.Manifest_isUsed = Manifest_isUsed
        struct.Reference_isUsed = Reference_isUsed
        struct.CanonicalizationMethod_isUsed = CanonicalizationMethod_isUsed
        struct.RSAKeyValue_isUsed = RSAKeyValue_isUsed
        struct.Transform_isUsed = Transform_isUsed
        struct.PGPData_isUsed = PGPData_isUsed
        struct.MgmtData_isUsed = MgmtData_isUsed
        struct.SignatureMethod_isUsed = SignatureMethod_isUsed
        struct.KeyInfo_isUsed = KeyInfo_isUsed
        struct.SPKIData_isUsed = SPKIData_isUsed
        struct.X509Data_isUsed = X509Data_isUsed
        struct.SignatureValue_isUsed = SignatureValue_isUsed
        struct.KeyName_isUsed = KeyName_isUsed
        struct.DigestValue_isUsed = DigestValue_isUsed
        struct.SignedInfo_isUsed = SignedInfo_isUsed
        struct.Object_isUsed = Object_isUsed
        struct.DC_EVSEStatus_isUsed = DC_EVSEStatus_isUsed
        struct.RelativeTimeInterval_isUsed = RelativeTimeInterval_isUsed
        struct.SalesTariffEntry_isUsed = SalesTariffEntry_isUsed
        struct.DC_EVPowerDeliveryParameter_isUsed = DC_EVPowerDeliveryParameter_isUsed
        struct.SASchedules_isUsed = SASchedules_isUsed
        struct.AC_EVChargeParameter_isUsed = AC_EVChargeParameter_isUsed
        struct.SAScheduleList_isUsed = SAScheduleList_isUsed
        struct.DC_EVStatus_isUsed = DC_EVStatus_isUsed
        struct.ServiceCharge_isUsed = ServiceCharge_isUsed
        struct.EVStatus_isUsed = EVStatus_isUsed
        struct.DC_EVChargeParameter_isUsed = DC_EVChargeParameter_isUsed
        struct.DC_EVSEChargeParameter_isUsed = DC_EVSEChargeParameter_isUsed
        struct.EVSEStatus_isUsed = EVSEStatus_isUsed
        struct.TimeInterval_isUsed = TimeInterval_isUsed
        struct.EVPowerDeliveryParameter_isUsed = EVPowerDeliveryParameter_isUsed
        struct.EVSEChargeParameter_isUsed = EVSEChargeParameter_isUsed
        struct.AC_EVSEStatus_isUsed = AC_EVSEStatus_isUsed
        struct.Entry_isUsed = Entry_isUsed
        struct.AC_EVSEChargeParameter_isUsed = AC_EVSEChargeParameter_isUsed
        struct.PMaxScheduleEntry_isUsed = PMaxScheduleEntry_isUsed
        struct.EVChargeParameter_isUsed = EVChargeParameter_isUsed
        struct.ServiceDiscoveryReq_isUsed = ServiceDiscoveryReq_isUsed
        struct.ServiceDiscoveryRes_isUsed = ServiceDiscoveryRes_isUsed
        struct.MeteringReceiptReq_isUsed = MeteringReceiptReq_isUsed
        struct.PaymentDetailsReq_isUsed = PaymentDetailsReq_isUsed
        struct.MeteringReceiptRes_isUsed = MeteringReceiptRes_isUsed
        struct.PaymentDetailsRes_isUsed = PaymentDetailsRes_isUsed
        struct.SessionSetupReq_isUsed = SessionSetupReq_isUsed
        struct.SessionSetupRes_isUsed = SessionSetupRes_isUsed
        struct.CableCheckReq_isUsed = CableCheckReq_isUsed
        struct.CableCheckRes_isUsed = CableCheckRes_isUsed
        struct.ContractAuthenticationReq_isUsed = ContractAuthenticationReq_isUsed
        struct.CertificateInstallationReq_isUsed = CertificateInstallationReq_isUsed
        struct.ContractAuthenticationRes_isUsed = ContractAuthenticationRes_isUsed
        struct.CertificateInstallationRes_isUsed = CertificateInstallationRes_isUsed
        struct.WeldingDetectionReq_isUsed = WeldingDetectionReq_isUsed
        struct.WeldingDetectionRes_isUsed = WeldingDetectionRes_isUsed
        struct.CertificateUpdateReq_isUsed = CertificateUpdateReq_isUsed
        struct.CertificateUpdateRes_isUsed = CertificateUpdateRes_isUsed
        struct.PowerDeliveryReq_isUsed = PowerDeliveryReq_isUsed
        struct.PowerDeliveryRes_isUsed = PowerDeliveryRes_isUsed
        struct.ChargingStatusReq_isUsed = ChargingStatusReq_isUsed
        struct.ChargingStatusRes_isUsed = ChargingStatusRes_isUsed
        struct.CurrentDemandReq_isUsed = CurrentDemandReq_isUsed
        struct.PreChargeReq_isUsed = PreChargeReq_isUsed
        struct.CurrentDemandRes_isUsed = CurrentDemandRes_isUsed
        struct.PreChargeRes_isUsed = PreChargeRes_isUsed
        struct.ServicePaymentSelectionReq_isUsed = ServicePaymentSelectionReq_isUsed
        struct.SessionStopReq_isUsed = SessionStopReq_isUsed
        struct.ServicePaymentSelectionRes_isUsed = ServicePaymentSelectionRes_isUsed
        struct.SessionStopRes_isUsed = SessionStopRes_isUsed
        struct.ChargeParameterDiscoveryReq_isUsed = ChargeParameterDiscoveryReq_isUsed
        struct.ChargeParameterDiscoveryRes_isUsed = ChargeParameterDiscoveryRes_isUsed
        struct.ServiceDetailReq_isUsed = ServiceDetailReq_isUsed
        struct.ServiceDetailRes_isUsed = ServiceDetailRes_isUsed
        struct._warning_ = _warning_
        return struct
