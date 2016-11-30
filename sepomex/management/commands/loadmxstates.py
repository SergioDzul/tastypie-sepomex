# -*- coding: utf-8 -*-

from __future__ import print_function

import csv

from django.core.management.base import BaseCommand, CommandError
from sepomex.models import MXEstado


class Command(BaseCommand):
    help = 'Load states objects from csv file'

    def handle(self, *args, **options):
        MXEstado.objects.all().delete()
        with open('data/sepomex_mx_states.txt', encoding='latin-1') as mxstates_file:
            reader = csv.DictReader(mxstates_file,
                                    delimiter='|',
                                    fieldnames=['id', 'name', 'abbr'])
            mxstates = [
                MXEstado(id=state['id'], abbr=state['abbr'], nombre=state['name'])
                for state in reader
            ]
            MXEstado.objects.bulk_create(mxstates)
        print(u'{} Estados creados!'.format(len(mxstates)))
