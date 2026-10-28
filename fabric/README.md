# Hyperledger Fabric Chaincode

This directory contains the smart contracts (chaincode) for the hospital blockchain network.

## Chaincode Structure

- `hospitalrecords`: Main chaincode for managing patient records on the blockchain

## Deployment

Chaincode will be deployed to the Fabric network during the setup process.

## Functions

### AddPatientRecord
Adds a new patient record to the blockchain.

**Parameters:**
- patientId: Patient identifier
- hospitalName: Name of the hospital
- department: Department name
- diagnosis: Patient diagnosis
- treatment: Treatment provided
- doctor: Attending doctor name

### GetPatientRecord
Retrieves a patient record from the blockchain.

**Parameters:**
- patientId: Patient identifier

### UpdatePatientRecord
Updates an existing patient record on the blockchain.

### GetPatientHistory
Retrieves the complete history of changes for a patient record.
