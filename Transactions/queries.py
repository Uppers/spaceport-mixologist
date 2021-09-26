import json
import sys
# requires Python SDK version 1.3 or higher
from algosdk.v2client import indexer
from algosdk.error import IndexerHTTPError


class Queries():
    def __init__(self):
        self.myindexer = indexer.IndexerClient(indexer_token="", indexer_address="http://localhost:8980")

    def account_exists(self, account_pk):
        # queries the indexer and returns True if the account exists
        try:
            response = self.myindexer.search_transactions_by_address(account_pk)
        except IndexerHTTPError:
            return False
        return True

    #def account_opted_in(self, account_pk, asset_id):
    #    # checks to see if account has made any transactions in a given asset
    #    try:
    #        response = self.myindexer.search_transactions_by_address(account_pk, asset_id)
    #    except:
    #        return None
    #    if len(response['transactions'])==0:
    #        return False
    #    else:
    #        True


   



"""
ac1 = "5KLSI3AHMBBDALXBEO2HEA3PBBCBAYT4PIHCD3B25557WGWUZGRTQETPHQ"
ac2 = "NTMTJYBQHWUXEGVG3XRRX5CH6FCYJ3HKCSIOYW4DLAOF6V2WHSIIFMWMPY"

query = Queries()
#opted_in_response = query.myindexer.search_transactions_by_address("5KLSI3AHMBBDALXBEO2HEA3PBBCBAYT4PIHCD3B25557WGWUZGRTQETPHQ", 23)
#print(len(opted_in_response["transactions"]))
response = query.myindexer.transaction("EUSA7ASCEHH5K4G3IM3RR5PZX2BSUYMLTRQ4P5KDE2H2T7RXTEPQ")
print(response)
print()
print()
print()
"""

#not_in_response = query.myindexer.search_transactions_by_address("NTMTJYBQHWUXEGVG3XRRX5CH6FCYJ3HKCSIOYW4DLAOF6V2WHSIIFMWMPY", 23)
#print(len(not_in_response["transactions"]))

#a = query.account_opted_in("NTMTJYBQHWUXEGVG3XRRX5CH6FCYJ3HKCSIOYW4DLAOF6V2WHSIIFMWMPY", 23)
#print(a)

#response = myindexer.search_transactions(asset_id=22) 
#response = myindexer.accounts()
#try:
#    response = myindexer.search_transactions_by_address("I3CMDHG236HVBDMCKEM22DLY5L2OJ3CBRUDHG4PVVFGEZ4QQR3X3KNHRMU", asset_id=22)
#except IndexerHTTPError:
#    print("This address does not exist")
#if not len(response['transactions']):
#    print("This account has not opted in")

