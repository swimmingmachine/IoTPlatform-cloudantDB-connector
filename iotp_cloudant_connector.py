import wiotp.sdk.application

myConfig = wiotp.sdk.application.parseConfigFile("application.yaml")
appClient = wiotp.sdk.application.ApplicationClient(config=myConfig, logHandlers=None)

serviceBinding = {
    "name": "Cloudant-frailty",
    "description": "Test Cloudant instance",
    "type": "cloudant",
    "credentials": {
        "host": "your cloudant service host url",
        "port": 443,
        "username": "your cloudant service username",
        "password": "your cloudant service password"
    }
}

cloudantService = appClient.serviceBindings.create(serviceBinding)

# Create the connector
connector = appClient.dsc.create(
    name="connector1", type="cloudant", serviceId=cloudantService.id, timezone="UTC",
    description="A iot cloudant connector", enabled=True
)

# Create a destination under the connector
destination1 = connector.destinations.create(name="all-data", bucketInterval="DAY")

# Create a rule under the connector, that routes all events to the destination
rule1 = connector.rules.createEventRule(
    name="allevents", destinationName=destination1.name, typeId="*", eventId="*",
    description="Send all events", enabled=True
)
# Create a second rule under the connector, that routes all state to the same destination
rule2 = connector.rules.createStateRule(
    name="allstate", destinationName=destination1.name, logicalInterfaceId="*",
    description="Send all state", enabled=True,
)