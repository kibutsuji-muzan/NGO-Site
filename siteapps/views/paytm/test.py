
from django.shortcuts import render
import json
from paytmchecksum import PaytmChecksum


def testview(request):


  paytmParams = dict()

  paytmParams["body"] = {
      "requestType"   : "Payment",
      "mid"           : "vOEvzH72354081858751",
      "websiteName"   : "localhost:8000",
      "orderId"       : "1",
      "callbackUrl"   : "",
      "txnAmount"     : {
          "value"     : "1.00",
          "currency"  : "INR",
      },
      "userInfo"      : {
          "custId"    : "CUST_001",
      },
  }

  # Generate checksum by parameters we have in body
  # Find your Merchant Key in your Paytm Dashboard at https://dashboard.paytm.com/next/apikeys 
  checksum = PaytmChecksum.generateSignature(json.dumps(paytmParams["body"]), "YOUR_MERCHANT_KEY")

  paytmParams["head"] = {
      "signature"    : checksum
  }

  post_data = json.dumps(paytmParams)

  # for Staging
  url = "https://securegw-stage.paytm.in/theia/api/v1/initiateTransaction?mid=vOEvzH72354081858751&orderId=1"

  # for Production
  # url = "https://securegw.paytm.in/theia/api/v1/initiateTransaction?mid=YOUR_MID_HERE&orderId=ORDERID_98765"
  response = request.post(url, data = post_data, headers = {"Content-type": "application/json"}).json()
  print(response)
  return render(request, 'payment/payment.html')