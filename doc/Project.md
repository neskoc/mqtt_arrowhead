# Assignment

## General information

- Results shall be presented on Dec15, lecture 13-17 or Jan 7 lecture hours still TBD.
- Max 15 minutes for presentation and demonstration of results
- Presentation and demo shall include:

  - SoSD documentation
  - SysDdocumentation
  - SD documentation
  - IDD documentation
  - Working code demo
  - SysML models if applicable

# Assignment submissions

- SoSD document
- SysD document
- IDD document(s), one foreach service produced
- SD document(s), one foreach service produced
- Code,source,uploaded to Github
- SysML model if applicable

# Documentation structure

Arrowhead consortium [20] has defined a three-level documentation structure: System of Systems, System, and Service level.

The main concept of the documentation structure is to provide abstract and implementation views of the Systems of Systems, systems, and services. The main purpose of the abstract view documents is to allow any developer to implement System of Systems, systems and services, based on these documents. This further support that the resulting implementation becomes Arrowhead Framework compliant.

## Abbreviations

- **SoSD**: The System of Systems Description, showos an abstract view of an SoS
- **SoSDD**: The System of Systems Design Description, shows an implementation view of the SoS with its technologies and deployment views
- **SysD**: black box System Description
- **SysDD**: white box System Description
- **SD**: the Service Description,
- **IDD**: the Interface Design Description,
- **CP**: the Communication Profile, and
- **SP**: the Semantic Profile

## System of Systems level documentation

The System of Systems level consists of two types of documents. The System of Systems Description (SoSD), which shows an abstract view of an SoS, and the System of Systems Design Description (SoSDD), which shows an implementation view of the SoS with its technologies and deployment views.

### SoSD

The SoSD describes the main functionalities and the generic architecture of the SoS. It will mainly be used to describe one System of Systems in an abstract way, without instantiating into any specific technologies. Examples of its usage are the description of generic SOA-based installations, like building automation systems or a factory automation system. The document should present its main building blocks as independent systems with pointers to their specific abstract view documents, the system Descriptions (SysDs).

Also, diagrams representing system behaviour, like use-case diagrams and behaviour diagrams (e.g., using UML, BPMN, SysML, AutomationML [21, 22, 23, 24]) must be included. This document also includes information about non-functional requirements, like required levels of QoS and security. For the Arrowhead Framework itself there is a generic SoSD for which the current version can be found at the Arrowhead Framework wiki [25].

### SoSDD

The SoSDD document describes how an SoSD has been implemented on a specific scenario, showing the technologies used and its setup. Therefore, it points out all necessary black box SysD and white box SysDD documents, describing the systems used in this realisation. The SoSDD should also contain behaviour diagrams which clearly identify the technologies used and the setup of this SoS realisation. The document can optionally include a description of its physical implementation and the non-functional requirements implemented by this realisation.

## System level documentation

System level documentation consists of a black box System Description (SysD) document and a white box System Design Description (SysDD) document.

### SysD

The SysD describes the system as a black box, documenting the system functionality and its hosted services and their provided and required interfaces with the corresponding technical solutions, without describing its internal im- plementation. The by the system provided service interfaces are referenced and defined in the Interface Design Description (IDD) document; see Section 3.3.3 below. The services provided are defined in the Service Design (SD) document, see Section 3.3.3 below. The SD document shall provide a clear definition of how to interface the system, thus enabling coding of a consumer system.

### SysDD

The SysDD extends the black box description, showing its internal details. This document is optional, since it might expose knowledge of the company which implemented the system, but it can be used as an internal document for future reference by the system owner.

## Service level documentation

Service level documentation consists of four documents: the Service Description (SD), the Interface Design Description (IDD), the Communication Profile (CP), and the Semantic Profile (SP).

### SD

The SD is a technology independent and abstract view of a service. The document describes the main objectives and functionalities of the service and its abstract interfaces. Further, an abstract information model shall be provided. Sequence Diagrams showing how the service is interacted with, shall also be provided.

### IDD

The IDD is pointed to by a SysD document. It states the actual implemented solution of a system. Here are defined the service identifiers of the specific service implementations. For the SOA protocol and encoding used the IDD is making reference to the Communication Profile (CP) document. For data and information semantics the IDD make reference to the Semantics Profile (SP) document.

### CP

The CP contains all the information regarding the transfer protocol, data compression, data encryption, and data encoding used, e.g., CoAP, UDP, EXI, DTLS, and XML.

### SP

The SP defines the data and information semantics used, e.g., SenML.
