import hashlib
import zipfile
from io import BytesIO

import requests
from flask import Flask, request, render_template

HITBOX_WORDS = [
    'AxisAlignedBB', 'func_174826_a', 'func_226277_ct_', 'func_174813_aQ().field_72338_b',  # FORGE
    'func_226281_cx_func_226277_ct_', 'func_174813_aQ().field_72337_e', 'func_226281_cx_',  # FABRIC
    'method_5829', 'class_238', 'method_23317', 'method_23321', 'method_5857',
    'dci', '.cD()', '.cc().b', '.cH()', '.cc().e'  # LABYMOD
]

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main_page():
    result_data = {'visible': False, 'result': {}}

    if request.method == 'POST':
        result_data['visible'] = True
        files = [file for file in request.files.getlist('file') if file.filename.endswith('.jar')]
        for file in files:
            result_data['result'].update({file.filename: f'Pre-cleaned! No suspicious functions found!'})
            file_hash = hashlib.sha1(b''.join(x for x in file.stream)).hexdigest()

            response = requests.get(url=f"https://api.modrinth.com/v2/version_file/{file_hash}")
            if response.status_code == 200:
                result_data['result'].update({file.filename: 'Clean! Found on modrinth.com'})
                continue

            file.seek(0)  # Return the pointer to the beginning of the file
            with zipfile.ZipFile(BytesIO(file.read()), 'r') as jar:
                file_list = [file for file in jar.namelist() if file.endswith('.class')]
                for file_name in file_list:
                    with jar.open(file_name) as file_class:
                        class_data = file_class.read()
                        for x in HITBOX_WORDS:
                            if x.encode() in class_data:
                                result_data['result'].update({file.filename: f'Suspicious! An {x} function has been found.'})
                                continue

    return render_template(template_name_or_list='index.html', data=result_data)


if __name__ == '__main__':
    app.run(debug=False)
