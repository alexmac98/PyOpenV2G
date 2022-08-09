import ctypes
from open_v2g_structs import *
from open_v2g_utils import OpenV2GUtils
from open_v2g_constants import *

class OpenV2GStructDeclarator:
    def appHandAppProtocolType( ProtocolNamespace: str="", 
                                VersionNumberMajor: int=0, 
                                VersionNumberMinor: int=0, 
                                SchemaID: int=0, 
                                Priority: int=0):
        converted_protocol_namespace = OpenV2GUtils.convert_to_array_type_characters(val=ProtocolNamespace, size=appHandAppProtocolType_ProtocolNamespace_CHARACTERS_SIZE)
        struct = appHandAppProtocolType()
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
        struct = appHandAnonType_supportedAppProtocolRes()
        struct.ResponseCode = ResponseCode
        struct.SchemaID = SchemaID
        struct.SchemaID_isUsed = SchemaID_isUsed
        return struct

    def appHandAnonType_supportedAppProtocolReq(AppProtocol: list[appHandAppProtocolType]=[]):
        struct = appHandAnonType_supportedAppProtocolReq()
        for i in range(len(AppProtocol)):
            struct.AppProtocol.array[i] = AppProtocol[i]
        struct.AppProtocol.arrayLen = len(AppProtocol)
        return struct

    def appHandEXIDocument( supportedAppProtocolReq: appHandAnonType_supportedAppProtocolReq=appHandAnonType_supportedAppProtocolReq(), 
                            supportedAppProtocolRes: appHandAnonType_supportedAppProtocolRes=appHandAnonType_supportedAppProtocolRes(), 
                            supportedAppProtocolReq_isUsed: int=0, 
                            supportedAppProtocolRes_isUsed: int=0, 
                            _warning_: int=0):
        struct = appHandEXIDocument()
        struct.supportedAppProtocolReq = supportedAppProtocolReq
        struct.supportedAppProtocolRes = supportedAppProtocolRes
        struct.supportedAppProtocolReq_isUsed = supportedAppProtocolReq_isUsed
        struct.supportedAppProtocolRes_isUsed = supportedAppProtocolRes_isUsed
        struct._warning_ = _warning_
        return struct

    def bitstream_t(size: int=256,
                    data: list[int]=[],
                    pos: int=0,
                    buffer: int=0,
                    capacity: int=256):

        c_size = ctypes.c_size_t(size)
        c_data = (ctypes.c_ubyte*size)(*data) 
        c_pos = ctypes.c_size_t(pos)
        c_buffer = ctypes.c_uint8(buffer) 
        c_capacity = ctypes.c_uint8(capacity)

        struct = bitstream_t()
        struct.size = c_size
        struct.data = ctypes.cast(c_data, ctypes.POINTER(ctypes.c_ubyte))
        struct.pos = ctypes.pointer(c_pos)
        struct.buffer = c_buffer
        struct.capacity = c_capacity
        return struct

    # --------------------- DIN ---------------------
    def dinSessionSetupReqType( EVCCID: int=0):
        struct = dinSessionSetupReqType()
        struct.EVCCID.bytes = OpenV2GUtils.convert_to_array_type_bytes(EVCCID)
        struct.EVCCID.bytesLen = dinSessionSetupReqType_EVCCID_BYTES_SIZE
        return struct

    def dinEVSEStatusType(noContent=0):
        struct = dinEVSEStatusType()
        struct.noContent = noContent
        return struct
        
    def dinAC_EVSEStatusType(   PowerSwitchClosed: int=0, 
                                RCD: int=0, 
                                NotificationMaxDelay: int=0, 
                                EVSENotification: int=0):
        struct = dinAC_EVSEStatusType()
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
        struct = dinDC_EVSEStatusType()
        struct.EVSEIsolationStatus = EVSEIsolationStatus
        struct.EVSEIsolationStatus_isUsed = EVSEIsolationStatus_isUsed
        struct.EVSEStatusCode = EVSEStatusCode
        struct.NotificationMaxDelay = NotificationMaxDelay
        struct.EVSENotification = EVSENotification
        return struct

    def dinPowerDeliveryResType(ResponseCode: int=0, 
                                EVSEStatus: dinEVSEStatusType=dinEVSEStatusType(), 
                                EVSEStatus_isUsed: int=0, 
                                AC_EVSEStatus: dinAC_EVSEStatusType=dinAC_EVSEStatusType(), 
                                AC_EVSEStatus_isUsed: int=0, 
                                DC_EVSEStatus: dinDC_EVSEStatusType=dinDC_EVSEStatusType(), 
                                DC_EVSEStatus_isUsed: int=0):
        struct = dinPowerDeliveryResType()
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
        struct = dinPhysicalValueType()
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
                            physicalValue: dinPhysicalValueType=dinPhysicalValueType(), 
                            physicalValue_isUsed: int=0, 
                            stringValue: str="", 
                            stringValue_isUsed: int=0):

        converted_name = OpenV2GUtils.convert_to_array_type_characters(val=Name)
        converted_string_value = OpenV2GUtils.convert_to_array_type_characters(val=stringValue)
        struct = dinParameterType()
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
                            Parameter: list[dinParameterType]=[]):
        converted_array = (dinParameterType*dinParameterSetType_Parameter_ARRAY_SIZE)(*Parameter)
        struct = dinParameterSetType()
        struct.ParameterSetID = ParameterSetID
        struct.Parameter.array = converted_array
        struct.Parameter.arrayLen = len(Parameter)
        return struct


    def dinServiceParameterListType(ParameterSet: list[dinParameterSetType]=[]):
        converted_array = (dinParameterSetType*dinServiceParameterListType_ParameterSet_ARRAY_SIZE)(*ParameterSet)
        struct = dinServiceParameterListType()
        struct.ParameterSet.array = converted_array
        struct.ParameterSet.arrayLen = len(ParameterSet)
        return struct


    def dinServiceDetailResType(ResponseCode: int=0, 
                                ServiceID: int=0, 
                                ServiceParameterList: dinServiceParameterListType=dinServiceParameterListType(), 
                                ServiceParameterList_isUsed: int=0):
        struct = dinServiceDetailResType()
        struct.ResponseCode = ResponseCode
        struct.ServiceID = ServiceID
        struct.ServiceParameterList = ServiceParameterList
        struct.ServiceParameterList_isUsed = ServiceParameterList_isUsed
        return struct

    
    def dinWeldingDetectionResType( ResponseCode: int=0, 
                                    DC_EVSEStatus: dinDC_EVSEStatusType=dinDC_EVSEStatusType(), 
                                    EVSEPresentVoltage: dinPhysicalValueType=dinPhysicalValueType()):
        struct = dinWeldingDetectionResType()
        struct.ResponseCode = ResponseCode
        struct.DC_EVSEStatus = DC_EVSEStatus
        struct.EVSEPresentVoltage = EVSEPresentVoltage
        return struct


    def dinContractAuthenticationResType(   ResponseCode: int=0, 
                                            EVSEProcessing: int=0):
        struct = dinContractAuthenticationResType()
        struct.ResponseCode = ResponseCode
        struct.EVSEProcessing = EVSEProcessing
        return struct

    
    def dinCanonicalizationMethodType(  Algorithm: str="", 
                                        ANY: str="", 
                                        ANY_isUsed: int=0):
        converted_algorithm = OpenV2GUtils.convert_to_array_type_characters(val=Algorithm, size=dinCanonicalizationMethodType_Algorithm_CHARACTERS_SIZE)
        converted_any = OpenV2GUtils.convert_to_array_type_characters(val=ANY, size=dinCanonicalizationMethodType_ANY_CHARACTERS_SIZE)
        struct = dinCanonicalizationMethodType()
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
        struct = dinSPKIDataType()
        struct.SPKISexp.array[0].bytes =  converted_spki_exp
        struct.SPKISexp.array[0].bytesLen = dinSPKIDataType_SPKISexp_BYTES_SIZE
        struct.SPKISexp.arrayLen = dinSPKIDataType_SPKISexp_ARRAY_SIZE
        struct.ANY.characters = converted_any
        struct.ANY.charactersLen = len(ANY)
        struct.ANY_isUsed = ANY_isUsed
        return struct        

    
    def dinListOfRootCertificateIDsType(RootCertificateID: list[str]=[]):
        struct = dinListOfRootCertificateIDsType()

        for i in range(len(RootCertificateID)):
            converted_characters = OpenV2GUtils.convert_to_array_type_characters(val=RootCertificateID[i], size=dinListOfRootCertificateIDsType_RootCertificateID_CHARACTERS_SIZE)
            struct.RootCertificateID.array[i].characters = converted_characters
            struct.RootCertificateID.array[i].charactersLen = len(RootCertificateID[i])
        
        struct.RootCertificateID.arrayLen = len(RootCertificateID)        
        return struct


    def dinSelectedServiceType( ServiceID: int=0, 
                                ParameterSetID: int=0, 
                                ParameterSetID_isUsed: int=0):
        struct = dinSelectedServiceType()
        struct.ServiceID = ServiceID
        struct.ParameterSetID = ParameterSetID
        struct.ParameterSetID_isUsed = ParameterSetID_isUsed
        return struct


    def dinSelectedServiceListType(SelectedService: list[dinSelectedServiceType]=[]):
        struct = dinSelectedServiceListType()
        for i in range(len(SelectedService)):
            struct.SelectedService.array[i] = SelectedService[i]
        struct.SelectedService.arrayLen = len(SelectedService)
        return struct


    def dinCurrentDemandResType(ResponseCode: int=0, 
                                DC_EVSEStatus: dinDC_EVSEStatusType=dinDC_EVSEStatusType(),
                                EVSEPresentVoltage: dinPhysicalValueType=dinPhysicalValueType(),
                                EVSEPresentCurrent: dinPhysicalValueType=dinPhysicalValueType(),
                                EVSECurrentLimitAchieved: int=0,
                                EVSEVoltageLimitAchieved: int=0,
                                EVSEPowerLimitAchieved: int=0,
                                EVSEMaximumVoltageLimit: dinPhysicalValueType=dinPhysicalValueType(),
                                EVSEMaximumVoltageLimit_isUsed: int=0,
                                EVSEMaximumCurrentLimit: dinPhysicalValueType=dinPhysicalValueType(),
                                EVSEMaximumCurrentLimit_isUsed: int=0,
                                EVSEMaximumPowerLimit: dinPhysicalValueType=dinPhysicalValueType(),
                                EVSEMaximumPowerLimit_isUsed: int=0):

        struct = dinCurrentDemandResType()
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
        struct = dinTransformType()
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
                                    EAmount: dinPhysicalValueType=dinPhysicalValueType(),
                                    EVMaxVoltage: dinPhysicalValueType=dinPhysicalValueType(),
                                    EVMaxCurrent: dinPhysicalValueType=dinPhysicalValueType(),
                                    EVMinCurrent: dinPhysicalValueType=dinPhysicalValueType()):

        struct = dinAC_EVChargeParameterType()                                        
        struct.DepartureTime = DepartureTime
        struct.EAmount = EAmount
        struct.EVMaxVoltage = EVMaxVoltage
        struct.EVMaxCurrent = EVMaxCurrent
        struct.EVMinCurrent = EVMinCurrent
        return struct


    def dinX509IssuerSerialType(X509IssuerName: str="", 
                                X509SerialNumber: int=0):
        converted_x509_issuer_name = OpenV2GUtils.convert_to_array_type_characters(val=X509IssuerName, size=dinX509IssuerSerialType_X509IssuerName_CHARACTERS_SIZE)
        struct = dinX509IssuerSerialType()
        struct.X509IssuerName.characters = converted_x509_issuer_name
        struct.X509IssuerName.charactersLen = len(X509IssuerName)
        struct.X509SerialNumber = X509SerialNumber
        return struct


    def dinX509DataType(X509IssuerSerial: list[dinX509IssuerSerialType]=[dinX509IssuerSerialType()], 
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
        struct = dinX509DataType()
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
                            MeterReading: dinPhysicalValueType=dinPhysicalValueType(),
                            MeterReading_isUsed: int=0,
                            SigMeterReading: int=0,
                            SigMeterReading_isUsed: int=0,
                            MeterStatus: int=0,
                            MeterStatus_isUsed: int=0,
                            TMeter: int=0,
                            TMeter_isUsed: int=0):
        
        converted_meter_id = OpenV2GUtils.convert_to_array_type_characters(val=MeterID, size=dinMeterInfoType_MeterID_CHARACTERS_SIZE)
        converted_sig_meter_reading = OpenV2GUtils.convert_to_array_type_bytes(val=SigMeterReading, size=dinMeterInfoType_SigMeterReading_BYTES_SIZE)
        struct = dinMeterInfoType()
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
                                    EVSEMaxCurrent: dinPhysicalValueType=dinPhysicalValueType(),
                                    EVSEMaxCurrent_isUsed: int=0,
                                    MeterInfo: dinMeterInfoType=dinMeterInfoType(),
                                    MeterInfo_isUsed: int=0,
                                    ReceiptRequired: int=0,
                                    AC_EVSEStatus: dinAC_EVSEStatusType=dinAC_EVSEStatusType()):

        converted_evse_id = OpenV2GUtils.convert_to_array_type_bytes(val=EVSEID, size=dinChargingStatusResType_EVSEID_BYTES_SIZE)
        struct = dinChargingStatusResType()
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
        struct = dinDC_EVStatusType()
        struct.EVReady = EVReady 
        struct.EVCabinConditioning = EVCabinConditioning 
        struct.EVCabinConditioning_isUsed = EVCabinConditioning_isUsed
        struct.EVRESSConditioning = EVRESSConditioning
        struct.EVRESSConditioning_isUsed = EVRESSConditioning_isUsed
        struct.EVErrorCode = EVErrorCode
        struct.EVRESSSOC = EVRESSSOC        
        return struct
    
    def dinWeldingDetectionReqType(DC_EVStatus: dinDC_EVStatusType=dinDC_EVStatusType()):
        struct = dinWeldingDetectionReqType()
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
        struct = dinSignaturePropertyType()
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
                                    SignatureProperty: list[dinSignaturePropertyType]=[dinSignaturePropertyType()]):
        converted_id = OpenV2GUtils.convert_to_array_type_characters(val=Id, size=dinSignaturePropertiesType_Id_CHARACTERS_SIZE)
        struct = dinSignaturePropertiesType()
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
        struct = dinContractAuthenticationReqType()
        struct.Id.characters = converted_id
        struct.Id.charactersLen = len(Id)
        struct.Id_isUsed = Id_isUsed
        struct.GenChallenge.characters = converted_gen_challenge
        struct.GenChallenge.charactersLen = len(GenChallenge)
        struct.GenChallenge_isUsed = GenChallenge_isUsed
        return struct


    def dinDC_EVPowerDeliveryParameterType( DC_EVStatus: dinDC_EVStatusType=dinDC_EVStatusType(),
                                            BulkChargingComplete: int=0,
                                            BulkChargingComplete_isUsed: int=0,
                                            ChargingComplete: int=0):

        struct = dinDC_EVPowerDeliveryParameterType()
        struct.DC_EVStatus = DC_EVStatus
        struct.BulkChargingComplete = BulkChargingComplete
        struct.BulkChargingComplete_isUsed = BulkChargingComplete_isUsed
        struct.ChargingComplete = ChargingComplete
        return struct


    def dinEVSEChargeParameterType(noContent: int=0):
        struct = dinEVSEChargeParameterType()
        struct.noContent = noContent
        return struct


    def dinCableCheckReqType(DC_EVStatus: dinDC_EVStatusType=dinDC_EVStatusType()):
        struct = dinCableCheckReqType()
        struct.DC_EVStatus = DC_EVStatus
        return struct

    
    def dinDC_EVChargeParameterType(DC_EVStatus: dinDC_EVStatusType=dinDC_EVStatusType(),
                                    EVMaximumCurrentLimit: dinPhysicalValueType=dinPhysicalValueType(),
                                    EVMaximumPowerLimit: dinPhysicalValueType=dinPhysicalValueType(),
                                    EVMaximumPowerLimit_isUsed: int=0,
                                    EVMaximumVoltageLimit: dinPhysicalValueType=dinPhysicalValueType(),
                                    EVEnergyCapacity: dinPhysicalValueType=dinPhysicalValueType(),
                                    EVEnergyCapacity_isUsed: int=0,
                                    EVEnergyRequest: dinPhysicalValueType=dinPhysicalValueType(),
                                    EVEnergyRequest_isUsed: int=0,
                                    FullSOC: int=0,
                                    FullSOC_isUsed: int=0,
                                    BulkSOC: int=0,
                                    BulkSOC_isUsed: int=0):

        struct = dinDC_EVChargeParameterType()
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
        struct = dinRelativeTimeIntervalType()
        struct.start = start
        struct.duration = duration
        struct.duration_isUsed = duration_isUsed
        return struct


    def dinIntervalType(noContent: int=0):
        struct = dinIntervalType()
        struct.noContent = noContent
        return struct


    def dinPMaxScheduleEntryType(   TimeInterval: dinIntervalType=dinIntervalType(),
                                    TimeInterval_isUsed: int=0,
                                    RelativeTimeInterval: dinRelativeTimeIntervalType=dinRelativeTimeIntervalType(),
                                    RelativeTimeInterval_isUsed: int=0,
                                    PMax: int=0):
        struct = dinPMaxScheduleEntryType()
        struct.TimeInterval = TimeInterval
        struct.TimeInterval_isUsed = TimeInterval_isUsed
        struct.RelativeTimeInterval = RelativeTimeInterval
        struct.RelativeTimeInterval_isUsed = RelativeTimeInterval_isUsed
        struct.PMax = PMax
        return struct


    def dinPMaxScheduleType(    PMaxScheduleID: int=0,
                                PMaxScheduleEntry: list[dinPMaxScheduleEntryType]=[]):
        struct = dinPMaxScheduleType()
        struct.PMaxScheduleID = PMaxScheduleID
        for i in range(len(PMaxScheduleEntry)):
            struct.PMaxScheduleEntry.array[i] = PMaxScheduleEntry[i]
        struct.PMaxScheduleEntry.arrayLen = len(PMaxScheduleEntry)
        return struct


    def dinCostType(costKind: int=0,
                    amount: int=0,
                    amountMultiplier: int=0,
                    amountMultiplier_isUsed: int=0):
        struct = dinCostType()
        struct.costKind = costKind
        struct.amount = amount
        struct.amountMultiplier = amountMultiplier
        struct.amountMultiplier_isUsed = amountMultiplier_isUsed
        return struct


    def dinConsumptionCostType( startValue: int=0,
                                Cost: list[dinCostType]=[]):
        struct = dinConsumptionCostType()
        struct.startValue = startValue
        for i in range(len(Cost)):
            struct.Cost.array[i] = Cost[i]
        struct.Cost.arrayLen = len(Cost)
        return struct 


    def dinSalesTariffEntryType(TimeInterval: dinIntervalType=dinIntervalType(),
                                TimeInteraval_isUsed: int=0,
                                RelativeTimeInterval: dinRelativeTimeIntervalType=dinRelativeTimeIntervalType(),
                                RelativeTimeInteraval_isUsed: int=0,
                                EPriceLevel: int=0,
                                ConsumptionCost: list[dinConsumptionCostType]=[]):
        struct = dinSalesTariffEntryType()
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
                            SalesTariffEntry: list[dinSalesTariffEntryType]=[]):
        converted_id = OpenV2GUtils.convert_to_array_type_characters(val=Id, size=dinSalesTariffType_Id_CHARACTERS_SIZE)
        converted_sales_tariff_description = OpenV2GUtils.convert_to_array_type_characters(val=SalesTariffDescription, size=dinSalesTariffType_SalesTariffDescription_CHARACTERS_SIZE)
        struct = dinSalesTariffType()
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
                                PMaxSchedule: dinPMaxScheduleType=dinPMaxScheduleType(),
                                SalesTariff: dinSalesTariffType=dinSalesTariffType(),
                                SalesTariff_isUsed: int=0):
        struct = dinSAScheduleTupleType()
        struct.SAScheduleTupleID = SAScheduleTupleID
        struct.PMaxSchedule = PMaxSchedule
        struct.SalesTariff = SalesTariff
        struct.SalesTariff_isUsed = SalesTariff_isUsed
        return struct
    

    def dinSAScheduleListType(SAScheduleTuple: list[dinSAScheduleTupleType]=[]):
        struct = dinSAScheduleListType()
        for i in range(len(SAScheduleTuple)):
            struct.SAScheduleTuple.array[i] = SAScheduleTuple[i]
        struct.SAScheduleTuple.arrayLen = len(SAScheduleTuple)
        return struct        


    def dinServicePaymentSelectionReqType(  SelectedPaymentOption: int=0,
                                            SelectedServiceList: dinSelectedServiceListType=dinSelectedServiceListType()):
        struct = dinServicePaymentSelectionReqType()
        struct.SelectedPaymentOption = SelectedPaymentOption
        struct.SelectedServiceList = SelectedServiceList
        return struct 


    def dinEVStatusType(noContent: int=0):
        struct = dinEVStatusType()
        struct.noContent = noContent
        return struct


    def dinPreChargeResType(ResponseCode: int=0,
                            DC_EVSEStatus: dinDC_EVSEStatusType=dinDC_EVSEStatusType(),
                            EVSEPresentVoltage: dinPhysicalValueType=dinPhysicalValueType()):

        struct = dinPreChargeResType()
        struct.ResponseCode = ResponseCode
        struct.DC_EVSEStatus = DC_EVSEStatus
        struct.EVSEPresentVoltage = EVSEPresentVoltage
        return struct

    
    def dinDC_EVSEChargeParameterType(  DC_EVSEStatus: dinDC_EVSEStatusType=dinDC_EVSEStatusType(),
                                        EVSEMaximumCurrentLimit: dinPhysicalValueType=dinPhysicalValueType(),
                                        EVSEMaximumPowerLimit: dinPhysicalValueType=dinPhysicalValueType(),
                                        EVSEMaximumPowerLimit_isUsed: int=0,
                                        EVSEMaximumVoltageLimit: dinPhysicalValueType=dinPhysicalValueType(),
                                        EVSEMinimumCurrentLimit: dinPhysicalValueType=dinPhysicalValueType(),
                                        EVSEMinimumVoltageLimit: dinPhysicalValueType=dinPhysicalValueType(),
                                        EVSECurrentRegulationTolerance: dinPhysicalValueType=dinPhysicalValueType(),
                                        EVSECurrentRegulationTolerance_isUsed: int=0,
                                        EVSEPeakCurrentRipple: dinPhysicalValueType=dinPhysicalValueType(),
                                        EVSEEnergyToBeDelivered: dinPhysicalValueType=dinPhysicalValueType(),
                                        EVSEEnergyToBeDelivered_isUsed: int=0):

        struct = dinDC_EVSEChargeParameterType()
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
        struct = dinPaymentDetailsResType()
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

        struct = dinDSAKeyValueType()
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
        struct = dinSASchedulesType()
        struct.noContent = noContent
        return struct 

    
    def dinEVChargeParameterType(noContent: int=0):
        struct = dinEVChargeParameterType()
        struct.noContent = noContent
        return struct 


    def dinBodyBaseType(noContent: int=0):
        struct = dinBodyBaseType()
        struct.noContent = noContent
        return struct 


    def dinSubCertificatesType(Certificate: list[str]=[]):
        struct = dinSubCertificatesType()
        for i in range(len(Certificate)):
            converted_certificate = OpenV2GUtils.convert_to_array_type_bytes_str(val=Certificate[i], size=dinSubCertificatesType_Certificate_BYTES_SIZE)
            struct.Certificate.array[i].bytes = converted_certificate
            struct.Certificate.array[i].bytesLen = len(Certificate[i])
        struct.Certificate.arrayLen = len(Certificate)
        return struct



    def dinCertificateChainType(Certificate: str="",
                                SubCertificates: dinSubCertificatesType=dinSubCertificatesType(),
                                SubCertificates_isUsed: int=0):

        converted_certificate = OpenV2GUtils.convert_to_array_type_bytes_str(val=Certificate, size=dinCertificateChainType_Certificate_BYTES_SIZE)
        struct = dinCertificateChainType()
        struct.Certificate.bytes = converted_certificate
        struct.Certificate.bytesLen = len(Certificate)
        struct.SubCertificates = SubCertificates
        struct.SubCertificates_isUsed = SubCertificates_isUsed
        return struct

    def dinCertificateUpdateResType(Id: str="",
                                    ResponseCode: int=0,
                                    ContractSignatureCertChain: dinCertificateChainType=dinCertificateChainType(),
                                    ContractSignatureEncryptedPrivateKey: str="",
                                    DHParams: str="",
                                    ContractID: str="",
                                    RetryCounter: int=0):
        converted_id = OpenV2GUtils.convert_to_array_type_characters(val=Id, size=dinCertificateUpdateResType_Id_CHARACTERS_SIZE)
        converted_contract_signature_encrypted_private_key = OpenV2GUtils.convert_to_array_type_bytes_str(val=ContractSignatureEncryptedPrivateKey, size=dinCertificateUpdateResType_ContractSignatureEncryptedPrivateKey_BYTES_SIZE)
        converted_dh_params = OpenV2GUtils.convert_to_array_type_bytes_str(val=DHParams, size=dinCertificateUpdateResType_DHParams_BYTES_SIZE)
        converted_contract_id = OpenV2GUtils.convert_to_array_type_characters(val=ContractID, size=dinCertificateUpdateResType_ContractID_CHARACTERS_SIZE)
        struct = dinCertificateUpdateResType()
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
        struct = dinNotificationType()
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
        struct = dinSignatureMethodType()
        struct.Algorithm.characters = converted_algorithm
        struct.Algorithm.charactersLen = len(Algorithm)
        struct.HMACOutputLength = HMACOutputLength
        struct.HMACOutputLength_isUsed = HMACOutputLength_isUsed
        struct.ANY.characters = converted_any
        struct.ANY.charactersLen = len(ANY)
        struct.ANY_isUsed = ANY_isUsed
        return struct

    def dinTransformsType(Transform: list[dinTransformType]=[]):
        struct = dinTransformsType()
        for i in range(len(Transform)):
            struct.Transform.array[i] = Transform[i]
        struct.Transform.arrayLen = len(Transform)
        return struct

    def dinDigestMethodType(Algorithm: str="",
                            ANY: str="",
                            ANY_isUsed: int=0):

        converted_algorithm = OpenV2GUtils.convert_to_array_type_characters(val=Algorithm, size=dinDigestMethodType_Algorithm_CHARACTERS_SIZE)
        converted_any = OpenV2GUtils.convert_to_array_type_characters(val=ANY, size=dinDigestMethodType_ANY_CHARACTERS_SIZE)
        struct = dinDigestMethodType()
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
                            Transforms: dinTransformsType=dinTransformsType(),
                            Transforms_isUsed: int=0,
                            DigestMethod: dinDigestMethodType=dinDigestMethodType(),
                            DigestValue: str=""):

        converted_id = OpenV2GUtils.convert_to_array_type_characters(val=Id, size=dinReferenceType_Id_CHARACTERS_SIZE)
        converted_uri = OpenV2GUtils.convert_to_array_type_characters(val=URI, size=dinReferenceType_URI_CHARACTERS_SIZE)
        converted_type = OpenV2GUtils.convert_to_array_type_characters(val=Type, size=dinReferenceType_Type_CHARACTERS_SIZE)
        converted_digest_value = OpenV2GUtils.convert_to_array_type_bytes_str(val=DigestValue, size=dinReferenceType_DigestValue_BYTES_SIZE)
        struct = dinReferenceType()
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
                            CanonicalizationMethod: dinCanonicalizationMethodType=dinCanonicalizationMethodType(),
                            SignatureMethod: dinSignatureMethodType=dinSignatureMethodType(),
                            Reference: list[dinReferenceType]=[]):
        converted_id = OpenV2GUtils.convert_to_array_type_characters(val=Id, size=dinSignedInfoType_Id_CHARACTERS_SIZE)
        struct = dinSignedInfoType()
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
        struct = dinSignatureValueType()
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
        struct = dinRSAKeyValueType()
        struct.Modulus.bytes = converted_modulus
        struct.Modulus.bytesLen = dinRSAKeyValueType_Modulus_BYTES_SIZE
        struct.Exponent.bytes = converted_exponent
        struct.Exponent.bytesLen = dinRSAKeyValueType_Exponent_BYTES_SIZE
        return struct
        

    def dinKeyValueType(DSAKeyValue: dinDSAKeyValueType=dinDSAKeyValueType(),
                        DSAKeyValue_isUsed: int=0,
                        RSAKeyValue: dinRSAKeyValueType=dinRSAKeyValueType(),
                        RSAKeyValue_isUsed: int=0,
                        ANY: str="",
                        ANY_isUsed: int=0):
        converted_any = OpenV2GUtils.convert_to_array_type_characters(val=ANY, size=dinKeyValueType_ANY_CHARACTERS_SIZE)
        struct = dinKeyValueType()
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
                                Transforms: dinTransformsType=dinTransformsType(),
                                Transforms_isUsed: int=0):
        converted_uri = OpenV2GUtils.convert_to_array_type_characters(val=URI, size=dinRetrievalMethodType_URI_CHARACTERS_SIZE)
        converted_type = OpenV2GUtils.convert_to_array_type_characters(val=Type, size=dinRetrievalMethodType_Type_CHARACTERS_SIZE)
        struct = dinRetrievalMethodType()
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
        struct = dinPGPDataType()
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
                        KeyValue: list[dinKeyValueType]=[dinKeyValueType()],
                        RetrievalMethod: list[dinRetrievalMethodType]=[dinRetrievalMethodType()],
                        X509Data: list[dinX509DataType]=[dinX509DataType()],
                        PGPData: list[dinPGPDataType]=[dinPGPDataType()],
                        SPKIData: list[dinSPKIDataType]=[dinSPKIDataType()],
                        MgmtData: list[str]=[""],
                        ANY: str="",
                        ANY_isUsed: int=0):
        
        converted_id = OpenV2GUtils.convert_to_array_type_characters(val=Id, size=dinKeyInfoType_Id_CHARACTERS_SIZE)
        converted_key_name = OpenV2GUtils.convert_to_array_type_characters(val=KeyName[0], size=dinKeyInfoType_KeyName_CHARACTERS_SIZE)
        converted_mgmt_data = OpenV2GUtils.convert_to_array_type_characters(val=MgmtData[0], size=dinKeyInfoType_MgmtData_CHARACTERS_SIZE)
        converted_any = OpenV2GUtils.convert_to_array_type_characters(val=ANY, size=dinKeyInfoType_ANY_CHARACTERS_SIZE)
        
        struct = dinKeyInfoType()
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
        struct = dinObjectType()
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
                            SignedInfo: dinSignedInfoType=dinSignedInfoType(),
                            SignatureValue: dinSignatureValueType=dinSignatureValueType(),
                            KeyInfo: dinKeyInfoType=dinKeyInfoType(),
                            KeyInfo_isUsed: int=0,
                            Object: list[dinObjectType]=[dinObjectType()]):
        converted_id = OpenV2GUtils.convert_to_array_type_characters(val=Id, size=dinSignatureType_Id_CHARACTERS_SIZE)
        struct = dinSignatureType()
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
                                Notification: dinNotificationType=dinNotificationType(),
                                Notification_isUsed: int=0,
                                Signature: dinSignatureType=dinSignatureType(),
                                Signature_isUsed: int=0):

        converted_session_id = OpenV2GUtils.convert_to_array_type_bytes(val=SessionID, size=dinMessageHeaderType_SessionID_BYTES_SIZE)
        struct = dinMessageHeaderType()
        struct.SessionID.bytes = converted_session_id
        struct.SessionID.bytesLen = dinMessageHeaderType_SessionID_BYTES_SIZE
        struct.Notification = Notification
        struct.Notification_isUsed = Notification_isUsed
        struct.Signature = Signature
        struct.Signature_isUsed = Signature_isUsed
        return struct


    def dinAC_EVSEChargeParameterType(  AC_EVSEStatus: dinAC_EVSEStatusType=dinAC_EVSEStatusType(),
                                        EVSEMaxVoltage: dinPhysicalValueType=dinPhysicalValueType(),
                                        EVSEMaxCurrent: dinPhysicalValueType=dinPhysicalValueType(),
                                        EVSEMinCurrent: dinPhysicalValueType=dinPhysicalValueType()):
        struct = dinAC_EVSEChargeParameterType()
        struct.AC_EVSEStatus = AC_EVSEStatus
        struct.EVSEMaxVoltage = EVSEMaxVoltage
        struct.EVSEMaxCurrent = EVSEMaxCurrent
        struct.EVSEMinCurrent = EVSEMinCurrent
        return struct
        

    def dinChargeParameterDiscoveryResType( ResponseCode: int=0,
                                            EVSEProcessingType: int=0,
                                            SASchedules: dinSASchedulesType=dinSASchedulesType(),
                                            SASchedules_isUsed: int=0,
                                            SAScheduleList: dinSAScheduleListType=dinSAScheduleListType(),
                                            SAScheduleList_isUsed: int=0,
                                            EVSEChargeParameter: dinEVSEChargeParameterType=dinEVSEChargeParameterType(),
                                            EVSEChargeParameter_isUsed: int=0,
                                            AC_EVSEChargeParameter: dinAC_EVSEChargeParameterType=dinAC_EVSEChargeParameterType(),
                                            AC_EVSEChargeParameter_isUsed: int=0,
                                            DC_EVSEChargeParameter: dinDC_EVSEChargeParameterType=dinDC_EVSEChargeParameterType(),
                                            DC_EVSEChargeParameter_isUsed: int=0):
        struct = dinChargeParameterDiscoveryResType()
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
        struct = dinProfileEntryType()
        struct.ChargingProfileEntryStart = ChargingProfileEntryStart        
        struct.ChargingProfileEntryMaxPower = ChargingProfileEntryMaxPower
        return struct


    def dinChargingProfileType( SAScheduleTupleID: int=0,
                                ProfileEntry: list[dinProfileEntryType]=[]):
        struct = dinChargingProfileType()
        struct.SAScheduleTupleID = SAScheduleTupleID
        for i in range(len(ProfileEntry)):
            struct.ProfileEntry.array[i] = ProfileEntry[i]
        struct.ProfileEntry.arrayLen = len(ProfileEntry)
        return struct 

    def dinEVPowerDeliveryParameterType(noContent: int=0):
        struct = dinEVPowerDeliveryParameterType()
        struct.noContent = noContent
        return struct

    def dinPowerDeliveryReqType(ReadyToChargeState: int=0,
                                ChargingProfile: dinChargingProfileType=dinChargingProfileType(),
                                ChargingProfile_isUsed: int=0,
                                EVPowerDeliveryParameter: dinEVPowerDeliveryParameterType=dinEVPowerDeliveryParameterType(),
                                EVPowerDeliveryParameter_isUsed: int=0,
                                DC_EVPowerDeliveryParameter: dinDC_EVPowerDeliveryParameterType=dinDC_EVPowerDeliveryParameterType(),
                                DC_EVPowerDeliveryParameter_isUsed: int=0):

        struct = dinPowerDeliveryReqType()
        struct.ReadyToChargeState = ReadyToChargeState
        struct.ChargingProfile = ChargingProfile
        struct.ChargingProfile_isUsed = ChargingProfile_isUsed
        struct.EVPowerDeliveryParameter = EVPowerDeliveryParameter
        struct.EVPowerDeliveryParameter_isUsed = EVPowerDeliveryParameter_isUsed
        struct.DC_EVPowerDeliveryParameter = DC_EVPowerDeliveryParameter
        struct.DC_EVPowerDeliveryParameter_isUsed = DC_EVPowerDeliveryParameter_isUsed
        return struct


    def dinEntryType(   TimeInterval: dinIntervalType=dinIntervalType(),
                        RelativeTimeInterval: dinRelativeTimeIntervalType=dinRelativeTimeIntervalType(),
                        TimeInterval_isUsed: int=0,
                        RelativeTimeInterval_isUsed: int=0):
        
        struct = dinEntryType()
        struct.TimeInterval = TimeInterval
        struct.RelativeTimeInterval = RelativeTimeInterval
        struct.TimeInterval_isUsed = TimeInterval_isUsed
        struct.RelativeTimeInterval_isUsed = RelativeTimeInterval_isUsed
        return struct
        

    def dinSessionStopType(noContent: int=0):
        struct = dinSessionStopType()
        struct.noContent = noContent
        return struct
    

    def dinServiceDetailReqType(ServiceID: int=0):
        struct = dinServiceDetailReqType()
        struct.ServiceID = ServiceID
        return struct
        

    def dinChargingStatusReqType(noContent: int=0):
        struct = dinChargingStatusReqType()
        struct.noContent = noContent
        return struct


    def dinCertificateInstallationReqType(  Id: str="",
                                            Id_isUsed: int=0,
                                            OEMProvisioningCert: str="",
                                            ListOfRootCertificateIDs: dinListOfRootCertificateIDsType=dinListOfRootCertificateIDsType(),
                                            DHParams: str=""):
        
        converted_id = OpenV2GUtils.convert_to_array_type_characters(val=Id, size=dinCertificateInstallationReqType_Id_CHARACTERS_SIZE)
        converted_oemp_profision_cert = OpenV2GUtils.convert_to_array_type_bytes_str(val=OEMProvisioningCert, size=dinCertificateInstallationReqType_OEMProvisioningCert_BYTES_SIZE)
        converted_dh_params = OpenV2GUtils.convert_to_array_type_bytes_str(val=DHParams, size=dinCertificateInstallationReqType_DHParams_BYTES_SIZE)
        struct = dinCertificateInstallationReqType()
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
        struct = dinPaymentOptionsType()
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
        struct = dinServiceTagType()
        struct.ServiceID = ServiceID
        struct.ServiceName.characters = converted_service_name
        struct.ServiceName.charactersLen = len(ServiceName)
        struct.ServiceName_isUsed = ServiceName_isUsed
        struct.ServiceCategory= ServiceCategory
        struct.ServiceScope.characters = converted_service_scope
        struct.ServiceScope.charactersLen = len(ServiceScope)
        struct.ServiceScope_isUsed = ServiceScope_isUsed
        return struct 

    def dinServiceChargeType(   ServiceTag: dinServiceTagType=dinServiceTagType(),
                                FreeService: int=0,
                                EnergyTransferType: int=0):
        struct = dinServiceChargeType()
        struct.ServiceTag = ServiceTag
        struct.FreeService = FreeService
        struct.EnergyTransferType = EnergyTransferType
        return struct 


    def dinServiceType( ServiceTag: dinServiceTagType=dinServiceTagType(),
                        FreeService: int=0):
        struct = dinServiceType()
        struct.ServiceTag = ServiceTag
        struct.FreeService = FreeService
        return struct
        

    def dinServiceTagListType(Service: list[dinServiceType]=[]):
        struct = dinServiceTagListType()
        for i in range(len(Service)):
            struct.Service.array[i] = Service[i]
        struct.Service.arrayLen = len(Service)
        return struct


    def dinServiceDiscoveryResType( ResponseCode: int=0,
                                    PaymentOptions: dinPaymentOptionsType=dinPaymentOptionsType(),
                                    ChargeService: dinServiceChargeType=dinServiceChargeType(),
                                    ServiceList: dinServiceTagListType=dinServiceTagListType(),
                                    ServiceList_isUsed: int=0):
        struct = dinServiceDiscoveryResType()
        struct.ResponseCode = ResponseCode
        struct.PaymentOptions = PaymentOptions
        struct.ChargeService = ChargeService
        struct.ServiceList = ServiceList
        struct.ServiceList_isUsed = ServiceList_isUsed
        return struct


    def dinCurrentDemandReqType(DC_EVStatus: dinDC_EVStatusType=dinDC_EVStatusType(),
                                EVTargetCurrent: dinPhysicalValueType=dinPhysicalValueType(),
                                EVMaximumVoltageLimit: dinPhysicalValueType=dinPhysicalValueType(),
                                EVMaximumVoltageLimit_isUsed: int=0,
                                EVMaximumCurrentLimit: dinPhysicalValueType=dinPhysicalValueType(),
                                EVMaximumCurrentLimit_isUsed:int=0,
                                EVMaximumPowerimit: dinPhysicalValueType=dinPhysicalValueType(),
                                EVMaximumPowerLimit_isUsed:int=0,
                                BulkChargingComplete: int=0,
                                BulkChargingComplete_isUsed: int=0,
                                ChargingComplete: int=0,
                                RemainingTimeToFullSoC: dinPhysicalValueType=dinPhysicalValueType(),
                                RemainingTimeToFullSoC_isUsed:int=0,
                                RemainingTimeToBulkSoC: dinPhysicalValueType=dinPhysicalValueType(),
                                RemainingTimeToBulkSoC_isUsed:int=0,
                                EVTargetVoltage: dinPhysicalValueType=dinPhysicalValueType()):

        struct = dinCurrentDemandReqType()
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


    def dinPreChargeReqType(DC_EVStatus: dinDC_EVStatusType=dinDC_EVStatusType(),
                            EVTargetVoltage: dinPhysicalValueType=dinPhysicalValueType(),
                            EVTargetCurrent: dinPhysicalValueType=dinPhysicalValueType()):
        struct = dinPreChargeReqType()
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
        struct = dinSessionSetupResType()
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
        struct = dinServiceDiscoveryReqType()
        struct.ServiceScope.characters = converted_service_scope
        struct.ServiceScope.charactersLen = len(ServiceScope)
        struct.ServiceScope_isUsed = ServiceScope_isUsed
        struct.ServiceCategory = ServiceCategory
        struct.ServiceCategory_isUsed = ServiceCategory_isUsed
        return struct 

    def dinServicePaymentSelectionResType(  ResponseCode: int=0):
        struct = dinServicePaymentSelectionResType()
        struct.ResponseCode = ResponseCode
        return struct 

    def dinPaymentDetailsReqType(   ContractID: str="",
                                    ContractSignatureCertChain: dinCertificateChainType=dinCertificateChainType()):
        converted_contract_id = OpenV2GUtils.convert_to_array_type_characters(val=ContractID, size=dinPaymentDetailsReqType_ContractID_CHARACTERS_SIZE)
        struct = dinPaymentDetailsReqType()
        struct.ContractID.characters = converted_contract_id
        struct.ContractID.charactersLen = len(ContractID)
        struct.ContractSignatureCertChain = ContractSignatureCertChain
        return struct

    def dinChargeParameterDiscoveryReqType( EVRequestedEnergyTransferType: int=0,
                                            EVChargeParameter: dinEVChargeParameterType=dinEVChargeParameterType(),
                                            EVChargeParameter_isUsed: int=0,
                                            AC_EVChargeParameter: dinAC_EVChargeParameterType=dinAC_EVChargeParameterType(),
                                            AC_EVChargeParameter_isUsed: int=0,
                                            DC_EVChargeParameter: dinDC_EVChargeParameterType=dinDC_EVChargeParameterType(),
                                            DC_EVChargeParameter_isUsed: int=0):
        struct = dinChargeParameterDiscoveryReqType()
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
                                    MeterInfo: dinMeterInfoType=dinMeterInfoType()):
        converted_id = OpenV2GUtils.convert_to_array_type_characters(val=Id, size=dinMeteringReceiptReqType_Id_CHARACTERS_SIZE)
        converted_session_id = OpenV2GUtils.convert_to_array_type_bytes(val=SessionID, size=dinMeteringReceiptReqType_SessionID_BYTES_SIZE)
        struct = dinMeteringReceiptReqType()
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
                                    AC_EVSEStatus: dinAC_EVSEStatusType=dinAC_EVSEStatusType()):
        struct = dinMeteringReceiptResType()
        struct.ResponseCode = ResponseCode
        struct.AC_EVSEStatus = AC_EVSEStatus
        return struct 

    def dinSessionStopResType(  ResponseCode: int=0):
        struct = dinSessionStopResType()
        struct.ResponseCode = ResponseCode
        return struct 

    def dinCertificateUpdateReqType(Id: str="",
                                    Id_isUsed: int=0,
                                    ContractSignatureCertChain: dinCertificateChainType=dinCertificateChainType(),
                                    ContractID: str="",
                                    ListOfRootCertificateIDs: dinListOfRootCertificateIDsType=dinListOfRootCertificateIDsType(),
                                    DHParams: str=""):
        converted_id = OpenV2GUtils.convert_to_array_type_characters(val=Id, size=dinCertificateUpdateReqType_Id_CHARACTERS_SIZE)
        converted_contract_id = OpenV2GUtils.convert_to_array_type_characters(val=ContractID, size=dinCertificateUpdateReqType_ContractID_CHARACTERS_SIZE)
        converted_dh_params = OpenV2GUtils.convert_to_array_type_bytes_str(val=DHParams, size=dinCertificateUpdateReqType_DHParams_BYTES_SIZE)
        struct = dinCertificateUpdateReqType()
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
                                            ContractSignatureCertChain: dinCertificateChainType=dinCertificateChainType(),
                                            ContractSignatureEncryptedPrivateKey: str="",
                                            DHParams: str="",
                                            ContractID: str=""):
        converted_id = OpenV2GUtils.convert_to_array_type_characters(val=Id, size=dinCertificateInstallationResType_Id_CHARACTERS_SIZE)
        converted_contract_signature_encrypted_private_key = OpenV2GUtils.convert_to_array_type_bytes_str(val=ContractSignatureEncryptedPrivateKey, size=dinCertificateInstallationResType_ContractSignatureEncryptedPrivateKey_BYTES_SIZE)
        converted_dh_params = OpenV2GUtils.convert_to_array_type_bytes_str(val=DHParams, size=dinCertificateInstallationResType_DHParams_BYTES_SIZE)
        converted_contract_id = OpenV2GUtils.convert_to_array_type_characters(val=ContractID, size=dinCertificateInstallationResType_ContractID_CHARACTERS_SIZE)
        struct = dinCertificateInstallationResType()
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
                                DC_EVSEStatus: dinDC_EVSEStatusType=dinDC_EVSEStatusType(),
                                EVSEProcessing: int=0):
        struct = dinCableCheckResType()
        struct.ResponseCode = ResponseCode
        struct.DC_EVSEStatus = DC_EVSEStatus
        struct.EVSEProcessing = EVSEProcessing
        return struct 

    def dinBodyType(BodyElement: dinBodyBaseType=dinBodyBaseType(),
                    SessionSetupReq: dinSessionSetupReqType=dinSessionSetupReqType(),
                    SessionSetupRes: dinSessionSetupResType=dinSessionSetupResType(),
                    ServiceDiscoveryReq: dinServiceDiscoveryReqType=dinServiceDiscoveryReqType(),
                    ServiceDiscoveryRes: dinServiceDiscoveryResType=dinServiceDiscoveryResType(),
                    ServiceDetailReq: dinServiceDetailReqType=dinServiceDetailReqType(),
                    ServiceDetailRes: dinServiceDetailResType=dinServiceDetailResType(),
                    ServicePaymentSelectionReq: dinServicePaymentSelectionReqType=dinServicePaymentSelectionReqType(),
                    ServicePaymentSelectionRes: dinServicePaymentSelectionResType=dinServicePaymentSelectionResType(),
                    PaymentDetailsReq: dinPaymentDetailsReqType=dinPaymentDetailsReqType(),
                    PaymentDetailsRes: dinPaymentDetailsResType=dinPaymentDetailsResType(),
                    ContractAuthenticationReq: dinContractAuthenticationReqType=dinContractAuthenticationReqType(),
                    ContractAuthenticationRes: dinContractAuthenticationResType=dinContractAuthenticationResType(),
                    ChargeParameterDiscoveryReq: dinChargeParameterDiscoveryReqType=dinChargeParameterDiscoveryReqType(),
                    ChargeParameterDiscoveryRes: dinChargeParameterDiscoveryResType=dinChargeParameterDiscoveryResType(),
                    PowerDeliveryReq: dinPowerDeliveryReqType=dinPowerDeliveryReqType(),
                    PowerDeliveryRes: dinPowerDeliveryResType=dinPowerDeliveryResType(),
                    ChargingStatusReq: dinChargingStatusReqType=dinChargingStatusReqType(),
                    ChargingStatusRes: dinChargingStatusResType=dinChargingStatusResType(),
                    MeteringReceiptReq: dinMeteringReceiptReqType=dinMeteringReceiptReqType(),
                    MeteringReceiptRes: dinMeteringReceiptResType=dinMeteringReceiptResType(),
                    SessionStopReq: dinSessionStopType=dinSessionStopType(),
                    SessionStopRes: dinSessionStopResType=dinSessionStopResType(),
                    CertificateUpdateReq: dinCertificateUpdateReqType=dinCertificateUpdateReqType(),
                    CertificateUpdateRes: dinCertificateUpdateResType=dinCertificateUpdateResType(),
                    CertificateInstallationReq: dinCertificateInstallationReqType=dinCertificateInstallationReqType(),
                    CertificateInstallationRes: dinCertificateInstallationResType=dinCertificateInstallationResType(),
                    CableCheckReq: dinCableCheckReqType=dinCableCheckReqType(),
                    CableCheckRes: dinCableCheckResType=dinCableCheckResType(),
                    PreChargeReq: dinPreChargeReqType=dinPreChargeReqType(),
                    PreChargeRes: dinPreChargeResType=dinPreChargeResType(),
                    CurrentDemandReq: dinCurrentDemandReqType=dinCurrentDemandReqType(),
                    CurrentDemandRes: dinCurrentDemandResType=dinCurrentDemandResType(),
                    WeldingDetectionReq: dinWeldingDetectionReqType=dinWeldingDetectionReqType(),
                    WeldingDetectionRes: dinWeldingDetectionResType=dinWeldingDetectionResType(),
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

        struct = dinBodyType()
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


    def dinAnonType_V2G_Message(Header: dinMessageHeaderType=dinMessageHeaderType(),
                                Body: dinBodyType=dinBodyType()):
        struct = dinAnonType_V2G_Message()
        struct.Header = Header
        struct.Body = Body
        return struct

    def dinManifestType(Id: str="",
                        Id_isUsed: int=0,
                        Reference: list[dinReferenceType]=[dinReferenceType()]):
        converted_id = OpenV2GUtils.convert_to_array_type_characters(val=Id, size=dinManifestType_Id_CHARACTERS_SIZE)
        struct = dinManifestType()
        struct.Id.characters = converted_id
        struct.Id.charactersLen = len(Id)
        struct.Id_isUsed = Id_isUsed
        struct.Reference.array[0] = Reference[0]
        struct.Reference.arrayLen = dinManifestType_Reference_ARRAY_SIZE
        return struct


    def dinEXIDocument( BodyElement: dinBodyBaseType=dinBodyBaseType(),
                        V2G_Message: dinAnonType_V2G_Message=dinAnonType_V2G_Message(),
                        SignatureProperty: dinSignaturePropertyType=dinSignaturePropertyType(),
                        DSAKeyValue: dinDSAKeyValueType=dinDSAKeyValueType(),
                        SignatureProperties: dinSignaturePropertiesType=dinSignaturePropertiesType(),
                        KeyValue: dinKeyValueType=dinKeyValueType(),
                        Transforms: dinTransformsType=dinTransformsType(),
                        DigestMethod: dinDigestMethodType=dinDigestMethodType(),
                        Signature: dinSignatureType=dinSignatureType(),
                        RetrievalMethod: dinRetrievalMethodType=dinRetrievalMethodType(),
                        Manifest: dinManifestType=dinManifestType(),
                        Reference: dinReferenceType=dinReferenceType(),
                        CanonicalizationMethod: dinCanonicalizationMethodType=dinCanonicalizationMethodType(),
                        RSAKeyValue: dinRSAKeyValueType=dinRSAKeyValueType(),
                        Transform: dinTransformType=dinTransformType(),
                        PGPData: dinPGPDataType=dinPGPDataType(),
                        MgmtData: str="",
                        SignatureMethod: dinSignatureMethodType=dinSignatureMethodType(),
                        KeyInfo: dinKeyInfoType=dinKeyInfoType(),
                        SPKIData: dinSPKIDataType=dinSPKIDataType(),
                        X509Data: dinX509DataType=dinX509DataType(),
                        SignatureValue: dinSignatureValueType=dinSignatureValueType(),
                        KeyName: str="",
                        DigestValue: str="",
                        SignedInfo: dinSignedInfoType=dinSignedInfoType(),
                        Object: dinObjectType=dinObjectType(),
                        DC_EVSEStatus: dinDC_EVSEStatusType=dinDC_EVSEStatusType(),
                        RelativeTimeInterval: dinRelativeTimeIntervalType=dinRelativeTimeIntervalType(),
                        SalesTariffEntry: dinSalesTariffEntryType=dinSalesTariffEntryType(),
                        DC_EVPowerDeliveryParameter: dinDC_EVPowerDeliveryParameterType=dinDC_EVPowerDeliveryParameterType(),
                        SASchedules: dinSASchedulesType=dinSASchedulesType(),
                        AC_EVChargeParameter: dinAC_EVChargeParameterType=dinAC_EVChargeParameterType(),
                        SAScheduleList: dinSAScheduleListType=dinSAScheduleListType(),
                        DC_EVStatus: dinDC_EVStatusType=dinDC_EVStatusType(),
                        ServiceCharge: dinServiceChargeType=dinServiceChargeType(),
                        EVStatus: dinEVStatusType=dinEVStatusType(),
                        DC_EVChargeParameter: dinDC_EVChargeParameterType=dinDC_EVChargeParameterType(),
                        DC_EVSEChargeParameter: dinDC_EVSEChargeParameterType=dinDC_EVSEChargeParameterType(),
                        EVSEStatus: dinEVSEStatusType=dinEVSEStatusType(),
                        TimeInterval: dinIntervalType=dinIntervalType(),
                        EVPowerDeliveryParameter: dinEVPowerDeliveryParameterType=dinEVPowerDeliveryParameterType(),
                        EVSEChargeParameter: dinEVSEChargeParameterType=dinEVSEChargeParameterType(),
                        AC_EVSEStatus: dinAC_EVSEStatusType=dinAC_EVSEStatusType(),
                        Entry: dinEntryType=dinEntryType(),
                        AC_EVSEChargeParameter: dinAC_EVSEChargeParameterType=dinAC_EVSEChargeParameterType(),
                        PMaxScheduleEntry: dinPMaxScheduleEntryType=dinPMaxScheduleEntryType(),
                        EVChargeParameter: dinEVChargeParameterType=dinEVChargeParameterType(),
                        ServiceDiscoveryReq: dinServiceDiscoveryReqType=dinServiceDiscoveryReqType(),
                        ServiceDiscoveryRes: dinServiceDiscoveryResType=dinServiceDiscoveryResType(),
                        MeteringReceiptReq: dinMeteringReceiptReqType=dinMeteringReceiptReqType(),
                        PaymentDetailsReq: dinPaymentDetailsReqType=dinPaymentDetailsReqType(),
                        MeteringReceiptRes: dinMeteringReceiptResType=dinMeteringReceiptResType(),
                        PaymentDetailsRes: dinPaymentDetailsResType=dinPaymentDetailsResType(),
                        SessionSetupReq: dinSessionSetupReqType=dinSessionSetupReqType(),
                        SessionSetupRes: dinSessionSetupResType=dinSessionSetupResType(),
                        CableCheckReq: dinCableCheckReqType=dinCableCheckReqType(),
                        CableCheckRes: dinCableCheckResType=dinCableCheckResType(),
                        ContractAuthenticationReq: dinContractAuthenticationReqType=dinContractAuthenticationReqType(),
                        CertificateInstallationReq: dinCertificateInstallationReqType=dinCertificateInstallationReqType(),
                        ContractAuthenticationRes: dinContractAuthenticationResType=dinContractAuthenticationResType(),
                        CertificateInstallationRes: dinCertificateInstallationResType=dinCertificateInstallationResType(),
                        WeldingDetectionReq: dinWeldingDetectionReqType=dinWeldingDetectionReqType(),
                        WeldingDetectionRes: dinWeldingDetectionResType=dinWeldingDetectionResType(),
                        CertificateUpdateReq: dinCertificateUpdateReqType=dinCertificateUpdateReqType(),
                        CertificateUpdateRes: dinCertificateUpdateResType=dinCertificateUpdateResType(),
                        PowerDeliveryReq: dinPowerDeliveryReqType=dinPowerDeliveryReqType(),
                        PowerDeliveryRes: dinPowerDeliveryResType=dinPowerDeliveryResType(),
                        ChargingStatusReq: dinChargingStatusReqType=dinChargingStatusReqType(),
                        ChargingStatusRes: dinChargingStatusResType=dinChargingStatusResType(),
                        CurrentDemandReq: dinCurrentDemandReqType=dinCurrentDemandReqType(),
                        PreChargeReq: dinPreChargeReqType=dinPreChargeReqType(),
                        CurrentDemandRes: dinCurrentDemandResType=dinCurrentDemandResType(),
                        PreChargeRes: dinPreChargeResType=dinPreChargeResType(),
                        ServicePaymentSelectionReq: dinServicePaymentSelectionReqType=dinServicePaymentSelectionReqType(),
                        SessionStopReq: dinSessionStopType=dinSessionStopType(),
                        ServicePaymentSelectionRes: dinServicePaymentSelectionResType=dinServicePaymentSelectionResType(),
                        SessionStopRes: dinSessionStopResType=dinSessionStopResType(),
                        ChargeParameterDiscoveryReq: dinChargeParameterDiscoveryReqType=dinChargeParameterDiscoveryReqType(),
                        ChargeParameterDiscoveryRes: dinChargeParameterDiscoveryResType=dinChargeParameterDiscoveryResType(),
                        ServiceDetailReq: dinServiceDetailReqType=dinServiceDetailReqType(),
                        ServiceDetailRes: dinServiceDetailResType=dinServiceDetailResType(),
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
        struct = dinEXIDocument()
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


    # --------------------- ISO1 ---------------------
    def iso1EVChargeParameterType(  DepartureTime: int=0,
                                    DepartureTime_isUsed: int=0):
        struct = iso1EVChargeParameterType()
        struct.DepartureTime = DepartureTime
        struct.DepartureTime_isUsed = DepartureTime_isUsed
        return struct

    
    def iso1DiffieHellmanPublickeyType( Id: str="",
                                        CONTENT: str=""):
        converted_id = OpenV2GUtils.convert_to_array_type_characters(val=Id, size=iso1DiffieHellmanPublickeyType_Id_CHARACTERS_SIZE)
        converted_content = OpenV2GUtils.convert_to_array_type_bytes_str(val=CONTENT, size=iso1DiffieHellmanPublickeyType_CONTENT_BYTES_SIZE)
        struct = iso1DiffieHellmanPublickeyType()
        struct.Id.characters = converted_id
        struct.Id.charactersLen = len(Id)
        struct.CONTENT.bytes = converted_content
        struct.CONTENT.bytesLen = iso1DiffieHellmanPublickeyType_CONTENT_BYTES_SIZE
        return struct


    def iso1SASchedulesType(noContent: int=0):
        struct = iso1SASchedulesType()
        struct.noContent = noContent
        return struct


    def iso1ServiceDetailReqType(   ServiceID: int=0):
        struct = iso1ServiceDetailReqType()
        struct.ServiceID = ServiceID
        return struct


    def iso1RelativeTimeIntervalType(   start: int=0,
                                        duration: int=0,
                                        duration_isUsed: int=0):
        struct = iso1RelativeTimeIntervalType()
        struct.start = start
        struct.duration = duration
        struct.duration_isUsed = duration_isUsed
        return struct


    def iso1EMAIDType(  Id: str="",
                        CONTENT: str=""):
        converted_id = OpenV2GUtils.convert_to_array_type_characters(val=Id, size=iso1EMAIDType_Id_CHARACTERS_SIZE)
        converted_content = OpenV2GUtils.convert_to_array_type_characters(val=CONTENT, size=iso1EMAIDType_CONTENT_CHARACTERS_SIZE)
        struct = iso1EMAIDType()
        struct.Id.characters = converted_id
        struct.Id.charactersLen = len(Id)
        struct.CONTENT.characters = converted_content
        struct.CONTENT.charactersLen = iso1EMAIDType_CONTENT_CHARACTERS_SIZE
        return struct


    def iso1EVStatusType(noContent: int=0):
        struct = iso1EVStatusType()
        struct.noContent = noContent
        return struct


    def iso1EVSEChargeParameterType(noContent: int=0):
        struct = iso1EVSEChargeParameterType()
        struct.noContent = noContent
        return struct


    def iso1EVPowerDeliveryParameterType(noContent: int=0):
        struct = iso1EVPowerDeliveryParameterType()
        struct.noContent = noContent
        return struct


    def iso1AuthorizationReqType(   Id: str="",
                                    Id_isUsed: int=0,
                                    GenChallenge: str="",
                                    GenChallenge_isUsed: int=0):
        converted_id = OpenV2GUtils.convert_to_array_type_characters(val=Id, size=iso1AuthorizationReqType_Id_CHARACTERS_SIZE)
        converted_gen_challenge = OpenV2GUtils.convert_to_array_type_bytes_str(val=GenChallenge, size=iso1AuthorizationReqType_GenChallenge_BYTES_SIZE)
        struct = iso1AuthorizationReqType()
        struct.Id.characters = converted_id
        struct.Id.charactersLen = len(Id)
        struct.Id_isUsed = Id_isUsed
        struct.GenChallenge.bytes = converted_gen_challenge
        struct.GenChallenge.bytesLen = iso1AuthorizationReqType_GenChallenge_BYTES_SIZE
        struct.GenChallenge_isUsed = GenChallenge_isUsed
        return struct


    def iso1MeterInfoType(  MeterID: str="",
                            MeterReading: int=0,
                            MeterReading_isUsed: int=0,
                            SigMeterReading: int=0,
                            SigMeterReading_isUsed: int=0,
                            MeterStatus: int=0,
                            MeterStatus_isUsed: int=0,
                            TMeter: int=0,
                            TMeter_isUsed: int=0):
        
        converted_meter_id = OpenV2GUtils.convert_to_array_type_characters(val=MeterID, size=iso1MeterInfoType_MeterID_CHARACTERS_SIZE)
        converted_sig_meter_reading = OpenV2GUtils.convert_to_array_type_bytes(val=SigMeterReading, size=iso1MeterInfoType_SigMeterReading_BYTES_SIZE)
        struct = iso1MeterInfoType()
        struct.MeterID.characters = converted_meter_id
        struct.MeterID.charactersLen = len(MeterID)
        struct.MeterReading = MeterReading
        struct.MeterReading_isUsed = MeterReading_isUsed
        struct.SigMeterReading.bytes = converted_sig_meter_reading
        struct.SigMeterReading.bytesLen = iso1MeterInfoType_SigMeterReading_BYTES_SIZE
        struct.SigMeterReading_isUsed = SigMeterReading_isUsed
        struct.MeterStatus = MeterStatus
        struct.MeterStatus_isUsed = MeterStatus_isUsed
        struct.TMeter = TMeter
        struct.TMeter_isUsed = TMeter_isUsed
        return struct


    def iso1ObjectType( Id: str="",
                        Id_isUsed: int=0,
                        MimeType: str="",
                        MimeType_isUsed=0,
                        Encoding: str="",
                        Encoding_isUsed: int=0,
                        ANY: str="",
                        ANY_isUsed: int=0):
        converted_id = OpenV2GUtils.convert_to_array_type_characters(val=Id, size=iso1ObjectType_Id_CHARACTERS_SIZE)
        converted_mime_type = OpenV2GUtils.convert_to_array_type_characters(val=MimeType, size=iso1ObjectType_MimeType_CHARACTERS_SIZE)
        converted_encoding = OpenV2GUtils.convert_to_array_type_characters(val=Encoding, size=iso1ObjectType_Encoding_CHARACTERS_SIZE)
        converted_any = OpenV2GUtils.convert_to_array_type_characters(val=ANY, size=iso1ObjectType_ANY_CHARACTERS_SIZE)
        struct = iso1ObjectType()
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


    def iso1RSAKeyValueType(Modulus: int=0,
                            Exponent: int=0):
        converted_modulus = OpenV2GUtils.convert_to_array_type_bytes(val=Modulus, size=iso1RSAKeyValueType_Modulus_BYTES_SIZE)
        converted_exponent = OpenV2GUtils.convert_to_array_type_bytes(val=Exponent, size=iso1RSAKeyValueType_Exponent_BYTES_SIZE)
        struct = iso1RSAKeyValueType()
        struct.Modulus.bytes = converted_modulus
        struct.Modulus.bytesLen = iso1RSAKeyValueType_Modulus_BYTES_SIZE
        struct.Exponent.bytes = converted_exponent
        struct.Exponent.bytesLen = iso1RSAKeyValueType_Exponent_BYTES_SIZE
        return struct


    def iso1SessionStopResType( ResponseCode: int=0):
        struct = iso1SessionStopResType()
        struct.ResponseCode = ResponseCode
        return struct

    
    def iso1SignatureValueType( Id: str="",
                                Id_isUsed: int=0,
                                CONTENT: str=""):
        converted_id = OpenV2GUtils.convert_to_array_type_characters(val=Id, size=iso1SignatureValueType_Id_CHARACTERS_SIZE)
        converted_content = OpenV2GUtils.convert_to_array_type_bytes_str(val=CONTENT, size=iso1SignatureValueType_CONTENT_BYTES_SIZE)
        struct = iso1SignatureValueType()
        struct.Id.characters = converted_id
        struct.Id.charactersLen = len(Id)
        struct.Id_isUsed = Id_isUsed
        struct.CONTENT.bytes = converted_content
        struct.CONTENT.bytesLen = len(CONTENT)
        return struct


    def iso1SubCertificatesType(Certificate: list[str]=[]):
        struct = iso1SubCertificatesType()
        for i in range(len(Certificate)):
            converted_certificate = OpenV2GUtils.convert_to_array_type_bytes_str(val=Certificate[i], size=iso1SubCertificatesType_Certificate_BYTES_SIZE)
            struct.Certificate.array[i].bytes = converted_certificate
            struct.Certificate.array[i].bytesLen = len(Certificate[i])
        struct.Certificate.arrayLen = len(Certificate)
        return struct


    def iso1DSAKeyValueType(P: int=0,
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

        struct = iso1DSAKeyValueType()
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

    
    def iso1IntervalType(noContent: int=0):
        struct = iso1IntervalType()
        struct.noContent = noContent
        return struct 


    def iso1MeteringReceiptReqType( Id: str="",
                                    Id_isUsed: int=0,
                                    SessionID: int=0,
                                    SAScheduleTupleID: int=0,
                                    SAScheduleTupleID_isUsed: int=0,
                                    MeterInfo: iso1MeterInfoType=iso1MeterInfoType()):
        converted_id = OpenV2GUtils.convert_to_array_type_characters(val=Id, size=iso1MeteringReceiptReqType_Id_CHARACTERS_SIZE)
        converted_session_id = OpenV2GUtils.convert_to_array_type_bytes(val=SessionID, size=iso1MeteringReceiptReqType_SessionID_BYTES_SIZE)
        struct = iso1MeteringReceiptReqType()
        struct.Id.characters = converted_id
        struct.Id.charactersLen = len(Id)
        struct.Id_isUsed = Id_isUsed
        struct.SessionID.bytes = converted_session_id
        struct.SessionID.bytesLen = dinMeteringReceiptReqType_SessionID_BYTES_SIZE
        struct.SAScheduleTupleID = SAScheduleTupleID
        struct.SAScheduleTupleID_isUsed = SAScheduleTupleID_isUsed
        struct.MeterInfo = MeterInfo
        return struct 


    def iso1KeyValueType(DSAKeyValue: iso1DSAKeyValueType=iso1DSAKeyValueType(),
                        DSAKeyValue_isUsed: int=0,
                        RSAKeyValue: iso1RSAKeyValueType=iso1RSAKeyValueType(),
                        RSAKeyValue_isUsed: int=0,
                        ANY: str="",
                        ANY_isUsed: int=0):
        converted_any = OpenV2GUtils.convert_to_array_type_characters(val=ANY, size=iso1KeyValueType_ANY_CHARACTERS_SIZE)
        struct = iso1KeyValueType()
        struct.DSAKeyValue = DSAKeyValue
        struct.DSAKeyValue_isUsed = DSAKeyValue_isUsed
        struct.RSAKeyValue = RSAKeyValue
        struct.RSAKeyValue_isUsed = RSAKeyValue_isUsed
        struct.ANY.characters = converted_any
        struct.ANY.charactersLen = len(ANY)
        struct.ANY_isUsed = ANY_isUsed
        return struct


    def iso1X509IssuerSerialType(   X509IssuerName: str="", 
                                    X509SerialNumber: int=0):
        converted_x509_issuer_name = OpenV2GUtils.convert_to_array_type_characters(val=X509IssuerName, size=iso1X509IssuerSerialType_X509IssuerName_CHARACTERS_SIZE)
        struct = iso1X509IssuerSerialType()
        struct.X509IssuerName.characters = converted_x509_issuer_name
        struct.X509IssuerName.charactersLen = len(X509IssuerName)
        struct.X509SerialNumber = X509SerialNumber
        return struct


    def iso1EVSEStatusType( NotificationMaxDelay: int=0,
                            EVSENotification: int=0):
        struct = iso1EVSEStatusType()
        struct.NotificationMaxDelay = NotificationMaxDelay
        struct.EVSENotification = EVSENotification
        return struct


    def iso1SignatureMethodType(Algorithm: str="",
                                HMACOutputLength: int=0,
                                HMACOutputLength_isUsed: int=0,
                                ANY: str="",
                                ANY_isUsed: int=0):
        converted_algorithm = OpenV2GUtils.convert_to_array_type_characters(val=Algorithm, size=iso1SignatureMethodType_Algorithm_CHARACTERS_SIZE)    
        converted_any = OpenV2GUtils.convert_to_array_type_characters(val=ANY, size=iso1SignatureMethodType_ANY_CHARACTERS_SIZE)
        struct = iso1SignatureMethodType()
        struct.Algorithm.characters = converted_algorithm
        struct.Algorithm.charactersLen = len(Algorithm)
        struct.HMACOutputLength = HMACOutputLength
        struct.HMACOutputLength_isUsed = HMACOutputLength_isUsed
        struct.ANY.characters = converted_any
        struct.ANY.charactersLen = len(ANY)
        struct.ANY_isUsed = ANY_isUsed
        return struct


    def iso1X509DataType(X509IssuerSerial: list[iso1X509IssuerSerialType]=[iso1X509IssuerSerialType()], 
                        X509SKI: int=0, 
                        X509SubjectName: str="", 
                        X509Certificate: int=0,
                        X509CRL: int=0,
                        ANY: str="",
                        ANY_isUsed: int=0):

        converted_any = OpenV2GUtils.convert_to_array_type_characters(val=ANY, size=iso1X509DataType_ANY_CHARACTERS_SIZE)
        converted_x509_subject_name = OpenV2GUtils.convert_to_array_type_characters(val=X509SubjectName, size=iso1X509DataType_X509SubjectName_CHARACTERS_SIZE)
        converted_x509_ski = OpenV2GUtils.convert_to_array_type_bytes(val=X509SKI, size=iso1X509DataType_X509SKI_BYTES_SIZE)
        converted_x509_certificate = OpenV2GUtils.convert_to_array_type_bytes(val=X509Certificate, size=dinX509DataType_X509Certificate_BYTES_SIZE)
        converted_x509_crl = OpenV2GUtils.convert_to_array_type_bytes(val=X509CRL, size=iso1X509DataType_X509CRL_BYTES_SIZE)
        struct = iso1X509DataType()
        struct.X509IssuerSerial.array[0] = X509IssuerSerial[0]
        struct.X509IssuerSerial.arrayLen = iso1X509DataType_X509IssuerSerial_ARRAY_SIZE
        struct.X509SKI.array[0].bytes = converted_x509_ski
        struct.X509SKI.array[0].bytesLen = iso1X509DataType_X509SKI_BYTES_SIZE
        struct.X509SKI.arrayLen = iso1X509DataType_X509SKI_ARRAY_SIZE
        struct.X509SubjectName.array[0].characters = converted_x509_subject_name
        struct.X509SubjectName.array[0].charactersLen = len(X509SubjectName)
        struct.X509SubjectName.arrayLen = iso1X509DataType_X509SubjectName_ARRAY_SIZE
        struct.X509Certificate.array[0].bytes = converted_x509_certificate
        struct.X509Certificate.array[0].bytesLen = iso1X509DataType_X509Certificate_BYTES_SIZE
        struct.X509Certificate.arrayLen = iso1X509DataType_X509Certificate_ARRAY_SIZE
        struct.X509CRL.array[0].bytes = converted_x509_crl
        struct.X509CRL.array[0].bytesLen = iso1X509DataType_X509CRL_BYTES_SIZE
        struct.X509CRL.arrayLen = iso1X509DataType_X509CRL_ARRAY_SIZE
        struct.ANY.characters = converted_any
        struct.ANY.charactersLen = len(ANY)
        struct.ANY_isUsed = ANY_isUsed
        return struct


    def iso1NotificationType(FaultCode: int=0,
                            FaultMsg: str="",
                            FaultMsg_isUsed: int=0):
        converted_fault_msg = OpenV2GUtils.convert_to_array_type_characters(val=FaultMsg, size=iso1NotificationType_FaultMsg_CHARACTERS_SIZE)
        struct = iso1NotificationType()
        struct.FaultCode = FaultCode
        struct.FaultMsg.characters = converted_fault_msg
        struct.FaultMsg.charactersLen = len(FaultMsg)
        struct.FaultMsg_isUsed = FaultMsg_isUsed
        return struct


    def iso1TransformType(  Algorithm: str="", 
                            ANY: str="", 
                            ANY_isUsed: int=0, 
                            XPath: str=""):
        converted_algorithm = OpenV2GUtils.convert_to_array_type_characters(val=Algorithm, size=iso1TransformType_Algorithm_CHARACTERS_SIZE)
        converted_any = OpenV2GUtils.convert_to_array_type_characters(val=ANY, size=iso1TransformType_ANY_CHARACTERS_SIZE)
        converted_xpath = OpenV2GUtils.convert_to_array_type_characters(val=XPath, size=iso1TransformType_XPath_CHARACTERS_SIZE)
        struct = iso1TransformType()
        struct.Algorithm.characters = converted_algorithm
        struct.Algorithm.charactersLen = len(Algorithm)
        struct.ANY.characters = converted_any
        struct.ANY.charactersLen = len(ANY)
        struct.ANY_isUsed = ANY_isUsed
        struct.XPath.array[0].characters = converted_xpath
        struct.XPath.array[0].charactersLen = len(XPath)
        struct.XPath.arrayLen = iso1TransformType_XPath_ARRAY_SIZE
        return struct

    
    def iso1PaymentDetailsResType(  ResponseCode: int=0,
                                    GenChallenge: str="",
                                    EVSETimeStamp: int=0):
        converted_gen_challenge = OpenV2GUtils.convert_to_array_type_bytes_str(val=GenChallenge, size=iso1PaymentDetailsResType_GenChallenge_BYTES_SIZE)
        struct = iso1PaymentDetailsResType()
        struct.ResponseCode = ResponseCode
        struct.GenChallenge.bytes = converted_gen_challenge
        struct.GenChallenge.bytesLen = len(GenChallenge)
        struct.EVSETimeStamp = EVSETimeStamp
        return struct 


    def iso1ContractSignatureEncryptedPrivateKeyType(   Id: str="",
                                                        CONTENT: str=""):
        converted_id = OpenV2GUtils.convert_to_array_type_characters(val=Id, size=iso1ContractSignatureEncryptedPrivateKeyType_Id_CHARACTERS_SIZE)
        converted_content = OpenV2GUtils.convert_to_array_type_bytes_str(val=CONTENT, size=iso1ContractSignatureEncryptedPrivateKeyType_CONTENT_BYTES_SIZE)
        struct = iso1ContractSignatureEncryptedPrivateKeyType()
        struct.Id.characters = converted_id
        struct.Id.charactersLen = len(converted_id)
        struct.CONTENT.bytes = converted_content
        struct.CONTENT.bytesLen = iso1ContractSignatureEncryptedPrivateKeyType_CONTENT_BYTES_SIZE
        return struct


    def iso1SPKIDataType(   SPKISexp: int=0, 
                            ANY: str="", 
                            ANY_isUsed: int=0):
        converted_any = OpenV2GUtils.convert_to_array_type_characters(val=ANY, size=iso1SPKIDataType_ANY_CHARACTERS_SIZE)
        converted_spki_exp = OpenV2GUtils.convert_to_array_type_bytes(val=SPKISexp, size=iso1SPKIDataType_SPKISexp_BYTES_SIZE)
        struct = iso1SPKIDataType()
        struct.SPKISexp.array[0].bytes =  converted_spki_exp
        struct.SPKISexp.array[0].bytesLen = dinSPKIDataType_SPKISexp_BYTES_SIZE
        struct.SPKISexp.arrayLen = dinSPKIDataType_SPKISexp_ARRAY_SIZE
        struct.ANY.characters = converted_any
        struct.ANY.charactersLen = len(ANY)
        struct.ANY_isUsed = ANY_isUsed
        return struct    


    def iso1SessionStopReqType( ChargingSession: int=0):
        struct = iso1SessionStopReqType()
        struct.ChargingSession = ChargingSession
        return struct


    def iso1EntryType(  TimeInterval: iso1IntervalType=iso1IntervalType(),
                        RelativeTimeInterval: iso1RelativeTimeIntervalType=iso1RelativeTimeIntervalType(),
                        TimeInterval_isUsed: int=0,
                        RelativeTimeInterval_isUsed: int=0):
        
        struct = iso1EntryType()
        struct.TimeInterval = TimeInterval
        struct.RelativeTimeInterval = RelativeTimeInterval
        struct.TimeInterval_isUsed = TimeInterval_isUsed
        struct.RelativeTimeInterval_isUsed = RelativeTimeInterval_isUsed
        return struct


    def iso1SessionSetupReqType( EVCCID: int=0):
        struct = iso1SessionSetupReqType()
        struct.EVCCID.bytes = OpenV2GUtils.convert_to_array_type_bytes(EVCCID, size=iso1SessionSetupReqType_EVCCID_BYTES_SIZE)
        struct.EVCCID.bytesLen = iso1SessionSetupReqType_EVCCID_BYTES_SIZE
        return struct


    def iso1CanonicalizationMethodType( Algorithm: str="", 
                                        ANY: str="", 
                                        ANY_isUsed: int=0):
        converted_algorithm = OpenV2GUtils.convert_to_array_type_characters(val=Algorithm, size=iso1CanonicalizationMethodType_Algorithm_CHARACTERS_SIZE)
        converted_any = OpenV2GUtils.convert_to_array_type_characters(val=ANY, size=iso1CanonicalizationMethodType_ANY_CHARACTERS_SIZE)
        struct = iso1CanonicalizationMethodType()
        struct.Algorithm.characters = converted_algorithm
        struct.Algorithm.charactersLen = len(Algorithm)
        struct.ANY.characters = converted_any
        struct.ANY.charactersLen = len(ANY)
        struct.ANY_isUsed = ANY_isUsed
        return struct


    def iso1DC_EVStatusType(EVReady: int=0,
                            EVErrorCode: int=0,
                            EVRESSSOC: int=0):
        struct = iso1DC_EVStatusType()
        struct.EVReady = EVReady
        struct.EVErrorCode = EVErrorCode
        struct.EVRESSSOC = EVRESSSOC
        return struct

    
    def iso1ServiceType(ServiceID: int=0,
                        ServiceName: str="",
                        ServiceName_isUsed: int=0,
                        ServiceCategory: int=0,
                        ServiceScope: str="",
                        ServiceScope_isUsed: int=0,
                        FreeService: int=0):
        converted_service_name = OpenV2GUtils.convert_to_array_type_characters(val=ServiceName, size=iso1ServiceType_ServiceName_CHARACTERS_SIZE)
        converted_service_scope = OpenV2GUtils.convert_to_array_type_characters(val=ServiceScope, size=iso1ServiceType_ServiceScope_CHARACTERS_SIZE)
        struct = iso1ServiceType()
        struct.ServiceID = ServiceID
        struct.ServiceName.characters = converted_service_name
        struct.ServiceName.charactersLen = len(ServiceName)
        struct.ServiceName_isUsed = ServiceName_isUsed
        struct.ServiceCategory = ServiceCategory
        struct.ServiceScope.characters = converted_service_scope
        struct.ServiceScope.charactersLen = len(ServiceScope)
        struct.ServiceScope_isUsed = ServiceScope_isUsed
        struct.FreeService = FreeService
        return struct


    def iso1ServiceDiscoveryReqType(ServiceScope: str="",
                                    ServiceScope_isUsed: int=0,
                                    ServiceCategory: int=0,
                                    ServiceCategory_isUsed: int=0):
        converted_service_scope = OpenV2GUtils.convert_to_array_type_characters(val=ServiceScope, size=iso1ServiceDiscoveryReqType_ServiceScope_CHARACTERS_SIZE)
        struct = iso1ServiceDiscoveryReqType()
        struct.ServiceScope.characters = converted_service_scope
        struct.ServiceScope.charactersLen = len(ServiceScope)
        struct.ServiceScope_isUsed = ServiceScope_isUsed
        struct.ServiceCategory = ServiceCategory
        struct.ServiceCategory_isUsed = ServiceCategory_isUsed
        return struct


    def iso1CableCheckReqType(  DC_EVStatus: iso1DC_EVStatusType=iso1DC_EVStatusType()):
        struct = iso1CableCheckReqType()
        struct.DC_EVStatus = DC_EVStatus
        return struct


    def iso1SelectedServiceType(ServiceID: int=0,
                                ParameterSetID: int=0,
                                ParameterSetID_isUsed: int=0):
        struct = iso1SelectedServiceType()
        struct.ServiceID = ServiceID
        struct.ParameterSetID = ParameterSetID    
        struct.ParameterSetID_isUsed = ParameterSetID_isUsed
        return struct


    def iso1AC_EVSEStatusType(  NotificationMaxDelay: int=0,
                                EVSENotification: int=0,
                                RCD: int=0):
        struct = iso1AC_EVSEStatusType()
        struct.NotificationMaxDelay = NotificationMaxDelay
        struct.EVSENotification = EVSENotification
        struct.RCD = RCD
        return struct


    def iso1BodyBaseType(noContent: int=0):
        struct = iso1BodyBaseType()
        struct.noContent = noContent
        return struct


    def iso1SupportedEnergyTransferModeType(EnergyTransferMode: list[int]=[]):
        struct = iso1SupportedEnergyTransferModeType()
        for i in range(len(EnergyTransferMode)):
            struct.EnergyTransferMode.array[i] = EnergyTransferMode[i]
        struct.EnergyTransferMode.arrayLen = len(EnergyTransferMode)
        return struct


    def iso1ChargingStatusReqType(noContent: int=0):
        struct = iso1ChargingStatusReqType()
        struct.noContent = noContent
        return struct


    def iso1PaymentServiceSelectionResType(ResponseCode: int=0):
        struct = iso1PaymentServiceSelectionResType()
        struct.ResponseCode = ResponseCode
        return struct

    
    def iso1DigestMethodType(   Algorithm: str="",
                                ANY: str="",
                                ANY_isUsed: int=0):

        converted_algorithm = OpenV2GUtils.convert_to_array_type_characters(val=Algorithm, size=iso1DigestMethodType_Algorithm_CHARACTERS_SIZE)
        converted_any = OpenV2GUtils.convert_to_array_type_characters(val=ANY, size=iso1DigestMethodType_ANY_CHARACTERS_SIZE)
        struct = iso1DigestMethodType()
        struct.Algorithm.characters = converted_algorithm
        struct.Algorithm.charactersLen = len(Algorithm)
        struct.ANY.characters = converted_any
        struct.ANY.charactersLen = len(ANY)
        struct.ANY_isUsed = ANY_isUsed
        return struct


    def iso1SignaturePropertyType(  Target: str="", 
                                    Id: str="", 
                                    Id_isUsed: int=0, 
                                    ANY: str="", 
                                    ANY_isUsed: int=0):
        converted_type = OpenV2GUtils.convert_to_array_type_characters(val=Target, size=iso1SignaturePropertyType_Target_CHARACTERS_SIZE)
        converted_id = OpenV2GUtils.convert_to_array_type_characters(val=Id, size=iso1SignaturePropertyType_Id_CHARACTERS_SIZE)
        converted_any = OpenV2GUtils.convert_to_array_type_characters(val=ANY, size=iso1SignaturePropertyType_ANY_CHARACTERS_SIZE)
        struct = iso1SignaturePropertyType()
        struct.Target.characters = converted_type
        struct.Target.charactersLen = len(Target)
        struct.Id.characters = converted_id
        struct.Id.charactersLen = len(Id)
        struct.Id_isUsed = Id_isUsed
        struct.ANY.characters = converted_any
        struct.ANY.charactersLen = len(ANY)
        struct.ANY_isUsed = ANY_isUsed
        return struct


    def iso1PGPDataType(PGPKeyID: str="",
                        PGPKeyID_isUsed: int=0,
                        PGPKeyPacket: str="",
                        PGPKeyPacket_isUsed: int=0,
                        ANY: str="",
                        ANY_isUsed: int=0):
        converted_pgp_key_id = OpenV2GUtils.convert_to_array_type_bytes_str(val=PGPKeyID, size=iso1PGPDataType_PGPKeyID_BYTES_SIZE)
        converted_pgp_key_packet = OpenV2GUtils.convert_to_array_type_bytes_str(val=PGPKeyPacket, size=iso1PGPDataType_PGPKeyPacket_BYTES_SIZE)
        converted_any = OpenV2GUtils.convert_to_array_type_characters(val=ANY, size=iso1PGPDataType_ANY_CHARACTERS_SIZE)
        struct = iso1PGPDataType()
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


    def iso1SessionSetupResType( ResponseCode: int=0,
                                EVSEID: str="",
                                EVSETimeStamp: int=0,
                                EVSETimeStamp_isUsed: int=0):
        converted_evse_id = OpenV2GUtils.convert_to_array_type_characters(val=EVSEID, size=iso1SessionSetupResType_EVSEID_CHARACTERS_SIZE)
        struct = iso1SessionSetupResType()
        struct.ResponseCode = ResponseCode
        struct.EVSEID.characters = converted_evse_id
        struct.EVSEID.charactersLen = len(EVSEID)
        struct.EVSETimeStamp = EVSETimeStamp
        struct.EVSETimeStamp_isUsed = EVSETimeStamp_isUsed
        return struct


    def iso1CertificateChainType(   Id: str="",
                                    Id_isUsed: int=0,
                                    Certificate: str="",
                                    SubCertificates: iso1SubCertificatesType=iso1SubCertificatesType(),
                                    SubCertificates_isUsed: int=0):

        converted_id = OpenV2GUtils.convert_to_array_type_characters(val=Id, size=iso1CertificateChainType_Id_CHARACTERS_SIZE)
        converted_certificate = OpenV2GUtils.convert_to_array_type_bytes_str(val=Certificate, size=iso1CertificateChainType_Certificate_BYTES_SIZE)
        struct = iso1CertificateChainType()
        struct.Id.characters = converted_id
        struct.Id.charactersLen = len(Id)
        struct.Id_isUsed = Id_isUsed
        struct.Certificate.bytes = converted_certificate
        struct.Certificate.bytesLen = iso1CertificateChainType_Certificate_BYTES_SIZE
        struct.SubCertificates = SubCertificates
        struct.SubCertificates_isUsed = SubCertificates_isUsed
        return struct


    def iso1DC_EVSEStatusType(  NotificationMaxDelay: int=0,
                                EVSENotification: int=0,
                                EVSEIsolationStatus: int=0,
                                EVSEIsolationStatus_isUsed: int=0,
                                EVSEStatusCode: int=0):
        struct = iso1DC_EVSEStatusType()
        struct.NotificationMaxDelay = NotificationMaxDelay
        struct.EVSENotification = EVSENotification
        struct.EVSEIsolationStatus = EVSEIsolationStatus
        struct.EVSEIsolationStatus_isUsed = EVSEIsolationStatus_isUsed
        struct.EVSEStatusCode = EVSEStatusCode
        return struct


    def iso1ServiceListType(Service: list[iso1ServiceType]=[]):
        struct = iso1ServiceListType()
        for i in range(len(Service)):
            struct.Service.array[i] = Service[i]
        struct.Service.arrayLen = len(Service)
        return struct 
        

    def iso1PowerDeliveryResType(   ResponseCode: int=0, 
                                    EVSEStatus: iso1EVSEStatusType=iso1EVSEStatusType(), 
                                    EVSEStatus_isUsed: int=0, 
                                    AC_EVSEStatus: iso1AC_EVSEStatusType=iso1AC_EVSEStatusType(), 
                                    AC_EVSEStatus_isUsed: int=0, 
                                    DC_EVSEStatus: iso1DC_EVSEStatusType=iso1DC_EVSEStatusType(), 
                                    DC_EVSEStatus_isUsed: int=0):
        struct = iso1PowerDeliveryResType()
        struct.ResponseCode = ResponseCode
        struct.EVSEStatus = EVSEStatus
        struct.EVSEStatus_isUsed = EVSEStatus_isUsed
        struct.AC_EVSEStatus = AC_EVSEStatus
        struct.AC_EVSEStatus_isUsed = AC_EVSEStatus_isUsed
        struct.DC_EVSEStatus = DC_EVSEStatus
        struct.DC_EVSEStatus_isUsed = DC_EVSEStatus_isUsed
        return struct  


    def iso1PaymentOptionListType(  PaymentOption: list[int]=[]):
        struct = iso1PaymentOptionListType()
        for i in range(len(PaymentOption)):
            struct.PaymentOption.array[i] = PaymentOption[i]
        struct.PaymentOption.arrayLen = len(PaymentOption)
        return struct      


    def iso1PhysicalValueType(  Multiplier: int=0,
                                Unit: int=0,
                                Value: int=0):
        struct = iso1PhysicalValueType()
        struct.Multiplier = Multiplier
        struct.Unit = Unit
        struct.Value = Value
        return struct

    def iso1PaymentDetailsReqType(  eMAID: str="",
                                    ContractSignatureCertChain: iso1CertificateChainType=iso1CertificateChainType()):
                
        converted_emaid = OpenV2GUtils.convert_to_array_type_characters(val=eMAID, size=iso1PaymentDetailsReqType_eMAID_CHARACTERS_SIZE)
        struct = iso1PaymentDetailsReqType()
        struct.eMAID.characters = converted_emaid
        struct.eMAID.charactersLen = len(eMAID)
        struct.ContractSignatureCertChain = ContractSignatureCertChain
        return struct


    def iso1AuthorizationResType(   ResponseCode: int=0,
                                    EVSEProcessing: int=0):
        struct = iso1AuthorizationResType()
        struct.ResponseCode = ResponseCode
        struct.EVSEProcessing = EVSEProcessing
        return struct

    def iso1DC_EVSEChargeParameterType( DC_EVSEStatus: iso1DC_EVSEStatusType=iso1DC_EVSEStatusType(),
                                        EVSEMaximumCurrentLimit: iso1PhysicalValueType=iso1PhysicalValueType(),
                                        EVSEMaximumPowerLimit: iso1PhysicalValueType=iso1PhysicalValueType(),
                                        EVSEMaximumVoltageLimit: iso1PhysicalValueType=iso1PhysicalValueType(),
                                        EVSEMinimumCurrentLimit: iso1PhysicalValueType=iso1PhysicalValueType(),
                                        EVSEMinimumVoltageLimit: iso1PhysicalValueType=iso1PhysicalValueType(),
                                        EVSECurrentRegulationTolerance: iso1PhysicalValueType=iso1PhysicalValueType(),
                                        EVSECurrentRegulationTolerance_isUsed: int=0,
                                        EVSEPeakCurrentRipple: iso1PhysicalValueType=iso1PhysicalValueType(),
                                        EVSEEnergyToBeDelivered: iso1PhysicalValueType=iso1PhysicalValueType(),
                                        EVSEEnergyToBeDelivered_isUsed: int=0):
        struct = iso1DC_EVSEChargeParameterType()
        struct.DC_EVSEStatus = DC_EVSEStatus
        struct.EVSEMaximumCurrentLimit = EVSEMaximumCurrentLimit
        struct.EVSEMaximumPowerLimit = EVSEMaximumPowerLimit
        struct.EVSEMaximumVoltageLimit = EVSEMaximumVoltageLimit
        struct.EVSEMinimumCurrentLimit = EVSEMinimumCurrentLimit
        struct.EVSEMinimumVoltageLimit = EVSEMinimumVoltageLimit
        struct.EVSECurrentRegulationTolerance = EVSECurrentRegulationTolerance
        struct.EVSECurrentRegulationTolerance_isUsed = EVSECurrentRegulationTolerance_isUsed
        struct.EVSEPeakCurrentRipple = EVSEPeakCurrentRipple
        struct.EVSEEnergyToBeDelivered = EVSEEnergyToBeDelivered
        struct.EVSEEnergyToBeDelivered_isUsed = EVSEEnergyToBeDelivered_isUsed
        return struct 


    def iso1ChargingStatusResType(  ResponseCode: int=0,
                                    EVSEID: str="",
                                    SAScheduleTupleID: int=0,
                                    EVSEMaxCurrent: iso1PhysicalValueType=iso1PhysicalValueType(),
                                    EVSEMaxCurrent_isUsed: int=0,
                                    MeterInfo: iso1MeterInfoType=iso1MeterInfoType(),
                                    MeterInfo_isUsed: int=0,
                                    ReceiptRequired: int=0,
                                    ReceiptRequired_isUsed: int=0,
                                    AC_EVSEStatus: iso1AC_EVSEStatusType=iso1AC_EVSEStatusType()):

        converted_evse_id = OpenV2GUtils.convert_to_array_type_characters(val=EVSEID, size=iso1ChargingStatusResType_EVSEID_CHARACTERS_SIZE)
        struct = iso1ChargingStatusResType()
        struct.ResponseCode = ResponseCode
        struct.EVSEID.characters = converted_evse_id
        struct.EVSEID.charactersLen = len(EVSEID)
        struct.SAScheduleTupleID = SAScheduleTupleID
        struct.EVSEMaxCurrent = EVSEMaxCurrent
        struct.EVSEMaxCurrent_isUsed = EVSEMaxCurrent_isUsed
        struct.MeterInfo = MeterInfo
        struct.MeterInfo_isUsed = MeterInfo_isUsed
        struct.ReceiptRequired = ReceiptRequired
        struct.ReceiptRequired_isUsed = ReceiptRequired_isUsed
        struct.AC_EVSEStatus = AC_EVSEStatus
        return struct

    
    def iso1ListOfRootCertificateIDsType(RootCertificateID: list[iso1X509IssuerSerialType]=[]):
        struct = iso1ListOfRootCertificateIDsType()
        for i in range(len(RootCertificateID)):
            struct.RootCertificateID.array[i] = RootCertificateID[i]
        struct.RootCertificateID.arrayLen = len(RootCertificateID)
        return struct


    def iso1ChargeServiceType(  ServiceID: int=0,
                                ServiceName: str="",
                                ServiceName_isUsed: int=0,
                                ServiceCategory: int=0,
                                ServiceScope: str="",
                                ServiceScope_isUsed: int=0,
                                FreeService: int=0,
                                SupportedEnergyTransferMode: iso1SupportedEnergyTransferModeType=iso1SupportedEnergyTransferModeType()):
        converted_service_name = OpenV2GUtils.convert_to_array_type_characters(val=ServiceName, size=iso1ChargeServiceType_ServiceName_CHARACTERS_SIZE)
        converted_service_scope = OpenV2GUtils.convert_to_array_type_characters(val=ServiceScope, size=iso1ChargeServiceType_ServiceScope_CHARACTERS_SIZE)
        struct = iso1ChargeServiceType()
        struct.ServiceID = ServiceID
        struct.ServiceName.characters = converted_service_name
        struct.ServiceName.charactersLen = len(ServiceName)
        struct.ServiceName_isUsed = ServiceName_isUsed
        struct.ServiceCategory = ServiceCategory
        struct.ServiceScope.characters = converted_service_scope
        struct.ServiceScope.charactersLen = len(ServiceScope)
        struct.ServiceScope_isUsed = ServiceScope_isUsed
        struct.FreeService = FreeService
        struct.SupportedEnergyTransferMode = SupportedEnergyTransferMode
        return struct


    def iso1SelectedServiceListType(SelectedService: list[iso1SelectedServiceType]=[]):
        struct = iso1SelectedServiceListType()
        for i in range(len(SelectedService)):
            struct.SelectedService.array[i] = SelectedService[i]
        struct.SelectedService.arrayLen = len(SelectedService)
        return struct


    def iso1CableCheckResType(  ResponseCode: int=0,
                                DC_EVSEStatus: iso1DC_EVSEStatusType=iso1DC_EVSEStatusType(),
                                EVSEProcessing: int=0):

        struct = iso1CableCheckResType()
        struct.ResponseCode = ResponseCode
        struct.DC_EVSEStatus = DC_EVSEStatus
        struct.EVSEProcessing = EVSEProcessing
        return struct


    def iso1TransformsType( Transform: list[iso1TransformType]=[]):
        struct = iso1TransformsType()
        for i in range(len(Transform)):
            struct.Transform.array[i] = Transform[i]
        struct.Transform.arrayLen = len(Transform)
        return struct 


    def iso1PreChargeReqType(   DC_EVStatus: iso1DC_EVStatusType=iso1DC_EVStatusType(),
                                EVTargetVoltage: iso1PhysicalValueType=iso1PhysicalValueType(),
                                EVTargetCurrent: iso1PhysicalValueType=iso1PhysicalValueType()):

        struct = iso1PreChargeReqType()
        struct.DC_EVStatus = DC_EVStatus
        struct.EVTargetVoltage = EVTargetVoltage
        struct.EVTargetCurrent = EVTargetCurrent
        return struct


    def iso1AC_EVChargeParameterType(   DepartureTime: int=0,
                                        DepartureTime_isUsed: int=0,
                                        EAmount: iso1PhysicalValueType=iso1PhysicalValueType(),
                                        EVMaxVoltage: iso1PhysicalValueType=iso1PhysicalValueType(),
                                        EVMaxCurrent: iso1PhysicalValueType=iso1PhysicalValueType(),
                                        EVMinCurrent: iso1PhysicalValueType=iso1PhysicalValueType()):
        struct = iso1AC_EVChargeParameterType()
        struct.DepartureTime = DepartureTime
        struct.DepartureTime_isUsed = DepartureTime_isUsed
        struct.EAmount = EAmount
        struct.EVMaxVoltage = EVMaxVoltage
        struct.EVMaxCurrent = EVMaxCurrent
        struct.EVMinCurrent = EVMinCurrent
        return struct

    
    def iso1PMaxScheduleEntryType(  TimeInterval: iso1IntervalType=iso1IntervalType(),
                                    TimeInterval_isUsed: int=0,
                                    RelativeTimeInterval: iso1RelativeTimeIntervalType=iso1RelativeTimeIntervalType(),
                                    RelativeTimeInterval_isUsed: int=0,
                                    PMax: iso1PhysicalValueType=iso1PhysicalValueType()):
        struct = iso1PMaxScheduleEntryType()
        struct.TimeInterval = TimeInterval
        struct.TimeInterval_isUsed = TimeInterval_isUsed
        struct.RelativeTimeInterval = RelativeTimeInterval
        struct.RelativeTimeInterval_isUsed = RelativeTimeInterval_isUsed
        struct.PMax = PMax
        return struct


    def iso1MeteringReceiptResType( ResponseCode: int=0,
                                    EVSEStatus: iso1EVSEStatusType=iso1EVSEStatusType(),
                                    EVSEStatus_isUsed: int=0,
                                    AC_EVSEStatus: iso1AC_EVSEStatusType=iso1AC_EVSEStatusType(),
                                    AC_EVSEStatus_isUsed: int=0,
                                    DC_EVSEStatus: iso1DC_EVSEStatusType=iso1DC_EVSEStatusType(),
                                    DC_EVSEStatus_isUsed: int=0):
        struct = iso1MeteringReceiptResType()
        struct.ResponseCode = ResponseCode
        struct.EVSEStatus = EVSEStatus
        struct.EVSEStatus_isUsed = EVSEStatus_isUsed
        struct.AC_EVSEStatus = AC_EVSEStatus
        struct.AC_EVSEStatus_isUsed = AC_EVSEStatus_isUsed
        struct.DC_EVSEStatus = DC_EVSEStatus
        struct.DC_EVSEStatus_isUsed = DC_EVSEStatus_isUsed
        return struct


    def iso1WeldingDetectionResType(ResponseCode: int=0,
                                    DC_EVSEStatus: iso1DC_EVSEStatusType=iso1DC_EVSEStatusType(),
                                    EVSEPresentVoltage: iso1PhysicalValueType=iso1PhysicalValueType()):
        struct = iso1WeldingDetectionResType()
        struct.ResponseCode = ResponseCode
        struct.DC_EVSEStatus = DC_EVSEStatus
        struct.EVSEPresentVoltage = EVSEPresentVoltage
        return struct


    def iso1ReferenceType(   Id: str="",
                            Id_isUsed: int=0,
                            URI: str="",
                            URI_isUsed: int=0,
                            Type: str="",
                            Type_isUsed: int=0,
                            Transforms: iso1TransformsType=iso1TransformsType(),
                            Transforms_isUsed: int=0,
                            DigestMethod: iso1DigestMethodType=iso1DigestMethodType(),
                            DigestValue: str=""):

        converted_id = OpenV2GUtils.convert_to_array_type_characters(val=Id, size=iso1ReferenceType_Id_CHARACTERS_SIZE)
        converted_uri = OpenV2GUtils.convert_to_array_type_characters(val=URI, size=iso1ReferenceType_URI_CHARACTERS_SIZE)
        converted_type = OpenV2GUtils.convert_to_array_type_characters(val=Type, size=iso1ReferenceType_Type_CHARACTERS_SIZE)
        converted_digest_value = OpenV2GUtils.convert_to_array_type_bytes_str(val=DigestValue, size=iso1ReferenceType_DigestValue_BYTES_SIZE)
        struct = iso1ReferenceType()
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


    def iso1CurrentDemandReqType(   DC_EVStatus: iso1DC_EVStatusType=iso1DC_EVStatusType(),
                                    EVTargetCurrent: iso1PhysicalValueType=iso1PhysicalValueType(),
                                    EVMaximumVoltageLimit: iso1PhysicalValueType=iso1PhysicalValueType(),
                                    EVMaximumVoltageLimit_isUsed: int=0,
                                    EVMaximumCurrentLimit: iso1PhysicalValueType=iso1PhysicalValueType(),
                                    EVMaximumCurrentLimit_isUsed:int=0,
                                    EVMaximumPowerimit: iso1PhysicalValueType=iso1PhysicalValueType(),
                                    EVMaximumPowerLimit_isUsed:int=0,
                                    BulkChargingComplete: int=0,
                                    BulkChargingComplete_isUsed: int=0,
                                    ChargingComplete: int=0,
                                    RemainingTimeToFullSoC: iso1PhysicalValueType=iso1PhysicalValueType(),
                                    RemainingTimeToFullSoC_isUsed:int=0,
                                    RemainingTimeToBulkSoC: iso1PhysicalValueType=iso1PhysicalValueType(),
                                    RemainingTimeToBulkSoC_isUsed:int=0,
                                    EVTargetVoltage: iso1PhysicalValueType=iso1PhysicalValueType()):

        struct = iso1CurrentDemandReqType()
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

    
    def iso1CostType(   costKind: int=0,
                        amount: int=0,
                        amountMultiplier: int=0,
                        amountMultiplier_isUsed: int=0):
        struct = iso1CostType()
        struct.costKind = costKind
        struct.amount = amount
        struct.amountMultiplier = amountMultiplier
        struct.amountMultiplier_isUsed = amountMultiplier_isUsed
        return struct


    def iso1DC_EVPowerDeliveryParameterType(DC_EVStatus: iso1DC_EVStatusType=iso1DC_EVStatusType(),
                                            BulkChargingComplete: int=0,
                                            BulkChargingComplete_isUsed: int=0,
                                            ChargingComplete: int=0):
        struct = iso1DC_EVPowerDeliveryParameterType()
        struct.DC_EVStatus = DC_EVStatus
        struct.BulkChargingComplete = BulkChargingComplete
        struct.BulkChargingComplete_isUsed = BulkChargingComplete_isUsed
        struct.ChargingComplete = ChargingComplete
        return struct


    def iso1RetrievalMethodType(URI: str="",
                                URI_isUsed: int=0,
                                Type: str="",
                                Type_isUsed: int=0,
                                Transforms: iso1TransformsType=iso1TransformsType(),
                                Transforms_isUsed: int=0):
        
        converted_uri = OpenV2GUtils.convert_to_array_type_characters(val=URI, size=iso1RetrievalMethodType_URI_CHARACTERS_SIZE)
        converted_type = OpenV2GUtils.convert_to_array_type_characters(val=Type, size=iso1RetrievalMethodType_Type_CHARACTERS_SIZE)

        struct = iso1RetrievalMethodType()
        struct.URI.characters = converted_uri
        struct.URI.charactersLen = len(URI)
        struct.URI_isUsed = URI_isUsed
        struct.Type.characters = converted_type
        struct.Type.charactersLen = len(Type)
        struct.Type_isUsed = Type_isUsed
        struct.Transforms = Transforms
        struct.Transforms_isUsed = Transforms_isUsed
        return struct



    def iso1CertificateUpdateResType(   ResponseCode: int=0,
                                        SAProvisioningCertificateChain: iso1CertificateChainType=iso1CertificateChainType(),
                                        ContractSignatureCertChain: iso1CertificateChainType=iso1CertificateChainType(),
                                        ContractSignatureEncryptedPrivateKey: iso1ContractSignatureEncryptedPrivateKeyType=iso1ContractSignatureEncryptedPrivateKeyType(),
                                        DHpublickey: iso1DiffieHellmanPublickeyType=iso1DiffieHellmanPublickeyType(),
                                        eMAID: iso1EMAIDType=iso1EMAIDType(),
                                        RetryCounter: int=0,
                                        RetryCounter_isUsed: int=0):
        struct = iso1CertificateUpdateResType()
        struct.ResponseCode = ResponseCode
        struct.SAProvisioningCertificateChain = SAProvisioningCertificateChain
        struct.ContractSignatureCertChain = ContractSignatureCertChain
        struct.ContractSignatureEncryptedPrivateKey = ContractSignatureEncryptedPrivateKey
        struct.DHpublickey = DHpublickey
        struct.eMAID = eMAID
        struct.RetryCounter = RetryCounter
        struct.RetryCounter_isUsed = RetryCounter_isUsed
        return struct


    def iso1CertificateInstallationResType( ResponseCode: int=0,
                                            SAProvisioningCertificateChain: iso1CertificateChainType=iso1CertificateChainType(),
                                            ContractSignatureCertChain: iso1CertificateChainType=iso1CertificateChainType(),
                                            ContractSignatureEncryptedPrivateKey: iso1ContractSignatureEncryptedPrivateKeyType=iso1ContractSignatureEncryptedPrivateKeyType(),
                                            DHpublickey: iso1DiffieHellmanPublickeyType=iso1DiffieHellmanPublickeyType(),
                                            eMAID: iso1EMAIDType=iso1EMAIDType()):

        struct = iso1CertificateInstallationResType()
        struct.ResponseCode = ResponseCode
        struct.SAProvisioningCertificateChain = SAProvisioningCertificateChain
        struct.ContractSignatureCertChain = ContractSignatureCertChain
        struct.ContractSignatureEncryptedPrivateKey = ContractSignatureEncryptedPrivateKey
        struct.DHpublickey = DHpublickey
        struct.eMAID = eMAID
        return struct


    def iso1WeldingDetectionReqType(DC_EVStatus: iso1DC_EVStatusType=iso1DC_EVStatusType()):
        struct = iso1WeldingDetectionReqType()
        struct.DC_EVStatus = DC_EVStatus
        return struct


    def iso1CurrentDemandResType(   ResponseCode: int=0,
                                    DC_EVSEStatus: iso1DC_EVSEStatusType=iso1DC_EVSEStatusType(),
                                    EVSEPresentVoltage: iso1PhysicalValueType=iso1PhysicalValueType(),
                                    EVSEPresentCurrent: iso1PhysicalValueType=iso1PhysicalValueType(),
                                    EVSECurrentLimitAchieved: int=0,
                                    EVSEVoltageLimitAchieved: int=0,
                                    EVSEPowerLimitAchieved: int=0,
                                    EVSEMaximumVoltageLimit: iso1PhysicalValueType=iso1PhysicalValueType(),
                                    EVSEMaximumVoltageLimit_isUsed: int=0,
                                    EVSEMaximumCurrentLimit: iso1PhysicalValueType=iso1PhysicalValueType(),
                                    EVSEMaximumCurrentLimit_isUsed: int=0,
                                    EVSEMaximumPowerLimit: iso1PhysicalValueType=iso1PhysicalValueType(),
                                    EVSEMaximumPowerLimit_isUsed: int=0,
                                    EVSEID: str="",
                                    SAScheduleTupleID: int=0,
                                    MeterInfo: iso1MeterInfoType=iso1MeterInfoType(), 
                                    MeterInfo_isUsed: int=0,
                                    ReceiptRequired: int=0 ,
                                    ReceiptRequired_isUsed: int=0):

        converted_evse_id = OpenV2GUtils.convert_to_array_type_characters(val=EVSEID, size=iso1CurrentDemandResType_EVSEID_CHARACTERS_SIZE)
        struct = iso1CurrentDemandResType()
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
        struct.EVSEID.characters = converted_evse_id
        struct.EVSEID.charactersLen = len(EVSEID)
        struct.SAScheduleTupleID = SAScheduleTupleID
        struct.MeterInfo = MeterInfo
        struct.MeterInfo_isUsed = MeterInfo_isUsed
        struct.ReceiptRequired = ReceiptRequired
        struct.ReceiptRequired_isUsed = ReceiptRequired_isUsed
        return struct

    
    def iso1AC_EVSEChargeParameterType( AC_EVSEStatus: iso1AC_EVSEStatusType=iso1AC_EVSEStatusType(),
                                        EVSENominalVoltage: iso1PhysicalValueType=iso1PhysicalValueType(),
                                        EVSEMaxCurrent: iso1PhysicalValueType=iso1PhysicalValueType()):
        struct = iso1AC_EVSEChargeParameterType()
        struct.AC_EVSEStatus = AC_EVSEStatus
        struct.EVSENominalVoltage = EVSENominalVoltage
        struct.EVSEMaxCurrent = EVSEMaxCurrent
        return struct

    
    def iso1PaymentServiceSelectionReqType( SelectedPaymentOption: int=0,
                                            SelectedServiceList: iso1SelectedServiceListType=iso1SelectedServiceListType()):
        struct = iso1PaymentServiceSelectionReqType()
        struct.SelectedPaymentOption = SelectedPaymentOption
        struct.SelectedServiceList = SelectedServiceList
        return struct


    def iso1SignaturePropertiesType(Id: str="",
                                    Id_isUsed: int=0,
                                    SignatureProperty: list[iso1SignaturePropertyType]=[]):
        converted_id = OpenV2GUtils.convert_to_array_type_characters(val=Id, size=iso1SignaturePropertiesType_Id_CHARACTERS_SIZE)
        struct = iso1SignaturePropertiesType()
        struct.Id.characters = converted_id
        struct.Id.charactersLen = len(Id)
        struct.Id_isUsed = Id_isUsed
        for i in range(len(SignatureProperty)):
            struct.SignatureProperty.array[i] = SignatureProperty[i]
        struct.SignatureProperty.arrayLen = len(SignatureProperty)
        return struct


    def iso1ParameterType(  Name: str="",
                            boolValue: int=0, 
                            boolValue_isUsed: int=0,
                            byteValue: int=0, 
                            byteValue_isUsed: int=0,
                            shortValue: int=0, 
                            shortValue_isUsed: int=0,
                            intValue: int=0, 
                            intValue_isUsed: int=0,
                            physicalValue: iso1PhysicalValueType=iso1PhysicalValueType(), 
                            physicalValue_isUsed: int=0,
                            stringValue: str="",
                            stringValue_isUsed: int=0):
        converted_name = OpenV2GUtils.convert_to_array_type_characters(val=Name, size=iso1ParameterType_Name_CHARACTERS_SIZE)
        converted_string_value = OpenV2GUtils.convert_to_array_type_characters(val=stringValue, size=iso1ParameterType_stringValue_CHARACTERS_SIZE)
        struct = iso1ParameterType()
        struct.Name.characters = converted_name
        struct.Name.charactersLen = len(Name)
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


    def iso1CertificateInstallationReqType( Id: str="",
                                            OEMProvisioningCert: str="",
                                            ListOfRootCertificateIDs: iso1ListOfRootCertificateIDsType=iso1ListOfRootCertificateIDsType()):
        converted_id = OpenV2GUtils.convert_to_array_type_characters(val=Id, size=iso1CertificateInstallationReqType_Id_CHARACTERS_SIZE)
        converted_oem_provisioning_cert = OpenV2GUtils.convert_to_array_type_bytes_str(val=OEMProvisioningCert, size=iso1CertificateInstallationReqType_OEMProvisioningCert_BYTES_SIZE)
        struct = iso1CertificateInstallationReqType()
        struct.Id.characters = converted_id
        struct.Id.charactersLen = len(Id)
        struct.OEMProvisioningCert.bytes = converted_oem_provisioning_cert
        struct.OEMProvisioningCert.bytesLen = len(OEMProvisioningCert)
        struct.ListOfRootCertificateIDs = ListOfRootCertificateIDs
        return struct 


    def iso1ServiceDiscoveryResType(ResponseCode: int=0,
                                    PaymentOptionList: iso1PaymentOptionListType=iso1PaymentOptionListType(),
                                    ChargeService: iso1ChargeServiceType=iso1ChargeServiceType(),
                                    ServiceList: iso1ServiceListType=iso1ServiceListType(),
                                    ServiceList_isUsed: int=0):
        struct = iso1ServiceDiscoveryResType()
        struct.ResponseCode = ResponseCode
        struct.PaymentOptionList = PaymentOptionList
        struct.ChargeService = ChargeService
        struct.ServiceList = ServiceList
        struct.ServiceList_isUsed = ServiceList_isUsed
        return struct 


    def iso1PreChargeResType(   ResponseCode: int=0,
                                DC_EVSEStatus: iso1DC_EVSEStatusType=iso1DC_EVSEStatusType(),
                                EVSEPresentVoltage: iso1PhysicalValueType=iso1PhysicalValueType()):
        struct = iso1PreChargeResType()
        struct.ResponseCode = ResponseCode
        struct.DC_EVSEStatus = DC_EVSEStatus
        struct.EVSEPresentVoltage = EVSEPresentVoltage
        return struct


    def iso1ParameterSetType(   ParameterSetID: int=0,
                                Parameter: list[iso1ParameterType]=[]):
        struct = iso1ParameterSetType()
        struct.ParameterSetID = ParameterSetID
        for i in range(len(Parameter)):
            struct.Parameter.array[i] = Parameter[i]
        struct.Parameter.arrayLen = len(Parameter)
        return struct 


    def iso1SignedInfoType( Id: str="",
                            Id_isUsed: int=0,
                            CanonicalizationMethod: iso1CanonicalizationMethodType=iso1CanonicalizationMethodType(),
                            SignatureMethod: iso1SignatureMethodType=iso1SignatureMethodType(),
                            Reference: list[iso1ReferenceType]=[]):

        converted_id = OpenV2GUtils.convert_to_array_type_characters(val=Id, size=iso1SignedInfoType_Id_CHARACTERS_SIZE)
        struct = iso1SignedInfoType()
        struct.Id.characters = converted_id
        struct.Id.charactersLen = len(Id)
        struct.Id_isUsed = Id_isUsed
        struct.CanonicalizationMethod = CanonicalizationMethod
        struct.SignatureMethod = SignatureMethod
        for i in range(len(Reference)):
            struct.Reference.array[i] = Reference[i]
        struct.Reference.arrayLen = len(Reference)
        return struct


    def iso1ProfileEntryType(   ChargingProfileEntryStart: int=0,
                                ChargingProfileEntryMaxPower: iso1PhysicalValueType=iso1PhysicalValueType(),
                                ChargingProfileEntryMaxNumberOfPhasesInUse: int=0,
                                ChargingProfileEntryMaxNumberOfPhasesInUse_isUsed: int=0):

        struct = iso1ProfileEntryType()
        struct.ChargingProfileEntryStart = ChargingProfileEntryStart
        struct.ChargingProfileEntryMaxPower = ChargingProfileEntryMaxPower
        struct.ChargingProfileEntryMaxNumberOfPhasesInUse = ChargingProfileEntryMaxNumberOfPhasesInUse
        struct.ChargingProfileEntryMaxNumberOfPhasesInUse_isUsed = ChargingProfileEntryMaxNumberOfPhasesInUse_isUsed
        return struct


    def iso1ManifestType(   Id: str="",
                            Id_isUsed: int=0,
                            Reference: list[iso1ReferenceType]=[]):
        converted_id = OpenV2GUtils.convert_to_array_type_characters(val=Id, size=iso1ManifestType_Id_CHARACTERS_SIZE)
        struct = iso1ManifestType()
        struct.Id.characters = converted_id
        struct.Id.charactersLen = len(Id)
        struct.Id_isUsed = Id_isUsed
        for i in range(len(Reference)):
            struct.Reference.array[i] = Reference[i]
        struct.Reference.arrayLen = len(Reference)
        return struct


    def iso1DC_EVChargeParameterType(   DepartureTime: int=0,
                                        DepartureTime_isUsed: int=0,
                                        DC_EVStatus: iso1DC_EVStatusType=iso1DC_EVStatusType(),
                                        EVMaximumCurrentLimit: iso1PhysicalValueType=iso1PhysicalValueType(),
                                        EVMaximumPowerLimit: iso1PhysicalValueType=iso1PhysicalValueType(),
                                        EVMaximumPowerLimit_isUsed: int=0,
                                        EVMaximumVoltageLimit: iso1PhysicalValueType=iso1PhysicalValueType(),
                                        EVEnergyCapacity: iso1PhysicalValueType=iso1PhysicalValueType(),
                                        EVEnergyCapacity_isUsed: int=0,
                                        EVEnergyRequest: iso1PhysicalValueType=iso1PhysicalValueType(),
                                        EVEnergyRequest_isUsed: int=0,
                                        FullSOC: int=0,
                                        FullSOC_isUsed: int=0,
                                        BulkSOC: int=0,
                                        BulkSOC_isUsed: int=0):
        struct = iso1DC_EVChargeParameterType()
        struct.DepartureTime = DepartureTime
        struct.DepartureTime_isUsed = DepartureTime_isUsed
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


    def iso1ConsumptionCostType(startValue: iso1PhysicalValueType=iso1PhysicalValueType(),
                                Cost: list[iso1CostType]=[]):
        struct = iso1ConsumptionCostType()
        struct.startValue = startValue
        for i in range(len(Cost)):
            struct.Cost.array[i] = Cost[i]
        struct.Cost.arrayLen = len(Cost)
        return struct


    def iso1PMaxScheduleType(   PMaxScheduleEntry: list[iso1PMaxScheduleEntryType]=[]):
        struct = iso1PMaxScheduleType()
        for i in range(len(PMaxScheduleEntry)):
            struct.PMaxScheduleEntry.array[i] = PMaxScheduleEntry[i]
        struct.PMaxScheduleEntry.arrayLen = len(PMaxScheduleEntry)
        return struct  
        

    def iso1CertificateUpdateReqType(   Id: str="",
                                        ContractSignatureCertChain: iso1CertificateChainType=iso1CertificateChainType(),
                                        eMAID: str="",
                                        ListOfRootCertificateIDs: iso1ListOfRootCertificateIDsType=iso1ListOfRootCertificateIDsType()):

        converted_id = OpenV2GUtils.convert_to_array_type_characters(val=Id, size=iso1CertificateUpdateReqType_Id_CHARACTERS_SIZE)
        converted_emaid = OpenV2GUtils.convert_to_array_type_characters(val=eMAID, size=iso1CertificateUpdateReqType_eMAID_CHARACTERS_SIZE)
        struct = iso1CertificateUpdateReqType()
        struct.Id.characters = converted_id
        struct.Id.charactersLen = len(Id)
        struct.ContractSignatureCertChain = ContractSignatureCertChain
        struct.eMAID.characters = converted_emaid
        struct.eMAID.charactersLen = len(eMAID)
        struct.ListOfRootCertificateIDs = ListOfRootCertificateIDs
        return struct


    def iso1KeyInfoType(Id: str="",
                        Id_isUsed: int=0,
                        KeyName: list[str]=[""], 
                        KeyValue: list[iso1KeyValueType]=[],
                        RetrievalMethod: list[iso1RetrievalMethodType]=[],
                        X509Data: list[iso1X509DataType]=[],
                        PGPData: list[iso1PGPDataType]=[],
                        SPKIData: list[iso1SPKIDataType]=[],
                        MgmtData: list[str]=[""],
                        ANY: str="",
                        ANY_isUsed: int=0):
        
        converted_id = OpenV2GUtils.convert_to_array_type_characters(val=Id, size=iso1KeyInfoType_Id_CHARACTERS_SIZE)
        converted_any = OpenV2GUtils.convert_to_array_type_characters(val=ANY, size=iso1KeyInfoType_ANY_CHARACTERS_SIZE)
        
        struct = iso1KeyInfoType()
        struct.Id.characters = converted_id
        struct.Id.charactersLen = len(Id)
        struct.Id_isUsed = Id_isUsed
        
        for i in range(len(KeyName)):
            converted_key_name = OpenV2GUtils.convert_to_array_type_characters(val=KeyName[i], size=iso1KeyInfoType_KeyName_CHARACTERS_SIZE)
            struct.KeyName.array[i].characters = converted_key_name
            struct.KeyName.array[i].charactersLen = len(KeyName[i])
        struct.KeyName.arrayLen = len(KeyName)

        for i in range(len(KeyValue)):
            struct.KeyValue.array[i] = KeyValue[i]
        struct.KeyValue.arrayLen = len(KeyValue)
        
        for i in range(len(RetrievalMethod)):
            struct.RetrievalMethod.array[i] = RetrievalMethod[i]
        struct.RetrievalMethod.arrayLen = len(RetrievalMethod)

        for i in range(len(X509Data)):
            struct.X509Data.array[i] = X509Data[i]
        struct.X509Data.arrayLen = len(X509Data)
                

        for i in range(len(PGPData)):
            struct.PGPData.array[i] = PGPData[i]
        struct.PGPData.arrayLen = len(PGPData)
                

        for i in range(len(SPKIData)):
            struct.SPKIData.array[i] = SPKIData[i]
        struct.SPKIData.arrayLen = len(SPKIData)

        for i in range(len(MgmtData)):
            converted_mgmt_data = OpenV2GUtils.convert_to_array_type_characters(val=MgmtData[i], size=iso1KeyInfoType_MgmtData_CHARACTERS_SIZE)
            struct.MgmtData.array[i].characters = converted_mgmt_data
            struct.MgmtData.array[i].charactersLen = len(MgmtData[i])
        struct.MgmtData.arrayLen = len(MgmtData)

        struct.ANY.characters = converted_any
        struct.ANY.charactersLen = len(ANY)
        struct.ANY_isUsed = ANY_isUsed

        return struct


    def iso1ChargeParameterDiscoveryReqType(MaxEntriesSAScheduleTuple: int=0,
                                            MaxEntriesSAScheduleTuple_isUsed: int=0,
                                            RequestedEnergyTransferMode: int=0,
                                            EVChargeParameter: iso1EVChargeParameterType=iso1EVChargeParameterType(),
                                            EVChargeParameter_isUsed: int=0,
                                            AC_EVChargeParameter: iso1AC_EVChargeParameterType=iso1AC_EVChargeParameterType(),
                                            AC_EVChargeParameter_isUsed: int=0,
                                            DC_EVChargeParameter: iso1DC_EVChargeParameterType=iso1DC_EVChargeParameterType(),
                                            DC_EVChargeParameter_isUsed: int=0):
        struct = iso1ChargeParameterDiscoveryReqType()
        struct.MaxEntriesSAScheduleTuple = MaxEntriesSAScheduleTuple
        struct.MaxEntriesSAScheduleTuple_isUsed = MaxEntriesSAScheduleTuple_isUsed
        struct.RequestedEnergyTransferMode = RequestedEnergyTransferMode
        struct.EVChargeParameter = EVChargeParameter
        struct.EVChargeParameter_isUsed = EVChargeParameter_isUsed
        struct.AC_EVChargeParameter = AC_EVChargeParameter
        struct.AC_EVChargeParameter_isUsed = AC_EVChargeParameter_isUsed
        struct.DC_EVChargeParameter = DC_EVChargeParameter
        struct.DC_EVChargeParameter_isUsed = DC_EVChargeParameter_isUsed
        return struct


    def iso1ChargingProfileType(ProfileEntry: list[iso1ProfileEntryType]=[]):
        struct = iso1ChargingProfileType()
        for i in range(len(ProfileEntry)):
            struct.ProfileEntry.array[i] = ProfileEntry[i]
        struct.ProfileEntry.arrayLen = len(ProfileEntry)
        return struct


    def iso1SalesTariffEntryType(   TimeInterval: iso1IntervalType=iso1IntervalType(),
                                    TimeInterval_isUsed: int=0,
                                    RelativeTimeInterval: iso1RelativeTimeIntervalType=iso1RelativeTimeIntervalType(),
                                    RelativeTimeInterval_isUsed: int=0,
                                    EPriceLevel: int=0,
                                    EPriceLevel_isUsed: int=0,
                                    ConsumptionCost: list[iso1ConsumptionCostType]=[]):
        

        struct = iso1SalesTariffEntryType()
        struct.TimeInterval = TimeInterval
        struct.TimeInterval_isUsed = TimeInterval_isUsed
        struct.RelativeTimeInterval = RelativeTimeInterval
        struct.RelativeTimeInterval_isUsed = RelativeTimeInterval_isUsed
        struct.EPriceLevel = EPriceLevel
        struct.EPriceLevel_isUsed = EPriceLevel_isUsed
        for i in range(len(ConsumptionCost)):
            struct.ConsumptionCost.array[i] = ConsumptionCost[i]
        struct.ConsumptionCost.arrayLen = len(ConsumptionCost)
        return struct


    def iso1SalesTariffType(Id: str="",
                            Id_isUsed: int=0,
                            SalesTariffID: int=0,
                            SalesTariffDescription: str="",
                            SalesTariffDescription_isUsed: int=0,
                            NumEPriceLevels: int=0,
                            NumEPriceLevels_isUsed: int=0,
                            SalesTariffEntry: list[iso1SalesTariffEntryType]=[]):
        converted_id = OpenV2GUtils.convert_to_array_type_characters(val=Id, size=iso1SalesTariffType_Id_CHARACTERS_SIZE)
        converted_sales_tariff_description = OpenV2GUtils.convert_to_array_type_characters(val=SalesTariffDescription, size=iso1SalesTariffType_SalesTariffDescription_CHARACTERS_SIZE)
        struct = iso1SalesTariffType()
        struct.Id.characters = converted_id
        struct.Id.charactersLen = len(Id)
        struct.Id_isUsed = Id_isUsed
        struct.SalesTariffID = SalesTariffID
        struct.SalesTariffDescription.characters = converted_sales_tariff_description
        struct.SalesTariffDescription.charactersLen = len(SalesTariffDescription)
        struct.SalesTariffDescription_isUsed = SalesTariffDescription_isUsed
        struct.NumEPriceLevels = NumEPriceLevels
        struct.NumEPriceLevels_isUsed = NumEPriceLevels_isUsed
        for i in range(len(SalesTariffEntry)):
            struct.SalesTariffEntry.array[i] = SalesTariffEntry[i]
        struct.SalesTariffEntry.arrayLen = len(SalesTariffEntry)
        return struct


    def iso1SignatureType(  Id: str="",
                            Id_isUsed: int=0,
                            SignedInfo: iso1SignedInfoType=iso1SignedInfoType(),
                            SignatureValue: iso1SignatureValueType=iso1SignatureValueType(),
                            KeyInfo: iso1KeyInfoType=iso1KeyInfoType(),
                            KeyInfo_isUsed: int=0,
                            Object: list[iso1ObjectType]=[]):
        converted_id = OpenV2GUtils.convert_to_array_type_characters(val=Id, size=iso1SignatureType_Id_CHARACTERS_SIZE)
        struct = iso1SignatureType()
        struct.Id.characters = converted_id
        struct.Id.charactersLen = len(Id)
        struct.Id_isUsed = Id_isUsed
        struct.SignedInfo = SignedInfo
        struct.SignatureValue = SignatureValue
        struct.KeyInfo = KeyInfo
        struct.KeyInfo_isUsed = KeyInfo_isUsed
        for i in range(len(Object)):
            struct.Object.array[i] = Object[i]
        struct.Object.arrayLen = len(Object)
        return struct


    def iso1PowerDeliveryReqType(   ChargeProgress: int=0,
                                    SAScheduleTupleID: int=0,
                                    ChargingProfile: iso1ChargingProfileType=iso1ChargingProfileType(),
                                    ChargingProfile_isUsed: int=0,
                                    EVPowerDeliveryParameter: iso1EVPowerDeliveryParameterType=iso1EVPowerDeliveryParameterType(),
                                    EVPowerDeliveryParameter_isUsed: int=0,
                                    DC_EVPowerDeliveryParameter: iso1DC_EVPowerDeliveryParameterType=iso1DC_EVPowerDeliveryParameterType(),
                                    DC_EVPowerDeliveryParameter_isUsed: int=0):

        struct = iso1PowerDeliveryReqType()
        struct.ChargeProgress = ChargeProgress
        struct.SAScheduleTupleID = SAScheduleTupleID
        struct.ChargingProfile = ChargingProfile
        struct.ChargingProfile_isUsed = ChargingProfile_isUsed
        struct.EVPowerDeliveryParameter = EVPowerDeliveryParameter
        struct.EVPowerDeliveryParameter_isUsed = EVPowerDeliveryParameter_isUsed
        struct.DC_EVPowerDeliveryParameter = DC_EVPowerDeliveryParameter
        struct.DC_EVPowerDeliveryParameter_isUsed = DC_EVPowerDeliveryParameter_isUsed
        return struct


    def iso1ServiceParameterListType(   ParameterSet: list[iso1ParameterSetType]=[]):
        struct = iso1ServiceParameterListType()
        for i in range(len(ParameterSet)):
            struct.ParameterSet.array[i] = ParameterSet[i]
        struct.ParameterSet.arrayLen = len(ParameterSet)
        return struct

    def iso1ServiceDetailResType(ResponseCode: int=0,
                                ServiceID: int=0,
                                ServiceParameterList: iso1ServiceParameterListType=iso1ServiceParameterListType(),
                                ServiceParameterList_isUsed: int=0):

        struct = iso1ServiceDetailResType()
        struct.ResponseCode = ResponseCode
        struct.ServiceID = ServiceID
        struct.ServiceParameterList = ServiceParameterList
        struct.ServiceParameterList_isUsed = ServiceParameterList_isUsed
        return struct


    def iso1SAScheduleTupleType(SAScheduleTupleID: int=0,
                                PMaxSchedule: iso1PMaxScheduleType=iso1PMaxScheduleType(),
                                SalesTariff: iso1SalesTariffType=iso1SalesTariffType(),
                                SalesTariff_isUsed: int=0):
        struct = iso1SAScheduleTupleType()
        struct.SAScheduleTupleID = SAScheduleTupleID
        struct.PMaxSchedule = PMaxSchedule
        struct.SalesTariff = SalesTariff
        struct.SalesTariff_isUsed = SalesTariff_isUsed
        return struct


    def iso1MessageHeaderType(  SessionID: int=0,
                                Notification: iso1NotificationType=iso1NotificationType(),
                                Notification_isUsed: int=0,
                                Signature: iso1SignatureType=iso1SignatureType(),
                                Signature_isUsed: int=0):

        converted_session_id = OpenV2GUtils.convert_to_array_type_bytes(val=SessionID, size=iso1MessageHeaderType_SessionID_BYTES_SIZE)
        struct = iso1MessageHeaderType()
        struct.SessionID.bytes = converted_session_id
        struct.SessionID.bytesLen = iso1MessageHeaderType_SessionID_BYTES_SIZE
        struct.Notification = Notification
        struct.Notification_isUsed = Notification_isUsed
        struct.Signature = Signature
        struct.Signature_isUsed = Signature_isUsed
        return struct


    def iso1SAScheduleListType( SAScheduleTuple: list[iso1SAScheduleTupleType]=[]):
        struct = iso1SAScheduleListType()
        for i in range(len(SAScheduleTuple)):
            struct.SAScheduleTuple.array[i] = SAScheduleTuple[i]
        struct.SAScheduleTuple.arrayLen = len(SAScheduleTuple)
        return struct


    def iso1ChargeParameterDiscoveryResType(ResponseCode: int=0,
                                            EVSEProcessing: int=0,
                                            SASchedules: iso1SASchedulesType=iso1SASchedulesType(),
                                            SASchedules_isUsed: int=0,
                                            SAScheduleList: iso1SAScheduleListType=iso1SAScheduleListType(),
                                            SAScheduleList_isUsed: int=0,
                                            EVSEChargeParameter: iso1EVSEChargeParameterType=iso1EVSEChargeParameterType(),
                                            EVSEChargeParameter_isUsed: int=0,
                                            AC_EVSEChargeParameter: iso1AC_EVSEChargeParameterType=iso1AC_EVSEChargeParameterType(),
                                            AC_EVSEChargeParameter_isUsed: int=0,
                                            DC_EVSEChargeParameter: iso1DC_EVSEChargeParameterType=iso1DC_EVSEChargeParameterType(),
                                            DC_EVSEChargeParameter_isUsed: int=0):
        struct = iso1ChargeParameterDiscoveryResType()
        struct.ResponseCode = ResponseCode
        struct.EVSEProcessing = EVSEProcessing
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


    def iso1BodyType(   BodyElement: iso1BodyBaseType=iso1BodyBaseType(),
		                SessionSetupReq: iso1SessionSetupReqType=iso1SessionSetupReqType(),
		                SessionSetupRes: iso1SessionSetupResType=iso1SessionSetupResType(),
		                ServiceDiscoveryReq: iso1ServiceDiscoveryReqType=iso1ServiceDiscoveryReqType(),
		                ServiceDiscoveryRes: iso1ServiceDiscoveryResType=iso1ServiceDiscoveryResType(),
		                ServiceDetailReq: iso1ServiceDetailReqType=iso1ServiceDetailReqType(),
		                ServiceDetailRes: iso1ServiceDetailResType=iso1ServiceDetailResType(),
		                PaymentServiceSelectionReq: iso1PaymentServiceSelectionReqType=iso1PaymentServiceSelectionReqType(),
		                PaymentServiceSelectionRes: iso1PaymentServiceSelectionResType=iso1PaymentServiceSelectionResType(),
		                PaymentDetailsReq: iso1PaymentDetailsReqType=iso1PaymentDetailsReqType(),
		                PaymentDetailsRes: iso1PaymentDetailsResType=iso1PaymentDetailsResType(),
		                AuthorizationReq: iso1AuthorizationReqType=iso1AuthorizationReqType(),
		                AuthorizationRes: iso1AuthorizationResType=iso1AuthorizationResType(),
		                ChargeParameterDiscoveryReq: iso1ChargeParameterDiscoveryReqType=iso1ChargeParameterDiscoveryReqType(),
		                ChargeParameterDiscoveryRes: iso1ChargeParameterDiscoveryResType=iso1ChargeParameterDiscoveryResType(),
		                PowerDeliveryReq: iso1PowerDeliveryReqType=iso1PowerDeliveryReqType(),
		                PowerDeliveryRes: iso1PowerDeliveryResType=iso1PowerDeliveryResType(),
		                MeteringReceiptReq: iso1MeteringReceiptReqType=iso1MeteringReceiptReqType(),
		                MeteringReceiptRes: iso1MeteringReceiptResType=iso1MeteringReceiptResType(),
		                SessionStopReq: iso1SessionStopReqType=iso1SessionStopReqType(),
		                SessionStopRes: iso1SessionStopResType=iso1SessionStopResType(),
		                CertificateUpdateReq: iso1CertificateUpdateReqType=iso1CertificateUpdateReqType(),
		                CertificateUpdateRes: iso1CertificateUpdateResType=iso1CertificateUpdateResType(),
		                CertificateInstallationReq: iso1CertificateInstallationReqType=iso1CertificateInstallationReqType(),
		                CertificateInstallationRes: iso1CertificateInstallationResType=iso1CertificateInstallationResType(),
		                ChargingStatusReq: iso1ChargingStatusReqType=iso1ChargingStatusReqType(),
		                ChargingStatusRes: iso1ChargingStatusResType=iso1ChargingStatusResType(),
		                CableCheckReq: iso1CableCheckReqType=iso1CableCheckReqType(),
		                CableCheckRes: iso1CableCheckResType=iso1CableCheckResType(),
		                PreChargeReq: iso1PreChargeReqType=iso1PreChargeReqType(),
		                PreChargeRes: iso1PreChargeResType=iso1PreChargeResType(),
		                CurrentDemandReq: iso1CurrentDemandReqType=iso1CurrentDemandReqType(),
		                CurrentDemandRes: iso1CurrentDemandResType=iso1CurrentDemandResType(),
		                WeldingDetectionReq: iso1WeldingDetectionReqType=iso1WeldingDetectionReqType(),
		                WeldingDetectionRes: iso1WeldingDetectionResType=iso1WeldingDetectionResType(),
                        BodyElement_isUsed: int=0,
                        SessionSetupReq_isUsed: int=0,
                        SessionSetupRes_isUsed: int=0,
                        ServiceDiscoveryReq_isUsed: int=0,
                        ServiceDiscoveryRes_isUsed: int=0,
                        ServiceDetailReq_isUsed: int=0,
                        ServiceDetailRes_isUsed: int=0,
                        PaymentServiceSelectionReq_isUsed: int=0,
                        PaymentServiceSelectionRes_isUsed: int=0,
                        PaymentDetailsReq_isUsed: int=0,
                        PaymentDetailsRes_isUsed: int=0,
                        AuthorizationReq_isUsed: int=0,
                        AuthorizationRes_isUsed: int=0,
                        ChargeParameterDiscoveryReq_isUsed: int=0,
                        ChargeParameterDiscoveryRes_isUsed: int=0,
                        PowerDeliveryReq_isUsed: int=0,
                        PowerDeliveryRes_isUsed: int=0,
                        MeteringReceiptReq_isUsed: int=0,
                        MeteringReceiptRes_isUsed: int=0,
                        SessionStopReq_isUsed: int=0,
                        SessionStopRes_isUsed: int=0,
                        CertificateUpdateReq_isUsed: int=0,
                        CertificateUpdateRes_isUsed: int=0,
                        CertificateInstallationReq_isUsed: int=0,
                        CertificateInstallationRes_isUsed: int=0,
                        ChargingStatusReq_isUsed: int=0,
                        ChargingStatusRes_isUsed: int=0,
                        CableCheckReq_isUsed: int=0,
                        CableCheckRes_isUsed: int=0,
                        PreChargeReq_isUsed: int=0,
                        PreChargeRes_isUsed: int=0,
                        CurrentDemandReq_isUsed: int=0,
                        CurrentDemandRes_isUsed: int=0,
                        WeldingDetectionReq_isUsed: int=0,
                        WeldingDetectionRes_isUsed: int=0):
        struct = iso1BodyType()
        struct.BodyElement = BodyElement
        struct.SessionSetupReq = SessionSetupReq
        struct.SessionSetupRes = SessionSetupRes
        struct.ServiceDiscoveryReq = ServiceDiscoveryReq
        struct.ServiceDiscoveryRes = ServiceDiscoveryRes
        struct.ServiceDetailReq = ServiceDetailReq
        struct.ServiceDetailRes = ServiceDetailRes
        struct.PaymentServiceSelectionReq = PaymentServiceSelectionReq
        struct.PaymentServiceSelectionRes = PaymentServiceSelectionRes
        struct.PaymentDetailsReq = PaymentDetailsReq
        struct.PaymentDetailsRes = PaymentDetailsRes
        struct.AuthorizationReq = AuthorizationReq
        struct.AuthorizationRes = AuthorizationRes
        struct.ChargeParameterDiscoveryReq = ChargeParameterDiscoveryReq
        struct.ChargeParameterDiscoveryRes = ChargeParameterDiscoveryRes
        struct.PowerDeliveryReq = PowerDeliveryReq
        struct.PowerDeliveryRes = PowerDeliveryRes
        struct.MeteringReceiptReq = MeteringReceiptReq
        struct.MeteringReceiptRes = MeteringReceiptRes
        struct.SessionStopReq = SessionStopReq
        struct.SessionStopRes = SessionStopRes
        struct.CertificateUpdateReq = CertificateUpdateReq
        struct.CertificateUpdateRes = CertificateUpdateRes
        struct.CertificateInstallationReq = CertificateInstallationReq
        struct.CertificateInstallationRes = CertificateInstallationRes
        struct.ChargingStatusReq = ChargingStatusReq
        struct.ChargingStatusRes = ChargingStatusRes
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
        struct.PaymentServiceSelectionReq_isUsed = PaymentServiceSelectionReq_isUsed
        struct.PaymentServiceSelectionRes_isUsed = PaymentServiceSelectionRes_isUsed
        struct.PaymentDetailsReq_isUsed = PaymentDetailsReq_isUsed
        struct.PaymentDetailsRes_isUsed = PaymentDetailsRes_isUsed
        struct.AuthorizationReq_isUsed = AuthorizationReq_isUsed
        struct.AuthorizationRes_isUsed = AuthorizationRes_isUsed
        struct.ChargeParameterDiscoveryReq_isUsed = ChargeParameterDiscoveryReq_isUsed
        struct.ChargeParameterDiscoveryRes_isUsed = ChargeParameterDiscoveryRes_isUsed
        struct.PowerDeliveryReq_isUsed = PowerDeliveryReq_isUsed
        struct.PowerDeliveryRes_isUsed = PowerDeliveryRes_isUsed
        struct.MeteringReceiptReq_isUsed = MeteringReceiptReq_isUsed
        struct.MeteringReceiptRes_isUsed = MeteringReceiptRes_isUsed
        struct.SessionStopReq_isUsed = SessionStopReq_isUsed
        struct.SessionStopRes_isUsed = SessionStopRes_isUsed
        struct.CertificateUpdateReq_isUsed = CertificateUpdateReq_isUsed
        struct.CertificateUpdateRes_isUsed = CertificateUpdateRes_isUsed
        struct.CertificateInstallationReq_isUsed = CertificateInstallationReq_isUsed
        struct.CertificateInstallationRes_isUsed = CertificateInstallationRes_isUsed
        struct.ChargingStatusReq_isUsed = ChargingStatusReq_isUsed
        struct.ChargingStatusRes_isUsed = ChargingStatusRes_isUsed
        struct.CableCheckReq_isUsed = CableCheckReq_isUsed
        struct.CableCheckRes_isUsed = CableCheckRes_isUsed
        struct.PreChargeReq_isUsed = PreChargeReq_isUsed
        struct.PreChargeRes_isUsed = PreChargeRes_isUsed
        struct.CurrentDemandReq_isUsed = CurrentDemandReq_isUsed
        struct.CurrentDemandRes_isUsed = CurrentDemandRes_isUsed
        struct.WeldingDetectionReq_isUsed = WeldingDetectionReq_isUsed
        struct.WeldingDetectionRes_isUsed = WeldingDetectionRes_isUsed
        return struct 


    def iso1AnonType_V2G_Message(   Header: iso1MessageHeaderType=iso1MessageHeaderType(),
                                    Body: iso1BodyType=iso1BodyType()):
        struct = iso1AnonType_V2G_Message()
        struct.Header = Header
        struct.Body = Body
        return struct


    def iso1EXIDocument(V2G_Message: iso1AnonType_V2G_Message=iso1AnonType_V2G_Message(),
	                    ServiceDiscoveryReq: iso1ServiceDiscoveryReqType=iso1ServiceDiscoveryReqType(),
	                    ServiceDiscoveryRes: iso1ServiceDiscoveryResType=iso1ServiceDiscoveryResType(),
	                    MeteringReceiptReq: iso1MeteringReceiptReqType=iso1MeteringReceiptReqType(),
	                    PaymentDetailsReq: iso1PaymentDetailsReqType=iso1PaymentDetailsReqType(),
	                    MeteringReceiptRes: iso1MeteringReceiptResType=iso1MeteringReceiptResType(),
	                    PaymentDetailsRes: iso1PaymentDetailsResType=iso1PaymentDetailsResType(),
	                    SessionSetupReq: iso1SessionSetupReqType=iso1SessionSetupReqType(),
	                    SessionSetupRes: iso1SessionSetupResType=iso1SessionSetupResType(),
	                    CableCheckReq: iso1CableCheckReqType=iso1CableCheckReqType(),
	                    CableCheckRes: iso1CableCheckResType=iso1CableCheckResType(),
	                    CertificateInstallationReq: iso1CertificateInstallationReqType=iso1CertificateInstallationReqType(),
	                    CertificateInstallationRes: iso1CertificateInstallationResType=iso1CertificateInstallationResType(),
	                    WeldingDetectionReq: iso1WeldingDetectionReqType=iso1WeldingDetectionReqType(),
	                    WeldingDetectionRes: iso1WeldingDetectionResType=iso1WeldingDetectionResType(),
	                    CertificateUpdateReq: iso1CertificateUpdateReqType=iso1CertificateUpdateReqType(),
	                    CertificateUpdateRes: iso1CertificateUpdateResType=iso1CertificateUpdateResType(),
	                    PaymentServiceSelectionReq: iso1PaymentServiceSelectionReqType=iso1PaymentServiceSelectionReqType(),
	                    PowerDeliveryReq: iso1PowerDeliveryReqType=iso1PowerDeliveryReqType(),
	                    PaymentServiceSelectionRes: iso1PaymentServiceSelectionResType=iso1PaymentServiceSelectionResType(),
	                    PowerDeliveryRes: iso1PowerDeliveryResType=iso1PowerDeliveryResType(),
	                    ChargingStatusReq: iso1ChargingStatusReqType=iso1ChargingStatusReqType(),
	                    ChargingStatusRes: iso1ChargingStatusResType=iso1ChargingStatusResType(),
	                    BodyElement: iso1BodyBaseType=iso1BodyBaseType(),
	                    CurrentDemandReq: iso1CurrentDemandReqType=iso1CurrentDemandReqType(),
	                    PreChargeReq: iso1PreChargeReqType=iso1PreChargeReqType(),
	                    CurrentDemandRes: iso1CurrentDemandResType=iso1CurrentDemandResType(),
	                    PreChargeRes: iso1PreChargeResType=iso1PreChargeResType(),
	                    SessionStopReq: iso1SessionStopReqType=iso1SessionStopReqType(),
	                    AuthorizationReq: iso1AuthorizationReqType=iso1AuthorizationReqType(),
	                    SessionStopRes: iso1SessionStopResType=iso1SessionStopResType(),
	                    AuthorizationRes: iso1AuthorizationResType=iso1AuthorizationResType(),
	                    ChargeParameterDiscoveryReq: iso1ChargeParameterDiscoveryReqType=iso1ChargeParameterDiscoveryReqType(),
	                    ChargeParameterDiscoveryRes: iso1ChargeParameterDiscoveryResType=iso1ChargeParameterDiscoveryResType(),
	                    ServiceDetailReq: iso1ServiceDetailReqType=iso1ServiceDetailReqType(),
	                    ServiceDetailRes: iso1ServiceDetailResType=iso1ServiceDetailResType(),
	                    DC_EVSEStatus: iso1DC_EVSEStatusType=iso1DC_EVSEStatusType(),
	                    RelativeTimeInterval: iso1RelativeTimeIntervalType=iso1RelativeTimeIntervalType(),
	                    SalesTariffEntry: iso1SalesTariffEntryType=iso1SalesTariffEntryType(),
	                    DC_EVPowerDeliveryParameter: iso1DC_EVPowerDeliveryParameterType=iso1DC_EVPowerDeliveryParameterType(),
	                    SASchedules: iso1SASchedulesType=iso1SASchedulesType(),
	                    AC_EVChargeParameter: iso1AC_EVChargeParameterType=iso1AC_EVChargeParameterType(),
	                    SAScheduleList: iso1SAScheduleListType=iso1SAScheduleListType(),
	                    DC_EVStatus: iso1DC_EVStatusType=iso1DC_EVStatusType(),
	                    EVStatus: iso1EVStatusType=iso1EVStatusType(),
	                    DC_EVChargeParameter: iso1DC_EVChargeParameterType=iso1DC_EVChargeParameterType(),
	                    DC_EVSEChargeParameter: iso1DC_EVSEChargeParameterType=iso1DC_EVSEChargeParameterType(),
	                    EVSEStatus: iso1EVSEStatusType=iso1EVSEStatusType(),
	                    TimeInterval: iso1IntervalType=iso1IntervalType(),
	                    EVPowerDeliveryParameter: iso1EVPowerDeliveryParameterType=iso1EVPowerDeliveryParameterType(),
	                    EVSEChargeParameter: iso1EVSEChargeParameterType=iso1EVSEChargeParameterType(),
	                    AC_EVSEStatus: iso1AC_EVSEStatusType=iso1AC_EVSEStatusType(),
	                    Entry: iso1EntryType=iso1EntryType(),
	                    AC_EVSEChargeParameter: iso1AC_EVSEChargeParameterType=iso1AC_EVSEChargeParameterType(),
	                    PMaxScheduleEntry: iso1PMaxScheduleEntryType=iso1PMaxScheduleEntryType(),
	                    EVChargeParameter: iso1EVChargeParameterType=iso1EVChargeParameterType(),
	                    SignatureProperty: iso1SignaturePropertyType=iso1SignaturePropertyType(),
	                    DSAKeyValue: iso1DSAKeyValueType=iso1DSAKeyValueType(),
	                    SignatureProperties: iso1SignaturePropertiesType=iso1SignaturePropertiesType(),
	                    KeyValue: iso1KeyValueType=iso1KeyValueType(),
	                    Transforms: iso1TransformsType=iso1TransformsType(),
	                    DigestMethod: iso1DigestMethodType=iso1DigestMethodType(),
	                    Signature: iso1SignatureType=iso1SignatureType(),
	                    RetrievalMethod: iso1RetrievalMethodType=iso1RetrievalMethodType(),
	                    Manifest: iso1ManifestType=iso1ManifestType(),
	                    Reference: iso1ReferenceType=iso1ReferenceType(),
	                    CanonicalizationMethod: iso1CanonicalizationMethodType=iso1CanonicalizationMethodType(),
	                    RSAKeyValue: iso1RSAKeyValueType=iso1RSAKeyValueType(),
	                    Transform: iso1TransformType=iso1TransformType(),
	                    PGPData: iso1PGPDataType=iso1PGPDataType(),
                        MgmtData: str="",
                        SignatureMethod: iso1SignatureMethodType=iso1SignatureMethodType(),
                        KeyInfo: iso1KeyInfoType=iso1KeyInfoType(),
                        SPKIData: iso1SPKIDataType=iso1SPKIDataType(),
                        X509Data: iso1X509DataType=iso1X509DataType(),
                        SignatureValue: iso1SignatureValueType=iso1SignatureValueType(),
                        KeyName: str="",
                        DigestValue: str="",
                        SignedInfo: iso1SignedInfoType=iso1SignedInfoType(),
                        Object: iso1ObjectType=iso1ObjectType(),
                        V2G_Message_isUsed: int=0,
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
                        CertificateInstallationReq_isUsed: int=0,
                        CertificateInstallationRes_isUsed: int=0,
                        WeldingDetectionReq_isUsed: int=0,
                        WeldingDetectionRes_isUsed: int=0,
                        CertificateUpdateReq_isUsed: int=0,
                        CertificateUpdateRes_isUsed: int=0,
                        PaymentServiceSelectionReq_isUsed: int=0,
                        PowerDeliveryReq_isUsed: int=0,
                        PaymentServiceSelectionRes_isUsed: int=0,
                        PowerDeliveryRes_isUsed: int=0,
                        ChargingStatusReq_isUsed: int=0,
                        ChargingStatusRes_isUsed: int=0,
                        BodyElement_isUsed: int=0,
                        CurrentDemandReq_isUsed: int=0,
                        PreChargeReq_isUsed: int=0,
                        CurrentDemandRes_isUsed: int=0,
                        PreChargeRes_isUsed: int=0,
                        SessionStopReq_isUsed: int=0,
                        AuthorizationReq_isUsed: int=0,
                        SessionStopRes_isUsed: int=0,
                        AuthorizationRes_isUsed: int=0,
                        ChargeParameterDiscoveryReq_isUsed: int=0,
                        ChargeParameterDiscoveryRes_isUsed: int=0,
                        ServiceDetailReq_isUsed: int=0,
                        ServiceDetailRes_isUsed: int=0,
                        DC_EVSEStatus_isUsed: int=0,
                        RelativeTimeInterval_isUsed: int=0,
                        SalesTariffEntry_isUsed: int=0,
                        DC_EVPowerDeliveryParameter_isUsed: int=0,
                        SASchedules_isUsed: int=0,
                        AC_EVChargeParameter_isUsed: int=0,
                        SAScheduleList_isUsed: int=0,
                        DC_EVStatus_isUsed: int=0,
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
                        _warning_: int=0):
    
        converted_mgmt_data = OpenV2GUtils.convert_to_array_type_characters(val=MgmtData, size=EXIDocument_MgmtData_CHARACTERS_SIZE)
        converted_key_name = OpenV2GUtils.convert_to_array_type_characters(val=KeyName, size=EXIDocument_KeyName_CHARACTERS_SIZE)
        converted_digest_value = OpenV2GUtils.convert_to_array_type_bytes_str(val=DigestValue, size=EXIDocument_DigestValue_BYTES_SIZE)
        struct = iso1EXIDocument()
        struct.V2G_Message = V2G_Message
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
        struct.CertificateInstallationReq = CertificateInstallationReq
        struct.CertificateInstallationRes = CertificateInstallationRes
        struct.WeldingDetectionReq = WeldingDetectionReq
        struct.WeldingDetectionRes = WeldingDetectionRes
        struct.CertificateUpdateReq = CertificateUpdateReq
        struct.CertificateUpdateRes = CertificateUpdateRes
        struct.PaymentServiceSelectionReq = PaymentServiceSelectionReq
        struct.PowerDeliveryReq = PowerDeliveryReq
        struct.PaymentServiceSelectionRes = PaymentServiceSelectionRes
        struct.PowerDeliveryRes = PowerDeliveryRes
        struct.ChargingStatusReq = ChargingStatusReq
        struct.ChargingStatusRes = ChargingStatusRes
        struct.BodyElement = BodyElement
        struct.CurrentDemandReq = CurrentDemandReq
        struct.PreChargeReq = PreChargeReq
        struct.CurrentDemandRes = CurrentDemandRes
        struct.PreChargeRes = PreChargeRes
        struct.SessionStopReq = SessionStopReq
        struct.AuthorizationReq = AuthorizationReq
        struct.SessionStopRes = SessionStopRes
        struct.AuthorizationRes = AuthorizationRes
        struct.ChargeParameterDiscoveryReq = ChargeParameterDiscoveryReq
        struct.ChargeParameterDiscoveryRes = ChargeParameterDiscoveryRes
        struct.ServiceDetailReq = ServiceDetailReq
        struct.ServiceDetailRes = ServiceDetailRes
        struct.DC_EVSEStatus = DC_EVSEStatus
        struct.RelativeTimeInterval = RelativeTimeInterval
        struct.SalesTariffEntry = SalesTariffEntry
        struct.DC_EVPowerDeliveryParameter = DC_EVPowerDeliveryParameter
        struct.SASchedules = SASchedules
        struct.AC_EVChargeParameter = AC_EVChargeParameter
        struct.SAScheduleList = SAScheduleList
        struct.DC_EVStatus = DC_EVStatus
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
        struct.DigestValue.bytesLen = len(DigestValue)
        struct.SignedInfo = SignedInfo
        struct.Object = Object
        struct.V2G_Message_isUsed = V2G_Message_isUsed
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
        struct.CertificateInstallationReq_isUsed = CertificateInstallationReq_isUsed
        struct.CertificateInstallationRes_isUsed = CertificateInstallationRes_isUsed
        struct.WeldingDetectionReq_isUsed = WeldingDetectionReq_isUsed
        struct.WeldingDetectionRes_isUsed = WeldingDetectionRes_isUsed
        struct.CertificateUpdateReq_isUsed = CertificateUpdateReq_isUsed
        struct.CertificateUpdateRes_isUsed = CertificateUpdateRes_isUsed
        struct.PaymentServiceSelectionReq_isUsed = PaymentServiceSelectionReq_isUsed
        struct.PowerDeliveryReq_isUsed = PowerDeliveryReq_isUsed
        struct.PaymentServiceSelectionRes_isUsed = PaymentServiceSelectionRes_isUsed
        struct.PowerDeliveryRes_isUsed = PowerDeliveryRes_isUsed
        struct.ChargingStatusReq_isUsed = ChargingStatusReq_isUsed
        struct.ChargingStatusRes_isUsed = ChargingStatusRes_isUsed
        struct.BodyElement_isUsed = BodyElement_isUsed
        struct.CurrentDemandReq_isUsed = CurrentDemandReq_isUsed
        struct.PreChargeReq_isUsed = PreChargeReq_isUsed
        struct.CurrentDemandRes_isUsed = CurrentDemandRes_isUsed
        struct.PreChargeRes_isUsed = PreChargeRes_isUsed
        struct.SessionStopReq_isUsed = SessionStopReq_isUsed
        struct.AuthorizationReq_isUsed = AuthorizationReq_isUsed
        struct.SessionStopRes_isUsed = SessionStopRes_isUsed
        struct.AuthorizationRes_isUsed = AuthorizationRes_isUsed
        struct.ChargeParameterDiscoveryReq_isUsed = ChargeParameterDiscoveryReq_isUsed
        struct.ChargeParameterDiscoveryRes_isUsed = ChargeParameterDiscoveryRes_isUsed
        struct.ServiceDetailReq_isUsed = ServiceDetailReq_isUsed
        struct.ServiceDetailRes_isUsed = ServiceDetailRes_isUsed
        struct.DC_EVSEStatus_isUsed = DC_EVSEStatus_isUsed
        struct.RelativeTimeInterval_isUsed = RelativeTimeInterval_isUsed
        struct.SalesTariffEntry_isUsed = SalesTariffEntry_isUsed
        struct.DC_EVPowerDeliveryParameter_isUsed = DC_EVPowerDeliveryParameter_isUsed
        struct.SASchedules_isUsed = SASchedules_isUsed
        struct.AC_EVChargeParameter_isUsed = AC_EVChargeParameter_isUsed
        struct.SAScheduleList_isUsed = SAScheduleList_isUsed
        struct.DC_EVStatus_isUsed = DC_EVStatus_isUsed
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
        struct._warning_ = _warning_
        return struct


    def iso1EXISchemaInformedElementFragmentGrammar(Id: str="",
                                                    Id_isUsed: int=0,
                                                    CHARACTERS_GENERIC: str="",
                                                    CHARACTERS_GENERIC_isUsed: int=0,
                                                    _warning_: int=0):
        
        converted_id = OpenV2GUtils.convert_to_array_type_characters(val=Id, size=exiElementFrag_Id_CHARACTERS_SIZE)
        converted_characters_generic = OpenV2GUtils.convert_to_array_type_characters(val=CHARACTERS_GENERIC, size=exiElementFrag_CHARACTERS_GENERIC_CHARACTERS_SIZE)
        struct = iso1EXISchemaInformedElementFragmentGrammar()
        struct.Id.characters = converted_id
        struct.Id.charactersLen = len(Id)
        struct.Id_isUsed = Id_isUsed
        struct.CHARACTERS_GENERIC.characters = converted_characters_generic
        struct.CHARACTERS_GENERIC.charactersLen = len(CHARACTERS_GENERIC)
        struct.CHARACTERS_GENERIC_isUsed = CHARACTERS_GENERIC_isUsed
        struct._warning_ = _warning_
        return struct
        