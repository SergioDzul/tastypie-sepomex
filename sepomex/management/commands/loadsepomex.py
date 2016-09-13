#!/usr/bin/env python
# encoding=utf8
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
# made by zodman

import csv
import glob

from django.core.management import call_command
from django.core.management.base import BaseCommand

from sepomex.models import MXEstado, MXAsentamiento, MXMunicipio
from sepomex.settings import FIELDNAMES
import io

class Command(BaseCommand):
    help = 'Load sepomex database into sepomex models'

    def handle(self, *args, **options):
        if MXEstado.objects.count() == 0:
            call_command('loadmxstates')

        if MXMunicipio.objects.count() == 0:
            call_command('loadmxmunicipalities')

        if MXAsentamiento.objects.count() == 0:
            files = glob.glob('data/municipalities/*txt')

            for name in files:
                with open(name) as municipalities_file:
                    reader = csv.DictReader(municipalities_file,
                                            delimiter='|',
                                            fieldnames=FIELDNAMES)

                    municipality = reader.next()
                    [municipality.update({k:v.decode("latin-1")}) for k,v in municipality.items()]
                    print municipality
                    state = MXEstado.objects.get(id=municipality['c_estado'])
                    municipio = MXMunicipio.objects.get(
                        clave=municipality['c_mnpio'], mx_estado=state,
                        nombre=municipality['D_mnpio'])

                    MXAsentamiento.objects.create(
                            cp=municipality['d_codigo'],
                            nombre=municipality['d_asenta'],
                            tipo_asentamiento=municipality['d_tipo_asenta'],
                            zona=municipality['d_zona'], mx_municipio=municipio,
                        )
                    for item in reader:
                        [item.update({k:v.decode("latin-1")}) for k,v in item.items()]
                        MXAsentamiento.objects.create(
                            cp=item['d_codigo'], nombre=item['d_asenta'],
                            tipo_asentamiento=item['d_tipo_asenta'],
                            zona=item['d_zona'], mx_municipio=municipio
                        ) 
                        
                    print "{} Asentamientos creados".format(MXAsentamiento.object.all().count())
