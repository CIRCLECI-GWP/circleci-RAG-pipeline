# Custom libs
import chains

# Other libs
from   flask import Flask, jsonify, make_response, request
import sys



# Initialize the application chain
#chain = chains.assistant_chain("Bob").getChain()
chain = chains.documentation_chain("https://docs.smith.langchain.com").getChain()


app = Flask(__name__)


# Handle HTTP POST request
@app.route("/", methods = ['POST'])
def chat():
    if not request.is_json:
        return make_response(
            jsonify(
                {"success": False,
                 "error": "Unexpected error, request is not in JSON format"}),
            400)
    
    try:
        data       = request.json
        user_input = data["message"]
        result     = chain.invoke({"question": user_input})
        
        return jsonify({"success": True, "data": result})
    except:
        return make_response(
            jsonify(
                {"success": False, 
                 "error": "Unexpected error: failed to send the message"}),
            400)
