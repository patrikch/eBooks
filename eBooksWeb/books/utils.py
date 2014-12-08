def nakrm(file):
    with open(file,mode="r") as f:
        for ln in f:
            if len(ln.strip()) > 0:
                arr = ln.strip().split(";")
                loc = models.Location.objects.get(id=int(arr[7]))
                key = models.Key.objects.get(id=int(arr[6]))
                b = models.Book(ebookfilename=arr[0],name=arr[1],authors=arr[2],publisher=arr[3],
                                format=arr[4],pubYear=int(arr[5]),location=loc)
                b.save()
