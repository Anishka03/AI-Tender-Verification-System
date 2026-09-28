from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(String(30), default="bidder")


class Tender(Base):
    __tablename__ = "tenders"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text)
    tender_number = Column(String(100))
    deadline = Column(String(100))
    file_path = Column(String(500))
    created_at = Column(DateTime, server_default=func.now())


class Requirement(Base):
    __tablename__ = "requirements"

    id = Column(Integer, primary_key=True, index=True)
    tender_id = Column(Integer, ForeignKey("tenders.id"))
    requirement_type = Column(String(100))
    requirement_text = Column(Text)
    required_value = Column(String(255))


class Bidder(Base):
    __tablename__ = "bidders"

    id = Column(Integer, primary_key=True, index=True)
    tender_id = Column(Integer, ForeignKey("tenders.id"))
    name = Column(String(255))
    company_name = Column(String(255))
    email = Column(String(150))


class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    bidder_id = Column(Integer, ForeignKey("bidders.id"))
    document_type = Column(String(100))
    file_path = Column(String(500))
    extracted_text = Column(Text)


class Verification(Base):
    __tablename__ = "verifications"

    id = Column(Integer, primary_key=True, index=True)
    bidder_id = Column(Integer, ForeignKey("bidders.id"))
    requirement_id = Column(Integer, ForeignKey("requirements.id"))
    status = Column(String(50))
    remarks = Column(Text)
    evidence = Column(Text)