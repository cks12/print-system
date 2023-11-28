import os
import win32print
import win32api


def printer(name: str):
    sep_tup = os.path.splitext(file)
    ext = sep_tup[1]
    file = sep_tup[0]
    default_printer_name = win32print.GetDefaultPrinter()
    hPrinter = win32print.OpenPrinter(default_printer_name)
    if ext == "zpl":
        zplFile = open(name, "r")
        raw_data = bytes(zplFile, 'utf-8')
        try:
            win32print.StartDocPrinter(
                hPrinter, 1, ("IMPRESSÃO WYNCONNECT", None, "RAW"))
            try:
                win32print.StartPagePrinter(hPrinter)
                win32print.WritePrinter(hPrinter, raw_data)
                win32print.EndPagePrinter(hPrinter)
            finally:
                win32print.EndDocPrinter(hPrinter)
        finally:
            win32print.ClosePrinter(hPrinter)
    if ext == "epl":
        zplFile = open(name, "r")
        raw_data = bytes(zplFile, 'utf-8')
        try:
            win32print.StartDocPrinter(
                hPrinter, 1, ("IMPRESSÃO WYNCONNECT", None, "RAW"))
            try:
                win32print.StartPagePrinter(hPrinter)
                win32print.WritePrinter(hPrinter, raw_data)
                win32print.EndPagePrinter(hPrinter)
            finally:
                win32print.EndDocPrinter(hPrinter)
        finally:
            win32print.ClosePrinter(hPrinter)
    if ext == "pdf":
        win32api.ShellExecute(0, "print", name, '/d:"%s"' %
                              default_printer_name, ".", 0)
