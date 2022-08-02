/*
 * Copyright (C) 2007-2018 Siemens AG
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Lesser General Public License as published
 * by the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Lesser General Public License for more details.
 *
 * You should have received a copy of the GNU Lesser General Public License
 * along with this program. If not, see <http://www.gnu.org/licenses/>.
 */

/*******************************************************************
 *
 * @author Daniel.Peintner.EXT@siemens.com
 * @version 0.9.4 
 * @contact Richard.Kuntschke@siemens.com
 *
 * <p>Code generated by EXIdizer</p>
 * <p>Schema: xmldsig-core-schema.xsd</p>
 *
 *
 ********************************************************************/



#include <stdint.h>

#include "xmldsigEXIDatatypes.h"
#include "../codec/EXITypes.h"


#ifndef EXI_xmldsig_DATATYPES_C
#define EXI_xmldsig_DATATYPES_C

#if DEPLOY_XMLDSIG_CODEC == SUPPORT_YES


void init_xmldsigEXIDocument(struct xmldsigEXIDocument* exiDoc) {
	exiDoc->SignatureProperty_isUsed = 0u;
	exiDoc->DSAKeyValue_isUsed = 0u;
	exiDoc->SignatureProperties_isUsed = 0u;
	exiDoc->KeyValue_isUsed = 0u;
	exiDoc->Transforms_isUsed = 0u;
	exiDoc->DigestMethod_isUsed = 0u;
	exiDoc->Signature_isUsed = 0u;
	exiDoc->RetrievalMethod_isUsed = 0u;
	exiDoc->Manifest_isUsed = 0u;
	exiDoc->Reference_isUsed = 0u;
	exiDoc->CanonicalizationMethod_isUsed = 0u;
	exiDoc->RSAKeyValue_isUsed = 0u;
	exiDoc->Transform_isUsed = 0u;
	exiDoc->PGPData_isUsed = 0u;
	exiDoc->MgmtData_isUsed = 0u;
	exiDoc->SignatureMethod_isUsed = 0u;
	exiDoc->KeyInfo_isUsed = 0u;
	exiDoc->SPKIData_isUsed = 0u;
	exiDoc->X509Data_isUsed = 0u;
	exiDoc->SignatureValue_isUsed = 0u;
	exiDoc->KeyName_isUsed = 0u;
	exiDoc->DigestValue_isUsed = 0u;
	exiDoc->SignedInfo_isUsed = 0u;
	exiDoc->Object_isUsed = 0u;
}


#if DEPLOY_XMLDSIG_CODEC_FRAGMENT == SUPPORT_YES
void init_xmldsigEXIFragment(struct xmldsigEXIFragment* exiFrag) {
	exiFrag->DigestValue_isUsed = 0u;
	exiFrag->X509Data_isUsed = 0u;
	exiFrag->KeyValue_isUsed = 0u;
	exiFrag->DigestMethod_isUsed = 0u;
	exiFrag->SPKISexp_isUsed = 0u;
	exiFrag->Transforms_isUsed = 0u;
	exiFrag->KeyName_isUsed = 0u;
	exiFrag->X509IssuerName_isUsed = 0u;
	exiFrag->MgmtData_isUsed = 0u;
	exiFrag->Reference_isUsed = 0u;
	exiFrag->SignatureProperties_isUsed = 0u;
	exiFrag->PGPKeyID_isUsed = 0u;
	exiFrag->PGPData_isUsed = 0u;
	exiFrag->DSAKeyValue_isUsed = 0u;
	exiFrag->SignatureValue_isUsed = 0u;
	exiFrag->KeyInfo_isUsed = 0u;
	exiFrag->SignatureProperty_isUsed = 0u;
	exiFrag->PGPKeyPacket_isUsed = 0u;
	exiFrag->PGPKeyPacket_isUsed = 0u;
	exiFrag->HMACOutputLength_isUsed = 0u;
	exiFrag->Exponent_isUsed = 0u;
	exiFrag->Manifest_isUsed = 0u;
	exiFrag->P_isUsed = 0u;
	exiFrag->CanonicalizationMethod_isUsed = 0u;
	exiFrag->Q_isUsed = 0u;
	exiFrag->Seed_isUsed = 0u;
	exiFrag->X509SubjectName_isUsed = 0u;
	exiFrag->X509Certificate_isUsed = 0u;
	exiFrag->RSAKeyValue_isUsed = 0u;
	exiFrag->X509IssuerSerial_isUsed = 0u;
	exiFrag->SPKIData_isUsed = 0u;
	exiFrag->G_isUsed = 0u;
	exiFrag->J_isUsed = 0u;
	exiFrag->SignedInfo_isUsed = 0u;
	exiFrag->X509SKI_isUsed = 0u;
	exiFrag->Transform_isUsed = 0u;
	exiFrag->XPath_isUsed = 0u;
	exiFrag->Object_isUsed = 0u;
	exiFrag->X509SerialNumber_isUsed = 0u;
	exiFrag->RetrievalMethod_isUsed = 0u;
	exiFrag->Modulus_isUsed = 0u;
	exiFrag->X509CRL_isUsed = 0u;
	exiFrag->Signature_isUsed = 0u;
	exiFrag->Y_isUsed = 0u;
	exiFrag->SignatureMethod_isUsed = 0u;
	exiFrag->PgenCounter_isUsed = 0u;
}
#endif /* DEPLOY_XMLDSIG_CODEC_FRAGMENT */

void init_xmldsigCanonicalizationMethodType(struct xmldsigCanonicalizationMethodType* xmldsigCanonicalizationMethodType) {
	xmldsigCanonicalizationMethodType->ANY_isUsed = 0u;
}

void init_xmldsigManifestType(struct xmldsigManifestType* xmldsigManifestType) {
	xmldsigManifestType->Id_isUsed = 0u;
	xmldsigManifestType->Reference.arrayLen = 0u;
}

void init_xmldsigObjectType(struct xmldsigObjectType* xmldsigObjectType) {
	xmldsigObjectType->Id_isUsed = 0u;
	xmldsigObjectType->MimeType_isUsed = 0u;
	xmldsigObjectType->Encoding_isUsed = 0u;
	xmldsigObjectType->ANY_isUsed = 0u;
}

void init_xmldsigTransformType(struct xmldsigTransformType* xmldsigTransformType) {
	xmldsigTransformType->ANY_isUsed = 0u;
	xmldsigTransformType->XPath.arrayLen = 0u;
}

void init_xmldsigSignatureMethodType(struct xmldsigSignatureMethodType* xmldsigSignatureMethodType) {
	xmldsigSignatureMethodType->HMACOutputLength_isUsed = 0u;
	xmldsigSignatureMethodType->ANY_isUsed = 0u;
}

void init_xmldsigDigestMethodType(struct xmldsigDigestMethodType* xmldsigDigestMethodType) {
	xmldsigDigestMethodType->ANY_isUsed = 0u;
}

void init_xmldsigRetrievalMethodType(struct xmldsigRetrievalMethodType* xmldsigRetrievalMethodType) {
	xmldsigRetrievalMethodType->URI_isUsed = 0u;
	xmldsigRetrievalMethodType->Type_isUsed = 0u;
	xmldsigRetrievalMethodType->Transforms_isUsed = 0u;
}

void init_xmldsigSignatureValueType(struct xmldsigSignatureValueType* xmldsigSignatureValueType) {
	xmldsigSignatureValueType->Id_isUsed = 0u;
}

void init_xmldsigX509IssuerSerialType(struct xmldsigX509IssuerSerialType* xmldsigX509IssuerSerialType) {
	(void)xmldsigX509IssuerSerialType; /* avoid unused warning */
}

void init_xmldsigSignedInfoType(struct xmldsigSignedInfoType* xmldsigSignedInfoType) {
	xmldsigSignedInfoType->Id_isUsed = 0u;
	xmldsigSignedInfoType->Reference.arrayLen = 0u;
}

void init_xmldsigSignaturePropertiesType(struct xmldsigSignaturePropertiesType* xmldsigSignaturePropertiesType) {
	xmldsigSignaturePropertiesType->Id_isUsed = 0u;
	xmldsigSignaturePropertiesType->SignatureProperty.arrayLen = 0u;
}

void init_xmldsigSignaturePropertyType(struct xmldsigSignaturePropertyType* xmldsigSignaturePropertyType) {
	xmldsigSignaturePropertyType->Id_isUsed = 0u;
	xmldsigSignaturePropertyType->ANY_isUsed = 0u;
}

void init_xmldsigKeyValueType(struct xmldsigKeyValueType* xmldsigKeyValueType) {
	xmldsigKeyValueType->DSAKeyValue_isUsed = 0u;
	xmldsigKeyValueType->RSAKeyValue_isUsed = 0u;
	xmldsigKeyValueType->ANY_isUsed = 0u;
}

void init_xmldsigRSAKeyValueType(struct xmldsigRSAKeyValueType* xmldsigRSAKeyValueType) {
	(void)xmldsigRSAKeyValueType; /* avoid unused warning */
}

void init_xmldsigPGPDataType(struct xmldsigPGPDataType* xmldsigPGPDataType) {
	xmldsigPGPDataType->PGPKeyID_isUsed = 0u;
	xmldsigPGPDataType->PGPKeyPacket_isUsed = 0u;
	xmldsigPGPDataType->ANY_isUsed = 0u;
}

void init_xmldsigTransformsType(struct xmldsigTransformsType* xmldsigTransformsType) {
	xmldsigTransformsType->Transform.arrayLen = 0u;
}

void init_xmldsigX509DataType(struct xmldsigX509DataType* xmldsigX509DataType) {
	xmldsigX509DataType->X509IssuerSerial.arrayLen = 0u;
	xmldsigX509DataType->X509SKI.arrayLen = 0u;
	xmldsigX509DataType->X509SubjectName.arrayLen = 0u;
	xmldsigX509DataType->X509Certificate.arrayLen = 0u;
	xmldsigX509DataType->X509CRL.arrayLen = 0u;
	xmldsigX509DataType->ANY_isUsed = 0u;
}

void init_xmldsigSignatureType(struct xmldsigSignatureType* xmldsigSignatureType) {
	xmldsigSignatureType->Id_isUsed = 0u;
	xmldsigSignatureType->KeyInfo_isUsed = 0u;
	xmldsigSignatureType->Object.arrayLen = 0u;
}

void init_xmldsigDSAKeyValueType(struct xmldsigDSAKeyValueType* xmldsigDSAKeyValueType) {
	xmldsigDSAKeyValueType->P_isUsed = 0u;
	xmldsigDSAKeyValueType->Q_isUsed = 0u;
	xmldsigDSAKeyValueType->G_isUsed = 0u;
	xmldsigDSAKeyValueType->J_isUsed = 0u;
	xmldsigDSAKeyValueType->Seed_isUsed = 0u;
	xmldsigDSAKeyValueType->PgenCounter_isUsed = 0u;
}

void init_xmldsigReferenceType(struct xmldsigReferenceType* xmldsigReferenceType) {
	xmldsigReferenceType->Id_isUsed = 0u;
	xmldsigReferenceType->URI_isUsed = 0u;
	xmldsigReferenceType->Type_isUsed = 0u;
	xmldsigReferenceType->Transforms_isUsed = 0u;
}

void init_xmldsigSPKIDataType(struct xmldsigSPKIDataType* xmldsigSPKIDataType) {
	xmldsigSPKIDataType->SPKISexp.arrayLen = 0u;
	xmldsigSPKIDataType->ANY_isUsed = 0u;
}

void init_xmldsigKeyInfoType(struct xmldsigKeyInfoType* xmldsigKeyInfoType) {
	xmldsigKeyInfoType->Id_isUsed = 0u;
	xmldsigKeyInfoType->KeyName.arrayLen = 0u;
	xmldsigKeyInfoType->KeyValue.arrayLen = 0u;
	xmldsigKeyInfoType->RetrievalMethod.arrayLen = 0u;
	xmldsigKeyInfoType->X509Data.arrayLen = 0u;
	xmldsigKeyInfoType->PGPData.arrayLen = 0u;
	xmldsigKeyInfoType->SPKIData.arrayLen = 0u;
	xmldsigKeyInfoType->MgmtData.arrayLen = 0u;
	xmldsigKeyInfoType->ANY_isUsed = 0u;
}



#endif /* DEPLOY_XMLDSIG_CODEC */

#endif

