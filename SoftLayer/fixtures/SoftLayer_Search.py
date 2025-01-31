advancedSearch = [
    {
        "relevanceScore": "4",
        "resourceType": "SoftLayer_Hardware",
        "resource": {
            "accountId": 307608,
            "domain": "vmware.test.com",
            "fullyQualifiedDomainName": "host14.vmware.test.com",
            "hardwareStatusId": 5,
            "hostname": "host14",
            "id": 123456,
            "manufacturerSerialNumber": "AAAAAAAAA",
            "notes": "A test notes",
            "provisionDate": "2018-08-24T12:32:10-06:00",
            "serialNumber": "SL12345678",
            "serviceProviderId": 1,
            "hardwareStatus": {
                "id": 5,
                "status": "ACTIVE"
            }
        }
    }
]

search = advancedSearch

getObjectTypes = [{"name": "SoftLayer_Event_Log",
                   "properties": [
                       {
                           "name": "accountId",
                           "sortableFlag": True,
                           "type": "integer"
                       }]},
                  {"name": "SoftLayer_Hardware",
                   "properties": [
                       {
                           "name": "accountId",
                           "sortableFlag": True,
                           "type": "integer"
                       },
                       {
                           "name": "datacenter.longName",
                           "sortableFlag": True,
                           "type": "string"
                       },
                       {
                           "name": "deviceStatus.name",
                           "sortableFlag": True,
                           "type": "string"
                       }]
                   }]
