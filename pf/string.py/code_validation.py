batch_code = "bLD-1234-A-HSP"
batch_code = batch_code.upper()
startwith_BLD = batch_code.startswith("BLD-")
endswith_HSP = batch_code.endswith("-HSP")
if startwith_BLD and endswith_HSP:
    print("Valid batch code")
else:
    print("Invalid batch code")