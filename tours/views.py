from django.shortcuts import render
from django.views import View

import random
import data

departures = data.departures
tours = data.tours
title = data.title
subtitle = data.subtitle
description = data.description


class MainView(View):
    template_name = 'index.html'

    def get(self, request):
        rand_tours = random.sample(list(tours.keys()), 6)
        dict_rand_tours = {tour_id: tours[tour_id] for tour_id in rand_tours}
        return render(
            request, self.template_name, context={
                'tours': dict_rand_tours,
                'departures': departures,
                'description': description,
                'subtitle': subtitle,
            }
        )


class DepartureView(View):
    template_name = 'departure.html'

    def get(self, request, departure):
        dict_dep = {}
        dep_property = {}
        price = []
        nights = []
        for key, value in tours.items():
            if value['departure'] == departure:
                dict_dep.update({key: value})
                price.append(value['price'])
                nights.append(value['nights'])
        dep_property.update(minprice=min(price))
        dep_property.update(maxprice=max(price))
        dep_property.update(minnights=min(nights))
        dep_property.update(maxnights=max(nights))
        dep_property.update(dep=departures[departure][3:])
        return render(request, self.template_name, context={
                'departures': departures,
                'selected_departure': dict_dep,
                'dep_property': dep_property,
            }
        )


class TourView(View):
    template_name = 'tour.html'

    def get(self, request, tour):
        return render(
            request, self.template_name, context={
                'departures': departures,
                'tour': tours[tour],
            }
        )
