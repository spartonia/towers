import folium

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.gis.geos import Point

from .models import OpenCellId, GADM


def inline_map(
    m
):
    """Takes a folium instance and embed HTML.
    Parameters
    ----------
    m : <folium instance>

    Returns
    -------
    embed : str
    """
    m._build_map()
    srcdoc = m.HTML.replace('"', '&quot;')
    embed = """
        <iframe srcdoc="{}"
        style="position:fixed; top:0px; left:0px; bottom:0px; right:0px; width:100%; height:100%; border:none;
        margin:0; padding:0; overflow:hidden; z-index:999999;";
         ></iframe>
     """.format(srcdoc)
    return embed


def get_coordinates(
    mcc_list=[602]
):
    """Returns lon/lat of matching mcc_list
    Parameters
    ----------
    mcc_list : [int]

    Returns
    -------
    coordinates : [(float, float)]
    """
    try:
        coordinates = OpenCellId.objects.filter(
            mcc__in=mcc_list
        ).values_list('lon', 'lat')
    except:
        coordinates = []
    return coordinates


def index(request):
    coords = get_coordinates()
    boundry = GADM.objects.all()[0].geom.boundary
    towers = folium.Map(
        location=boundry.centroid[::-1],
        # location=[30, 31],
        zoom_start=5,
        # tiles='OpenStreetMap'
        tiles='Mapbox Bright'
    )
    for b_line in boundry:
        b_line = [(i[1], i[0]) for i in b_line]
        towers.line(b_line, line_color='green', line_weight=5)

    for loc in coords:
        towers.circle_marker(
            location=loc[::-1],
            fill_color='orange',
            line_color='orange'
            # popup=str(loc)
        )

    test_p = Point(27.674483, 27.217795).buffer(100)
    # import ipdb; ipdb.set_trace()
    for b in test_p:
        towers.circle_marker(
            location=b[::-1],
            fill_color='blue'
        )
    html = inline_map(towers)
    return HttpResponse(html)


def is_covered(
    point=(0,0)
):
    """

    :param point:
    :return:
    """
    # find the points which their distance to the base point is less than or
    # equal to their coverage (range); then rank in distance decs.
    pass