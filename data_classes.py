from dataclasses import dataclass, field
import datetime

# Exercise
# Part I: Create Data Classes
# Create data classes for:
# Orders
# Invoices
# Customers


# Part II: Override Operators
# We want to compare orders to other orders. Override the comparison operators for > and >=.

@dataclass
class Orders:
    orderID: int
    customerID: int
    salepersonPersonID: int
    pickedByPersonID: int
    contactPersonID: int
    backorderOrderID: int
    orderDate: datetime.date
    ExpectedDeliveryDate: datetime.date
    customerPurchaseOrderNumber: str
    isUnderSupplyBackordered: bool
    comments: str
    deliveryInstructions: str
    internalComments: str
    pickingCompletedWhen: datetime.datetime
    lastEditedBy: int
    lastEditedWhen: datetime.datetime

# Part II: Override Operators
# We also want to compare invoices to other invoices. Override the comparison operators as well.
@dataclass
class Invoices:
    invoiceID: int
    customerID: int
    billToCustomerID: int
    orderID: int
    deliveryMethodID: int
    contactPersonID: int
    accountsPersonID: int
    salespersonPersonID: int
    packedByPersonID: int
    invoiceDate: datetime.datetime
    customerPurchaseOrderNumber: str
    isCreditNote: bool
    creditNoteReason: str
    comments: str
    deliveryInstructions: str
    internalComments: str
    totalDryItems: int
    totalChillerItems: int
    deliveryRun: str
    runPosition: str
    returnedDeliveryData: str
    confirmedDeliveryTime: datetime.datetime
    confirmedReceivedBy: str
    lastEditedBy: int
    lastEditedWhen: datetime.datetime

@dataclass
class Customers:
    customerID: int
    customerName: str
    billToCustomerID: int
    customerCategoryID: int
    buyingGroupID: int
    primaryContactPersonID: int
    alternateContactPersonID: int
    deliveryMethodID: int
    deliveryCityID: int
    postalCityID: int
    creditLimit: float
    accountOpenedDate: datetime.date
    standardDiscountPercentage: float
    isStatementSent: bool
    isOnCreditHold: bool
    paymentDays: int
    phoneNumber: str
    faxNumber: str
    deliveryRun: str
    runPosition: str
    websiteURL: str
    deliveryAddressLine1: str
    deliveryAddressLine2: str
    deliveryPostalCode: str
    deliveryLocation: str
    postalAddressLine1: str
    postalAddressLine2: str
    postalPostalCode: str
    lastEditedBy: int
    validFrom: datetime.datetime
    validTo: datetime.datetime
