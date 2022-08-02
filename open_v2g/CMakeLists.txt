cmake_minimum_required(VERSION 3.5)

project(open_v2g)

include_directories(source/appHandshake)
include_directories(source/transport)
include_directories(source/din)
include_directories(source/codec)
include_directories(source/iso1)
include_directories(source/iso2)

add_library(open_v2g STATIC
		source/appHandshake/appHandEXIDatatypes.c
		source/appHandshake/appHandEXIDatatypes.h
		source/appHandshake/appHandEXIDatatypesDecoder.c
		source/appHandshake/appHandEXIDatatypesDecoder.h
		source/appHandshake/appHandEXIDatatypesEncoder.c
		source/appHandshake/appHandEXIDatatypesEncoder.h
		source/codec/BitInputStream.c
		source/codec/BitInputStream.h
		source/codec/BitOutputStream.c
		source/codec/BitOutputStream.h
		source/codec/ByteStream.c
		source/codec/ByteStream.h
		source/codec/DecoderChannel.c
		source/codec/DecoderChannel.h
		source/codec/EncoderChannel.c
		source/codec/EncoderChannel.h
		source/codec/ErrorCodes.h
		source/codec/EXIConfig.h
		source/codec/EXIHeaderDecoder.c
		source/codec/EXIHeaderDecoder.h
		source/codec/EXIHeaderEncoder.c
		source/codec/EXIHeaderEncoder.h
		source/codec/EXIOptions.h
		source/codec/EXITypes.h
		source/codec/MethodsBag.c
		source/codec/MethodsBag.h
		source/din/dinEXIDatatypes.c
		source/din/dinEXIDatatypes.h
		source/din/dinEXIDatatypesDecoder.c
		source/din/dinEXIDatatypesDecoder.h
		source/din/dinEXIDatatypesEncoder.c
		source/din/dinEXIDatatypesEncoder.h
		source/iso1/iso1EXIDatatypes.c
		source/iso1/iso1EXIDatatypes.h
		source/iso1/iso1EXIDatatypesDecoder.c
		source/iso1/iso1EXIDatatypesDecoder.h
		source/iso1/iso1EXIDatatypesEncoder.c
		source/iso1/iso1EXIDatatypesEncoder.h
		source/iso2/iso2EXIDatatypes.c
		source/iso2/iso2EXIDatatypes.h
		source/iso2/iso2EXIDatatypesDecoder.c
		source/iso2/iso2EXIDatatypesDecoder.h
		source/iso2/iso2EXIDatatypesEncoder.c
		source/iso2/iso2EXIDatatypesEncoder.h
		source/transport/v2gtp.c
		source/transport/v2gtp.h
)
target_compile_options(open_v2g PRIVATE)
