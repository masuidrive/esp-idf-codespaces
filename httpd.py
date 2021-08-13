#!/usr/bin/python
import http.server
import socketserver
from io import BytesIO
import zipfile
import json
from os.path import basename

buildpath = 'build/'

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            body = b'Hello World2'
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.send_header('Content-length', len(body))
            self.end_headers()
            self.wfile.write(body)
        
        if self.path == "/esp32.zip":
            fflasher_args = open('build/flasher_args.json','r')
            flasher_args = json.load(fflasher_args)

            filelist = []
            for addr, filename in flasher_args['flash_files'].items():
                filelist.append(f"{addr}\t{basename(filename)}")

            mem_zip = BytesIO()
            with zipfile.ZipFile(mem_zip, mode="w",compression=zipfile.ZIP_DEFLATED) as zf:
                for addr, filename in flasher_args['flash_files'].items():
                    zf.write(buildpath+filename, basename(filename))
                zf.writestr('files.tsv', "\n".join(filelist))

            body = mem_zip.getvalue()

            self.send_response(200)
            self.send_header('Content-type', 'application/octet-stream')
            self.send_header('Content-length', len(body))
            self.send_header('Content-Disposition', 'attachment; filename="esp32.zip"')
            self.end_headers()
            self.wfile.write(body)



httpd = socketserver.TCPServer(('', 8000), Handler)
httpd.serve_forever()
