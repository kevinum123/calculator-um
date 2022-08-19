from flask import Flask, jsonify, request, Response


app = Flask(__name__)


@app.route('/operacion', methods=['GET'])
def operacion():


    inputData = request.json
    jsonResult = {}

    if 'numero_uno' in inputData and 'numero_dos' in inputData and 'tipo_operacion' in inputData:

        try:

            if inputData['tipo_operacion'] == 'suma':

                result = int(inputData['numero_uno']) + int(inputData['numero_dos'])
            
            elif inputData['tipo_operacion'] == 'resta':

                result = int(inputData['numero_uno']) - int(inputData['numero_dos'])

            elif inputData['tipo_operacion'] == 'multiplicacion':

                result = int(inputData['numero_uno']) * int(inputData['numero_dos'])

            elif inputData['tipo_operacion'] == 'division':

                result = int(inputData['numero_uno']) / int(inputData['numero_dos'])

            jsonResult['resultado'] = result
            jsonResult['tipo_operacion'] = f"Se ha realizado una {inputData['tipo_operacion']} exitosamente"


            return jsonResult, 200

        except ZeroDivisionError as ex:

            return jsonify({'status' : 'Error', 'Description' : str(ex)}), 400

        

    else:

        return jsonify({'status' : 'Error', 'Description' : 'No se enviaron los datos solicitados'}), 400


if __name__ == '__main__':

    app.run(debug=False)