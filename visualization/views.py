import folium

from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.gis.geos import Point, GeometryCollection

from .models import OpenCellId, GADM


# NOTE : we stick with the 4326 standard i.e (lat/lon) - inverse of google map coords- for creating geometries.

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
        b_line = [i[::-1] for i in b_line]
        towers.line(b_line, line_color='green', line_weight=5)

    for loc in coords:
        towers.circle_marker(
            location=loc[::-1],
            fill_color='orange',
            line_color='orange'
            # popup=str(loc)
        )
    elqasr = (28.830439, 25.579540)
    p = Point(elqasr, srid=4326)
    towers.simple_marker(
        location=p[::-1],
        popup='elqasr %s' % str(elqasr)
    )
    # import ipdb; ipdb.set_trace()
    # p.transform(900913)
    # test_p = p.buffer(220000)
    # test_p.transform(4326)
    # import ipdb; ipdb.set_trace()
    # for b in test_p:
    #     b = [i[::-1] for i in b]
    #     towers.line(
    #         b,
    #         line_color='blue',
    #     )
    html = inline_map(towers)
    return HttpResponse(html)


def create_coverage_area():
    ocid_list = OpenCellId.objects.all().values_list(
        'lon',
        'lat',
        'range'
    )
    coverage_collection = []
    for ocid in ocid_list:
        lon, lat, range_ = ocid
        p = Point(lat, lon, srid=4326)
        p.transform(900913)
        buffer_width = range_ if range_ > 0 else 10000
        buffered = p.buffer(buffer_width)
        buffered.transform(4326)
        coverage_collection.append(buffered)

    return coverage_collection


def is_covered(
    point=(0, 0),
    country_name='Egypt'
):
    """Tells if the point is covered by the signal. Finds the points which their distance to the
    lookup_point is less than or equal to their coverage (range).

    Parameters
    ----------
    point : (float, float)
        the format is in (lat, lon)
    country_name : str

    Returns
    -------
    status : bool
    """

    if not GADM.is_valid_point(country_name, point):
        print 'point=%s is not a valid point in %s' %(point, country_name)
        return False

    lookup_point = Point(*point, srid=4326)
    country_geom = GADM.objects.get(name_engli__iexact=country_name).geom
    if OpenCellId.objects.filter(coord__within=country_geom).extra(
        where=['ST_Distance_Sphere(coord, ST_PointFromText(%s, 4326)) <= range'],
        params=[lookup_point.wkt]
    ).exists():
        print 'point=%s is covered in %s.' %(point, country_name)
    else:
        print 'point=%s is not covered in %s' %(point, country_name)


# remember to add country filter : look in the points which are within country borders
# OpenCellId.objects.all().extra(
#         where=['ST_Distance_Sphere(coord, ST_PointFromText(%s, 4326)) < range'],
#         params=[p_cairo.wkt]
# ).count()

