from asyncio import protocols
from audioop import mul
from dis import Instruction
from inspect import Parameter, signature
import unittest
from pkg_resources import declare_namespace

from requests import Response
from open_v2g_utils import OpenV2GUtils
from open_v2g import OpenV2G
from open_v2g_structs import *
from open_v2g_constants import *
from open_v2g_struct_declarator import OpenV2GStructDeclarator


class OpenV2GTester(unittest.TestCase):
    def setUp(self):
        self.ov2g = OpenV2G()

    # ---------- appHandshake ---------- #
    # open_v2g/source/appHandshake/appHandEXIDatatypes.c
    def test_init_appHandEXIDocument(self):
        print("\n[+] Testing init_appHandEXIDocument")

        exi_doc = OpenV2GStructDeclarator.appHandEXIDocument(
            supportedAppProtocolReq_isUsed=1,
            supportedAppProtocolRes_isUsed=1,
        )

        # Check whether the exi_doc is well updated
        self.ov2g.init_appHandEXIDocument(exiDoc=exi_doc)
        
        assert exi_doc.supportedAppProtocolReq_isUsed == 0
        assert exi_doc.supportedAppProtocolRes_isUsed == 0
        print("[*] OK")

    def test_init_appHandAppProtocolType(self):
        print("\n[+] Testing init_appHandAppProtocolType")

        app_protocol = OpenV2GStructDeclarator.appHandAppProtocolType(
            ProtocolNamespace="urn:iso:15118:2:2010:MsgDef",
            VersionNumberMajor=1,
            VersionNumberMinor=0,
            SchemaID=1,
            Priority=1,
        )

        self.ov2g.init_appHandAppProtocolType(appHandAppProtocolType=app_protocol)

        assert app_protocol.VersionNumberMajor == 1
        assert app_protocol.VersionNumberMinor == 0
        assert app_protocol.SchemaID == 1
        assert app_protocol.Priority == 1
        assert len(app_protocol.ProtocolNamespace.characters) == appHandAppProtocolType_ProtocolNamespace_CHARACTERS_SIZE

        print("[*] OK")

    def test_init_appHandAnonType_supportedAppProtocolReq(self):
        print("\n[+] Testing init_appHandAnonType_supportedAppProtocolReq")

        supported_app_protocol_req = OpenV2GStructDeclarator.appHandAnonType_supportedAppProtocolReq(
            AppProtocol=[
                OpenV2GStructDeclarator.appHandAppProtocolType(
                    ProtocolNamespace="urn:iso:15118:2:2010:MsgDef",
                    VersionNumberMajor=1,
                    VersionNumberMinor=0,
                    SchemaID=1,
                    Priority=1,
                )
            ]
        )

        self.ov2g.init_appHandAnonType_supportedAppProtocolReq(appHandAnonType_supportedAppProtocolReq=supported_app_protocol_req)

        assert len(list(supported_app_protocol_req.AppProtocol.array)) == appHandAnonType_supportedAppProtocolReq_AppProtocol_ARRAY_SIZE
        assert supported_app_protocol_req.AppProtocol.arrayLen == 0
        print("[*] OK")

    def test_init_appHandAnonType_supportedAppProtocolRes(self):
        print("\n[+] Testing init_appHandAnonType_supportedAppProtocolRes")

        print(f"[Python] {sizeof(appHandAnonType_supportedAppProtocolRes)=}")

        supported_app_protocol_res = OpenV2GStructDeclarator.appHandAnonType_supportedAppProtocolRes(
            ResponseCode=appHandresponseCodeType_Failed_NoNegotiation,
            SchemaID=2,
            SchemaID_isUsed=1
        )
        
        self.ov2g.init_appHandAnonType_supportedAppProtocolRes(appHandAnonType_supportedAppProtocolRes=supported_app_protocol_res)

        assert supported_app_protocol_res.SchemaID_isUsed == 0

        print("[*] OK")


    # open_v2g/source/appHandshake/appHandEXIDatatypesDecoder.c
    # open_v2g/source/appHandshake/appHandEXIDatatypesEncoder.c
    # open_v2g/source/transport/v2gtp.c
    # open_v2g/source/codec/*
    def test_apphandshake(self):
        print("\n[+] Testing apphandshake")

        buffer1 = (c_ubyte*256)()
        buffer2 = (c_ubyte*256)()

        size = c_size_t(256)
        pos1 = c_size_t(8)
        pos2 = c_size_t(0)

        buffer_byte = c_uint8(0)
        buffer_capacity = c_uint8(256)
        # encode request
        stream1 = OpenV2GStructDeclarator.bitstream_t(
            size=size,
            data=buffer1,
            pos=pos1,
            buffer=buffer_byte,
            capacity=buffer_capacity
        )

        # encode response
        stream2 = OpenV2GStructDeclarator.bitstream_t(
            size=size,
            data=buffer2,
            pos=pos2,
            buffer=buffer_byte,
            capacity=buffer_capacity
        )

        ns0 = "urn:iso:15118:2:2010:MsgDef"
        ns1 = "urn:din:70121:2012:MsgDef"

        handshake = OpenV2GStructDeclarator.appHandEXIDocument()
        handshakeResp = OpenV2GStructDeclarator.appHandEXIDocument()

        self.ov2g.init_appHandEXIDocument(handshake)

        handshake.supportedAppProtocolReq_isUsed = 1
        handshake.supportedAppProtocolReq.AppProtocol.arrayLen = 2

        handshake.supportedAppProtocolReq.AppProtocol.array[0].ProtocolNamespace.charactersLen = OpenV2GUtils.writeStringToEXIString(ns0, handshake.supportedAppProtocolReq.AppProtocol.array[0].ProtocolNamespace.characters)
        handshake.supportedAppProtocolReq.AppProtocol.array[0].SchemaID = 1
        handshake.supportedAppProtocolReq.AppProtocol.array[0].VersionNumberMajor = 1
        handshake.supportedAppProtocolReq.AppProtocol.array[0].VersionNumberMinor = 0
        handshake.supportedAppProtocolReq.AppProtocol.array[0].Priority = 1

        handshake.supportedAppProtocolReq.AppProtocol.array[1].ProtocolNamespace.charactersLen = OpenV2GUtils.writeStringToEXIString(ns1, handshake.supportedAppProtocolReq.AppProtocol.array[1].ProtocolNamespace.characters)
        handshake.supportedAppProtocolReq.AppProtocol.array[1].SchemaID = 2
        handshake.supportedAppProtocolReq.AppProtocol.array[1].VersionNumberMajor = 1
        handshake.supportedAppProtocolReq.AppProtocol.array[1].VersionNumberMinor = 0
        handshake.supportedAppProtocolReq.AppProtocol.array[1].Priority = 2
        
        print("----- FIRST -----")
        print(f"[Python][before encode] pos1 = {pos1.value}")
        print(f"[Python][before encode] buffer1 = {[hex(b) for b in buffer1[:pos1.value]]}")
        errn = self.ov2g.encode_appHandExiDocument(stream=stream1, exiDoc=handshake)
        print(f"[Python] errn[encode_appHandExiDocument]: {errn}")
        print(f"[Python][after encode] pos1 = {pos1.value}")
        print(f"[Python][after encode] buffer1 = {[hex(b) for b in buffer1[:pos1.value]]}")
        print()

        if errn == 0:
            errn = self.ov2g.write_v2gtpHeader(stream1.data, pos1.value-V2GTP_HEADER_LENGTH, V2GTP_EXI_TYPE) 
            print(f"[Python] errn[write_v2gtpHeader]: {errn}")
            print(f"[Python][after write_v2gtpheader] pos1 = {pos1.value}")
            print(f"[Python][after write_v2gtpheader] buffer1 = {[hex(b) for b in buffer1[:pos1.value]]}")
            print()

            if errn == 0:
                print(f"EV side: send message to the EVSE")

        if errn == 0:
            exiDoc = OpenV2GStructDeclarator.appHandEXIDocument()

            payloadLength = c_uint32()

            errn = self.ov2g.read_v2gtpHeader(inStream=stream1.data, payloadLength=pointer(payloadLength))
            print(f"[Python] errn[read_v2gtpHeader]: {errn}")
            print(f"[Python][after read_v2gtpheader] payloadLength = {payloadLength.value}")
            print()

            pos1 = c_size_t(8)
            if errn == 0:
                stream1.pos = pointer(pos1)

                errn = self.ov2g.decode_appHandExiDocument(stream=stream1, exiDoc=exiDoc)
                print(f"[Python] errn[decode_appHandExiDocument]: {errn}")
                assert errn == 0             


        # check list of application handhsake protocols of the EV

        print()
        for i in range(exiDoc.supportedAppProtocolReq.AppProtocol.arrayLen):
            protocol_namespace = OpenV2GUtils.EXIStringToASCIIString(exiDoc.supportedAppProtocolReq.AppProtocol.array[i].ProtocolNamespace.characters, exiDoc.supportedAppProtocolReq.AppProtocol.array[i].ProtocolNamespace.charactersLen)
            version_number_major = exiDoc.supportedAppProtocolReq.AppProtocol.array[i].VersionNumberMajor
            version_number_minor = exiDoc.supportedAppProtocolReq.AppProtocol.array[i].VersionNumberMinor
            schema_id = exiDoc.supportedAppProtocolReq.AppProtocol.array[i].SchemaID
            priority = exiDoc.supportedAppProtocolReq.AppProtocol.array[i].Priority

            print(f"\tProtocol entry #={i+1}")
            print(f"\t\tProtocolNamespace={protocol_namespace}")
            print(f"\t\tVersion=[{version_number_minor}, {version_number_major}]")
            print(f"\t\tSchemaID={schema_id}")
            print(f"\t\tPriority={priority}")
            print()


        print("----- SECOND -----")
        appHandResp = OpenV2GStructDeclarator.appHandEXIDocument()
        self.ov2g.init_appHandEXIDocument(exiDoc=appHandResp)

        appHandResp.supportedAppProtocolRes_isUsed = 1
        appHandResp.supportedAppProtocolRes.ResponseCode = appHandresponseCodeType_OK_SuccessfulNegotiation
        appHandResp.supportedAppProtocolRes.SchemaID = exiDoc.supportedAppProtocolReq.AppProtocol.array[0].SchemaID
        appHandResp.supportedAppProtocolRes.SchemaID_isUsed = 1

        pos2 = c_size_t(V2GTP_HEADER_LENGTH)
        stream2.pos = pointer(pos2)

        errn = self.ov2g.encode_appHandExiDocument(stream=stream2, exiDoc=appHandResp)

        print(f"[Python] errn[encode_appHandExiDocument]: {errn}")
        print(f"[Python][after encode_appHandExiDocument] pos2 = {pos2.value}")
        print(f"[Python][after encode_appHandExiDocument] buffer2 = {[hex(b) for b in buffer2[:pos2.value]]}")
        print()        

        if errn == 0:
            errn = self.ov2g.write_v2gtpHeader(stream2.data, pos2.value - V2GTP_HEADER_LENGTH, V2GTP_EXI_TYPE)
            print(f"[Python] errn[write_v2gtpHeader]: {errn}")
            print(f"[Python][after write_v2gtpheader] pos2 = {pos2.value}")
            print(f"[Python][after write_v2gtpheader] buffer2 = {[hex(b) for b in buffer2[:pos2.value]]}")
            print()        

        errn = self.ov2g.read_v2gtpHeader(inStream=stream2.data, payloadLength=pointer(payloadLength))
        print(f"[Python] errn[read_v2gtpHeader]: {errn}")
        print(f"[Python][after read_v2gtpheader] payloadLength = {payloadLength.value}")

        if errn == 0:
            pos2 = c_size_t(V2GTP_HEADER_LENGTH)
            stream2.pos = pointer(pos2)

            print(f"[Python][before decode_appHandExiDocument] buffer2 = {[hex(b) for b in buffer2[:pos2.value]]}")
            errn = self.ov2g.decode_appHandExiDocument(stream=stream2, exiDoc=handshakeResp)
            print(f"[Python] errn[decode_appHandExiDocument]: {errn}")

            if errn == 0:
                print("EV side: Response of the EVSE")

                if(handshakeResp.supportedAppProtocolRes.ResponseCode == appHandresponseCodeType_OK_SuccessfulNegotiation):
                    print(f"ResponseCode={handshakeResp.supportedAppProtocolRes.ResponseCode}")
                    print(f"SchemaID={handshakeResp.supportedAppProtocolRes.SchemaID}")
                    print(f"SchemaID_isUsed={handshakeResp.supportedAppProtocolRes.SchemaID_isUsed}")
        
        
        assert errn == 0

        print("[*] OK")

    # ---------- din ---------- #
    # open_v2g/source/din/dinEXIDataTypes.c
    # Validated
    def test_init_dinSessionSetupReqType(self):
        print("\n[+] Testing init_dinSessionSetupReqType")

        session_setup_req_type = OpenV2GStructDeclarator.dinSessionSetupReqType(EVCCID=1)

        self.ov2g.init_dinSessionSetupReqType(dinSessionSetupReqType=session_setup_req_type)

        print("[*] OK")

    # Validated
    def test_init_dinEVSEStatusType(self):
        print("\n[+] Testing init_dinEVSEStatusType")

        evse_status_type = OpenV2GStructDeclarator.dinEVSEStatusType()

        self.ov2g.init_dinEVSEStatusType(dinEVSEStatusType=evse_status_type)

        print("[*] OK")


    # Validated        
    def test_init_dinAC_EVSEStatusType(self):
        print("\n[+] Testing init_dinEVSEStatusType")

        ac_evse_status_type = OpenV2GStructDeclarator.dinAC_EVSEStatusType(
            PowerSwitchClosed=1,
            RCD=1,
            NotificationMaxDelay=10,
            EVSENotification=1
        )

        # print(f"[Python] pointer ac_evse_status_type = {byref(ac_evse_status_type)}")
        # print(f"[Python] sizeof dinAC_EVSEStatusType = {sizeof(dinAC_EVSEStatusType)}")

        self.ov2g.init_dinAC_EVSEStatusType(dinAC_EVSEStatusType=ac_evse_status_type)

        print("[*] OK")
    
    # Validated
    def test_init_dinDC_EVSEStatusType(self):
        print("\n[+] Testing init_dinEVSEStatusType")

        dc_evse_status_type = OpenV2GStructDeclarator.dinDC_EVSEStatusType(
            EVSEIsolationStatus=dinisolationLevelType_Valid,
            EVSEIsolationStatus_isUsed=1,
            EVSEStatusCode=dinDC_EVSEStatusCodeType_EVSE_Ready,
            NotificationMaxDelay=10,
            EVSENotification=1
        )

        print(f"[Python] pointer ac_evse_status_type = {byref(dc_evse_status_type)}")
        print(f"[Python] sizeof dinAC_EVSEStatusType = {sizeof(dinDC_EVSEStatusType)}")

        self.ov2g.init_dinDC_EVSEStatusType(dinDC_EVSEStatusType=dc_evse_status_type)

        assert dc_evse_status_type.EVSEIsolationStatus_isUsed == 0

        print("[*] OK")

    # Validated
    def test_init_dinPowerDeliveryResType(self):
        print("\n[+] Testing init_dinPowerDeliveryResType")


        power_delivery_res_type = OpenV2GStructDeclarator.dinPowerDeliveryResType(
            ResponseCode=dinresponseCodeType_OK,
            EVSEStatus=OpenV2GStructDeclarator.dinEVSEStatusType(),
            EVSEStatus_isUsed=1,
            AC_EVSEStatus=OpenV2GStructDeclarator.dinAC_EVSEStatusType(PowerSwitchClosed=1, RCD=10, NotificationMaxDelay=20, EVSENotification=4),
            AC_EVSEStatus_isUsed=1,
            DC_EVSEStatus=OpenV2GStructDeclarator.dinDC_EVSEStatusType(EVSEIsolationStatus=10, EVSEIsolationStatus_isUsed=1, EVSEStatusCode=dinDC_EVSEStatusCodeType_EVSE_Ready, NotificationMaxDelay=10, EVSENotification=1),
            DC_EVSEStatus_isUsed=1,
        )

        # print(f"[Python] sizeof dinAC_EVSEStatusType = {sizeof(dinPowerDeliveryResType)}")
        # print(f"[Python] pointer power_delivery_res_type = {byref(power_delivery_res_type)}")

        self.ov2g.init_dinPowerDeliveryResType(dinPowerDeliveryResType=power_delivery_res_type)

        assert power_delivery_res_type.EVSEStatus_isUsed == 0
        assert power_delivery_res_type.AC_EVSEStatus_isUsed == 0
        assert power_delivery_res_type.DC_EVSEStatus_isUsed == 0
        
        print("[*] OK")

    # Validated
    def test_init_dinPhysicalValueType(self):
        print("\n[+] Testing init_dinPhysicalValueType")

        physicalValue = OpenV2GStructDeclarator.dinPhysicalValueType(
            Multiplier=2, 
            Unit=dinunitSymbolType_Ah, 
            Unit_isUsed=1, 
            Value=12
        )

        # print(f"{sizeof(dinPhysicalValueType)=}")
        # for field in dinPhysicalValueType._fields_:
        #     field_name = field[0]
        #     field_class = field[1]

        #     if "_isUsed" not in field_name:
        #         print(f"[Python] sizeof({field_name}) = {sizeof(field_class)}")

        # print(f"[Python] {dinPhysicalValueType.Multiplier.offset=}")
        # print(f"[Python] {dinPhysicalValueType.Unit.offset=}")
        # print(f"[Python] {dinPhysicalValueType.Unit_isUsed.offset=}")
        # print(f"[Python] {dinPhysicalValueType.Value.offset=}")


        self.ov2g.init_dinPhysicalValueType(dinPhysicalValueType=physicalValue)

        assert physicalValue.Unit_isUsed == 0

        print("[*] OK")

    # Validated
    def test_init_dinParameterType(self):
        print("\n[+] Testing init_dinParameterType")
        
        parameter_type = OpenV2GStructDeclarator.dinParameterType(
            Name="RandomParameter",
            ValueType=dinvalueType_int,
            boolValue=1,
            boolValue_isUsed=1,
            byteValue=8,
            byteValue_isUsed=1,
            shortValue=16,
            shortValue_isUsed=1,
            intValue=32,
            intValue_isUsed=1,
            physicalValue=OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=2, Unit=dinunitSymbolType_Ah, Unit_isUsed=1, Value=12),
            physicalValue_isUsed=1,
            stringValue="This is a string",
            stringValue_isUsed=1

        )

        # print("\n[*] OK")
        
        # print(f"[Python] sizeof dinParameterType = {sizeof(dinParameterType)}")


        # for field in dinParameterType._fields_:
        #     field_name = field[0]
        #     field_class = field[1]

        #     if "_isUsed" not in field_name:
        #         print(f"[Python] sizeof({field_name}) = {sizeof(field_class)}")

        # print(f"[Python] offset dinParameterType.Name = {dinParameterType.Name.offset}")
        # print(f"[Python] offset dinParameterType.ValueType = {dinParameterType.ValueType.offset}")
        # print(f"[Python] offset dinParameterType.boolValue = {dinParameterType.boolValue.offset}")
        # print(f"[Python] offset dinParameterType.boolValue_isUsed = {dinParameterType.boolValue_isUsed.offset}")
        # print(f"[Python] offset dinParameterType.shortValue = {dinParameterType.shortValue.offset}")
        # print(f"[Python] offset dinParameterType.shortValue_isUsed = {dinParameterType.shortValue_isUsed.offset}")
        # print(f"[Python] offset dinParameterType.intValue = {dinParameterType.intValue.offset}")
        # print(f"[Python] offset dinParameterType.intValue_isUsed = {dinParameterType.intValue_isUsed.offset}")
        # print(f"[Python] offset dinParameterType.physicalValue = {dinParameterType.physicalValue.offset}")
        # print(f"[Python] offset dinParameterType.physicalValue_isUsed = {dinParameterType.physicalValue_isUsed.offset}")
        # print(f"[Python] offset dinParameterType.stringValue = {dinParameterType.stringValue.offset}")
        # print(f"[Python] offset dinParameterType.stringValue_isUsed = {dinParameterType.stringValue_isUsed.offset}")


        self.ov2g.init_dinParameterType(dinParameterType=parameter_type)

        assert parameter_type.boolValue_isUsed == 0
        assert parameter_type.byteValue_isUsed == 0
        assert parameter_type.shortValue_isUsed == 0
        assert parameter_type.intValue_isUsed == 0
        assert parameter_type.physicalValue_isUsed == 0
        assert parameter_type.stringValue_isUsed == 0

    # Validated
    def test_init_dinParameterSetType(self):
        print("\n[+] Testing init_dinParameterSetType")

        parameter_set_type = OpenV2GStructDeclarator.dinParameterSetType(
            ParameterSetID=1,
            Parameter=[
                OpenV2GStructDeclarator.dinParameterType(
                    Name="Voltage",
                    ValueType=dinvalueType_int,
                    physicalValue=OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=dinunitSymbolType_V, Unit_isUsed=1, Value=230),
                    physicalValue_isUsed=1,
                ),
                OpenV2GStructDeclarator.dinParameterType(
                    Name="Current",
                    ValueType=dinvalueType_int,
                    physicalValue=OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=dinunitSymbolType_A, Unit_isUsed=1, Value=6),
                    physicalValue_isUsed=1,
                ),
                
            ]
        )

        # print(f"[Python] sizeof dinParameterSetType = {sizeof(dinParameterSetType)}")


        # for field in dinParameterSetType._fields_:
        #     field_name = field[0]
        #     field_class = field[1]

        #     if "_isUsed" not in field_name:
        #         print(f"[Python] sizeof({field_name}) = {sizeof(field_class)}")

        # print(f"[Python] {dinParameterSetType.ParameterSetID.offset=}")
        # print(f"[Python] {dinParameterSetType.Parameter.offset=}")


        self.ov2g.init_dinParameterSetType(dinParameterSetType=parameter_set_type)

        assert parameter_set_type.Parameter.arrayLen == 0


        print("[*] OK")

    # Validated
    def test_init_dinServiceParameterListType(self):
        print("\n[+] Testing init_dinServiceParameterListType")
        
        service_parameter_list_type = OpenV2GStructDeclarator.dinServiceParameterListType(
            ParameterSet=[
                OpenV2GStructDeclarator.dinParameterSetType(
                    ParameterSetID=1,
                    Parameter=[
                        OpenV2GStructDeclarator.dinParameterType(
                            Name="Voltage",
                            ValueType=dinvalueType_int,
                            physicalValue=OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=dinunitSymbolType_V, Unit_isUsed=1, Value=230),
                            physicalValue_isUsed=1,
                        ),
                        OpenV2GStructDeclarator.dinParameterType(
                            Name="Current",
                            ValueType=dinvalueType_int,
                            physicalValue=OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=dinunitSymbolType_A, Unit_isUsed=1, Value=6),
                            physicalValue_isUsed=1,
                        ),
                    ]
                ),

                OpenV2GStructDeclarator.dinParameterSetType(
                    ParameterSetID=2,
                    Parameter=[
                        OpenV2GStructDeclarator.dinParameterType(
                            Name="Tensao",
                            ValueType=dinvalueType_int,
                            physicalValue=OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=dinunitSymbolType_V, Unit_isUsed=1, Value=230),
                            physicalValue_isUsed=1,
                        ),
                        OpenV2GStructDeclarator.dinParameterType(
                            Name="Intensidade",
                            ValueType=dinvalueType_int,
                            physicalValue=OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=dinunitSymbolType_A, Unit_isUsed=1, Value=6),
                            physicalValue_isUsed=1,
                        ),
                    ]
                ),
            ]
        )


        # print(f"[Python] {sizeof(dinServiceParameterListType)=}")

        self.ov2g.init_dinServiceParameterListType(dinServiceParameterListType=service_parameter_list_type)
        
        assert service_parameter_list_type.ParameterSet.arrayLen == 0

        print("[*] OK")

    # Validated
    def test_init_dinServiceDetailResType(self):
        print("\n[+] Testing init_dinServiceDetailResType")
        
        service_detail_res_type = OpenV2GStructDeclarator.dinServiceDetailResType(
            ResponseCode=dinresponseCodeType_OK_NewSessionEstablished,
            ServiceID=1,
            ServiceParameterList=OpenV2GStructDeclarator.dinServiceParameterListType(
                ParameterSet=[
                    OpenV2GStructDeclarator.dinParameterSetType(
                        ParameterSetID=1,
                        Parameter=[
                            OpenV2GStructDeclarator.dinParameterType(
                                Name="Voltage",
                                ValueType=dinvalueType_int,
                                physicalValue=OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=dinunitSymbolType_V, Unit_isUsed=1, Value=230),
                                physicalValue_isUsed=1,
                            ),
                            OpenV2GStructDeclarator.dinParameterType(
                                Name="Current",
                                ValueType=dinvalueType_int,
                                physicalValue=OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=dinunitSymbolType_A, Unit_isUsed=1, Value=6),
                                physicalValue_isUsed=1,
                            ),
                        ]
                    ),

                    OpenV2GStructDeclarator.dinParameterSetType(
                        ParameterSetID=2,
                        Parameter=[
                            OpenV2GStructDeclarator.dinParameterType(
                                Name="Tensao",
                                ValueType=dinvalueType_int,
                                physicalValue=OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=dinunitSymbolType_V, Unit_isUsed=1, Value=230),
                                physicalValue_isUsed=1,
                            ),
                            OpenV2GStructDeclarator.dinParameterType(
                                Name="Intensidade",
                                ValueType=dinvalueType_int,
                                physicalValue=OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=dinunitSymbolType_A, Unit_isUsed=1, Value=6),
                                physicalValue_isUsed=1,
                            ),
                        ]
                    ),
                ]
            ),
            ServiceParameterList_isUsed=1
        )

        # print(f"[Python] {sizeof(dinServiceDetailResType)}")
        self.ov2g.init_dinServiceDetailResType(dinServiceDetailResType=service_detail_res_type)

        assert service_detail_res_type.ServiceParameterList_isUsed == 0

        print("[*] OK")

    # Validated
    def test_init_dinWeldingDetectionResType(self):
        print("\n[+] Testing init_dinWeldingDetectionResType")

        welding_detection_res_type = OpenV2GStructDeclarator.dinWeldingDetectionResType(
            ResponseCode=dinresponseCodeType_FAILED_ChallengeInvalid,
            DC_EVSEStatus=OpenV2GStructDeclarator.dinDC_EVSEStatusType(
                EVSEIsolationStatus=dinisolationLevelType_Fault,
                EVSEIsolationStatus_isUsed=1,
                EVSEStatusCode=dinDC_EVSEStatusCodeType_EVSE_IsolationMonitoringActive,
                NotificationMaxDelay=10,
                EVSENotification=2
            ),
            EVSEPresentVoltage=OpenV2GStructDeclarator.dinPhysicalValueType(
                Multiplier=1,
                Unit=dinunitSymbolType_V,
                Unit_isUsed=1,
                Value=230
            )
        )

        print(f"[Python] {sizeof(dinWeldingDetectionResType)=}")

        self.ov2g.init_dinWeldingDetectionResType(dinWeldingDetectionResType=welding_detection_res_type)

        print("[*] OK")

    # Validated
    def test_init_dinContractAuthenticationResType(self):
        print("\n[+] Testing init_dinContractAuthenticationResType")

        contract_authenticatio_res_type = OpenV2GStructDeclarator.dinContractAuthenticationResType(
            ResponseCode=dinresponseCodeType_FAILED_CertChainError,
            EVSEProcessing=dinEVSEProcessingType_Ongoing
        )

        print(f"[Python] {sizeof(dinContractAuthenticationResType)=}")

        self.ov2g.init_dinContractAuthenticationResType(dinContractAuthenticationResType=contract_authenticatio_res_type)

        print("[*] OK")

    
    # Validated
    def test_init_dinCanonicalizationMethodType(self):
        print("\n[+] Testing init_dinCanonicalizationMethodType")

        canonicalization_method_type = OpenV2GStructDeclarator.dinCanonicalizationMethodType(
            Algorithm="SHA256",
            ANY="UNGA",
            ANY_isUsed=1
        )

        print(f"{sizeof(dinCanonicalizationMethodType)=}")

        self.ov2g.init_dinCanonicalizationMethodType(dinCanonicalizationMethodType=canonicalization_method_type)

        assert canonicalization_method_type.ANY_isUsed == 0
        print("[*] OK")


    # Validated
    def test_init_dinSPKIDataType(self):
        print("\n[+] Testing init_dinSPKIDataType")

        spki_data_type = OpenV2GStructDeclarator.dinSPKIDataType(
            SPKISexp=64, 
            ANY="Any String", 
            ANY_isUsed=1
        )

        # print(f"[Python] {sizeof(dinSPKIDataType)=}")

        self.ov2g.init_dinSPKIDataType(dinSPKIDataType=spki_data_type)

        assert spki_data_type.SPKISexp.arrayLen == 0
        assert spki_data_type.ANY_isUsed == 0

        print("[*] OK")


    # Validated
    def test_init_dinListOfRootCertificateIDsType(self):
        print("\n[+] Testing init_dinListOfRootCertificateIDsType")
        
        list_of_root_certificate_ids = OpenV2GStructDeclarator.dinListOfRootCertificateIDsType(
            RootCertificateID=[
                "ID1", "ID2", "ID3"
            ]
        )

        print(f"[Python] {sizeof(dinListOfRootCertificateIDsType)=}")

        self.ov2g.init_dinListOfRootCertificateIDsType(dinListOfRootCertificateIDsType=list_of_root_certificate_ids)

        assert list_of_root_certificate_ids.RootCertificateID.arrayLen == 0

        print("[*] OK")

    # Validated
    def test_init_dinSelectedServiceType(self):
        print("\n[+] Testing init_dinSelectedServiceType")
        
        selected_service_type = OpenV2GStructDeclarator.dinSelectedServiceType(
            ServiceID=2,
            ParameterSetID=3,
            ParameterSetID_isUsed=1
        )

        self.ov2g.init_dinSelectedServiceType(dinSelectedServiceType=selected_service_type)

        assert selected_service_type.ParameterSetID_isUsed == 0


        print("[*] OK")

    # Validated
    def test_init_dinSelectedServiceListType(self):
        print("\n[+] Testing init_dinSelectedServiceListType")

        selected_service_list = OpenV2GStructDeclarator.dinSelectedServiceListType(
            SelectedService=[
                OpenV2GStructDeclarator.dinSelectedServiceType(
                    ServiceID=1,
                    ParameterSetID=2,
                    ParameterSetID_isUsed=1
                ),
                OpenV2GStructDeclarator.dinSelectedServiceType(
                    ServiceID=2,
                    ParameterSetID=4,
                    ParameterSetID_isUsed=1
                ),
            ]
        )

        self.ov2g.init_dinSelectedServiceListType(dinSelectedServiceListType=selected_service_list)
        
        assert selected_service_list.SelectedService.arrayLen == 0

        print("[*] OK")

    # Validated
    def test_init_dinCurrentDemandResType(self):
        print("\n[+] Testing init_dinCurrentDemandResType")

        current_demand_res = OpenV2GStructDeclarator.dinCurrentDemandResType(
            ResponseCode=dinresponseCodeType_FAILED,
            DC_EVSEStatus=OpenV2GStructDeclarator.dinDC_EVSEStatusType(
                EVSEIsolationStatus=1,
                EVSEIsolationStatus_isUsed=1,
                EVSEStatusCode=2,
                NotificationMaxDelay=10,
                EVSENotification=1
            ),
            EVSEPresentVoltage=OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=dinunitSymbolType_V, Unit_isUsed=1, Value=230),
            EVSEPresentCurrent=OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=dinunitSymbolType_A, Unit_isUsed=1, Value=6),
            EVSECurrentLimitAchieved=1,
            EVSEVoltageLimitAchieved=1,
            EVSEPowerLimitAchieved=1,
            EVSEMaximumVoltageLimit=OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=dinunitSymbolType_V, Unit_isUsed=1, Value=400),
            EVSEMaximumVoltageLimit_isUsed=1,
            EVSEMaximumCurrentLimit=OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=dinunitSymbolType_A, Unit_isUsed=1, Value=200),
            EVSEMaximumCurrentLimit_isUsed=1,
            EVSEMaximumPowerLimit=OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=dinunitSymbolType_W, Unit_isUsed=1, Value=300),
            EVSEMaximumPowerLimit_isUsed=1
        )

        print(f"{sizeof(dinCurrentDemandResType)=}")

        self.ov2g.init_dinCurrentDemandResType(dinCurrentDemandResType=current_demand_res)
        
        assert current_demand_res.EVSEMaximumVoltageLimit_isUsed == 0
        assert current_demand_res.EVSEMaximumCurrentLimit_isUsed == 0
        assert current_demand_res.EVSEMaximumPowerLimit_isUsed == 0

        print("[*] OK")

    
    # Validated
    def test_init_dinTransformType(self):
        print("\n[+] Testing init_dinTransformType")

        transform_type = OpenV2GStructDeclarator.dinTransformType(
            Algorithm="SHA256",
            ANY="Any string",
            ANY_isUsed=1,
            XPath="/home/alex"
        )

        # print(f"[Python] {sizeof(dinTransformType)=}")

        self.ov2g.init_dinTransformType(dinTransformType=transform_type)
        
        assert transform_type.ANY_isUsed == 0
        assert transform_type.XPath.arrayLen == 0

        print("[*] OK")

    # Validated
    def test_init_dinAC_EVChargeParameterType(self):
        print("\n[+] Testing init_dinAC_EVChargeParameterType")

        ac_ev_charge_parameter_type = OpenV2GStructDeclarator.dinAC_EVChargeParameterType(
            DepartureTime=10,
            EAmount=OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=dinunitSymbolType_Wh, Unit_isUsed=1, Value=3000),
            EVMaxVoltage=OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=dinunitSymbolType_V, Unit_isUsed=1, Value=400),
            EVMaxCurrent=OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=dinunitSymbolType_A, Unit_isUsed=1, Value=10),
            EVMinCurrent=OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=dinunitSymbolType_A, Unit_isUsed=1, Value=1),
        ) 

        self.ov2g.init_dinAC_EVChargeParameterType(dinAC_EVChargeParameterType=ac_ev_charge_parameter_type)

        print("[*] OK")

    # Validated
    def test_init_dinX509IssuerSerialType(self):
        print("\n[+] Testing init_dinX509IssuerSerialType")

        x509_issuer_serial = OpenV2GStructDeclarator.dinX509IssuerSerialType(
            X509IssuerName="The issuer name",
            X509SerialNumber=28731,
        )

        self.ov2g.init_dinX509IssuerSerialType(dinX509IssuerSerialType=x509_issuer_serial)

        print("[*] OK")

    # Validated
    def test_init_dinX509DataType(self):
        print("\n[+] Testing init_dinX509DataType")

        x509_data = OpenV2GStructDeclarator.dinX509DataType(
            X509IssuerSerial=[
                OpenV2GStructDeclarator.dinX509IssuerSerialType(
                    X509IssuerName="The issuer name",
                    X509SerialNumber=28731,
                )
            ],
            X509SKI=37182,
            X509SubjectName="Subject Name",
            X509Certificate=39123819,
            X509CRL=231939,
            ANY="Anything",
            ANY_isUsed=1
        )

        self.ov2g.init_dinX509DataType(dinX509DataType=x509_data)

        assert x509_data.X509IssuerSerial.arrayLen == 0
        assert x509_data.X509SKI.arrayLen == 0
        assert x509_data.X509SubjectName.arrayLen == 0
        assert x509_data.X509Certificate.arrayLen == 0
        assert x509_data.X509CRL.arrayLen == 0
        assert x509_data.ANY_isUsed == 0
        
        print("[*] OK")

    # Validated
    def test_init_dinMeterInfoType(self):
        print("\n[+] Testing init_dinChargingStatusResType")

        meter_info = OpenV2GStructDeclarator.dinMeterInfoType(
            MeterID="AC_Meter1",
            MeterReading=OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=1, Unit_isUsed=1, Value=10),
            MeterReading_isUsed=1,
            SigMeterReading=3291,
            SigMeterReading_isUsed=1,
            MeterStatus=2,
            MeterStatus_isUsed=1,
            TMeter=321,
            TMeter_isUsed=1
        )
        # print(f"[Python] {sizeof(dinMeterInfoType)=}")

        # for field in dinMeterInfoType._fields_:
        #     field_name = field[0]
        #     field_class = field[1]

        #     if "_isUsed" not in field_name:
        #         print(f"[Python] sizeof {field_name} = {sizeof(field_class)}")
                
        # print(f"[Python] {dinMeterInfoType.MeterID.offset=}")
        # print(f"[Python] {dinMeterInfoType.MeterReading.offset=}")
        # print(f"[Python] {dinMeterInfoType.SigMeterReading.offset=}")
        # print(f"[Python] {dinMeterInfoType.MeterStatus.offset=}")
        # print(f"[Python] {dinMeterInfoType.TMeter.offset=}")

        self.ov2g.init_dinMeterInfoType(dinMeterInfoType=meter_info)

        assert meter_info.MeterReading_isUsed == 0
        assert meter_info.SigMeterReading_isUsed == 0
        assert meter_info.MeterStatus_isUsed == 0
        assert meter_info.TMeter_isUsed == 0
        print("[*] OK")
    
    # Validated
    def test_init_dinChargingStatusResType(self):
        print("\n[+] Testing init_dinChargingStatusResType")

        charging_status_res_type = OpenV2GStructDeclarator.dinChargingStatusResType(
            ResponseCode=4,
            EVSEID=12,
            SAScheduleTupleID=3,
            EVSEMaxCurrent=OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=dinunitSymbolType_A, Unit_isUsed=1, Value=100),
            EVSEMaxCurrent_isUsed=1,
            MeterInfo=OpenV2GStructDeclarator.dinMeterInfoType(
                MeterID="AC_Meter1",
                MeterReading=OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=1, Unit_isUsed=1, Value=10),
                MeterReading_isUsed=1,
                SigMeterReading=3291,
                SigMeterReading_isUsed=1,
                MeterStatus=2,
                MeterStatus_isUsed=1,
                TMeter=321,
                TMeter_isUsed=1
            ),
            MeterInfo_isUsed=1,
            ReceiptRequired=1,
            AC_EVSEStatus=OpenV2GStructDeclarator.dinAC_EVSEStatusType(
                PowerSwitchClosed=1,
                RCD=2,
                NotificationMaxDelay=10,
                EVSENotification=1
            )
        )

        # print(f"[Python] {sizeof(dinChargingStatusResType)=}")

        self.ov2g.init_dinChargingStatusResType(dinChargingStatusResType=charging_status_res_type)
        
        assert charging_status_res_type.EVSEMaxCurrent_isUsed == 0
        assert charging_status_res_type.MeterInfo_isUsed == 0

        print("[*] OK")

    # Validated
    def test_init_dinDC_EVStatusType(self):
        print("\n[+] Testing init_dinDC_EVStatusType")

        dc_ev_status_type = OpenV2GStructDeclarator.dinDC_EVStatusType(
            EVReady=1,
            EVCabinConditioning=2,
            EVCabinConditioning_isUsed=1,
            EVRESSConditioning=3,
            EVRESSConditioning_isUsed=1,
            EVErrorCode=4,
            EVRESSSOC=50
        )

        self.ov2g.init_dinDC_EVStatusType(dinDC_EVStatusType=dc_ev_status_type)

        assert dc_ev_status_type.EVCabinConditioning_isUsed == 0
        assert dc_ev_status_type.EVRESSConditioning_isUsed == 0


        print("[*] OK")

    # Validated
    def test_init_dinWeldingDetectionReqType(self):
        print("\n[+] Testing init_dinWeldingDetectionReqType")

        welding_detection_req_type = OpenV2GStructDeclarator.dinWeldingDetectionReqType(
            DC_EVStatus=OpenV2GStructDeclarator.dinDC_EVStatusType(
                EVReady=1,
                EVCabinConditioning=2,
                EVCabinConditioning_isUsed=1,
                EVRESSConditioning=3,
                EVRESSConditioning_isUsed=1,
                EVErrorCode=4,
                EVRESSSOC=50
            )
        )

        self.ov2g.init_dinWeldingDetectionReqType(dinWeldingDetectionReqType=welding_detection_req_type)

        print("[*] OK")

    # Validated
    def test_init_dinSignaturePropertyType(self):
        print("\n[+] Testing init_dinSignaturePropertyType")

        signature_property_type = OpenV2GStructDeclarator.dinSignaturePropertyType(
            Target="The target",
            Id="The id",
            Id_isUsed=1,
            ANY="Anything",
            ANY_isUsed=1
        )

        self.ov2g.init_dinSignaturePropertyType(dinSignaturePropertyType=signature_property_type)

        assert signature_property_type.Id_isUsed == 0
        assert signature_property_type.ANY_isUsed == 0

        print("[*] OK")

    # Validated
    def test_init_dinSignaturePropertiesType(self):
        print("\n[+] Testing init_dinSignaturePropertiesType")

        signature_properties_type = OpenV2GStructDeclarator.dinSignaturePropertiesType(
            Id="The main id",
            Id_isUsed=1,
            SignatureProperty=[
                OpenV2GStructDeclarator.dinSignaturePropertyType(
                    Target="The target",
                    Id="The id",
                    Id_isUsed=1,
                    ANY="Anything",
                    ANY_isUsed=1
                )
            ]
        )

        self.ov2g.init_dinSignaturePropertiesType(dinSignaturePropertiesType=signature_properties_type)

        assert signature_properties_type.Id_isUsed == 0
        assert signature_properties_type.SignatureProperty.arrayLen == 0
        
        print("[*] OK")

    # Validated
    def test_init_dinContractAuthenticationReqType(self):
        print("\n[+] Testing init_dinContractAuthenticationReqType")

        contract_authentication_req = OpenV2GStructDeclarator.dinContractAuthenticationReqType(
            Id="Contract ID",
            Id_isUsed=1,
            GenChallenge="The GEN Challenge",
            GenChallenge_isUsed=1
        )

        self.ov2g.init_dinContractAuthenticationReqType(dinContractAuthenticationReqType=contract_authentication_req)

        assert contract_authentication_req.Id_isUsed == 0
        assert contract_authentication_req.GenChallenge_isUsed == 0

        
        print("[*] OK")


    # Validated
    def test_init_dinDC_EVPowerDeliveryParameterType(self):
        print("\n[+] Testing init_dinDC_EVPowerDeliveryParameterType")

        dc_ev_power_delivery_parameter_type = OpenV2GStructDeclarator.dinDC_EVPowerDeliveryParameterType(
            DC_EVStatus=OpenV2GStructDeclarator.dinDC_EVStatusType(
                EVReady=1,
                EVCabinConditioning=2,
                EVCabinConditioning_isUsed=1,
                EVRESSConditioning=3,
                EVRESSConditioning_isUsed=1,
                EVErrorCode=4,
                EVRESSSOC=50
            ),
            BulkChargingComplete=1,
            BulkChargingComplete_isUsed=1,
            ChargingComplete=1
        )

        # print(f"[Python] {sizeof(dinDC_EVPowerDeliveryParameterType)=}")
        # print(f"[Python] {sizeof(dinDC_EVStatusType)=}")
        # print(f"[Python] {dinDC_EVPowerDeliveryParameterType.DC_EVStatus.offset=}")
        # print(f"[Python] {dinDC_EVPowerDeliveryParameterType.BulkChargingComplete.offset=}")
        # print(f"[Python] {dinDC_EVPowerDeliveryParameterType.BulkChargingComplete_isUsed.offset=}")
        # print(f"[Python] {dinDC_EVPowerDeliveryParameterType.ChargingComplete.offset=}")

        self.ov2g.init_dinDC_EVPowerDeliveryParameterType(dinDC_EVPowerDeliveryParameterType=dc_ev_power_delivery_parameter_type)

        assert dc_ev_power_delivery_parameter_type.BulkChargingComplete_isUsed == 0
        
        print("[*] OK")


    # Validated
    def test_init_dinEVSEChargeParameterType(self):
        print("\n[+] Testing init_dinEVSEChargeParameterType")

        evse_charge_parameter_type = OpenV2GStructDeclarator.dinEVSEChargeParameterType(
            noContent=1
        )

        self.ov2g.init_dinEVSEChargeParameterType(dinEVSEChargeParameterType=evse_charge_parameter_type)
        
        print("[*] OK")

    # Validated
    def test_init_dinCableCheckReqType(self):
        print("\n[+] Testing init_dinCableCheckReqType")

        cable_check_req = OpenV2GStructDeclarator.dinCableCheckReqType(
            DC_EVStatus=OpenV2GStructDeclarator.dinDC_EVStatusType(
                EVReady=1,
                EVCabinConditioning=2,
                EVCabinConditioning_isUsed=1,
                EVRESSConditioning=3,
                EVRESSConditioning_isUsed=1,
                EVErrorCode=4,
                EVRESSSOC=50
            ),
        )

        self.ov2g.init_dinCableCheckReqType(dinCableCheckReqType=cable_check_req)


        print("[*] OK")

    # Validated
    def test_init_dinDC_EVChargeParameterType(self):
        print("\n[+] Testing init_dinDC_EVChargeParameterType")

        dc_ev_charge_parameter_type = OpenV2GStructDeclarator.dinDC_EVChargeParameterType(
            DC_EVStatus=OpenV2GStructDeclarator.dinDC_EVStatusType(
                EVReady=1,
                EVCabinConditioning=2,
                EVCabinConditioning_isUsed=1,
                EVRESSConditioning=3,
                EVRESSConditioning_isUsed=1,
                EVErrorCode=4,
                EVRESSSOC=50
            ),
            EVMaximumCurrentLimit=OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=2, Unit_isUsed=1, Value=100),
            EVMaximumPowerLimit=OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=2, Unit_isUsed=1, Value=100),
            EVMaximumPowerLimit_isUsed=1,
            EVMaximumVoltageLimit=OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=2, Unit_isUsed=1, Value=100),
            EVEnergyCapacity=OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=2, Unit_isUsed=1, Value=100),
            EVEnergyCapacity_isUsed=1,
            EVEnergyRequest=OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=2, Unit_isUsed=1, Value=100),
            EVEnergyRequest_isUsed=1,
            FullSOC=50,
            FullSOC_isUsed=1,
            BulkSOC=40,
            BulkSOC_isUsed=1,
        )

        
        # print(f"[Python] {sizeof(dinDC_EVChargeParameterType)=}")

        self.ov2g.init_dinDC_EVChargeParameterType(dinDC_EVChargeParameterType=dc_ev_charge_parameter_type)

        assert dc_ev_charge_parameter_type.EVMaximumPowerLimit_isUsed == 0
        assert dc_ev_charge_parameter_type.EVEnergyCapacity_isUsed == 0
        assert dc_ev_charge_parameter_type.EVEnergyRequest_isUsed == 0
        assert dc_ev_charge_parameter_type.FullSOC_isUsed == 0
        assert dc_ev_charge_parameter_type.BulkSOC_isUsed == 0

        print("[*] OK")

    # Validated
    def test_init_dinRelativeTimeIntervalType(self):
        print("\n[+] Testing init_dinRelativeTimeIntervalType")

        relative_time_interval_type = OpenV2GStructDeclarator.dinRelativeTimeIntervalType(
            start=2,
            duration=10,
            duration_isUsed=1
        )

        self.ov2g.init_dinRelativeTimeIntervalType(dinRelativeTimeIntervalType=relative_time_interval_type)

        assert relative_time_interval_type.duration_isUsed == 0


        print("[*] OK")
 

    # Validated
    def test_init_dinIntervalType(self):
        print("\n[+] Testing init_dinIntervalType")

        interval_type = OpenV2GStructDeclarator.dinIntervalType(noContent=2)

        self.ov2g.init_dinIntervalType(dinIntervalType=interval_type)

        print("[*] OK")

    # Validated
    def test_init_dinPMaxScheduleEntryType(self):
        print("\n[+] Testing init_dinPMaxScheduleEntryType")
        
        pmax_schedule_entry = OpenV2GStructDeclarator.dinPMaxScheduleEntryType(
            TimeInterval=OpenV2GStructDeclarator.dinIntervalType(noContent=1),
            TimeInterval_isUsed=1,
            RelativeTimeInterval=OpenV2GStructDeclarator.dinRelativeTimeIntervalType(
                start=2,
                duration=10,
                duration_isUsed=1
            ),
            RelativeTimeInterval_isUsed=1,
            PMax=20
        )

        # print(f"[Python] {sizeof(dinPMaxScheduleEntryType)}")

        self.ov2g.init_dinPMaxScheduleEntryType(dinPMaxScheduleEntryType=pmax_schedule_entry)

        assert pmax_schedule_entry.TimeInterval_isUsed == 0
        assert pmax_schedule_entry.RelativeTimeInterval_isUsed == 0

        print("[*] OK")

    # Validated
    def test_init_dinPMaxScheduleType(self):
        print("\n[+] Testing init_dinPMaxScheduleType")

        pmax_schedule = OpenV2GStructDeclarator.dinPMaxScheduleType(
            PMaxScheduleID=2,
            PMaxScheduleEntry=[
                OpenV2GStructDeclarator.dinPMaxScheduleEntryType(
                    TimeInterval=OpenV2GStructDeclarator.dinIntervalType(noContent=1),
                    TimeInterval_isUsed=1,
                    RelativeTimeInterval=OpenV2GStructDeclarator.dinRelativeTimeIntervalType(
                        start=2,
                        duration=10,
                        duration_isUsed=1
                    ),
                    RelativeTimeInterval_isUsed=1,
                    PMax=20
                ),

                OpenV2GStructDeclarator.dinPMaxScheduleEntryType(
                    TimeInterval=OpenV2GStructDeclarator.dinIntervalType(noContent=1),
                    TimeInterval_isUsed=1,
                    RelativeTimeInterval=OpenV2GStructDeclarator.dinRelativeTimeIntervalType(
                        start=2,
                        duration=10,
                        duration_isUsed=1
                    ),
                    RelativeTimeInterval_isUsed=1,
                    PMax=30
                )

            ]
        )

        self.ov2g.init_dinPMaxScheduleType(dinPMaxScheduleType=pmax_schedule)

        assert pmax_schedule.PMaxScheduleEntry.arrayLen == 0

        print("[*] OK")
        
    # Validated
    def test_init_dinCostType(self):
        print("\n[+] Testing init_dinCostType")

        cost = OpenV2GStructDeclarator.dinCostType(
            costKind=2,
            amount=32,
            amountMultiplier=1,
            amountMultiplier_isUsed=1
        )

        # print(f"[Python] {sizeof(dinCostType)=}")
        self.ov2g.init_dinCostType(dinCostType=cost)

        assert cost.amountMultiplier_isUsed == 0

        print("[*] OK")

    # Validated
    def test_init_dinConsumptionCostType(self):
        print("\n[+] Testing init_dinConsumptionCostType")

        consumption_cost = OpenV2GStructDeclarator.dinConsumptionCostType(
            startValue=10,
            Cost=[
                OpenV2GStructDeclarator.dinCostType(
                    costKind=2,
                    amount=32,
                    amountMultiplier=1,
                    amountMultiplier_isUsed=1
                ),

                OpenV2GStructDeclarator.dinCostType(
                    costKind=2,
                    amount=48,
                    amountMultiplier=1,
                    amountMultiplier_isUsed=1
                )
            ]
        )

        self.ov2g.init_dinConsumptionCostType(dinConsumptionCostType=consumption_cost)

        assert consumption_cost.Cost.arrayLen == 0

        print("[*] OK")

    # Validated
    def test_init_dinSalesTariffEntryType(self):
        print("\n[+] Testing init_dinSalesTariffEntryType")

        sales_tariff_entry = OpenV2GStructDeclarator.dinSalesTariffEntryType(
            TimeInterval=OpenV2GStructDeclarator.dinIntervalType(noContent=1),
            TimeInteraval_isUsed=1,
            RelativeTimeInterval=OpenV2GStructDeclarator.dinRelativeTimeIntervalType(
                start=0,
                duration=10,
                duration_isUsed=1
            ),
            RelativeTimeInteraval_isUsed=1,
            EPriceLevel=2,
            ConsumptionCost=[
                OpenV2GStructDeclarator.dinConsumptionCostType(
                    startValue=10,
                    Cost=[
                        OpenV2GStructDeclarator.dinCostType(
                            costKind=2,
                            amount=32,
                            amountMultiplier=1,
                            amountMultiplier_isUsed=1
                        ),

                        OpenV2GStructDeclarator.dinCostType(
                            costKind=2,
                            amount=48,
                            amountMultiplier=1,
                            amountMultiplier_isUsed=1
                        )
                    ]
                )
            ],
        )

        # print(f"[Python] {sizeof(dinSalesTariffEntryType)=}")

        self.ov2g.init_dinSalesTariffEntryType(dinSalesTariffEntryType=sales_tariff_entry)

        assert sales_tariff_entry.TimeInterval_isUsed == 0
        assert sales_tariff_entry.RelativeTimeInterval_isUsed == 0
        assert sales_tariff_entry.ConsumptionCost.arrayLen == 0

        print("[*] OK")

    # Validated
    def test_init_dinSalesTariffType(self):
        print("\n[+] Testing init_dinSalesTariffType")

        sales_tariff = OpenV2GStructDeclarator.dinSalesTariffType(
            Id="ID1",
            SalesTariffID=2,
            SalesTariffDescription="The sales",
            SalesTariffDescription_isUsed=1,
            NumEPriceLevels=10,
            SalesTariffEntry=[
                OpenV2GStructDeclarator.dinSalesTariffEntryType(
                    TimeInterval=OpenV2GStructDeclarator.dinIntervalType(noContent=1),
                    TimeInteraval_isUsed=1,
                    RelativeTimeInterval=OpenV2GStructDeclarator.dinRelativeTimeIntervalType(
                        start=0,
                        duration=10,
                        duration_isUsed=1
                    ),
                    RelativeTimeInteraval_isUsed=1,
                    EPriceLevel=2,
                    ConsumptionCost=[
                        OpenV2GStructDeclarator.dinConsumptionCostType(
                            startValue=10,
                            Cost=[
                                OpenV2GStructDeclarator.dinCostType(
                                    costKind=2,
                                    amount=32,
                                    amountMultiplier=1,
                                    amountMultiplier_isUsed=1
                                ),

                                OpenV2GStructDeclarator.dinCostType(
                                    costKind=2,
                                    amount=48,
                                    amountMultiplier=1,
                                    amountMultiplier_isUsed=1
                                )
                            ]
                        )
                    ],
                )
            ]
        )

        self.ov2g.init_dinSalesTariffType(dinSalesTariffType=sales_tariff)

        assert sales_tariff.SalesTariffDescription_isUsed == 0
        assert sales_tariff.SalesTariffEntry.arrayLen == 0

        print("[*] OK")

    # Validated
    def test_init_dinSAScheduleTupleType(self):
        print("\n[+] Testing init_dinSAScheduleTupleType")
        
        sa_schedule_tuple = OpenV2GStructDeclarator.dinSAScheduleTupleType(
            SAScheduleTupleID=1,
            PMaxSchedule=OpenV2GStructDeclarator.dinPMaxScheduleType(
                PMaxScheduleID=2,
                PMaxScheduleEntry=[
                    OpenV2GStructDeclarator.dinPMaxScheduleEntryType(
                        TimeInterval=OpenV2GStructDeclarator.dinIntervalType(noContent=1),
                        TimeInterval_isUsed=1,
                        RelativeTimeInterval=OpenV2GStructDeclarator.dinRelativeTimeIntervalType(
                            start=2,
                            duration=10,
                            duration_isUsed=1
                        ),
                        RelativeTimeInterval_isUsed=1,
                        PMax=20
                    ),

                    OpenV2GStructDeclarator.dinPMaxScheduleEntryType(
                        TimeInterval=OpenV2GStructDeclarator.dinIntervalType(noContent=1),
                        TimeInterval_isUsed=1,
                        RelativeTimeInterval=OpenV2GStructDeclarator.dinRelativeTimeIntervalType(
                            start=2,
                            duration=10,
                            duration_isUsed=1
                        ),
                        RelativeTimeInterval_isUsed=1,
                        PMax=30
                    )

                ]
            ),

            SalesTariff=OpenV2GStructDeclarator.dinSalesTariffType(
                Id="ID1",
                SalesTariffID=2,
                SalesTariffDescription="The sales",
                SalesTariffDescription_isUsed=1,
                NumEPriceLevels=10,
                SalesTariffEntry=[
                    OpenV2GStructDeclarator.dinSalesTariffEntryType(
                        TimeInterval=OpenV2GStructDeclarator.dinIntervalType(noContent=1),
                        TimeInteraval_isUsed=1,
                        RelativeTimeInterval=OpenV2GStructDeclarator.dinRelativeTimeIntervalType(
                            start=0,
                            duration=10,
                            duration_isUsed=1
                        ),
                        RelativeTimeInteraval_isUsed=1,
                        EPriceLevel=2,
                        ConsumptionCost=[
                            OpenV2GStructDeclarator.dinConsumptionCostType(
                                startValue=10,
                                Cost=[
                                    OpenV2GStructDeclarator.dinCostType(
                                        costKind=2,
                                        amount=32,
                                        amountMultiplier=1,
                                        amountMultiplier_isUsed=1
                                    ),

                                    OpenV2GStructDeclarator.dinCostType(
                                        costKind=2,
                                        amount=48,
                                        amountMultiplier=1,
                                        amountMultiplier_isUsed=1
                                    )
                                ]
                            )
                        ],
                    )
                ]
            ),
            SalesTariff_isUsed=1
        )

        self.ov2g.init_dinSAScheduleTupleType(dinSAScheduleTupleType=sa_schedule_tuple)

        assert sa_schedule_tuple.SalesTariff_isUsed == 0

        print("[*] OK")

    # Validated
    def test_init_dinSAScheduleListType(self):
        print("\n[+] Testing init_dinSAScheduleListType")
        
        sa_schedule_tuple = OpenV2GStructDeclarator.dinSAScheduleTupleType(
            SAScheduleTupleID=1,
            PMaxSchedule=OpenV2GStructDeclarator.dinPMaxScheduleType(
                PMaxScheduleID=2,
                PMaxScheduleEntry=[
                    OpenV2GStructDeclarator.dinPMaxScheduleEntryType(
                        TimeInterval=OpenV2GStructDeclarator.dinIntervalType(noContent=1),
                        TimeInterval_isUsed=1,
                        RelativeTimeInterval=OpenV2GStructDeclarator.dinRelativeTimeIntervalType(
                            start=2,
                            duration=10,
                            duration_isUsed=1
                        ),
                        RelativeTimeInterval_isUsed=1,
                        PMax=20
                    ),

                    OpenV2GStructDeclarator.dinPMaxScheduleEntryType(
                        TimeInterval=OpenV2GStructDeclarator.dinIntervalType(noContent=1),
                        TimeInterval_isUsed=1,
                        RelativeTimeInterval=OpenV2GStructDeclarator.dinRelativeTimeIntervalType(
                            start=2,
                            duration=10,
                            duration_isUsed=1
                        ),
                        RelativeTimeInterval_isUsed=1,
                        PMax=30
                    )

                ]
            ),

            SalesTariff=OpenV2GStructDeclarator.dinSalesTariffType(
                Id="ID1",
                SalesTariffID=2,
                SalesTariffDescription="The sales",
                SalesTariffDescription_isUsed=1,
                NumEPriceLevels=10,
                SalesTariffEntry=[
                    OpenV2GStructDeclarator.dinSalesTariffEntryType(
                        TimeInterval=OpenV2GStructDeclarator.dinIntervalType(noContent=1),
                        TimeInteraval_isUsed=1,
                        RelativeTimeInterval=OpenV2GStructDeclarator.dinRelativeTimeIntervalType(
                            start=0,
                            duration=10,
                            duration_isUsed=1
                        ),
                        RelativeTimeInteraval_isUsed=1,
                        EPriceLevel=2,
                        ConsumptionCost=[
                            OpenV2GStructDeclarator.dinConsumptionCostType(
                                startValue=10,
                                Cost=[
                                    OpenV2GStructDeclarator.dinCostType(
                                        costKind=2,
                                        amount=32,
                                        amountMultiplier=1,
                                        amountMultiplier_isUsed=1
                                    ),

                                    OpenV2GStructDeclarator.dinCostType(
                                        costKind=2,
                                        amount=48,
                                        amountMultiplier=1,
                                        amountMultiplier_isUsed=1
                                    )
                                ]
                            )
                        ],
                    )
                ]
            ),
            SalesTariff_isUsed=1
        )

        sa_schedule_list = OpenV2GStructDeclarator.dinSAScheduleListType(
            SAScheduleTuple=[
                sa_schedule_tuple
            ]
        )

        self.ov2g.init_dinSAScheduleListType(dinSAScheduleListType=sa_schedule_list)

        assert sa_schedule_list.SAScheduleTuple.arrayLen == 0

        print("[*] OK")

    
    # Validated
    def test_init_dinServicePaymentSelectionReqType(self):
        print("\n[+] Testing init_dinServicePaymentSelectionReqType")

        service_payment_selection_req = OpenV2GStructDeclarator.dinServicePaymentSelectionReqType(
            SelectedPaymentOption=1,
            SelectedServiceList=OpenV2GStructDeclarator.dinSelectedServiceListType(
                SelectedService=[
                    OpenV2GStructDeclarator.dinSelectedServiceType(
                        ServiceID=1,
                        ParameterSetID=2,
                        ParameterSetID_isUsed=1
                    ),

                    OpenV2GStructDeclarator.dinSelectedServiceType(
                        ServiceID=2,
                        ParameterSetID=3,
                        ParameterSetID_isUsed=1
                    )
                ]
            )
        )

        self.ov2g.init_dinServicePaymentSelectionReqType(dinServicePaymentSelectionReqType=service_payment_selection_req)

        print("[*] OK")

    # Validated
    def test_init_dinEVStatusType(self):
        print("\n[*] Testing init_dinEVStatusType")

        ev_status = OpenV2GStructDeclarator.dinEVStatusType(noContent=1)

        self.ov2g.init_dinEVStatusType(dinEVStatusType=ev_status)

        print("[*] OK")

    # Validated
    def test_init_dinPreChargeResType(self):
        print("\n[+] Testing init_dinPreChargeResType")

        pre_charge_res = OpenV2GStructDeclarator.dinPreChargeResType(
            ResponseCode=2,
            DC_EVSEStatus=OpenV2GStructDeclarator.dinDC_EVSEStatusType(EVSEIsolationStatus=10, EVSEIsolationStatus_isUsed=1, EVSEStatusCode=dinDC_EVSEStatusCodeType_EVSE_Ready, NotificationMaxDelay=10, EVSENotification=1),
            EVSEPresentVoltage=OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=2, Unit_isUsed=1, Value=230)
        )


        self.ov2g.init_dinPreChargeResType(dinPreChargeResType=pre_charge_res)


        print("[*] OK")

    # Validated
    def test_init_dinDC_EVSEChargeParameterType(self):
        print("\n[+] Testing init_dinDC_EVSEChargeParameterType")

        dc_evse_charge_parameter = OpenV2GStructDeclarator.dinDC_EVSEChargeParameterType(
            DC_EVSEStatus= OpenV2GStructDeclarator.dinDC_EVSEStatusType(EVSEIsolationStatus=1, EVSEIsolationStatus_isUsed=1, EVSEStatusCode=2, NotificationMaxDelay=3, EVSENotification=4),
            EVSEMaximumCurrentLimit= OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=2, Unit_isUsed=1, Value=10),
            EVSEMaximumPowerLimit= OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=2, Unit_isUsed=1, Value=10),
            EVSEMaximumPowerLimit_isUsed=1,
            EVSEMaximumVoltageLimit= OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=2, Unit_isUsed=1, Value=10),
            EVSEMinimumCurrentLimit= OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=2, Unit_isUsed=1, Value=10),
            EVSEMinimumVoltageLimit= OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=2, Unit_isUsed=1, Value=10),
            EVSECurrentRegulationTolerance= OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=2, Unit_isUsed=1, Value=10),
            EVSECurrentRegulationTolerance_isUsed=1,
            EVSEPeakCurrentRipple= OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=2, Unit_isUsed=1, Value=10),
            EVSEEnergyToBeDelivered= OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=2, Unit_isUsed=1, Value=54),
            EVSEEnergyToBeDelivered_isUsed=1
        )

        self.ov2g.init_dinDC_EVSEChargeParameterType(dinDC_EVSEChargeParameterType=dc_evse_charge_parameter)

        assert dc_evse_charge_parameter.EVSEMaximumPowerLimit_isUsed == 0
        assert dc_evse_charge_parameter.EVSECurrentRegulationTolerance_isUsed == 0
        assert dc_evse_charge_parameter.EVSEEnergyToBeDelivered_isUsed == 0

        print("[*] OK")

    # Validated
    def test_init_dinPaymentDetailsResType(self):
        print("\n[+]Testing init_dinPaymentDetailsResType")

        payment_details_res = OpenV2GStructDeclarator.dinPaymentDetailsResType(
            ResponseCode=1,
            GenChallenge="GenChallenge",
            DateTimeNow=31241
        )

        self.ov2g.init_dinPaymentDetailsResType(dinPaymentDetailsResType=payment_details_res)


        print("[*] OK")

    # Validated
    def test_init_dinDSAKeyValueType(self):
        print("\n[+] Testing init_dinDSAKeyValueType")

        dsa_key_value = OpenV2GStructDeclarator.dinDSAKeyValueType(
            P=1,
            P_isUsed=1,
            Q=2,
            Q_isUsed=1,
            G=3,
            G_isUsed=1,
            Y=4,
            J=5,
            J_isUsed=1,
            Seed=6,
            Seed_isUsed=1,
            PgenCounter=7,
            PgenCounter_isUsed=1
        )

        print(f"[Python] {sizeof(dinDSAKeyValueType)=}")
        self.ov2g.init_dinDSAKeyValueType(dinDSAKeyValueType=dsa_key_value)

        assert dsa_key_value.P_isUsed == 0
        assert dsa_key_value.Q_isUsed == 0
        assert dsa_key_value.G_isUsed == 0
        assert dsa_key_value.J_isUsed == 0
        assert dsa_key_value.Seed_isUsed == 0
        assert dsa_key_value.PgenCounter_isUsed == 0

        print("[*] OK")

    # Validated
    def test_init_dinSASchedulesType(self):
        print("\n[+] Testing init_dinSASchedulesType")

        sa_schedules = OpenV2GStructDeclarator.dinSASchedulesType(noContent=1)

        self.ov2g.init_dinSASchedulesType(dinSASchedulesType=sa_schedules)

        print("[*] OK")

    # Validated
    def test_init_dinEVChargeParameterType(self):
        print("\n[+] Testing init_dinEVChargeParameterType")

        ev_charge_parameter = OpenV2GStructDeclarator.dinEVChargeParameterType(noContent=1)

        self.ov2g.init_dinEVChargeParameterType(dinEVChargeParameterType=ev_charge_parameter)

        print("[*] OK")

    # Validated
    def test_init_dinBodyBaseType(self):
        print("\n[+] Testing init_dinBodyBaseType")

        body_base = OpenV2GStructDeclarator.dinBodyBaseType(noContent=1)

        self.ov2g.init_dinBodyBaseType(dinBodyBaseType=body_base)

        print("[*] OK")

    # Validated
    def test_init_dinSubCertificatesType(self):
        print("\n[+] Testing init_dinSubCertificatesType")

        sub_certificates = OpenV2GStructDeclarator.dinSubCertificatesType(
            Certificate=[
                "Certificate 1",
                "Certificate 2",
                "Certificate 3",
            ]
        )

        self.ov2g.init_dinSubCertificatesType(dinSubCertificatesType=sub_certificates)

        assert sub_certificates.Certificate.arrayLen == 0


        print("[*] OK")

    # Validated    
    def test_init_dinCertificateChainType(self):
        print("\n[+] Testing init_dinCertificateChainType")

        certificate_chain_type = OpenV2GStructDeclarator.dinCertificateChainType(
            Certificate="MainCertificate",
            SubCertificates=OpenV2GStructDeclarator.dinSubCertificatesType(
                Certificate=[
                    "Certificate 1",
                    "Certificate 2",
                    "Certificate 3",
                ]
            ),
            SubCertificates_isUsed=1   
        )

        
        self.ov2g.init_dinCertificateChainType(dinCertificateChainType=certificate_chain_type)

        assert certificate_chain_type.SubCertificates_isUsed == 0

        print("[*] OK")
    
    # Validated
    def test_init_dinCertificateUpdateResType(self):
        print("\n[+] Testing init_dinCertificateUpdateResType")

        certificate_update_res = OpenV2GStructDeclarator.dinCertificateUpdateResType(
            Id="My ID",
            ResponseCode=2,
            ContractSignatureCertChain=OpenV2GStructDeclarator.dinCertificateChainType(
                Certificate="MainCertificate",
                SubCertificates=OpenV2GStructDeclarator.dinSubCertificatesType(
                    Certificate=[
                        "Certificate 1",
                        "Certificate 2",
                        "Certificate 3",
                    ]
                ),
                SubCertificates_isUsed=1   
            ),
            ContractSignatureEncryptedPrivateKey="SuperSecretPrivateKey",
            DHParams="DH Params",
            ContractID="Contract ID",
            RetryCounter=1
        )

        self.ov2g.init_dinCertificateUpdateResType(dinCertificateUpdateResType=certificate_update_res)


        print("[*] OK")
    
    # Validated
    def test_init_dinNotificationType(self):
        print("\n[+] Testing init_dinNotificationType")

        notification = OpenV2GStructDeclarator.dinNotificationType(
            FaultCode=2,
            FaultMsg="High temperature",
            FaultMsg_isUsed=1
        )

        # print(f"{sizeof(dinNotificationType)=}")
        self.ov2g.init_dinNotificationType(dinNotificationType=notification)


        assert notification.FaultMsg_isUsed == 0


        print("[*] OK")

    # Validated
    def test_init_dinSignatureMethodType(self):
        print("\n[+] Testing init_dinSignatureMethodType")

        signature_method = OpenV2GStructDeclarator.dinSignatureMethodType(
            Algorithm="SHA256",
            HMACOutputLength=10,
            HMACOutputLength_isUsed=1,
            ANY="ANY String",
            ANY_isUsed=1
        )

        # print(f"{sizeof(dinSignatureMethodType)=}")

        self.ov2g.init_dinSignatureMethodType(dinSignatureMethodType=signature_method)

        assert signature_method.HMACOutputLength_isUsed == 0
        assert signature_method.ANY_isUsed == 0

        print("[*] OK")

    # Validated
    def test_init_dinTransformsType(self):
        print("\n[+] Testing init_dinTransformsType")
        
        transforms = OpenV2GStructDeclarator.dinTransformsType(
            Transform=[
                OpenV2GStructDeclarator.dinTransformType(
                    Algorithm="SHA256",
                    ANY="ANY string",
                    ANY_isUsed=1,
                    XPath="/home/alex"
                )
            ]
        )

        # print(f"{sizeof(dinTransformsType)=}")

        self.ov2g.init_dinTransformsType(dinTransformsType=transforms)

        assert transforms.Transform.arrayLen == 0

        print("[*] OK")

    # Validated
    def test_init_dinDigestMethodType(self):
        print("\n[+] Testing init_dinDigestMethodType")

        digest_method = OpenV2GStructDeclarator.dinDigestMethodType(
            Algorithm="SHA256",
            ANY="ANY str",
            ANY_isUsed=1
        )

        # print(f"{sizeof(dinDigestMethodType)=}")

        self.ov2g.init_dinDigestMethodType(dinDigestMethodType=digest_method)

        assert digest_method.ANY_isUsed == 0

        print("[*] OK")

    # Validated
    def test_init_dinReferenceType(self):
        print("\n[+] Testing init_dinReferenceType")

        reference = OpenV2GStructDeclarator.dinReferenceType(
            Id="Reference ID",
            Id_isUsed=1,
            URI="file://home/alex",
            URI_isUsed=1,
            Type="Type",
            Type_isUsed=1,
            Transforms=OpenV2GStructDeclarator.dinTransformsType(
                Transform=[
                    OpenV2GStructDeclarator.dinTransformType(
                        Algorithm="SHA256",
                        ANY="ANY string",
                        ANY_isUsed=1,
                        XPath="/home/alex"
                    )
                ]
            ),
            Transforms_isUsed=1,
            DigestMethod=OpenV2GStructDeclarator.dinDigestMethodType(
                Algorithm="SHA256",
                ANY="ANY str",
                ANY_isUsed=1
            ),
            DigestValue="Digest value"
        )

        self.ov2g.init_dinReferenceType(dinReferenceType=reference)

        assert reference.Id_isUsed == 0
        assert reference.URI_isUsed == 0
        assert reference.Type_isUsed == 0
        assert reference.Transforms_isUsed == 0


        print("[*] OK")

    # Validated
    def test_init_dinSignedInfoType(self):
        print("\n[+] Testing init_dinSignedInfoType")

        signed_info = OpenV2GStructDeclarator.dinSignedInfoType(
            Id="SigInfoID",
            Id_isUsed=1,
            CanonicalizationMethod=OpenV2GStructDeclarator.dinCanonicalizationMethodType(
                Algorithm="ALGORITHM",
                ANY="Any str",
                ANY_isUsed=1
            ),
            SignatureMethod=OpenV2GStructDeclarator.dinSignatureMethodType(
                Algorithm="SHA256",
                HMACOutputLength=10,
                HMACOutputLength_isUsed=1,
                ANY="ANY String",
                ANY_isUsed=1
            ),
            Reference=[
                OpenV2GStructDeclarator.dinReferenceType(
                    Id="Reference ID",
                    Id_isUsed=1,
                    URI="file://home/alex",
                    URI_isUsed=1,
                    Type="Type",
                    Type_isUsed=1,
                    Transforms=OpenV2GStructDeclarator.dinTransformsType(
                        Transform=[
                            OpenV2GStructDeclarator.dinTransformType(
                                Algorithm="SHA256",
                                ANY="ANY string",
                                ANY_isUsed=1,
                                XPath="/home/alex"
                            )
                        ]
                    ),
                    Transforms_isUsed=1,
                    DigestMethod=OpenV2GStructDeclarator.dinDigestMethodType(
                        Algorithm="SHA256",
                        ANY="ANY str",
                        ANY_isUsed=1
                    ),
                    DigestValue="Digest value"
                )
            ]
        )

        # print(f"{sizeof(dinSignedInfoType)=}")
        self.ov2g.init_dinSignedInfoType(dinSignedInfoType=signed_info)

        assert signed_info.Id_isUsed == 0
        assert signed_info.Reference.arrayLen == 0

        print("[*] OK")

    # Validated
    def test_init_dinSignatureValueType(self):
        print("\n[+] Testing init_dinSignatureValueType")

        signature_value = OpenV2GStructDeclarator.dinSignatureValueType(
            Id="SignatureValue ID",
            Id_isUsed=1,
            CONTENT="CONTENT"
        )
        # print(f"[Python] {sizeof(dinSignatureValueType)=}")
        self.ov2g.init_dinSignatureValueType(dinSignatureValueType=signature_value)

        assert signature_value.Id_isUsed == 0

        print("[*] OK")


    # Validated
    def test_init_dinRSAKeyValueType(self):
        print("\n[+] Testing init_dinRSAKeyValueType")

        rsa_key_value = OpenV2GStructDeclarator.dinRSAKeyValueType(
            Modulus=10,
            Exponent=2
        )
        
        # print(f"[Python] {sizeof(dinRSAKeyValueType)=}")

        self.ov2g.init_dinRSAKeyValueType(dinRSAKeyValueType=rsa_key_value)

        print("[*] OK")


    # Validated
    def test_init_dinKeyValueType(self):
        print("\n[+] Testing init_dinKeyValueType")

        key_value = OpenV2GStructDeclarator.dinKeyValueType(
            DSAKeyValue=OpenV2GStructDeclarator.dinDSAKeyValueType(
                P=1,
                P_isUsed=1,
                Q=2,
                Q_isUsed=1,
                G=3,
                G_isUsed=1,
                Y=4,
                J=5,
                J_isUsed=1,
                Seed=6,
                Seed_isUsed=1,
                PgenCounter=7,
                PgenCounter_isUsed=1
            ),
            DSAKeyValue_isUsed=1,
            RSAKeyValue=OpenV2GStructDeclarator.dinRSAKeyValueType(
                Modulus=10,
                Exponent=2
            ),
            RSAKeyValue_isUsed=1,
            ANY="ANY STRING",
            ANY_isUsed=1
        )

        # print(f"[Python] {sizeof(dinKeyValueType)=}")

        self.ov2g.init_dinKeyValueType(dinKeyValueType=key_value)

        assert key_value.DSAKeyValue_isUsed == 0
        assert key_value.RSAKeyValue_isUsed == 0
        assert key_value.ANY_isUsed == 0

        print("[*] OK")

    # Validated
    def test_init_dinRetrievalMethodType(self):
        print("\n[+] Testing init_dinRetrievalMethodType")

        retrieval_method = OpenV2GStructDeclarator.dinRetrievalMethodType(
            URI="/home/alex",
            URI_isUsed=1,
            Type="the type",
            Type_isUsed=1,
            Transforms=OpenV2GStructDeclarator.dinTransformsType(
                Transform=[
                    OpenV2GStructDeclarator.dinTransformType(
                        Algorithm="SHA112",
                        ANY="ANy str",
                        ANY_isUsed=1,
                        XPath="/home/alex"
                    )
                ]
            ),
            Transforms_isUsed=1
        )

        print(f"[Python] {sizeof(dinRetrievalMethodType)=}")

        self.ov2g.init_dinRetrievalMethodType(dinRetrievalMethodType=retrieval_method)

        assert retrieval_method.URI_isUsed == 0
        assert retrieval_method.Type_isUsed == 0
        assert retrieval_method.Transforms_isUsed == 0


        print("[*] OK")

    # Validated
    def test_init_dinPGPDataType(self):
        print("\n[+] Testing init_dinPGPDataType")

        pgp_data = OpenV2GStructDeclarator.dinPGPDataType(
            PGPKeyID="PGPKEYID",
            PGPKeyID_isUsed=1,
            PGPKeyPacket="The packet",
            PGPKeyPacket_isUsed=1,
            ANY="ANY STR",
            ANY_isUsed=1
        )

        # print(f"[Python] {sizeof(dinPGPDataType)=}")
        self.ov2g.init_dinPGPDataType(dinPGPDataType=pgp_data)

        assert pgp_data.PGPKeyID_isUsed == 0
        assert pgp_data.PGPKeyPacket_isUsed == 0
        assert pgp_data.ANY_isUsed == 0

        print("[*] OK")


    # Validated
    def test_init_dinKeyInfoType(self):
        print("\n[+] Testing init_dinKeyInfoType")

        key_info = OpenV2GStructDeclarator.dinKeyInfoType(
            Id="ID",
            Id_isUsed=1,
            KeyName=["Key"],
            KeyValue=[
                OpenV2GStructDeclarator.dinKeyValueType(
                    DSAKeyValue=OpenV2GStructDeclarator.dinDSAKeyValueType(
                        P=1,
                        P_isUsed=1,
                        Q=2,
                        Q_isUsed=1,
                        G=3,
                        G_isUsed=1,
                        Y=4,
                        J=5,
                        J_isUsed=1,
                        Seed=6,
                        Seed_isUsed=1,
                        PgenCounter=7,
                        PgenCounter_isUsed=1
                    ),
                    DSAKeyValue_isUsed=1,
                    RSAKeyValue=OpenV2GStructDeclarator.dinRSAKeyValueType(
                        Modulus=10,
                        Exponent=2
                    ),
                    RSAKeyValue_isUsed=1,
                    ANY="ANY STRING",
                    ANY_isUsed=1
                )   
            ],
            RetrievalMethod=[
                OpenV2GStructDeclarator.dinRetrievalMethodType(
                    URI="/home/alex",
                    URI_isUsed=1,
                    Type="the type",
                    Type_isUsed=1,
                    Transforms=OpenV2GStructDeclarator.dinTransformsType(
                        Transform=[
                            OpenV2GStructDeclarator.dinTransformType(
                                Algorithm="SHA112",
                                ANY="ANy str",
                                ANY_isUsed=1,
                                XPath="/home/alex"
                            )
                        ]
                    ),
                    Transforms_isUsed=1
                )
            ],
            X509Data=[
                OpenV2GStructDeclarator.dinX509DataType(
                    X509IssuerSerial=[
                        OpenV2GStructDeclarator.dinX509IssuerSerialType(
                            X509IssuerName="The issuer name",
                            X509SerialNumber=28731,
                        )
                    ],
                    X509SKI=37182,
                    X509SubjectName="Subject Name",
                    X509Certificate=39123819,
                    X509CRL=231939,
                    ANY="Anything",
                    ANY_isUsed=1
                )
            ],
            PGPData=[
                OpenV2GStructDeclarator.dinPGPDataType(
                    PGPKeyID="PGPKEYID",
                    PGPKeyID_isUsed=1,
                    PGPKeyPacket="The packet",
                    PGPKeyPacket_isUsed=1,
                    ANY="ANY STR",
                    ANY_isUsed=1
                )
            ],
            SPKIData=[
                OpenV2GStructDeclarator.dinSPKIDataType(
                    SPKISexp=64, 
                    ANY="Any String", 
                    ANY_isUsed=1
                )
            ],
            MgmtData=[
                "MgmtData"
            ],
            ANY="ANY str",
            ANY_isUsed=1
        )

        print(f"[Python] {sizeof(dinKeyInfoType)=}")
        self.ov2g.init_dinKeyInfoType(dinKeyInfoType=key_info)

        assert key_info.Id_isUsed == 0
        assert key_info.KeyName.arrayLen == 0
        assert key_info.KeyValue.arrayLen == 0
        assert key_info.RetrievalMethod.arrayLen == 0
        assert key_info.X509Data.arrayLen == 0
        assert key_info.PGPData.arrayLen == 0
        assert key_info.SPKIData.arrayLen == 0
        assert key_info.MgmtData.arrayLen == 0
        assert key_info.ANY_isUsed == 0
        
        print("[*] OK")

    # Validated
    def test_init_dinObjectType(self):
        print("\n[+] Testing init_dinObjectType")

        object = OpenV2GStructDeclarator.dinObjectType(
            Id="Object ID",
            Id_isUsed=1,
            MimeType="MimeType",
            MimeType_isUsed=1,
            Encoding="Enconding",
            Encoding_isUsed=1,
            ANY="ANY str",
            ANY_isUsed=1
        )

        print(f"[Python] {sizeof(dinObjectType)=}")
        self.ov2g.init_dinObjectType(dinObjectType=object)

        assert object.Id_isUsed == 0
        assert object.MimeType_isUsed == 0
        assert object.Encoding_isUsed == 0
        assert object.ANY_isUsed == 0

        print("[*] OK")

    # Validated
    def test_init_dinSignatureType(self):
        print("\n[+] Testing init_dinSignatureType")

        signature = OpenV2GStructDeclarator.dinSignatureType(
            Id="ID",
            Id_isUsed=1,
            SignedInfo=OpenV2GStructDeclarator.dinSignedInfoType(
                Id="SigInfoID",
                Id_isUsed=1,
                CanonicalizationMethod=OpenV2GStructDeclarator.dinCanonicalizationMethodType(
                    Algorithm="ALGORITHM",
                    ANY="Any str",
                    ANY_isUsed=1
                ),
                SignatureMethod=OpenV2GStructDeclarator.dinSignatureMethodType(
                    Algorithm="SHA256",
                    HMACOutputLength=10,
                    HMACOutputLength_isUsed=1,
                    ANY="ANY String",
                    ANY_isUsed=1
                ),
                Reference=[
                    OpenV2GStructDeclarator.dinReferenceType(
                        Id="Reference ID",
                        Id_isUsed=1,
                        URI="file://home/alex",
                        URI_isUsed=1,
                        Type="Type",
                        Type_isUsed=1,
                        Transforms=OpenV2GStructDeclarator.dinTransformsType(
                            Transform=[
                                OpenV2GStructDeclarator.dinTransformType(
                                    Algorithm="SHA256",
                                    ANY="ANY string",
                                    ANY_isUsed=1,
                                    XPath="/home/alex"
                                )
                            ]
                        ),
                        Transforms_isUsed=1,
                        DigestMethod=OpenV2GStructDeclarator.dinDigestMethodType(
                            Algorithm="SHA256",
                            ANY="ANY str",
                            ANY_isUsed=1
                        ),
                        DigestValue="Digest value"
                    )
                ]
            ),
            SignatureValue=OpenV2GStructDeclarator.dinSignatureValueType(
                Id="SignatureValue ID",
                Id_isUsed=1,
                CONTENT="CONTENT"
            ),
            KeyInfo=OpenV2GStructDeclarator.dinKeyInfoType(
                Id="ID",
                Id_isUsed=1,
                KeyName=["Key"],
                KeyValue=[
                    OpenV2GStructDeclarator.dinKeyValueType(
                        DSAKeyValue=OpenV2GStructDeclarator.dinDSAKeyValueType(
                            P=1,
                            P_isUsed=1,
                            Q=2,
                            Q_isUsed=1,
                            G=3,
                            G_isUsed=1,
                            Y=4,
                            J=5,
                            J_isUsed=1,
                            Seed=6,
                            Seed_isUsed=1,
                            PgenCounter=7,
                            PgenCounter_isUsed=1
                        ),
                        DSAKeyValue_isUsed=1,
                        RSAKeyValue=OpenV2GStructDeclarator.dinRSAKeyValueType(
                            Modulus=10,
                            Exponent=2
                        ),
                        RSAKeyValue_isUsed=1,
                        ANY="ANY STRING",
                        ANY_isUsed=1
                    )   
                ],
                RetrievalMethod=[
                    OpenV2GStructDeclarator.dinRetrievalMethodType(
                        URI="/home/alex",
                        URI_isUsed=1,
                        Type="the type",
                        Type_isUsed=1,
                        Transforms=OpenV2GStructDeclarator.dinTransformsType(
                            Transform=[
                                OpenV2GStructDeclarator.dinTransformType(
                                    Algorithm="SHA112",
                                    ANY="ANy str",
                                    ANY_isUsed=1,
                                    XPath="/home/alex"
                                )
                            ]
                        ),
                        Transforms_isUsed=1
                    )
                ],
                X509Data=[
                    OpenV2GStructDeclarator.dinX509DataType(
                        X509IssuerSerial=[
                            OpenV2GStructDeclarator.dinX509IssuerSerialType(
                                X509IssuerName="The issuer name",
                                X509SerialNumber=28731,
                            )
                        ],
                        X509SKI=37182,
                        X509SubjectName="Subject Name",
                        X509Certificate=39123819,
                        X509CRL=231939,
                        ANY="Anything",
                        ANY_isUsed=1
                    )
                ],
                PGPData=[
                    OpenV2GStructDeclarator.dinPGPDataType(
                        PGPKeyID="PGPKEYID",
                        PGPKeyID_isUsed=1,
                        PGPKeyPacket="The packet",
                        PGPKeyPacket_isUsed=1,
                        ANY="ANY STR",
                        ANY_isUsed=1
                    )
                ],
                SPKIData=[
                    OpenV2GStructDeclarator.dinSPKIDataType(
                        SPKISexp=64, 
                        ANY="Any String", 
                        ANY_isUsed=1
                    )
                ],
                MgmtData=[
                    "MgmtData"
                ],
                ANY="ANY str",
                ANY_isUsed=1
            ),
            KeyInfo_isUsed=1,
            Object=[
                OpenV2GStructDeclarator.dinObjectType(
                    Id="Object ID",
                    Id_isUsed=1,
                    MimeType="MimeType",
                    MimeType_isUsed=1,
                    Encoding="Enconding",
                    Encoding_isUsed=1,
                    ANY="ANY str",
                    ANY_isUsed=1
                )
            ]
        )

        print(f"[Python] {sizeof(dinSignatureType)=}")
        self.ov2g.init_dinSignatureType(dinSignatureType=signature)

        assert signature.Id_isUsed == 0
        assert signature.KeyInfo_isUsed == 0
        assert signature.Object.arrayLen == 0

        print("[*] OK")


    # Validated
    def test_init_dinMessageHeaderType(self):
        print("\n[+] Testing init_dinMessageHeaderType")

        message_header = OpenV2GStructDeclarator.dinMessageHeaderType(
            SessionID=10,
            Notification=OpenV2GStructDeclarator.dinNotificationType(
                FaultCode=2,
                FaultMsg="High temperature",
                FaultMsg_isUsed=1
            ),
            Signature=OpenV2GStructDeclarator.dinSignatureType(
                Id="ID",
                Id_isUsed=1,
                SignedInfo=OpenV2GStructDeclarator.dinSignedInfoType(
                    Id="SigInfoID",
                    Id_isUsed=1,
                    CanonicalizationMethod=OpenV2GStructDeclarator.dinCanonicalizationMethodType(
                        Algorithm="ALGORITHM",
                        ANY="Any str",
                        ANY_isUsed=1
                    ),
                    SignatureMethod=OpenV2GStructDeclarator.dinSignatureMethodType(
                        Algorithm="SHA256",
                        HMACOutputLength=10,
                        HMACOutputLength_isUsed=1,
                        ANY="ANY String",
                        ANY_isUsed=1
                    ),
                    Reference=[
                        OpenV2GStructDeclarator.dinReferenceType(
                            Id="Reference ID",
                            Id_isUsed=1,
                            URI="file://home/alex",
                            URI_isUsed=1,
                            Type="Type",
                            Type_isUsed=1,
                            Transforms=OpenV2GStructDeclarator.dinTransformsType(
                                Transform=[
                                    OpenV2GStructDeclarator.dinTransformType(
                                        Algorithm="SHA256",
                                        ANY="ANY string",
                                        ANY_isUsed=1,
                                        XPath="/home/alex"
                                    )
                                ]
                            ),
                            Transforms_isUsed=1,
                            DigestMethod=OpenV2GStructDeclarator.dinDigestMethodType(
                                Algorithm="SHA256",
                                ANY="ANY str",
                                ANY_isUsed=1
                            ),
                            DigestValue="Digest value"
                        )
                    ]
                ),
                SignatureValue=OpenV2GStructDeclarator.dinSignatureValueType(
                    Id="SignatureValue ID",
                    Id_isUsed=1,
                    CONTENT="CONTENT"
                ),
                KeyInfo=OpenV2GStructDeclarator.dinKeyInfoType(
                    Id="ID",
                    Id_isUsed=1,
                    KeyName=["Key"],
                    KeyValue=[
                        OpenV2GStructDeclarator.dinKeyValueType(
                            DSAKeyValue=OpenV2GStructDeclarator.dinDSAKeyValueType(
                                P=1,
                                P_isUsed=1,
                                Q=2,
                                Q_isUsed=1,
                                G=3,
                                G_isUsed=1,
                                Y=4,
                                J=5,
                                J_isUsed=1,
                                Seed=6,
                                Seed_isUsed=1,
                                PgenCounter=7,
                                PgenCounter_isUsed=1
                            ),
                            DSAKeyValue_isUsed=1,
                            RSAKeyValue=OpenV2GStructDeclarator.dinRSAKeyValueType(
                                Modulus=10,
                                Exponent=2
                            ),
                            RSAKeyValue_isUsed=1,
                            ANY="ANY STRING",
                            ANY_isUsed=1
                        )   
                    ],
                    RetrievalMethod=[
                        OpenV2GStructDeclarator.dinRetrievalMethodType(
                            URI="/home/alex",
                            URI_isUsed=1,
                            Type="the type",
                            Type_isUsed=1,
                            Transforms=OpenV2GStructDeclarator.dinTransformsType(
                                Transform=[
                                    OpenV2GStructDeclarator.dinTransformType(
                                        Algorithm="SHA112",
                                        ANY="ANy str",
                                        ANY_isUsed=1,
                                        XPath="/home/alex"
                                    )
                                ]
                            ),
                            Transforms_isUsed=1
                        )
                    ],
                    X509Data=[
                        OpenV2GStructDeclarator.dinX509DataType(
                            X509IssuerSerial=[
                                OpenV2GStructDeclarator.dinX509IssuerSerialType(
                                    X509IssuerName="The issuer name",
                                    X509SerialNumber=28731,
                                )
                            ],
                            X509SKI=37182,
                            X509SubjectName="Subject Name",
                            X509Certificate=39123819,
                            X509CRL=231939,
                            ANY="Anything",
                            ANY_isUsed=1
                        )
                    ],
                    PGPData=[
                        OpenV2GStructDeclarator.dinPGPDataType(
                            PGPKeyID="PGPKEYID",
                            PGPKeyID_isUsed=1,
                            PGPKeyPacket="The packet",
                            PGPKeyPacket_isUsed=1,
                            ANY="ANY STR",
                            ANY_isUsed=1
                        )
                    ],
                    SPKIData=[
                        OpenV2GStructDeclarator.dinSPKIDataType(
                            SPKISexp=64, 
                            ANY="Any String", 
                            ANY_isUsed=1
                        )
                    ],
                    MgmtData=[
                        "MgmtData"
                    ],
                    ANY="ANY str",
                    ANY_isUsed=1
                ),
                KeyInfo_isUsed=1,
                Object=[
                    OpenV2GStructDeclarator.dinObjectType(
                        Id="Object ID",
                        Id_isUsed=1,
                        MimeType="MimeType",
                        MimeType_isUsed=1,
                        Encoding="Enconding",
                        Encoding_isUsed=1,
                        ANY="ANY str",
                        ANY_isUsed=1
                    )
                ]
            ),
            Notification_isUsed=1,
            Signature_isUsed=1
        )

        # print(f"[Python] {sizeof(dinMessageHeaderType)=}")
        self.ov2g.init_dinMessageHeaderType(dinMessageHeaderType=message_header)

        assert message_header.Notification_isUsed == 0
        assert message_header.Signature_isUsed == 0


        print("[*] OK")

    
    def test_init_dinAC_EVSEChargeParameterType(self):
        print("\n[+] Testing init_dinAC_EVSEChargeParameterType")

        ac_evse_charge_parameter = OpenV2GStructDeclarator.dinAC_EVSEChargeParameterType(
            AC_EVSEStatus=OpenV2GStructDeclarator.dinAC_EVSEStatusType(
                PowerSwitchClosed=1,
                RCD=10,
                NotificationMaxDelay=20,
                EVSENotification=1
            ),
            EVSEMaxVoltage=OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=1, Unit_isUsed=1, Value=10),
            EVSEMaxCurrent=OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=1, Unit_isUsed=1, Value=10),
            EVSEMinCurrent=OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=1, Unit_isUsed=1, Value=10),
        )

        print(f"[Python] {sizeof(dinAC_EVSEChargeParameterType)=}")

        self.ov2g.init_dinAC_EVSEChargeParameterType(dinAC_EVSEChargeParameterType=ac_evse_charge_parameter)


        print("[*] OK")

    # Validated
    def test_init_dinChargeParameterDiscoveryResType(self):
        print("\n[+] Testing init_dinChargeParameterDiscoveryResType")

        charge_parameter_discovery_res = OpenV2GStructDeclarator.dinChargeParameterDiscoveryResType(
            ResponseCode=2,
            EVSEProcessingType=1,
            SASchedules=OpenV2GStructDeclarator.dinSASchedulesType(noContent=1),
            SASchedules_isUsed=1,
            SAScheduleList=OpenV2GStructDeclarator.dinSAScheduleListType(
                SAScheduleTuple=[
                    OpenV2GStructDeclarator.dinSAScheduleTupleType(
                        SAScheduleTupleID=1,
                        PMaxSchedule=OpenV2GStructDeclarator.dinPMaxScheduleType(
                            PMaxScheduleID=2,
                            PMaxScheduleEntry=[
                                OpenV2GStructDeclarator.dinPMaxScheduleEntryType(
                                    TimeInterval=OpenV2GStructDeclarator.dinIntervalType(noContent=1),
                                    TimeInterval_isUsed=1,
                                    RelativeTimeInterval=OpenV2GStructDeclarator.dinRelativeTimeIntervalType(
                                        start=2,
                                        duration=10,
                                        duration_isUsed=1
                                    ),
                                    RelativeTimeInterval_isUsed=1,
                                    PMax=20
                                ),
                                OpenV2GStructDeclarator.dinPMaxScheduleEntryType(
                                    TimeInterval=OpenV2GStructDeclarator.dinIntervalType(noContent=1),
                                    TimeInterval_isUsed=1,
                                    RelativeTimeInterval=OpenV2GStructDeclarator.dinRelativeTimeIntervalType(
                                        start=2,
                                        duration=10,
                                        duration_isUsed=1
                                    ),
                                    RelativeTimeInterval_isUsed=1,
                                    PMax=30
                                )

                            ]
                        ),
                        SalesTariff=OpenV2GStructDeclarator.dinSalesTariffType(
                            Id="ID1",
                            SalesTariffID=2,
                            SalesTariffDescription="The sales",
                            SalesTariffDescription_isUsed=1,
                            NumEPriceLevels=10,
                            SalesTariffEntry=[
                                OpenV2GStructDeclarator.dinSalesTariffEntryType(
                                    TimeInterval=OpenV2GStructDeclarator.dinIntervalType(noContent=1),
                                    TimeInteraval_isUsed=1,
                                    RelativeTimeInterval=OpenV2GStructDeclarator.dinRelativeTimeIntervalType(
                                        start=0,
                                        duration=10,
                                        duration_isUsed=1
                                    ),
                                    RelativeTimeInteraval_isUsed=1,
                                    EPriceLevel=2,
                                    ConsumptionCost=[
                                        OpenV2GStructDeclarator.dinConsumptionCostType(
                                            startValue=10,
                                            Cost=[
                                                OpenV2GStructDeclarator.dinCostType(
                                                    costKind=2,
                                                    amount=32,
                                                    amountMultiplier=1,
                                                    amountMultiplier_isUsed=1
                                                ),

                                                OpenV2GStructDeclarator.dinCostType(
                                                    costKind=2,
                                                    amount=48,
                                                    amountMultiplier=1,
                                                    amountMultiplier_isUsed=1
                                                )
                                            ]
                                        )
                                    ],
                                )
                            ]
                        ),
                        SalesTariff_isUsed=1
                    )
                ]
            ),
            SAScheduleList_isUsed=1,
            EVSEChargeParameter=OpenV2GStructDeclarator.dinEVSEChargeParameterType(noContent=1),
            EVSEChargeParameter_isUsed=1,
            AC_EVSEChargeParameter=OpenV2GStructDeclarator.dinAC_EVSEChargeParameterType(
                AC_EVSEStatus=OpenV2GStructDeclarator.dinAC_EVSEStatusType(
                    PowerSwitchClosed=1,
                    RCD=10,
                    NotificationMaxDelay=20,
                    EVSENotification=1
                ),
                EVSEMaxVoltage=OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=1, Unit_isUsed=1, Value=10),
                EVSEMaxCurrent=OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=1, Unit_isUsed=1, Value=10),
                EVSEMinCurrent=OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=1, Unit_isUsed=1, Value=10),
            ),
            AC_EVSEChargeParameter_isUsed=1,
            DC_EVSEChargeParameter=OpenV2GStructDeclarator.dinDC_EVSEChargeParameterType(
                DC_EVSEStatus= OpenV2GStructDeclarator.dinDC_EVSEStatusType(EVSEIsolationStatus=1, EVSEIsolationStatus_isUsed=1, EVSEStatusCode=2, NotificationMaxDelay=3, EVSENotification=4),
                EVSEMaximumCurrentLimit= OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=2, Unit_isUsed=1, Value=10),
                EVSEMaximumPowerLimit= OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=2, Unit_isUsed=1, Value=10),
                EVSEMaximumPowerLimit_isUsed=1,
                EVSEMaximumVoltageLimit= OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=2, Unit_isUsed=1, Value=10),
                EVSEMinimumCurrentLimit= OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=2, Unit_isUsed=1, Value=10),
                EVSEMinimumVoltageLimit= OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=2, Unit_isUsed=1, Value=10),
                EVSECurrentRegulationTolerance= OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=2, Unit_isUsed=1, Value=10),
                EVSECurrentRegulationTolerance_isUsed=1,
                EVSEPeakCurrentRipple= OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=2, Unit_isUsed=1, Value=10),
                EVSEEnergyToBeDelivered= OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=2, Unit_isUsed=1, Value=54),
                EVSEEnergyToBeDelivered_isUsed=1
            ),
            DC_EVSEChargeParameter_isUsed=1
        )

        # print(f"[Python] {sizeof(dinChargeParameterDiscoveryResType)=}")

        self.ov2g.init_dinChargeParameterDiscoveryResType(dinChargeParameterDiscoveryResType=charge_parameter_discovery_res)

        assert charge_parameter_discovery_res.SASchedules_isUsed == 0
        assert charge_parameter_discovery_res.SAScheduleList_isUsed == 0
        assert charge_parameter_discovery_res.EVSEChargeParameter_isUsed == 0
        assert charge_parameter_discovery_res.AC_EVSEChargeParameter_isUsed == 0
        assert charge_parameter_discovery_res.DC_EVSEChargeParameter_isUsed == 0

        print("[*] OK")

    
    # Validated
    def test_init_dinProfileEntryType(self):
        print("\n[+] Testing init_dinProfileEntryType")

        profile_entry = OpenV2GStructDeclarator.dinProfileEntryType(
            ChargingProfileEntryStart=200,
            ChargingProfileEntryMaxPower=100,
        )
        
        # print(f"[Python] {sizeof(dinProfileEntryType)=}")

        self.ov2g.init_dinProfileEntryType(dinProfileEntryType=profile_entry)
        
        print("[*] OK")

    # Validated
    def test_init_dinChargingProfileType(self):
        print("\n[+] Testing init_dinChargingProfileType")

        charging_profile = OpenV2GStructDeclarator.dinChargingProfileType(
            SAScheduleTupleID=1,
            ProfileEntry=[
                OpenV2GStructDeclarator.dinProfileEntryType(
                    ChargingProfileEntryStart=0,
                    ChargingProfileEntryMaxPower=100,
                ),
                OpenV2GStructDeclarator.dinProfileEntryType(
                    ChargingProfileEntryStart=100,
                    ChargingProfileEntryMaxPower=300,
                )
            ]
        )
        
        # print(f"[Python] {sizeof(dinChargingProfileType)=}")

        self.ov2g.init_dinChargingProfileType(dinChargingProfileType=charging_profile)

        assert charging_profile.ProfileEntry.arrayLen == 0

        print("[*] OK")


    # Validated
    def test_init_dinEVPowerDeliveryParameterType(self):
        print("\n[+] Testing init_dinEVPowerDeliveryParameterType")

        ev_power_delivery_parameter = OpenV2GStructDeclarator.dinEVPowerDeliveryParameterType(noContent=1)

        self.ov2g.init_dinEVPowerDeliveryParameterType(dinEVPowerDeliveryParameterType=ev_power_delivery_parameter)
        
        print("[*] OK")


    # Validated
    def test_init_dinPowerDeliveryReqType(self):
        print("\n[+] Testing init_dinPowerDeliveryReqType")

        power_delivery_req = OpenV2GStructDeclarator.dinPowerDeliveryReqType(
            ReadyToChargeState=1,
            ChargingProfile=OpenV2GStructDeclarator.dinChargingProfileType(
                SAScheduleTupleID=1,
                ProfileEntry=[
                    OpenV2GStructDeclarator.dinProfileEntryType(
                        ChargingProfileEntryStart=0,
                        ChargingProfileEntryMaxPower=100,
                    ),
                    OpenV2GStructDeclarator.dinProfileEntryType(
                        ChargingProfileEntryStart=100,
                        ChargingProfileEntryMaxPower=300,
                    )
                ]
            ),
            ChargingProfile_isUsed=1,
            EVPowerDeliveryParameter=OpenV2GStructDeclarator.dinEVPowerDeliveryParameterType(noContent=1),
            EVPowerDeliveryParameter_isUsed=1,
            DC_EVPowerDeliveryParameter=OpenV2GStructDeclarator.dinDC_EVPowerDeliveryParameterType(
                DC_EVStatus=OpenV2GStructDeclarator.dinDC_EVStatusType(
                    EVReady=1,
                    EVCabinConditioning=2,
                    EVCabinConditioning_isUsed=1,
                    EVRESSConditioning=3,
                    EVRESSConditioning_isUsed=1,
                    EVErrorCode=4,
                    EVRESSSOC=50
                ),
                BulkChargingComplete=1,
                BulkChargingComplete_isUsed=1,
                ChargingComplete=1
            ),
            DC_EVPowerDeliveryParameter_isUsed=1
        )

        # print(f"[Python] {sizeof(dinPowerDeliveryReqType)=}")

        self.ov2g.init_dinPowerDeliveryReqType(dinPowerDeliveryReqType=power_delivery_req)

        assert power_delivery_req.ChargingProfile_isUsed == 0
        assert power_delivery_req.EVPowerDeliveryParameter_isUsed == 0
        assert power_delivery_req.DC_EVPowerDeliveryParameter_isUsed == 0

        print("[*] OK")

    # Validated
    def test_init_dinEntryType(self):
        print("\n[+] Testing init_dinEntryType")

        entry = OpenV2GStructDeclarator.dinEntryType(
            TimeInterval=OpenV2GStructDeclarator.dinIntervalType(noContent=1),
            RelativeTimeInterval=OpenV2GStructDeclarator.dinRelativeTimeIntervalType(
                start=0,
                duration=10,
                duration_isUsed=1
            ),
            TimeInterval_isUsed=1,
            RelativeTimeInterval_isUsed=1
        )

        # print(f"[Python] {sizeof(dinEntryType)=}")

        self.ov2g.init_dinEntryType(dinEntryType=entry)

        assert entry.TimeInterval_isUsed == 0
        assert entry.RelativeTimeInterval_isUsed == 0

        print("[*] OK")
    
    # Validated
    def test_init_dinSessionStopType(self):
        print("\n[+] Testing init_dinSessionStopType")
        
        session_stop = OpenV2GStructDeclarator.dinSessionStopType(noContent=1)

        self.ov2g.init_dinSessionStopType(dinSessionStopType=session_stop)

        print("[*] OK")

    # Validated
    def test_init_dinServiceDetailReqType(self):
        print("\n[+] Testing init_dinServiceDetailReqType")
        
        service_detail_req = OpenV2GStructDeclarator.dinServiceDetailReqType(ServiceID=10)

        self.ov2g.init_dinServiceDetailReqType(dinServiceDetailReqType=service_detail_req)

        print("[*] OK")


    # Validated
    def test_init_dinChargingStatusReqType(self):
        print("\n[+] Testing init_dinChargingStatusReqType")

        charging_status_req = OpenV2GStructDeclarator.dinChargingStatusReqType(noContent=1)

        self.ov2g.init_dinChargingStatusReqType(dinChargingStatusReqType=charging_status_req)

        print("[*] OK")

    # Validated
    def test_init_dinCertificateInstallationReqType(self):
        print("\n[+] Testing init_dinCertificateInstallationReqType")

        certificate_installation_req = OpenV2GStructDeclarator.dinCertificateInstallationReqType(
            Id="CertificateID",
            Id_isUsed=1,
            OEMProvisioningCert="oemp prov certi",
            ListOfRootCertificateIDs=OpenV2GStructDeclarator.dinListOfRootCertificateIDsType(
                RootCertificateID=[
                    "ID1", "ID2", "ID3"
                ]
            ),
            DHParams="dh params"
        )

        print(f"[Python] {sizeof(dinCertificateInstallationReqType)=}")
        self.ov2g.init_dinCertificateInstallationReqType(dinCertificateInstallationReqType=certificate_installation_req)
        
        assert certificate_installation_req.Id_isUsed == 0

        print("[*] OK")


    # Validated
    def test_init_dinPaymentOptionsType(self):
        print("\n[+] Testing init_dinPaymentOptionsType")
        
        payment_options = OpenV2GStructDeclarator.dinPaymentOptionsType(
            PaymentOption=[1,2,3]
        )

        self.ov2g.init_dinPaymentOptionsType(dinPaymentOptionsType=payment_options)

        assert payment_options.PaymentOption.arrayLen == 0
        
        print("[*] OK")

    # Validated
    def test_init_dinServiceTagType(self):
        print("\n[+] Testing init_dinServiceTagType")

        service_tag = OpenV2GStructDeclarator.dinServiceTagType(
            ServiceID=2,
            ServiceName="Service NAME",
            ServiceName_isUsed=1,
            ServiceCategory=3,
            ServiceScope="Charge",
            ServiceScope_isUsed=1
        )

        # print(f"[Python] {sizeof(dinServiceTagType)=}")

        self.ov2g.init_dinServiceTagType(dinServiceTagType=service_tag)

        assert service_tag.ServiceName_isUsed == 0
        assert service_tag.ServiceScope_isUsed == 0

        print("[*] OK")

    # Validated
    def test_init_dinServiceChargeType(self):
        print("\n[+] Testing init_dinServiceChargeType")

        service_charge = OpenV2GStructDeclarator.dinServiceChargeType(
            ServiceTag=OpenV2GStructDeclarator.dinServiceTagType(
                ServiceID=2,
                ServiceName="Service NAME",
                ServiceName_isUsed=1,
                ServiceCategory=3,
                ServiceScope="Charge",
                ServiceScope_isUsed=1
            ),
            FreeService=1,
            EnergyTransferType=1
        )

        # print(f"[Python] {sizeof(dinServiceChargeType)=}")

        self.ov2g.init_dinServiceChargeType(dinServiceChargeType=service_charge)

        print("[*] OK")

    # Validated
    def test_init_dinServiceType(self):
        print("\n[+] Testing init_dinServiceType")

        service = OpenV2GStructDeclarator.dinServiceType(
            ServiceTag=OpenV2GStructDeclarator.dinServiceTagType(
                ServiceID=2,
                ServiceName="Service NAME",
                ServiceName_isUsed=1,
                ServiceCategory=3,
                ServiceScope="Charge",
                ServiceScope_isUsed=1
            ),
            FreeService=1
        )

        # print(f"[Python] {sizeof(dinServiceType)=}")

        self.ov2g.init_dinServiceType(dinServiceType=service)


        print("[*] OK")

    # Validated
    def test_init_dinServiceTagListType(self):
        print("\n[+] Testing init_dinServiceTagListType")

        service_tag_list = OpenV2GStructDeclarator.dinServiceTagListType(
            Service=[
                OpenV2GStructDeclarator.dinServiceType(
                    ServiceTag=OpenV2GStructDeclarator.dinServiceTagType(
                        ServiceID=1,
                        ServiceName="Service NAME1",
                        ServiceName_isUsed=1,
                        ServiceCategory=2,
                        ServiceScope="Charge",
                        ServiceScope_isUsed=1
                    ),
                    FreeService=1
                ),

                OpenV2GStructDeclarator.dinServiceType(
                    ServiceTag=OpenV2GStructDeclarator.dinServiceTagType(
                        ServiceID=2,
                        ServiceName="Service NAME",
                        ServiceName_isUsed=1,
                        ServiceCategory=3,
                        ServiceScope="Charge",
                        ServiceScope_isUsed=1
                    ),
                    FreeService=1
                )

            ]
        )

        print(f"[Python] {sizeof(dinServiceTagListType)=}")

        self.ov2g.init_dinServiceTagListType(dinServiceTagListType=service_tag_list)

        assert service_tag_list.Service.arrayLen == 0


        print("[*] OK")

    # Validated
    def test_init_dinServiceDiscoveryResType(self):
        print("\n[+] Testing init_dinServiceDiscoveryResType")

        service_discovery_res = OpenV2GStructDeclarator.dinServiceDiscoveryResType(
            ResponseCode=1,
            PaymentOptions=OpenV2GStructDeclarator.dinPaymentOptionsType(
                PaymentOption=[1,2,3]
            ),
            ChargeService=OpenV2GStructDeclarator.dinServiceChargeType(
                ServiceTag=OpenV2GStructDeclarator.dinServiceTagType(
                    ServiceID=2,
                    ServiceName="Service NAME",
                    ServiceName_isUsed=1,
                    ServiceCategory=3,
                    ServiceScope="Charge",
                    ServiceScope_isUsed=1
                ),
                FreeService=1,
                EnergyTransferType=1
            ),
            ServiceList=OpenV2GStructDeclarator.dinServiceTagListType(
                Service=[
                    OpenV2GStructDeclarator.dinServiceType(
                        ServiceTag=OpenV2GStructDeclarator.dinServiceTagType(
                            ServiceID=1,
                            ServiceName="Service NAME1",
                            ServiceName_isUsed=1,
                            ServiceCategory=2,
                            ServiceScope="Charge",
                            ServiceScope_isUsed=1
                        ),
                        FreeService=1
                    ),

                    OpenV2GStructDeclarator.dinServiceType(
                        ServiceTag=OpenV2GStructDeclarator.dinServiceTagType(
                            ServiceID=2,
                            ServiceName="Service NAME",
                            ServiceName_isUsed=1,
                            ServiceCategory=3,
                            ServiceScope="Charge",
                            ServiceScope_isUsed=1
                        ),
                        FreeService=1
                    )

                ]
            ),
            ServiceList_isUsed=1
        )

        print(f"[Python] {sizeof(dinServiceDiscoveryResType)=}")
        self.ov2g.init_dinServiceDiscoveryResType(dinServiceDiscoveryResType=service_discovery_res)

        assert service_discovery_res.ServiceList_isUsed == 0

        print("[*] OK")

    # Validated
    def test_init_dinCurrentDemandReqType(self):
        print("\n[+] Testing init_dinCurrentDemandReqType")

        current_demand_req = OpenV2GStructDeclarator.dinCurrentDemandReqType(
            DC_EVStatus=OpenV2GStructDeclarator.dinDC_EVStatusType(
                EVReady=1,
                EVCabinConditioning=2,
                EVCabinConditioning_isUsed=1,
                EVRESSConditioning=3,
                EVRESSConditioning_isUsed=1,
                EVErrorCode=4,
                EVRESSSOC=50
            ),
            EVTargetCurrent=OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=2, Unit=dinunitSymbolType_Ah, Unit_isUsed=1, Value=12),
            EVMaximumVoltageLimit=OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=2, Unit=dinunitSymbolType_Ah, Unit_isUsed=1, Value=12),
            EVMaximumVoltageLimit_isUsed=1,
            EVMaximumCurrentLimit= OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=2, Unit=dinunitSymbolType_Ah, Unit_isUsed=1, Value=12),
            EVMaximumCurrentLimit_isUsed=1,
            EVMaximumPowerimit= OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=2, Unit=dinunitSymbolType_Ah, Unit_isUsed=1, Value=12),
            EVMaximumPowerLimit_isUsed=1,
            BulkChargingComplete=1,
            BulkChargingComplete_isUsed=1,
            ChargingComplete=1,
            RemainingTimeToFullSoC=OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=2, Unit=dinunitSymbolType_Ah, Unit_isUsed=1, Value=12),
            RemainingTimeToFullSoC_isUsed=1,
            RemainingTimeToBulkSoC=OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=2, Unit=dinunitSymbolType_Ah, Unit_isUsed=1, Value=12),
            RemainingTimeToBulkSoC_isUsed=1,
            EVTargetVoltage=OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=2, Unit=dinunitSymbolType_Ah, Unit_isUsed=1, Value=12)
        )

        # print(f"[Python] {sizeof(dinCurrentDemandReqType)=}")

        self.ov2g.init_dinCurrentDemandReqType(dinCurrentDemandReqType=current_demand_req)

        assert current_demand_req.EVMaximumVoltageLimit_isUsed == 0
        assert current_demand_req.EVMaximumCurrentLimit_isUsed == 0
        assert current_demand_req.EVMaximumPowerLimit_isUsed == 0
        assert current_demand_req.BulkChargingComplete_isUsed == 0
        assert current_demand_req.RemainingTimeToFullSoC_isUsed == 0
        assert current_demand_req.RemainingTimeToBulkSoC_isUsed == 0

        print("[*] OK")
    

    # Validated
    def test_init_dinPreChargeReqType(self):
        print("\n[+] Testing init_dinPreChargeReqType")
        
        pre_charge_req = OpenV2GStructDeclarator.dinPreChargeReqType(
            DC_EVStatus=OpenV2GStructDeclarator.dinDC_EVStatusType(
                EVReady=1,
                EVCabinConditioning=2,
                EVCabinConditioning_isUsed=1,
                EVRESSConditioning=3,
                EVRESSConditioning_isUsed=1,
                EVErrorCode=4,
                EVRESSSOC=50
            ),
            EVTargetVoltage=OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=2, Unit=dinunitSymbolType_Ah, Unit_isUsed=1, Value=12),
            EVTargetCurrent=OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=2, Unit=dinunitSymbolType_Ah, Unit_isUsed=1, Value=12),
        )

        # print(f"[Python] {sizeof(dinPreChargeReqType)=}")

        self.ov2g.init_dinPreChargeReqType(dinPreChargeReqType=pre_charge_req)


        print("[*] OK")

    # Validated
    def test_init_dinSessionSetupResType(self):
        print("\n[+] Testing init_dinSessionSetupResType")

        session_setup_res = OpenV2GStructDeclarator.dinSessionSetupResType(
            ResponseCode=1,
            EVSEID=3000,
            DateTimeNow=16980808,
            DateTimeNow_isUsed=1
        )

        # print(f"[Python] {sizeof(dinSessionSetupResType)=}")

        self.ov2g.init_dinSessionSetupResType(dinSessionSetupResType=session_setup_res)

        assert session_setup_res.DateTimeNow_isUsed == 0

        print("[*] OK")

    # Validated
    def test_init_dinServiceDiscoveryReqType(self):
        print("\n[+] Testing init_dinServiceDiscoveryReqType")
        
        service_discovery_req = OpenV2GStructDeclarator.dinServiceDiscoveryReqType(
            ServiceScope="Charge",
            ServiceScope_isUsed=1,
            ServiceCategory=2,
            ServiceCategory_isUsed=1
        )
        
        print(f"[Python] {sizeof(dinServiceDiscoveryReqType)=}")

        self.ov2g.init_dinServiceDiscoveryReqType(dinServiceDiscoveryReqType=service_discovery_req)

        assert service_discovery_req.ServiceScope_isUsed == 0
        assert service_discovery_req.ServiceCategory_isUsed == 0

        print("[*] OK")

    # Validated
    def test_init_dinServicePaymentSelectionResType(self):
        print("\n[+] Testing init_dinServicePaymentSelectionResType")

        service_payment_selection_req = OpenV2GStructDeclarator.dinServicePaymentSelectionResType(
            ResponseCode=2
        )

        # print(f"[Python] {sizeof(dinServicePaymentSelectionResType)=}")

        self.ov2g.init_dinServicePaymentSelectionResType(dinServicePaymentSelectionResType=service_payment_selection_req)


        print("[*] OK")

    # Validated
    def test_init_dinPaymentDetailsReqType(self):
        print("\n[+] Testing init_dinPaymentDetailsReqType")

        payment_details_req = OpenV2GStructDeclarator.dinPaymentDetailsReqType(
            ContractID="ContractID",
            ContractSignatureCertChain=OpenV2GStructDeclarator.dinCertificateChainType(
                Certificate="MainCertificate",
                SubCertificates=OpenV2GStructDeclarator.dinSubCertificatesType(
                    Certificate=[
                        "Certificate 1",
                        "Certificate 2",
                        "Certificate 3",
                    ]
                ),
                SubCertificates_isUsed=1   
            )
        )

        # print(f"[Python] {sizeof(dinPaymentDetailsReqType)=}")

        self.ov2g.init_dinPaymentDetailsReqType(dinPaymentDetailsReqType=payment_details_req)
            
        print("[*] OK")

    # Validated
    def test_init_dinChargeParameterDiscoveryReqType(self):
        print("\n[+] Testing init_dinChargeParameterDiscoveryReqType")

        charge_parameter_discovery_req = OpenV2GStructDeclarator.dinChargeParameterDiscoveryReqType(
            EVRequestedEnergyTransferType=2,
            EVChargeParameter=OpenV2GStructDeclarator.dinEVChargeParameterType(noContent=1),
            EVChargeParameter_isUsed=1,
            AC_EVChargeParameter=OpenV2GStructDeclarator.dinAC_EVChargeParameterType(
                DepartureTime=10,
                EAmount=OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=dinunitSymbolType_Wh, Unit_isUsed=1, Value=3000),
                EVMaxVoltage=OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=dinunitSymbolType_V, Unit_isUsed=1, Value=400),
                EVMaxCurrent=OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=dinunitSymbolType_A, Unit_isUsed=1, Value=10),
                EVMinCurrent=OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=dinunitSymbolType_A, Unit_isUsed=1, Value=1),
            ),
            AC_EVChargeParameter_isUsed=1,
            DC_EVChargeParameter=OpenV2GStructDeclarator.dinDC_EVChargeParameterType(
                DC_EVStatus=OpenV2GStructDeclarator.dinDC_EVStatusType(
                    EVReady=1,
                    EVCabinConditioning=2,
                    EVCabinConditioning_isUsed=1,
                    EVRESSConditioning=3,
                    EVRESSConditioning_isUsed=1,
                    EVErrorCode=4,
                    EVRESSSOC=50
                ),
                EVMaximumCurrentLimit=OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=2, Unit_isUsed=1, Value=100),
                EVMaximumPowerLimit=OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=2, Unit_isUsed=1, Value=100),
                EVMaximumPowerLimit_isUsed=1,
                EVMaximumVoltageLimit=OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=2, Unit_isUsed=1, Value=100),
                EVEnergyCapacity=OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=2, Unit_isUsed=1, Value=100),
                EVEnergyCapacity_isUsed=1,
                EVEnergyRequest=OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=2, Unit_isUsed=1, Value=100),
                EVEnergyRequest_isUsed=1,
                FullSOC=50,
                FullSOC_isUsed=1,
                BulkSOC=40,
                BulkSOC_isUsed=1,
            ),
            DC_EVChargeParameter_isUsed=1
        )

        # print(f"[Python] {sizeof(dinChargeParameterDiscoveryReqType)=}")

        self.ov2g.init_dinChargeParameterDiscoveryReqType(dinChargeParameterDiscoveryReqType=charge_parameter_discovery_req)

        assert charge_parameter_discovery_req.EVChargeParameter_isUsed == 0
        assert charge_parameter_discovery_req.AC_EVChargeParameter_isUsed == 0
        assert charge_parameter_discovery_req.DC_EVChargeParameter_isUsed == 0
            
        print("[*] OK")


    # Validated
    def test_init_dinMeteringReceiptReqType(self):
        print("\n[+] Testing init_dinMeteringReceiptReqType")

        metering_receipt_req = OpenV2GStructDeclarator.dinMeteringReceiptReqType(
            Id="Receipt ID",
            Id_isUsed=1,
            SessionID=87,
            SAScheduleTupleID=1,
            SAScheduleTupleID_isUsed=1,
            MeterInfo=OpenV2GStructDeclarator.dinMeterInfoType(
                MeterID="AC_Meter1",
                MeterReading=OpenV2GStructDeclarator.dinPhysicalValueType(Multiplier=1, Unit=1, Unit_isUsed=1, Value=10),
                MeterReading_isUsed=1,
                SigMeterReading=3291,
                SigMeterReading_isUsed=1,
                MeterStatus=2,
                MeterStatus_isUsed=1,
                TMeter=321,
                TMeter_isUsed=1
            )
        )

        # print(f"[Python] {sizeof(dinMeteringReceiptReqType)=}")

        self.ov2g.init_dinMeteringReceiptReqType(dinMeteringReceiptReqType=metering_receipt_req)

        assert metering_receipt_req.Id_isUsed == 0
        assert metering_receipt_req.SAScheduleTupleID_isUsed == 0

        print("[*] OK")

    
    # Validated
    def test_init_dinMeteringReceiptResType(self):
        print("\n[+] Testing init_dinMeteringReceiptResType")

        metering_receipt_res = OpenV2GStructDeclarator.dinMeteringReceiptResType(
            ResponseCode=2,
            AC_EVSEStatus=OpenV2GStructDeclarator.dinAC_EVSEStatusType(
                PowerSwitchClosed=1,
                RCD=1,
                NotificationMaxDelay=10,
                EVSENotification=1
            )
        )

        # print(f"[Python] {sizeof(dinMeteringReceiptResType)=}")

        self.ov2g.init_dinMeteringReceiptResType(dinMeteringReceiptResType=metering_receipt_res)

        print("[*] OK")

    
    # Validated
    def test_init_dinSessionStopResType(self):
        print("\n[+] Testing init_dinSessionStopResType")

        session_stop_res = OpenV2GStructDeclarator.dinSessionStopResType(
            ResponseCode=2
        )

        self.ov2g.init_dinSessionStopResType(dinSessionStopResType=session_stop_res)            

        print("[*] OK")


    # Validated
    def test_init_dinCertificateUpdateReqType(self):
        print("\n[+] Testing init_dinCertificateUpdateReqType")

        certificate_update_req = OpenV2GStructDeclarator.dinCertificateUpdateReqType(
            Id="ID",
            Id_isUsed=1,
            ContractSignatureCertChain=OpenV2GStructDeclarator.dinCertificateChainType(
                Certificate="MainCertificate",
                SubCertificates=OpenV2GStructDeclarator.dinSubCertificatesType(
                    Certificate=[
                        "Certificate 1",
                        "Certificate 2",
                        "Certificate 3",
                    ]
                ),
                SubCertificates_isUsed=1   
            ),
            ContractID="Contract",
            ListOfRootCertificateIDs=OpenV2GStructDeclarator.dinListOfRootCertificateIDsType(
                RootCertificateID=[
                    "ID1", "ID2", "ID3"
                ]
            ),
            DHParams="DHParams"
        )

        # print(f"[Python] {sizeof(dinCertificateUpdateReqType)=}")

        self.ov2g.init_dinCertificateUpdateReqType(dinCertificateUpdateReqType=certificate_update_req)

        assert certificate_update_req.Id_isUsed == 0

        print("[*] OK")


    # Validated
    def test_init_dinCertificateInstallationResType(self):
        print("\n[+] Testing init_dinCertificateInstallationResType")

        certificate_installation_res = OpenV2GStructDeclarator.dinCertificateInstallationResType(
            Id="ID",
            ResponseCode=2,
            ContractSignatureCertChain=OpenV2GStructDeclarator.dinCertificateChainType(
                Certificate="MainCertificate",
                SubCertificates=OpenV2GStructDeclarator.dinSubCertificatesType(
                    Certificate=[
                        "Certificate 1",
                        "Certificate 2",
                        "Certificate 3",
                    ]
                ),
                SubCertificates_isUsed=1   
            ),
            ContractSignatureEncryptedPrivateKey="super secret key",
            DHParams="DH Parameters",
            ContractID="Contract ID"
        )

        # print(f"[Python] {sizeof(dinCertificateInstallationResType)=}")

        self.ov2g.init_dinCertificateInstallationResType(dinCertificateInstallationResType=certificate_installation_res)

        print("[*] OK")

    # Validated
    def test_init_dinCableCheckResType(self):
        print("\n[+] Testing init_dinCableCheckResType")

        cable_check_res = OpenV2GStructDeclarator.dinCableCheckResType(
            ResponseCode=2,
            DC_EVSEStatus=OpenV2GStructDeclarator.dinDC_EVSEStatusType(
                EVSEIsolationStatus=dinisolationLevelType_Valid,
                EVSEIsolationStatus_isUsed=1,
                EVSEStatusCode=dinDC_EVSEStatusCodeType_EVSE_Ready,
                NotificationMaxDelay=10,
                EVSENotification=1
            ),
            EVSEProcessing=1
        )

        print(f"[Python] {sizeof(dinCableCheckResType)=}")

        self.ov2g.init_dinCableCheckResType(dinCableCheckResType=cable_check_res)
            

        print("[*] OK")

    # Validated
    def test_init_dinBodyType(self):
        print("\n[+] Testing init_dinBodyType")

        body = OpenV2GStructDeclarator.dinBodyType(
            SessionSetupReq=OpenV2GStructDeclarator.dinSessionSetupReqType(EVCCID=1),
            SessionSetupReq_isUsed=1
        )

        print(f"[Python] {sizeof(dinBodyType)=}")

        self.ov2g.init_dinBodyType(dinBodyType=body)

        assert body.BodyElement_isUsed == 0
        assert body.SessionSetupReq_isUsed == 0
        assert body.SessionSetupRes_isUsed == 0
        assert body.ServiceDiscoveryReq_isUsed == 0
        assert body.ServiceDiscoveryRes_isUsed == 0
        assert body.ServiceDetailReq_isUsed == 0
        assert body.ServiceDetailRes_isUsed == 0
        assert body.ServicePaymentSelectionReq_isUsed == 0
        assert body.ServicePaymentSelectionRes_isUsed == 0
        assert body.PaymentDetailsReq_isUsed == 0
        assert body.PaymentDetailsRes_isUsed == 0
        assert body.ContractAuthenticationReq_isUsed == 0
        assert body.ContractAuthenticationRes_isUsed == 0
        assert body.ChargeParameterDiscoveryReq_isUsed == 0
        assert body.ChargeParameterDiscoveryRes_isUsed == 0
        assert body.PowerDeliveryReq_isUsed == 0
        assert body.PowerDeliveryRes_isUsed == 0
        assert body.ChargingStatusReq_isUsed == 0
        assert body.ChargingStatusRes_isUsed == 0
        assert body.MeteringReceiptReq_isUsed == 0
        assert body.MeteringReceiptRes_isUsed == 0
        assert body.SessionStopReq_isUsed == 0
        assert body.SessionStopRes_isUsed == 0
        assert body.CertificateUpdateReq_isUsed == 0
        assert body.CertificateUpdateRes_isUsed == 0
        assert body.CertificateInstallationReq_isUsed == 0
        assert body.CertificateInstallationRes_isUsed == 0
        assert body.CableCheckReq_isUsed == 0
        assert body.CableCheckRes_isUsed == 0
        assert body.PreChargeReq_isUsed == 0
        assert body.PreChargeRes_isUsed == 0
        assert body.CurrentDemandReq_isUsed == 0
        assert body.CurrentDemandRes_isUsed == 0
        assert body.WeldingDetectionReq_isUsed == 0
        assert body.WeldingDetectionRes_isUsed == 0
        print("[*] OK")

    # Validated
    def test_init_dinAnonType_V2G_Message(self):
        print("\n[+] Testing init_dinAnonType_V2G_Message")

        v2g_message = OpenV2GStructDeclarator.dinAnonType_V2G_Message(
            Header=OpenV2GStructDeclarator.dinMessageHeaderType(
                SessionID=10,
                Notification=OpenV2GStructDeclarator.dinNotificationType(
                    FaultCode=2,
                    FaultMsg="High temperature",
                    FaultMsg_isUsed=1
                ),
                Signature=OpenV2GStructDeclarator.dinSignatureType(
                    Id="ID",
                    Id_isUsed=1,
                    SignedInfo=OpenV2GStructDeclarator.dinSignedInfoType(
                        Id="SigInfoID",
                        Id_isUsed=1,
                        CanonicalizationMethod=OpenV2GStructDeclarator.dinCanonicalizationMethodType(
                            Algorithm="ALGORITHM",
                            ANY="Any str",
                            ANY_isUsed=1
                        ),
                        SignatureMethod=OpenV2GStructDeclarator.dinSignatureMethodType(
                            Algorithm="SHA256",
                            HMACOutputLength=10,
                            HMACOutputLength_isUsed=1,
                            ANY="ANY String",
                            ANY_isUsed=1
                        ),
                        Reference=[
                            OpenV2GStructDeclarator.dinReferenceType(
                                Id="Reference ID",
                                Id_isUsed=1,
                                URI="file://home/alex",
                                URI_isUsed=1,
                                Type="Type",
                                Type_isUsed=1,
                                Transforms=OpenV2GStructDeclarator.dinTransformsType(
                                    Transform=[
                                        OpenV2GStructDeclarator.dinTransformType(
                                            Algorithm="SHA256",
                                            ANY="ANY string",
                                            ANY_isUsed=1,
                                            XPath="/home/alex"
                                        )
                                    ]
                                ),
                                Transforms_isUsed=1,
                                DigestMethod=OpenV2GStructDeclarator.dinDigestMethodType(
                                    Algorithm="SHA256",
                                    ANY="ANY str",
                                    ANY_isUsed=1
                                ),
                                DigestValue="Digest value"
                            )
                        ]
                    ),
                    SignatureValue=OpenV2GStructDeclarator.dinSignatureValueType(
                        Id="SignatureValue ID",
                        Id_isUsed=1,
                        CONTENT="CONTENT"
                    ),
                    KeyInfo=OpenV2GStructDeclarator.dinKeyInfoType(
                        Id="ID",
                        Id_isUsed=1,
                        KeyName=["Key"],
                        KeyValue=[
                            OpenV2GStructDeclarator.dinKeyValueType(
                                DSAKeyValue=OpenV2GStructDeclarator.dinDSAKeyValueType(
                                    P=1,
                                    P_isUsed=1,
                                    Q=2,
                                    Q_isUsed=1,
                                    G=3,
                                    G_isUsed=1,
                                    Y=4,
                                    J=5,
                                    J_isUsed=1,
                                    Seed=6,
                                    Seed_isUsed=1,
                                    PgenCounter=7,
                                    PgenCounter_isUsed=1
                                ),
                                DSAKeyValue_isUsed=1,
                                RSAKeyValue=OpenV2GStructDeclarator.dinRSAKeyValueType(
                                    Modulus=10,
                                    Exponent=2
                                ),
                                RSAKeyValue_isUsed=1,
                                ANY="ANY STRING",
                                ANY_isUsed=1
                            )   
                        ],
                        RetrievalMethod=[
                            OpenV2GStructDeclarator.dinRetrievalMethodType(
                                URI="/home/alex",
                                URI_isUsed=1,
                                Type="the type",
                                Type_isUsed=1,
                                Transforms=OpenV2GStructDeclarator.dinTransformsType(
                                    Transform=[
                                        OpenV2GStructDeclarator.dinTransformType(
                                            Algorithm="SHA112",
                                            ANY="ANy str",
                                            ANY_isUsed=1,
                                            XPath="/home/alex"
                                        )
                                    ]
                                ),
                                Transforms_isUsed=1
                            )
                        ],
                        X509Data=[
                            OpenV2GStructDeclarator.dinX509DataType(
                                X509IssuerSerial=[
                                    OpenV2GStructDeclarator.dinX509IssuerSerialType(
                                        X509IssuerName="The issuer name",
                                        X509SerialNumber=28731,
                                    )
                                ],
                                X509SKI=37182,
                                X509SubjectName="Subject Name",
                                X509Certificate=39123819,
                                X509CRL=231939,
                                ANY="Anything",
                                ANY_isUsed=1
                            )
                        ],
                        PGPData=[
                            OpenV2GStructDeclarator.dinPGPDataType(
                                PGPKeyID="PGPKEYID",
                                PGPKeyID_isUsed=1,
                                PGPKeyPacket="The packet",
                                PGPKeyPacket_isUsed=1,
                                ANY="ANY STR",
                                ANY_isUsed=1
                            )
                        ],
                        SPKIData=[
                            OpenV2GStructDeclarator.dinSPKIDataType(
                                SPKISexp=64, 
                                ANY="Any String", 
                                ANY_isUsed=1
                            )
                        ],
                        MgmtData=[
                            "MgmtData"
                        ],
                        ANY="ANY str",
                        ANY_isUsed=1
                    ),
                    KeyInfo_isUsed=1,
                    Object=[
                        OpenV2GStructDeclarator.dinObjectType(
                            Id="Object ID",
                            Id_isUsed=1,
                            MimeType="MimeType",
                            MimeType_isUsed=1,
                            Encoding="Enconding",
                            Encoding_isUsed=1,
                            ANY="ANY str",
                            ANY_isUsed=1
                        )
                    ]
                ),
                Notification_isUsed=1,
                Signature_isUsed=1
            ),

            Body=OpenV2GStructDeclarator.dinBodyType(
                SessionSetupReq=OpenV2GStructDeclarator.dinSessionSetupReqType(EVCCID=1),
                SessionSetupReq_isUsed=1
            )
        )

        # print(f"[Python] {sizeof(dinAnonType_V2G_Message)=}")

        self.ov2g.init_dinAnonType_V2G_Message(dinAnonType_V2G_Message=v2g_message)

        print("[*] OK")

    # Validated
    def test_init_dinManifestType(self):
        print("\n[+] Testing init_dinManifestType")

        manifest = OpenV2GStructDeclarator.dinManifestType(
            Id="ID",
            Id_isUsed=1,
            Reference=[
                OpenV2GStructDeclarator.dinReferenceType(
                    Id="Reference ID",
                    Id_isUsed=1,
                    URI="file://home/alex",
                    URI_isUsed=1,
                    Type="Type",
                    Type_isUsed=1,
                    Transforms=OpenV2GStructDeclarator.dinTransformsType(
                        Transform=[
                            OpenV2GStructDeclarator.dinTransformType(
                                Algorithm="SHA256",
                                ANY="ANY string",
                                ANY_isUsed=1,
                                XPath="/home/alex"
                            )
                        ]
                    ),
                    Transforms_isUsed=1,
                    DigestMethod=OpenV2GStructDeclarator.dinDigestMethodType(
                        Algorithm="SHA256",
                        ANY="ANY str",
                        ANY_isUsed=1
                    ),
                    DigestValue="Digest value"
                )
            ]
        )

        # print(f"[Python] {sizeof(dinManifestType)=}")

        self.ov2g.init_dinManifestType(dinManifestType=manifest)

        assert manifest.Id_isUsed == 0
        assert manifest.Reference.arrayLen == 0
        
        print("[*] OK")

    # Validated
    def test_init_dinEXIDocument(self):
        print("\n[+] Testing init_dinEXIDocument")

        exi_document = OpenV2GStructDeclarator.dinEXIDocument(
            SessionSetupRes=OpenV2GStructDeclarator.dinSessionSetupResType(
                ResponseCode=1,
                EVSEID=3000,
                DateTimeNow=16980808,
                DateTimeNow_isUsed=1
            ),
            SessionSetupRes_isUsed=1
        )

        print(f"[Python] {sizeof(dinEXIDocument)=}")

        self.ov2g.init_dinEXIDocument(exiDoc=exi_document)
        
        assert exi_document.BodyElement_isUsed == 0
        assert exi_document.V2G_Message_isUsed == 0
        assert exi_document.SignatureProperty_isUsed == 0
        assert exi_document.DSAKeyValue_isUsed == 0
        assert exi_document.SignatureProperties_isUsed == 0
        assert exi_document.KeyValue_isUsed == 0
        assert exi_document.Transforms_isUsed == 0
        assert exi_document.DigestMethod_isUsed == 0
        assert exi_document.Signature_isUsed == 0
        assert exi_document.RetrievalMethod_isUsed == 0
        assert exi_document.Manifest_isUsed == 0
        assert exi_document.Reference_isUsed == 0
        assert exi_document.CanonicalizationMethod_isUsed == 0
        assert exi_document.RSAKeyValue_isUsed == 0
        assert exi_document.Transform_isUsed == 0
        assert exi_document.PGPData_isUsed == 0
        assert exi_document.MgmtData_isUsed == 0
        assert exi_document.SignatureMethod_isUsed == 0
        assert exi_document.KeyInfo_isUsed == 0
        assert exi_document.SPKIData_isUsed == 0
        assert exi_document.X509Data_isUsed == 0
        assert exi_document.SignatureValue_isUsed == 0
        assert exi_document.KeyName_isUsed == 0
        assert exi_document.DigestValue_isUsed == 0
        assert exi_document.SignedInfo_isUsed == 0
        assert exi_document.Object_isUsed == 0
        assert exi_document.DC_EVSEStatus_isUsed == 0
        assert exi_document.RelativeTimeInterval_isUsed == 0
        assert exi_document.SalesTariffEntry_isUsed == 0
        assert exi_document.DC_EVPowerDeliveryParameter_isUsed == 0
        assert exi_document.SASchedules_isUsed == 0
        assert exi_document.AC_EVChargeParameter_isUsed == 0
        assert exi_document.SAScheduleList_isUsed == 0
        assert exi_document.DC_EVStatus_isUsed == 0
        assert exi_document.ServiceCharge_isUsed == 0
        assert exi_document.EVStatus_isUsed == 0
        assert exi_document.DC_EVChargeParameter_isUsed == 0
        assert exi_document.DC_EVSEChargeParameter_isUsed == 0
        assert exi_document.EVSEStatus_isUsed == 0
        assert exi_document.TimeInterval_isUsed == 0
        assert exi_document.EVPowerDeliveryParameter_isUsed == 0
        assert exi_document.EVSEChargeParameter_isUsed == 0
        assert exi_document.AC_EVSEStatus_isUsed == 0
        assert exi_document.Entry_isUsed == 0
        assert exi_document.AC_EVSEChargeParameter_isUsed == 0
        assert exi_document.PMaxScheduleEntry_isUsed == 0
        assert exi_document.EVChargeParameter_isUsed == 0
        assert exi_document.ServiceDiscoveryReq_isUsed == 0
        assert exi_document.ServiceDiscoveryRes_isUsed == 0
        assert exi_document.MeteringReceiptReq_isUsed == 0
        assert exi_document.PaymentDetailsReq_isUsed == 0
        assert exi_document.MeteringReceiptRes_isUsed == 0
        assert exi_document.PaymentDetailsRes_isUsed == 0
        assert exi_document.SessionSetupReq_isUsed == 0
        assert exi_document.SessionSetupRes_isUsed == 0
        assert exi_document.CableCheckReq_isUsed == 0
        assert exi_document.CableCheckRes_isUsed == 0
        assert exi_document.ContractAuthenticationReq_isUsed == 0
        assert exi_document.CertificateInstallationReq_isUsed == 0
        assert exi_document.ContractAuthenticationRes_isUsed == 0
        assert exi_document.CertificateInstallationRes_isUsed == 0
        assert exi_document.WeldingDetectionReq_isUsed == 0
        assert exi_document.WeldingDetectionRes_isUsed == 0
        assert exi_document.CertificateUpdateReq_isUsed == 0
        assert exi_document.CertificateUpdateRes_isUsed == 0
        assert exi_document.PowerDeliveryReq_isUsed == 0
        assert exi_document.PowerDeliveryRes_isUsed == 0
        assert exi_document.ChargingStatusReq_isUsed == 0
        assert exi_document.ChargingStatusRes_isUsed == 0
        assert exi_document.CurrentDemandReq_isUsed == 0
        assert exi_document.PreChargeReq_isUsed == 0
        assert exi_document.CurrentDemandRes_isUsed == 0
        assert exi_document.PreChargeRes_isUsed == 0
        assert exi_document.ServicePaymentSelectionReq_isUsed == 0
        assert exi_document.SessionStopReq_isUsed == 0
        assert exi_document.ServicePaymentSelectionRes_isUsed == 0
        assert exi_document.SessionStopRes_isUsed == 0
        assert exi_document.ChargeParameterDiscoveryReq_isUsed == 0
        assert exi_document.ChargeParameterDiscoveryRes_isUsed == 0
        assert exi_document.ServiceDetailReq_isUsed == 0
        assert exi_document.ServiceDetailRes_isUsed == 0
        
        print("[*] OK")

    # Validated
    def test_encode_dinExiDocument(self):
        print("\n[+] Testing encode_dinExiDocument")

        buffer = (c_ubyte*256)()
        size = c_size_t(256)
        pos = c_size_t(8)
        buffer_byte = c_uint8(0)
        buffer_capacity = c_uint8(256)
        # encode request

        stream = OpenV2GStructDeclarator.bitstream_t(
            size=size,
            data=buffer,
            pos=pos,
            buffer=buffer_byte,
            capacity=buffer_capacity
        )

        exi_doc = OpenV2GStructDeclarator.dinEXIDocument(
            SessionSetupRes=OpenV2GStructDeclarator.dinSessionSetupResType(
                ResponseCode=1,
                EVSEID=3000,
                DateTimeNow=16980808,
                DateTimeNow_isUsed=1
            ),
            SessionSetupRes_isUsed=1
        )

        errn = self.ov2g.encode_dinExiDocument(stream=stream, exiDoc=exi_doc)
        print(f"{errn=}")

        assert errn == 0

        print("[*] OK")


    # open_v2g/din/dinEXIDatatypesDecoder.c
    def test_encode_and_decode_dinEXIDocument(self):
        print("\n[+] Testing encode_and_decode_dinEXIDocument")

        size = c_size_t(256)
        buffer_byte = c_uint8(0)
        buffer_capacity = c_uint8(256)

        buffer = (c_ubyte*256)()
        pos = c_size_t(8)
        stream = OpenV2GStructDeclarator.bitstream_t(
            size=size,
            data=buffer,
            pos=pos,
            buffer=buffer_byte,
            capacity=buffer_capacity
        )

        exi_doc = OpenV2GStructDeclarator.dinEXIDocument(
            SessionSetupRes=OpenV2GStructDeclarator.dinSessionSetupResType(
                ResponseCode=1,
                EVSEID=3000,
                DateTimeNow=16980808,
                DateTimeNow_isUsed=1
            ),
            SessionSetupRes_isUsed=1
        )

        # Encoding EXI document
        errn = self.ov2g.encode_dinExiDocument(stream=stream, exiDoc=exi_doc)

        assert errn == 0

        # Let's decode it and store the information on a new exiDoc (initially empty)

        # Reset pos
        pos = c_size_t(8)
        stream.pos = pointer(pos)

        exiDocDecoded = OpenV2GStructDeclarator.dinEXIDocument() # empty

        errn = self.ov2g.decode_dinExiDocument(stream=stream, exiDoc=exiDocDecoded)

        assert errn == 0
        
        print(f"[Python] {exiDocDecoded.SessionSetupRes.ResponseCode=}")
        print(f"[Python] {exiDocDecoded.SessionSetupRes.EVSEID.bytes[:]=}")
        print(f"[Python] {exiDocDecoded.SessionSetupRes.DateTimeNow=}")
        print(f"[Python] {exiDocDecoded.SessionSetupRes.DateTimeNow_isUsed=}")

        print("[*] OK")


if __name__ == '__main__':
    unittest.main()



