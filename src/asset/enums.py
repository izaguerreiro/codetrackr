from enum import Enum
from .helpers import EnumDatabaseMixin


class LicenceType(str, EnumDatabaseMixin, Enum):
    COMERCIAL = "licença comercial"
    OPEN_SOURCE = "licença de código aberto"
    TRIAL = "licença de avaliação"


class AssetStatus(str, EnumDatabaseMixin, Enum):
    ACTIVE = "Ativo"
    INACTIVE = "Inativo"
    OPERATION = "Em operação"
    OUT_OF_USE = "Fora de uso"
    EXPIRED = "Expirado"


class SupplierStatus(str, EnumDatabaseMixin, Enum):
    ACTIVE = "Ativo"
    REVIEW = "Em avaliação"
    CLOSED = "Encerrado"
    NEGOCIATION = "Em negociação"
