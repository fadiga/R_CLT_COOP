#!/usr/bin/env python
# -*- coding= UTF-8 -*-
# Fad

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

from models import Immatriculation
from Common.ui.util import get_temp_filename


def pdFview(filename, dmd):
    """
        cette views est cree pour la generation du PDF
    """

    if not filename:
        filename = get_temp_filename('pdf')

    # Static source pdf to be overlayed
    PDFSOURCE = 'tools/immat_source.pdf'
    TMP_FILE = 'tools/tmp.pdf'
    # DATE_FORMAT = u"%d/%m/%Y"

    DEFAULT_FONT_SIZE = 11
    FONT = 'Courier'
    # A simple function to return a leading 0 on any single digit int.

    def double_zero(value):
        try:
            return '%02d' % value
        except TypeError:
            return value

    # setup the empty canvas
    from io import FileIO as file
    # from Common.pyPdf import PdfFileWriter, PdfFileReader
    from PyPDF2 import PdfFileWriter, PdfFileReader

    # PDF en entrée
    input1 = PdfFileReader(file(PDFSOURCE, "rb"))

    # PDF en sortie
    output = PdfFileWriter()
    # Récupération du nombre de pages
    n_pages = input1.getNumPages()
    # Pour chaque page
    immat = Immatriculation.select().where(Immatriculation.scoop == dmd.scoop).get()
    for i in range(n_pages):
        # Récupération de la page du doc initial (input1)
        page = input1.getPage(i)
        y = 630
        x = 70
        p = canvas.Canvas(TMP_FILE, pagesize=A4)
        p.setFont(FONT, DEFAULT_FONT_SIZE)
        p.drawString(x + 70, y + 73, str(dmd.scoop.display_region()))
        p.drawString(x + 70, y + 37, str(dmd.scoop.display_cercle()))

        denom1, denom2 = controle_caratere(dmd.scoop.denomination, 60, 65)
        p.drawString(x, y - 90, denom1)
        p.drawString(x, y - 120, denom2)

        p.drawString(x + 120, y - 154, str(dmd.id))
        p.drawString(x + 300, y - 154, str(
            dmd.start_date.strftime("%d / %B / %Y")))
        p.drawString(x + 70, y - 190, str(immat.name_declarant))
        p.drawString(x + 65, y - 224, str(immat.display_quality()))
        p.drawString(x + 176, y - 262, str(immat.procuration))
        p.drawString(x + 120, y - 298, str(dmd.scoop.display_commune()))
        p.drawString(x + 355, y - 298, str(dmd.scoop.display_vfq()))
        p.drawString(x + 90, y - 334, str(dmd.scoop.rue))
        p.drawString(x + 317, y - 334, str(dmd.scoop.porte))
        p.drawString(x + 67, y - 369, str(dmd.scoop.tel))
        p.drawString(x + 227, y - 369, str(dmd.scoop.bp))
        p.drawString(x + 350, y - 369, str(dmd.scoop.email))
        p.drawString(x + 100, y - 400, str(dmd.scoop.immatricule))
        p.drawString(
            x + 60, y - 470, str(dmd.scoop.display_cercle()))
        p.drawString(
            x + 370, y - 470, str(immat.date.strftime("%d/%m/%Y")))
        p.showPage()
        # Sauvegarde de la page
        p.save()
        # Création du watermark
        watermark = PdfFileReader(file(TMP_FILE, "rb"))
        # Création page_initiale+watermark
        page.mergePage(watermark.getPage(0))
        # Création de la nouvelle page
        output.addPage(page)
    # Nouveau pdf
    file_dest = filename + ".pdf"
    outputStream = file(file_dest, u"wb")
    output.write(outputStream)
    outputStream.close()

    return file_dest


def controle_caratere(lettre, nb_controle, nb_limite):
    """
        cette fonction decoupe une chaine de caratere en fonction
        du nombre de caratere donnée et conduit le reste à la ligne
    """
    lettre = lettre
    if len(lettre) <= nb_controle:
        ch = lettre
        ch2 = u""
        return ch, ch2
    else:
        ch = ch2 = u""
        for n in lettre.split(u" "):
            if len(ch) <= nb_limite:
                ch = ch + u" " + n
            else:
                ch2 = ch2 + u" " + n
        return ch, ch2
