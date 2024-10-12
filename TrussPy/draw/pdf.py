import time
import pdfkit
from ..data_types import Visualization_Data

def generate_pdf(data: Visualization_Data, img1: str, img2: str):
    path_to_wkhtmltopdf = r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
    config = pdfkit.configuration(wkhtmltopdf=path_to_wkhtmltopdf)

    html_content1 = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            @page {
                size: A4;
                margin: 20mm;
            }
            body {
                font-family: Arial, sans-serif;
            }
            .page {
                page-break-after: always;
            }
            .content {
                height: 100%;
                box-sizing: border-box;
            }
        </style>
        <title>A4 Size PDF Example</title>
    </head>
    <body>
        <div class="content">
            <h1>桁架计算结果报告</h1>
            <p>
    '''
    html_content2 = '''
            < / p >
        < / div >
        < div class = "page" > </ >
        < div class = "content" >
            < img src = "
    '''
    html_content3 = '''
    " alt = "1" >
            < img src = "
    '''
    html_content4 = '''
            " alt = "1" >
    '''
    html_content5 = '''
        < / div >
    < / body >
    < / html >
    '''
    html = html_content1 + '124' + html_content2 + img1 + html_content3 + img2 + html_content4 + html_content5

    pdfkit.from_string(html, './output_a4.pdf', configuration=config)
