from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # Database
    database_url: str = "postgresql://user:password@localhost:5432/hospital_blockchain"
    db_user: str = "user"
    db_password: str = "password"
    db_host: str = "localhost"
    db_port: int = 5432
    db_name: str = "hospital_blockchain"
    
    # JWT
    secret_key: str = "your-super-secret-key-change-this-in-production"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30
    
    # Hyperledger Fabric
    fabric_org_name: str = "org1"
    fabric_peer_url: str = "grpc://localhost:7051"
    fabric_orderer_url: str = "grpc://localhost:7050"
    fabric_channel_name: str = "hospitalchannel"
    fabric_chaincode_name: str = "hospitalrecords"
    
    # API
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    debug: bool = False
    
    class Config:
        env_file = ".env"
        case_sensitive = False

settings = Settings()
