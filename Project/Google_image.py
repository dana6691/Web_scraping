## Image download 
## To save it: right click on downlods folder > Reveals in Explorer
from google_images_download import google_images_download

response = google_images_download.googleimagesdownload()
arguments = {"keywords":"shrimp, crab", "limit":20, "print_urls":True, "format":"png"}
paths = response.download(arguments) #passing arguments to the function
print(paths)