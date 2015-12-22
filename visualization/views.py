import folium

from django.shortcuts import render
from django.http import HttpResponse

from .models import OpenCellId


def inline_map(
    m
):
    """Takes a folium instance and embed HTML.
    Parameters
    ----------
    m : <folium instance>
    width : int
    height : int

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
    coordinates = OpenCellId.objects.filter(
        mcc__in=mcc_list
    ).values_list('lat', 'lon')
    return coordinates


def index(request):
    # width, height = 650, 500
    # html = "<html><body>Almost there</body></html>"
    coords = get_coordinates()
    towers = folium.Map(
        location=[30, 31],
        zoom_start=5,
        tiles='OpenStreetMap'
    )
    for loc in coords:
        towers.simple_marker(
            location=loc,
            popup=str(loc)
        )
    html = inline_map(towers)
    return HttpResponse(html)

