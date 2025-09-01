# similar to switch case 

def http_status(status):
    match status:
        case 200:
            return "Ok"
        case 404:
            return "Not found"
        case 500:
            return "Internal Server Error"
        case _:
            return "unknown Status"
print(http_status(200))
print(http_status(404))
print(http_status(500))
print(http_status("_"))
    