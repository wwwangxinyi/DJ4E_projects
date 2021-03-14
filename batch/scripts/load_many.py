import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from unesco.models import Site, Category, Region, Iso, State



def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Category.objects.all().delete()
    Region.objects.all().delete()
    Iso.objects.all().delete()
    State.objects.all().delete()
    Site.objects.all().delete()

    # name,description,justification,year,longitude,latitude,
    # area_hectares,category,state,region,iso
    for row in reader:
        print(row)

        try:
            y = int(row[3])
        except:
            y = None

        try:
            lo = float(row[4])
        except:
            lo = None

        try:
            la = float(row[5])
        except:
            la = None
        
        try:
            ar = float(row[6])
        except:
            ar = None

        c, created = Category.objects.get_or_create(name=row[7])
        s, created = State.objects.get_or_create(name=row[8])
        r, created = Region.objects.get_or_create(name=row[9])
        i, created = Iso.objects.get_or_create(name=row[10])

        site = Site(name=row[0],description=row[1],justification=row[2],longitude=lo,latitude=la,area_hectares=ar,year=y,category=c,region=r,state=s,iso=i)
        site.save()