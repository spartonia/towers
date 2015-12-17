import os
import csv
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Towers.settings')

import django
django.setup()

from visualization.models import OpenCellId


mcc_good = [
    602,  # Egypt
]


def popuplate_OpenCellId(
    csv_file='cell_towers.csv',
    mcc_list=mcc_good
):
    """Populate OpenCellId model.
    Parameters
    ----------
    csv_file : str
    mcc_list : list
    """

    print 'Populating OpenCellId ..'
    with open(csv_file) as f:
        csv_dict = csv.DictReader(f)
        bulk_open_cell_ids = []
        for line in csv_dict:
            if int(line['mcc']) in mcc_list:
                if not line['unit']:
                    line['unit'] = None
                try:
                    ocid = OpenCellId(**line)
                    # bulk_open_cell_ids.append(ocid)
                    ocid.save()
                except Exception as e:
                    print e
                    print 'At line:', csv_dict.line_num
                    pass

    # OpenCellId.objects.bulk_create(bulk_open_cell_ids)
    print 'Done!'
if __name__ == '__main__':
    popuplate_OpenCellId()
