import json
from django.contrib.gis.geos import Point
from dajaxice.decorators import dajaxice_register

from visualization.models import GADM, OpenCellId


@dajaxice_register
def is_covered(
    request,
    lat,
    lon,
    country_name='Egypt'
):
    """Tells if the point is covered by the signal. Finds the points which their distance to the
    lookup_point is less than or equal to their coverage (range).

    Parameters
    ----------
    request : <Requset>
    lat : float
    lon : float
    country_name : str

    Returns
    -------
    result_str : str
    """
    result_str = None
    point = (lat, lon)
    if not GADM.is_valid_point(country_name, point):
        result_str = 'point=%s is not a valid point in %s' %(point, country_name)
    else:
        lookup_point = Point(*point, srid=4326)
        country_geom = GADM.objects.get(name_engli__iexact=country_name).geom
        if OpenCellId.objects.filter(coord__within=country_geom).extra(
            select={
                'coord': 'coord',
                'range': 'CASE WHEN range > 0 THEN range ELSE 10000 END'
            },
            where=['ST_Distance_Sphere(coord, ST_PointFromText(%s, 4326)) <= range'],
            params=[lookup_point.wkt]
        ).exists():
            result_str = 'point=%s is covered in %s.' %(point, country_name)
        else:
            result_str = 'point=%s is not covered in %s' %(point, country_name)

    return json.dumps({"status": result_str})