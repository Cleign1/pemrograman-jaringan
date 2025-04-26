from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
    <h1>Hello, World!</h1>
    <p>Selamat datang di aplikasi Flask Saya. </p>
    '''

# @app.route('/datadiri')
# def data_diri():
#     return '''
#     <h1>Nama Saya, Muhamad Ibnu Khaidar Hafiz</h1>
#     <h2>NPM Saya 50421867</h2>
#     <p>Saya kelas 4IA15</p>
#     <table border="1">
#         <tr>
#             <th>Nama</th>
#             <th>NPM</th>
#             <th>Kelas</th>
#         </tr>
#         <tr>
#             <td>Muhamad Ibnu Khaidar Hafiz</td>
#             <td>50421867</td>
#             <td>4IA15</td>
#         </tr>
#     </table>
#     '''

## LA Pemrograman Jaringan
@app.route('/datadiri')
def data_diri():
    return '''
    <h1>Hello!</h1>
    <p> salam kenal. ini data diri saya </p>
    <table border="1">
        <tr>
            <th>Nama</th>
            <td>Muhamad Ibnu Khaidar Hafiz</td>
        </tr>
        <tr>
            <th>NPM</th>
            <td>50421867</td>
        </tr>
        <tr>
            <th>Kelas</th>
            <td>4IA15</td>
        </tr>
    </table>

    '''

if __name__ == '__main__':
    app.run(debug=True, port=5000)