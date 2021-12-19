import wiotp.sdk.application

#options = wiotp.sdk.application.parseEnvVars()
myConfig = wiotp.sdk.application.parseConfigFile("application.yaml")

appClient = wiotp.sdk.application.ApplicationClient(myConfig)

# Iterate through all service bindings
for s in appClient.serviceBindings:
    print(s.name)
    print(" - " + s.description)
    print(" - " + s.type)
    print()

print()

# Iterate through service bindings of type "cloudant"
for s in appClient.serviceBindings.find(typeFilter="cloudant"):
    print(s.name)
    print(" - " + s.description)
    print(" - " + s.type)
    print()