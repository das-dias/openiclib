import datetime

from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from collections.abc import Iterable as _Iterable, Mapping as _Mapping
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PDK(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    PDK_UNKNOWN: _ClassVar[PDK]
    PDK_SKYWATER130: _ClassVar[PDK]
    PDK_IHP130SG: _ClassVar[PDK]
    PDK_GF180: _ClassVar[PDK]
    PDK_GF90: _ClassVar[PDK]
    PDK_GF45: _ClassVar[PDK]

class CircuitClass(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CIRCUIT_CLASS_UNKNOWN: _ClassVar[CircuitClass]
    CIRCUIT_CLASS_ANALOG: _ClassVar[CircuitClass]
    CIRCUIT_CLASS_DIGITAL: _ClassVar[CircuitClass]
    CIRCUIT_CLASS_MIXED_SIGNAL: _ClassVar[CircuitClass]
    CIRCUIT_CLASS_OPTICAL: _ClassVar[CircuitClass]

class ClassifiedBy(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    CLASSIFIED_BY_UNSPECIFIED: _ClassVar[ClassifiedBy]
    CLASSIFIED_BY_MANUAL: _ClassVar[ClassifiedBy]
    CLASSIFIED_BY_LLM_GITHUB_MODELS: _ClassVar[ClassifiedBy]
    CLASSIFIED_BY_LLM_CLAUDE: _ClassVar[ClassifiedBy]
    CLASSIFIED_BY_LLM_OLLAMA: _ClassVar[ClassifiedBy]
    CLASSIFIED_BY_KEYWORD: _ClassVar[ClassifiedBy]
PDK_UNKNOWN: PDK
PDK_SKYWATER130: PDK
PDK_IHP130SG: PDK
PDK_GF180: PDK
PDK_GF90: PDK
PDK_GF45: PDK
CIRCUIT_CLASS_UNKNOWN: CircuitClass
CIRCUIT_CLASS_ANALOG: CircuitClass
CIRCUIT_CLASS_DIGITAL: CircuitClass
CIRCUIT_CLASS_MIXED_SIGNAL: CircuitClass
CIRCUIT_CLASS_OPTICAL: CircuitClass
CLASSIFIED_BY_UNSPECIFIED: ClassifiedBy
CLASSIFIED_BY_MANUAL: ClassifiedBy
CLASSIFIED_BY_LLM_GITHUB_MODELS: ClassifiedBy
CLASSIFIED_BY_LLM_CLAUDE: ClassifiedBy
CLASSIFIED_BY_LLM_OLLAMA: ClassifiedBy
CLASSIFIED_BY_KEYWORD: ClassifiedBy

class Design(_message.Message):
    __slots__ = ("id", "name", "summary", "source_url", "repo_owner", "repo_name", "pdk", "circuit_class", "circuit_type", "silicon_proven", "specifications", "tags", "classified_by", "classified_at", "local_path", "readme_excerpt")
    class SpecificationsEntry(_message.Message):
        __slots__ = ("key", "value")
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: str
        value: str
        def __init__(self, key: _Optional[str] = ..., value: _Optional[str] = ...) -> None: ...
    ID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    SUMMARY_FIELD_NUMBER: _ClassVar[int]
    SOURCE_URL_FIELD_NUMBER: _ClassVar[int]
    REPO_OWNER_FIELD_NUMBER: _ClassVar[int]
    REPO_NAME_FIELD_NUMBER: _ClassVar[int]
    PDK_FIELD_NUMBER: _ClassVar[int]
    CIRCUIT_CLASS_FIELD_NUMBER: _ClassVar[int]
    CIRCUIT_TYPE_FIELD_NUMBER: _ClassVar[int]
    SILICON_PROVEN_FIELD_NUMBER: _ClassVar[int]
    SPECIFICATIONS_FIELD_NUMBER: _ClassVar[int]
    TAGS_FIELD_NUMBER: _ClassVar[int]
    CLASSIFIED_BY_FIELD_NUMBER: _ClassVar[int]
    CLASSIFIED_AT_FIELD_NUMBER: _ClassVar[int]
    LOCAL_PATH_FIELD_NUMBER: _ClassVar[int]
    README_EXCERPT_FIELD_NUMBER: _ClassVar[int]
    id: str
    name: str
    summary: str
    source_url: str
    repo_owner: str
    repo_name: str
    pdk: PDK
    circuit_class: CircuitClass
    circuit_type: _containers.RepeatedScalarFieldContainer[str]
    silicon_proven: bool
    specifications: _containers.ScalarMap[str, str]
    tags: _containers.RepeatedScalarFieldContainer[str]
    classified_by: ClassifiedBy
    classified_at: _timestamp_pb2.Timestamp
    local_path: str
    readme_excerpt: str
    def __init__(self, id: _Optional[str] = ..., name: _Optional[str] = ..., summary: _Optional[str] = ..., source_url: _Optional[str] = ..., repo_owner: _Optional[str] = ..., repo_name: _Optional[str] = ..., pdk: _Optional[_Union[PDK, str]] = ..., circuit_class: _Optional[_Union[CircuitClass, str]] = ..., circuit_type: _Optional[_Iterable[str]] = ..., silicon_proven: _Optional[bool] = ..., specifications: _Optional[_Mapping[str, str]] = ..., tags: _Optional[_Iterable[str]] = ..., classified_by: _Optional[_Union[ClassifiedBy, str]] = ..., classified_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., local_path: _Optional[str] = ..., readme_excerpt: _Optional[str] = ...) -> None: ...

class DesignDatabase(_message.Message):
    __slots__ = ("version", "generated_at", "designs")
    VERSION_FIELD_NUMBER: _ClassVar[int]
    GENERATED_AT_FIELD_NUMBER: _ClassVar[int]
    DESIGNS_FIELD_NUMBER: _ClassVar[int]
    version: str
    generated_at: _timestamp_pb2.Timestamp
    designs: _containers.RepeatedCompositeFieldContainer[Design]
    def __init__(self, version: _Optional[str] = ..., generated_at: _Optional[_Union[datetime.datetime, _timestamp_pb2.Timestamp, _Mapping]] = ..., designs: _Optional[_Iterable[_Union[Design, _Mapping]]] = ...) -> None: ...
