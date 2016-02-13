# -*- coding: utf-8 -*-
import os
import pandas as pd
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Towers.settings')

import django
django.setup()

from django.contrib.gis.utils import LayerMapping
from django.db import IntegrityError, transaction

from visualization.models import (
    OpenCellId,
    GADM,
    GADM1,
    GADM2,
    gadm_mapping,
    gadm1_mapping,
    gadm2_mapping
)


mcc_good = [
    602,  # Egypt
]


def populate_OpenCellId(
    csv_file=os.path.join(
        os.path.abspath('.'),
        'data',
        'cell_towers.csv'
    ),
    mcc_list=mcc_good
):
    """Populate OpenCellId model.
    Parameters
    ----------
    csv_file : str
    mcc_list : list
    """

    print 'Populating OpenCellId ..'
    try:
        csv_data = pd.read_csv(csv_file)
    except Exception as e:
        print 'Error reading OpenCellId data'
        print e.message
        return

    good_data = csv_data[csv_data['mcc'].isin(mcc_list)]
    good_data['averageSignal'].fillna(0, inplace=True)
    good_data.dropna(
        subset=good_data.columns.drop('unit'),
        inplace=True
    )
    good_data.reset_index(
        inplace=True,
        drop=True
    )

    # bulk_open_cell_ids = []
    for idx, row in good_data.iterrows():
        line = row.to_dict()
        if str(line['unit']) == 'nan':
            line['unit'] = None
        try:
            ocid = OpenCellId(**line)
            ocid.save()
        except Exception as e:
            print e
            print 'in line:', idx
            pass
        
    # OpenCellId.objects.bulk_create(bulk_open_cell_ids)

    print 'Done!'


def populate_GADM(
    model,
    shp_file,
    mapping_dict,
    verbose=False
):
    """
    Populates a model of GADM family
    Parameters
    ----------
    model : <model>
    shp_file : str
    mapping_dict : dict
    verbose : bool
    """
    try:
        lm = LayerMapping(
            model,
            shp_file,
            mapping_dict,
            transform=False,
        )
        with transaction.atomic():
            lm.save(verbose=verbose)
    except IntegrityError as ie:
        print "Integrity error:", ie.message
    except Exception as e:
        print 'Error loading GADM data!'
        print e.message


def load():
    populate_OpenCellId()
    populate_GADM(
        GADM,
        './data/SWE_adm0.shp',
        gadm_mapping
    )
    populate_GADM(
        GADM1,
        './data/SWE_adm1.shp',
        gadm1_mapping
    )
    populate_GADM(
        GADM2,
        './data/SWE_adm2.shp',
        gadm2_mapping
    )


if __name__ == '__main__':
    load()