from django.db.models import Prefetch
from django.shortcuts import render

from . import models

# Create your views here.


# inefficient way to fetch
# def home(request):
#     car_models = models.CarModel.objects.all()  # 100 data
#     car_details = []
#     for car in car_models:  # 100 query
#         car_details.append(
#             {
#                 "car_name": car.name,
#                 "car_company": car.car_company.name,
#                 "ceo_name": models.Ceo.objects.filter(car_company=car.car_company)
#                 .first()
#                 .name,
#                 "fuel_names": [
#                     fuel.name for fuel in models.FuelType.objects.filter(car_models=car)
#                 ],
#             }
#         )

#         # total query number =  1 + 3N = ( N+1 )
#     return render(request, "cars/home.html", {"car_details": car_details})


# efficient way


def home(request):
    car_models = models.CarModel.objects.select_related(
        "car_company__ceo"
    ).prefetch_related(Prefetch("fueltype_set"))

    # select related(one to one, many to one)
    # prefetch related (many to many)

    car_details = []
    for car in car_models:
        car_details.append(
            {
                "car_name": car.name,
                "car_company": car.car_company.name,
                "ceo_name": car.car_company.ceo.name,
                "fuel_names": [
                    fuel.name for fuel in models.FuelType.objects.filter(car_models=car)
                ],
            }
        )

    return render(request, "cars/home.html", {"car_details": car_details})
