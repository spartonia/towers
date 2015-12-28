from django.contrib.gis.db import models
from django.contrib.gis.geos import Point


class OpenCellId(models.Model):
    radio = models.CharField(
        max_length=10
    )
    mcc = models.IntegerField()
    net = models.IntegerField()
    area = models.IntegerField()
    cell = models.IntegerField()
    unit = models.IntegerField(
        null=True
    )
    lon = models.FloatField()
    lat = models.FloatField()
    range = models.IntegerField()
    samples = models.IntegerField()
    changeable = models.IntegerField()
    created = models.IntegerField()
    updated = models.IntegerField()
    averageSignal = models.IntegerField()
    coord = models.PointField(null=True)
    objects = models.GeoManager()

    def save(
        self,
        *args,
        **kwargs
    ):
        self.coord = Point(self.lat, self.lon, srid=4326)
        # p.transform(900913)
        # buffer_width = self.range if self.range > 0 else 10000
        # buffered = p.buffer(buffer_width)
        # buffered.transform(4326)
        # self.coverage_geom.append(buffered)
        super(OpenCellId, self).save(*args, **kwargs)


# This is an auto-generated Django model module created by ogrinspect.
class GADM(models.Model):
    id_0 = models.IntegerField()
    iso = models.CharField(max_length=3)
    name_engli = models.CharField(max_length=50)
    name_iso = models.CharField(max_length=54)
    name_fao = models.CharField(max_length=50)
    name_local = models.CharField(max_length=54)
    name_obsol = models.CharField(max_length=150)
    name_varia = models.CharField(max_length=160)
    name_nonla = models.CharField(max_length=50)
    name_frenc = models.CharField(max_length=50)
    name_spani = models.CharField(max_length=50)
    name_russi = models.CharField(max_length=50)
    name_arabi = models.CharField(max_length=50)
    name_chine = models.CharField(max_length=50)
    waspartof = models.CharField(max_length=100)
    contains = models.CharField(max_length=50)
    sovereign = models.CharField(max_length=40)
    iso2 = models.CharField(max_length=4)
    www = models.CharField(max_length=2)
    fips = models.CharField(max_length=6)
    ison = models.FloatField()
    validfr = models.CharField(max_length=12)
    validto = models.CharField(max_length=10)
    pop2000 = models.FloatField()
    sqkm = models.FloatField()
    popsqkm = models.FloatField()
    unregion1 = models.CharField(max_length=254)
    unregion2 = models.CharField(max_length=254)
    developing = models.FloatField()
    cis = models.FloatField()
    transition = models.FloatField()
    oecd = models.FloatField()
    wbregion = models.CharField(max_length=254)
    wbincome = models.CharField(max_length=254)
    wbdebt = models.CharField(max_length=254)
    wbother = models.CharField(max_length=254)
    ceeac = models.FloatField()
    cemac = models.FloatField()
    ceplg = models.FloatField()
    comesa = models.FloatField()
    eac = models.FloatField()
    ecowas = models.FloatField()
    igad = models.FloatField()
    ioc = models.FloatField()
    mru = models.FloatField()
    sacu = models.FloatField()
    uemoa = models.FloatField()
    uma = models.FloatField()
    palop = models.FloatField()
    parta = models.FloatField()
    cacm = models.FloatField()
    eurasec = models.FloatField()
    agadir = models.FloatField()
    saarc = models.FloatField()
    asean = models.FloatField()
    nafta = models.FloatField()
    gcc = models.FloatField()
    csn = models.FloatField()
    caricom = models.FloatField()
    eu = models.FloatField()
    can = models.FloatField()
    acp = models.FloatField()
    landlocked = models.FloatField()
    aosis = models.FloatField()
    sids = models.FloatField()
    islands = models.FloatField()
    ldc = models.FloatField()
    geom = models.MultiPolygonField(srid=4326, null=True)
    objects = models.GeoManager()

    @staticmethod
    def is_valid_point(
        country_name,
        point,
        margin_km=50
    ):
        """
        Checks if the point is within county's borders with margin of 'margin_km' kilometers from its borders.

        Parameters
        ----------
        country_name : str
        point : tuple
        margin_km : int

        Returns
        -------
        status : bool
        """
        pnt = Point(*point, srid=4326)
        country = GADM.objects.filter(name_engli__iexact=country_name)
        if not country:
            return False
        if country.distance(pnt).get(name_engli__iexact=country_name).distance.km < margin_km:
            return True
        return False


# Auto-generated `LayerMapping` dictionary for GADM model
gadm_mapping = {
    'id_0' : 'ID_0',
    'iso' : 'ISO',
    'name_engli' : 'NAME_ENGLI',
    'name_iso' : 'NAME_ISO',
    'name_fao' : 'NAME_FAO',
    'name_local' : 'NAME_LOCAL',
    'name_obsol' : 'NAME_OBSOL',
    'name_varia' : 'NAME_VARIA',
    'name_nonla' : 'NAME_NONLA',
    'name_frenc' : 'NAME_FRENC',
    'name_spani' : 'NAME_SPANI',
    'name_russi' : 'NAME_RUSSI',
    'name_arabi' : 'NAME_ARABI',
    'name_chine' : 'NAME_CHINE',
    'waspartof' : 'WASPARTOF',
    'contains' : 'CONTAINS',
    'sovereign' : 'SOVEREIGN',
    'iso2' : 'ISO2',
    'www' : 'WWW',
    'fips' : 'FIPS',
    'ison' : 'ISON',
    'validfr' : 'VALIDFR',
    'validto' : 'VALIDTO',
    'pop2000' : 'POP2000',
    'sqkm' : 'SQKM',
    'popsqkm' : 'POPSQKM',
    'unregion1' : 'UNREGION1',
    'unregion2' : 'UNREGION2',
    'developing' : 'DEVELOPING',
    'cis' : 'CIS',
    'transition' : 'Transition',
    'oecd' : 'OECD',
    'wbregion' : 'WBREGION',
    'wbincome' : 'WBINCOME',
    'wbdebt' : 'WBDEBT',
    'wbother' : 'WBOTHER',
    'ceeac' : 'CEEAC',
    'cemac' : 'CEMAC',
    'ceplg' : 'CEPLG',
    'comesa' : 'COMESA',
    'eac' : 'EAC',
    'ecowas' : 'ECOWAS',
    'igad' : 'IGAD',
    'ioc' : 'IOC',
    'mru' : 'MRU',
    'sacu' : 'SACU',
    'uemoa' : 'UEMOA',
    'uma' : 'UMA',
    'palop' : 'PALOP',
    'parta' : 'PARTA',
    'cacm' : 'CACM',
    'eurasec' : 'EurAsEC',
    'agadir' : 'Agadir',
    'saarc' : 'SAARC',
    'asean' : 'ASEAN',
    'nafta' : 'NAFTA',
    'gcc' : 'GCC',
    'csn' : 'CSN',
    'caricom' : 'CARICOM',
    'eu' : 'EU',
    'can' : 'CAN',
    'acp' : 'ACP',
    'landlocked' : 'Landlocked',
    'aosis' : 'AOSIS',
    'sids' : 'SIDS',
    'islands' : 'Islands',
    'ldc' : 'LDC',
    'geom' : 'POLYGON',
}