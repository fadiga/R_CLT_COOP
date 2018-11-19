#!/usr/bin/env python
# -*- coding= UTF-8 -*-
# Fad

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

from models import Immatriculation
# from Common.cel import cel
from configuration import Config
from Common.ui.util import get_temp_filename


def pdFview(filename, dmd):
    """
        cette views est cree pour la generation du PDF
    """

    if not filename:
        filename = get_temp_filename('pdf')
        # print(filename)
    # on recupere les items de la facture

    # Static source pdf to be overlayed
    PDFSOURCE = 'tools/immat_source.pdf'
    TMP_FILE = 'tmp.pdf'
    DATE_FORMAT = u"%d/%m/%Y"

    DEFAULT_FONT_SIZE = 11
    FONT = 'Courier-Bold'
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
        # p.setFont(FONT, DEFAULT_FONT_SIZE)

        denomination1, denomination2 = controle_caratere(
            dmd.scoop.denomination, 60, 65)
        p.drawString(x, y - 90, denomination1)
        p.drawString(x, y - 120, denomination2)
        p.drawString(x, y - 154, str(dmd.id).rjust(36, ' '))
        p.drawString(
            x, y - 154, str(dmd.start_date.strftime("%d / %B / %Y")).rjust(115, ' '))
        p.drawString(x, y - 190, str(immat.name_declarant).rjust(23, ' '))
        p.drawString(x, y - 224, str(immat.quality).rjust(36, ' '))
        p.drawString(x, y - 262, str(immat.procuration).rjust(57, ' '))
        p.drawString(x, y - 298, str(dmd.scoop.commune).rjust(40))
        p.drawString(x, y - 298, str(dmd.scoop.vfq).rjust(106, ' '))
        p.drawString(x, y - 334, str(dmd.scoop.rue).rjust(30, ' '))
        p.drawString(x, y - 334, str(dmd.scoop.porte).rjust(97, ' '))
        p.drawString(x, y - 369, str(dmd.scoop.tel).rjust(20, ' '))
        p.drawString(x, y - 369, str(dmd.scoop.bp).rjust(70, ' '))
        p.drawString(x, y - 369, str(dmd.scoop.email).rjust(110, ' '))
        p.drawString(x, y - 400, str(dmd.scoop.immatricule).rjust(50, ' '))
        p.drawString(
            x, y - 470, str(dmd.scoop.cercle).rjust(10, ' '))
        p.drawString(
            x, y - 470, str(immat.date.strftime("%d/%m/%Y")).rjust(113, ' '))
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
