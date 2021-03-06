import folium

from django.shortcuts import render

from .models import OpenCellId, GADM, GADM1, GADM2


# NOTE : we stick with the 4326 standard i.e (lat/lon) - which is inverse of google map coords- for creating geometries.

def inline_map(
    m
):
    """Takes a folium.Map instance and embed HTML.
    Parameters
    ----------
    m : <folium.Map>

    Returns
    -------
    embed : str
    """
    m._build_map()
    srcdoc = m.HTML.replace('"', '&quot;')
    embed = """
        <iframe srcdoc="{}"
        style="position:fixed; top:0px; left:0px; bottom:0px; right:0px; width:100%; height:100%; border:none;
        margin:0; padding:0; overflow:hidden; z-index:2;";
         ></iframe>
     """.format(srcdoc)
    return embed


def get_coordinates(
    mcc_list=[240]
):
    """Returns lat/lon of the country of matching mcc_list
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
    context_dict = {}
    coords = get_coordinates()
    boundary = GADM.objects.filter(name_engli__iexact='Sweden')[0].geom.boundary
    towers = folium.Map(
        location=boundary.centroid[::-1],
        zoom_start=4,
        # tiles='OpenStreetMap'
        tiles='Mapbox Bright'
    )
    # for b_line in boundary:
    #     b_line = [i[::-1] for i in b_line]
    #     towers.line(b_line, line_color='green', line_weight=5)
    #
    # adm1_boundaries = []
    # for adm1 in GADM1.objects.filter(name_0__iexact='Sweden'):
    #     adm1_boundaries.append(adm1.geom.boundary)
    # for boundary in adm1_boundaries:
    #     for b_line in boundary:
    #         b_line = [i[::-1] for i in b_line]
    #     towers.line(b_line, line_color='blue', line_weight=1)
    coords = [(y, x) for x, y in coords]
    for loc in coords:
        towers.circle_marker(
            location=loc,
            fill_color='orange',
            line_color='orange'
        )

    map_html = inline_map(towers)
    context_dict['map_html'] = map_html
    return render(request, 'visualization/index.html', context_dict)