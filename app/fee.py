def process_fees(fees):
    """Process raw fees from the data into displayable strings."""
    result = []
    for fee in fees:
        fee_description = ""
        if "percentage" in fee:
            percentage = fee["percentage"]
            if not percentage:
                continue
            if "$" in percentage or "?" in percentage:
                fee_description = percentage
            else:
                fee_description = "{}%".format(percentage)
        if "name" in fee:
            fee_description = fee["name"] + " - " + fee_description
        result.append(fee_description)
    return result
