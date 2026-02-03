import enum


class DermatologistStatus(str, enum.Enum):
    pending = "pending"
    approved = "approved"
    rejected = "rejected"