from enum import StrEnum


class DeliveryStates(StrEnum):
    DELIVERED = 'CONSEGNATO'
    PENDING = 'IN CONSEGNA'
    DELAYED = 'IN RITARDO'
